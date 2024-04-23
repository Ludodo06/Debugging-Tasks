# Changez la couleur des LEDS en utilisant le format RGB (de 0 à 32)
nf_leds_top(12,4,32)



































# ------------------------------------------------------------- #
# ------------------------------------------------------------- #
# ------------------------------------------------------------- #
# ------------------------------------------------------------- #
# ------------------------------------------------------------- #
# ---------------- DONT TOUCH - USED FOR LOGS ----------------- #



print(" --- Start of the program leds.py --- ")
        
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





























