#!/usr/bin/python
# -*- coding: utf-8 -*-
#import MeCab
#m = MeCab.Tagger()
#print m.parse("おはよう、RaspberryPiがやっときましたよ。いえー。")

import eyeD3
tag=eyeD3.Tag()
tag.link("/home/pi/share/TBS_2014-10-02-0813.mp3")
tag.header.setVersion(eyeD3.ID3_V2_3);
tag.setTextEncoding(eyeD3.UTF_16_ENCODING);
tag.setTitle(u"テスト")
tag.setArtist(u"テストw")
tag.update()
