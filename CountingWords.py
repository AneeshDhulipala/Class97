print('Write a sentence')
WriteSentence = input()
CharacterCount = 0
WordCount = 0

for i in WriteSentence : 
    CharacterCount = CharacterCount + 1
    if i == ' ':
        WordCount=WordCount+1
print('Number of Words are')
print(WordCount+1)
print('Number of characters is')
print(CharacterCount)

