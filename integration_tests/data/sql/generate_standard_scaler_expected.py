from sklearn.preprocessing import StandardScaler
import pandas as pd
import numpy as np
test_dataset_df = pd.read_csv("data_standard_scaler.csv")
second_column = test_dataset_df.iloc[:, 1:2]
transformer = StandardScaler().fit(second_column)
test_dataset_df['col_to_scale_scaled']=transformer.transform(second_column)
print(test_dataset_df)
test_dataset_df.to_csv("data_standard_scaler_expected.csv",index=False)
