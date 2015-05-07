import matplotlib.pyplot as plt
import pandas as pd
import scipy.stats as stats

loansData = pd.read_csv('loansData.csv')
loansData.hist(column='Amount.Requested', bins=5)
plt.savefig("ARhisto.png")


#loansData.dropna(inplace=True)
loansData.boxplot(column='Amount.Requested')
plt.savefig("ARboxplot.png")

#loansData.hist(column='Amount.Requested')
#plt.savefig("ARhisto.png")

plt.figure()
graph = stats.probplot(loansData['Amount.Requested'], dist="norm", plot=plt)
plt.savefig("ARprob.png")
