def main():
    tarot_deck = {
    0:"The Fool",
    1:"The Magician",
    2:"The High Priestess",
    3:"The Empress",
    4:"The Emperor",
    5:"The Hierophant",
    6:"The Lovers",
    7:"The Chariot",
    8:"Strength",
    9:"The Hermit",
    10:"Wheel of Fortune",
    11:"Justice",
    12:"The Hanged Man",
    13:"Death",
    14:"Temperance",
    15:"The Devil",
    16:"The Tower",
    17:"The Star",
    18:"The Moon",
    19:"The Sun",
    20:"Judgment",
    21:"The World"
    }

    user_selection = []

    card1 = int(input("Pick a number between 0 and 21 for your past card: "))
    user_selection.append(tarot_deck[card1])
    card2 = int(input("Pick another number between 0 and 21 for your present card: "))
    user_selection.append(tarot_deck[card2])
    card3 = int(input("Pick another number between 0 and 21 for your future card: "))
    user_selection.append(tarot_deck[card3])

    print("your past is {}".format(user_selection[0]))
    print("your present is {}".format(user_selection[1]))
    print("your future is {}".format(user_selection[2]))

if __name__ == "__main__":
    main()