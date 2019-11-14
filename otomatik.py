#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
import time

os.system("anonsurf start")
os.system("clear")
print("Yeni IP Adres :")
print("-----------------------------")
os.system("curl icanhazip.com")
print("-----------------------------")

while True:
	time.sleep(60)
	os.system("anonsurf restart")
	os.system("clear")
	print("Yeni IP Adres :")
	print("-----------------------------")
	os.system("curl icanhazip.com")
	print("-----------------------------")
