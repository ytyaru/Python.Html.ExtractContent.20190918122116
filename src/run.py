#!/usr/bin/env python3
# coding: utf8
# 事前準備
#   pip3 install extractcontent3
#   wget -O index.html 適当なニュースサイトURL
import sys
import os
import extractcontent3

print(extractcontent3.__file__)
if len(sys.argv) < 1:
    raise Error('第1引数にHTMLファイルパスを指定してください。')
    exit()
if not os.path.isfile(sys.argv[0]): 
    raise Error('第1引数HTMLファイルパスが存在しません。:'+sys.argv[0])
    exit()

extractor = extractcontent3.ExtractContent()
print(dir(extractor))

opt = {"threshold":50}
extractor.set_option(opt)

html = open("index.html").read()
extractor.analyse(html)
text, title = extractor.as_text()
html, title = extractor.as_html()
title = extractor.extract_title(html)

print(title)
print(text)
print(html)

