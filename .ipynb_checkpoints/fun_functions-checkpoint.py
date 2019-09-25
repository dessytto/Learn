def numJewelsInStones(J, S):
    """
    :type J: str
    :type S: str
    :rtype: int
    """
    counter = 0
    for i in range(len(S)):
        if S[i] in J:
            counter += 1
            print(S[i], i)
    return(counter)
    
def FizzBuzz(n):
    for i in range(1,n):
        if ((i%3 == 0) and (i%5 ==0)):
            print('FizzBuzz')
        elif i%3 == 0:
            print('Fizz')
        elif i%5 == 0:
            print('Buzz')
        else:
            print(i)

def toLowerCase(str):
    return str.lower()

# 961. N-Repeated Element in Size 2N Array
def repeatedNTimes(A):
    B = []
    for i in range(len(A)):
        if A[i] not in B:
            B.append(A[i])
        else:
            return A[i]
        
###########################################
        
def selfDividingNumbers(left, right):
    mylist = []
    for i in range(left, right+1):
        if '0' not in str(i):
            flag = 1
            for j in str(i):
                if not i%int(j) == 0:
                    flag = 0
            if flag == 1:
                mylist.append(i)
    return(mylist)
    
    
def fib(N):
    if N <=1:
        return N
    else:
        return fib(N - 2) + fib(N - 1)


# 977. Squares of a Sorted Array    
def sortedSquares(A):
    AA = []
    for i in range(len(A)):
        
        AA.append(A[i]**2)
    AA.sort()
    return(AA)

def sortedSquares2(A):
    AA = [A[i]**2 for i in range(len(A))]
    AA.sort()
    return(AA)
####################################

# 905. Sort Array By Parity
def sortArrayByParity(A):
    B = []
    for i in range(len(A)):
        if A[i]%2 ==0:
            B.insert(0,A[i])
        else:
            B.append(A[i])
    return(B)


#1002. Find Common Characters
def commonChars(A):
    letters_in_all = []
    for letter in A[0]:
        letter_is_in_all = 1
        for i in range(1, len(A)):
            if letter not in A[i]:
                letter_is_in_all = 0
        if letter_is_in_all == 1:
            letters_in_all.append(letter)
            A = [w.replace(letter, '',1) for w in A]
    return(letters_in_all)


# A program that rolls a dice N times 
# and displays how many times each number was rolled
def rollDice(N):
    import random
    dice = [random.randint(1,6) for i in range(N)]
    print('1: ', dice.count(1), ' times')
    print('2: ', dice.count(2), ' times')
    print('3: ', dice.count(3), ' times')
    print('4: ', dice.count(4), ' times')
    print('5: ', dice.count(5), ' times')
    print('6: ', dice.count(6), ' times')

## A function that reverses the order of words in a string
def reverseOrder(S):
    S = S.split()
    S_reversed = []
    for i in range(len(S)):
        S_reversed.insert(0, S[i])
    S_reversed = ' '.join(S_reversed)
    return(S_reversed)
    

        

def bubble_sort(L):
    ssorted = 0
    while ssorted == 0:
        ssorted = 1
        for i in range (len(L)-1):
            #temp = 0
            if L[i] > L[i+1]:
                L[i], L[i+1] = L[i+1], L[i]
                ssorted = 0
    return(L)
        




def calculate_median(l):
    l = sorted(l)
    l_len = len(l)
    if l_len < 1:
        return None
    if l_len % 2 == 0 :
        return ( l[(l_len-1)/2] + l[(l_len+1)/2] ) / 2.0
    else:
        return l[(l_len-1)/2]
    
def Binary_search(L, k):
    L = sorted(L)
    i = len(L)//2
    if i == 0 and k != L[i]:
        return False
    elif k == L[i]:
        return True
    elif k > L[i]:
        return Binary_search(L[i:], k)
    elif k < L[i]:
        return Binary_search(L[:i], k)
    























