import re

import numpy as np
import pandas as pd
from pathlib import Path

def load_cde_txt(path, sep="\t", encoding="latin1"):
    return pd.read_csv(path, sep=sep, dtype=str, encoding=encoding)


def clean_calschls_safety(
    df_raw: pd.DataFrame, years: str = "2017-2019", level_filter: str = "All"
) -> pd.DataFrame:
    """
    Clean a raw CalSCHLS 'Perceptions of School Safety' DataFrame into a tidy format.

    Parameters
    ----------
    df_raw : pandas.DataFrame
        Raw DataFrame as imported from Excel/text — containing county header rows,
        'Grade Level', and percentage columns in string form.
    years : str, optional
        The CalSCHLS year range (default '2017-2019').
    level_filter : str, optional
        Filter label for Level of Safety (default 'All').

    Returns
    -------
    pandas.DataFrame
        Cleaned DataFrame with columns:
        ['geography','geo_type','grade','very_safe_pct','safe_pct',
         'neither_pct','unsafe_pct','very_unsafe_pct','years','level_of_safety_filter']

    Notes
    -----
    - Detects rows that contain county/state names ending in 'Percent'.
    - Parses Grade 9/11 rows into numeric columns.
    - Converts '%' strings to floats and sets 'S'/'N/A' to NaN.
    """

    def _clean_val(x):
        if pd.isna(x):
            return np.nan
        x = str(x).strip().replace("%", "")
        if x in {"N/A", "S", ""}:
            return np.nan
        try:
            return float(x)
        except ValueError:
            return np.nan

    rows = []
    region = None

    # Loop through all rows
    for _, row in df_raw.iterrows():
        # Flatten and join all values to handle irregular formats
        values = [str(v).strip() for v in row if pd.notna(v)]
        if not values:
            continue

        line = "\t".join(values)

        # Detect new region headers (e.g., 'Alameda County Percent')
        if line.endswith("Percent") and not line.startswith("Grade Level"):
            region = line.replace("Percent", "").strip()
            continue

        # Detect data lines ('Grade 9', 'Grade 11')
        if line.startswith("Grade 9") or line.startswith("Grade 11"):
            match = re.match(r"Grade\s+(9|11)\s+(.*)", line)
            if not match or region is None:
                continue

            grade = int(match.group(1))
            rest = match.group(2)
            parts = re.split(r"\t+|\s{2,}", rest)
            if len(parts) < 5:
                parts = rest.split()
            vals = (parts + [""] * 5)[:5]

            vs, s, n, u, vu = map(_clean_val, vals)
            rows.append(
                {
                    "geography": region,
                    "geo_type": "County" if "County" in region else "State",
                    "grade": grade,
                    "very_safe_pct": vs,
                    "safe_pct": s,
                    "neither_pct": n,
                    "unsafe_pct": u,
                    "very_unsafe_pct": vu,
                    "years": years,
                    "level_of_safety_filter": level_filter,
                }
            )

    df_clean = pd.DataFrame(rows)

    # Sort for readability
    if not df_clean.empty:
        df_clean["geo_type"] = pd.Categorical(
            df_clean["geo_type"], categories=["State", "County"], ordered=True
        )
        df_clean = df_clean.sort_values(["geo_type", "geography", "grade"]).reset_index(
            drop=True
        )

    return df_clean


def clean_safety_by_connectedness(df_raw: pd.DataFrame) -> pd.DataFrame:
    """
    Clean the 'Perceptions of School Safety, by Level of School Connectedness' dataset
    (KidsData/CalSCHLS Excel export) into a tidy dataframe.

    Parameters
    ----------
    df_raw : pd.DataFrame
        Raw dataframe read directly from Excel using pd.read_excel().

    Returns
    -------
    pd.DataFrame
        Tidy dataframe with columns:
        ['Geography', 'Connectedness', 'Very Safe', 'Safe',
         'Neither Safe nor Unsafe', 'Unsafe', 'Very Unsafe', 'Safety_Positive']
    """
    # 1️⃣ Drop all-empty rows/columns
    df = df_raw.dropna(how="all").dropna(axis=1, how="all").copy()

    # 2️⃣ Reset index for easier iteration
    df.reset_index(drop=True, inplace=True)

    # 3️⃣ Find rows that contain region names (header rows)
    region_rows = []
    for i in range(len(df)):
        row_str = str(df.iloc[i, 0]).strip()
        if "County" in row_str or row_str == "California":
            region_rows.append(i)

    # 4️⃣ Extract all regions and their associated 3 rows (High, Medium, Low)
    records = []
    for idx in region_rows:
        region = str(df.iloc[idx, 0]).strip()
        # Usually, after this line: header row + 3 data rows
        sub_df = df.iloc[
            idx + 2 : idx + 5
        ].copy()  # skip header line ("Level of School Connectedness ...")
        sub_df.columns = df.iloc[
            idx + 1
        ].tolist()  # use the "Level of School Connectedness" header row
        sub_df["Geography"] = region
        records.append(sub_df)

    # 5️⃣ Combine
    df_clean = pd.concat(records, ignore_index=True)

    # 6️⃣ Remove any 'Percent' columns or artifacts
    if "Percent" in df_clean.columns:
        df_clean.drop(columns=["Percent"], inplace=True, errors="ignore")

    # 7️⃣ Convert percentages (e.g. '27.4%') → float
    for col in [
        "Very Safe",
        "Safe",
        "Neither Safe nor Unsafe",
        "Unsafe",
        "Very Unsafe",
    ]:
        df_clean[col] = (
            df_clean[col]
            .astype(str)
            .str.replace("%", "", regex=False)
            .replace({"S": np.nan, "N/A": np.nan, "nan": np.nan})
            .astype(float)
        )

    # 8️⃣ Add derived "Safety_Positive" (% who feel safe or very safe)
    df_clean["Safety_Positive"] = df_clean["Very Safe"] + df_clean["Safe"]

    # 9️⃣ Reorder columns
    df_clean = df_clean[
        [
            "Geography",
            "Level of School Connectedness",
            "Very Safe",
            "Safe",
            "Neither Safe nor Unsafe",
            "Unsafe",
            "Very Unsafe",
            "Safety_Positive",
        ]
    ].rename(columns={"Level of School Connectedness": "Connectedness"})

    # 10️⃣ Optional: make Connectedness categorical
    df_clean["Connectedness"] = pd.Categorical(
        df_clean["Connectedness"], categories=["High", "Medium", "Low"], ordered=True
    )

    return df_clean


def clean_columns(df):
    """
    Clean column names by removing newlines, excessive spaces,
    and standardizing capitalization.
    """
    df = df.copy()
    df.columns = (
        df.columns.str.replace("\n", " ", regex=False)  # remove newline characters
        .str.replace(r"\s+", " ", regex=True)  # collapse multiple spaces
        .str.strip()  # trim leading/trailing spaces
    )
    return df

def rpkl(folder_path, filename, show_cols=True):
    """
    Read, clean, and standardize a pickle file into a pandas DataFrame.

    - Converts column names to lowercase, underscores, and removes spaces.
    - Automatically builds a 'cdscode' column if not present and if possible.
    - Optionally prints the cleaned column list.

    Parameters
    ----------
    folder_path : Path or str
        Folder containing the pickle file.
    filename : str
        Name of the pickle file.
    show_cols : bool, default=True
        Whether to print the cleaned column list.

    Returns
    -------
    pd.DataFrame
        Cleaned DataFrame with standardized column names and optional 'cdscode'.
    """

    # --- Load pickle ---
    df = pd.read_pickle(folder_path / filename)

    # --- Clean column names ---
    df.columns = (
        df.columns
        .str.strip()
        .str.lower()
        .str.replace(r"\s+", "_", regex=True)
        .str.replace(r"[^\w_]", "", regex=True)
    )

    # --- Check if 'cdscode' already exists ---
    if "cdscode" not in df.columns:
        def find_col(options):
            for c in options:
                if c in df.columns:
                    return c
            return None

        county_col = find_col(["county_code", "countycode"])
        district_col = find_col(["district_code", "districtcode"])
        school_col = find_col(["school_code", "schoolcode"])

        if all([county_col, district_col, school_col]):
            df["cdscode"] = (
                df[county_col].astype(str).str.zfill(2)
                + df[district_col].astype(str).str.zfill(5)
                + df[school_col].astype(str).str.zfill(7)
            )
            print(f"✅ Added 'cdscode' using: {county_col}, {district_col}, {school_col}")
        else:
            missing = [
                name
                for name, col in zip(
                    ["county", "district", "school"],
                    [county_col, district_col, school_col],
                )
                if col is None
            ]
            print(f"⚠️ Could not build 'cdscode' (missing {', '.join(missing)})")
    else:
        print("ℹ️ 'cdscode' already exists — skipping creation")

    # --- Optionally print columns ---
    if show_cols:
        print(f"\n📁 Columns in {filename}:")
        print(df.columns.tolist())

    return df

def create_county_fr_geography(df, column="geography"):
    df["county"] = (
        df[column]
        .str.replace(" County", "", regex=False)
        .str.strip()
    )

    return df 

def create_safety_connectedness_features(df):
    """
    Create composite School Safety and Connectedness metrics from CalSCHLS county data.
    Expects columns: county, connectedness_level, very_safe, safe, neither, unsafe, very_unsafe (in % values)
    Returns: DataFrame with county-level features ready to merge with your main dataset.
    """
    # make sure percentages are numeric
    pct_cols = ["very_safe", "safe", "neither", "unsafe", "very_unsafe"]
    df[pct_cols] = df[pct_cols].replace("%", "", regex=True).astype(float)

    # convert levels to numeric weights
    level_weight = {"High": 3, "Medium": 2, "Low": 1}
    df["level_weight"] = df["connectedness"].map(level_weight)

    # compute safety score within each row (1–5 scale)
    df["safety_score"] = (
        df["very_safe"] * 5
        + df["safe"] * 4
        + df["neither"] * 3
        + df["unsafe"] * 2
        + df["very_unsafe"] * 1
    ) / 100

    # now aggregate to county level
    agg = (
        df.groupby("county")
        .agg(
            avg_safety_score=("safety_score", "mean"),
            high_conn=("connectedness", lambda x: np.mean(x == "High")),
            low_conn=("connectedness", lambda x: np.mean(x == "Low")),
        )
        .reset_index()
    )

    # compute connectedness ratio and climate index
    agg["conn_ratio"] = agg["high_conn"] / (agg["low_conn"] + 1e-6)
    agg["school_climate_index"] = (agg["avg_safety_score"] * 0.5) + (
        agg["conn_ratio"] / agg["conn_ratio"].max() * 0.5
    )

    return agg


FIGURE_DIR = Path("../media/eda")

def export_fig(fig, filename, dpi=300):
    """
    Save matplotlib figure to a PNG file inside the media/eda folder. 

    Parameters
    ----------
    fig : matplotlib Figure
        Figure object to save.
    filename : str
        Base file name without the .png extension.
    dpi : int, optional
        Resolution of saved image (default=300).
    """
    out_path = FIGURE_DIR / f"{filename}.png"
    fig.savefig(out_path, dpi=dpi, bbox_inches="tight")
    print(f"[saved] {out_path}")


# dictionary to prettify feature names
pretty_names = {
    # ----- Targets / outcomes -----
    "regular_hs_diploma_graduates_rate": "Graduation Rate (%)",
    "graduation_rate": "Graduation Rate (%)",
    "dropout_rate": "Dropout Rate (%)",
    "still_enrolled_rate": "Still Enrolled After 4 Years (%)",
    "high_grad_rate": "High Graduation Category",
    "target_grad_category": "Graduation Outcome Category",

    # ----- Enrollment / cohort -----
    "cohortstudents": "Cohort Size (Students)",
    "eligible_cumulative_enrollment": "Cumulative Enrollment (Eligible Students)",
    "pct_senior_cohort": "Percent of Cohort in Grade 12",
    "pct_hs_enrollment": "Percent of Enrollment in High School Grades",

    # ----- Attendance / engagement (ABC: Attendance) -----
    "chronicabsenteeismrate": "Chronic Absenteeism Rate (%)",
    "unexcused_absences_percent": "Unexcused Absences (%)",
    "outofschool_suspension_absences_percent": "Suspension Absence Rate (%)",

    # ----- Socioeconomic (ABC context) -----
    "percent__eligible_free_k12": "Percent Eligible for Free Meals",
    "frpm_count_k12": "FRPM Student Count",

    # ----- Academic preparedness / course (ABC: Course) -----
    "met_uccsu_grad_reqs_rate": "UC/CSU A–G Completion Rate (%)",
    "seal_of_biliteracy_rate": "Seal of Biliteracy Rate (%)",
    "grade_retention_ratio": "Grade Retention Ratio",

    # ----- Staffing ratios / resources -----
    "stu_tch_ratio": "Student–Teacher Ratio",
    "stu_adm_ratio": "Student–Administrator Ratio",
    "stu_psv_ratio": "Student–Support Staff Ratio",

    # ----- Teacher education attainment -----
    "pct_associate": "Teachers with Associate Degree (%)",
    "pct_bachelors": "Teachers with Bachelor's Degree (%)",
    "pct_bachelors_plus": "Teachers with Bachelor's or Higher (%)",
    "pct_master": "Teachers with Master's Degree (%)",
    "pct_master_plus": "Teachers with Master's or Higher (%)",
    "pct_doctorate": "Teachers with Doctorate (%)",
    "pct_juris_doctor": "Teachers with Juris Doctor (JD) (%)",
    "pct_no_degree": "Teachers with No Degree Reported (%)",

    # ----- Teacher experience -----
    "pct_experienced": "Experienced Teachers (%)",
    "pct_inexperienced": "Inexperienced Teachers (%)",
    "pct_first_year": "First-Year Teachers (%)",
    "pct_second_year": "Second-Year Teachers (%)",

    # ----- Safety / climate -----
    "pct_unsafe_gr11": "Unsafe Perception (Grade 11) (%)",
    "pct_safe_gr11": "Safe Perception (Grade 11) (%)",
    "pct_neutral_gr11": "Neutral Safety Perception (Grade 11) (%)",
    "avg_safety_score": "Average Safety Score",
    "school_climate_index": "School Climate Index",

    # ----- ID / location (if you ever plot them, but usually you won't) -----
    "cdscode": "School CDS Code (ID)",
    "county": "County",
    "latitude": "Latitude",
    "longitude": "Longitude",

    # ----- School type flags -----
    "virtual": "Virtual School Status",
    "magnet": "Magnet School Status",
    "yearroundyn": "Year-Round School Status",
    "multilingual": "Multilingual Program Status",
}
