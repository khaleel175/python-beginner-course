contacts = {
    'number': 4,
    'students':[
        {'name': 'sayeed', 'email': 'sayeed@gmail.com'},
        {'name': 'khaleel', 'email': 'khaleel@gmail.com'},
        {'name': 'imran', 'email': 'imran@gmail.com'}
    ]
}

print('student emails:')
for student in contacts['students']:
    print(student['email'])
