p = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,' ']

def inZeile(a,b):
    if b > 9: 
        print(a, end=' ')
    else:
        print(a, end='  ')

def anfangderZeile(a,b):
    if a > 9:
        if b > 9: 
            print(' ',a, end=' ')
        else:
            print(' ',a, end='  ')
    else:
        if b > 9: 
            print('  ',a, end=' ')
        else:
            print('  ',a, end='  ')
            
def print_pos(p):
    for i in range(len(p)):
        if (i-3)%4 == 0:
            print(p[i], end='\n')
        elif i%4 == 0:
            anfangderZeile(p[i], p[i+1])
        else:
            if i == 14: 
                print(p[i], end=' ')
            else:
                inZeile(p[i], p[i+1])
            
print_pos(p)