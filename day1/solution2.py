file = open('input.txt', 'r')
total = 0
validDigits = {
    "one": "1",
    "two": "2",
    "three": "3",
    "four": "4",
    "five": "5",
    "six": "6",
    "seven": "7",
    "eight": "8",
    "nine": "9"
}
counter = 1
while True:
    numberStr = ""
    digits = ""
    line = file.readline()
    if not line:
        break
    for i in validDigits:
        if(i in line):
            digits = digits + validDigits[i]
    print(digits)
            
    for char in line:
        if(char.isdigit()):
            numberStr += char
    #print(counter, numberStr[0] + (numberStr[-1]))
    
    total += int(numberStr[0] + (numberStr[-1]))
    counter += 1

print("total is:", total)
