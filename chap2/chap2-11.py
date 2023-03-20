import requests;
from pathlib import Path;
import sys;
sys.path.append(str(Path(__file__).resolve().parent.parent));
import sample.sample_data as sample_data;
from bs4 import BeautifulSoup;
import urllib

url = sample_data.image_url_1;
img_data = requests.get(url);
print(img_data);
filename = url.split("/")[-1];
print(filename);

with open(filename, mode="wb") as f:
    f.write(img_data.content);
