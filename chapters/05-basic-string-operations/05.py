x = input("Enter a word: ").lower()

vowels = ["a", "e", "i", "o", "u"]

for vowel in vowels:
    # Method 1:
    # print("Count of " + vowel + " in " + x + ":", x.count(vowel))

    # Method 2: using string formatting
    print("Count of %s in %s: %d" % (vowel, x, x.count(vowel)))
