'''
This is what we want :-
5 4 3 2 1 
4 3 2 1 
3 2 1 
2 1 
1
'''

rows = 5
coloumn = 5
for i in range(0, rows+1):
    for j in range(coloumn-i, 0, -1):
        print(j, end=' ')
    print()
