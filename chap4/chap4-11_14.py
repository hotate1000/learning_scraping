from pathlib import Path;
import pandas as pd;
import sys;
sys.path.append(str(Path(__file__).resolve().parent.parent))
import pandas as pd;
import matplotlib.pyplot as plt;

df1 = pd.read_csv("sample/heikin_kion.csv", index_col="時点");
df2 = pd.read_csv("sample/saikou_kion.csv", index_col="時点");
df3 = pd.read_csv("sample/saitei_kion.csv", index_col="時点");

print(df1.columns.values);
print(df2.columns.values);
print(df3.columns.values);
print("-----");

df1["東京都"].plot();
df2["東京都"].plot();
df3["東京都"].plot();
plt.ylim(-10,40);
plt.legend(loc="lower right");
plt.show();
