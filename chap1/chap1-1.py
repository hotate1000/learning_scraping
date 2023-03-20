import requests;
from pathlib import Path;
import sys;
sys.path.append(str(Path(__file__).resolve().parent.parent));
import sample_data;

url = sample_data.sample_url;
response = requests.get(url);
print(response);
response.encoding = response.apparent_encoding;
print(response.text);
