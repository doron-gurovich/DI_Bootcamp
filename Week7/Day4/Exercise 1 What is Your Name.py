# -*- coding: utf-8 -*-
"""
Created on Fri Nov 19 12:45:55 2021

@author: 97250
"""

def get_full_name(first_name, last_name, middle_name = ""):
    return first_name + " " + middle_name + " " + last_name

print(get_full_name("first_name", "last_name"))
print(get_full_name("first_name", "last_name", "middle_name"))


morse = {
    # Letters
    "a": ".-",
    "b": "-...",
    "c": "-.-.",
    "d": "-..",
    "e": ".",
    "f": "..-.",
    "g": "--.",
    "h": "....",
    "i": "..",
    "j": ".---",
    "k": "-.-",
    "l": ".-..",
    "m": "--",
    "n": "-.",
    "o": "---",
    "p": ".--.",
    "q": "--.-",
    "r": ".-.",
    "s": "...",
    "t": "-",
    "u": "..-",
    "v": "...-",
    "w": ".--",
    "x": "-..-",
    "y": "-.--",
    "z": "--..",
    # Numbers
    "0": "-----",
    "1": ".----",
    "2": "..---",
    "3": "...--",
    "4": "....-",
    "5": ".....",
    "6": "-....",
    "7": "--...",
    "8": "---..",
    "9": "----.",
    # Punctuation
    "&": ".-...",
    "'": ".----.",
    "@": ".--.-.",
    ")": "-.--.-",
    "(": "-.--.",
    ":": "---...",
    ",": "--..--",
    "=": "-...-",
    "!": "-.-.--",
    ".": ".-.-.-",
    "-": "-....-",
    "+": ".-.-.",
    '"': ".-..-.",
    "?": "..--..",
    "/": "-..-.",
    " ": "/",
}

def from_english_to_morse(conversion_flag, txt, **kwargs):
    """
    Info: From English To Morse
    
    Write a function that converts English text to morse code and another one that does the opposite.
    Hint: Check the internet for a translation table, every letter is separated with a space and every word is separated with a slash /
    """
    try:
        if (conversion_flag == "direct") :
            result_list = list(map(lambda ch:kwargs.get(ch), txt))
            result = ' '.join(result_list)
        else:
            result_list = list(map(lambda mor:list(kwargs.keys())[list(kwargs.values()).index(mor)], txt.split(' ')))
            result = ''.join(result_list)
        
        return result
    except:
        print("Something went wrong when writing to the file")


conversion_flag1 = "direct"
str1 = "hello world"

conversion_flag2 = "indirect"
str2 = from_english_to_morse(conversion_flag1, str1, **morse)

str2_1 = "--- -. .-.. .. -. . / -.-. --- -- .--. .- .-. .. ... --- -."
str3 = from_english_to_morse(conversion_flag2, str2_1, **morse)

print(f"""
      _______________________________________\n
      
      Input: {str1} \n
      
      From English to Morse: {str2} \n
      From Morse to English: {str3}
      
      """)

