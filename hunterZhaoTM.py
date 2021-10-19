#Hunter Zhao
#zero-one-starTM.txt
#0n1n0n.txt

#starting global variable
lines = []
word = ""
currentState = "0"
currentRead = 1
currentLine = int()
valid = True
accept = False

#asks user for input file and converts the turing machine code into a list of strings
inFile = input("Input file from same directory")
with open(inFile) as f:
    lines = [line.rstrip() for line in f]
i=0
while i<len(lines):
    if (lines[i] == ""):
        del lines[i]
    elif lines[i][0] == "/" and lines[i][1] == "/":
        del lines[i]
    elif "//" in lines[i]:
        split_string = lines[i].split("//", 1)
        lines[i] = split_string[0]
        #print(lines[i])
        i += 1
    else:
        #print(lines[i])
        i += 1
for x in range(len(lines)):
    lines[x] = lines[x].replace(" ", "")
    #print(lines[x])

#find the right line in the turing machine to use
def findLine():
    global lines
    global currentLine
    global currentState
    global currentRead
    global word
    i = 0
    while i<len(lines):
        #print(i)
        #print(lines[i][0],currentState,lines[i][1],word[currentRead])
        if (lines[i][0] == currentState) and (lines[i][1] == word[currentRead]):
            currentLine = i
            return True
        else:
            i += 1
    return False

#asks the user for a word
def asking():
    global word
    word = input("Input a word")
    word = "B" + word + "B"
    print(word)

#does the instruction found in the machine onto the word
def machine():
    global valid
    global word
    global lines
    global currentState
    global currentRead
    global currentLine
    global accept
    if findLine():
        word = word[:currentRead] + lines[currentLine][3] + word[currentRead + 1:]
        #word[currentRead] = lines[currentLine][3]
        if lines[currentLine][4] == "R":
            currentRead += 1
        else:
            currentRead -= 1
        currentState = lines[currentLine][2]
        print(word)
        if currentState == "f":
            valid = False
            accept = True
            return
    else:
        valid = False
        
#resets the input and variables
while True:
    asking()
    while valid:
        machine()
    if accept == True:
        print("Accepted")
        word = ""
        currentState = "0"
        currentRead = 1
        currentLine = int()
        valid = True
        accept = False
    else:
        print("Doesn't Accept")
        word = ""
        currentState = "0"
        currentRead = 1
        currentLine = int()
        valid = True
        accept = False

#Credit to stackoverflow for reading file inputs
