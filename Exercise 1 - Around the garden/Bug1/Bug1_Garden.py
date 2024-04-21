# forward_time = 4000
# turn_time = 1100
# timer_period[0] = 10000
# going_forward = False
# 
# 
# @onevent
# def timer0():
#     global leds_top, going_forward, motor_left_target, motor_right_target
#     going_forward = not going_forward
#     if going_forward:
#         timer_period[0] = forward_time
#         nf_leds_top(0,32,0) # Green
#         motor_right_target = 200
#         motor_left_target = 200
#     else:
#         timer_period[0] = turn_time
#         nf_leds_top(32,16,0) # Orange
#         motor_right_target = 200
#         motor_left_target = -200
        
        
        
  
  
  
  
  
  
  





# ------------------------------------------------------------- #
# ------------------------------------------------------------- #
# ------------------------------------------------------------- #
# ------------------------------------------------------------- #
# ------------------------------------------------------------- #
# ---------------- DONT TOUCH - USED FOR LOGS ----------------- #



print(" --- Debut du programme --- ")
        
# To avoid flood, can print once every second if manipulated
can_print = True
def timer1():
    global can_print
    print("OKKKK")
    can_print = True
        
left_last = 0
right_last = 0

@onevent
def acc():
    global left_last, right_last, can_print
    
    # If the motors' speed changes
    if left_last != motor_left_target or right_last != motor_right_target:
        
        # Update and print the new target
        left_last = motor_left_target
        right_last = motor_right_target
        print("New speed: left=", left_last, ", right=", right_last)
        
    # Check the acc to see if Thymio is manipulated
    elif (acc[0] > 3 or acc[0] < -3 or acc[1] > 4 or acc[1] < -4) and (left_last !=0 or right_last !=0) and can_print:
        print("Thymio manipulated", acc[0], acc[1])
        can_print = False
        timer_period[1] = 1000
        
    # Be less indulgent for the thresholds if Thymio is not supposed to move    
    if (acc[0] > 3 or acc[0] < -3 or acc[1] > 3 or acc[1] < -3)  and (left_last ==0 or right_last ==0) and can_print:
        print("Thymio manipulated", acc[0], acc[1])
        can_print = False
        timer_period[1] = 1000
        

# Button prints
@onevent
def button_center():   print("Button center pressed")
@onevent
def button_forward():  print("Button forward pressed")
@onevent
def button_left():     print("Button left pressed")
@onevent
def button_right():    print("Button right pressed")
@onevent
def button_backward(): print("Button backward pressed")