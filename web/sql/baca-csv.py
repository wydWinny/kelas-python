import pandas as pd
import matplotlib.pyplot as plt 
import os

directory = 'data'

dataframes = []

for filename in os.listdir(directory):
    if filename.endswith('.csv'):
        filepath = os.path.join(directory, filename)
        try:
            df = pd.read_csv(filepath)
            print('before: ', df)
            df['store'] = filename.replace('.csv', '')
            print('after: \n', df)
            dataframes.append(df)
        except Exception as e:
            print(f"Error reading {filename} : {e}")

for d in dataframes:
    print(d)

if len(dataframes) > 0:
    combined_df = pd.concat(dataframes, ignore_index = True)
    for store, store_data in combined_df.groupby('store'):
        store_data = store_data.sort_values(by = ['tanggal'], ascending = True )
        print(store_data)

        plt.figure(figsize=(12,6))
        plt.title('Borma Sales')
        plt.xlabel('tanggal')
        plt.ylabel('sales')
        plt.bar(store_data['tanggal'], store_data['sales'], color = 'violet')
        plt.savefig(f'{store}.png')
        print(combined_df)

    # combined_df = combined_df.sort_values(by = 'sales')
    # print(combined_df)

    # print("All files combined into a single dataframe")
    # plt.figure(figsize=(12,6))
    # plt.bar(combined_df['tanggal'], combined_df['tanggal'], color='violet')
    # plt.savefig('./result.png')
   

