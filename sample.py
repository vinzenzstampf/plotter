import re
import numpy as np
from ROOT import RDataFrame as RDF
from ROOT.ROOT import EnableImplicitMT as multicore
import pandas as pd
from pdb import set_trace

multicore()

# from root_numpy import root2array

class Sample(object):
    def __init__(self, 
                 name, 
                 label,
                 selection,
                 datacard_name,
                 colour,
                 position_in_stack, 
                 basedir, 
                 postfix, 
                 isdata, 
                 ismc, 
                 issignal, 
                 weight,
                 xs):
        self.name              = name             
        print 'loading', self.name
        self.label             = label   
        self.selection         = selection         
        self.datacard_name     = datacard_name            
        self.colour            = colour           
        self.position_in_stack = position_in_stack
        self.basedir           = basedir          
        self.postfix           = postfix          
        self.isdata            = isdata           
        self.ismc              = ismc             
        self.issignal          = issignal         
        self.weight            = weight           
        self.xs                = xs        
        self.nevents           = 1.
        self.file              = '/'.join([basedir, self.name, postfix])          
        
        if not self.isdata:
            nevents_file = '/'.join([basedir, self.name, 'SkimAnalyzerCount/SkimReport.txt'])
            with open(nevents_file) as ff:
                lines = ff.readlines()
                for line in lines:
                    if 'Sum Norm Weights' in line:
                        self.nevents = float(re.findall(r'\d+', lines[2])[0])
                        break
        tree_file = '/'.join([self.basedir, self.name, self.postfix])
        
        rdf = RDF('tree', tree_file)
        rdf = rdf.Filter(self.selection)
        # set_trace()
        df = rdf.AsNumpy()
        self.df = pd.DataFrame(df)
        # scale to 1/pb 
        self.lumi_scaling = 1. if self.isdata else (self.xs / self.nevents)
 
