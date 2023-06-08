#!/bin/bash

rosservice call /red/mavros/cmd/command "{broadcast: false, command: 511, confirmation: 0, param1: 30, param2: 5000, param3: 0.0, param4: 0.0, param5: 0.0, param6: 0.0, param7: 0.0}"
sleep 5
rosservice call /red/mavros/cmd/command "{broadcast: false, command: 511, confirmation: 0, param1: 27, param2: 5000, param3: 0.0, param4: 0.0, param5: 0.0, param6: 0.0, param7: 0.0}"

