from colorama import Fore
import requests
import time
import os
os.system('cls')
red = Fore.RED
blue = Fore.BLUE
white = Fore.WHITE

logo = blue + ''' 

        ██╗██████╗░  ██╗███╗░░██╗███████╗░█████╗░
        ██║██╔══██╗  ██║████╗░██║██╔════╝██╔══██╗
        ██║██████╔╝  ██║██╔██╗██║█████╗░░██║░░██║
        ██║██╔═══╝░  ██║██║╚████║██╔══╝░░██║░░██║
        ██║██║░░░░░  ██║██║░╚███║██║░░░░░╚█████╔╝
        ╚═╝╚═╝░░░░░  ╚═╝╚═╝░░╚══╝╚═╝░░░░░░╚════╝░
              MADE BY SiMPLYISHAN
'''
print(logo)

info = requests.get('https://api.myip.com/')
print(red + "Your Ip Details Are" + blue + ' : ' + white + info.text)
time.sleep(3)
ask = input(white + """ Want To Save This Credentials In Txt File? 
                  1 - Yes 
                  2 - No \n""")
if ask == '1':
    with open('ipinfo.txt', 'w') as f:
        f.write(info.text)
        f.close()
    print('file saved...!')
elif ask == 'Yes':
    with open('ipinfo.txt', 'w') as f:
        f.write(info.text)
        f.close()
    print('file saved...!')
elif ask == 'yes':
    with open('ipinfo.txt', 'w') as f:
        f.write(info.text)
        f.close()
    print('file saved...!')
else:
    pass

time.sleep(2)
print('Thanks for using ipinfo by simplyishan!')
time.sleep(3)
exit()
