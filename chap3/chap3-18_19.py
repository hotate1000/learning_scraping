from pathlib import Path;
import sys;
sys.path.append(str(Path(__file__).resolve().parent.parent));
import pandas as pd;
import matplotlib.pyplot as plt;

df = pd.read_csv("sample/test.csv", index_col=0);

color_list = ["skyblue", "steelblue", "tomato", "cadetblue", "orange", "sienna"];
df.T.plot.bar(color=color_list);
plt.legend(loc="lower right");
plt.show();
plt.savefig("chap3/tmp/graph.png")