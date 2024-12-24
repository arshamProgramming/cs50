

camel = input('came lcase: ')
for i in camel:
    if i.isupper():
        camel = camel.replace(i, '_' + i.lower())
print(camel)
