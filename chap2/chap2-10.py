import requests;
from pathlib import Path;
import sys;
sys.path.append(str(Path(__file__).resolve().parent.parent));
import sample.sample_data as sample_data;
from bs4 import BeautifulSoup;
import urllib

url = sample_data.sample_url_2;
html = requests.get(url);
soup = BeautifulSoup(html.content, "html.parser");

filename = "chap2/linklist.txt";
with open(filename, mode="w", encoding="utf-8") as f:
    for element in soup.find_all("a"):
        url_href = element.get("href");
        link_url = urllib.parse.urljoin(url, url_href);
        f.write(element.text+"\n");
        f.write(link_url+"\n");
        f.write("\n");