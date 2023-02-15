#!/usr/bin/env python

import random
import subprocess
from gazebo_msgs.srv import DeleteModel, DeleteModelRequest

from geometry_msgs.msg import Point
from icuas23_competition.msg import poi
import rospy
import numpy as np

def construct_poi(pose):
	d = 2
	r = d*1.25
	cc_x = pose[0] + d*np.cos(pose[3])
	cc_y = pose[1] + d*np.sin(pose[3])

	z_off = 2*np.random.random()-4

	return (cc_x, cc_y, pose[2]+z_off, r)



tile_poses = [(7.56, 8.32, 9.1, 0.7854), (7.57, 14.60, 5.5, -0.7854), (3.00, 43.36, 11.1, -1.5707), (9.3, 43.36, 4.8, -1.5707), (10.36, 45.3, 3.8, 0), (10.36, 46.2, 12.1, 0), (10.36, 44.5, 8.35, 0), (16.2, 44.275, 7.3, -1.5707), (5.92, 12, 4.35, 3.1415), (6.34, 11, 4.35, 0)]

rospy.init_node('spawner_deleter')
# delete_model = rospy.ServiceProxy("/gazebo/delete_model", DeleteModel)
pub = rospy.Publisher('poi', poi, queue_size=10, latch=True)
# for i in range(5):
poses = random.sample(tile_poses, 10)

command1 = "roslaunch icuas23_competition spawn_crack.launch name:=crack_1 x:=%s y:=%s z:=%s yaw:=%s" % poses[0]
command2 = "roslaunch icuas23_competition spawn_crack.launch name:=crack_2 x:=%s y:=%s z:=%s yaw:=%s" % poses[1]
command3 = "roslaunch icuas23_competition spawn_crack.launch name:=crack_3 x:=%s y:=%s z:=%s yaw:=%s" % poses[2]
command4 = "roslaunch icuas23_competition spawn_crack.launch name:=crack_4 x:=%s y:=%s z:=%s yaw:=%s" % poses[3]
command5 = "roslaunch icuas23_competition spawn_crack.launch name:=crack_5 x:=%s y:=%s z:=%s yaw:=%s" % poses[4]
command6 = "roslaunch icuas23_competition spawn_crack.launch name:=noncrack_1 x:=%s y:=%s z:=%s yaw:=%s" % poses[5]
command7 = "roslaunch icuas23_competition spawn_crack.launch name:=noncrack_2 x:=%s y:=%s z:=%s yaw:=%s" % poses[6]
command8 = "roslaunch icuas23_competition spawn_crack.launch name:=noncrack_3 x:=%s y:=%s z:=%s yaw:=%s" % poses[7]
command9 = "roslaunch icuas23_competition spawn_crack.launch name:=noncrack_4 x:=%s y:=%s z:=%s yaw:=%s" % poses[8]
command10 = "roslaunch icuas23_competition spawn_crack.launch name:=noncrack_5 x:=%s y:=%s z:=%s yaw:=%s" % poses[9]
roslaunch = subprocess.Popen(command1.split(" "), shell=False)
rospy.sleep(2)
roslaunch = subprocess.Popen(command2.split(" "), shell=False)
rospy.sleep(2)
roslaunch = subprocess.Popen(command3.split(" "), shell=False)
rospy.sleep(2)
roslaunch = subprocess.Popen(command4.split(" "), shell=False)
rospy.sleep(2)
roslaunch = subprocess.Popen(command5.split(" "), shell=False)
rospy.sleep(2)
roslaunch = subprocess.Popen(command6.split(" "), shell=False)
rospy.sleep(2)
roslaunch = subprocess.Popen(command7.split(" "), shell=False)
rospy.sleep(2)
roslaunch = subprocess.Popen(command8.split(" "), shell=False)
rospy.sleep(2)
roslaunch = subprocess.Popen(command9.split(" "), shell=False)
rospy.sleep(2)
roslaunch = subprocess.Popen(command10.split(" "), shell=False)
rospy.sleep(2)

print("Publishing pois")

PoIArray = poi()
point_list = []
for pose in poses:
	point_of_interest = construct_poi(pose)

	msg = Point()

	msg.x = point_of_interest[0]
	msg.y = point_of_interest[1]
	msg.z = point_of_interest[2]

	point_list.append(msg)

PoIArray.poi = point_list

pub.publish(PoIArray)
rospy.sleep(5)

	# raw_input("Press enter to continue...")

	# req = DeleteModelRequest()
	# req.model_name = "crack_1"
	# delete_model.call(req)
	# req.model_name = "crack_2"
	# delete_model.call(req)
	# req.model_name = "crack_3"
	# delete_model.call(req)
	# req.model_name = "crack_4"
	# delete_model.call(req)
	# req.model_name = "crack_5"
	# delete_model.call(req)
	# req.model_name = "noncrack_1"
	# delete_model.call(req)
	# req.model_name = "noncrack_2"
	# delete_model.call(req)
	# req.model_name = "noncrack_3"
	# delete_model.call(req)
	# req.model_name = "noncrack_4"
	# delete_model.call(req)
	# req.model_name = "noncrack_5"
	# delete_model.call(req)
	# break