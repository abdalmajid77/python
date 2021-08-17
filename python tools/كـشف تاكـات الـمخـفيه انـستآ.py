import requests
import json
import pyfiglet,sys,time
rs = requests.session()
R = "\033[1;31m"
G = "\033[1;32m"
B = "\033[0;94m"
Y = "\033[1;33m"
br = pyfiglet.figlet_format("Instagram")
print(R+br)
def slow(T): 
	for r in T + '\n' :
	    sys.stdout.write(r)
	    sys.stdout.flush()
	    time.sleep(15/1400)

slow(R+"""اداه كشف جميع تاكات الحساب سهله الاستخدام سجل بوهمي اول شي ❤️
---------------------------------------------------------------~
""")                                                          
slow(R+'''
 by : @JJ9MJ
 Telegram :@bccccccc
---------------------------------------------------------------~
''')
print(Y+"سجل بحساب انستا:")
print("")     
username = input("يوزر :")
password = input("باسورد :")
Target = input("يوزر الضحيه :")
url = 'https://www.instagram.com/accounts/login/ajax/'
headers = {
     'accept': '*/*',
    'accept-encoding': 'gzip, deflate, br',
    'accept-language': 'ar,en-US;q=0.9,en;q=0.8',
    'content-length': '275',
    'content-type': 'application/x-www-form-urlencoded',
    'cookie': 'csrftoken=DqBQgbH1p7xEAaettRA0nmApvVJTi1mR; ig_did=C3F0FA00-E82D-41C4-99E9-19345C41EEF2; mid=X8DW0gALAAEmlgpqxmIc4sSTEXE3; ig_nrcb=1',
    'origin': 'https://www.instagram.com',
    'referer': 'https://www.instagram.com/',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-origin',
    'user-agent': 'Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.198 Mobile Safari/537.36',
    'x-csrftoken': 'DqBQgbH1p7xEAaettRA0nmApvVJTi1mR',
    'x-ig-app-id': '936619743392459',
    'x-ig-www-claim': '0',
    'x-instagram-ajax': 'bc3d5af829ea',
    'x-requested-with': 'XMLHttpRequest'
    }
data = {
         'username': f'{username}',
         'enc_password': f'#PWD_INSTAGRAM_BROWSER:0:1589682409:{password}',
         'queryParams': '{}',
         'optIntoOneTap': 'false'
    }    
r = rs.post(url, headers=headers, data=data)
if  'authenticated":true' in r.text:
    print("")
    print(G+"-"*25)	
    print("")
    print(G+"تم تسجيل :"+username)
    try:
        u = rs.get(f"https://www.instagram.com/{Target}/?__a=1")
        id =  str(u.json()["graphql"]["user"]["id"])
        print(G+f"{Target} : {id}")
        print("")
        print(G+"-"*25)
    except:
    	print(R+"عذرا يوزر الضحيه خطأ ")
    	exit()	
    s =rs.get('https://www.instagram.com/graphql/query/?query_hash=303a4ae99711322310f25250d988f3b7&variables={"reel_ids":["%s"],"tag_names":[],"location_ids":[],"highlight_reel_ids":[],"precomposed_overlay":false,"show_story_viewer_list":true,"story_viewer_fetch_count":50}'%(id))
    ss = json.loads(s.content.decode())
    if len(ss['data']['reels_media'])>0:
        print("")
        print(B+"Usernames hidden in the story :")
        print("")
        for i in ss['data']['reels_media']:
            da = i['items']
            if len(da)>0:
                for ii in da:
                    if len(ii['tappable_objects'])>0:
                        for iii in ii['tappable_objects']:
                            user = iii['username']   
                            print(G+f"username :{user}")       
    else:
    	print(R+"عذرا اسم المستخدم لم يضع اي تاك @")   	
elif '{"message":"checkpoint_required"' in r.text:
	print(R+"Checkpoint")
else:
    print(R+"اليوزر او الرمز خطا اعد المحاوله")