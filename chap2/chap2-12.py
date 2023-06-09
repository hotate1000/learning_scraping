import requests;
from pathlib import Path;
import sys;
sys.path.append(str(Path(__file__).resolve().parent.parent));
import sample.sample_data as sample_data;
from bs4 import BeautifulSoup;
import urllib;

out_folder = Path("chap2/img");
out_folder.mkdir(exist_ok=True);

url = sample_data.image_url_1;
img_data = requests.get(url);

filename = url.split("/")[-1];
out_path = out_folder.joinpath(filename);

with open(out_path, "wb") as f:
    f.write(img_data.content);
