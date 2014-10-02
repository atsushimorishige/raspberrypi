#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys
reload(sys)
sys.setdefaultencoding('utf-8')

import csv
import random
import urllib
import MeCab
import re



def textdownload(sourceURL):
    res = urllib.urlopen(sourceURL)
    downloadedText = res.read()
    #青空文庫の文字コードはshiftJISなので変換。デフォルトエンコーディングがasciiだとUnicodeDecodeErrorを吐かれる
    downloadedText = unicode(downloadedText,'shift_jis')
    downloadedText = re.sub("\n","", downloadedText)
    #本文のところだけを抜き出す
    downloadedText = re.search('<div class="main_text">.+?</div>',downloadedText).group()
    #ルビ抜き。全角文字を使うときはユニコード指定
    downloadedText = re.sub(u'（</rp>.+?<rp>）',"", downloadedText)
    #タグ抜き。
    downloadedText = re.sub('<.+?>',"", downloadedText)
    #MeCabはstrじゃないとパースしてくれないので、str形式で出力
    return str(downloadedText)
 
def wakati(text):
    t = MeCab.Tagger("-Owakati")
    m = t.parse(text)
    result = m.rstrip(" \n").split(" ")
    return result

if __name__=="__main__":
	urlList=[]
	with open('./share/list_person_all_extended_utf8.csv','r') as f:
		reader = csv.reader(f)
		header = next(reader)
		for row in reader:
			urlList.append(row[50])
	#print(reader.line_num)
	#print urlList[random.randint(1,reader.line_num)]
	urlResult=urlList[random.randint(1,reader.line_num)]	
	src=textdownload(urlResult)
	wordlist = wakati(src)
	markov = {}
	w1=''
	w2=''
	w3=''
	for word in wordlist:
		if w1 and w2 and w3:
			if (w1,w2,w3) not in markov:
               		 	markov[(w1,w2,w3)] = []
        		markov[(w1,w2,w3)].append(word)
        	w1,w2,w3=w2,w3,word
	count = 0
	sentence=''
	w1,w2,w3=random.choice(markov.keys())
    #カウントの数はおこのみで
	while count <50:
		if markov.has_key((w1,w2,w3))==True:
			tmp = random.choice(markov[(w1,w2,w3)])
			sentence += tmp
        	w1,w2,w3=w2,w3,tmp
        	count +=1   
    #時々、文の切れっ端から最初の文章が始まるので、最初の句点(。)までの部分は取っ払う。 
	sentence = re.sub("^.+?。", "", sentence)
    #閉じ括弧も同様
	sentence = re.sub("^」", "", sentence)       
    #あと、最後の句点(。)から先も取っ払ってしまう
	#sentence = re.search(r".+。", sentence).group()
	print("らずぱいから自動ツイート："+sentence)
	#print(len(sentence))
	print("元ネタ："+urlResult)
