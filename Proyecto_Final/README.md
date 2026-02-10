# Final Project

## Overview
This project focuses on performing Exploratory Data Analysis (EDA) using both manual and automatic methods. The analysis is conducted on datasets stored in the `data/raw` directory, with processed data saved in the `data/processed` directory. The results, including visualizations and reports, are organized in the `reports/figures` directory.

## Project Structure
- **notebooks/**: Contains Jupyter notebooks for analysis.
  - `20260207_Final_Project.ipynb`: Main notebook for EDA tasks.
  
- **src/**: Source code for data processing and EDA.
  - `data_processing.py`: Data cleaning and preprocessing functions.
  - `eda_manual.py`: Functions for manual EDA, including visualizations and summary statistics.
  - `eda_automatic.py`: Functions for automatic EDA, generating reports and visualizations.

- **data/**: Directory for data files.
  - **raw/**: Raw data files.
  - **processed/**: Processed data files ready for analysis.

- **reports/**: Directory for storing figures and visualizations.
  - **figures/**: Generated figures from the analysis.

- **requirements.txt**: Lists necessary Python packages and dependencies for the project.

- **environment.yml**: Conda environment configuration file.

- **.gitignore**: Specifies files and directories to be ignored by Git.

## Installation
To set up the project environment, you can use either `requirements.txt` or `environment.yml`.

### Using requirements.txt
1. Create a virtual environment (optional but recommended).
2. Install the required packages:
   ```
   pip install -r requirements.txt
   ```

### Using environment.yml
1. Create a conda environment:
   ```
   conda env create -f environment.yml
   ```

## Usage
- Open the Jupyter notebook `20260207 Proyecto final.ipynb` to start the analysis.
- Use the scripts in the `src` directory for data processing and EDA tasks.

## License
This project is licensed under the MIT License.