
def findWeight(x, limit = 100):
    allWeights = [3**num for num in range(limit)]
    result, i= [], 0
    while(sum(result) != x):
        if 2*allWeights[i] >= x and sum(result) != x:
            for j in range(i, -1,-1):
                if(sum(result) == x): return result
                if 2*allWeights[j] + sum(result) <= x and sum(result) <= x:
                    result.append(allWeights[j])
                    result.append(allWeights[j])
                elif allWeights[j] + sum(result) <= x and sum(result) <= x:
                    result.append(allWeights[j])
        i += 1
    return result


print(findWeight(81))