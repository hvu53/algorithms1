# Method2:  Sort and compare
# s1 and s2 are different, they are anagrams only if they consist of exactly the same characters

def anagram(s1,s2):
   alist1 = list(s1)
   alist2 = list(s2)

   alist1.sort()
   alist2.sort()

   pos = 0
   matches = True
   while pos < len(s1) and matches:
      if alist1[pos] == alist2[pos]:
         pos += 1
      else:
         matches = False
   return matches


##print(anagram('abcd','dcba'))


print(anagram('abcd','dcba'))
print(anagram('abce','dcba'))
