import re
import time
import ROOT as rt
# import uproot
# import rootpy
# import root_pandas
# from rootpy.plotting import Hist
import numpy as np
import pandas as pd
# from rootpy.plotting import Hist
# from root_numpy import root2array
from collections import OrderedDict
import sklearn
from selections import selections, selections_df
from evaluate_nn import Evaluator
from sample import Sample
from variables import variables
import matplotlib.pyplot as plt
from matplotlib.patches import Patch
from pdb import set_trace

# basedir        = '/Users/manzoni/Documents/efficiencyNN/HNL/mmm/ntuples/'
basedir        = '/Users/cesareborgia/cernbox/2018_new/mmm/'
postfix        = 'HNLTreeProducer/tree.root'
lumi           = 59700. # fb-1
selection_data = selections['baseline']
# selection_mc   = selections['baseline'] 
selection_mc   = '&'.join([selections['baseline'], selections['ispromptlepton']])

# NN evaluator
model          = 'net_model_weighted.h5'
transformation = 'input_tranformation_weighted.pck'
features       = 'input_features.pck'
evaluator      = Evaluator(model, transformation, features)

@rt.DeclareCppCallable(["float"] * len(evaluator.features), "float") # does this init work?!
def evaluate_RDF(*arg):
    return evaluator.eval_rdf(arg) 

print '============> starting reading the trees'
now = time.time()
                   
data = [
    Sample('Single_mu_2018A', '2018A', selection_data, 'data_obs', 'black', 9999, basedir, postfix, True, False, False, 1., 1.),
    # Sample('Single_mu_2018B', '2018B', selection_data, 'data_obs', 'black', 9999, basedir, postfix, True, False, False, 1., 1.),
    # Sample('Single_mu_2018C', '2018C', selection_data, 'data_obs', 'black', 9999, basedir, postfix, True, False, False, 1., 1.),
    # Sample('Single_mu_2018D', '2018D', selection_data, 'data_obs', 'black', 9999, basedir, postfix, True, False, False, 1., 1.),
]

mc = [
    Sample('DYJetsToLL_M50_ext', r'DY$\to\ell\ell$', selection_mc, 'DY', 'gold'     ,10, basedir, postfix, False, True, False, 1.,  6077.22),
    # Sample('TTJets_ext'        , r'$t\bar{t}$'     , selection_mc, 'TT', 'slateblue', 0, basedir, postfix, False, True, False, 1.,   831.76),
    # Sample('WW'                , 'WW'              , selection_mc, 'WW', 'blue'     , 5, basedir, postfix, False, True, False, 1.,    75.88),
    # Sample('WZ'                , 'WZ'              , selection_mc, 'WZ', 'blue'     , 5, basedir, postfix, False, True, False, 1.,    27.6 ),
    # Sample('ZZ'                , 'ZZ'              , selection_mc, 'ZZ', 'blue'     , 5, basedir, postfix, False, True, False, 1.,    12.14),
]            

signal = [
]

print '============> it took %.2f seconds' %(time.time() - now)

# evaluate FR

# prepare inputs for cpp-callable in RDataFrame
in_list = ', '.join(evaluator.features)
# print 'in_list: ', in_list

for isample in (data+mc+signal): # WHY SIGNAL HERE?!
    # TODO FIX ABS -> LOG ABS
    isample.df = isample.df.Define('log_abs_l0_dxy', 'abs(l0_dxy)')
    isample.df = isample.df.Define('log_abs_l0_dz' , 'abs(l0_dz )')
    isample.df = isample.df.Define('log_abs_l1_dxy', 'abs(l1_dxy)')
    isample.df = isample.df.Define('log_abs_l1_dz' , 'abs(l1_dz )')
    isample.df = isample.df.Define('log_abs_l2_dxy', 'abs(l2_dxy)')
    isample.df = isample.df.Define('log_abs_l2_dz' , 'abs(l2_dz )')
    # TODO FIX ABS -> LOG ABS
    isample.df = isample.df.Define('abs_l0_eta', 'abs(l0_eta)')
    isample.df = isample.df.Define('abs_l1_eta', 'abs(l1_eta)')
    isample.df = isample.df.Define('abs_l2_eta', 'abs(l2_eta)')
    # FAKE RATE
    isample.df = isample.df.Define('fr', 'CppCallable::evaluate_RDF( ' + in_list + ' )')
    isample.df = isample.df.Define('fr_corr', 'fr / (1. - fr)')


# split the dataframe in tight and loose-not-tight (called simply loose for short)
for isample in (mc+data):
    isample.df_tight = isample.df.Filter(selections_df['tight'])
    isample.df_lnt   = isample.df.Filter('! ( ' + selections_df['tight'] + ' )')

# sort depending on their position in the stack
mc.sort(key = lambda x : x.position_in_stack)

can = rt.TCanvas()

for variable, bins, xlabel, ylabel in variables:
    
    set_trace()
    print 'plotting', variable

    # plot MC stack in tight
    stack_tight = rt.THStack()


    stack_tight   = [getattr(imc.df_tight, variable)                                         for imc in mc] 
    labels_tight  = [imc.label                                                               for imc in mc]
    colours_tight = ['steelblue'                                                             for imc in mc] 
    weights_tight = [lumi * imc.df_tight.weight * imc.lumi_scaling * imc.df_tight.lhe_weight for imc in mc] 

    # plot MC stack in loose * fr / (1-fr)
    stack_loose   = [getattr(imc.df_loose, variable)                                                                     for imc in mc] 
    labels_loose  = [imc.label                                                                                           for imc in mc]
    colours_loose = ['skyblue'                                                                                           for imc in mc] 
    weights_loose = [-1.* lumi * imc.df_loose.weight * imc.lumi_scaling * imc.df_loose.lhe_weight * imc.df_loose.fr_corr for imc in mc] 
    
    # data in loose
    data_loose = df_data.query('not(%s)'%selections_df['tight']) 
    
    stack_loose  .append(data_loose[variable])
    labels_loose .append('nonprompt')
    colours_loose.append('skyblue')
    weights_loose.append(data_loose['fr_corr'])
    
    # merge the stacks together
    stack   = stack_tight   + stack_loose  
    labels  = labels_tight  + labels_loose 
    colours = colours_tight + colours_loose
    weights = weights_tight + weights_loose
    
    # plot    
    expectation = plt.hist(stack, bins, stacked=True, label=labels, weights=weights, color=colours)

    # plot data in tight
    data_tight = df_data.query(selections_df['tight']) 
    bin_centres = np.array([0.5*(bins[i] + bins[i+1]) for i in np.arange(len(bins)-1)])
    counts = np.array([data_tight.query( '%s > %f and %s <= %f' %(variable, bins[i], variable, bins[i+1]) ).shape[0] for i in np.arange(len(bins)-1)])
    plt.errorbar(bin_centres, counts, yerr=np.sqrt(counts), fmt='o', color='black', label='observed')
            
    # ratio pad
    exp = expectation[0][-1] 
    obs = counts  
    
    # FIXME! need to understand ratio pads and company
#     plt.errorbar(bin_centres, counts/exp, fmt='o', color='black')
    
    # legend and save it! 
    legend_entries = []

    objs, labels =  plt.axes().get_legend_handles_labels()
    for jj in range(len(objs)):
        if labels[jj] == 'observed':
            legend_entries.append(objs[jj])

    legend_entries += [
        Patch(facecolor='steelblue', edgecolor='steelblue', label='prompt'),
        Patch(facecolor='skyblue'  , edgecolor='skyblue'  , label='nonprompt')
    ]
        
    # set_trace()
    # plt.legend(handles=legend_entries)
    plt.xlabel(xlabel)
    plt.ylabel(ylabel)
    plt.savefig('%s.pdf' %variable)

    # outfile = rt.TFile.Open('datacard_%s.root' %variable, 'recreate')
    # outfile.cd()
    # h_data = Hist(bins, name='data_obs')
    # h_data.fill_array(df_data[variable])
    # h_data.Write()
    # for imc in mc:
        # h_mc = Hist(bins, name=imc.datacard_name)
        # h_mc.fill_array(imc.df[variable], imc.df.weight * imc.df.lumi_scaling * imc.df.lhe_weight)
        # h_mc.Write()
    # outfile.Close()
