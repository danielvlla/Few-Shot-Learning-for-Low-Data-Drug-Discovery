import os

dirs = [
    './RandomForest',
    './GCNBenchmark',
    './SiameseNets',
    './MatchingNets',
    './ProtoNets',
    './RelationNets',
    './data/raw'
]

for directory in dirs:
    if not os.path.exists(directory):
        os.makedirs(directory)
        print("Created Directory: ", directory)
    else:
        print("Directory already exists: ", directory)
