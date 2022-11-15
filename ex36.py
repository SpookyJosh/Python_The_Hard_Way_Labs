from sys import exit

def left():
    print("> You reach for the left cupboard")
    print("> You reach around, you feel a plastic container and a glass jar")
    print("> Which will you choose? The container or the jar?")
    choice=input("> ")

    if choice=='jar':
        print("> You get a jar full of raisins")
        exit(0)
    elif choice=='container':
        print("> Congrats, you got a container full of cookies")
        exit(0)
    else:
        none()
def right():
    print("> You reach for the right cupboard")
    print("> You feel a bag and a box, which do you grab?")
    choice=input("> ")

    if choice=='bag':
        print("> You got a bag of wheat thins")
        exit(0)
    elif choice=='box':
        print("> congrats you got a bag of scooby doo fruit snacks")
        exit(0)
    else:
        none()
def none():
    print("> Sorry bud, you ain't gettin no snacks today")

def start():
    print("> You walk into the kitchen")
    print("> Your tummy is grumbling")
    print("> You are so hungry you could eat a horse")
    print("> There are two cupboards, one to the left and one to the right")
    print("> Select either the left or the right cupboard")

    mylist=['right','left','neither']
    choice=input(f"> Your options are {mylist[0]}, {mylist[1]}, and {mylist[2]}. Make a choice: ")

    if choice=='left':
        print("> looks like you chose the left cupboard")
        left()

    elif choice=='right':
        print("> looks like you chose the right cupboard")
        right()
    else:
        print("> You chose neither, goodbye")
        exit(0)
start()
