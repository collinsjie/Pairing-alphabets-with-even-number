alphabets = input('>')
even_numbers = list(range(2,len(alphabets)*2+1,2))
pair = {alphabet: number for alphabet, number in zip(alphabets, even_numbers)}
print(pair)

#Alternatively:
string=input('>')
even= list(range(2,len(string)*2 +1,2))
mydict={string[i]:even[i] for i in range(len(string))}
print(mydict)
