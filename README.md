# Mini Project 2 - Blue Bank

#### Project brief:
Blue Bank is a bank that has a loan department which is currently understaffed. They supply loans to individuals and don’t have much reporting on how risky these borrowers are. They’d like to see a report of borrowers who may have issues paying back the loan.

___

In order to satisfy the project brief, I will need to process and manipulate the dataset using the Pandas library in Python.  

Here's a summary of what my Python code will need to do:

1. Import the required libraries incl. json, pandas, numpy, and matplotlib.pyplot.
2. Read a JSON file named and load its contents into a dataframe.
3. The exponential of the annual income will need to be calculated using the numpy 'exp()' function and then added as a new column.
4. Define the Fico category for each loan based on the 'fico' column based on ranges using conditional statements.
5. Define 'High' or 'Low' interest rates based on the values in the interest rate column using conditional statements.
6. The number of loans (or rows) will then be counted for each Fico category using the 'groupby' function, and a bar chart will be created to visualize the counts.
7. Similarly, the number of loans will be counted for each 'purpose' using the 'groupby' function, and another bar chart will be to visualize the counts.
8. Scatter plots will also be created using the annual income column as the y-coordinate and the dti column as the x-coordinate.
9. The modified DataFrame will then be written to a CSV file named 'loan_cleaned.csv', including the index column.

In summary, the code will need to read JSON data, transform it into a DataFrame, perform data analysis and visualization using pandas and matplotlib, and export the modified DataFrame to a CSV file.

Below is the dashboard that I created with the cleaned dataset:  
[Link to Interactive Dashboard](https://public.tableau.com/app/profile/douglas1371/viz/BlueBankLoans_16873800924500/LoanDashboard)  
![Blue Bank Loan Dashboard](https://github.com/DougWicker/Mini-Project-2-Blue-Bank/blob/8f97bc0a394571f428393be68a7fc363b6f865ad/Blue%20Bank/Blue%20Bank%20Loans%20Dashboard.png)

This project was part of a Data Analysis Bootcamp, hosted on Udemy and Created by Dee Naidoo, and contributed to the following certificate:
![Certificate of Completion](https://github.com/DougWicker/Mini-Project-2-Blue-Bank/blob/8f97bc0a394571f428393be68a7fc363b6f865ad/Bootcamp%20Certificate.jpg)
