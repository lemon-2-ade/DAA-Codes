from typing import List

def get_combinations(characters: List[str]):
    
    def backtrack(path: List[str], index: int):
        if path:
            result.append("".join(path))
        
        for i in range(index, len(characters)):
            path.append(characters[i])
            backtrack(path.copy(), i + 1)
            path.pop()

    result = []
    backtrack([], 0)
    return sorted(result)

if __name__ == "__main__":
    characters = "a b c d e".split()
    combinations = get_combinations(characters)
    print(combinations)