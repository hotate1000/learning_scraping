from pathlib import Path;
import pandas as pd;
import sys;
sys.path.append(str(Path(__file__).resolve().parent.parent))
import pandas as pd;
import matplotlib.pyplot as plt;
import folium;

df = pd.read_csv("sample/syoukasen.csv", encoding="shift-jis");

hydrant = df [["緯度","経度"]].values;

m = folium.Map(location=[35.942957, 136.198863], zoom_start=16);
for data in hydrant:
    print(data[0],data[1]);
    folium.Marker([data[0], data[1]]).add_to(m);
m.save('chap4/tmp/hydrant.html');
