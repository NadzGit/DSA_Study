seen = {}
def first_non_repeating_char(s):
    for char in s:
        seen[char] = seen.get(char,0) +1
    
    for x in s:
        if seen[x] == 1:
            return x
    return "Nothing found"

print(first_non_repeating_char("poopy"))
      





