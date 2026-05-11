
Development Workflow
Data Preparation
I used Pandas for the initial data cleaning and exploratory analysis. The pipeline includes handling missing values, cleaning outliers in the training set, and normalizing numerical features using StandardScaler to ensure the Autoencoder converged properly.

Model Implementation

Isolation Forest: I used this as a baseline because it is effective at isolating anomalies in high-dimensional space without requiring labeled data.

Autoencoders (PyTorch): I built a neural network to learn a compressed representation of normal traffic. The model identifies anomalies based on reconstruction error; if the model cannot accurately reconstruct a data point, it is flagged as an outlier.

Note on Transformers: I experimented with Transformer-based architectures for this data. However, for this specific dataset and the reconstruction-based approach, I found the Autoencoder provided more stable and reliable results.

Results
The Isolation Forest was fast and efficient for simple outliers.

The Autoencoder was better at capturing complex, non-linear relationships and "hidden" anomalies.

├── data/
│   ├── demo/               # Sample data for testing the final pipeline
│   ├── processed/          # Cleaned data and model predictions (IF, AE, Transformer)
│   └── raw/                # Original network.csv dataset
├── models/                 # Saved weights (.pth) and serialized models (.joblib, .pkl)
├── notebooks/              # Step-by-step development process
│   ├── 00_data_prep.ipynb  # Data cleaning and feature engineering
│   ├── 01_if_baseline.ipynb# Isolation Forest implementation
│   ├── 02_autoencoder.ipynb# Deep Learning (PyTorch) implementation
│   ├── 03_transformer.ipynb# Experimental Transformer architecture
│   ├── 04_compare.ipynb    # Performance metrics and visualization
│   └── 05_demo.ipynb       # Final pipeline testing on unseen data
└── README.md

Author
Anand Kumar Tanuku""")
