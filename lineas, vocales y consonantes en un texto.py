text = '''Once there was an elephant,
Who tried to use the telephant
No! No! I mean an elephone
Who tried to use the telephone'''
vowels = 0
consonants = 0
counter = 0
CoList = text.split("\n")
for i in CoList:
    if i:
        counter += 1
for t in text:    
    if (t == 'a' or t == 'e' or t == 'i' or t == 'o' or t == 'u'
       or t == 'A' or t == 'E' or t == 'I' or t == 'O' or t == 'U'):
        vowels = vowels + 1
    else:
        consonants = consonants + 1

print(f'Number of Lines: {counter}')
print("Number of Vowels: ", vowels)
print("Number of Consonants: ", consonants)