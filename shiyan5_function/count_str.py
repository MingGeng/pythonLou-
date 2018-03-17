#!/usr/bin/en python3

def char_count(str):
    char_list = set(str)
    for char in char_list:
        print(char, str.count(char))

def better_char_count(str):
    char_dict = {}
    for char in str:
#        char_dict[char] += (0 if char_dict.get(char) is None else 1)
        char_dict[char] = char_dict.get(char,1) + (0 if char_dict.get(char) is None else 1)
    print(char_dict)


#        print(char_dict.get(char))
#        r = char_dict.get(char)
#        if r is not None:
#            char_dict[char] += 1
#        else:
#            char_dict[char] = 1  
#        print(char_dict)    

if __name__ == '__main__':
    s = input("Enter a string: ")
    char_count(s)
    print("Better ?:")
    better_char_count(s)    


