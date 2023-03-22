from pathlib import Path;
import pandas as pd;
import sys;
sys.path.append(str(Path(__file__).resolve().parent.parent))
import pandas as pd;
import folium;

df = pd.read_csv("sample/tenpo.csv");

print(len(df));
print(df.columns.values);
print("-----");

store = df[["緯度","経度","店舗名(日本語)"]].values;
print(len(store));
print(store);
print("-----");

m = folium.Map(location=[35.942957, 136.198863], zoom_start=16);
for data in store:
    folium.Marker([data[0],data[1]], tooltip=data[2]).add_to(m);
m.save("chap4/tmp/store.html");
