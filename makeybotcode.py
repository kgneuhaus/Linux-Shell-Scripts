#Raspberry Pi Global Setting
from gpiozero import LED
from gpiozero import PWMLED
from gpiozero import Servo
from time import sleep

# Debug Settings
debug_messages = 1 # If debug messages is 1 then message will be printed, else if 0 they will be silenced
if debug_messages : print("Debug Message are 'ON'")
else : print("Debug Message are 'OFF'")

warning_messages = 1 # If debug messages is 1 then message will be printed, else if 0 they will be silenced
if warning_messages : print("Warning Message are 'ON'")
else : print("Warning Message are 'OFF'")
# Raspberry Pi Pins
r_red_pwm_pin = PWMLED(5)
r_green_pwm_pin = PWMLED(15)
r_blue_pwm_pin = PWMLED(18)

l_red_pwm_pin = PWMLED(27)
l_green_pwm_pin = PWMLED(22)
l_blue_pwm_pin = PWMLED(23)

red_led = LED(3)
yellow_led = LED(4)
green_led = LED(17)

#wave_servo = Servo(14)
myCorrection = 0.45
maxPW = (2.0 + myCorrection)/1000
minPW = (1.0 - myCorrection +0.25)/1000
wave_servo = Servo(14, min_pulse_width = minPW, max_pulse_width = maxPW)

#print(dir(r_red_pwm_pin))

def stop_light(traffic):
    if debug_messages : print("Running stop_light function")
    if debug_messages : print(traffic)
    red,yellow,green = traffic
    if debug_messages : print(traffic[red])

def eyes_RGB(eyes):
    if debug_messages : print("Running eyes_RGB function")
    if debug_messages : print(eyes)
       
    left_eye, right_eye = eyes
    if debug_messages : print(left_eye)
    if debug_messages : print(right_eye)
    
def wave(wave_data):
    print(dir(wave_servo))
    while True:
        servo.mid()
        print("mid")
        sleep(0.5)
        servo.min()
        print("min")
        sleep(1)
        servo.mid()
        print("mid")
        sleep(0.5)
        servo.max()
        print("max")
        sleep(1)
        servo.mid()
        print("mid")
        sleep(0.5)
        servo.min()
        print("min")
        sleep(1)
def servo_pos(pos):
    print(pos)
    wave.value = pos
    print("pos =", arm.value)
    sleep(0.5)
    arm.detach()
   
def get_robot_feature_data():
    if debug_messages : print("Runninng get_robot_feature_data function")
    right_eye = {'leye_red_RGBLED':.44, 'leye_green_RGBLED':.5, 'leye_blue_RGBLED':.99}
    left_eye =  {'reye_red_RGBLED':1, 'reye_green_RGBLED':.5, 'reye_blue_RGBLED':.99}
    stop_light = {'red_LED':1, 'yellow_LED':0, 'green_LED':0}
    
    # servo
    rfd = [stop_light, left_eye, right_eye]
    if debug_messages : print(rfd)
    if debug_messages : print("Returning get_robot_feature_data function")
    return(rfd)

def main():
    print("Welcome To The STEAM Clown Makey Bot")
    if debug_messages : print("Calling get_robot_feature_data function")
#    robot_features = get_robot_feature_data()
    stop_light_LEDs, left_RGB, right_RGB = get_robot_feature_data()
    if debug_messages : print(stop_light_LEDs)
    if debug_messages : print(left_RGB)
    if debug_messages : print(right_RGB)

    if debug_messages : print("Calling stop_light function")
    stop_light(stop_light_LEDs)
    if debug_messages : print("Returned from stop_light function")

    if debug_messages : print("Calling eyes_RGB function")
    eyes_RGB([left_RGB,right_RGB])
    if debug_messages : print("Returned from eyes_RGB function")
    
    if debug_messages : print("Calling servo wave function")
    wave(wave_data)
    if debug_messages : print("Returned from servo wave function")
    

main()
