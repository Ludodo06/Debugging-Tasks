min = 1000
max = 0

@onevent
def acc():
    global min, max
    min = acc[2] if acc[2] < min
    print(acc[2])
    
#motor_right_target = 200
#motor_left_target = 200
