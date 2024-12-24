inp=input('greeting: ').strip().lower()
if inp.startswith('hello'):
    print('$0')
elif inp.startswith('h'):
    print('$20')
else:
    print('$100')