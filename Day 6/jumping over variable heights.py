#https://reeborg.ca/reeborg.html?lang=en&mode=python&menu=worlds%2Fmenus%2Freeborg_intro_en.json&name=Hurdle%204&url=worlds%2Ftutorial_en%2Fhurdle4.json
def jump_hurdles():
    turn_left()
    while wall_on_rigjt():
        move()
    turn_right()
    move()
    turn_right()
    while front_is_clear():
        move()
        
        
        
while not at_goal():
    if wall_in_front():
        jump_hurdles()  
    else:
        move()