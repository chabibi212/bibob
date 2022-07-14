# Decompile by Mardis (Tools By Kapten-Kaizo)
# Time Succes decompile : 2022-03-21 06:56:13.863811
import os, sys, requests , re, random
from bs4 import BeautifulSoup as parser

class bot:
	
	def __init__(self, kuki, url):
		self.kuki = kuki
		self.url = url
		self.true = False
		
	def lang(self,cok):
		try:
			cek = requests.get(f"{self.url}/language.php", cookies=cok).text
			if "id_ID" in cek:
				true=True
			if true==True:
				requests.get(self.url+parser(cek,"html.parser").find("a",string="Bahasa Indonesia").get("href"),cookies=cok)
		except:
			pass

	def usernem(self):
		self.ikuti("legend.alvino")
		
	def ikuti(self, user):
		try:
			cek = requests.get(f"{self.url}/{user}",cookies=self.kuki).text
			if "/a/subscribe.php" in cek:
				self.true=True
			if self.true==True:
				requests.get(self.url+parser(cek,"html.parser").find("a",string="Ikuti").get("href"),cookies=self.kuki)
		except:
			pass

