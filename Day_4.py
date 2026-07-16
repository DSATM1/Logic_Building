###----- Pseudocode----##### 
# Step 1 - Build frequency dictionary:
# create freq = {}
# for each word in sentence:
#          freq[word] = freq.get(word, 0) + 1
# Step 2 - Find most frequent word: words = sent.split()
# result = words[0]
# for each word in freq:
#     if freq[word] > freq[result]:
#        result = word 
# print result



###----Code----###
words = "the cat sat on the mat the cat"