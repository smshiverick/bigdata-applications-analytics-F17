# Project: Workflow Pipeline
The steps involved in carrying out the project analysis and report are outlined below. 

## Step 1. Download the data
* The `get-data.py` function extracts the NSDUH-2015 data from the SAMH Data Archive.
* This function was also included in the interactive notebook `BDA-Project-Data.ipynb`. 

## Step 2. Data Cleaning and Preparation
* Steps involved in cleaning the data are descrived in `BDA-Project-Data.ipynb`.
* Missing values were removed, data values were recoded, features were renamed. 
* The data was subset according to features of interest and aggregated variables created. 

## Step 3. Exploratory Data Analysis
* Frequency summaries and crosstabulations created in 'BDA-Project-Explore-Data.ipynb'.
* Simple frequency histogram plotted proportions of Prescription Opioid Misuse and Heroin Use. 

## Step 4. Data Visualization
* Scatterplot with weighted regression created in `BDA-Project-Data-Visualization.ipynb`. 
* Pairplots for selected features were created using Seaborn package.

## Step 5. Analytics Classifier Models for Heroin Use
* Classifier models were constructed using Scikit-Learn in `BDA-Analytics-Classifier-Heroin.ipynb`.
* Logistic regression classifier, Decision Trees, Random Forests, Gradient Boosting Classifier.
* Plots of Coefficints with value of Regularization Parameter, and Feature Importance.

## Step 6. Analytics: Classifier Models for Prescription Opioid Misuse
* Classifier models for PRLMIS were constructed in `BDA-Analytics-Classifier-Heroin.ipynb`.
* Logistic regression classifier, Decision Trees, Random Forests, Gradient Boosting Classifier.
* Plots of Coefficints with value of Regularization Parameter, and Feature Importance.

## Step 7. Discussion and Conclusion
* Summary of major findings, extension to Big Data, Health Analytics
* Comparison of Classifier Models
* Limitations and Future Directions

## Appendix. Code References
* References for code and interactive python Jupyter Notebooks
