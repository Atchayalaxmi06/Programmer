yab=raw_input()
vol={'a','e','i','o','u'}
cot={'b','c','d','f','g','h','j','k','l','m','n','p','q','r','s','t','v','w','x','y','z'}
if yab in vol:
  print("Vowel")
elif yab in cot:
  print("Consonant")
else:
  print("invalid")
