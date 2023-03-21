from pathlib import Path;
import pandas as pd
import sys;

sys.path.append(str(Path(__file__).resolve().parent.parent));
df = pd.read_csv("sample/test.csv");
print(df);
print("--------");

print("データの件数=", len(df));
print("項目名=", df.columns.values);
print("インデックス=", df.index.values);
print("--------");

print("国語列データ\n", df["国語"]);
print("国語と数学の列データ\n",df[["国語","数学"]]);
print("--------");

print("Aのデータ\n", df.loc[0]);
print("AとCのデータ\n", df.loc[[0,2]]);
print("Aの数学うのデータ\n", df.loc[0]["数学"]);