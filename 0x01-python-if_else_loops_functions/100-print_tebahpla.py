#!/usr/bin/python3
start_i = 122
end_i = 96
dec_i = -1
for i in range(start_i, end_i, dec_i):
    if(i % 2 != 0):
        i -= 32
    print('{}'.format(chr(i)), end='')
