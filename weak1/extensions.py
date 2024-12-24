fname = input('File name: ').strip().lower()

if fname.endswith('.gif'):
    print('image/gif')

elif fname.endswith('.jpg') or f.endswith('.jpeg'):
    print('image/jpeg')

elif fname.endswith('.png'):
    print('image/png')
