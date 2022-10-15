doc = input()
sentence = input()

doc = doc.replace(sentence, '_')
print(doc.count('_'))