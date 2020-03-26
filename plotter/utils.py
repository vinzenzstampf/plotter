from datetime import datetime
from os import environ as env
from os.path import exists as ensure_path
from os import makedirs
from getpass import getuser as user
import pickle

def set_paths(channel, year):
    assert channel in ['mmm', 'mem', 'mem_os', 'mem_ss', 'eem', 'eem_os', 'eem_ss', 'eee'], 'ERROR: Channel not valid.'
    assert year in [2016, 2017, 2018], 'ERROR: Year not valid.'    
    if user() == 'manzoni': 
        env['NTUPLE_BASE_DIR'] = '/Users/manzoni/Documents/HNL/ntuples/'
        env['NTUPLE_DIR']      = '/Users/manzoni/Documents/HNL/ntuples/%d/%s' %(year, channel.split('_')[0])
        env['PLOT_DIR']        = '/Users/manzoni/Documents/HNL/plotter/plots_%d_%s/' %(year, channel)
        env['NN_DIR']          = '/Users/manzoni/Documents/HNL/NN/'

    if user() == 'cesareborgia': 
        env['NTUPLE_BASE_DIR'] = '/Users/cesareborgia/cernbox/hnl/'
        env['NTUPLE_DIR']      = '/Users/cesareborgia/cernbox/ntuples/%d/%s' %(year, channel.split('_')[0])
        env['PLOT_DIR']        = '/Users/cesareborgia/Dropbox/documents/physics/phd/plots/%d/%s/' %(year, channel)
        env['NN_DIR']          = '/Users/cesareborgia/HNL/plotter/NN/trainings/'

def get_time_str():
    today   = datetime.now()
    date    = today.strftime('%y%m%d')
    hour    = str(today.hour)
    minit   = str(today.minute)
    time_str = date + '_' + hour + 'h_' + minit + 'm/'
    return time_str

def plot_dir(region_label=''):
    plot_dir = env['PLOT_DIR'] + get_time_str()
    if len(region_label): plot_dir = plot_dir[:-1] + '_' + region_label + '/'
    if not ensure_path(plot_dir): makedirs(plot_dir)       #mkdir(plot_dir)
    return  plot_dir

def nn_dir(channel,region_label):
    nn_dir = env['NN_DIR'] + channel + '_' + get_time_str()
    if len(region_label): nn_dir = nn_dir[:-1] + '_' + region_label + '/'
    if not ensure_path(nn_dir): makedirs(nn_dir)
    return  nn_dir

def save_plotter_and_selections(plotter, sel_data, sel_mc, sel_tight):

    with open('/'.join([plotter.plt_dir, 'plotter.pck']), 'wb') as plt_file:
        pickle.dump(plotter, plt_file)

    with open('/'.join([plotter.plt_dir, 'selections.py']), 'a') as selection_file:
        
        print('selection_data = [', file=selection_file)
        for isel in sel_data:
            print("\t'%s'," %isel , file=selection_file)
        print(']', file=selection_file)

        print('\n'*2+'#'*80+'\n'*2, file=selection_file)

        print('selection_mc = ['  , file=selection_file)
        for isel in sel_mc:
            print("\t'%s'," %isel , file=selection_file)
        print(']', file=selection_file)

        print('\n'*2+'#'*80+'\n'*2, file=selection_file)

        print("'selection_tight = '%s'" %sel_tight, file=selection_file)
        
