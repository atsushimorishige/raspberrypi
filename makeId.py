#!/usr/bin/python
# -*- coding: utf-8 -*-
import datetime
import sys


def getPersonalty(arg1):
	if arg1 == 1:
		return ("伊集院","伊集院光深夜の馬鹿力")
	elif arg1 == 2:
		return ("爆笑問題","真夜中のカーボーイ")
	elif arg1 == 3:
		return ("山里亮太","不毛な議論")
	elif arg1 == 4:
		return ("おぎやはぎ","メガネびいき")
	elif arg1 == 5:
		return ("バナナマン","バナナムーン")
	elif arg1 == 6:
		return ("エレ片","コント太郎")
	else:
		return ("other","other")



if __name__ == '__main__':
	import eyeD3
	argvs = sys.argv
	tag=eyeD3.Tag()
	d=datetime.datetime.now()
	tuple=getPersonalty(d.weekday())
	print d.weekday()
	print tuple[0]
	print argvs[1]
	
	tag.link(argvs[1])
	tag.header.setVersion(eyeD3.ID3_V2_4)
	tag.setTextEncoding(eyeD3.UTF_8_ENCODING);
	tag.setTitle(tuple[0]+str(d))
	tag.setAlbum(tuple[0])
	tag.setArtist(tuple[1])
	tag.update()
