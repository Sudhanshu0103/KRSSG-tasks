t = int(input())

state = 0

cars = [0]*8
steps = 1

def get_signal(cars):
    """
    - select the lane with max number of cars for the first car
    - after that, select the lane which is compatible and has max cars
    """

    car_1_idx = cars.index(max(cars))

    poss_values = []
    if (car_1_idx % 2 == 0 and (car_1_idx == 0 or car_1_idx == 4 )):
        poss_values = [1, 2, 7]
    elif (car_1_idx % 2 == 0 and (car_1_idx == 2 or car_1_idx == 6 )):
        poss_values = [1,-2, 3]
    elif (car_1_idx % 2 == 1 and (car_1_idx == 1 or car_1_idx == 5 )):
        poss_values = [1,-2, 3]
    else:
        poss_values = [-1, -2, 3]
    
    poss_nex_car_idx = [(car_1_idx + val + 8)%8 for val in poss_values]

    max_cars = 0
    max_idx = 0

    for idx in poss_nex_car_idx:
        if cars[idx] > max_cars:
            max_cars = cars[idx]
            max_idx = idx

    car_2_idx = max_idx 

    signal = 1 << car_1_idx
    if cars[car_2_idx] > 0:
        signal |= (1 << car_2_idx)

    return signal

for tcount in range(t):
    #getting current state before step
    for i in range(len(cars)):
        if (cars[i] > 0):
            state |= (1 << i)
    #taking input string of new cars
    str_inp = str(input("enter input :"))
    print(str_inp)
    
    int_inp = int(str_inp, 2)
    print(int_inp)
    if tcount == 0:
        state = int_inp 
    else:
        state = state | int_inp 
    print("input: ", str_inp)
    #printing the step number
    print("step-",steps)
    # updating cars waiting list before step
    cars = [cars[i] + int(str_inp[i]) for i in range(8)]
    print("cars after input and before step: ", cars)

    signal = get_signal(cars)

    print("signal: ", str('{0:08b}'.format(signal))[::-1])

    # update state after step
    state = state & (~signal)
    for i in range(8):
        if signal & (1 << i) and cars[i]>0:
            cars[i] -= 1
    #printing cars list after step done
    print("cars after signal given: ", cars)
    #increment step count
    steps += 1
    print("")

print("")
print("INPUT DONEE....") 
print("")

while sum(cars) > 0:
    #printing the step number
    print("step-",steps)
    #initial cars waiting queue before step done
    print("cars before signal: ", cars)

    #getting current state before step
    for i in range(len(cars)):
        if (cars[i] > 0):
            state |= (1 << i)
    #getting signal for the step
    signal = get_signal(cars)
    print("signal: ", str('{0:08b}'.format(signal))[::-1])

    # update state after step done
    state = state & (~signal)
    for i in range(8):
        if signal & (1 << i) and cars[i]>0:
            cars[i] -= 1
    #final cars waiting queue after step done
    print("cars after signal: ", cars)
    #increment step count
    steps += 1
    print("")

