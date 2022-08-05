def inWord(num):
    ones = [
        "zero",
        "one",
        "two",
        "three",
        "four",
        "five",
        "six",
        "seven",
        "eight",
        "nine",
        "ten",
        "eleven",
        "twelve",
        "thirteen",
        "fourteen",
        "fifteen",
        "sixteen",
        "seventeen",
        "eighteen",
        "nineteen",
    ]
    tens = [
        "",
        "",
        "twenty",
        "thirty",
        "forty",
        "fifty",
        "sixty",
        "seventy",
        "eighty",
        "ninety",
    ]
    word = ""

    if num <= 19:
        word = ones[num]

    elif num >= 20 and num <= 99:
        ten = int(num / 10)
        one = num % 10
        word = tens[ten] + " " + ones[one]

    elif num >= 100 and num <= 999:
        hundred = int(num / 100)
        num %= 100
        ten = int(num / 10)
        one = num % 10
        word = ones[hundred] + " hundred and " + tens[ten] + " " + ones[one]
    return word


num = -1

while num <= 0:
    num = int(input("Enter a positive number: "))
    if num <= 0:
        print("I said posiitve!")
    else:
        print("in word: " + inWord(num))
