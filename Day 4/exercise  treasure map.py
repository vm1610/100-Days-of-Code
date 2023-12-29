row1 = ["⬜️","️⬜️","️⬜️"]
row2 = ["⬜️","⬜️","️⬜️"]
row3 = ["⬜️️","⬜️️","⬜️️"]
map=[row1,row2,row3]
print(f"{row1}\n{row2}\n{row3}")
position=input("where do u want to put the treasurwe?")
map[int(position[0])-1][int(position[1])-1]="X"
print(f"{row1}\n{row2}\n{row3}")