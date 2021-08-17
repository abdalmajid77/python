import random,webbrowser
rr='1234567890'
R =('='*60)
BGreen=' [1;36m'
g=' [1;37m'

print(f'''{BGreen}{R}

Fucking Tool To make Fucking Combo \n By @trprogram ~ @ttrakos & @PiPPi
{R}
''')
print('[+] 077 \n [+] 078 ')
b= ('077','078')
i =int(input(g+'[+] Choose the number you want :'))
print(R)
for i in range(i):
 k=str("".join(random.choice(b)for i in range(1)))
 r=str("".join(random.choice(rr)for i in range(8)))
 n=(k+r)
 print(n+':'+n)
 with open('XS2.txt', 'a') as x:
  x.write(n+':'+n+'''
''')
print(R)  
print('It was saved in a file name [XS2.txt] good ')  
webbrowser.open('https://t.me/JJ9MJ')
