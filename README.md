# US Healthcare Cost Analysis: 30-Year Spending Evolution (1991-2020)

## Project Overview
This project analyzes healthcare spending trends across U.S. states over three decades, examining regional patterns, cost disparities, and spending evolution. The analysis combines data from the Kaiser Family Foundation (KFF) for four key years (1991, 2000, 2010, 2020) to provide insights into long-term healthcare cost dynamics.

## Prerequisites

### Python Installation
1. **Install Python** (Version 3.8 or higher recommended):
   - Visit [python.org](https://www.python.org/downloads/)
   - Download the appropriate version for your OS.
   - During installation, check "Add Python to PATH".
   - Verify installation by opening terminal/command prompt and typing:
     ```bash
     python --version
     ```

2. **Text Editor/IDE** (Choose one):
   - VSCode (Recommended): [Download](https://code.visualstudio.com/)
   - PyCharm: [Download](https://www.jetbrains.com/pycharm/)
   - Jupyter Lab: Will be installed with requirements.

### Package Management
1. **Understanding Python Packages**:
   - Packages are collections of Python modules.
   - They extend Python's functionality for data analysis.
   - Key packages in this project:
     - `pandas`: Data manipulation and analysis.
     - `numpy`: Numerical computations.
     - `matplotlib` & `seaborn`: Data visualization.
     - `jupyter`: Interactive notebook environment.
     - `statsmodels`: Statistical analyses.

2. **Virtual Environment**:
   ```bash
   # Create virtual environment
   python -m venv venv

   # Activate virtual environment
   # On Windows:
   venv\Scripts\activate
   # On macOS/Linux:
   source venv/bin/activate

3. **Install required packages**:

``` python
pip install -r requirements.txt
```

### Project Structure:
``` shell
healthcare_analysis/
│
├── data/                              
│   ├── raw/                          # Original KFF datasets
│   │   ├── kff_healthcare_spending_per_capita_1991.csv
│   │   ├── kff_healthcare_spending_per_capita_2000.csv
│   │   ├── kff_healthcare_spending_per_capita_2010.csv
│   │   └── kff_healthcare_spending_per_capita_2020.csv
│   └── processed/                    # Cleaned datasets
│
├── notebooks/                        # Analysis notebooks
│   ├── 01_data_loading.ipynb        # Initial data preparation
│   ├── 02_exploratory_analysis_2020.ipynb
│   ├── 02_exploratory_analysis_2010.ipynb
│   ├── 02_exploratory_analysis_2000.ipynb
│   ├── 02_exploratory_analysis_1991.ipynb
│   └── 06_complete_comparison.ipynb # Cross-temporal analysis
│
├── src/                             # Source code
│   ├── data/                       
│   │   └── data_loader.py          # Data loading utilities
│   └── analysis/
│       └── metrics.py              # Analysis functions
│
├── requirements.txt                 # Package dependencies
└── README.md                       # Project documentation
```

### Installation and Setup
1. Clone the Repository:
``` python 
git clone https://github.com/tunderscoreyler9/us-healthcare-cost-analysis.git
cd us-healthcare-cost-analysis
```

2. Environment Setup:
``` python
# Create virtual environment
python -m venv venv

# Activate virtual environment
# Windows:
venv\Scripts\activate
# macOS/Linux:
source venv/bin/activate

# Install dependencies
pip install -r requirements.txt
```

### 3. Data Preparation
- The KFF dataset files are in the `data/raw/` directory.
- Files are named correctly according to their years.
- Run the data loading notebook (`01_data_loading.ipynb`) first to prepare datasets.

### Analysis Components

#### Individual Year Analyses
Each year-specific notebook (1991, 2000, 2010, 2020) contains:
- Basic statistical summaries.
- Regional analysis.
- Distribution analysis.
- Outlier detection.
- Visualization suite.
- Statistical significance testing.

#### Longitudinal Analysis
The complete comparison notebook includes:
- 30-year trend analysis.
- Growth rate calculations.
- Cross-temporal patterns.
- Regional evolution studies.

### Key Features

#### Data Processing
- Automated data cleaning and standardization.
- Regional classification system.
- Outlier detection and handling.
- Missing value management.

#### Statistical Analysis
- Descriptive statistics.
- Inferential testing.
- Time series analysis.
- Regional comparisons.

#### Visualization Suite
- Time series plots.
- Distribution analysis.
- Regional comparisons.
- Growth rate visualizations.

### Usage Guide

#### 1. Initial Setup
```bash
# Navigate to project directory
cd us-healthcare-cost-analysis

# Activate virtual environment
source venv/bin/activate  # or venv\Scripts\activate on Windows

# Launch Jupyter
jupyter lab
```

### 2. Running the Analysis
1. Start with `01_data_loading.ipynb`.
2. Proceed through year-specific analyses (02-05).
3. Complete with longitudinal comparison (06).

### 3. Modifying the Analysis
- Parameters can be adjusted in `src/analysis/metrics.py`.
- Regional definitions can be modified in notebooks.
- Visualization settings can be customized in plot commands.

### Results and Findings
Detailed findings are available in each notebook, including:
- Regional spending patterns.
- Growth rate analysis.
- Statistical significance tests.
- Trend visualizations.

### Troubleshooting

#### Common Issues and Solutions

**Package Installation Errors**:
```bash
pip install --upgrade pip
pip install -r requirements.txt --no-cache-dir
```

### Jupyter Notebook Issues
```bash
jupyter notebook clean
jupyter lab build
```

### Data Loading Errors
- Verify file paths in `data_loader.py`.
- Check CSV file formatting.
- Ensure correct file names.

### Contributing
1. Fork the repository.
2. Create a feature branch.
3. Commit changes.
4. Push to the branch.
5. Create a Pull Request.

### Future Development
- Integration with demographic data.
- Policy impact analysis.
- Healthcare outcome correlation.
- Economic factor integration.
- Interactive dashboard development.

### License
This project is licensed under the MIT License - see the LICENSE file for details.

### Acknowledgments
- Kaiser Family Foundation for data provision.
- Healthcare policy research community.
- Python data science community.
- Family support and inspiration.

### Contact
For questions or collaboration:
- **GitHub**: [tunderscoreyler9](https://github.com/tunderscoreyler9)
- **Project Issues**: [Issue Tracker](https://github.com/tunderscoreyler9/us-healthcare-cost-analysis/issues)