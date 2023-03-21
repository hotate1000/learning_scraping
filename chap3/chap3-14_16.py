from pathlib import Path;
import sys;
sys.path.append(str(Path(__file__).resolve().parent.parent));
import pandas as pd;
import matplotlib.pyplot as plt;

df = pd.read_csv("sample/test.csv", index_col=0);

df.plot.bar();
plt.legend(loc="lower right");
plt.show();

df.plot.barh();
plt.legend(loc="lower left");
plt.show();

df.plot.bar(stacked=True);
plt.legend(loc="lower right");
plt.show();

df.plot.box();
plt.show();

df.plot.area();
plt.legend(loc="lower right");
plt.show();
# print("---------");

df["数学"].plot.barh();
plt.legend(loc="lower left");
plt.show();

df[["国語", "数学"]].plot.barh();
plt.legend(loc="lower left");
plt.show();

df.loc["A太"].plot.barh();
plt.legend(loc="lower left");
plt.show();

df.loc["A太"].plot.pie(labeldistance=0.6);
plt.legend(loc="lower left");
plt.show();
