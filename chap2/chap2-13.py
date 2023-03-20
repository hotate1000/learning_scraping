import requests;
from pathlib import Path;
import sys;
sys.path.append(str(Path(__file__).resolve().parent.parent));
import sample.sample_data as sample_data;
from bs4 import BeautifulSoup;
import urllib;

url = sample_data.sample_url_2;
html = requests.get(url);
soup = BeautifulSoup(html.content, "html.parser");

for element in soup.find_all("img"):
    src = element.get("src");
    print('------');
    print(src);
    print('------');
    image_url = urllib.parse.urljoin(url, src);
    filename = image_url.split("/")[-1];
    print(src, ">>", filename);