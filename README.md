# Arrhythmic Heartbeat Classification Model
## ECE 284 Project - Spring 2025 
## Stephen Wilcox

All of the coding was done in .ipynb files and they are in the code folder.

The following packages are required to run the code and most of the scripts start with a download link for them.: wfdb numpy scipy matplotlib scikit-learn torch torchvision torchaudio biosppy peakutils

In order to run the code it requires the files from https://www.physionet.org/content/mitdb/1.0.0/ and https://physionet.org/content/nsrdb/1.0.0/. They can be downloaded manually and put into the data folder or you can navigate to the code directory and run download_data.ipynb.

Note that I did the project in the UCSD Jupyter Hub and there isnt an option to download the whole folder so I have only added the .ipynb's and none of the checkpoints.

The models tested in the paper are:

final_basic_cnn.ipynb

final_se_cnn.ipynb

final_multilayer_cnn.ipynb

final_model.ipynb