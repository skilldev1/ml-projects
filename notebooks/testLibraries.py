import sys
print("Python Version:", sys.version)
print()

# Test Core ML
import numpy as np
import pandas as pd
from sklearn.datasets import load_iris
print("✅ NumPy, Pandas, Scikit-learn loaded")

# Test Deep Learning
import torch
print("✅ PyTorch loaded - GPU:", torch.cuda.is_available())

# Test NLP
from transformers import pipeline
print("✅ Transformers loaded")

# Test Visualization
import matplotlib.pyplot as plt
import seaborn as sns
print("✅ Matplotlib, Seaborn loaded")

# Test Jupyter
import jupyter
print("✅ Jupyter loaded")

# Test Gradient Boosting
import xgboost as xgb
import lightgbm as lgb
print("✅ XGBoost, LightGBM loaded")

print("\n" + "="*50)
print("🎉 ALL ML LIBRARIES WORKING ON PYTHON 3.14! 🎉")
print("="*50)