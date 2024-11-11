# US Healthcare Cost Analysis

## Objective
To analyze healthcare costs across different U.S. states, identify cost disparities, and understand the patterns in healthcare spending across different regions of the United States.

## Questions to Explore:
- What is the average healthcare cost per person in each state?
- Which states have the highest and lowest healthcare costs?
- How do factors like insurance coverage, healthcare access, or state policies affect costs?

## Key Findings
- Analysis of 2020 healthcare spending per capita across all US states
- Regional variations in healthcare costs
- State-by-state comparisons with national averages
- Distribution patterns in healthcare spending

## Project Structure

``` shell
healthcare_analysis/
│
├── data/                            # Store all downloaded datasets here
│   ├── raw/                         # Original downloaded files
│   │    └── kff_healthcare_spending_per_capita_2020.csv
│   └── processed/                   # Cleaned and processed datasets
│
├── notebooks/                       # Jupyter notebooks for analysis
│   ├── 01_data_loading.ipynb        # Initial data loading and cleaning
│   └── 02_exploratory_analysis.ipynb # Comprehensive analysis and visualizations
│
├── src/                             # Python source code
│   ├── init.py
│   ├── data_loader.py               # Functions for loading different data sources
│   ├── data_cleaner.py              # Data cleaning functions
│   └── visualisations.py            # Visualization functions
│
└── README.md                        # Project documentation
```


## Data Sources
- **Kaiser Family Foundation (KFF) State Health Facts**
- Dataset: Healthcare Spending per Capita by State (2020)

## Analysis Components
1. **Data Loading and Initial Overview**
   - Data cleaning and preparation
   - Basic statistical summaries
   - Initial data validation

2. **Regional Analysis**
   - Definition of four major US regions
   - Regional statistics and comparisons
   - Box plot visualizations of regional distributions

3. **State-by-State Analysis**
   - Comprehensive bar plots
   - State rankings
   - Regional comparisons

4. **Distribution Analysis**
   - Healthcare spending distribution
   - Comparison to national average
   - Variance analysis

5. **Statistical Summaries**
   - Detailed regional statistics
   - Top and bottom spending states
   - Differences from national average

## Key Visualizations
- Regional distribution box plots
- State-by-state comparison bar plots
- Healthcare spending distribution histograms
- Regional analysis with statistical summaries

## Requirements
Required Python packages:
``` python
pandas>=2.0.0
numpy>=1.24.0
matplotlib>=3.7.0
seaborn>=0.12.0
jupyter>=1.0.0
```

## Setup and Installation
1. Clone the repository
    ```bash
    git clone https://github.com/yourusername/us-healthcare-cost-analysis.git
    cd us-healthcare-cost-analysis
    ```

2. Create and activate virtual environment
    ```bash
    python -m venv venv
    source venv/bin/activate  # On Windows: venv\Scripts\activate
    ```

3. Install required packages
    ```bash
    pip install -r requirements.txt
    ```

4. Launch Jupyter Notebook
    ```bash
    jupyter notebook
    ```

## Usage
1. Start with `01_data_loading.ipynb` for initial data preparation
2. Move to `02_exploratory_analysis.ipynb` for comprehensive analysis

## Results
The analysis reveals:
- Significant variations in healthcare spending across regions
- Clear patterns in state-level healthcare costs
- Regional clustering of healthcare spending levels
- Identification of outlier states in terms of healthcare costs

## Future Work
Potential areas for expansion:
- Additional demographic analysis
- Time series analysis of spending trends
- Correlation with other healthcare metrics
- Policy impact analysis

## Contributing
Feel free to fork the repository and submit pull requests. For major changes, please open an issue first to discuss what you would like to change.

## License
This project is licensed under the MIT License - see the LICENSE file for details.

## Acknowledgments
- Data provided by Kaiser Family Foundation
- Analysis inspired by healthcare policy research