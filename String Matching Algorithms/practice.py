def kmp_string_match(pattern: str, text: str):   
    m, n = len(pattern), len(text)
    i = j = 0

    def get_lps(pattern: str):
        m = len(pattern)
        lps = [0] * m
        i, j = 1, 0

        while i < m:
            if pattern[i] == pattern[j]:
                j += 1
                lps[i] = j
                i += 1
            else:
                if j == 0:
                    lps[i] = 0
                    i += 1
                else:
                    j = lps[j - 1]
        
        return lps
    
    lps = get_lps(pattern)
    indices = []

    while i < n:
        if text[i] == pattern[j]:
            i += 1
            j += 1
        
        if j == m:
            index = i - j
            indices.append(index)
            j = lps[j - 1]
        elif i < n and text[i] != pattern[j]:
            if j == 0:
                i += 1
            else:
                j = lps[j - 1]
    
    return indices

def rabin_karp_match(pattern: str, text: str):

    m, n = len(pattern), len(text)
    q, d, h = 101, 256, 1
    pattern_hash = text_hash = 0

    for i in range(m - 1):
        h = (h * d) % q
    
    for i in range(m):
        text_hash = (d * text_hash + ord(text[i])) % q
        pattern_hash = (d * pattern_hash+ ord(pattern[i])) % q
    
    indices = []
    
    for i in range(n - m + 1):
        if pattern_hash == text_hash:
            if text[i:i+m] == pattern:
                indices.append(i)
        
        if i < n - m:
            text_hash = (d * (text_hash - ord(text[i]) * h) + ord(text[i+m])) % q
            if text_hash < 0:
                text_hash += q
    
    return indices

if __name__ == '__main__':

    pattern = "ABABCABAB"
    text = "BABABABABCABABCABAB"

    indices = rabin_karp_match(pattern, text)
    print(f"Indices: {indices}")