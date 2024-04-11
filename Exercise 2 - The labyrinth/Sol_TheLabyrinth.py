# DO NOT MODIFY THE CODE BELOW, GO DIRECTLY TO LINE 24
def go_forward():
    global motor_left_target, motor_right_target, timer_period
    timer_period[0] = 2500
    nf_leds_top(0,32,0)
    motor_left_target = 300
    motor_right_target = 300
    
def pivot_left():
    global motor_left_target, motor_right_target, timer_period
    timer_period[0] = 1500
    nf_leds_top(32,16,0)
    motor_left_target = -150
    motor_right_target = 150
    
def pivot_right():
    global motor_left_target, motor_right_target, timer_period
    timer_period[0] = 1500
    nf_leds_top(32,16,0)
    motor_left_target = 150
    motor_right_target = -150
    
def stop():
    global motor_left_target, motor_right_target
    nf_leds_top(0,0,0)
    motor_left_target = 0
    motor_right_target = 0
# DO NOT MODIFY THE CODE ABOVE


timer_period[0] = 100 #[ms] : Start the path immediatly
current_step = 0

@onevent
def timer0():
    global current_step
    if current_step == 0: go_forward()
    if current_step == 1: pivot_right()
    if current_step == 2: go_forward()
    if current_step == 3: pivot_right()
    if current_step == 4: go_forward()
    if current_step == 5: pivot_left()
    if current_step == 6: go_forward()
    if current_step == 7: go_forward()
    if current_step == 8: pivot_left()
    if current_step == 9: go_forward()
    if current_step == 10: pivot_left()
    if current_step == 11: go_forward()
    if current_step == 12: pivot_right()
    if current_step == 13: go_forward()
    if current_step == 14: pivot_left()  # modify here
    if current_step == 15: go_forward()
    if current_step == 16: pivot_right()
    if current_step == 17: go_forward()
    if current_step == 18: pivot_left()
    if current_step == 19: go_forward()
    if current_step == 20: pivot_left()
    if current_step == 21: go_forward()
    if current_step == 22: stop()
    current_step += 1