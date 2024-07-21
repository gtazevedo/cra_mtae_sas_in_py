# Credit Risk Analytics - Measurement Techniques Applications and Examples in SAS examples in python

This project is still under development. 

Here I'll build my own python examples using as base the SAS examples given in the book. The codes will be usually separated into `.ipynb` files and might not have the best possible implementation of the functions but will give you a close enough (plots won't be visually the same) or equal result to the ones in the book.

If you need a more detailed introduction into some python concepts, functions or packages for these implementations you can refer to [Snake Bear](https://snakebear.science/index.html).

Each chapter will be a different python notebook and these notebooks will have a short resumen of the theory in the book along with the examples. Sometimes this theory can be complemented with my knowledge or outside sources (when referenced). To have a look at the complete theory I recommend reading the book, you can find more details, papers, trainings, where to buy, the preview or info about the authors at  [Credit Risk Analytics](www.creditriskanalytics.net).

It's important to notice that this github project has no relationship with the authors nor their course in python (you can check it [here](https://www.deepcreditrisk.com/), this course is related to their book Deep Credit Risk: Machine Learning with Python). As of the moment I'm writing these notebooks I haven't taken this course nor watched their videos in youtube so my approach to converting these analysis to python may differ.

## Datasets

I'll go only to the brief descriptions that can be found in the books about the datasets but I won't make them available in my git project as they are available at [Credit Risk Analytics](www.creditriskanalytics.net).

More details please check Credit risk analytics : measurement techniques, applications, and examples in SAS.

### HMEQ

Reports characteristics and delinquency information for 5960 home equity loans. The data set has the following characteristics:

- BAD: 1 = applicating defaulted on loan or seriously delinquent; 0 = applicant paid the loan
- LOAN: Amount of the loan request
- MORTDUE: Amout due on existing mortgage
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

Data set in panel form and reports origination and performance observations for 50000 residentials U.S. mortgage borrowers over 60 periods. Periods have been deidentified. Key variables include:

- id: Borrower ID
- time: Time stamp of observation
- orig_time: Time stamp for origination
- first_time: Time stamp for first observation
- mat_time: Time stamp for maturity
- balance_time: Outstading balance at observation time
- LTV_time: Loan-to-value ratio at observation time, in %
- interest_rate_time: Interest rate at observation time, in %
- hpi_time: House price index at observation time, base year = 100
- gdp_time: GDP growth at observation time, in %
- uer_time: Unemployment rate at observation time, in %
- REtype_CO_orig_time: Real estate type condominium = 1, otherwise = 0
- REtype_PU_orig_time: Real estate planned urban development = 1, otherwise = 0 
- REtype_SF_orig_time: Single-family home = 1, otherwise = 0
- investor_orig_time: Investor borrower = 1, otherwise = 0
- balance_orig_time: Outstading balance at origination time
- FICO_orig_time: FICO score at origination time, in %
- LTV_orig_time: Loan-to-value ratio at origination time, in %
- Interest_Rate_orig_time: Interest rate at origination time, in %
- hpi_orig_time: House price index at origination time, base year = 100
- default_time: Default observation at observation time
- payoff_time: Payoff observation at observation time
- status_time: Default(1), payoff(2), and nondefault/nonpayoff(0) observation at observation time

### Data Set LGD

Data set includes 2545 observations on loans and LGDs. Key variables are:

- LTV: Loan-to-value ratio, in %
- Recovery_rate: Recovery_rate, in %
- lgd_time: Loss rate given default (LGD) in %
- y_logistic - Logistic transofmration of the LGD
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
- LIQASSTA: liquid assets to total assets
- SIZE: Natural logarithm of total assets


