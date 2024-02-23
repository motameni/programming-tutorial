def play_game():
    """
    The result will be:
    0: draw
    1: player 1 is winner
    2: player 2 is winner
    """
    choice1 = input("Player 1 (s: Sang, k: Kaghaz, g: Gheychi): ")
    choice2 = input("Player 2 (s: Sang, k: Kaghaz, g: Gheychi): ")
    if choice1 == choice2:
        return 0
    if (choice1 == "k" and choice2 == "s") or \
       (choice1 == "s" and choice2 == "g") or \
       (choice1 == "g" and choice2 == "k"):
        return 1
    else:
        return 2
