all=input("How many decks of playing cards do you want?""(1-3)")
if int(all) not in range(1,4):
    exit("input wrong")
else:
    user=input("dealer and player what do you want?(p or d)").lower()
    if user == "d" or user == "p":
        n_user=input("how many user you want fight?")
        if n_user.isdecimal:
            name=input("do you want a name or just random?")
            # level=input("wWhat level do you want to challenge? we have low,media and high ")
        else:
            exit("input wrong need decimal")
    else:
        exit("input wrong")
