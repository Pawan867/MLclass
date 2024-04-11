import numpy as np
# import seaborn as sns
# Create Custom Dataset

dataset = [11, 10, 12, 14, 12, 15, 14, 13, 15, 102, 12, 14, 17, 19, 107, 10,
           13, 12, 14, 12, 108, 12, 11, 14, 13, 15, 10, 15, 12, 10, 14, 13, 15, 10]
print(dataset)

sns.histplot(dataset, bins=30, kde=True, alpha=0.6, color='blue')
