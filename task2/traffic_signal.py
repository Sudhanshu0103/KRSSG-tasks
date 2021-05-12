

#take number of input new cars array as input fron user
t = int(input("enter no. of input arrays of new cars :"))

#initialise cars waiting list  elements to zero
cars_waiting = [0 for i in range(8)]
print(cars_waiting)

#initialise new cars array to zero as well
new_cars = [0 for i in range(8)]
#variable to store number of steps done
steps = 0

#function to take input of new cars from user and update the cars waiting list
def input_func(steps):
    input_string = input('Enter 8 elements of the new cars list separated by space ')
    print("\n")
    new_cars = input_string.split()

    # print list
    print('new cars list: ', new_cars)

    # convert each item to int type
    for i in range(len(new_cars)):
    # convert each item to int type
      new_cars[i] = int(new_cars[i])
    print(new_cars)

    #updating cars waiting list
    for i in range(len(new_cars)):
        cars_waiting[i] += new_cars[i]

#function to give particular side straight and right both green
def straightAndright(steps,alphabet,straight,right):
    print("step-",steps)
    #decreasing elements of corresponding lights by one
    cars_waiting[straight] -= 1
    cars_waiting[right] -= 1
    print(alphabet,"-go straight, go right ")


#function to give right green to opposites
def opposites_right(steps, alphabet1 , alphabet2,right1 ,right2):
    print("step-",steps)
    #decreasing elements of corresponding lights by one
    cars_waiting[right1] -= 1
    cars_waiting[right2] -= 1
    #printing which lights to keep on
    print(alphabet1,"-go right, ",alphabet2,"-go right")
    
#function to give one side right and another straight green
def one_straight_right(steps,alphabet1 ,alphabet2 ,straight ,right):
    print("step-",steps)
    #decreasing elements of corresponding lights by one
    cars_waiting[straight] -= 1
    cars_waiting[right] -= 1
    #printing which lights to keep on
    print(alphabet1,"-go right ,",alphabet2,"-go straight")

def opposites_straight(steps,alphabet1,alphabet2 ,straight1 ,straight2):
    print("step-",steps)
    #decreasing elements of corresponding lights by one
    cars_waiting[straight1] -= 1
    cars_waiting[straight2] -= 1
    #printing which lights to keep on
    print(alphabet1,"-go straight ,",alphabet2,"-go straight")

def one_car(steps , alphabet ,straight ,right):
    print("step-",steps)
    if(cars_waiting[straight] > 0):
        cars_waiting[straight] -= 1
        print(alphabet,"-go straight")
    else:
        cars_waiting[right] -= 1
        print(alphabet,"-go right")



def print_initial_queue():
    #printing cars waiting queue before step done
    print("initial waiting list at this step is :",cars_waiting)

def print_final_queue():
    #printing cars waiting queue after step done
    print("final waiting list at this step :",cars_waiting)
    print("\n")

def start():
    #making value of steps global
    global steps

    while True:
        #for steps less than t take input
        if (steps < t):
            input_func(steps)
        else:
            pass
        print_initial_queue()
        #checking conditions for one straight one right for same side
        if (cars_waiting[0] > 0 and cars_waiting[1] > 0):
            straightAndright(steps,str("A"),0 ,1)
        elif (cars_waiting[2] > 0 and cars_waiting[3] > 0):
            straightAndright(steps,str("B"),2 ,3)
        elif (cars_waiting[4] > 0 and cars_waiting[5] > 0):
            straightAndright(steps,str("C"),4 ,5)
        elif (cars_waiting[6] > 0 and cars_waiting[7] > 0):
            straightAndright(steps,str("D"),6 ,7)
        #checking conditions for opposites taking right
        elif (cars_waiting[1] > 0 and cars_waiting[3] > 0):
            opposites_right(steps ,str("A"),str("B"),1 ,3)
            steps += 1
        elif (cars_waiting[5] > 0 and cars_waiting[7] > 0):
            opposites_right(steps ,str("C"),str("D"),5 ,7)
            steps += 1
        #checking conditions for one side straight another right
        elif (cars_waiting[1] > 0 and cars_waiting[4] > 0):
            one_straight_right(steps, str("A"),str("C"),1 ,4)
            steps += 1
        elif (cars_waiting[5] > 0 and cars_waiting[2] > 0):
            one_straight_right(steps, str("C"),str("B"),5 ,2)
            steps += 1
        elif (cars_waiting[3] > 0 and cars_waiting[6] > 0):
            one_straight_right(steps, str("B"),str("D"),3 ,6)
            steps += 1
        elif (cars_waiting[7] > 0 and cars_waiting[0] > 0):
            one_straight_right(steps, str("D"),str("A"),1 ,4)
            steps += 1
        #checking coditions for opposites straight green
        elif (cars_waiting[0] > 0 and cars_waiting[2] > 0):
            opposites_straight(steps ,str("A"),str("B"), 0, 2)
            steps += 1
        elif (cars_waiting[4] > 0 and cars_waiting[6] > 0):
            opposites_straight(steps ,str("C"),str("D"), 4, 6)
            steps += 1

        elif (cars_waiting[0] > 0 or cars_waiting[1] > 0):
            one_car(steps,str("A"),0 ,1)
        elif (cars_waiting[2] > 0 or cars_waiting[3] > 0):
            one_car(steps,str("B"),2 ,3)
        elif (cars_waiting[4] > 0 or cars_waiting[5] > 0):
            one_car(steps,str("C"),4 ,5)
        elif (cars_waiting[6] > 0 or cars_waiting[7] > 0):
            one_car(steps,str("D"),6 ,7)
        else:
            print(steps)
            break
        steps += 1
        print_final_queue()
        

start()
# print(cars_waiting)