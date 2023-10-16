"""
File: columnar.py
Name: Marcus Persson (m.h.o.persson@student.rug.nl)

Description:
    This program is a recreation of columnar transposition.
"""


def create_table(_sentence, _column_order):
    _column_length = len(_column_order)
    _lst = []

    for i in range(0, len(_sentence), _column_length):
        _row = []
        _column_cnt = 0
        for j in range(_column_length):
            if i + j < len(_sentence):
                _column_cnt += 1
                _row.append(_sentence[i + j])
        # In the event there are incomplete rows we're just appending with an empty string.
        while _column_cnt < _column_length:
            _row.append('')
            _column_cnt += 1
        _lst.append(_row)

    return _lst


sentence = input()
column_order = input()

lst = create_table(sentence, column_order)
encoded_lst = []

for column in range(len(column_order)):
    pos = str(int(column) + 1)
    pos = column_order.index(pos)
    for i in range(len(lst)):
        encoded_lst.append(lst[i][pos])

print(''.join(encoded_lst))
