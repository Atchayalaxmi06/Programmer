yab=input()
vol={'a','e','i','o','u' or 'A','E','I','O','U'}
cot={'b','c','d','f','g','h','j','k','l','m','n','p','q','r','s','t','v','w','x','y','z' or
     'B','C','D','F','G','H','J','K','L','M','N','P','Q','R','S','T','V','W','X','Y','Z'}
if yab in vol:
  print("Vowel")
elif yab in cot:
  print("Consonant")
else:
  print("invalid")
