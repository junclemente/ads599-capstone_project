import pandas as pd 



def load_cde_txt(path, sep="\t", encoding="latin1"):
    return pd.read_csv(path, sep=sep, dtype=str, encoding=encoding)
