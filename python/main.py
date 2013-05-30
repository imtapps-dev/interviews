numerals = {
    1:'I',
    5:'V',
    10:'X'
}

def PIRVal(nums,upper):
    prev = False
    nums.sort()
    for num in nums:
        if num > upper:
            return prev
        else:
            prev = num
    return prev

def roman(i):
    if numerals.has_key(i):
        return numerals[i]
    elif i < 4:
        return 'I' * i
    elif i == 4:
        return 'IV'
    elif i > 5 and i < 9:
        return 'V' + roman(i - 5)
    elif i == 9:
        return 'IX'
    elif i == 11:
        return 'XI'
