from collections import Counter, defaultdict, OrderedDict

# li = [12, 13, 14, 15, 16, 17, 17]
# sentence = 'hi hi hihi hi I am Saleh'
# print(Counter(li))
# print(Counter(sentence))
# print("\n")

# dictionary = defaultdict(lambda: 'default item',
#                          {
#                              "first": 'me',
#                              "second": 'also me',
#                              "third": 'am I naricisst?'
#                          })

# print(dictionary['third'])

# d_order = OrderedDict()
# d_order[56] = "Marker pen"
# d_order[50] = "Smoothy pen"

# print(d_order.keys())


import datetime

# print(datetime.time(5, 45, 2))
# print(datetime.date.today())


from array import array

arr = array('i', [12, 111, 566])

for item in arr:
    print(item, end="  ")
