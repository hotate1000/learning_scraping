import requests;
from pathlib import Path;
import sys;
sys.path.append(str(Path(__file__).resolve().parent.parent));
import sample.sample_data as sample_data;
from bs4 import BeautifulSoup;
import urllib;
import time;

url = sample_data.image_url_1;
html = requests.get(url);
soup = BeautifulSoup(html.content, "html.parser");

out_folder = Path("chap2/img");
out_folder.mkdir(exist_ok=True);

for element in soup.find_all("img"):
    src = element.get("src");

    image_url = urllib.parse.urljoin(url, src);
    img_data = requests.get(url);

    filename = image_url.split("/")[-1];
    out_path = out_folder.joinpath(filename);

    with open(out_path, mode="wb") as f:
        f.write(img_data.content);
        time.sleep(1);
