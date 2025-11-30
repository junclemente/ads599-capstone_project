from pathlib import Path

def get_paths():
    """
    Robust paths for local + deployed Streamlit.
    Anchors to /app even when called from /app/utils.
    """
    try:
        # paths.py -> app/utils/paths.py
        # parent = utils, parent of that = app
        APP_DIR = Path(__file__).resolve().parents[1]
    except NameError:
        # Notebook / interactive fallback
        APP_DIR = Path.cwd() if Path.cwd().name == "app" else Path.cwd() / "app"

    ROOT_DIR = APP_DIR.parent

    ASSETS_DIR = APP_DIR / "assets"
    MODELS_DIR = ROOT_DIR / "models"
    DATA_DIR   = ROOT_DIR / "data"

    return {
        "APP_DIR": APP_DIR,
        "ROOT_DIR": ROOT_DIR,
        "ASSETS_DIR": ASSETS_DIR,
        "MODELS_DIR": MODELS_DIR,
        "DATA_DIR": DATA_DIR,
    }