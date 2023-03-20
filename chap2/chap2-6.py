import requests;
from pathlib import Path;
import sys;
sys.path.append(str(Path(__file__).resolve().parent.parent));
import sample.sample_data as sample_data;
from bs4 import BeautifulSoup;

url = sample_data.sample_url_2;
html = requests.get(url);
soup = BeautifulSoup(html.content, "html.parser");

chap2 = soup.find(id="chap2");
print(chap2);
print(type(soup));
print(type(chap2));
print("--------")
for element in chap2.find_all("li"):
    print(element.text);