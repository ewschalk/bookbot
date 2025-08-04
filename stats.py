def number(text):
    count = 0
    split = text.split()
    for s in split:
        count += 1
    return count

def character(text):
    characters = {"a":0 ,"b":0 ,"c":0 , "d":0, "e":0, "f":0, "g":0, "h":0, "i":0, "j":0, "k":0, "l":0, "m":0, "n":0, "o":0, "p":0, "q":0, "r":0, "s":0, "t":0, "u":0, "v":0, "w":0, "x":0, "y":0, "z":0, "1":0, "2":0, "3":0, "4":0, "5":0, "6":0, "7":0, "8":0, "9":0, "0":0, ",":0, ".":0, ";":0, ":":0, "?":0, "!":0, "'":0, "\"":0, "-":0, "_":0, "(":0, ")":0, "[":0, "]":0, " ":0, "æ":0, "â":0, "ê":0, "ë":0, "ô":0}
    text = text.lower()
    for char in text:
        if char in characters:
            characters[char]+= 1
    return characters

def get_alpha_list(char_dict):
    alpha_list = []
    for char, count in char_dict.items():
        if char.isalpha():
            alpha_list.append({"char": char, "num": count})
    return alpha_list




 
    




