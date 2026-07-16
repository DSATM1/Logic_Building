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
"""sent = "the cat sp sat on the sp mat sp the cat sp "
freq = {}
for word in sent.split():
    freq[word] = freq.get(word, 0) + 1

words = sent.split()
result = words[0]
for word in freq:
    if freq[word] > freq[result]:
        result = word

print(result)"""

###----- Pseudocode----##### 
# create lst and target
# create result = []
# for i in range(len(lst)):
# for j in range(i+1, len(lst):
# if lst[i] + lst[j] == target:
# result.append((lst[i], lst[j]))
# print result


###----Code----###
"""lst = [1, 2, 3, 4, 5]
target = 5
result = []
for i in range(len(lst)):
    for j in range(i+1, len(lst)):
        if lst[i] + lst[j] == target:
            result.append((lst[i],lst[j]))
print(result)"""  




###----- Pseudocode----##### 
# ok input - words of sent 
# output - only words longer than 4 char 
# rule :
# create a sent of words 
# create count = 0 
# for each item in sent.split() :
#            if len(item) > 4 : 
#                 count += 1
# print(count)



###----Code----###