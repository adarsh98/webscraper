import json

with open('quotedata.json') as json_data:
    data = json.load(json_data)

quote_list = []

for i in data:
    quote_list.append(i['Quote'])

new_list = []

for i in range(len(quote_list)):
    val = quote_list[i]
    new_list.append(val[1:(len(val) - 1)]) 

for i in range(len(quote_list)):
    quote_list[i] = str(quote_list[i])

for i in range(len(quote_list)):
    quote_list[i] = ''.join(quote_list[i])

words = []

for i in new_list:
    words.append(i.split())

word_dict = {} 

for i in range(len(words)):
    for j in (words[i]):
        if j not in word_dict:
            val = j
            word_dict[val] = 1
        else:
            val = j
            word_dict[val] += 1

maxi = 0

for k in word_dict:
    if(word_dict[k] > maxi):
        maxi = word_dict[k]
        most_word = k

print("The most used word is", most_word, "and it is used", maxi, "times.")

    