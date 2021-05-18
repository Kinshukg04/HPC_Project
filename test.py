import library

def test_function(input_list):
    #do operation
    x = min(input_list)
    return x

def post_function(results):
    x = min(results)
    return x

library(test_function,input_list,multiprocess=False,database=None)