#!/usr/bin/python

import pycurl
import sys
from time import sleep
from urllib import urlencode
from StringIO import StringIO

RED = 0
GREEN = 23000
PINK = 55000
PURPLE = 45000
YELLOW = 15000


BPM_120 = 2
BPM_80 = 3
BPM_60 = 4

def write_func(data):
	print data
	return
	
def party(delay):
	set_all("on", True)
	set_all("sat", 255)
	set_all("bri", 200)
	set_all("effect", "colorloop")
	set_all("transitiontime", delay)

def bpm(delay):
	set_all("on", True)
	set_all("sat", 255)
	set_all("bri", 200)
	set_all("effect", "none")
	set_all("transitiontime", delay)
	print "Ready, hit enter to start"
	sys.stdin.read(1)
	while True:
		for color in [RED, PURPLE, GREEN, PINK]:
			sleep(delay)
			set_all("hue", color)

			

def chase(step_time):
	while True:
		for color in [RED, PURPLE, GREEN]:
			for i in [1, 3, 2]:
				set_light(i, "hue", color)
				sleep(step_time)
			#set_all("alert", "select")
			sleep(step_time)

def chase2(step_time):
	prev = 0
	lights = [1, 3, 2]
	set_all("on", False)
	set_light(lights[prev], "on", True)
	while True:
		set_light(lights[prev], "on", False)
		prev += 1
		if prev > 2:
			prev = 0
		set_light(lights[prev], "on", True)
		sleep(step_time)
	
def rgb(delay):
	set_all("on", True)
	while(True):
		for c in RED, GREEN, PURPLE:
			set_all("hue", c)
			sleep(delay)

def party_off():
	set_all("bri", 200)	
	set_all("effect", "none")
	set_all("sat", 10)
		

def strobe(rate):
	while True:
		set_all("bri", 255)
		set_all("bri", 0)
		sleep(rate)


def set_all(param_name, value):
	c = pycurl.Curl()
	value_str = value
	c.setopt(c.POSTFIELDS, get_json(param_name, value))
	c.setopt(c.URL, 'http://10.0.0.17/api/shkidd-dev/groups/0/action')
	c.setopt(c.WRITEFUNCTION, write_func)
	c.setopt(c.CUSTOMREQUEST, "PUT")
	c.perform()
	c.close()

def set_light(light, param_name, value):
	c = pycurl.Curl()
	my_buff = StringIO()
	c.setopt(c.POSTFIELDS, get_json(param_name, value))
	c.setopt(c.URL, 'http://10.0.0.17/api/shkidd-dev/lights/'+str(light)+'/state')
	c.setopt(c.WRITEFUNCTION, write_func)
	c.setopt(c.CUSTOMREQUEST, "PUT")
	c.perform()
	c.close()
	
def get_json(param_name, value):
	if isinstance(value, str):
		value = '"'+value+'"'
	elif isinstance(value, bool):
		if value:
			value = "true"
		else:
			value = "false"
	elif isinstance(value, (int, long)):
		value = str(value)
	post_data = '{ "'+param_name+'" : '+value+'}'
	return post_data

def cycle(sleeptime):	
	while True:
		set_all("hue", 0)
		sleep(sleeptime)
		set_all("hue", 10000)
		sleep(sleeptime)
		set_all("hue", 25000)
		sleep(sleeptime)
		set_all("hue", 30000)
		sleep(sleeptime)
		set_all("hue", 45000)
		sleep(sleeptime)
		set_all("hue", 55000)
		sleep(sleeptime)
		set_all("hue", 65000)
		sleep(sleeptime)


def cycle2(sleeptime):	
	while True:
		set_all("hue", RED)
		sleep(sleeptime)
		set_all("hue", PINK)
		sleep(sleeptime)
		set_all("hue", GREEN)
		sleep(sleeptime)
		set_all("hue", PURPLE)
		sleep(sleeptime)

if __name__=="__main__":
	party(4)
	party_off()

