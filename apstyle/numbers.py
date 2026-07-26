def format_cardinal_number(n):
    number_words = {
        1: "one",
        2: "two",
        3: "three",
        4: "four",
        5: "five",
        6: "six",
        7: "seven",
        8: "eight",
        9: "nine",
    }

    if n < 10:
        return number_words[n]

    if n > 1000000:
        millions = n / 1000000
        if millions == int(millions):
            millions = int(millions)
        return "{} million".format(millions)


    return "{:,}".format(n)
