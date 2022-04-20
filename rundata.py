from data import *
import sys
from pyfiglet import Figlet
from termcolor import colored, cprint
from Tmiec import *
'''T
from PIL import Image
img = Image.open("ivt.png")
img.show()
'''
text = colored('Hello, World!', 'red', attrs=['reverse', 'blink'])
f=Figlet(font='standard')
print(colored(f.renderText(' O & M SERVICE '), 'green'))


print(" ")
choose_site=input(" NHẬP THÔNG TIN INVERTER (TMEIC or SIEMEN) : ")
print(" ")
if choose_site=="TMEIC":
    print(" INVETER TMEIC")
    while(1):
        try:
            print(" ")
            input_data=input(" Yêu cầu nhập mã lỗi TMEIC (UFxxx / UAxxx or exit) : ")
            print(" ")
            if (input_data=="exit"):
                break
            list_key = list(IVT_TMEIC.get(input_data).keys())
            dict_var = IVT_TMEIC.get(input_data)
            for i in range(len(list_key)):
                print(list_key[i] + " : " + dict_var[list_key[i]] )
                
        except:
            print("YÊU CẦU NHẬP LẠI MÃ LỖI ! ")
            print("")
else:
    
    while(1):
        print("IVT SIEMENS")
        try:
            print(" ")
            input_data=input(" Yêu cầu nhập mã lỗi SIEMEN or exit : ")
            print(" ")
            if (input_data=="exit"):
                break
            list_key = list(IVT.get(input_data).keys())
            dict_var = IVT.get(input_data)
            for i in range(len(list_key)):
                print(list_key[i] + " : " + dict_var[list_key[i]] )
                
        except:
            print("YÊU CẦU NHẬP LẠI MÃ LỖI ! ")
            print("")
