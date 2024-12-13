# US Healthcare Cost Analysis 1991-2020

## Objective
To analyze longitudinal healthcare cost trends across U.S. states from 1991 to 2020, identify long-term cost disparities, and understand the evolution of healthcare spending patterns across different regions of the United States.

## Questions Explored
- How have healthcare costs per capita evolved across different states over three decades?
- Which states consistently show highest and lowest healthcare costs?
- What regional patterns emerge in healthcare spending over time?
- How has the distribution of healthcare spending changed between 1991 and 2020?

## Key Findings
- Analysis of healthcare spending per capita across all US states for four key years (1991, 2000, 2010, 2020).
- Identification of long-term regional cost variations.
- Tracking of state-by-state spending evolution.
- Analysis of growth rates and spending patterns.
- Cross-temporal comparisons of healthcare costs.

## Project Structure
```shell
healthcare_analysis/
│
├── data/                                # Data storage
│   ├── raw/                            # Original downloaded files
│   │   ├── kff_healthcare_spending_per_capita_1991.csv
│   │   ├── kff_healthcare_spending_per_capita_2000.csv
│   │   ├── kff_healthcare_spending_per_capita_2010.csv
│   │   └── kff_healthcare_spending_per_capita_2020.csv
│   └── processed/                      # Cleaned and processed datasets
│
├── notebooks/                          # Jupyter notebooks for analysis
│   ├── 01_data_loading.ipynb         # Data loading and cleaning
│   ├── 02_exploratory_analysis_2020.ipynb         # Analysis of 2020 data
│   ├── 02_exploratory_analysis_2010         # Analysis of 2010 data
│   ├── 02_exploratory_analysis_2000         # Analysis of 2000 data
│   ├── 02_exploratory_analysis_1991     # Analysis of 1991 data
│   └── 06_complete_comparison.ipynb   # Cross-temporal analysis
│
├── src/                               # Python source code
│   ├── __init__.py
│   ├── data/                         # Data handling modules
│   │   ├── data_loader.py           # Data loading functions
│   └─ analysis/                    # Analysis modules
│       └── metrics.py               # Analysis metrics
│
└── README.md                         # Project documentation


## Data Sources
- **Kaiser Family Foundation (KFF) State Health Facts**
- Datasets: Healthcare Spending per Capita by State for:
  - 1991
  - 2000
  - 2010
  - 2020

## Analysis Components
1. **Individual Year Analyses** (Notebooks 02-05)
   - Year-specific data cleaning and preparation.
   - Basic statistical summaries.
   - Regional analysis.
   - State rankings and comparisons.
   - Cross-regional comparisons.
   - Temporal changes in regional patterns.
   - Regional variance analysis.

2. **Longitudinal Comparison** (Notebook 06)
   - 30-year trend analysis.
   - Growth rate calculations.
   - Cross-temporal patterns.
   - Regional evolution.

## Key Visualizations
- Time series plots of spending trends.
- Regional distribution box plots.
- State-by-state comparison bar plots.
- Growth rate analysis charts.
- Cross-temporal comparison visualizations.

## Requirements
Required Python packages:
``` python
pandas>=2.0.0 numpy>=1.24.0 matplotlib>=3.7.0 seaborn>=0.12.0 jupyter>=1.0.0
```


## Setup and Installation
1. Clone the repository:
`https://github.com/tunderscoreyler9/us-healthcare-cost-analysis.git`

2. Create and activate a virtual environment:
``` python
# To create the venv, type:
python -m venv venv 

# To activate the venv:
source venv/bin/activate 

# On Windows, use this to activate your venv
venv\Scripts\activate
```


3. Install required packages:
``` python
pip install -r requirements.txt
```


## Usage
1. Start with individual year analyses (Notebooks 02-05).
2. Explore regional patterns in these notebooks.
3. Examine complete temporal comparison (Notebook 06).

## Results
The analysis reveals:
- Significant growth in healthcare spending across all states from 1991 to 2020.
- Persistent regional disparities in healthcare costs.
- Varying growth rates across different regions and states.
- Evolution of healthcare spending distribution over time.

## Future Work
Potential areas for expansion:
- Integration with demographic data.
- Policy impact analysis across time periods.
- Healthcare outcome correlation analysis.
- Economic factor integration.

## Contributing
Contributions are welcome! Please feel free to submit a Pull Request.

## License
This project is licensed under the MIT License - see the LICENSE file for details.

## Acknowledgments
- Data provided by Kaiser Family Foundation.
- Analysis inspired by healthcare policy research, KFF, and my family.
- Project completed as part of data analysis coursework.