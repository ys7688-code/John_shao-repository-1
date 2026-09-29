number_of_words = int(input("How many words will you enter? > "))

while number_of_words < 3 or number_of_words > 6:
    print("Invalid input. Please enter a number between 3 and 6 ")
    number_of_words = int(input("How many words will you enter? > "))

shortest_word = '                                                              '
longest_word = ' '
total_length = 0
for i in range(number_of_words):
    word = input(f"Word #{i+1} please > ")
    total_length += len(word)
    if len(shortest_word) >= len(word) :
        shortest_word = word
    if len(longest_word) <= len(word) :
        longest_word = word
print(f"Shortest: {shortest_word}")
print(f"Longest: {longest_word}")
print(f"Average length: {(total_length / number_of_words):.2f}")