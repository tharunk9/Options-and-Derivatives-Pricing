import numpy as np
import random 

s0 = 47.84 #spot price
r  = 0.03  #risk free rate
v  = 0.38 # volatility
m  = 100  #number of days to maturity
n  = 365
t = np.sqrt(1/365) #Delta T
u = np.exp(v*t)
d = 1/u
p = (np.exp(r*(1/365)) - d) / (u-d) 
df = np.exp(r*(-100/365)) #discounting Factor

print("---------PART 1---------")
def option(price): # to check option price and returns 100 if it's between 50 and 60
    if 50 < price <=60:
          return 100
    else: return 0
 
payoff = []
for i in range(100000):
    s0 = 47.84
    for j in range(m): # iteration for number of days to maturity-> m
        if p > random.uniform(0,1): 
              s0 = s0*u
        else: s0 = s0*d
            
            
    payoff.append(df*option(s0))
    
print('With Monte Carlo Simulation, binomial option price is : ', np.mean(payoff))    
print('this model simulated the mean of 100, 000 in randomwalk for price moments.',
     'As per law of large numbers, I think this has better price predictibility with given conditions.')


#---------------------------------PART 2-------------------------------------------------------

print("",
    "---------PART 2---------")

def bin_call(n,s0,v,r):
    tp = np.zeros([n+1, n+1]) #price of the tree
    
    
    for i in range(n+1): #creating a matrice with u and d factors
        for j in range(i+1):
            tp[j,i]= s0*(d**j)*(u**(i-j))
            
    price = np.zeros([n+1,n+1]) 
    for i in range(n):
        price[i,n] = tp[i,n]
    
    for i in np.arange(n-1, -1, -1): #arranging the tree, as the price is calculated from backward
        for j in np.arange(0,i+1):
            price[j,i] = np.exp(-r*1/365) * (p*price[j,i+1] + (1-p)*price[j+1, i+1])
    return price[0,0] # price at root node of the tree.
    
c= bin_call(n,s0,v,r)/2
print('Theoritical Binomial Price: ', c)
    
print('the price needed to calculate using binomial trees is computationally inefficient as the number of steps increase ',
    'Also, the uncertainity in probabilities is difficult to estimate for practical purposes.',
    'so I would prefer monte carlo simulation although it is computationally exaustive as this.')
#------------------------------------Part 3-------------------------------------------------
print("---------PART 3---------")
ov = [] #option value
strike = []
x = 1+ r/365

for i in range (100000):
    s0 = 47.84
    for j in range(100):
        ra= np.random.normal(0,1) #creating the random variable from normally distributed range of 0 to 1
        s0 = ((s0*x) + v / (np.sqrt(365)*ra))
    strike.append(s0)
    
    if 50< strike[i] <= 60: # if between 50 to 60, appends 100 else 0
        ov.append(100)
    else: ov.append(0)
  
realistic = np.mean(ov)*np.exp(-ra*1/365) #price discounting
print('the realistic option price is: ', realistic)

print("The changes are made with respect to the interest rate by taking additional factor ra into condideration",
    'which was passed through random variable of a normal distribution of range 0 to 1')







