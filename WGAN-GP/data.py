# -*- coding: utf-8 -*-
"""
@author: @harshit
"""
import glob
import json
import numpy as np

class DATA():
    def __init__(self, mw_family, file_len):
        self.mw_family = mw_family
        self.file_len = file_len
    
    def file_size(self, fname):
        sz = 0
        with open(fname, "r") as f:
            for i, l in enumerate(f):
                sz = i
                continue
        return sz+1
  
    def load_data(self, tokenize):
        path = self.mw_family+'/*.txt'
        files = glob.glob(path)
        print('Total samples for %s: %d' % (self.mw_family, len(files)))
        if tokenize:
            with open('opdict'+self.mw_family+'.json', "r") as json_file:
                mapping = json.load(json_file)
        print('Mappings in JSON file: %d'%len(mapping))
        data = []
        for file in files:
            if self.file_size(file) >= self.file_len:
                current_file = []
                with open(file, "r") as rf:
                    for line in rf:
                        if len(current_file) < self.file_len:
                            line = line.strip()
                            if tokenize:
                                if line in mapping:
                                    current_file.append(mapping[line])
                                else:
                                    current_file.append(len(mapping))
                            else:
                                current_file.append(line)
                        else:
                            break
                    data.append(current_file)
            else:
                continue
        return np.array(data), len(mapping)