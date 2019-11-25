# BankStatementDashboard

## Overview: 
This project is to create an interactive finance dashboard to help aid in achieving financial goals. 

## Goals: 
 This project will provide financial information, insights, and tools in display tabs. The first tab is a historical tab that shows analytics of transactions from 2014. The historical tab will display transactional trends, statistical insights and changes in spending patterns. The second tab is a budget manager that will help categorize transactions, set categorized budgets and provide analytics. The last goal of this project is to implement a smart AI assistant that suggests alternate purchases. For example, it should recognize a regular coffee purchase from Starbucks and suggest an alternative cheaper well-rated option like McDonald's coffee. 
 <a name="footnote">Note</a>: The smart AI assistent will be created in a separate repo for easy modification and portability to other applications. 

## Techonlogies used: 
- Dash
- Plotly 
- Python

## Milestone 1 -- Complete

- [data_extraction.py](data_extraction.py) bins bank statements into respective subdirectories by the year of the bank statement. Then, `data_extraction.py` scrapes the PDF bank statement for transactions. 
    - <a name="Sidenote">Sidenote</a>: The script is not able to scrape all the information from PDF files yet. This problem will be addressed in the future. 

- [make_datasets.py](make_datasets.py) creates a dataframe by creating date column (yyyy-mm-dd), extracts city names from the complete transaction name and puts them into a new column 'City'. 
    - I.E. The transaction: `[SFU PARKING SERVICES BURNABY BC]` , `[Burnaby]` will be extracted.

- [hist_trans_tab.py](hist_trans_tab.py) is the source code for the historical tab. The historical tab displays an interactive table that can be filtered and sorted. The graph displayed will show a stacked bar graph to show the number of transactions in each city. 
    - <a name="Sidenote">Sidenote</a>: The option to dynamically switch between showing amount of money spent in each city and being able to filter out some cities is still a work in progress. 

- [budget_manager.py](budget_manager.py) is the code for the budget manager tab. The budget manager tab allows users to add new transactions through a form and displays an interactive data table of transactions that are saved in the transaction.csv file. The changes to the data table are real-time and does not require the user to refresh the page.

## Milestone 2 -- In progress

### Finished
- More analytics have been added to the historical tab & budget manager. 

### Journal Log
- The budget target widget needs to be added.
- The ability to upload a bank statement and have the program scrape transactions needs to be added.
    - This functionality must eliminate any duplicates that could be added. 
- A recently discovered RBC API could help this project grab transactional data 
    - <a name="Update">Update</a>: The RBC API requires a company association to use the application. So, the API method will no longer be considered. The current scraper will be further developed to be more automated.  
- Sentry was added to help notify app downtime. Sentry has been useful for debugging. 
- New plots and color scheme changes were added to the Budget Manager. 


