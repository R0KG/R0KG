
with open('inp_1.txt', 'r') as file:
    total_sum = 0
    for line in file:
        first_int = 0
        second_int = 0
        first = False
        only_one = False
        digits_amout = int(sum(1 for char in line if char.isdigit()))
        if digits_amout == 1:
            only_one = True
        for char in line:
            
            if only_one and first == False and char.isdigit():
                first_int = int(char)
                second_int = int(char)
                first = True
                break
            if char.isdigit():
                if first == False:
                    first_int = int(char)
                    first = True
                else:
                    second_int = int(char)
        total_sum+= first_int*10 + second_int
    print(total_sum)
                
            


