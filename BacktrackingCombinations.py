"""
This is a template to do the backtracking 
to search for all unique combinations
"""
def BacktrackCombinations(nums, target):
    #Problem specific settings
    #DFSearch([initial parameters])
    pass



def DFSearch(choice_pool, start, stop, path, res, prb_param):
    """
    Typically, you will have a choice pool, start index, stop index to 
    limit the choice scope to avoid repetitions 
    path is used to track your path, path has a path cost
    res is the global result pool to keep legimate solutions
    prb_param is problem specific parameters to be added
    """
    #1.Do you goal test here
    # Iterate on your choice pool
    for i in xrange(start, stop):
        #Allow element repetition, new start starts with i
        DFSearch(choice_pool, i, stop, path+[choice_pool[i]], res, prb_param)
        #Disallow repetition, new start starts with i+1 
        DFSearch(choice_pool, i+1, stop, path+[choice_pool[i]], res, prb_param)
    

