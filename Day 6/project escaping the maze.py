#https://reeborg.ca/reeborg.html?lang=en&mode=python&menu=worlds%2Fmenus%2Freeborg_intro_en.json&name=Maze&url=worlds%2Ftutorial_en%2Fmaze1.json
while not at_goal():
    if right_is_clear():
          turn_right()
          move()
    elif front_is_clear():
        move()
    else:
        turn_left()

    #debugging the edge case
while front_is_clear():
    move()
turn_left()
        
while not at_goal():
    if right_is_clear():
          turn_right()
          move()
    elif front_is_clear():
        move()
    else:
        turn_left()