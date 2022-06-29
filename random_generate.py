# random generator [7, 20)
import random

# print(random.random())

# this method will return a random generated value between 7 and 20

def random_number(start, end): 
    OriginalRandNo = random.random() #this is  a random number from 0 to 1
    ExpandedRandomRange = OriginalRandNo * abs(end - start) # (here  13 is differencce between two numbers)
    # ^ now range has expanded from 0-1 to 0-13
    FInalRandNumber = ExpandedRandomRange + start # < this moved range from 0-13 to 7 -  20

    # return 13 * random.random() + 7
    return FInalRandNumber

# for i in range(20):
    # print(f"try no. {i} : {random_number(7, 20)}")

print( random.uniform(23, 26))
print( random_number(23, 26))

print(random.randint(1, 6))
print("generate your Punjabi baby name: ")
prefixx = ['sukh', 'jas', 'man', 'jag', 'ras', 'gur', 'har', 'bal', 'sharan']
sufixx = ['deep', 'preet', 'jeet', 'pinder', 'winder', 'roop', 'neet', 'pal']

print(random.choice(prefixx) + random.choice(sufixx)) 

# print( s_game[random.randint(0, len(s_game) - 1 )] )
