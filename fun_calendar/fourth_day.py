
# first part
# with open('fourth_day_inp.txt','r') as text:
#     result = 0
#     for line in text:
#         winning_numbers = line.split(':')[1].split('|')[0].split()
#         numbers_you_have = line.split(':')[1].split('|')[1].split()
#         winning_numbers = [int(num) for num in winning_numbers]
#         numbers_you_have = [int(num) for num in numbers_you_have]
#         counter = 0
#         for win_num in winning_numbers:
#             if win_num in numbers_you_have:
#                 counter += 1
#         if counter > 1:
#             result += 2**(counter - 1)
#         else:
#             result += counter
#     print(result)


#second part

with open('fourth_day_inp.txt','r') as text:
    result = 0
    copies_dict = { key: 0 for key in range(1,217)}
    key_counter = 1 # for index in the dict
    for line in text:
        card_num = line.split(':')[0].split(' ')[1]
        winning_numbers = line.split(':')[1].split('|')[0].split()
        numbers_you_have = line.split(':')[1].split('|')[1].split()
        winning_numbers = [int(num) for num in winning_numbers]
        numbers_you_have = [int(num) for num in numbers_you_have]
        inner_counter = key_counter
        copies_dict[key_counter] += 1
        for win_num in winning_numbers:
            if win_num in numbers_you_have:
                inner_counter+=1
                for i in range (0,copies_dict[key_counter]):
                    copies_dict[inner_counter] += 1
                
        
        key_counter +=1
    print(sum(copies_dict.values()))
