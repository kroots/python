#solve_me_second.py

def solveMeSecond(a,b):
   #print a, b
   return a+b


n = int(raw_input())   #faster than n = input() , since input() executes the line as python command
for i in range(0,n):
    a, b = raw_input().split()
    a,b = int(a),int(b)
    res = solveMeSecond(a,b)
    print res