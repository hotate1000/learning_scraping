from pathlib import Path;
import pandas as pd;
import sys;
sys.path.append(str(Path(__file__).resolve().parent.parent))
import pandas as pd;
import folium;

out_folder = Path("chap4/tmp");
out_folder.mkdir(exist_ok=True);

df = pd.read_csv("sample/syoukasen.csv", encoding="shift-jis");

print(len(df));
print(df.columns.values);
print("-----");

hydrant = df[["経度","緯度"]].values;
print(len(hydrant));
print(hydrant);
print("-----");

m = folium.Map(location=[35.942957, 136.198863], zoom_start=16);
folium.Marker([35.942957, 136.198863]).add_to(m);
m.save("chap4/tmp/sabae.html");