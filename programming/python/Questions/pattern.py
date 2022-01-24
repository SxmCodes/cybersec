'''
output 
1
22
333
4444
55555
'''

# This will call for 5 and this outer loop is for rows.
for i in range(6):
    # This loop is for coloumns.
    for j in range(i):
        # end=' ' will print a  space after the displayed string instead of a newline.
        print(i , end=' ')

    # This will print new line after each row.
    print(' ')

