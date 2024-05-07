@onevent
def acc():
    print(acc[0],acc[1],acc[2])
    print(prox_ground_delta[0], prox_ground_delta[1])
    
go = False
@onevent
def button_forward():
    global motor_right_target, motor_left_target
    
    if button_forward:
        go = not go
    
    if go:
        motor_left_target = 200
        motor_right_target = 200
        
    else:
        motor_left_target = 0
        motor_right_target = 0