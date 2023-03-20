import requests;
from pathlib import Path;
import sys;
sys.path.append(str(Path(__file__).resolve().parent.parent));
import sample.sample_data as sample_data;
from bs4 import BeautifulSoup;

url = sample_data.yahoo_news;
html = requests.get(url);
soup = BeautifulSoup(html.content, 'html.parser');

topic = soup.find(class_="sc-fhiYOA lmAaIt");
for element in topic.find_all("a"):
    print(element.text);
