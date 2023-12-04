#   Aiden Morrison
#   CSCI 128 – Section J
#   Assessment 5
#   References: no one
#   Time: 3 hours
def pcc(inital, lamba):  # define a function with the parameters of inital and lamba
    x = inital  # assign inital population to x
    seen = set()  # create empty set to keep track of values
    while True:  # create infinite loop
        new = lamba * x * (1 - x)  # calculate next population fraction
        new = round(new, 6)  # rounds value to 6 decimals
        if new in seen:  # checking if value has been seen before, tracking iterations
            iteration_values = []  # create empty list
            current_x = new  # assigns value to this
            while current_x not in iteration_values:  # create loop to find and store values within iteration
                iteration_values.append(current_x)  # add current value to iteration list
                current_x = round(lamba * current_x * (1 - current_x), 6)  # calculate next value and round to 6 decimals
            for val in iteration_values:  # iterate over each value in iteration
                print("OUTPUT", val)  # print each value
            return  # exit function when iteration has been printed
        seen.add(new)  # add current value to seen values
        if new == x:  # checking if population fraction converged to single value
            print("OUTPUT", new)  # print converged value
            return  # exit function once population is a single value
        x = new  # update x for next iteration
inital = float(input("INPUT> ").strip())  # input inital population and convert to float
lamba = float(input("INPUT> ").strip())  # input growth and convert to float
pcc(inital, lamba)  # call the function, calculate and print output