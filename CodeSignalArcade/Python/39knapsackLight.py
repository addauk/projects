def solution(value1, weight1, value2, weight2, maxW):

    if weight1 + weight2 <= maxW:
        return value1 + value2
    elif weight1 > maxW : 

        if weight2 > maxW:
            return 0
        else:
            return value2
    else:
        if weight2 <= maxW:
            return max(value1,value2)
        else:
            return value1
        
        
    
