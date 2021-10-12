import os
import time
import colorama
from colorama import Fore 

def banner_funtion():
	os.system("figlet Xscanner1.0")
	print(Fore.WHITE + "Creador: @Crypto453")
def windows_clear():
	os.system("clear")

windows_clear()
banner_funtion()
list_a = ["[1] Escaneo de puertos manual", "[2] Escaneo de puertos automatico", "[3] EXIT"]
for lista_x in list_a:
	print(Fore.WHITE + lista_x)
	time.sleep(0.3)
user_a = int(input("===> "))
if user_a == 1:
	user_b = input(Fore.RED + "Escriba la direccion IP: ")
	user_b_b = input(Fore.RED + "Escriba los puertos \n debe dejar espacios ejemplo: 40 78 86 45\n===> ")
	os.system(f"nc -v -z {user_b} {user_b_b}")
	print(Fore.WHITE + "Escaneo completado")
elif user_a == 2:
	principal_user = input(Fore.WHITE + "Escriba la direccion IP: ")
	os.system(f"nc -v -z {principal_user} 1-1000")
	print(Fore.RED + "Escaneo completado... 1000 puertos escaneados")
elif user_a	== 3:
	quit()
else:
	print("error, intentelo denuevo")