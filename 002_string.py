my_sentence = "python is fun and powerful!"
print("Length of the string",len(my_sentence))
print("First character", (my_sentence[0]))
print("Substring", (my_sentence[10:]))
print("Lowercase:", my_sentence.lower())
print("Count of 'o':", my_sentence.count('o'))
print("Index of 'fun':", my_sentence.find('fun'))
new_sentence = my_sentence.replace('powerful', 'amazing')
print("Modified sentence:", new_sentence)
new_message = "Learning python is exciting!"
concat_1 = my_sentence + " " + new_message
print("Concatenation using +:", concat_1)
concat_2 = "{} {}".format(my_sentence, new_message)
print("Concatenation using format():", concat_2)
concat_3 = f"{my_sentence} {new_message}"
print("Concatenation using f-string:", concat_3)
print("Available methods:", dir(my_sentence))
help(str.replace)
