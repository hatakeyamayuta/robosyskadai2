#!/usr/bin/env python
import rospy
import wiringpi
import time
import subprocess
from std_msgs.msg import String
def cb(message):
	global n
	n = message.data
	if n =="on":
		wiringpi.digitalWrite( led_pin, 1 )
	elif n=="off":
		wiringpi.digitalWrite( led_pin, 0 )
	else:
		wiringpi.digitalWrite( led_pin, 1 )
		time.sleep(0.5)
		wiringpi.digitalWrite( led_pin, 0 )
		time.sleep(0.5)
				
if __name__=='__main__':
	led_pin = 2
	wiringpi.wiringPiSetupSys()
	subprocess.check_call('gpio export 2 out',shell=True)
	wiringpi.pinMode( led_pin, 1 )
	
	rospy.init_node('twice')
	sub = rospy.Subscriber('count_up',String,cb)
	pub = rospy.Publisher('twice',String,queue_size=1)
	rate = rospy.Rate(10)
	while not rospy.is_shutdown():
		pub.publish("run")
		rate.sleep()
