# -*- coding: utf-8 -*-

def downloader(url):
	import urllib2
	response = urllib2.urlopen(url)
	return response.read().decode('cp1251')

def parser(html_code):
	import re
	token = """<div class="b-cat-item".+\n.+\n\s*href="/catalog/products/(.+)_kanva.+">(.+)</a>\n.+\n.+\n.+\n.+\n.+src="(.+)"\n"""
	return re.findall(token, html_code)
	
def downloadPict(url, filename):
	import urllib
	urllib.urlretrieve(url, filename)
	pass

def imageSaver(raw_html):
	import string, os
	if not os.path.exists("/home/rishat/krestiki_pict"):
		os.mkdir("/home/rishat/krestiki_pict");
	for row in raw_html:
		downloadPict("http://krestiki.ru"+ row[2],"/home/rishat/krestiki_pict/"+row[2].split("/")[6])
	pass

def getPages():
	z = []
	for i in range(1,60):
		z.append("http://krestiki.ru/catalog/products/kanva_s_risunkom_dlya_vyshivaniya/?PAGEN_1=" + str(i))
	return z

html = ""
krestiki_pages = getPages()

for krestiki_page in krestiki_pages:
	z = parser(downloader(krestiki_page))
	imageSaver(z);
	print krestiki_page
	for i in z:
		html += "<tr>\n"
		html += "\t<td><img src='/files/image/krestiki/"+ i[2].split("/")[6] +"'></td>\n"
		html += "\t<td>Size: "+i[0]+"</td>\n"
		html += "\t<td>"+i[1]+"</td>\n"
		html += "</tr>\n"

print html.encode('utf8')
