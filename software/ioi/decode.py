def decode_pattern(input_file):
    # Open the file in read mode
    with open(input_file, 'r') as file:
        # Loop through each line in the file
        total = 0
        for line in file:
            # Split the line into a list of numbers
            numbers = line.strip().split()
            #print(numbers)
            numbers = [int(x) for x in numbers]
            print(numbers)
            # Get the non-zero numbers in the list
            if numbers[1] > 127:
                result = (numbers[5] * numbers[0]) + numbers[2] + 10 + min(numbers[:2])
            else:
                if numbers[5] > 0:
                    result = (numbers[5] * numbers[0]) + numbers[2]
                else:
                    result = (numbers[5] * numbers[0]) + numbers[2] + max(numbers[:2])
            total = total + result
            print(result)
            #print(total)
        
        print("The total is " + str(total))


# Call the function with the input file name
decode_pattern('IOI.txt')