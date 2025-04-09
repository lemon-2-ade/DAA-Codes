def get_lps(pattern: str):
    
    m = len(pattern)
    lps = [0] * m
    j = 0
    i = 1   

    while i < m:
        if pattern[i] == pattern[j]:
            j += 1
            lps[i] = j
            i += 1
        else:
            if j != 0:
                j = lps[j - 1]
            else:
                lps[i] = 0
                i += 1

    return lps

def kmp_string_match(text: str, pattern: str):

    i = j = 0
    m = len(pattern)
    n = len(text)
    lps = get_lps(pattern)

    while i < n:
        if pattern[j] == text[i]:
            i += 1
            j += 1

        if j == m:
            print(f"Pattern found at index: {i-j}")
            j = lps[j-1]

        elif i < n and pattern[j] != text[i]:
            if j != 0:
                j = lps[j-1]
            else:
                i += 1

if __name__ == "__main__":

    pattern = "ABABCABAB"
    text = "BABABABABCABABCABAB"
    kmp_string_match(text, pattern)