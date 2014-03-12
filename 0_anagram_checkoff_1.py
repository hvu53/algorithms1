# Method1: Checking Off
# Check to see that each character in the first string actually occurs in the second.
# If it is possible to checkoff each character, the 2 strings must be anagrams
# Checking off a character will be accomplished by replacing it with None

def anagram(s1,s2):
   alist = list(s2)

   pos1 = 0
   stillOK = True

   while pos1 < len(s1) and stillOK:
      pos2 = 0
      found = False
      while pos2 < len(alist) and not found:
         if s1[pos1] == alist[pos2]:
            found = True
         else:
            pos2 +=1

      if found:
         alist[pos2] = None
      else:
         stillOK = False

      pos1 +=1

   return stillOK

##print(anagram('abcd','dcba'))
##
##def anagram(s1,s2):
##   r = True
##   for i in s1:
##      if i not in s2:
##         r = False
##   return r

print(anagram('abcd','dcba'))
print(anagram('abce','dcba'))
