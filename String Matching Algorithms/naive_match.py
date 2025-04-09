string = "AABAACAADAABAAABAA"
pattern = "AABA"

n = len(string)
m = len(pattern)

count = 0
positions = []

for i in range(n-m+1):
    match = True

    for j in range(m):
        if string[i+j] != pattern[j]:
            match = False
            break
    
    if match:
        count += 1
        positions.append(i)

if count:
    print("Number of times the pattern occurs:", count)
    print("Positions where the pattern matches:", positions)
else:
    print("Pattern not found in the string.")