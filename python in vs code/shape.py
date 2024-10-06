while 1 == 1:
    choice = int(input(
            "press 1 for the volume of cube \n presss 2 for the volume of cylinder \n press 3 for the volume of cone \n prss 4 for the volume of sphere "
        )
    )
    if choice == 1:
        side = int(input("enter a side"))
        volume = side * side * side
        print("volume of the cube", volume)
    elif choice == 2:
        radius = int(input("enter a radius "))
        a = radius * radius
        height = int(input("enter a height "))
        volume = 3.14 * a * height
        print("volume of cylinder", volume)
    elif choice == 3:
        radius = int(input("enter a radius "))
        a = radius * radius
        height = int(input("enter a height "))
        volume = 3.14 * a * (height / )
        print("volume of cone", volume)
    elif choice == 4:
        radius = int(input("enter a radius "))
        a = radius * radius
        height = int(input("enter a height "))
        volume = 4 / 3 * 3.14 * a
        print("volume of cylinder", volume)
    elif choice == 5:
        exit()
    else:
        print("you have enter wrong vlaue ")
