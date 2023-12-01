file = open('input.txt', 'r')
total = 0
while True:
    numberStr = ""
    line = file.readline()
    if not line:
        break
    for char in line:
        if(char.isdigit()):
            numberStr += char
    total += int(numberStr[0] + numberStr[len(numberStr) - 1])

print(total)