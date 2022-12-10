import re


def readFile():
    file = open("InputData.txt", "r")
    return file


def findContains(line, pattern):
    split = line.strip().split(",")
    first = re.search(pattern, split[0])
    second = re.search(pattern, split[1])
    if ((int(first.group(1)) <= int(second.group(1)) and int(first.group(2)) >= int(second.group(2))) or (
            int(second.group(1)) <= int(first.group(1)) and int(second.group(2)) >= int(first.group(2)))):
        return 1
    return 0


def main():
    file = readFile()
    total = 0
    pattern = "(\\d+)-(\\d+)"
    
    for line in file:
        total = total + findContains(line, pattern)

    print(f"Total number of contains: {total}")
    file.close()

if (__name__ == "__main__"):
    main()
