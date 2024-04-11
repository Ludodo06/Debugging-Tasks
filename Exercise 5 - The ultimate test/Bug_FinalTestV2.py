# Constants
WALLS = 0
LINE = 1
STOP = 2

# Start
mode = WALLS

@onevent
def prox():
    global mode, motor_left_target, motor_right_target
    
    if mode == WALLS:
        nf_leds_top(32,0,0) # Red
        steer = (prox_horizontal[0] - prox_horizontal[4])//20        # left: 0, right: 4
        
        motor_left_target = 200 - steer
        motor_right_target = 200 + steer
        
        if prox_ground_delta[0] < 800 or prox_ground_delta[1] < 800: # left: 0, right: 1
            mode = LINE
    
    if mode == LINE:
        nf_leds_top(0,0,32) # Blue
        steer = prox_ground_delta[0] - prox_ground_delta[1]          # left: 0, right: 1
        
        motor_left_target = 200 - steer
        motor_right_target = 200 + steer
    
    if mode == STOP:
        nf_leds_top(0,32,0) # Green
        motor_left_target = 0
        motor_right_target = 0
            
@onevent
def buttons():
    global motor_left_target, motor_right_target
    if button_center:
        motor_left_target = 0
        motor_right_target = 0
 

