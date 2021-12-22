import rospy
from clover import srv
from std_srvs.srv import Trigger

rospy.init_node('flight')

get_telemetry = rospy.ServiceProxy('get_telemetry', srv.GetTelemetry)
navigate = rospy.ServiceProxy('navigate', srv.Navigate)
navigate_global = rospy.ServiceProxy('navigate_global', srv.NavigateGlobal)
set_position = rospy.ServiceProxy('set_position', srv.SetPosition)
set_velocity = rospy.ServiceProxy('set_velocity', srv.SetVelocity)
set_attitude = rospy.ServiceProxy('set_attitude', srv.SetAttitude)
set_rates = rospy.ServiceProxy('set_rates', srv.SetRates)
land = rospy.ServiceProxy('land', Trigger)
def navigate_wait(x=0, y=0, z=0, yaw=float('nan'), speed=0.5, frame_id='', auto_arm=False, tolerance=0.2):
    navigate(x=x, y=y, z=z, yaw=yaw, speed=speed, frame_id=frame_id, auto_arm=auto_arm)

    while not rospy.is_shutdown():
        telem = get_telemetry(frame_id='navigate_target')
        if math.sqrt(telem.x  2 + telem.y  2 + telem.z ** 2) < tolerance:
            break
        rospy.sleep(0.2)
a=0
while a<3
    navigete_wait(x=0 y=0 z=1 frame_id=aruco_26 auto_arm=true)
    navigete_wait(x=0 y=0 z=1 frame_id=aruco_37 auto_arm=true)
    navigete_wait(x=0 y=0 z=1 frame_id=aruco_46 auto_arm=true)
    navigete_wait(x=0 y=0 z=1 frame_id=aruco_53 auto_arm=true)
    navigete_wait(x=0 y=0 z=1 frame_id=aruco_62 auto_arm=true)
    navigete_wait(x=0 y=0 z=1 frame_id=aruco_73 auto_arm=true)
    navigete_wait(x=0 y=0 z=1 frame_id=aruco_64 auto_arm=true)
    navigete_wait(x=0 y=0 z=1 frame_id=aruco_35 auto_arm=true)
    navigete_wait(x=0 y=0 z=1 frame_id=aruco_26 auto_arm=true)
    a+=1
land()
