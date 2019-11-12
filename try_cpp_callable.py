import ROOT as rt
from evaluate_nn import Evaluator
from pdb import set_trace

feats = ['l0_pt', 'l1_pt', 'l2_pt', 'hnl_dr_12', 'hnl_m_12', 'sv_prob', 'hnl_2d_disp', 'abs_l0_eta', 'abs_l1_eta', 'abs_l2_eta', 'log_abs_l0_dxy', 'log_abs_l0_dz', 'log_abs_l1_dxy', 'log_abs_l1_dz', 'log_abs_l2_dxy', 'log_abs_l2_dz']

# feats = ['abs_l0_eta', 'abs_l1_eta', 'abs_l2_eta']#, 'log_abs_l0_dxy', 'log_abs_l0_dz', 'log_abs_l1_dxy', 'log_abs_l1_dz', 'log_abs_l2_dxy', 'log_abs_l2_dz']

n_vars = len(feats)
print 'n_vars: ', n_vars


def evaluate(x):
    y =0 
    for i in x: y+= i
    return y

model          = 'net_model_weighted.h5'
transformation = 'input_tranformation_weighted.pck'
features       = 'input_features.pck'
evaluator      = Evaluator(model, transformation, features)

@rt.DeclareCppCallable(["float"] * n_vars, "float") # does this init work?!
def evaluate_RDF(*arg):
    # return evaluate(arg) 
    return evaluator.eval_rdf(arg) 


f_in = '/Users/cesareborgia/cernbox/2018_new/mmm/TTJets/HNLTreeProducer/tree.root'
rdf = rt.RDataFrame('tree', f_in)

# rdf = rdf.Define("x", "CppCallable::evaluate_RDF(l1_pt, l2_pt, l0_pt, hnl_dr_12)")

rdf = rdf.Define('log_abs_l0_dxy', 'abs(l0_dxy)')
rdf = rdf.Define('log_abs_l0_dz' , 'abs(l0_dz )')
rdf = rdf.Define('log_abs_l1_dxy', 'abs(l1_dxy)')
rdf = rdf.Define('log_abs_l1_dz' , 'abs(l1_dz )')
rdf = rdf.Define('log_abs_l2_dxy', 'abs(l2_dxy)')
rdf = rdf.Define('log_abs_l2_dz' , 'abs(l2_dz )')
rdf = rdf.Define('abs_l0_eta', 'abs(l0_eta)')
rdf = rdf.Define('abs_l1_eta', 'abs(l1_eta)')
rdf = rdf.Define('abs_l2_eta', 'abs(l2_eta)')

# df['log_abs_l0_dxy'] = np.log10(np.abs(df.l0_dxy))
# df['log_abs_l0_dz' ] = np.log10(np.abs(df.l0_dz ))
# df['log_abs_l1_dxy'] = np.log10(np.abs(df.l1_dxy))
# df['log_abs_l1_dz' ] = np.log10(np.abs(df.l1_dz ))
# df['log_abs_l2_dxy'] = np.log10(np.abs(df.l2_dxy))
# df['log_abs_l2_dz' ] = np.log10(np.abs(df.l2_dz ))

in_list = ', '.join(feats)
print 'in_list: ', in_list
# set_trace()
rdf = rdf.Define("x", 'CppCallable::evaluate_RDF( ' + in_list + ' )')

th1 = rdf.Histo1D('x').GetPtr()

th1.Draw()

