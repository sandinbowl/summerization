text = "i like apple. apple is good. wow."

# temp = text.split('.')
# sents = []
# for  t in temp:
#     if t != '' and i != ' ':
#         sents.append(t.strip())

sents = [i.strip() for i in text.split('.') if i != '' and i != ' ']

# print(sents)

