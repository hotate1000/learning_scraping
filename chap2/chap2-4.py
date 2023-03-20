import requests;
from pathlib import Path;
import sys;
sys.path.append(str(Path(__file__).resolve().parent.parent));
import sample.sample_data as sample_data;
from bs4 import BeautifulSoup;

url = sample_data.sample_url_2;
html = requests.get(url);
soup = BeautifulSoup(html.content, "html.parser");

for element in soup.find_all('li'):
    print(element.text);
