import numpy as np

# def format_data(fp):
#     df = pd.read_csv(fp, delim_whitespace=True, engine='python')
#     #dropping labels
#     df = df.drop(df.columns[0], axis=1)
#     #splitting data into index and queries
#     index_df = df.iloc[:10001,0:]
#     query_df = df.iloc[10001:10101,0:]
#     #writing to txt file
#     index_df.to_csv('index_vec.txt', sep='|', header=None, index=None)
#     query_df.to_csv('query_vec.txt', sep='|', header=None, index=None)
def DEFAULT_write(fname, m):
    with open(fname, 'wb') as f:
        np.array(m.shape[0], dtype=np.int32).tofile(f)
        np.array(m.shape[1], dtype=np.int32).tofile(f)
        m.tofile(f)
def DEFAULT_read(fname, np_type):
    buf = np.fromfile(fname, dtype='int32')
    n = buf[0]
    d = buf[1]
    print(buf.shape)
    print(n)
    print(d)
    #assert((n*d) % (buf.shape[0] - 2) == 0)
    return buf[2:].view(np_type).reshape(n, d).copy()

