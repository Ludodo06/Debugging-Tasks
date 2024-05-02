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
    if current_step == 14: pivot_left()
    if current_step == 15: go_forward()
    if current_step == 16: pivot_right()
    if current_step == 17: go_forward()
    if current_step == 18: pivot_left()
    if current_step == 19: go_forward()
    if current_step == 20: pivot_left()
    if current_step == 21: go_forward()
    if current_step == 22: stop()
    
    
    
    
    
    
# ---------------------------- #  
# ---------------------------- #  
# ---------------------------- #  
# ---------------------------- #    
# DO NOT MODIFY THE CODE BELOW #
    current_step += 1

timer_period[0] = 100
current_step = 0

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
    
# DO NOT MODIFY THE CODE ABOVE #
# ---------------------------- #  
# ---------------------------- #  
# ---------------------------- #  
# ---------------------------- #  
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
# ------------------------------------------------------------- #
# ------------------------------------------------------------- #
# ------------------------------------------------------------- #
# ------------------------------------------------------------- #
# ------------------------------------------------------------- #
# ---------------- DONT TOUCH - USED FOR LOGS ----------------- #



print(" --- Start of the program Sol_TheLabyrinth.py --- ")
        
# To avoid flood, can print once every second if manipulated
can_print_acc = True
can_print_mot = True

@onevent
def timer1():
    global can_print_acc, can_print_mot
    can_print_acc = True
    can_print_mot = True
    timer_period[1] = 0
        
left_last = 0
right_last = 0

@onevent
def acc():
    global left_last, right_last, can_print_acc, can_print_mot, timer_period
    
    # If the motors' speed changes
    if left_last != motor_left_target or right_last != motor_right_target:
        
        # Update and print the new target
        left_last = motor_left_target
        right_last = motor_right_target
        print("New target speed:\tleft", left_last, "\tright", right_last)
        can_print_mot = False
        can_print_acc = False
        timer_period[1] = 400
        
    # Check the acc to see if Thymio is manipulated
    elif (acc[0]*acc[0] > 9 or acc[1]*acc[1] > 36) and (left_last !=0 or right_last !=0) and can_print_acc:
        print("Thymio manipulated: \tx", acc[0], "\t\ty", acc[1], "\t\tz", acc[2])
        can_print_acc = False
        timer_period[1] = 1000
        
    # Be less indulgent for the thresholds if Thymio is not supposed to move    
    if (acc[2]-20)*(acc[2]-20) > 9  and (left_last == 0 or right_last == 0) and can_print_acc:
        print("Thymio manipulated: \tx", acc[0], "\t\ty", acc[1], "\t\tz", acc[2])
        can_print_acc = False
        timer_period[1] = 1000
        
    # Check if he manipulates the wheels
    if ((left_last == 0 and motor_left_speed*motor_left_speed > 121) or (right_last == 0 and motor_right_speed*motor_right_speed > 121)) and can_print_mot:
        print("Wheels manipulated: \tleft", motor_left_speed, "\tright", motor_right_speed)
        can_print_mot = False
        timer_period[1] = 1000
        
# Button prints
@onevent
def button_center():   print("Button pressed: \tbutton_center")
@onevent
def button_forward():  print("Button pressed: \tbutton_forward")
@onevent
def button_left():     print("Button pressed: \tbutton_left")
@onevent
def button_right():    print("Button pressed: \tbutton_right")
@onevent
def button_backward(): print("Button pressed: \tbutton_backward")
