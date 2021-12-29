Sequence = input("Input Sequence: ")
CurrentFloor = 0
CurrentIndex = 1
for Item in Sequence:
    if Item == "(":
        CurrentFloor += 1
    if Item == ")":
        CurrentFloor -= 1
    if CurrentFloor == -1:
        print(CurrentIndex)
        break
    CurrentIndex += 1
