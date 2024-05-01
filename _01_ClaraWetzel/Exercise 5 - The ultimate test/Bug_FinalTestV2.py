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

        motor_left_target = 200 + steer
        motor_right_target = 200 - steer
        
        if prox_ground_delta[0] > 800 or prox_ground_delta[1] > 800: # left: 0, right: 1
            mode = LINE
            
    if mode == LINE:
        nf_leds_top(0,0,32) # Blue
        steer = (prox_ground_delta[0] - prox_ground_delta[1])//8          # left: 0, right: 1
        
        motor_left_target = 200 - steer
        motor_right_target = 200 + steer
    
    if mode == STOP:
        nf_leds_top(0,32,0) # Green
        motor_left_target = 0
        motor_right_target = 0
            
@onevent
def buttons():
    global motor_left_target, motor_right_target, mode
    if button_center:
        motor_left_target = 0
        motor_right_target = 0
 































# ------------------------------------------------------------- #
# ------------------------------------------------------------- #
# ------------------------------------------------------------- #
# ------------------------------------------------------------- #
# ------------------------------------------------------------- #
# ---------------- DONT TOUCH - USED FOR LOGS ----------------- #



print(" --- Start of the program Bug_FinalTestV2.py --- ")
        
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
        print("LOGS: Wheels ,", left_last, ",", right_last)
        can_print_mot = False
        can_print_acc = False
        timer_period[1] = 400
        
    # Check the acc to see if Thymio is manipulated
    elif (acc[0]*acc[0] > 9 or acc[1]*acc[1] > 36) and (left_last !=0 or right_last !=0) and can_print_acc:
        print("LOGS: Acc ,", acc[0], ",", acc[1], ",", acc[2])
        can_print_acc = False
        timer_period[1] = 1000
        
    # Be less indulgent for the thresholds if Thymio is not supposed to move    
    if (acc[2]-20)*(acc[2]-20) > 9  and (left_last == 0 or right_last == 0) and can_print_acc:
        print("LOGS: Acc ,", acc[0], ",", acc[1], ",", acc[2])
        can_print_acc = False
        timer_period[1] = 1000
        
# Button prints
@onevent
def button_center():
    if button_center: print("LOGS: center , pressed")
    else:            print ("LOGS: center , released")
@onevent
def button_left():
    if button_left: print("LOGS: left , pressed")
    else:            print ("LOGS: left , released")
@onevent
def button_right():
    if button_right: print("LOGS: right , pressed")
    else:            print ("LOGS: right , released")
@onevent
def button_forward():
    if button_forward: print("LOGS: forward , pressed")
    else:            print ("LOGS: forward , released")
@onevent
def button_backward():
    if button_backward: print("LOGS: backward , pressed")
    else:            print ("LOGS: backward , released")