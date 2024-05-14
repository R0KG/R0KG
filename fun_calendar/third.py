# import re


# def numbers_indx_dic(line):
#     dic = {}
#     numbers = re.findall(r"\d+", line)
#     for num in numbers:
#         dic[num] = [i for i in range(line.find(num), line.find(num) + len(num))]
#     return dic


# def symbols_indx(line):
#     symbols_list = []
#     for index, char in enumerate(line):
#         if char not in '01234566789.':
#             symbols_list.append(index)
#     return symbols_list





# def start():

#     with open("third_inp.txt", "r") as text:
#         sum = 0
#         content = text.readlines()
#         content = [line.strip() for line in content]
#         for index, line in enumerate(content):
#             if index != 0 and index != len(content) - 1:
#                 symbols_indexes = []
#                 symbols_indexes.append(symbols_indx(content[index - 1]))
#                 symbols_indexes.append(symbols_indx(content[index]))
#                 symbols_indexes.append(symbols_indx(content[index + 1]))
#                 merged_list_symbols = [
#                     item for sublist in symbols_indexes for item in sublist
#                 ]
#                 print(f"index: {index} and symbols {symbols_indexes}")

#                 numbers_indexes = numbers_indx_dic(line)
#                 for number, indexes in numbers_indexes.items():
#                     for num_index in indexes:
#                         ## first index
#                         if num_index == 0 or num_index == len(line) - 1:
#                             if num_index in merged_list_symbols:
#                                 sum += int(number)
#                                 print(number)
#                                 break
#                         else:   
#                             if (
#                                 num_index - 1 in merged_list_symbols
#                                 or num_index in merged_list_symbols
#                                 or num_index + 1 in merged_list_symbols
#                             ):
#                                 sum +=  int(number)
#                                 print(number)
#                                 break
#                 print(sum)
#             elif index == 0:
#                 symbols_indexes = []
#                 symbols_indexes.append(symbols_indx(content[index]))
#                 symbols_indexes.append(symbols_indx(content[index + 1]))
#                 merged_list_symbols = [
#                     item for sublist in symbols_indexes for item in sublist
#                 ]
#                 print(f"index: {index} and symbols {symbols_indexes}")

#                 numbers_indexes = numbers_indx_dic(line)
#                 for number, indexes in numbers_indexes.items():
#                     for num_index in indexes:
#                         ## first index
#                         if num_index == 0 or num_index == len(line) - 1:
#                             if num_index in merged_list_symbols:
#                                 sum += int(number)
#                                 print(number)
#                                 break
#                         else:   
#                             if (
#                                 num_index - 1 in merged_list_symbols
#                                 or num_index in merged_list_symbols
#                                 or num_index + 1 in merged_list_symbols
#                             ):
#                                 sum +=  int(number)
#                                 print(number)
#                                 break
#                 print(sum)    
#             elif index == len(content) - 1:      
#                 symbols_indexes = []
#                 symbols_indexes.append(symbols_indx(content[index]))
#                 symbols_indexes.append(symbols_indx(content[index - 1]))
#                 merged_list_symbols = [
#                     item for sublist in symbols_indexes for item in sublist
#                 ]
#                 print(f"index: {index} and symbols {symbols_indexes}")

#                 numbers_indexes = numbers_indx_dic(line)
#                 for number, indexes in numbers_indexes.items():
#                     for num_index in indexes:
#                         ## first index
#                         if num_index == 0 or num_index == len(line) - 1:
#                             if num_index in merged_list_symbols:
#                                 sum += int(number)
#                                 print(number)
#                                 break
#                         else:   
#                             if (
#                                 num_index - 1 in merged_list_symbols
#                                 or num_index in merged_list_symbols
#                                 or num_index + 1 in merged_list_symbols
#                             ):
#                                 print(number)
#                                 sum +=  int(number)
#                                 break
#                 print(sum)   



# start()



import math as m, re

board = list(open('third_inp.txt'))
chars = {(r, c): [] for r in range(140) for c in range(140)
                    if board[r][c] not in '01234566789.'}


for r, row in enumerate(board):
    for n in re.finditer(r'\d+', row):
        edge = {(r, c) for r in (r-1, r, r+1)
                       for c in range(n.start()-1, n.end()+1)}
        
        for o in edge & chars.keys():
            chars[o].append(int(n.group()))

print(sum(sum(p)    for p in chars.values()),
      sum(m.prod(p) for p in chars.values() if len(p)==2))

# for window in windowed(chain([""], data.split('\n'), [""]), 3):
#     for m in re.finditer(r'\d+', window[1]):
#         if any(re.search(r'[^\d.]', s[max(0, m.start() - 1):m.end() + 1]) is not None for s in window):
#             r += int(m.group(0))