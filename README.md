# AI-Face-FairnessBench

<figure>
  <img src="assets/dataset_overview.png" alt="Dataset Overview">
</figure>

## License
The AI-Face Dataset is licensed under [CC BY-NC-ND 4.0](https://creativecommons.org/licenses/by-nc-nd/4.0/legalcode)

## Download
The dataset will be released soon along side the EULA. If you would like to access the AI-Face Dataset, please upload the signed EULA to the Google form that we will provide soon, the download link will be sent to you.

## 1. Installation

You can run the following script to configure the necessary environment:

```
cd AI_Face_FairnessBench
conda create -n FairnessBench python=3.9.0
conda activate FairnessBench
pip install -r requirements.txt
```
## 2. Dataset Preparation and Description
After getting our AI-Face dataset, put the provided `train.csv` and `test.csv` within AI-Face dataset under  [`./dataset`](./dataset).

train.csv and test.csv is formatted:

| Column                     | Description                                                         |
|----------------------------|---------------------------------------------------------------------|
| Image Path                 | Path to the image file                                              |
| Gender                     | Gender label: 1 - Male, 0 - Female                                  |
| Age                        | Age label: 0 - Child, 1 - Youth, 3 - Adult, 4 - Middle-aged, 5-Senior|
| Skin Tone                  | Skin Tone label: Monk Skin Tone Scale             |
| Intersection               | 0-(Male,Light), 1-(Male,Medium), 2-(Male,Dark), 3-(Female,Light), 4-(Female,Medium), 5-(Female,Dark)|
| Target                     | Label indicating real (0) or fake (1) image                         |


#### 📝 Note 

Dataset will be released soon.
   
```
AI-Face Dataset
  ├── AttGAN
  ├── Latent_Diffusion
  ├── Palette
  ├── ...
  ├── ...
```

## 3. Load Pretrained Weights
Before running the training code, make sure you load the pre-trained weights. We provide pre-trained weights under [`./training/pretrained`](./training/pretrained). You can also download *Xception* model trained on ImageNet (through this [link](http://data.lip6.fr/cadene/pretrainedmodels/xception-b5690688.pth)) or use your own pretrained *Xception*.

## 4. Train
To run the training code, you should first go to the [`./training/`](./training/) folder, then run [`train_test.py`](training/train_test.py):

```
cd training

python train_test.py 
```

You can adjust the parameters in [`train_test.py`](training/train_test.py) to specify the parameters, *e.g.,* model, batchsize, learning rate, *etc*.

`--lr`: learning rate, default is 0.0005. 

`--train_batchsize`: batchsize for training, default is 128.

`--test_batchsize`: batchsize for testing, default is 32.

` --datapath`: /path/to/[`dataset`](./dataset).

`--model`: detector name ['xception', 'efficientnet', 'core', 'ucf', 'srm', 'f3net', 'spsl', 'daw_fdd', 'dag_fdd', 'fair_df_detector'], default is 'xception'.

`--dataset_type`: dataset type loaded for detectors, default is 'no_pair'. For 'ucf' and 'fair_df_detector', it should be 'pair'. 

#### 📝 Note
To train ViT-b/16 and UnivFD, please run  [`train_test_vit.py`](training/train_test_vit.py) and [`train_test_clip.py`](training/train_test_clip.py), respectively.

## 📦 [`Provided Detectors`](./training/detectors)
|                  | File name                               | Paper                                                                                                                                                                                                                                                                                                                                                         |
|------------------|-----------------------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Xception          | [xception_detector.py](./training/detectors/xception_detector.py)         | [Xception: Deep learning with depthwise separable convolutions](https://openaccess.thecvf.com/content_cvpr_2017/html/Chollet_Xception_Deep_Learning_CVPR_2017_paper.html) |
| EfficientNet-B4            | [efficientnetb4_detector.py](./training/detectors/xception_detector.py)       |  [Efficientnet: Rethinking model scaling for convolutional neural networks](http://proceedings.mlr.press/v97/tan19a.html)                                                                                                                                                                                                                                                                                              |
| ViT-B/16      |  [train_test_vit.py](./training/train_test_vit.py) | [An Image is Worth 16x16 Words: Transformers for Image Recognition at Scale](https://arxiv.org/abs/2010.11929)                                                                                                                                                                                                                  |
| UCF      | [ucf_detector.py](./training/detectors/ucf_detector.py) | [UCF: Uncovering Common Features for Generalizable Deepfake Detection](https://openaccess.thecvf.com/content/ICCV2023/papers/Yan_UCF_Uncovering_Common_Features_for_Generalizable_Deepfake_Detection_ICCV_2023_paper.pdf) |
| UnivFD    |  [train_test_clip.py](./training/train_test_clip.py) | [Towards Universal Fake Image Detectors that Generalize Across Generative Models](https://openaccess.thecvf.com/content/CVPR2023/papers/Ojha_Towards_Universal_Fake_Image_Detectors_That_Generalize_Across_Generative_Models_CVPR_2023_paper.pdf) | 
| CORE    |  [core_detector.py](./training/detectors/core_detector.py) | [CORE: Consistent Representation Learning for Face Forgery Detection](https://openaccess.thecvf.com/content/CVPR2022W/WMF/papers/Ni_CORE_COnsistent_REpresentation_Learning_for_Face_Forgery_Detection_CVPRW_2022_paper.pdf) |  
| F3Net    |  [f3net_detector.py](./training/detectors/f3net_detector.py) | [Thinking in Frequency: Face Forgery Detection by Mining Frequency-aware Clues](https://www.ecva.net/papers/eccv_2020/papers_ECCV/papers/123570086.pdf) | 
| SRM    |  [srm_detector.py](./training/detectors/srm_detector.py) | [Generalizing Face Forgery Detection with High-frequency Features](https://openaccess.thecvf.com/content/CVPR2021/papers/Luo_Generalizing_Face_Forgery_Detection_With_High-Frequency_Features_CVPR_2021_paper.pdf) | 
| SPSL    |  [spsl_detector.py](./training/detectors/spsl_detector.py) | [Spatial-Phase Shallow Learning: Rethinking Face Forgery Detection in Frequency Domain](https://arxiv.org/abs/2103.01856) | 
| DAW-FDD    |  [daw_fdd.py](./training/detectors/daw_fdd.py) | [Improving Fairness in Deepfake Detection](https://openaccess.thecvf.com/content/WACV2024/papers/Ju_Improving_Fairness_in_Deepfake_Detection_WACV_2024_paper.pdf) | 
| DAG-FDD    |  [dag_fdd.py](./training/detectors/dag_fdd.py) | [Improving Fairness in Deepfake Detection](https://openaccess.thecvf.com/content/WACV2024/papers/Ju_Improving_Fairness_in_Deepfake_Detection_WACV_2024_paper.pdf) | 
| PG-FDD    |  [fair_df_detector.py](./training/detectors/fair_df_detector.py) | [Preserving Fairness Generalization in Deepfake Detection](https://arxiv.org/abs/2402.17229) | 


