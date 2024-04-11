forward_time = 7800
turn_time = 1100
timer_period[0] = 100
going_forward = False


@onevent
def timer0():
    global leds_top, going_forward, motor_left_target, motor_right_target
    going_forward = not going_forward
    if going_forward:
        timer_period[0] = forward_time
        nf_leds_top(0,32,0) # Green
        motor_right_target = 250
        motor_left_target = 250
    else:
        timer_period[0] = turn_time
        nf_leds_top(32,16,0) # Orange
        motor_right_target = 200
        motor_left_target = 200
        

