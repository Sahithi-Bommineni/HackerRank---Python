# Mr. Vincent works in a door mat manufacturing company. One day, he designed a new door mat with the following specifications:

# Mat size must be X. (N is an odd natural number, and M is 3 times N.)
# The design should have 'WELCOME' written in the center.
# The design pattern should only use |, . and - characters.
# Sample Designs

#     Size: 7 x 21 
#     ---------.|.---------
#     ------.|..|..|.------
#     ---.|..|..|..|..|.---
#     -------WELCOME-------
#     ---.|..|..|..|..|.---
#     ------.|..|..|.------
#     ---------.|.---------
    
#     Size: 11 x 33
#     ---------------.|.---------------
#     ------------.|..|..|.------------
#     ---------.|..|..|..|..|.---------
#     ------.|..|..|..|..|..|..|.------
#     ---.|..|..|..|..|..|..|..|..|.---
#     -------------WELCOME-------------
#     ---.|..|..|..|..|..|..|..|..|.---
#     ------.|..|..|..|..|..|..|.------
#     ---------.|..|..|..|..|.---------
#     ------------.|..|..|.------------
#     ---------------.|.---------------
# Input Format

# A single line containing the space separated values of N and M.

# Constraints

# Output Format

# Output the design pattern.

# Sample Input

# 9 27
# Sample Output

# ------------.|.------------
# ---------.|..|..|.---------
# ------.|..|..|..|..|.------
# ---.|..|..|..|..|..|..|.---
# ----------WELCOME----------
# ---.|..|..|..|..|..|..|.---
# ------.|..|..|..|..|.------
# ---------.|..|..|.---------
# ------------.|.------------

# Enter your code here. Read input from STDIN. Print output to STDOUT
def top(n,m):
    for i in range(n):
        if i%2!=0 and i<=(n-2):
            print((".|."*i).center(m,"-"))
def bottom(n,m):
    for i in range(n,0,-1):
      if i%2!=0 and i<=(n-2):
            print((".|."*i).center(m,"-"))  
user = input()
user = user.split()
n = int(user[0])
m = int(user[1])
string = "WELCOME"
if(n%2!=0 and m==n*3):
    top(n,m)
    print(string.center(m,'-'))
    bottom(n,m)
