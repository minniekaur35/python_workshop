print("This is a spelling checker project.")


from textblob import TextBlob

def correct_sentence_spelling(sentence):
    
    sentence = TextBlob(sentence)
    
    result = sentence.correct()
    
    print(result)

line = input("please enter a line: ") 
correct_sentence_spelling(line)