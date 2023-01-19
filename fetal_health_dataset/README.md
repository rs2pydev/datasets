# Dataset for Fetal Health Multi-Class Classification of  

## 1. Sources 

- [Original Source - UCI ML Repository: Cardiotocography Data Set](https://archive.ics.uci.edu/ml/datasets/cardiotocography)
- [Alternative Source: Kaggle - Fetal Health Classification Dataset](https://www.kaggle.com/datasets/andrewmvd/fetal-health-classification)

## 2. Dataset Description

Reduction of child mortality is reflected in several of the United Nations' Sustainable Development Goals and is a key indicator of human 
progress. The UN expects that by 2030, countries end preventable deaths of newborns and children under 5 years of age, with all countries 
aiming to reduce under‑5 mortality to at least as low as 25 per 1,000 live births.

Parallel to notion of child mortality is of course maternal mortality, which accounts for 2,95,000 deaths during and following pregnancy 
and childbirth (as of 2017). The vast majority of these deaths (94%) occurred in low-resource settings, and most could have been prevented.

In light of what was mentioned above, Cardiotocograms (CTGs) are a simple and cost accessible option to assess fetal health, allowing healthcare 
professionals to take action in order to prevent child and maternal mortality. The equipment itself works by sending ultrasound pulses and reading 
its response, thus shedding light on fetal heart rate (FHR), fetal movements, uterine contractions and more.

This dataset contains 2126 records of 22 features extracted from Cardiotocogram exams. There are two alternative target variables in this dataset: 

- **Class:** FHR pattern class code (1 to 10) - *Target variable for a 10-class classification task with **NSP** variable considered as a feature variable.*

- **NSP:** Fetal state class code -  *Target variable for a 3-class classification task with **Class** variable considered as a feature variable.*
  - N=normal
  - S=suspect
  - P=pathologic 

## 3. Problem Statement

Use the given Cardiotocogram (CTG) data to classify the health of a fetus as **Normal**, **Suspect** or **Pathological** with the objective of 
preventing child and maternal mortalities. In simple terms, use this dataset to create a multi-class classification model to classify CTG features 
into the three fetal health states.

## 4.1 Attribute Information

| S.N | Attribute | Description |
| :--- | :--- | :--- |
| 1. | **LB** | FHR baseline (beats per minute) |
| 2. | **AC** | # of accelerations per second |
| 3. | **FM** | # of fetal movements per second |
| 4. | **UC** | # of uterine contractions per second |
| 5. | **DL** | # of light decelerations per second |
| 6. | **DS** | # of severe decelerations per second |
| 7. | **DP** | # of prolongued decelerations per second |
| 8. | **ASTV** | Percentage of time with abnormal short term variability |
| 9. | **MSTV** | Mean value of short term variability |
| 10. | **ALTV** | Percentage of time with abnormal long term variability |
| 11. | **MLTV** | Mean value of long term variability |
| 12. | **Width** | Width of FHR histogram |
| 13. | **Min** | Minimum of FHR histogram |
| 14. | **Max** | Maximum of FHR histogram |
| 15. | **Nmax** | # of histogram peaks |
| 16. | **Nzeros** | # of histogram zeros |
| 17. | **Mode** | Histogram mode |
| 18. | **Mean** | Histogram mean |
| 19. | **Median** | Histogram median |
| 20. | **Variance** | Histogram variance |
| 21. | **Tendency** | Histogram tendency |

## 4.2 Feature Variable

- **CLASS:** FHR pattern class code (1 to 10) - Use this as a feature if you intend to perform a 10-class classification task. Consider, **NSP** variable as a predictor variable.

- **NSP:** Fetal state class code (N=normal; S=suspect; P=pathologic) - Use this as a feature if you intend to perform a 3-class classification task. Consider, **Class** variable as a predictor variable.


## 5. Acknowledgement

If you use this dataset in your research, **do not forget** to cite the following: 
1. [Ayres de Campos et al. (2000) *SisPorto 2.0: A Program for Automated Analysis of Cardiotocograms*, J Matern Fetal Med **5**:311-318[(https://onlinelibrary.wiley.com/doi/10.1002/1520-6661(200009/10)9:5%3C311::AID-MFM12%3E3.0.CO;2-9)
2. [Article DOI](https://doi.org/10.1002/1520-6661(200009/10)9:5%3C311::AID-MFM12%3E3.0.CO;2-9)

