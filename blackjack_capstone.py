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
                   

                                      
     
from replit import clear
import random
cards=[1,2,3,4,5,6,7,8,9,10,10,10,10,11]
print(logo)
start=input("Do you wants to play blackjack type 'y' for yes or 'n' to exit:")





def user():
    print(logo)
    choices1=[]
    total=0
    for i in range(0,2):
        random_card=random.choice(cards)
        choices1.append(random_card)
    print(f"Your starting card is {choices1}")
    for j in choices1:
        total+=j
    print(f"Your current total = {total}")
    
    choices=[]
    c_total=0
    random_card=random.choice(cards)  
    choices.append(random_card)
    print(f"computer starting card is {choices}")
    for n in choices:
        c_total+=n
    print(f"Computer current total = {c_total}")
    
    condition = True
    while condition:
        draw_hit=input("Type 'draw' to draw new card or 'Hit' to show:")
        while c_total<16:
            random_card=random.choice(cards)
            choices.append(random_card)
            if random_card==11 and random_card+c_total>21: 
                random_card=1
            
            c_total+=random_card
        if draw_hit=='hit':
            print(f"Computer current cards are {choices}")
            print(f"Computer current total = {c_total}")
        
        if draw_hit == "hit":
            condition = False
            if total==c_total:
                print("Draw")
            if total>21:   
                print("You loose")
            elif total>c_total and total<=21:
                print("You win")
            elif c_total>total and c_total<=21:
                print("Computer wins")    
            else:
                print("You win")
        
        if draw_hit == "draw":
            random_card=random.choice(cards)
            choices1.append(random_card)
            if random_card==11 and random_card+total>21: 
                random_card=1
            print(f"Your current cards are {choices1}")
            total+=random_card
            print(f"Your current total = {total}")
    start=input("Do you wants to play blackjack type 'y' for yes or 'n' to exit:") 
    if start == 'y':
        clear()
        user()
    
user()


