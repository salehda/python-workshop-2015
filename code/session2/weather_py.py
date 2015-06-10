# -*- coding: utf-8 -*-
"""
Created on Tue Jun 09 11:29:37 2015

@author: David
"""

import os 
my_filename=__file__
script_dir=os.path.dirname(my_filename)
root_dir=os.path.dirname(script_dir)
print root_dir

data_dir=os.path.join(root_dir,'scripts')
filename=os.path.join(data_dir,'weather.csv')
print "my file exists?{}".format(os.path.exists(filename))