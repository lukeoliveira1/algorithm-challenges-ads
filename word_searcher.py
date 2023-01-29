cont = 0
with open("corpus.txt", "r", encoding='utf-8') as document:
    for f in document.readlines():
        # readlines returns a list containing each file line as a list item.
        if f.find('bottle') > -1:
            # find = returns the index of first occurrence of a sub-string within another
            cont += f.count('bottle')
            # count = return the number of occurrences of a substring within a string
            print(f.find('bottle'))
            print(f)

print("repetitions: ", cont)
