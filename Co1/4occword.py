sent = input("enter the text = ")
words = sent.split(' ')
count = {}
for word in words:                                                                                                                                                                                              
    count[word] = count.get(word, 0) + 1   
print(count)        
