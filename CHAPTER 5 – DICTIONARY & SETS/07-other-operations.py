# 3. Difference (- or .difference())
''' Pehle set ke wo elements deta hai jo dusre me
nahi hain Used in data filtering.'''
set1 = {1,2,45,23,78}
set2 = {1,2,44.34,89}
set3 = set1.difference(set2)
set4 = set1-set2
print(set3)
print(set4)

# 4. Symmetric Difference (^ or .symmetric_difference())
'''Dono sets ke unique (non-common) elements deta hai.
Medium importance.'''
set5 = set1.symmetric_difference(set2)
set6 = set1^set2
print(set5,set6)