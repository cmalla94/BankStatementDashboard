# BankStatementDashboard
The goal is have an interactive finance dashboard that helps me achieve my finanical goals. The project at the moment is to have an historical tab which shows analytics on transactions from 2014 to display how my spending patterns have changed or other insights that may be interesting. The second tab is the budget manager which will allow me to categorize transactions, set categorized budgets and have analytics. The end goal is have a smart assistant to suggest alternatives for my purchases, for example, it should recognize a regular coffee purchase from Starbucks then it may suggest a alternative cheaper yet upholding review standards option like McDonald's coffee. The AI assistant will in a separate repo once created so it can be modified and reused by other applications.

# Techonlogies used: Dash, Plotly, Python

## Milestone 1 -- Complete

-Worte a Python script (data_extraction.py) that first bins bank statments into respective subdirectories named as the year the bank statement belongs to. Then it pseudo-automates the scraping of PDF bank statemnts, it isn't fully automated because the PDFs are not being read the same way even though the PDF documents are the same structure, I only needed some data to start with my analysis so I was satisfied with around 600 rows. Will figure out alternative later to get all transactions

-make_datasets.py then creates a dataframe by creating date column (yyyy-mm-dd) and also extracting city names from the complete transaction name and putting them into a new column 'City'. For example, the transaction: [SFU PARKING SERVICES BURNABY BC] , [Burnaby] will be extracted

-hist_trans_tab.py is the code for the historical tab which displays an interactive table that can be filtered/sorted. Has a stacked bar graph to show number of transactions in each city and (work in progress), being able to dynamically switch to a bar graph to show amount of money spent in each city and being able filter out some cities

-budget_manager.py is the code for the budget manager tab which allows user to add new transactions through a form and shows the interactive datatable with the transactions saved into the transaction.csv file. The changes to the datatable are real-time and doesn't require refreshing the page

## Milestone 2 -- In progress

-More analytics to added to historical tab & budget manager. Add budget target widget, being able to upload a bank statement and have the program scrape and add the transactions (eliminating any duplicates) or looking into recently discovered RBC API to get my transactions 

--Update: RBC API requires me to have a company associated with the application, I will just keep using my personalized scraper but will make changes to make it more automated

-Added Sentry which emails me whenever my app breaks and just really useful for debugging
-Added new plots to the Budget Manager and made changes to color scheme

