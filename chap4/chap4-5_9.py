from pathlib import Path;
import sys;
sys.path.append(str(Path(__file__).resolve().parent.parent))
import pandas as pd;
import matplotlib.pyplot as plt;

df = pd.read_csv("sample/zinkou.csv", index_col="全国・都道府県", encoding="shift_jis");
df = df.drop("全国", axis=0);
df["2015年"] = pd.to_numeric(df["2015年"].str.replace(",",""));
df=df.sort_values("2015年", ascending=False);
df["2015年"].plot.bar(figsize=(10,6));
plt.show();
print("-----");

df["2020年"] = pd.to_numeric(df["2020年"].str.replace(",",""));
df["人口増減"] = df["2020年"] - df["2015年"];
df = df.sort_values("人口増減", ascending=False);
df["人口増減"].plot.bar(figsize=(10,6));
plt.show()
