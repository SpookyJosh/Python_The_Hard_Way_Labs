def left():

def right():


def start():
    print("You walk into the kitchen")
    print("Your tummy is grumbling")
    print("You are so hungry you could eat a horse")
    print("There are two cupboards, one to the left and one to the right")
    print("Select either the left or the right cupboard")
    
    choice=input("> ")

    if choice=='left':
        print("looks like you chose the left cupboard")
        left()

    elif choice=='right':
        print("looks like you chose the right cupboard")
        right()
    else:
        print("You are directionally challenged, no snack for you")
        exit(0)
start()
