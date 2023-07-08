import json
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

#method to read json data
json_file = open('loan_data_json.json')
data = json.load(json_file)

#transform dictionary to dataframe
loandata = pd.DataFrame(data)

#find unique values in column
loandata['purpose'].unique()

#describe the data
loandata.describe()

#describe data for specific colume
loandata['int.rate'].describe()
loandata['fico'].describe()
loandata['dti'].describe()

#get exponent of log.annual.inc
#install numpy
income =np.exp(loandata['log.annual.inc'])
loandata['annual income'] = income
loandata['annual income'].describe()

#add category to credit score ('fico')
length = len(loandata)
ficocat = []
for x in range(0,length):
    if loandata['fico'][x] >= 300 and loandata['fico'][x] <400:
        cat = 'Very Poor'
    elif loandata['fico'][x] >= 400 and loandata['fico'][x] <600:
        cat = 'Poor'
    elif loandata['fico'][x] >= 600 and loandata['fico'][x] <660:
        cat = 'Fair'
    elif loandata['fico'][x] >= 660 and loandata['fico'][x] <780:
        cat = 'Good'
    elif loandata['fico'][x] >= 780:
        cat = 'Excellent'
    else:
        cat = "Unknown"
    ficocat.append(cat)
    
ficocat = pd.Series(ficocat)
loandata['fico.category'] = ficocat

#example of conditional statment
loandata.loc[loandata['int.rate']>0.12, 'int.rate.type'] = 'High'
loandata.loc[loandata['int.rate']<=0.12, 'int.rate.type'] = 'Low'

#number of loans (or rows) by fico category
catplot = loandata.groupby(['fico.category']).size()
#create bar chart based on catplot
catplot.plot.bar(color = 'green', width = 0.1)
#show the bar chart
plt.show()

purpplot = loandata.groupby(['purpose']).size()
purpplot.plot.bar(color = 'purple', width = 0.3)
plt.show()


#scatter plots
ypoint = loandata['annual income']
xpoint = loandata['dti']
plt.scatter(xpoint, ypoint, )
plt.show()

#writing to csv
loandata.to_csv('loan_cleaned.csv', index = True)
