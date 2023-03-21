from pathlib import Path;
import pandas as pd;
import sys;
sys.path.append(str(Path(__file__).resolve().parent.parent))

out_folder = Path("chap3/tmp");
out_folder.mkdir(exist_ok=True);

df = pd.read_csv("sample/test.csv");
national_lang = df.sort_values("国語", ascending=False);
national_lang.to_csv("chap3/tmp/export1.csv");