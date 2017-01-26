def is_pangram(sentence):
    """ Returns true if the inputted sentence is a panagram """
    sent = sentence.lower()
    letters = {}
    total = 0
    for i in sent:
        if 97 <= ord(i) <= 122:
            letters.setdefault(i, 1)
    for key in letters:
        total += letters[key]

    return total == 26
