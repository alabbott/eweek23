def fib_hash():

    current = 2
    last = 1
    sum = 0

    # for all values of the fibonacci sequence under 1,000,000
    while  current < 1000000:
        print("Checking: " + str(current))
        # check if the current value is even
        if current % 2 ==0:

            # if so add it to the total
            sum = sum + current
        
        next = current + last
        last = current
        current = next
        print("Current Sum: " + str(sum))

fib_hash()