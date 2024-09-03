


import re
from collections import Counter

def calculate_total_winnings(hands, card_order, joker_transform=False):
    def sort_key(hand):
        if joker_transform and 'J' in hand:
            highest_card = max((card for card in hand if card != 'J'), key=lambda c: card_order.index(c), default='2')
            hand = hand.replace('J', Counter(hand.replace('J', '')).most_common(1)[0][0] if hand.count('J') < 5 else highest_card)
        return (tuple(sorted(Counter(hand).values(), reverse=True)), tuple(card_order.index(c) for c in hand))

    return sum(w * (i + 1) for i, h in enumerate(sorted(hands.keys(), key=sort_key)) for w in [hands[h]])

def load_hands(file_path):
    with open(file_path, 'r') as file:
        return {h: int(b) for h, b in re.findall(r'(\w{5}) (\d+)', file.read())}


file_path = ''
hands = load_hands(file_path)
print("Total Winnings Part 1:", calculate_total_winnings(hands, '23456789TJQKA'))
print("Total Winnings Part 2:", calculate_total_winnings(hands, 'J23456789TQKA', joker_transform=True))
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
        while(len(comb) > 0):
            for word in comb:
                temp = word[0]
                if temp < min_letter:
                    min_letter = temp
            for word in comb:
                temp_word = word.split()
                if temp_word.startswith(min_letter):
                    temp_list.append(word)
            
            if len(temp_list) == 1:
                list.append(temp_list)
            else:
                list_pairs = []
                for word in temp_list:
                    min_letter = word[1]
                    for str in temp_list:
                        if str[1] < min_letter:
                            min_letter = str[1]
                    sort_l = []
                    for word in temp_list:
                        temp_word = word.split()
                        if temp_word.startswith(min_letter):
                            sort_l.append(word)
                    temp_sort = sort_l[0]
                    
                        
                    
                        
                    

            

with open('7_inp.txt','r') as file:
    cont = file.read()
    print(sort(cont))