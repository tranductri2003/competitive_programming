# for large numbers we will have to memoize!
steps = 100
 
# generic memoizer
def memoize(func):
    '''Memoizing decorator that checks whether the wrapped function 
    has been previously run with the current argument value. 
    If it has then that value is retrieved and offered instead 
    of rerunning the function'''
    memos = {}
    def wrapper(x):
        if x not in memos:
            memos[x] = func(x)
        return memos[x]
    return wrapper
 
@memoize
def one_step(steps_to_go):
    '''given a number of steps to climb recursively climb either 
    1, 2, or 3 steps once we reach the end of the steps pass 
    totalled step values back up the recursive chain'''
    # try to take one step
    if steps_to_go == 1:
        # upon finding there is only one step to go return 1 
        # as there is only 1 way to climb this
        return 1
    # try to take 2 steps
    elif steps_to_go == 2:
        # upon finding there are 2 steps to go return 2 
        # (2 ways to climb: 2; 1,1)
        return 2
    # try to take 3 steps
    elif steps_to_go == 3:
        # upon finding there are 3 steps to go return 4 
        # (4 ways to climb: 3; 2,1; 1,2; 1,1,1)
        return 4
    else:
        # add all the results of stepping again 
        # (taking each of the 3 different steps)
        return (one_step(steps_to_go-1) + one_step(steps_to_go-2)
                + one_step(steps_to_go-3))
 
# print our answer
print(one_step(steps))