file = open("(FILE NAME)", "r")
Curr_santa_X = 0
Curr_santa_Y = 0
Curr_rsanta_X = 0
Curr_rsanta_Y = 0
Uni_house = ["0T0"]
Uni_house_count = 1
Santa_counter = 1
Rsanta_counter = 0
D_santa_counter = 0
D_rsanta_counter = 0
Sequence = (file.read())
print(Sequence)
for item in Sequence:
    if D_santa_counter == 1:
        Rsanta_counter += 2
        D_santa_counter = 0
    if D_rsanta_counter == 1:
        Santa_counter += 2
        D_rsanta_counter = 0
    if Santa_counter > Rsanta_counter:
        if item == "^":
            Curr_santa_Y += 1
        if item == "v":
            Curr_santa_Y += -1
        if item == ">":
            Curr_santa_X += 1
        if item == "<":
            Curr_santa_X += -1
        Curr_sPos = str(Curr_santa_X) + "T" + str(Curr_santa_Y)
        print("S" + Curr_sPos)
        if Curr_sPos not in Uni_house:
            Uni_house.append(Curr_sPos)
            Uni_house_count += 1
        D_santa_counter += 1
    if Santa_counter < Rsanta_counter:
        if item == "^":
            Curr_rsanta_Y += 1
        if item == "v":
            Curr_rsanta_Y += -1
        if item == ">":
            Curr_rsanta_X += 1
        if item == "<":
            Curr_rsanta_X += -1
        Curr_rsPos = str(Curr_rsanta_X) + "T" + str(Curr_rsanta_Y)
        print("R" + Curr_rsPos)
        if Curr_rsPos not in Uni_house:
            Uni_house.append(Curr_rsPos)
            Uni_house_count += 1
        D_rsanta_counter += 1
print(Uni_house_count)
