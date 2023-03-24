valid_card = {'A':1,'2':2,'3':3,'4':4,'5':5,'6':6,'7':7,'8':8,'9':9,'T':10,'J':10,'Q':10,'K':10}
thinks = input()
bust = int(input())
all_card_left = []
no_bust_card = []
card_counts = {card: 0 for card in valid_card}
for think in thinks.split('.'):
    if all(char in valid_card.keys() for char in think):
        for card in think:
            card_counts[card] += 1
    else:
        continue
for card,count in card_counts.items():
    if count >=4:
        continue
    else:
        all_card_left.extend([card]*(4-count))
        if bust > valid_card[card]:
            no_bust_card.extend([card]*(4-count))
print(str(round(len(no_bust_card)/len(all_card_left)*100))+'%')
