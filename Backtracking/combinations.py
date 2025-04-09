def get_combinations(letters):

    def backtrack(path: list, index: 0):
        if index == len(letters):
            combinations.append(''.join(path))
            return
        
        for letter in letters:
            if letter in path:
                continue
            
            path.append(letter)
            backtrack(path, index + 1)
            path.pop()
            
    
    combinations = []
    backtrack([], 0)

    return combinations

if __name__ == "__main__":

    letters = 'a b c'.split()
    combinations = get_combinations(letters)
    print(" ".join(combinations))