## Environment setup guide
Do the following manul setup for using `soccer-two`, some instructions taking from [this issue](https://github.com/Unity-Technologies/ml-agents/issues/5624#issuecomment-1044794585)

```bash
conda create -n beta_goal python=3.9.7 -y
conda activate beta_goal
conda install pytorch=1.8 -y
conda install grpcio h5py -y
pip install mlagents-envs==0.27.0 -q
pip install mlagents==0.27.0 -q
pip install setuptools==66 wheel==0.38.4
pip install --upgrade pip==22.0.2
pip install soccer-twos
pip install --upgrade numpy==1.26.4
pip install requests  
```

Then it gets tricky, we need to change an auto-detection of a path to absolute path, in this `/Users/kevinb/miniforge3/envs/beta_goal/lib/python3.9/site-packages/soccer_twos/__init__.py` file change `env_config["env_path"]` on line 66 and 71 to absolute path (use your own path):

```bash
"/Users/kevinb/miniforge3/envs/beta_goal/lib/python3.9/site-packages/soccer_twos/bin/v2/mac_os/soccer-twos.app"
```