#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
import time

os.system("apt install figlet")
os.system("clear")
os.system("figlet OTO IP")
print("""
Bu araçla otomatik olarak IP Adres değiştirebilirsiniz, değeri saniye olarak girin.
""")

sure = input("IP Değişim Süre(saniye) : ")

os.system("anonsurf start")
os.system("clear")
print("Yeni IP Adres :")
print("-----------------------------")
os.system("curl icanhazip.com")
print("-----------------------------")

while True:
	time.sleep(sure)
	os.system("anonsurf restart")
	os.system("clear")
	print("Yeni IP Adres :")
	print("-----------------------------")
	os.system("curl icanhazip.com")
	print("-----------------------------")
