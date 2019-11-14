#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
import time

os.system("anonsurf start")
os.system("clear")
os.system("curl icanhazip.com")

while True:
	time.sleep(60)
	os.system("anonsurf restart")
	os.system("clear")
	os.system("curl icanhazip.com")