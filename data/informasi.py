# Decompile by Mardis (Tools By Kapten-Kaizo)
# Time Succes decompile : 2022-03-21 06:58:24.553587
import re,json

uid = None
username = None

class info:
	
	def __init__(self,kuki,kontol):
		self.kuki,self.kontol = kuki,kontol

	def myinfo(self):
		global uid, username
		uid = self.kuki.get("c_user")
		nama = re.findall("\<title\>(.*?)<\/title\>", self.kontol)[0]
		try:
			username = re.findall('> . <a href="\/(.*?)\/friends', self.kontol)[0]
		except:
			pass
		open("data/my_info","w").write(json.dumps({
		    "uid":uid,
		    "nama":nama,
		    "username":username
		    }
		))
		
		
