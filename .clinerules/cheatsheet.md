# Project Cheatsheet

## Key Directories

```bash
./codes/                  # Main analysis notebooks
./codes/Utils/           # Utility Python modules
./model/                 # Trained models
./figs_tabs/            # Output figures and tables
```

## Common Commands

### Running Analysis Notebooks
NOTE: The following commands only serve as examples, pointing towards the relevant scripts. It doesn't mean running it will work. It is strongly advised to open the corresponding scripts in a jupyter environment and run by cells according to the users' needs.
```bash
# Patent Information Extraction
jupyter notebook codes/_2_00_patent_IE.ipynb

# Patent-Census Matching
jupyter notebook codes/_2_01_matcher_patent_census.ipynb

# ML Training & Evaluation
jupyter notebook codes/_2_02_ml_training_pred_eval_150.ipynb

# Occupational Similarity Analysis
jupyter notebook codes/_2_04_occ_sim_UK.ipynb
jupyter notebook codes/_2_04_occ_sim_US.ipynb
```

## Model Locations

### Patent-Census Matching Models
```bash
# Base path for matching models
./model/patent_census_match/smoted_5_models_5_cols/

# Individual model files
cb.pkl      # CatBoost
gnb.pkl     # Gaussian Naive Bayes
lgbm.pkl    # LightGBM
rf.pkl      # Random Forest
xgb.pkl     # XGBoost
```

### Name/Address Processing
```bash
# spaCy model path
./model/name_addr_md/
```

### Neural Network Model
```bash
# PyTorch model
./model/simple_nn_80_smoted.pt
```

## Utility Modules

```python
# Geographic utilities
from codes.Utils.geo import *

# HISCO similarity functions
from codes.Utils.hisco_sim import *

# Gender classification
from codes.Utils.sex_1_2_9 import *
```

## Output Directories

```bash
# Figures and tables
./figs_tabs/

# Notebook outputs
./codes/outputs/

# CatBoost logs
./codes/catboost_info/
```

## Notebook Naming Convention

- _2_XX_: Main analysis notebooks
- _3_X_: Modern data analysis notebooks
- Utils/: Utility scripts and modules

## Common Data Processing Steps

1. Patent Information Extraction:
   - Input: Raw patent documents
   - Process: Information extraction using spaCy
   - Output: Structured patent data

2. Patent-Census Matching:
   - Input: Processed patent data, census records
   - Process: ML-based matching
   - Output: Matched patent-census pairs

3. Occupational Similarity:
   - Input: Processed occupation data
   - Process: Similarity computation
   - Output: Similarity matrices and visualizations

## Model Training Workflow

1. Data Preprocessing:
   ```python
   # Run preprocessing notebook
   codes/pre_proc_patent.ipynb
   ```

2. Model Training:
   ```python
   # Train ML models
   codes/_2_02_ml_training_pred_eval_150.ipynb
   ```

3. Evaluation:
   ```python
   # Check results in
   codes/outputs/
   figs_tabs/
