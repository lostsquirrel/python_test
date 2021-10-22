#检查密码有效性
# 1。长度不小于10位
# 2。包含小写字母
# 3。包含大写字母
# 4。包含数字
import re
def checkio(data):
    """Return True if password strong and False if not"""
    return bool(len(data) >= 10 
                and [a for a in data if a.isupper()] 
                and [a for a in data if a.islower()] 
                and [a for a in data if a.isdigit()])
print('First ', 'Done' if checkio('A1213pokl')==False else 'wrong')
print('Second ', 'Done' if checkio('bAse730onE4')==True else 'wrong')

# def checkio(data):

#     #replace this for solution
#     if len(data) < 10 : return False
#     has_digit = False
#     has_lower = False
#     has_upper = False
#     for letter in data :
#     	if letter.isdigit():
#     		has_digit = True
#     		break;
#     for letter in data :
#     	if letter.isupper():
#     		has_upper = True
#     		break;
#     for letter in data :
#     	if letter.islower():
#     		has_lower = True
#     		break;		
#     return has_digit and has_lower and has_upper

# Some hints
# Just check all conditions
#
# ##
# These "asserts" using only for self-checking and not necessary for auto-testing
if __name__ == '__main__':
    assert checkio('A1213pokl') == False, "1st example"
    assert checkio('bAse730onE4') == True, "2nd example"
    assert checkio('asasasasasasasaas') == False, "3rd example"
    assert checkio('QWERTYqwerty') == False, "4th example"
    assert checkio('123456123456') == False, "5th example"
    assert checkio('QwErTy911poqqqq') == True, "6th example"