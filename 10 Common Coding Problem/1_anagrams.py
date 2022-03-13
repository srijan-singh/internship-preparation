def anagram(str1:str, str2: str) -> bool:
    
    # Reference
    memo1 = {}
    memo2 = {}

    for i in str1:
        # If character is repeated
        if i in memo1:
            memo1[i] += 1
        # New character
        else:
            memo1[i] = 1

    for i in str2:
        if i in memo2:
            memo2[i] += 1
        else:
            memo2[i] = 1

    for i in memo1:
        
        # Character dosen't exist in second string
        if i not in memo2:
            return False

        # Character's repitition isn't same
        if memo1[i] != memo2[i]:
            return False

    return True


if __name__ == "__main__":

    str1 = "nameless"
    str2 = "salesmen"

    print(anagram(str1, str2))
        

