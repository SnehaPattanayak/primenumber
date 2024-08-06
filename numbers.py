#checking for Even 
def isEven(n):
   if n%2==0:
      return True
   else:
      return False

#checking for Prime
def isPrime(n):
   if n>1:
      for i in range(2,n//2+1):
         if n%i==0:
            return False
      else:
         return True

#checking for Palindrome
def isPalindrome(n):
   t=n
   rev=0
   while t>0:
      d=t%10
      rev=rev*10+d
      t//=10
   if rev==n:
      return True
   else:
      return False

#checking for PaliPrime
def isPaliPrime(n):
   if isPrime and isPrime:
      return True
   else:
      return False

#checking Armstrong
def isArmstrong(n):
   lgth=len(str(n))
   t=n
   s=0
   while t>0:
      d=t%10
      s=s+d**lgth
      t/=10
   if s==n:
      return True
   else:
      return False


#checking for Disarium
def isDiasrium(n):
   t=n
   s=0
   dp=len(str(t))
   while t>0:
      d=t%10
      s=s+d**dp
      t/=10
   if s==n:
      return True
   else:
      return False


#checking for Special
def isSpecial(n):
   t=n
   s=0
   while t>0:
      d=t%10
      fact=1
      for f in range(1,d+1):
         fact*=f
      s+=fact
      t/=10
   if s==n:
      return True
   else:
      return False
   

#checking for Perfect
def isPerfect(n):
   s=0
   for f in range(1,n//2+1):
      if n%f==0:
         s+=f
   if s==n:
      return True
   else:
      return False


#checking for Harshad
def isHarshad(n):
   t=n
   s=0
   while t>0:
      d=t%10
      s+=d
      t//=10
   if n%s==0:
      return True
   else:
      return False


#checking for Special
def isSpecial(n):
   t=n
   s=0
   while t>0:
      d=t%10
      fact=1
      for f in range(1,d+1):
         fact*=f
      s+=fact
      t//=10
   if s==n:
      return True
   else:
      return False

'''#checking for Anagram
def isAnagram(a,b):
   if len(a)=len(b):
      #sorted()    
'''

n=int(input())
def call(n):
   if isEven(n):
      print("Even")
   if isPrime(n):
      print("Prime")
   if isPalindrome(n):
      print("Palindrome")
   if isArmstrong(n):
      print("Armstrong")
   if isDiasrium(n):
      print("Diasrium")
   if isSpecial(n):
      print("Special")
   if isHarshad(n):
      print("Harshad")
   else:
      print("None")
call(n)


