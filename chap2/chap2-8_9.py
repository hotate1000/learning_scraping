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

for element in soup.find_all('a'):
    print(element.text);
    url_href = element.get("href");
    print(url_href);
print('---------');
for element in soup.find_all('a'):
    print(element.text);
    url_href = element.get("href");
    link_url = urllib.parse.urljoin(url, url_href);
    print(link_url);