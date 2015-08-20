# 咱的字你敢捌－台語漢字

##緣起
為推廣台語漢字，特設立此平台，依教育部閩南語常用辭典為標準校正台語歌詞用字。
為著欲推廣台語漢字，特別設立這个平台，依教育部閩南語常用辭典為標準校正台語歌詞用字。
(純為學術研究，絕無商業用途)

附件有簡介之PPT歡迎[點閱](https://docs.google.com/viewer?a=v&pid=sites&srcid=ZGVmYXVsdGRvbWFpbnx0YWl3YW5lc2VjaGFyYWN0ZXJzfGd4OjIxMmI2MDA2YjcyZGI5NDU): )

## 資料處理

### 原始資料
本專案原始資料是用(google-sites-liberation)[https://github.com/sih4sing5hong5/google-sites-liberation]掠的。

### 臺灣言語資料庫
在`臺灣言語資料庫`專案目錄下
```bash
git clone https://github.com/Taiwanese-Corpus/Linya-huang_taiwanesecharacters.git
sudo apt-get install -y python-virtualenv
virtualenv --python=python3 venv
. venv/bin/activate
pip install -r requirements.txt
echo "from 轉到臺灣言語資料庫.整合到資料庫 import 走 ; 走()" | PYTHONPATH=Linya-huang_taiwanesecharacters python manage.py shell
```