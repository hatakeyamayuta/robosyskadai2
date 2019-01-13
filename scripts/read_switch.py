#!/usr/bin/env python
import rospy
from std_msgs.msg import String

if __name__=='__main__':
	rospy.init_node('count')
	pub = rospy.Publisher('count_up',String,queue_size=3)
	rate = rospy.Rate(10)
	while not rospy.is_shutdown():
		with open('/home/ubuntu/switch.txt') as f:
			s = f.read()
			s = s.strip()	
		pub.publish(s)
		rate.sleep()
