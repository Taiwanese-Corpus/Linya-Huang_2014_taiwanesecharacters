# -*- coding: utf-8 -*-
from 臺灣言語資料庫.資料模型 import 來源表
from 臺灣言語資料庫.資料模型 import 版權表
from bs4 import BeautifulSoup
from os.path import dirname, abspath, join, isdir
from posix import listdir
from 臺灣言語資料庫.資料模型 import 文本表


class 整合到資料庫:
    黃琳雅 = 來源表.objects.get_or_create(名='黃琳雅')[0]
    薛丞宏 = 來源表.objects.get_or_create(名='薛丞宏')[0]
    版權 = 版權表.objects.get_or_create(版權='無版權')[0]
    專案目錄 = join(dirname(abspath(__file__)), '..')
    公家內容 = {
        '來源': 黃琳雅,
        '版權': 版權,
        '種類': '語句',
        '語言腔口': '閩南語',
        '著作所在地': '臺灣',
        '著作年': '2014',
    }

    def 加詞目(self, 收錄者, 舊, 新):
        公家內容 = {
            '收錄者': 收錄者,
        }
        公家內容.update(self.公家內容)

        母語內容 = {
            '文本資料': 舊,
        }
        母語內容.update(公家內容)
        文本 = 文本表.加資料(母語內容)
        新母語內容 = {
            '文本資料': 新,
        }
        新母語內容.update(公家內容)
        文本.校對做(新母語內容)

    def 資料抓出來(self):
        歌詞目錄 = join(self.專案目錄, '咱的字你敢捌', 'min-nan-yu-ge-ci-xiao-zheng')
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


def 走(收錄者=整合到資料庫.薛丞宏):
    到資料庫 = 整合到資料庫()
    for 舊, 新 in 到資料庫.資料抓出來():
        print(舊, '@@', 新)
        到資料庫.加詞目(收錄者, 舊, 新)
    return
