def helper(func):
    def check(a,b):
            if b==0:
                return 'Infinite'
            else:
                return func(a,b)
    return check

@helper
def div(a,b):
    return a/b

#div=helper(div)
print('Division=>',div(5,0))
