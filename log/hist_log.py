import matplotlib.pyplot as plt #Visulization
import seaborn as sns #Visulization
%matplotlib inline

plt.hist(train['quality'], bins=12)
plt.title("quality_Histgram")
plt.xlabel('quality')
plt.ylabel('count')
plt.show()
