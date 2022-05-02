# The tool is free, it is forbidden to sell it or modify its rights
# Developed by mr.joker
# instagram : @221298 | telegram : @vv1ck
try:
	from requests import post,get
	from random import choice
	import threading,requests,uuid
	from colorama import Fore
except Exception as Joker:exit(Joker)
Blou = Fore.BLUE;wit = "\033[1;37;40m"
uuid=uuid.uuid4()
class Auto_claimer_Target:
	def __init__(self):
		self.dn=0;self.err=0;self.prox=0
		self.use=0
		self.sis=0
		self.stops=0
		self.proxylist = []
		self.username = input('[$] Enter username (Target) : ')
		if self.username=='':exit(input('[!] You cannot leave this option blank ..!'))
		self.sisn=input('[$] Enter sessionid : ')
		if self.sisn=='':exit(input('[!] You cannot leave this option blank ..!'))
		try:self.proxy=open(input('[$] Enter name file (proxy) : '),'r').read().splitlines()
		except FileNotFoundError:exit(input('\n[-] The file name is incorrect !\n'))
		
		try:self.Trts=int(input('[$] Enter threading : '))
		except ValueError:exit(input('\n [-] Please enter a number, not a letter !\n'))
		self.headers={'Host': 'api2.musical.ly','Connection': 'close','sdk-version': '1','User-Agent': 'TikTok 13.3.0 rv:133016 (iPhone; iOS 14.6; ar_JO@numbers=latn) Cronet','x-tt-trace-id': '00-f9a861fb243149ececad769a2f885ed7-f9a861fb243149ec-01','Cookie': 'sessionid='+self.sisn,'X-Khronos': '1651151348','X-Gorgon': '830077702001086c95c07d5bae723fcdaa9ea05f9960faad72f8'}
		self.urls=f'https://api2.musical.ly/aweme/v1/search/sug/?version_code=13.3.0&pass-region=1&pass-route=1&language=ar&app_name=musical_ly&vid={uuid}&app_version=13.3.0&carrier_region=JO&is_my_cn=0&channel=App%20Store&mcc_mnc=41601&device_id={uuid}&tz_offset=10800&account_region=&sys_region=JO&aid=1233&locale=ar&residence=JO&screen_width=1125&uoo=1&openudid=7426eb7827be74f624392caad15e75cecb964e47&os_api=18&ac=WIFI&os_version=14.6&app_language=ar&tz_name=Asia/Amman&current_region=JO&device_platform=iphone&build_number=133016&device_type=iPhone11,2&iid=7091638634483238662&idfa={uuid}&keyword={self.username}&source=discover'
		self.Check_sessionid()
	
	def Claimed(self):
		try:
			sent=post('https://www.tiktok.com/passport/web/login_name/update/?aid=1988&app_language=ar&app_name=tiktok_web&browser_language=en&browser_name=Mozilla&browser_online=true',headers={'Host': 'www.tiktok.com','Accept': '*/*','Accept-Language': 'en','Content-Type': 'application/x-www-form-urlencoded','Origin': 'https://www.tiktok.com','tt-csrf-token': 'Kp0Tepeh-mSyGmG3e6VP-bgxl1oqUg7_Gcq0','Connection': 'keep-alive','User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_6) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/14.1.1 Safari/605.1.15','Content-Length': '22','Cookie': 'sessionid='+self.sisn},data=f'login_name={self.username}')
			
			if ( '"message":"success"' in sent.text ):
				while 1:
					self.stops+=1
					if self.stops==1:
						exit(input(f'\n================\n[$] Claimed [{self.username}] ✅|\nSessionid: {sisn}\n================\n'))
						exit(0)
					elif self.stops==2:
						exit(input(f'\n================\n[$] Claimed [{self.username}] ✅|\nSessionid: {sisn}\n================\n'))
						exit(0)
					elif self.stops==3:
						exit(input(f'\n================\n[$] Claimed [{self.username}] ✅|\nSessionid: {sisn}\n================\n'))
						exit(0)
					else:
						exit(input(f'\n================\n[$] Claimed [{self.username}] ✅|\nSessionid: {sisn}\n================\n'))
						exit(0)
			elif ( '"الاسم موجود بالفعل"' in sent.text ):pass
			elif ( 'انتهت المحادثة، الرجاء تسجيل الدخول مرة أخرى.' in sent.text ):
				print(f"\n================\nYou can't use this sessionid it's off : {self.sisn}\n================\n")
			elif ( 'login name can only be updated once within one month.' in sent.text ):
				exit(input(f'\n================\nYour username can only be changed once in a month :\nsessionid: {self.sisn}\n================'))
			else:
				self.err+=1
				print(f'\rCheck [{self.dn}] | errors [{self.err}] | Proxies [{self.prox}] | User[{self.username}]\r',end="")
		except KeyboardInterrupt:exit()
	
	def Check_Auto2(self):
		while True:
			for pro in self.proxy:
				self.proxylist.append(pro)
				run = str(choice(self.proxylist))
			try:
				PROXY = {
					"http": f"http://{run}",
					"https": f"http://{run}"}
				sent=get(self.urls,headers=self.headers,proxies=PROXY)
				if ( f'"content":"{self.username}"' in sent.text ):
					self.dn+=1
					print(f'\rCheck [{self.dn}] | errors [{self.err}] | Proxies [{self.prox}] | User[{self.username}]\r',end="")
				elif ( '"info":"{}"' in sent.text ):
					th1 = threading.Thread(target=self.Claimed)
					th1.start()
				elif ( sent.status_code == 403 ):
					self.prox+=1
					print(f'\rCheck [{self.dn}] | errors [{self.err}] | Proxies [{self.prox}] | User[{self.username}]\r',end="")
				else:
					self.err+=1
					print(f'\rCheck [{self.dn}] | errors [{self.err}] | Proxies [{self.prox}] | User[{self.username}]\r',end="")
			except KeyboardInterrupt:exit()
			except RuntimeError:pass
			except requests.exceptions.ConnectionError:
				self.prox+=1
				print(f'\rCheck [{self.dn}] | errors [{self.err}] | Proxies [{self.prox}] | User[{self.username}]\r',end="")
	
	def Check_Auto_Target(self):
		while True:
			try:
				sent=get(self.urls,headers=self.headers)
				if ( f'"content":"{self.username}"' in sent.text ):
					self.dn+=1
					print(f'\rCheck [{self.dn}] | errors [{self.err}] | Proxies [{self.prox}] | User[{self.username}]\r',end="")
				elif ( '"info":"{}"' in sent.text ):
					th1 = threading.Thread(target=self.Claimed)
					th1.start()
				elif ( sent.status_code == 403 ):
					th1 = threading.Thread(target=self.Check_Auto2)
					th1.start()
				else:
					self.err+=1
					print(f'\rCheck [{self.dn}] | errors [{self.err}] | Proxies [{self.prox}] | User[{self.username}]\r',end="")
			except KeyboardInterrupt:exit()
			except requests.exceptions.ConnectionError:
				self.prox+=1
				print(f'\rCheck [{self.dn}] | errors [{self.err}] | Proxies [{self.prox}] | User[{self.username}]\r',end="")
			except RuntimeError:pass
	def TRYS(self):
		theards = []
		for i in range(self.Trts):
			th1 = threading.Thread(target=self.Check_Auto_Target)
			th1.start()
			theards.append(th1)	
		for th2 in theards:
			th2.join()
	def Check_sessionid(self):
		sent = get('https://www.tiktok.com/api/user/detail/?aid=1988&app_language=ar&app_name=tiktok_web&browser_language=ar&browser_name=Mozilla&browser_online=true&tz_name=Asia%2FAmman&uniqueId='+self.username+'&verifyFp=verify_l2opi6gw_qo0YieDW_P7ue_4Z3c_84pN_Fgkr4dNltFI1&webcast_language=ar',headers = {'Host': 'www.tiktok.com','Accept': '*/*','Connection': 'keep-alive','Cookie': 'sessionid='+self.sisn,'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_6) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/14.1.1 Safari/605.1.15','Accept-Language': 'ar',})
		if ( f'"uniqueId":"{self.username}"' in sent.text ) :
			if input('\n[?] are you ready? [ y / n ] : ') == 'y':
				print('\n\n=========================\n')
				self.TRYS()
			else:exit()
		elif ( '"user": {}' in sent.text ):
			exit(input(f'[!] This sessionid is not working >> {self.sisn}'))
		elif ( '"uniqueId":""' in sent.text ) :
			if input('\n[?] are you ready? [ y / n ] : ') == 'y':
				print('\n\n=========================\n')
				th1 = threading.Thread(target=self.Claimed)
				th1.start()
			else:exit()
		else:print(sent.text)
class Auto_claimer_TIKTOK:
	def __init__(self):
		self.dn=0;self.err=0;self.prox=0
		self.use=0
		self.sis=0
		self.proxylist = []
		self.ss=input('[$] Enter name file (sessionid) : ')
		try:self.listSisn=open(self.ss,'r').read().splitlines()
		except FileNotFoundError:exit(input('\n[-] The file name is incorrect !\n'))
		
		try:self.listUser=open(input('[$] Enter name file (username) : '), 'r').read().splitlines()
		except FileNotFoundError:exit(input('\n[-] The file name is incorrect !\n'))
		
		try:self.proxy=open(input('[$] Enter name file (proxy) : '),'r').read().splitlines()
		except FileNotFoundError:exit(input('\n[-] The file name is incorrect !\n'))
		
		try:self.Trts=int(input('[$] Enter threading : '))
		except ValueError:exit(input('\n [-] Please enter a number, not a letter !\n'))
		
		self.Check_sessionid()
	def Claimed(self):
		global username,sisn
		try:
			sent=post('https://www.tiktok.com/passport/web/login_name/update/?aid=1988&app_language=ar&app_name=tiktok_web&browser_language=en&browser_name=Mozilla&browser_online=true',headers={'Host': 'www.tiktok.com','Accept': '*/*','Accept-Language': 'en','Content-Type': 'application/x-www-form-urlencoded','Origin': 'https://www.tiktok.com','tt-csrf-token': 'Kp0Tepeh-mSyGmG3e6VP-bgxl1oqUg7_Gcq0','Connection': 'keep-alive','User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_6) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/14.1.1 Safari/605.1.15','Content-Length': '22','Cookie': 'sessionid='+sisn},data=f'login_name={username}')
			
			if ( '"message":"success"' in sent.text ):
				print(f'\n================\n[$] Claimed [{username}] ✅|\nSessionid: {sisn}\n================\n')
				with open('Claimed-TikTok.txt', 'a') as J:
					J.write('username: '+username+'|sessionid: '+sisn+'\n')
			elif ( '"الاسم موجود بالفعل"' in sent.text ):pass
			elif ( 'انتهت المحادثة، الرجاء تسجيل الدخول مرة أخرى.' in sent.text ):
				print(f"\n================\nYou can't use this sessionid it's off : {sisn}\n================\n")
			elif ( 'login name can only be updated once within one month.' in sent.text ):
				print(f'\n================\nYour username can only be changed once in a month :\nsessionid: {sisn}\n================')
			else:
				self.err+=1
				print(f'\rCheck [{self.dn}] | errors [{self.err}] | Proxies [{self.prox}] | User[{username}]\r',end="")
		except KeyboardInterrupt:exit()
	def Check_Auto2(self):
		global username,headers,urls,sisn
		while True:
			for pro in self.proxy:
				self.proxylist.append(pro)
				run = str(choice(self.proxylist))
			try:
				PROXY = {
					"http": f"http://{run}",
					"https": f"http://{run}"}
				sent=get(urls,headers=headers,proxies=PROXY)
				if ( f'"content":"{username}"' in sent.text ):
					self.dn+=1
					print(f'\rCheck [{self.dn}] | errors [{self.err}] | Proxies [{self.prox}] | User[{username}]\r',end="")
				elif ( '"info":"{}"' in sent.text ):
					th1 = threading.Thread(target=self.Claimed)
					th1.start()
				elif ( sent.status_code == 403 ):
					self.prox+=1
					print(f'\rCheck [{self.dn}] | errors [{self.err}] | Proxies [{self.prox}] | User[{username}]\r',end="")
				else:
					self.err+=1
					print(f'\rCheck [{self.dn}] | errors [{self.err}] | Proxies [{self.prox}] | User[{username}]\r',end="")
			except KeyboardInterrupt:exit()
			except RuntimeError:pass
			except requests.exceptions.ConnectionError:
				self.prox+=1
				print(f'\rCheck [{self.dn}] | errors [{self.err}] | Proxies [{self.prox}] | User[{username}]\r',end="")
	def Check_Auto_list(self):
		global username,headers,urls,sisn
		while True:
			if self.use >= len(self.listUser):
				self.use=0
				username = self.listUser[self.use]
				self.use+=1
			else:
				username = self.listUser[self.use]
				self.sis+=1
			
			if self.sis >= len(self.listSisn):
				self.sis=0
				sisn = self.listSisn[self.sis]
				self.sis+=1
			else:
				sisn = self.listSisn[self.sis]
				self.sis+=1
			headers={'Host': 'api2.musical.ly','Connection': 'close','sdk-version': '1','User-Agent': 'TikTok 13.3.0 rv:133016 (iPhone; iOS 14.6; ar_JO@numbers=latn) Cronet','x-tt-trace-id': '00-f9a861fb243149ececad769a2f885ed7-f9a861fb243149ec-01','Cookie': 'sessionid='+sisn,'X-Khronos': '1651151348','X-Gorgon': '830077702001086c95c07d5bae723fcdaa9ea05f9960faad72f8'}
			urls=f'https://api2.musical.ly/aweme/v1/search/sug/?version_code=13.3.0&pass-region=1&pass-route=1&language=ar&app_name=musical_ly&vid={uuid}&app_version=13.3.0&carrier_region=JO&is_my_cn=0&channel=App%20Store&mcc_mnc=41601&device_id={uuid}&tz_offset=10800&account_region=&sys_region=JO&aid=1233&locale=ar&residence=JO&screen_width=1125&uoo=1&openudid=7426eb7827be74f624392caad15e75cecb964e47&os_api=18&ac=WIFI&os_version=14.6&app_language=ar&tz_name=Asia/Amman&current_region=JO&device_platform=iphone&build_number=133016&device_type=iPhone11,2&iid=7091638634483238662&idfa={uuid}&keyword={username}&source=discover'
			try:
				sent=get(urls,headers=headers)
				if ( f'"content":"{username}"' in sent.text ):
					self.dn+=1
					print(f'\rCheck [{self.dn}] | errors [{self.err}] | Proxies [{self.prox}] | User[{username}]\r',end="")
				elif ( '"info":"{}"' in sent.text ):
					th1 = threading.Thread(target=self.Claimed)
					th1.start()
				elif ( sent.status_code == 403 ):
					th1 = threading.Thread(target=self.Check_Auto2)
					th1.start()
				else:
					self.err+=1
					print(f'\rCheck [{self.dn}] | errors [{self.err}] | Proxies [{self.prox}] | User[{username}]\r',end="")
			except KeyboardInterrupt:exit()
			except requests.exceptions.ConnectionError:
				self.prox+=1
				print(f'\rCheck [{self.dn}] | errors [{self.err}] | Proxies [{self.prox}] | User[{username}]\r',end="")
			except RuntimeError:pass	
	def TRYS(self):
		theards = []
		for i in range(self.Trts):
			th1 = threading.Thread(target=self.Check_Auto_list)
			th1.start()
			theards.append(th1)	
		for th2 in theards:
			th2.join()
	def Check_sessionid(self):
		file=open(self.ss, 'r')
		while 1:
			sisn = file.readline().split('\n')[0]
			if sisn=='':
				mods=input('\n[$] The process of checking the session has finished, do you want to start the tool or not? [ y / n ] : ')
				if ( mods == 'y' ):
					print('\n\n=======================\n')
					self.TRYS()
				else:exit()
			sent=get('https://api16-normal-c-alisg.tiktokv.com/aweme/v1/notice/list/message/?device_id=7090896374259009030&os_version=14.6&is_my_cn=0&residence=JO&iid=7093099257280382722&app_name=musical_ly&pass-route=1&locale=ar&pass-region=1&ac=WIFI&sys_region=JO&version_code=16.6.2&vid=B7113870-9703-4621-8C59-4DAFEF3156CF&channel=App%20Store&op_region=JO&os_api=18&idfa=233E9D40-0755-46BA-87B7-F3BEC64B4FBC&device_platform=iphone&device_type=iPhone11,2&openudid=7426eb7827be74f624392caad15e75cecb964e47&account_region=&tz_name=Asia/Amman&tz_offset=10800&current_region=JO&carrier_region=JO&build_number=166206&aid=1233&mcc_mnc=41601&screen_width=1125&content_language=&app_skin=white&language=ar&cdid=63BF2BA0-A9F5-4A0E-8DBE-0F3530C9949C&uoo=1&app_version=16.6.2&app_language=ar&min_time=0&is_mark_read=1&max_time=0&count=20&notice_group=36',headers={'Host': 'api16-normal-c-alisg.tiktokv.com','Connection': 'keep-alive','sdk-version': '1','User-Agent': 'TikTok 16.6.2 rv:166206 (iPhone; iOS 14.6; ar_JO@numbers=latn) Cronet','x-tt-store-idc': 'alisg','x-tt-store-region': 'jo','X-SS-DP': '1233','x-tt-trace-id': '00-85faa965106267ecaee6d046060804d1-85faa965106267ec-01','Cookie': 'sessionid='+sisn,'X-Khronos': '1651515238','X-Gorgon': '84020014200072709939e14bbf4b34830c70f662bfb81f847c59'}).text
			if ( '"انتهت صلاحية تسجيل الدخول"' in sent) :
				print(f'[!] This sessionid is not working >> {sisn}')
			else:
				print(f'[$] The sessionid is working >> {sisn}')
def Settings():
	Modes=input(f"""{Blou}
       _       _   Auto 
   ___| | __ _(_)_ __ ___   ___ _ __  
  / __| |/ _` | | '_ ` _ \ / _ \ '__| 
 | (__| | (_| | | | | | | |  __/ |    
  \___|_|\__,_|_|_| |_| |_|\___|_|    
               For TikTok
           By Joker @221298
{wit}
- 1 ) Target one account [username+sessionid]
- 2 ) Targeting through a list [usernames+sessions]
- 99 ) Exit(0)
Enter : """)
	if Modes=='1':Auto_claimer_Target()
	elif Modes=='2':Auto_claimer_TIKTOK()
	else:exit()
Settings()
