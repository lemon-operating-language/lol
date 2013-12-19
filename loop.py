#!/usr/bin/env python2
#-*- coding: utf-8 -*-

import time,program

while 1:
	try:
		reload(program)
		print time.time(), program.program.to_text()
	except Exception as e:
		print time.time(), str(e)
	time.sleep(1)
