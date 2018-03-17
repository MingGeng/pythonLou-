def char_count(str):
    countdict = {}
    for char in str:
        c = countdict.get(char)
        if c is None:
            countdict[char] = 1
        else:
            countdict[char] += 1
        print(countdict)
if __name__ == '__main__':
    s = input("Enter a string: ")
    char_count(s)
