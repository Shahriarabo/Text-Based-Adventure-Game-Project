ans = input("Do you want to play this game ? [yes/no] : ")

if ans == "yes":
    print("Welcome to play this Game ")
    ans = input("Do you want to visit jungle/cave ? [jungle/cave] : ")
    if ans == "jungle":
        ans= input("You see Tirger 🐅🐅🐅,Do you want to Fight 🥷🥷🥷 with tiger or run away 🏃‍♂️🏃‍♂️🏃‍♂️ [fight/run] : ")
        if ans == "fight":
            print("The Tiger eat him 🍴🍴🍴and The Game is finished !")
        else:
            print("He save your Life ✌️✌️🫶 and The Game is finished !")

    else:
        ans = input("You see Bear 🐻🐻🐻,Do you want to Fight 🥷🥷🥷with tiger or run away 🏃‍♂️🏃‍♂️🏃‍♂️[fight/run] : ")
        if ans == "fight":
            print("The Bear kil him 🚑🚑🚑 and The Game is finished !")
        else:
            print("He save your Life ✌️✌️🫶 and The Game is finished !")

else:
    print("The Game is finished ! 🖐️🖐️🖐️")