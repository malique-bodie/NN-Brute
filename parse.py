import pandas as pd

def format_data(fp):
    df = pd.read_csv(fp, delim_whitespace=True, engine='python')
    #dropping labels
    df = df.drop(df.columns[0], axis=1)
    #splitting data into index and queries
    index_df = df.iloc[:10001,0:]
    query_df = df.iloc[10001:10101,0:]
    #writing to txt file
    index_df.to_csv('index_vec.txt', sep='|', header=None, index=None)
    query_df.to_csv('query_vec.txt', sep='|', header=None, index=None)

format_data('./glove.6B.50d.txt')


