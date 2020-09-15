import pandas as pd

def readvanilla():
    filepath ='data/iris.data'
    with open(filepath,'r') as fp:
        data = fp.read()

    data_lines = data.split('\n')

    data_final = [f.split(',') for f in data_lines]

    return data_final

def read_pandas(filepath,**kwargs):
    df = pd.read_csv(filepath,**kwargs)
    return df

if __name__ == '__main__':
    df = read_pandas("data/iris.data",names=["sepal_length","sepal_width","petal_length","petal_width","class"])
    print(df["sepal_length"])
