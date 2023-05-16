#!/bin/bash

export_falconb
export UAV_NAMESPACE=red
roslaunch uav_ros_gui rqt.launch perspective:=$(pwd)/challenge_layout_rw.perspective
