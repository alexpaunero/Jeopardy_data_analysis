import pandas as pd

#Task 2
pd.set_option('display.max_colwidth', -1)

df = pd.read_csv('jeopardy.csv')
print(df.head())

#Task 3
find_values = ["King", "England"]

def filterdf(dftofilter, valuestofind):
  filter = lambda x: all(word in x for word in valuestofind)
  return dftofilter.loc[dftofilter[" Question"].apply(filter)]

filtered = filterdf(df, find_values)
print(filtered[" Question"])

#Task 5
df[" Value"] = df[" Value"].str.replace('None', '$0')
df[" Value"] = df[" Value"].str[1:]
df[" Value"] = df[" Value"].str.replace(',', '').astype(float)

#Task 6
def get_answer_counts(data):
    return data[" Answer"].value_counts()
print(get_answer_counts(filtered))
