import library_blackjack

#Start Output
player_score = 0
computer_score = 0
player_deck = []
computer_deck = []
play = False
print(library_blackjack.logo)
#Game Starts
if library_blackjack.start():
    library_blackjack.deal_card_start(player_deck,computer_deck)
    library_blackjack.print_cards(player_deck,computer_deck,True)
    if library_blackjack.check_for_wl(player_deck,computer_deck) == "Player won":
        print("Player Won")
    play = True
while play:
    if library_blackjack.start() == True:
        library_blackjack.add_one_card(player_deck)
        player_score = library_blackjack.count_score(player_deck,computer_deck)[0]
        computer_score = library_blackjack.count_score(player_deck,computer_deck)[1]
        library_blackjack.print_cards(player_deck,computer_deck,True)
        if library_blackjack.check_for_wl(player_deck,computer_deck) == "Player won":
            print("Player won")
            play = False
        elif library_blackjack.check_for_wl(player_deck,computer_deck) == "Player lost": 
            print("Player lost")
            play = False
    else:
        player_score = library_blackjack.count_score(player_deck,computer_deck)[0]
        computer_score = library_blackjack.count_score(player_deck,computer_deck)[1]
        library_blackjack.print_cards(player_deck,computer_deck)
        if computer_score > 16:
            library_blackjack.print_cards(player_deck,computer_deck)
            if library_blackjack.check_for_wl(player_deck,computer_deck,True) == "Player won":
                print("Player won")
                play = False
            elif library_blackjack.check_for_wl(player_deck,computer_deck,True) == "Computer won":
                print("Computer won")
                play = False
        else:
            while computer_score <= 16:
                library_blackjack.add_one_card(computer_deck)
                computer_score = library_blackjack.count_score(player_deck,computer_deck)[1]   
            library_blackjack.print_cards(player_deck,computer_deck)
            if library_blackjack.check_for_wl(player_deck,computer_deck,True) == "Player won":
                print("Player won")
                play = False
            elif library_blackjack.check_for_wl(player_deck,computer_deck,True) == "Computer won":
                print("Computer won")
                play = False

            
    

