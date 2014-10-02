#!/usr/bin/python
# -*- coding: utf-8 -*-
#import MeCab
#m = MeCab.Tagger()
#print m.parse("おはよう、RaspberryPiがやっときましたよ。いえー。")

import eyed3

audiofile = eyed3.load("./share/TBS_2014-10-02-0813.mp3")
audiofile.tag.artist = (u"テスト")
audiofile.tag.artist = (u"アルバム名")
audiofile.tag.artist = (u"タイトル")
