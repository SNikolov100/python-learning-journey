def palindrome(word, index):
    if word[index] != word[-1 - index]:
        return f"{word} is not a palindrome"
    border = len(word) // 2
    if index == border:
        return f"{word} is a palindrome"
    return palindrome(word,index + 1)



print(palindrome("abcba", 0))
print("======================")
print(palindrome("peter", 0))