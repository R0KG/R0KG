
import re

# Bool for true/false if it´s a combination 
def four_of_kind(word):

    letter_counts = {}
    
    for letter in word:
        if letter in letter_counts:
            letter_counts[letter] += 1
        else:
            letter_counts[letter] = 1
    if len(letter_counts) == 2:
        if 4 in letter_counts.values():
            return True
    return False
            
    
def full_house(word):
    letter_counts = {}
    
    for letter in word:
        if letter in letter_counts:
            letter_counts[letter] += 1
        else:
            letter_counts[letter] = 1
    if len(letter_counts) == 2:
        if 2 in letter_counts.values() and 3 in letter_counts.values():
            return True
    return False    
    
def three_of_kind(word):
    letter_counts = {}
    
    for letter in word:
        if letter in letter_counts:
            letter_counts[letter] += 1
        else:
            letter_counts[letter] = 1
    
    if 3 in letter_counts.values():
        return True
    return False

    
def two_pair(word):
    letter_counts = {}
    
    for letter in word:
        if letter in letter_counts:
            letter_counts[letter] += 1
        else:
            letter_counts[letter] = 1
            
    count_occ = sum(1 for value in letter_counts.values() if value == 2)
    
    if count_occ == 2:
        return True
    return False    
    
def one_pair(word):
    letter_counts = {}
    
    for letter in word:
        if letter in letter_counts:
            letter_counts[letter] += 1
        else:
            letter_counts[letter] = 1
            
    if 2 in letter_counts.values():
        return True
    return False



def sort(inp):
    list = [[],[],[],[],[],[],[]]
    for word in inp.splitlines():
        temp = word[:5]
        letter_counts = {}
        for letter in temp:
            if letter in letter_counts:
                letter_counts[letter] += 1
            else:
                letter_counts[letter] = 1
        if len(letter_counts) == 1:
            list[6].append(word)
        elif four_of_kind(temp):
            list[5].append(word)
        elif full_house(temp):
            list[4].append(word)
        elif three_of_kind(temp):
            list[3].append(word)       
        elif two_pair(temp):
            list[2].append(word)
        elif one_pair(temp):
            list[1].append(word)
        else:
            list[0].append(word)
    return list



def internal_sort(inp):
    list = []
    for comb in inp:
        temp_list = []
        min_letter = temp[0]
        for word in comb:
            temp = comb[0]
            if temp < min_letter:
                min_letter = temp
        for word in comb:
            temp_word = word.split()
            if temp_word.startswith(min_letter):
                temp_list.append(word)
        
        if len(temp_list) == 1:
            list.append(temp_list)
        else:
            for word in temp_list:
                
                    

            

with open('7_inp.txt','r') as file:
    cont = file.read()
    print(sort(cont))