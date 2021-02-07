nums = ['1450', '33', '871', '19', '14378', '32', '1005', '44', '8907', '16']

def last_char(s):
    return s[-1]

nums_sorted = sorted(nums, key=last_char)
print (nums_sorted)
