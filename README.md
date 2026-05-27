# Credit Risk Analytics - Measurement Techniques, Applications, and Examples in SAS: Python Implementations

This project is actively under development. This repository contains Python implementations of the methodologies and SAS examples presented in the book *Credit Risk Analytics: Measurement Techniques, Applications, and Examples in SAS* by Bart Baesens, Daniel Roesch, and Harald Scheule. The goal is to cover all chapters and subsequently provide solutions for the practice questions at the end of each chapter.

Here, I build my own Python examples using the SAS baselines provided in the book. The code is organized into Jupyter Notebooks (`.ipynb`). While these notebooks may not always represent the most optimal or advanced Python programming patterns, they are designed to produce equivalent or highly comparable results to the ones in the book (although visual styling for plots may differ slightly).

If you need a more detailed introduction to some Python concepts, functions, or packages for these implementations, you can refer to [Snake Bear](https://snakebear.science/index.html).

Each chapter is contained in a separate Jupyter Notebook. These notebooks include a concise summary of the theory discussed in the book alongside the code examples. Occasionally, the theoretical summaries are supplemented by outside sources or personal insights (which will be specifically referenced; the book itself will not be cited at every instance, as the repository is entirely based on its content). To explore the comprehensive theory, I highly recommend reading the book. You can find more details, papers, training programs, ordering options, preview chapters, and author biographies at [Credit Risk Analytics](http://www.creditriskanalytics.net).

It is important to note that this GitHub project is entirely independent and has no official relationship with the authors, nor is it associated with their Python course (which you can check [here](https://www.deepcreditrisk.com/) for their book *Deep Credit Risk: Machine Learning with Python*). At the time of developing these notebooks, I have not taken their course or watched their YouTube videos; thus, my approach to translating these analyses to Python may differ.

Even though this project is independent, I highly recommend reading the authors' books or keeping them on hand for reference and sanity checks.

## Datasets

I provide only brief descriptions of the datasets as found in the book. I will not host the dataset files in this repository since they are proprietary and can be downloaded from the official website [Credit Risk Analytics](http://www.creditriskanalytics.net).

For more details, please refer to the book: *Credit Risk Analytics: Measurement Techniques, Applications, and Examples in SAS*.

### HMEQ

Reports characteristics and delinquency information for 5960 home equity loans. The dataset has the following characteristics:

- BAD: 1 = applicant defaulted on loan or is seriously delinquent; 0 = applicant paid the loan
- LOAN: Amount of the loan request
- MORTDUE: Amount due on existing mortgage
- VALUE: Value of current property
- REASON: DebtCon = Debt consolidation; HomeImp = Home improvement
- JOB: Occupational categories
- YOJ: Years at present job
- DEROG: Number of major derogatory reports
- DELINQ: Number of delinquent credit lines
- CLAGE: Age of oldest credit line in months
- NINQ: Number of recent credit inquiries
- CLNO: Number of credit lines
- DEBTINC: Debt-to-income ratio

### Data Set Mortgage

Dataset in panel form that reports origination and performance observations for 50,000 residential U.S. mortgage borrowers over 60 periods. Periods have been deidentified. Key variables include:

- id: Borrower ID
- time: Time stamp of observation
- orig_time: Time stamp for origination
- first_time: Time stamp for first observation
- mat_time: Time stamp for maturity
- balance_time: Outstanding balance at observation time
- LTV_time: Loan-to-value ratio at observation time, in %
- interest_rate_time: Interest rate at observation time, in %
- hpi_time: House price index at observation time, base year = 100
- gdp_time: GDP growth at observation time, in %
- uer_time: Unemployment rate at observation time, in %
- REtype_CO_orig_time: Real estate type condominium = 1, otherwise = 0
- REtype_PU_orig_time: Real estate planned urban development = 1, otherwise = 0 
- REtype_SF_orig_time: Single-family home = 1, otherwise = 0
- investor_orig_time: Investor borrower = 1, otherwise = 0
- balance_orig_time: Outstanding balance at origination time
- FICO_orig_time: FICO score at origination time, in %
- LTV_orig_time: Loan-to-value ratio at origination time, in %
- Interest_Rate_orig_time: Interest rate at origination time, in %
- hpi_orig_time: House price index at origination time, base year = 100
- default_time: Default observation at observation time
- payoff_time: Payoff observation at observation time
- status_time: Default(1), payoff(2), and nondefault/nonpayoff(0) observation at observation time

### Data Set LGD

Dataset includes 2545 observations on loans and LGDs. Key variables are:

- LTV: Loan-to-value ratio, in %
- Recovery_rate: Recovery rate, in %
- lgd_time: Loss rate given default (LGD) in %
- y_logistic: Logistic transformation of the LGD
- lnrr: Natural logarithm of the recovery rate
- Y_probit: Probit transformation of the LGD
- purpose1: Indicator variable for the purpose of the loan; 1 = renting purpose, 0 = other
- event: Indicator variable for a default or cure event; 1 = event, 0 = no event

### Data Set Ratings

Corporate ratings where the ratings have been numerically encoded (1 = AAA, and so on). It has the following variables:

- COMMEQTA: Common equity to total assets
- LLPLOANS: Loan loss provision to total loans
- COSTTOINCOME: Operating costs to operating income
- ROE: Return on equity
- LIQASSTA: Liquid assets to total assets
- SIZE: Natural logarithm of total assets


