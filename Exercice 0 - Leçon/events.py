@onevent
def buttons():                                     # Triggers everytime a button is pressed
    
    global motor_left_target, motor_right_target   # Usefull to modify global variables 
    
    if button_forward:                             # If the button is pressed
        motor_left_target = 250                    # Then go forward with both wheels
        motor_right_target = 250
        
        
@onevent
def prox():                                        # Triggers everytime there's an obstacle
    
    global motor_left_target, motor_right_target   # Usefull to modify global variables
    
    if prox_horizontal[2] > 2000:                  # If an obstacle is detected in front
        motor_left_target = 0                      # Then stop the wheels
        motor_right_target = 0 