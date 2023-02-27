number = []#Establishing an empty list
number.extend([5, 6, 7])# adding multiple items to the empty list from before ( could be established with these numbers however this was done for practice )
print(number)
print(number[0])
print(len(number))
letter = []
letter.append(4)
letter.append('testing')
print(letter)
print(number+letter)
y = 0
for x in number:
    y = y + x
    print(x)
print(y)
number.append(letter)
print(number[-1][-1])
