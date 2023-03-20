import requests;
from pathlib import Path;
import sys;
sys.path.append(str(Path(__file__).resolve().parent.parent));
import sample_data;
import codecs

url = sample_data.sample_url;
response = requests.get(url);
response.encoding = response.apparent_encoding;

filename = "chap1/download.txt";

f = codecs.open(filename, mode="w", encoding="utf-8");
f.write(response.text);
f.close();
print(response.text);

print('--------------');

with open(filename, mode="w", encoding="utf-8") as fw:
    fw.write(response.text);
print(response.text);