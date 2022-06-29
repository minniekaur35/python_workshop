# there is a circle, circle is on a square board and has a bull's eye. 
# I have a square's side. If you half its side, its going to be the center of x and y axis in the circle, where x and y meets. 
# givenn length of board = a = 6
# air speed = random (0, 2)
# player enters est. calculated center of circle = x, y
# to get bulls eye = a/2, a/2
# should be center = 3,3
# affect by air on arrow =  *
# actual because  of air  = ??
import random 
side = random.randint(5, 20)
air_speed = random.randint(1, 5)
directions = ['North', 'South', 'East', 'West']
air_direction = random.choice(directions)
print('\033[1m' + "WELCOME TO ARCHER'S ACADEMY." + '\033[0m')
print("You'll be randomnly given a side of the square board that has a circle in it. That circle will have a bull's eye, which should be your aim. Calculate the co-ordinates of the circle to hit your aim. ")
print("Good Luck!")
target = """ 
MMMWWWWWWWWXKOkkxxkkOKXWWWWWWWWMMM
MWWWWWWXOo:'..      ..':oOXWWWWWWM
WWWWN0l'.    ........    .'l0NWWWW
WWWKl.   .';clloooollc;'.   .lKWWW     Side Length
WNk'   .;loooollllllooool;.   'kNW       is  -- {side}
Wk.   ,loool::;;;;;;::loool,   .kW
K,   ,oool:;;;:cllc:;;;:looo,   ;K
x.  .lool:;;:dO0KK0Od:;;:lool.  .x     Air Speed
l   'oooc;;;o0KKKKKK0o;;;cooo'   l       is  -- {speed}
o   'oool;;;lOKKKKKKOl;;;lool'   o
O.  .:oooc;;;coxkkxoc;;;cooo:.  .O     Air Direction
Nl   .coooc:;;;;;;;;;;:loooc.   lN       is  -- {dir}
WXc.  .;looolcc::::ccloool;.  .cXW
WWXo.   .,coodoooooodooc;.   .oXWW
WWWN0c.   ..',;;;;;;,'..   .l0NWWW
WWWWWNKd:..            ..:dKNWWWWW
MMWWWWWWNKOdlc:;;;;:cldOKNWWWWWWMM
""".format(side=side, speed=air_speed, dir=air_direction)
print(target)
# print(f"The square board with bull's eye painted on it, has a side of length {side}.")


def check_target_hit(x,y):
    affect_of_air_on_x = 0
    affect_of_air_on_y = 0
    if air_direction == 'North':
        affect_of_air_on_y = air_speed
    elif air_direction == 'South':
        affect_of_air_on_y = (-air_speed)
    elif air_direction == 'East':
        affect_of_air_on_x  = air_speed
    elif air_direction == 'West':
        affect_of_air_on_x  = (-air_speed)
    arrow_hit = (float(x) - affect_of_air_on_x, float(y) - affect_of_air_on_y )
    print("Arrow hits:", arrow_hit)
    return (float(x) == side/2 + affect_of_air_on_x  and float(y) == side/2 + affect_of_air_on_y)


def oversmart_mannpreet(x,y):
    air_pressure_on_x = 0
    air_pressure_on_y = 0

    if air_direction == "North":
        air_pressure_on_y += air_speed
    if air_direction == "South":
        air_pressure_on_y -= air_speed
    if air_direction == "East":
        air_pressure_on_x += air_speed
    if air_direction == "West":
        air_pressure_on_x -= air_speed
    
    position_of_arrow = (float(x) + air_pressure_on_x , float(y) + air_pressure_on_y)
    print(position_of_arrow)

    return (side/2, side/2) == position_of_arrow

 
for _ in range(5):
    x_axis = input("Enter an x axis of bull's eye: ")
    y_axis = input("Enter a y axis of bull's eye: ")

    # if check_target_hit(x_axis, y_axis):
    if oversmart_mannpreet(x_axis, y_axis):
        print("BullsEYE!! Congrats you have won :)")
        break
    else:
        print("Dang!! you missed it buddy try again")




