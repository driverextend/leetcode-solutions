# maybe a stack


def longestCommonPrefix(strs: list[str]) -> str:
    if len(strs) == 1:
        return strs[0]

    if "" in strs:
        return ""

    stack = list(strs[0])

    for word in strs:
        wordArr = list(word)
        while stack != wordArr:
            if len(stack) < len(wordArr):
                wordArr.pop()
            elif len(stack) == len(wordArr):
                stack.pop()
                wordArr.pop()
            else:
                stack.pop()
    return "".join(stack)


print(longestCommonPrefix(["ca", "c", "bba", "bacb", "bcb"]))
