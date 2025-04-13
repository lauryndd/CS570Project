import sys

#Mismatch penalty
alpha = [[0, 110, 48, 94],
         [110, 0, 118, 48],
         [48, 118, 0, 110],
         [94, 48, 110, 0]]

#Gap penalty
delta = 30

def stringInsert(str1, str2, index):
    string1_split = str1[:index]
    string2_split = str1[index:]
    return string1_split + str2 + string2_split

def inputGeneration(inputFile):
    f = open(inputFile, "r", encoding="utf-8")
    inputText = f.read()
    f.close()

    inputLineSep = inputText.splitlines()
    s1 = inputLineSep[0]
    s2 = str()

    for i in range(1, len(inputLineSep)):
        if s2 == "":
            if inputLineSep[i].isalpha():
                s2 = inputLineSep[i];
            if inputLineSep[i].isdigit():
                s1 = stringInsert(s1, s1, int(inputLineSep[i]) + 1)
        if inputLineSep[i].isdigit():
            s2 = stringInsert(s2, s2, int(inputLineSep[i]) + 1)
    return s1, s2

def main(input, output):
    s1, s2 = inputGeneration(input)
    print(s1, s2)

    f = open(output, "w")
    f.write("some content")
    f.close()

if __name__ == '__main__':
    input = sys.argv[1]
    output = sys.argv[2]
    main(input, output)
