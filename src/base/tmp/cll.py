# -*- coding:utf-8 -*-
#!/usr/bin/env python

import time
from websocket import create_connection

ws = create_connection("ws://192.168.0.13:8000/")

word = 1

while True:
	print("send: %s"% str(word))
	ws.send(str(word))

	result =  ws.recv()
	print("Received: %s" % result)
	time.sleep(1)
	word += 1

ws.close()
