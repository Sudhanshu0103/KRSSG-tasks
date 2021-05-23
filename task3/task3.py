import numpy
import math
import cv2
import random

# reading image in greyscale form
img = cv2.imread('task_rrt_star_connect.png',cv2.IMREAD_GRAYSCALE)

h , b = img.shape
for i in range(h):
    for j in range(b):
        if ( img[i][j] > 127 ):
            img[i][j] = 255
        else:
            img[i][j] = 0

#taking the fixed value to move to new node
d = 1

# t1x and t1y are the x and y co ordinates of the tree from initial node and t2 is tree from target node with same conventions as of t1
t1x =[47]
t1y =[38]
t2x =[510]
t2y =[481]

distance_tree = [0]

# function to generate random point on image
def generate_rand():
    x_rand = random.randint(0,b+1)
    y_rand = random.randint(0,h+1)
    check_nearest( x_rand ,y_rand)


# comparing distance of new node from nearest node and our fixed distance
def check_distance(x_node, y_node ,x_rand , y_rand):
    distance = math.sqrt( (x_node-x_rand)**2 + (y_node - y_rand)**2 )
    return distance

# function to find the nearest node on tree from random point
def check_nearest(x_rand ,y_rand):
    min = 1000000
    for i in range(len(t1x)):
        distance = check_distance(t1x[i] , t1y[i] ,x_rand ,y_rand)
        if distance < min:
            min = distance
            x_nearest = t1x[i]
            y_nearest = t1y[i]
            new_node(distance,x_rand,y_rand,x_nearest, y_nearest)

# checking if new node to is found
def new_node(distance,x_rand , y_rand ,x_nearest ,y_nearest):
    if (d < distance):
        x_new = int((d*(x_rand) + (distance-d)*(x_nearest))/distance)
        y_new = int((d*(x_rand) + (distance-d)*(x_nearest))/distance)
    else:
        x_new = x_rand
        y_new = y_rand
    check_if_valid_node(x_new ,  y_new ,x_nearest ,y_nearest)

# checking if new node is valid
def check_if_valid_node(x_new ,y_new,x_nearest,y_nearest ):
    if (img[x_new][y_new] == 255):
        pass
    else:
        t1x.append(x_new)
        t1y.append(y_new)
        total_distance(x_new ,y_new ,x_nearest ,y_nearest)

# getting distance to the corresponding node
def total_distance(x_new ,y_new ,x_nearest ,y_nearest):
    distance = math.sqrt( (x_new - x_nearest)**2 + (y_new - y_nearest)**2 )
    distance_tree.append(distance)





