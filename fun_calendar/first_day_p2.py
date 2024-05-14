



with open('inp_1.txt', 'r') as file:
    total_sum = 0
    counter = 0
    number_words = {
        "one": 1, "two": 2, "three": 3, "four": 4, 
        "five": 5, "six": 6, "seven": 7, "eight": 8, "nine": 9
    }
    for line in file:
        

        word = ""
        first_int = 0
        second_int = 0
        first = False
        only_one = False
        digits_amout = int(sum(1 for char in line if char.isdigit()))
        if digits_amout == 1:
            only_one = True
        for char in line:
            
            if char.isdigit():
                if only_one and first == False:
                    first_int = int(char)
                    second_int = int(char)
                    first = True
                    
                
                if first == False:
                    first_int = int(char)
                    first = True
                else:
                    second_int = int(char)
            else:
                word+= char
                
                for key in number_words:
                    
                    if key in word:
                        if first == False:
                            first_int = number_words[key]
                            second_int = first_int
                            first = True
                        else:
                            second_int = number_words[key]
                        word = word[-1]
            
        total_sum+= first_int*10 + second_int
        counter+=1
        print(f"{counter}: {first_int*10 + second_int}")
    print(total_sum)
                
                
                
#             #one, two, three, four, five, six, seven, eight, and nine also count as valid "digits".



