needle = input()
haystack = input()

count = 0

for i, c in enumerate(haystack):
    if haystack[i:i+len(needle)] == needle:
        count += 1

print(count)
