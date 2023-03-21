from pathlib import Path;
import pandas as pd;
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
print("--------");

df["美術"] = [68, 73, 82, 77, 94, 96, 55];
print("列データ（美術）を追加\n", df);
df.loc[7] = ["H田", 88, 65, 34, 66, 49, 77];
print("行データ（H田）を追加\n", df);
print("--------");

print("「名前」の列を削除\n", df.drop("名前", axis=1));
print("インデックス2の行を削除\n", df.drop(2, axis=0));
print("--------");

data_n = df[df["国語"] >= 90];
print("国語が90点以上\n", data_n);
data_m = df[df["数学"] <= 70];
print("数学が70点以下\n", data_m);
print("--------");

print("国語の最高点=", df["国語"].max());
print("国語の最低点=", df["国語"].min());
print("国語の平均点=", df["国語"].mean());
print("国語の中央値=", df["国語"].median());
print("国語の合計=", df["国語"].sum());
print("--------");

national_lang = df.sort_values("国語", ascending=False);
print("国語の点数が高いもの順でソート\n", national_lang);
print("--------");

print("通常\n", df);
print("行列変更\n", df.T);
print("Pythonのリスト化\n", df.values);
print("Pythonのリスト化、行列変更\n", df.T.values);
print("--------");


