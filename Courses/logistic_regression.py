import numpy as np
import pandas as pd
import statsmodels.api as sm
import matplotlib.pyplot as plt
from sklearn import linear_model, datasets

loansData = pd.read_csv('https://spark-public.s3.amazonaws.com/dataanalysis/loansData.csv')

loansData.dropna(inplace=True)

cleanInterestRate = loansData['Interest.Rate'].map(lambda x: round(float(x.rstrip('%')) / 100, 4))
loansData['Interest.Rate'] = cleanInterestRate

cleanLoanLength = loansData['Loan.Length'].map(lambda y: int(y.rstrip(' months')))
loansData['Loan.Length'] = cleanLoanLength

cleanFico = loansData['FICO.Range'].map(lambda x: x.split('-'))
cleanFico = cleanFico.map(lambda z:[int(n) for n in z])
simpleFico = [score[0] for score in cleanFico]
loansData['FICO.Score'] = simpleFico

loansData['lessthan12'] = loansData['Interest.Rate'].map(lambda x: True if x <= 0.12 else False)
#print loansData['lessthan12'][1:10]
loansData['constant'] = [1 for i in simpleFico]

intrate = loansData['Interest.Rate']
loanamt = loansData['Amount.Requested']
fico = loansData['FICO.Score']
lessthan12 = loansData['lessthan12']
loanLength = loansData['Loan.Length']
constant = loansData['constant']

ind_vars = ['Amount.Requested','FICO.Score','constant']

logit = sm.Logit(loansData['lessthan12'], loansData[ind_vars])

result = logit.fit()

coeff = result.params

print coeff

e = 2.71828
intercept = 3.959676
FicoScore = 720
LoanAmount = 10000

p = 1/(1 + e**(intercept - 0.008673 * FicoScore + 0.000019 * LoanAmount))

print "IR-Probability: ", p 

intercept = -60.171952

def logistic_function(score,amount):
	p = 1/(1 + e**(intercept + 0.087423 * score - 0.000174 * amount))
	print "Lessthan12 prob: ", p
	return

logistic_function(800,10000)

#columns = ['score', 'amount']
#index = np.arange(5000) #
#df_t = pd.DataFrame(columns=columns, index = index)

#columns = ['score', 'amount']
#index = np.arange(5000) #
#df_f = pd.DataFrame(columns=columns, index = index)

df_t_score = []
df_t_amount = []

df_f_score = []
df_f_amount = []

for index, row in loansData.iterrows():
	if row['lessthan12'] == True:
		df_t_score.append(row['FICO.Score'])
		df_t_amount.append(row['Amount.Requested'])
	else:
		df_f_score.append(row['FICO.Score'])
		df_f_amount.append(row['Amount.Requested'])

fig = plt.figure(figsize = (10, 8))

plt.plot(df_t_score, df_t_amount, label = 'True',
mfc = 'None', mec='coral', alpha = .3)

plt.plot(df_f_score, df_f_amount, label = 'False',
mfc = 'None', mec='steelblue', alpha = .3)

plt.xlabel('Score')
plt.ylabel('Loan Amount')
plt.legend(loc='upper left')
plt.show()