# plotter

tested in the following environment, set up with `conda`

```
conda env --name plotter create -f plotter/conda_env/alt_root_conda_environment.yml
python -m pip install rootpy --user
conda activate plotter
python -m pip install rootpy --user
python -m pip install modin --user
```

# Limits

```
combineCards.py disp1=datacard_hnl_m_12_lxy_lt_0p5_hnl_m_10_v2_1p0Em06_majorana.txt disp2=datacard_hnl_m_12_lxy_0p5_to_2p0_hnl_m_10_v2_1p0Em06_majorana.txt disp3=datacard_hnl_m_12_lxy_mt_2p0_hnl_m_10_v2_1p0Em06_majorana.txt > datacard_hnl_m_12_combined_hnl_m_10_v2_1p0Em06_majorana.txt

combine -M AsymptoticLimits datacard_hnl_m_12_combined_hnl_m_10_v2_1p0Em06_majorana.txt --run blind

combine -M HybridNew --testStat=LHC --frequentist -d datacard_hnl_m_12_combined_hnl_m_10_v2_1p0Em06_majorana.txt -T 1000 -C 0.95 --rMin 0 --rMax 50  
```
