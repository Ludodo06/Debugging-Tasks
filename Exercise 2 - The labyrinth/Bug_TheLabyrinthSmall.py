# DO NOT MODIFY THE CODE BELOW, GO DIRECTLY TO LINE 24
def go_forward():
    global motor_left_target, motor_right_target, timer_period
    timer_period[0] = 2100
    nf_leds_top(0,32,0)
    motor_left_target = 300
    motor_right_target = 300
    
def pivot_left():
    global motor_left_target, motor_right_target, timer_period
    timer_period[0] = 1480
    nf_leds_top(32,16,0)
    motor_left_target = -150
    motor_right_target = 150
    
def pivot_right():
    global motor_left_target, motor_right_target, timer_period
    timer_period[0] = 1480
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
current_step = 1

@onevent
def timer0():
    global current_step
    if current_step == 1: go_forward()
    if current_step == 2: pivot_right()
    if current_step == 3: go_forward()
    if current_step == 4: pivot_right()
    if current_step == 5: go_forward()
    if current_step == 6: pivot_left()
    if current_step == 7: go_forward()
    if current_step == 8: pivot_right()
    if current_step == 9: go_forward()
    if current_step = 10: stop()
    current_step += 1
