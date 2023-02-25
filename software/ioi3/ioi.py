def decode(input_file):
    with open(input_file, 'r') as file:
        total = 0
        for line in file:
            values = line.split("	")
            values = [int(value.strip()) for value in values]
            if sum(values[3:6]) == 0:
                result = values[1] + values[2]
            else:
                result = 0
                
            if values[3] > 0:
                result += abs(values[3] - values[1])
                
            if values[4] > 0:
                result += values[1] / values[0]
                
            if values[5] > 0:
                result += values[5] * values[0] + values[2]

            total = total + result
        
    return total
            

                

input_file = "ioi.txt"

total = decode(input_file)

print(total)