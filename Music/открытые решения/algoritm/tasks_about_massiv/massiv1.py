import os

def sum_numbers(name):
    summa=0
    if (os.stat(name).st_size == 0):
        return 0      
    else:
        with open(name,'r') as f:
            for row in f:
                summa+=int(row)
        return summa

