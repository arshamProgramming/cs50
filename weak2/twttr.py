vowels=['a','e','i','o','u']
userIN=input('input: ')
for i in userIN:
    if i.lower() in vowels:
        userIN =userIN.replace(i,'')
print(f'output: {userIN} ')