
def my_compare(x,y):
    if x % 2 == 0 and y % 2 == 0:
        return (x > y) - (x < y)
    if x % 2 != 0 and y % 2 != 0:
        return (x < y) - (x > y)
    if x % 2 == 0:
        return -1
    return 1