
dataTxt = '''b	b	b	w	b	b	w
b	w	b	w	b	w	b
b	b	b	w	b	b	w
b	w	b	w	b	w	b
b	w	b	w	b	b	w
w	w	w	w	w	w	w
b	b	b	w	b	b	b
w	b	w	w	b	w	w
w	b	w	w	b	b	w
w	b	w	w	b	w	w
w	b	w	w	b	b	b
w	w	w	w	w	w	w
b	b	b	w	b	w	b
b	w	w	w	b	w	b
b	w	w	w	b	b	b
b	w	w	w	b	w	b
b	b	b	w	b	w	b
w	w	w	w	w	w	w'''

data = [
    [0 if i == "b" else 255 for i in row.split('\t')] for row in dataTxt.split('\n')
]

def update(input):
    global data
    if input == 't':
        data = [
            [0 if pixel == 255 else 255 for pixel in row]
            for row in data
        ]
    return data
