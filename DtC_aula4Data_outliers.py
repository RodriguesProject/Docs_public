import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

dt = pd.read_csv("titanic.csv")

sns.boxplot(x=dt["age"])
plt.show()
#portanto temos outliers, ou seja, valores que estão muito distantes da média.. No gráfico ficou evidenciado que os dados acima de 65 anos são outliers, ou seja, estão muito distantes da média. Esses valores podem influenciar negativamente a análise dos dados, por isso é importante identificá-los e tratá-los adequadamente.
