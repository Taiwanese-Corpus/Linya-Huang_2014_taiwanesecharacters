# -*- coding: utf-8 -*-
from os.path import dirname, abspath, join, isdir
from posix import listdir

from bs4 import BeautifulSoup
import yaml


_專案目錄 = dirname(abspath(__file__))


class 處理資料:

    def 資料抓出來(self):
        歌詞目錄 = join(_專案目錄, '咱的字你敢捌', 'min-nan-yu-ge-ci-xiao-zheng')
        for 資料夾 in listdir(歌詞目錄):
            if isdir(join(歌詞目錄, 資料夾)):
                with open(join(歌詞目錄, 資料夾, 'index.html')) as 檔案:
                    格式 = BeautifulSoup(檔案, 'lxml')
                    舊歌詞 = self._整理出內底歌詞(
                        格式, "sites-layout-tile sites-tile-name-content-1"
                    )
                    新歌詞 = self._整理出內底歌詞(
                        格式, "sites-layout-tile sites-tile-name-content-2")
                    for 舊, 新 in zip(舊歌詞, 新歌詞):
                        if '純學術用絕無商業用途' not in 新 and 新 != '':
                            yield (舊, 新)

    def _整理出內底歌詞(self, 格式, class名):
        td內容 = 格式.findAll("td", {"class": class名})[0]
        開始 = False
        for 第幾筆, 一逝 in enumerate(td內容.findAll('p')):
            資料 = ' '.join(一逝.get_text().strip().split())
            if 第幾筆 >= 2:
                if '作詞' not in 資料 and '作曲' not in 資料 and '編曲' not in 資料:
                    開始 = True
                if 開始 and 資料 != '':
                    yield 資料


if __name__ == '__main__':
    資料內容 = {
        '來源': '黃琳雅',
        '版權': '無版權',
        '種類': '語句',
        '語言腔口': '閩南語',
        '著作所在地': '臺灣',
        '著作年': '2014',
        '下層': [],
    }
    到資料庫 = 處理資料()
    for 舊, 新 in 到資料庫.資料抓出來():
        print(舊, '@@', 新)
        資料內容['下層'].append({'相關資料組': [舊, 新]})

    with open(join(_專案目錄, '咱的字你敢捌.yaml'), 'w') as 檔案:
        yaml.dump(資料內容, 檔案, default_flow_style=False, allow_unicode=True)
