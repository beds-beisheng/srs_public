#!/usr/bin/env python  
import roslib
roslib.load_manifest('srs_symbolic_grounding')
from geometry_msgs.msg import *
import rospy
import tf


def publisher():
	pub = rospy.Publisher('robot_base_pose', Pose2D)
	rospy.init_node('publisher')
	listener = tf.TransformListener()
	rb_pose = Pose2D()
	listener.waitForTransform("/map", "/base_link", rospy.Time(0), rospy.Duration(4.0))
	while not rospy.is_shutdown():
		try:
			(trans,rot) = listener.lookupTransform("/map", "/base_link", rospy.Time(0))
			rb_pose.x = trans[0]
			rb_pose.y = trans[1]
			rb_pose_rpy = tf.transformations.euler_from_quaternion(rot)
			rb_pose.theta = rb_pose_rpy[2]
			rospy.loginfo(rb_pose)
			pub.publish(rb_pose)
			rospy.sleep(0.5)
		except (tf.LookupException, tf.ConnectivityException): pass





	
if __name__ == '__main__':
	publisher()

