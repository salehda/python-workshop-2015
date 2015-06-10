# -*- coding: utf-8 -*-
"""
Created on Tue Jun 09 11:37:47 2015
this is a script to catch the mean temp 
@author: David
"""

import os 
my_filename=__file__
script_dir=os.path.dirname(my_filename)
root_dir=os.path.dirname(script_dir)
print root_dir

data_dir=os.path.join(root_dir,'data')
filename=os.path.join(data_dir,'weather.csv')
print "my file exists?{}".format(os.path.exists(filename))

#Target is Mean temp

import csv
my_temps=[]
parser=csv.reader(open(filename,'rb'))#rb is read in bytes 
header=parser.next()
mean_temp_idx= 9
for line in parser:
    try:
        my_float=float(line[mean_temp_idx])
    except:
        print"error floating"
    else:
        my_temps.append(my_float)
print my_temps


