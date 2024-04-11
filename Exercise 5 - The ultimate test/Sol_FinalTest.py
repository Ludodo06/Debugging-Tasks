# Constants
SENSORS = 0
LINE = 1
STOP = 2
SPEED = 200
PROX_LEFT = 0
PROX_RIGHT = 4
PROX_FRONT = 2
GROUND_LEFT = 0
GROUND_RIGHT = 1
SENSOR_DIV = 20
MIN_GROUND = 200

# Start
mode = SENSORS

@onevent
def prox():
    global mode, motor_left_target, motor_right_target
    
    if mode == SENSORS:
        steer = (prox_horizontal[PROX_LEFT] - prox_horizontal[PROX_RIGHT])//SENSOR_DIV
        nf_leds_top(32,0,0) # Red
        
        if prox_ground_delta[GROUND_LEFT] < MIN_GROUND or prox_ground_delta[GROUND_RIGHT] < MIN_GROUND:
            mode = LINE
    
    if mode == LINE:
        steer = prox_ground_delta[GROUND_LEFT] - prox_ground_delta[GROUND_RIGHT]
        nf_leds_top(0,0,32) # Blue
    
    motor_left_target = SPEED + steer
    motor_right_target = SPEED - steer
    
    if mode == STOP:
        nf_leds_top(0,32,0) # Green
        motor_left_target = 0
        motor_right_target = 0
            
@onevent
def buttons():
    global mode, motor_left_target, motor_right_target
    if button_center:
        motor_left_target = 0
        motor_right_target = 0
        mode = STOP
 


