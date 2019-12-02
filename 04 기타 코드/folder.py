 -*- coding: utf-8 -*-
"""
Created on Fri Jul 19 16:08:20 2019

@author: SHF_W
"""

import os
from datetime import datetime

def createFolder(directory):
    try:
        if not os.path.exists(directory):
            os.makedirs(directory)
    except OSError:
        print ('Error: Creating directory. ' +  directory)
        
timestamp = datetime.now().strftime('%y%b%d%H%M%S')
# Example
createFolder('./data_'+timestamp)