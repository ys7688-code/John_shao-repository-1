cards_in_hand = list(input("Enter your hand: > "))
cards_in_hand_sorted = ''
digits = ''
letters = ''
for i in cards_in_hand:
    if i.isdigit() :
        digits += i
    else:
        letters += i
cards_in_hand_sorted = digits + letters
sum = 0
number_of_aces = 0
for i in range(len(cards_in_hand_sorted)) :
    card = cards_in_hand_sorted[i]
    if cards_in_hand_sorted[(i+1) % len(cards_in_hand_sorted)] == '0':
        sum += 10
        i += 1
    else :
        if card == 'J' or card == 'Q' or card == 'K' :
            sum += 10
        elif card == 'A' :
            number_of_aces += 1
            if sum + 11 <= 21 and sum + 11 >= 17:
                sum += 11
            else :
                sum += 1
                number_of_aces -= 1
            while sum > 21 and number_of_aces > 0 :
                if sum > 21 :
                    sum -= 10
                number_of_aces -= 1
        else :
            sum += int(card)
    # print(sum)
if number_of_aces > 0 :
    while sum > 21 and number_of_aces > 0 :
        sum -= 10
        number_of_aces -= 1

if sum < 17 :
    print("Hit")
elif sum >= 17 and sum <= 21 :
    print("Stay")
else :
    print("Bust")