import random
logo = """
.------.            _     _            _    _            _    
|A_  _ |.          | |   | |          | |  (_)          | |   
|( \/ ).-----.     | |__ | | __ _  ___| | ___  __ _  ___| | __
| \  /|K /\  |     | '_ \| |/ _` |/ __| |/ / |/ _` |/ __| |/ /
|  \/ | /  \ |     | |_) | | (_| | (__|   <| | (_| | (__|   < 
`-----| \  / |     |_.__/|_|\__,_|\___|_|\_\ |\__,_|\___|_|\_\\
      |  \/ K|                            _/ |                
      `------'                           |__/           
"""

def start():
    answer = input("Do you want to play Blackjack? Type 'y' or 'n': ")
    if answer == 'y':
          return True
    elif answer == 'n':
          return False
    else:
           print("here is the incorrect input, try again: ")
           start()
           
collection_cards = [2,2,2,2,3,3,3,3,4,4,4,4,5,5,5,5,6,6,6,6,7,7,7,7,8,8,8,8,9,9,9,9,10,10,10,10,'J','J','J','J','Q','Q','Q','Q','K','K','K','K','A','A','A','A']
def deal_card_start(player_cards,computer_cards):
      for i in range(2):
            rand_card = random.choice(collection_cards)
            collection_cards.remove(rand_card)
            player_cards.append(rand_card)
            rand_card = random.choice(collection_cards)
            collection_cards.remove(rand_card)
            computer_cards.append(rand_card)

def count_score(player_cards,computer_cards):
      player_score = 0
      comp_score = 0
      for card in player_cards:
            if type(card) == int:
                  if card >= 2 and card <= 10:
                        player_score += card
            else:
                  if card == 'A':
                        if (player_score + 11) > 21:
                              player_score += 1
                        else:
                              player_score += 11
                  else:
                        player_score += 10
                  
      for card in computer_cards:
            if type(card) == int:
                  if card >= 2 and card <= 10:
                        comp_score += card
            else:
                  if card == 'A':
                        if (comp_score + 11) > 21:
                              comp_score += 1
                        else:
                              comp_score += 11
                  else:
                        comp_score += 10
                  
      return [player_score,comp_score]

def print_cards(player_cards,computer_cards,first = False):
      res = count_score(player_cards,computer_cards)
      print(f"{player_cards}: {res[0]}")
      if not first:
            print(f"{computer_cards}: {res[1]}")
      else:
            comp_score = 0
            card = computer_cards[0]
            if type(card) == int:
                  if card >= 2 and card <= 10:
                        comp_score += card
            else:
                  if card == 'A':
                        if (comp_score + 11) > 21:
                              comp_score += 1
                        else:
                              comp_score += 11
                  else:
                        comp_score += 10
            print(f"{computer_cards[0]}:{comp_score}")
            
      
def check_for_wl(player_cards,computer_cards,end = False):
      res = count_score(player_cards,computer_cards)
      if not end:
            if res[0] == 21:
                  return "Player won"
            elif res[0] > 21:
                  return "Player lost" 
            if res[1] == 21:
                  return "Computer won"
            elif res[1] > 21:
                  return "Computer lost"
      else:
            if res[0] == 21:
                  return "Player won"
            elif res[0] > 21:
                  return "Player lost" 
            elif res[1] == 21:
                  return "Computer won"
            elif res[1] > 21:
                  return "Computer lost"
            elif (res[0] > res[1]) and res[0] < 22:
                  return "Player won"
            elif (res[1] > res[0]) and res[1] < 22:                  
                  return "Computer won"
            elif res[0] > 21:
                  return "Computer Won"
            elif res[1] > 21:
                  return "Player Won"                  
      
      
def add_one_card(player_deck):
      rand_card = random.choice(collection_cards)
      collection_cards.remove(rand_card)
      player_deck.append(rand_card)

         

                                      
     
