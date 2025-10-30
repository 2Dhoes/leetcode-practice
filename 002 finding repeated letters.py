    result = []

    for a,b in zip(word1,word2):
        result.append(a)
        result.append(b)

    result.append(word1[len(result)//2:])
    result.append(word2[len(result)//2:])

    return ''.join(result)