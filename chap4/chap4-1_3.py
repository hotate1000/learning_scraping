from pathlib import Path;
import sys;
sys.path.append(str(Path(__file__).resolve().parent.parent))

import pandas as pd;

df = pd.read_csv("sample/13tokyo/13TOKYO.CSV", header=None, encoding="shift_jis", dtype=str);
print(len(df));
print(df.columns.values);
print("-----");

results = df[df[2] == "1600006"];
print(results[[2,6,7,8]]);
print("-----");

results = df[df[8] == "四谷"];
print(results[[2,6,7,8]]);

results = df[df[8].str.contains("四谷")];
print(results[[2,6,7,8]]);
print('-----');
