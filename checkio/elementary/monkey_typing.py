# -*- coding:utf-8 -*-
'''
Created on 2015-03-06

@author: lisong
'''
def count_words(text, words):
    amount = 0
    for w in words:
        if w in text.lower():
            amount += 1
    return amount
''

if __name__ == '__main__':
    #These uu"1sserts" using only for self-checking and not necessary for auto-testing
    print(count_words("How aresjfhdskfhskd you?", {"how", "are", "you", "hello"}))
    assert count_words("How aresjfhdskfhskd you?", {"how", "are", "you", "hello"}) == 3, "Example"
    assert count_words("Bananas, give me bananas!!!", {"banana", "bananas"}) == 2, "BANANAS!"
    assert count_words("Lorem ipsum dolor sit amet, consectetuer adipiscing elit.",
                       {"sum", "hamlet", "infinity", "anything"}) == 1, "Weird text"

'''
def count_words(text, words):
    return sum(w in text.lower() for w in words)
    
'''
