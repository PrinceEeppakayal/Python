
#INFO: It is a function is used to generate a sequence of numbers. It is used in for loop. 

#CONSIDER:    start, stop, step_size       
for i in range(  1 ,  10 ,  2 ):
    print(i)

#INFO: start is the starting number of the sequence.
#INFO: stop is the number before which the sequence stops.
#INFO: step_size is the difference between the numbers in the sequence.


#INFO: for-else loop: The else part runs if the loop exhausts.
for i in range(5):
    print(i)
else:
    print("Loop completed")

#INFO: break statement: Is used to come out of the loop when encountered.
for i in range(5):
    if i == 3:
        break
    print(i)

#INFO: continue statement: It used is stops the current iteration of the loop and moves to the next iteration.
for i in range(5):
    if i == 3:
        continue
    print(i)

#INFO: pass statement: It is a null statement it does nothing and is used as a placeholder.
for i in range(5):
    if i == 3:
        pass
    print(i)

    