# -*- coding:utf-8 -*-
'''
Created on 2015-03-17

@author: lisong
pangram:字母表所有的字母都出现(最好只出现一次)的句子
A pangram (Greek:παν γράμμα, pan gramma, 
"every letter") or holoalphabetic sentence for a given 
alphabet is a sentence using every letter of the alphabet 
at least once. Perhaps you are familiar with the well 
known pangram "The quick brown fox jumps over the lazy dog".

For this mission, we will use the latin alphabet (A-Z). 
You are given a text with latin letters and punctuation symbols.
 You need to check if the sentence is a pangram or not. Case does not matter.

Input: A text as a string.

Output: Whether the sentence is a pangram or not as a boolean.

Example:

check_pangram("The quick brown fox jumps over the lazy dog.") == True
check_pangram("ABCDEF.") == False
1
2
How it is used: Pangrams have been used to display typefaces, 
test equipment, and develop skills in handwriting, calligraphy, and keyboarding for ages.

Precondition:

all(ch in (string.punctuation + string.ascii_letters + " ") for ch in text)
0 < len(text)
'''
def check_pangram(text):
    show_letter = list()
    res = False
    for letter in text:
        if letter.isalpha():
            letter = letter.lower()
            if not(letter in show_letter):
                show_letter.append(letter)
                
    if len(show_letter) == 26:
        res = True
#     print show_letter, res
    
    return res

if __name__ == '__main__':
    # These "asserts" using only for self-checking and not necessary for auto-testing
    assert check_pangram("The quick brown fox jumps over the lazy dog."), "brown fox"
    assert not check_pangram("ABCDEF"), "ABC"
    assert check_pangram("Bored? Craving a pub quiz fix? Why, just come to the Royal Oak!"), "Bored?"
    
    '''
    from string import ascii_lowercase
​
​
    def check_pangram(text):
        return set(ascii_lowercase).issubset(set(text.lower()))
    '''