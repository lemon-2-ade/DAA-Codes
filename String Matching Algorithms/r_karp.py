def rabin_karp_match(text: str, pattern: str):

    d = 256
    q = 101

    n = len(text)
    m = len(pattern)

    pattern_hash = 0
    text_hash = 0
    h = 1

    for i in range(m - 1):
        h = (h * d) % q
    
    for i in range(m):
        pattern_hash = (d * pattern_hash + ord(pattern[i])) % q
        text_hash = (d * text_hash + ord(text[i])) % q
    
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

    text = 'abbabbcdabbaeganna'
    pattern = 'abba'

    indices = rabin_karp_match(text, pattern)
    
    if indices:
        print(f"Indices: {indices}")
    else:
        print("No such match found!")