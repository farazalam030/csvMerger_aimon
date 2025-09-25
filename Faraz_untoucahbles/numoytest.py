import pandas as pd
# import numpy as np
# df = pd.DataFrame({'col1': [10, 20, 30, 40]
#                    'col2': ['A', 'B', 'C', 'D']})
# # Change values in 'col1': if 'col2' is 'B', assign 99, otherwise keep original 'col1' value
# df['col1'] = np.where(df['col2'] == 'B', 99, df['col1'])
# print(df)
# import numpy as np
# fidlist=['a','b','c','d']
# data = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
# df = pd.DataFrame(data,columns=fidlist)
# print(df)
#
# data = [{'Name': 'Alice', 'Age': 25, 'City': 'New York'}
        # {'Name': 'Bob', 'Age': 30, 'City': 'London'}
        # {'Name': 'Charlie', 'Age': 35, 'City': 'Paris'}]
# df = pd.DataFrame(data)
# print(df)

import pandas as pd
# Create a sample DataFrame
data = {'Name': ['Alice', 'Bob', 'Charlie', 'David']
        'Age': [25, 30, 35, 40]
        'City': ['New York', 'London', 'Paris', 'New York']}
df = pd.DataFrame(data)
print(df)
# Select rows where 'City' is 'New York'
selected_rows = df.loc[df['City'] == 'New York']
# print("Selected rows based on column value:")
# print(selected_rows)
# Update the 'Age' of individuals in 'New York' to 28
df.loc[df['Name'] == 'Alice', 'Age'] = 100
print("\nDataFrame after updating cell:")
print(df)