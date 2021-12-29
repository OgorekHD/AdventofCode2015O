file = open("(FILE NAME)", "r")
Curr_X = 0
Curr_Y = 0
Uni_house = ["0T0"]
Uni_house_count = 1
Sequence = file.read()
for item in Sequence:
    if item == "^":
        Curr_Y += 1
    if item == "v":
        Curr_Y += -1
    if item == ">":
        Curr_X += 1
    if item == "<":
        Curr_X += -1
    Curr_Pos = str(Curr_X) + "T" + str(Curr_Y)
    if Curr_Pos not in Uni_house:
        Uni_house.append(Curr_Pos)
        Uni_house_count += 1
print(Uni_house_count)
