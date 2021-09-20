#print("Choose from the 6 different areas of the goal to shoot at")
#position = input("choose a number from 1 to 6 to aim at that postion of the goal ")

shot = 6
while  str(shot).isnumeric():
    if int(shot)>=1 and int(shot)<=6:
       print("1. top right \n"
             "2. top left \n"
             "3. top middle \n"
             "4. bottom middle \n"
             "5. top left \n"
             "6. bottom right \n")
       shot = input("choose a number from 1 to 6 to aim at that postion of the goal ")
