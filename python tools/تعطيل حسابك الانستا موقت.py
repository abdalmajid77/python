import requests
logo = ("""
       ――――――――𝐂𝐇 @JJ9MJ――――――――
           __     ___    __  ___  _____  
          / /    / _ \  |  |/  / | ____| 
         / /_   | | | | |  '  /  | |__   
        | '_ \  | | | | |    <   |___ \  
        | (_) | | |_| | |  .  \   ___) | 
         \___/   \___/  |__|\__\ |____/                                 
       ――――――――𝐁𝐘 @FFF0FFFF――――――――""")
print(logo)
r=requests.session()
Username = input('|*| Username >> ')
Password = input('|*| Password >> ')
def login_60k5():
    global Username
    global Password
    url = 'https://www.instagram.com/accounts/login/ajax/'
    hed1 ={'Accept': '*/*', 'Content-Type': 'application/x-www-form-urlencoded', 'Referer': f'https://www.instagram.com/{Username}/', 'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.2918.69 Safari/537.36', 'X-CSRFToken': 'zh823H0iQUdPtXyX7VryrkIauUF210Z3', 'X-IG-App-ID': '936619743392459', 'X-IG-WWW-Claim': 'hmac.AR0-HjAY_xuK-Lany9-2bVGPus2rT6hx0bfOO1SHQiulMoU8', 'X-Instagram-AJAX': 'c1a5380865bf', 'X-Requested-With': 'XMLHttpRequest'}
    data1 = {'username': Username, 'enc_password': f'#PWD_INSTAGRAM_BROWSER:0:1589682409:{Password}', 'queryParams': {}, 'optIntoOneTap': 'false'}
    login = r.post(url,headers=hed1,data=data1)
    respons = login.text
    try:
        url_id = f'https://www.instagram.com/{Username}/?__a=1'
        rq_id = r.get(url_id, headers={'sec-ch-ua-mobile': '?0', 'Upgrade-Insecure-Requests': '1',
                                       'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.212 Safari/537.36 OPR/76.0.4017.177'}).json()
        user_id = str(rq_id['logging_page_id'])
        idd = (user_id.split('_')[1])
        if ('userId') in respons:
            print('[*] Login Done @' + Username + ' <-> ' + idd)
            CSR = login.cookies['csrftoken']
            USER_ID = login.cookies['ds_user_id']
            MID = login.cookies['mid']
            RUR = login.cookies['rur']
            SESSION_ID = login.cookies['sessionid']
            haski = f"csrftoken={CSR}; rur={RUR}; mid={MID}; ds_user_id={USER_ID}; sessionid={SESSION_ID};"
        elif ("checkpoint_required") in respons:
            print("[+] Secure @" + Username + ' <-> ' + idd)
            exit()
        else:
            print('[+]login Failed ')
            exit()
        def lo_60k5():
            url2= 'https://www.instagram.com/accounts/remove/request/temporary/'
            data2 = {'deletion-reason': 'too-busy', 'enc_password': f'#PWD_INSTAGRAM_BROWSER:0:1620504501:{Password}'}
            hed2={'accept': '*/*', 'accept-encoding': 'gzip,deflate,br', 'accept-language': 'ar', 'content-length': '239', 'content-type': 'application/x-www-form-urlencoded', 'Host': 'www.instagram.com', 'origin': 'https://www.instagram.com', 'referer': 'https://www.instagram.com/accounts/remove/request/temporary/', 'cookie': haski, 'user-agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64; Trident/7.0; rv:11.0) like Gecko', 'x-csrftoken': CSR, 'X-IG-App-ID': '936619743392459', 'X-IG-WWW-Claim': 'hmac.AR0k0teiPVS0FMBX4nePHqp7mg_3jxknidXiexZIYAlYpARU', 'X-Instagram-AJAX': 'fae627f53bc4', 'X-Requested-With': 'XMLHttpRequest'}
            ban = r.post(url2,headers=hed2,data=data2).text
            if '{"message":"Sorry, you can only disable your account once a week. Try again in a few days.","status":"fail"}' in ban:
                print("انتظر بعض ايام قبل تعطيل")
            elif 'ok' in ban:
                print('تم تعطيل حسابك القميل جدا بنجاح')
            else:
                print(ban)
        lo_60k5()
    except:print('Username not found')
login_60k5()