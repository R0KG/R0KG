



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
        counter  = 0
        total_amount = len(line)
        for char in line:
            counter += 1
            if char.isdigit():
                if only_one and first == False:
                    first_int = int(char)
                    second_int = int(char)
                    first = True
                    break
        
                if first == False:
                        first_int = int(char)
                        first = True
                else:
                        second_int = int(char)

            else:
                if total_amount - counter >= 3:
                    temp_word_1 = ""
                    temp_word_2 = ""
                    temp_word_3 = ""
                    if total_amount - counter == 3:
                        temp_word_1 = line[counter-1:counter+2]
                    elif total_amount - counter == 4:
                        temp_word_2 = line[counter-1:counter+3]
                    elif total_amount - counter == 5:
                        temp_word_3 = line[counter-1:counter+4]
                    else:
                        start = counter - 1
                        end_3 = counter + 2
                        end_4 = counter + 3
                        end_5 = counter + 4
                        temp_word_1 = line[start:end_3]
                        temp_word_2 = line[start:end_4]
                        temp_word_3 = line[start:end_5]
                    if temp_word_1 in ["one","two","six"]:
                            if first == False and len(line) <=3:
                                if temp_word_1 == "one":
                                    first_int = 1
                                if temp_word_1 == "two":
                                    first_int = 2     
                                if temp_word_1 == "six":
                                    first_int = 6
                                second_int = first_int
                                first = True
                            if first == False:
                                if temp_word_1 == "one":
                                    first_int = 1
                                if temp_word_1 == "two":
                                    first_int = 2     
                                if temp_word_1 == "six":
                                    first_int = 6
                                first = True
                            else:
                                if temp_word_1 == "one":
                                    second_int = 1
                                if temp_word_1 == "two":
                                    second_int = 2     
                                if temp_word_1 == "six":
                                    second_int = 6                       
                        
        total_sum+= first_int*10 + second_int
    print(total_sum)
                
            #one, two, three, four, five, six, seven, eight, and nine also count as valid "digits".


