import pandas as pd
import numpy as np    // importing library's for data operations
df1=pd.read_csv(r"C:\Users\ramgo\OneDrive\Desktop\Book1.csv")
x=df1.iloc[:].values //inserting all rows data into x
print(x)

>>
array([['ram', 1.0, 2.0, nan, 'yes'],                          // before imputer operation
       ['ads', 5.0, nan, 1.0, 'no'],
       ['eee', nan, nan, nan, 'no'],
       ['abc', 58.7, 9.0, 1.0, 'no'],
       ['ttt', nan, nan, nan, 'yes'],
       ['uuu', nan, nan, nan, 'not given'],
       ['df', nan, nan, nan, 'not given'],
       ['dfv', nan, nan, nan, 'yes']], dtype=object)


from sklearn.impute import SimpleImputer
imputer= SimpleImputer(missing_values=np.nan,strategy='mean')     // strategy can be changed to median also 
imputer =imputer.fit(x[:,1:4])
x[:,1:4]=imputer.transform(x[:,1:4])
print(x)

array([['ram', 1.0, 2.0, 1.0, 'yes'],
       ['ads', 5.0, 5.5, 1.0, 'no'],                              // after imputer operation(mean) all the nan values will be converted into mean whith respect there column
       ['eee', 21.566666666666666, 5.5, 1.0, 'no'],
       ['abc', 58.7, 9.0, 1.0, 'no'],
       ['ttt', 21.566666666666666, 5.5, 1.0, 'yes'],
       ['uuu', 21.566666666666666, 5.5, 1.0, 'not given'],
       ['df', 21.566666666666666, 5.5, 1.0, 'not given'],
       ['dfv', 21.566666666666666, 5.5, 1.0, 'yes']], dtype=object)
