# -*- coding: utf-8 -*-
"""
Created on Tue Jun 09 10:26:02 2015
A script to compute average of number
@author: David
"""

def average(nums):
    n=len(nums)
    return sum(nums)*1.0/n
    
def main(options):

    my_nums=options.nums
    my_ints=[]
    for i in my_nums:
        my_ints.append(float(i))   
    my_avg=average(my_ints)
    print " the average of {} is {}".format(my_nums,my_avg)
if __name__=="__main__":
    import argparse
    parser=argparse.ArgumentParser()
    parser.add_argument('nums',nargs='*',help="Alist of numbers")
    options=parser.parse_args()
    main(options)
 