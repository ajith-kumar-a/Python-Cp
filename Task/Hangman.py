import random


hangman_words = {
    "Elephant": "A large mammal with a trunk.",
    "Giraffe": "The tallest land animal with a long neck.",
    "Oxygen": "A gas essential for human respiration.",
    "Pyramid": "Ancient monumental structures found in Egypt.",
    "Banana": "A yellow tropical fruit that monkeys love.",
    "Volcano": "A mountain that erupts with lava.",
    "Rainbow": "A colorful arc seen after rain.",
    "Telescope": "An instrument used to observe distant objects in space.",
    "Chocolate": "A sweet treat made from cocoa beans.",
    "Kangaroo": "An Australian marsupial that hops."
}


listHangman = list(hangman_words)

ran = random.randint(0,9)

word = listHangman[ran]
word = word.upper()
wordLen = len(word)

ansList = []
for i in word:
    ansList.append("_")

gueseLetter = ""
while(ansList != list(word)):

    gueseLetter = input(f"\nGuess \' {hangman_words[word.capitalize()]} \' Letter : ")
    gueseLetter = gueseLetter[0].upper()
    if word.__contains__(gueseLetter):
        for i in range(wordLen):
            if gueseLetter == word[i]:
                ansList[i] = gueseLetter
        
    for i in ansList:
        print(i,end=" ")

print("\nYou Won the Game")


