"""Description."""
import time

from hitbot_interface import HitbotInterface

robot_id = 123
robot = HitbotInterface(robot_id)
robot.net_port_initial()

time.sleep(1)
is_connected = robot.is_connect()
print('Connection: ', is_connected)

if is_connected == 1:  # success

    print('Robot connected.')

    # initialize the robot
    init = robot.initial(1, 1000)

    if init == 1:
        print('Robot initialized.')
        while True:
            robot.unlock_position()
            robot.new_movej_angle(0, 0, 0, 0, 50, 0)
            robot.wait_stop()
            robot.movej_xyz_lr(30, 60, 0, 0, 50, 0, 1)
            robot.wait_stop()
            robot.new_movej_angle(0, 60, 0, 0, 50, 0)
            robot.wait_stop()
            robot.movel_xyz(30, -50, 0, 0, 50)
            robot.wait_stop()
            print('run finsh')
            time.sleep(1)
    else:
        raise RuntimeError('Not initialized!!!')
else:
    raise RuntimeError('No robot connection!!!')
