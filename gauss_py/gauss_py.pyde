# divisor = 2
# row = [1,2,3,4,5]

def gauss(A):
    """converts a matrix into the identity matrix by gaussian elimination,
    with the last column containing the solutions to the variables."""
    """solving equations like this:
        2x+y-z=8
        -3x-y+2z=-1
        -2x+y+2z=-3
        """
    m = len(A)
    n = len(A[0])
    for j,row in enumerate(A):
    #diagonal term to be 1
    #by dividing row by diagonal term
        if row[j] != 0: #diagonal term cant be 0
            divisor = row[j] #diagonal term
            for i, term in enumerate(row):
                row[i] = term / divisor
        #add the other rows to the additive inverse for every row        
        for i in range(m):
            if i != j: #dont do it to row j
                #calculate the additive inverse
                addinv = -1*A[i][j] #for every term in the ith row
                for ind in range(n):
                    #add the correrponding term in the jth row
                    #multiplied by the additive inverse
                    #to the term in the ith row
                    A[i][ind] += addinv*A[j][ind]
    return A

B = [[2,1,-1,8],[-3,-1,2,-1],[-2,1,2,-3]]
print(gauss(B))    

# for i, term in enumerate(row):
#     row[i] = term / divisor
# # print(row)


            
