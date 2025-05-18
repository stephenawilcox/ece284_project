import wfdb

# Download MIT-BIH Arrhythmia Database
wfdb.dl_database(
    'mitdb',                # PhysioNet database ID
    dl_dir='../data/mitdb'     # Local directory to store the files
)

# Download Normal Sinus Rhythm Database
wfdb.dl_database(
    'nsrdb',
    dl_dir='../data/nsrdb'
)