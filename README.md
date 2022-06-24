# Few-shot Learning for Low-Data Drug Discovery

Implementations for the following machine learning models:

- Random Forests
- Graph Convolutional Network
- [Siamese Networks](https://www.cs.cmu.edu/~rsalakhu/papers/oneshot1.pdf)
- [Matching Networks](https://proceedings.neurips.cc/paper/2016/file/90e1357833654983612fb05e3ec9148c-Paper.pdf)
- [Prototypical Networks](https://www.cs.toronto.edu/~zemel/documents/prototypical_networks_nips_2017.pdf)
- [Relation Networks](https://openaccess.thecvf.com/content_cvpr_2018/papers/Sung_Learning_to_Compare_CVPR_2018_paper.pdf)

The last 3 networks also include our implementation of the iterative refinement LSTM from [Low Data Drug Discovery with One-Shot Learning](https://pubs.acs.org/doi/10.1021/acscentsci.6b00367).

The Jupyter notebooks are run on Google Colab, with Google Drive mounted. Before uploading the Repo to Google Drive, run the `create_dirs.py` script by running `python create_dirs.py`. Empty directories will be created for every technique, which will serve as the directories for the outputs from each respective Colab notebook. The experiments which utilise ECFP rather than GCNs can be run on Tox21 data using the `Prototypical Nets Tox21 ECFP.ipynb` notebook.

## Tox21 
  
The dataset is obtained from the DeepChem AWS bucket. Accessed from: https://deepchemdata.s3-us-west-1.amazonaws.com/datasets/tox21.csv.gz. Last Accessed: 08 Nov 2021 in CSV format.

## MUV
  
The dataset was obtained from the DeepChem AWS bucket. Accessed from: https://deepchemdata.s3-us-west-1.amazonaws.com/datasets/muv.csv.gz. Last Accessed: 08 Nov 2021 in CSV format.

## Database of Useful (Docking) Decoys — Enhanced (DUD-E)
  
The data for the GPCR subset was obtained directly from the DUD-E website.Accessed from: http://dude.docking.org/subsets. Last Accessed: 08 Nov 2021. The actives and decoys for the targets within the DUD-E subsets are provided as separate SMILES files. These files are loaded using the Pandas library and aggregated in a CSV file contained all the actives and decoys for the GPCR subset.
