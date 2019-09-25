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
    
    
    
house_colors = ['b']*10    
n=2
for colorscheme in range(3**n):
    helper = colorscheme
    helper2 = n
    for ihouse in range(n):
        # Color scheme is base-3
        if (ihouse == 0):
            color_of_ith_house = colorscheme % 3
        else:
            color_of_ith_house = (colorscheme / (3*ihouse)) % 3
        if (color_of_ith_house == 0):
            house_colors[ihouse] = 'b'
        if (color_of_ith_house == 1):
            house_colors[ihouse] = 'g'
        if (color_of_ith_house == 2):
            house_colors[ihouse] = 'r'             
    print(house_colors)

Programming 2
Point Value: 20 points
Suppose there are  houses on one side of a street. It costs  dollars to paint house  blue,  dollars to paint it in green, and  dollars to paint it in red. You are tasked to paint the  houses such that no two neighboring houses are painted in same color.

In this problem, you will write Python3 code in the code editor below to complete the lowest_cost function, which takes in three lists of length : blue_costs, green_costs, red_costs. The  element of blue_costs is , the  element of green_costs is , and the  element of red_costs is . Each element in the lists is a positive integer.

Your task is to output a list representing the coloring scheme for each of the  houses that has minimum total cost. Specifically, your output list will be of length , where each element in the list is either 'b', 'g', or 'r'. The  element of the output list represents the color of house  in your minimum cost coloring scheme. Note that there will be exactly 1 minimum cost coloring scheme.

A few examples are provided below:

For inputs
blue_costs = [1, 1, 1]
green_costs = [3, 5, 7]
red_costs = [4, 6, 4]

the output list should be ['b', 'g', 'b'] (total cost of 7). Painting each house blue would be the cheapest, but remember that no two neighboring houses can be the same color.

For inputs
blue_costs = [18, 12, 1, 9]
green_costs = [13, 15, 7, 9]
red_costs = [12, 16, 4, 8]

the output list should be ['r', 'g', 'b', 'r'] (total cost of 36).

For inputs
blue_costs = [100, 1, 76, 14]
green_costs = [22, 20, 1, 2]
red_costs = [99, 99, 5, 12]

the output list should be ['g', 'b', 'r', 'g'] (total cost of 30).

You can write your own test cases in the input text box. In this case, your test case should be three space-separated lists of comma-delimited integers, representing the blue_costs, green_costs, and red_costs inputs, respectively. An example custom test case input would be:

1,2,3 11,7,1 5,5,5

which represents blue_costs = [1, 2, 3], green_costs = [11, 7, 1], red_costs = [5, 5, 5].

When you finish coding, click the  button to get results from an input set. Any output from the testing (print statements, errors, etc.) will be displayed in the console, as well as results from the test cases. The number of test inputs your algorithm is correct on will also be displayed in the console after running your code. Note that when you submit your interview we will test your algorithm on hidden input sets.













# COMPLETE THE FUNCTION

# check if a color combination is acceptable
def is_acceptable(house_colors):
    for i in range(len(house_colors)-1):
        if house_colors[i] == house_colors [i+1]:
            return False
    return True
    

def lowest_cost(blue_costs, green_costs, red_costs):
    lowest_so_far = float('inf')

    n = len(blue_costs)
    house_colors = ['b' for i in range(n)]
    
    #for ihouse in range(n):
    #    for icolor in ['b', 'g', 'r']:
            
    
    for colorscheme in range(3**n):
        for ihouse in range(n):
            # Color scheme is base-3
            if (ihouse == 0):
                color_of_ith_house = colorscheme % 3
            else:
                color_of_ith_house = int(colorscheme / (3*ihouse)) % 3
            if (color_of_ith_house == 0):
                house_colors[ihouse] = 'b'
            if (color_of_ith_house == 1):
                house_colors[ihouse] = 'g'
            if (color_of_ith_house == 2):
                house_colors[ihouse] = 'r'             
        #print(house_colors)

        cost = 0
        for i in range(n):
            if house_colors[i] == 'b':
                cost += blue_costs[i]
            if house_colors[i] == 'g':
                cost += green_costs[i]
            else:
                cost += red_costs[i]            
            
        if is_acceptable(house_colors):
            if (cost < lowest_so_far):
                cost = lowest_so_far
                best_coloring = house_colors
    return best_coloring
    





