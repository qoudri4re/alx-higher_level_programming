#!/usr/bin/python3
def magic_calculation(a, b):
    var = 0
    for i in range(1, 3):
        try:
            if (i > a):
                raise Exception('Too far')
            else:
                var += (a**b)/i
        except Exception as e:
            var = (b + a)
            break
    return var
