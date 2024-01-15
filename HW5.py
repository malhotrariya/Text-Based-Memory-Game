'''
15-110 Homework 5
Name: Riya Malhotra
Andrew ID: riyamalh

'''
# import libraries
import random

'''
#1 - generateBoard(words)
Parameters: 1D list of strings
Returns: 2D list (board)
'''

def generateBoard(words):
    cards = []
    for word in words:
        card1 = [word, False]
        card2 = [word, False]
        cards.append(card1)
        cards.append(card2)
    random.shuffle(cards)
    return cards

'''
#2 - displayBoard(board)
Parameters: 2D list (board)
Returns: None
'''

def displayBoard(board):
    for index in range(len(board)):
        cards = board[index]
        if cards[1] == True: 
            print(str(index) + " : " + str(cards[0]))
        else:
            print(str(index) + " : " + "???")

'''
#3 - getFlippedCards(board)
Parameters: 2D list (board)
Returns: 1D list of ints
'''

def getFlippedCards(board):
    result = []
    for index in range(len(board)):
            if board[index][1] == True:
                result.append(index)
    return result

'''
#4 - pickIndex(board)
Parameters: 2D list (board)
Returns: int
'''

def pickIndex(board):
    while True:
        PickedCard = input("Pick a card index: ")
        if PickedCard.isdigit():
            index = int(PickedCard)
            if index < 0 or index >= len(board):
                print("Out of range. Pick a valid card.")
            elif board[index][1] == True:
                print("You've already flipped that card. Pick a different card.")
            else:
                return index
                    
        else:
            print("That's not an integer!")
            
'''
#5 - loadWords(filename)
Parameters: str
Returns: 1D list of strs
'''
def loadWords(filename):
    f = open(filename, "r")
    text = f.read()
    textWords = text.split(",")
    f.close()
    return textWords
print("textWords")

'''
#6 - playMemoryGame(filename)
Parameters: str
Returns: None
'''

def playMemoryGame(filename):
    words = loadWords(filename)
    board = generateBoard(words)
    print("Welcome to Memory!")
    displayBoard(board)
    cardPick = 0
    while len(getFlippedCards(board)) < len(board):
        cardPick = cardPick + 1
        
        index1 = pickIndex(board)
        board[index1][1] = True
        displayBoard(board)
        
        index2 = pickIndex(board)
        board[index2][1] = True
        displayBoard(board)
        
        if board[index1][0] == board[index2][0]:
            print("Good guess!")
        if board[index1][1] == False:
            print("Try again!")
        print("---")
    print("Good game! You Took " + str(cardPick) + " moves to clear the board.")
        

################################################################################
''' Test Functions '''

def testGenerateBoard():
    print("Testing generateBoard()...", end="")
    # NOTE: this just tests that you're making the right cards.
    # Random order is tested on Gradescope.
    assert(type(generateBoard(["dog", "cat"])) == list)
    assert(sorted(generateBoard(["dog", "cat"])) == [ ["cat", False], ["cat", False], ["dog", False], ["dog", False] ])
    assert(sorted(generateBoard(["dog", "cat", "owl"])) == [ ["cat", False], ["cat", False], ["dog", False], ["dog", False], ["owl", False], ["owl", False] ])
    assert(sorted(generateBoard(["dog", "cat", "owl", "hat", "egg"])) == [ ["cat", False], ["cat", False], ["dog", False], ["dog", False], ["egg", False], ["egg", False], ["hat", False], ["hat", False], ["owl", False], ["owl", False] ])
    assert(sorted(generateBoard(["dog"])) == [ ["dog", False], ["dog", False] ])
    assert(generateBoard([]) == [])

    # Make sure that the cards aren't aliased!
    board = generateBoard(["dog"])
    board[0][1] = True
    assert(board[1][1] == False) # second card should *not* change when first card is changed.
    print("... done!")

def testDisplayBoard():
    print("Testing displayBoard()...")
    # Compare your output to the expected output to make sure it looks right!
    print("Display Test 1:")
    displayBoard([ ["dog", False], ["cat", True], ["cat", False], ["dog", True] ])
    # Should print:
    #0: ???
    #1: cat
    #2: ???
    #3: dog
    print("-----")
    print("Display Test 2:")
    displayBoard([ ["owl", True], ["owl", True], ["cat", False], ["dog", False], ["cat", True], ["dog", False] ])
    # Should print:
    #0: owl
    #1: owl
    #2: ???
    #3: ???
    #4: cat
    #5: ???
    print("-----")
    print("Display Test 3:")
    displayBoard([["egg", False], ["owl", False], ["owl", False], ["cat", False], ["cat", False], ["hat", False], ["egg", False], ["hat", False], ["dog", False], ["dog", False]])
    # Should print:
    #0: ???
    #1: ???
    #2: ???
    #3: ???
    #4: ???
    #5: ???
    #6: ???
    #7: ???
    #8: ???
    #9: ???
    print("-----")
    print("Display Test 4:")
    displayBoard([ ["dog", True], ["dog", True] ])
    # Should print:
    #0: dog
    #1: dog
    print("-----")
    print("... done!")

def testGetFlippedCards():
    print("Testing getFlippedCards()...", end="")
    assert(getFlippedCards([ ["dog", False], ["cat", True], ["cat", False], ["dog", True] ]) == [1, 3])
    assert(getFlippedCards([ ["owl", True], ["owl", True], ["cat", False], ["dog", False], ["cat", True], ["dog", False] ]) == [0, 1, 4])
    assert(getFlippedCards([["egg", False], ["owl", False], ["owl", False], ["cat", False], ["cat", False], ["hat", False], ["egg", False], ["hat", False], ["dog", False], ["dog", False]]) == [])
    assert(getFlippedCards([ ["dog", True], ["dog", True] ]) == [0, 1])
    assert(getFlippedCards([]) == [])
    print("... done!")

def testPickIndex():
    print("Testing pickIndex()...")
    # You'll need to test this one yourself! Try using the same inputs that we did in the writeup and see if you get the expected messages.
    print("pickIndex Test 1:")
    board1 = [ ["owl", False], ["dog", True], ["cat", False], ["cat", False], ["owl", False], ["dog", True] ]
    # test -> print message [not an integer]
    # 6 -> print message [out of range]
    # 1 -> print message [already flipped]
    # Valid indexes you can try: 0, 2, 3, 4
    index = pickIndex(board1)
    assert(index in [0, 2, 3, 4]) # four possible indexes to pick
    print("-----")
    print("pickIndex Test 2:")

    board2 = [ ["dog", True], ["dog", False] ]
    # The only valid index is 1
    assert(pickIndex(board2) == 1)
    print("-----")
    print("... done!")

def testLoadWords():
    print("Testing loadWords()...", end="")
    # Make sure you've downloaded memory1.txt, memory2.txt, and memory3.txt into the correct folder first!
    assert(loadWords("memory1.txt") == [ "dog", "cat" ])
    assert(loadWords("memory2.txt") == [ "owl", "dog", "cat" ])
    assert(loadWords("memory3.txt") == [ "cat", "dog", "horse", "hat", "owl" ])
    print("... done!")

def runPlayMemoryGame():
    print("Running playMemoryGame()...")
    # Make sure you've downloaded memory1.txt, memory2.txt, and memory3.txt into the correct folder first!
    print("Game test 1:")
    playMemoryGame("memory1.txt")
    # Play the game, see if it works
    print("-----")

    print("Game test 2:")
    playMemoryGame("memory3.txt")
    print("-----")
    print("... done!")

def testAll():
    testGenerateBoard()
    testDisplayBoard()
    testGetFlippedCards()
    testPickIndex()
    testLoadWords()
    runPlayMemoryGame()

testAll()