motor_left_target = 255
motor_right_target = 255

@onevent
def prox():
    global prox_horizontal, motor_left_target, motor_right_target
    
    nf_leds_top(32,16,0) # Orange
    
    if prox_horizontal[3] > 2500:
        nf_leds_top(0,32,0) # Green
        motor_left_target = -255
        motor_right_target = -255
        
    elif prox_horizontal[6] > 2500:
        nf_leds_top(32,0,0) # Red
        motor_left_target = 255
        motor_right_target = 255