# **Needs extracting all explicitly displayed API-key**
# Patent-Census Data Analysis Project

This project focuses on analyzing and linking patent data with census records through machine learning approaches, along with occupational similarity analysis for both UK and US datasets.

## Project Structure

```
.
├── codes/                    # Jupyter notebooks and Python scripts
│   ├── Utils/               # Utility Python modules
│   └── ...                  # Various analysis notebooks
├── model/                   # Trained models and configurations
│   ├── name_addr_md/       # spaCy model for name/address processing
│   └── patent_census_match/ # ML models for patent-census matching
├── figs_tabs/              # Generated figures and tables
```

## Core Components

### 1. Patent Information Extraction
- Located in: `codes/_2_00_patent_IE.ipynb`
- Extracts structured information from patent documents

### 2. Patent-Census Matching
- Located in: `codes/_2_01_matcher_patent_census.ipynb`
- ML models for matching patent records with census data
- Uses ensemble of models (CatBoost, XGBoost, LightGBM, Random Forest)

### 3. ML Training and Evaluation
- Located in: `codes/_2_02_ml_training_pred_eval_150.ipynb`
- Model training workflows and evaluation metrics
- Includes SMOTE sampling for handling imbalanced data

### 4. Occupational Similarity Analysis
- UK Analysis: `codes/_2_04_occ_sim_UK.ipynb`
- US Analysis: `codes/_2_04_occ_sim_US.ipynb`
- Modern UK Analysis: `codes/_3_1_occ_sim_UK_modern.ipynb`

## Utility Modules

Located in `codes/Utils/`:
- `geo.py`: Geographic data processing
- `hisco_sim.py`: HISCO classification similarity computations
- `sex_1_2_9.py`: Gender classification utilities

## Models

### Patent-Census Matching Models
Located in `model/patent_census_match/smoted_5_models_5_cols/`:
- CatBoost (`cb.pkl`)
- Gaussian Naive Bayes (`gnb.pkl`)
- LightGBM (`lgbm.pkl`)
- Random Forest (`rf.pkl`)
- XGBoost (`xgb.pkl`)

### Name/Address Processing Model
Located in `model/name_addr_md/`:
- spaCy model for processing names and addresses
- Includes NER, parsing, and tokenization capabilities

## Getting Started

1. Set up Python environment (recommended Python 3.x)
2. Install required packages:
```bash
pip install -r requirements.txt  # Note: Create this file with necessary dependencies
```

Key dependencies:
- Jupyter Notebook
- PyTorch 
- CatBoost
- XGBoost
- LightGBM
- spaCy
- scikit-learn

## Usage
NOTE: The following commands only serve as examples, pointing towards the relevant scripts. It doesn't mean running it will work. It is strongly advised to open the corresponding scripts in a jupyter environment and run by cells according to the users' needs.

1. Patent Information Extraction:
```bash
jupyter notebook codes/_2_00_patent_IE.ipynb
```

2. Patent-Census Matching:
```bash
jupyter notebook codes/_2_01_matcher_patent_census.ipynb
```

3. ML Training & Evaluation:
```bash
jupyter notebook codes/_2_02_ml_training_pred_eval_150.ipynb
```

4. Occupational Similarity Analysis:
```bash
jupyter notebook codes/_2_04_occ_sim_UK.ipynb  # For UK analysis
jupyter notebook codes/_2_04_occ_sim_US.ipynb  # For US analysis
```

## Outputs

- Generated figures are saved in `figs_tabs/`
- Trained models are saved in `model/`
- Analysis outputs from notebooks are saved in `codes/outputs/`
