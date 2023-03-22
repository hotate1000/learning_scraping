from pathlib import Path;
import sys;
sys.path.append(str(Path(__file__).resolve().parent.parent))
import pandas as pd;

df = pd.read_csv("sample/zinkou.csv", index_col="全国・都道府県", encoding="shift_jis");
print(len(df));
print(df.columns.values);