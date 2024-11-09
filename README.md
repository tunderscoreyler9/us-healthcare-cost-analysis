# us-healthcare-cost-analysis
## Objective: 
To analyze healthcare costs across different U.S. states, identify cost disparities, and understand the factors contributing to these differences (e.g., state regulations, demographics, insurance coverage).

## Questions to Explore:
- What is the average healthcare cost per person in each state?
- Which states have the highest and lowest healthcare costs?
- How do factors like insurance coverage, healthcare access, or state policies affect costs?

healthcare_analysis/
│
├── data/                      # Store all downloaded datasets here
│   ├── raw/                  # Original downloaded files
│   └── processed/            # Cleaned and processed datasets
│
├── notebooks/                # Jupyter notebooks for analysis
│   ├── 01_data_loading.ipynb
│   ├── 02_data_cleaning.ipynb
│   ├── 03_exploratory_analysis.ipynb
│   └── 04_statistical_analysis.ipynb
│
├── src/                      # Python source code
│   ├── __init__.py
│   ├── data_loader.py       # Functions for loading different data sources
│   ├── data_cleaner.py      # Data cleaning functions
│   └── visualizations.py     # Visualization functions
│
└── README.md                 # Project documentation