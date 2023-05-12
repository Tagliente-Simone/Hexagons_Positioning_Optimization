import pandas as pd

df = pd.read_csv("composizione_fasci.csv")

df['compo_fascio'] = df['compo_fascio'].str.replace('4/3/2003', '3-4-3')

df = df.drop(df[df['lunghezza'] > 700].index)




df = df.drop(df[df['compo_fascio'] == "(11-10)x2" ].index)
df = df.dropna(subset=['compo_fascio'])
df = df.drop(df[df['compo_fascio'] == "(17-16)x2" ].index)
df = df.drop(df[df['compo_fascio'] == "(16-15)x2" ].index)
df = df.drop(df[df['compo_fascio'] == "(13-12)x2" ].index)
df = df.drop(df[df['compo_fascio'] == "(12-11)x2" ].index)
df = df.drop(df[df['compo_fascio'] == "(15-14)x2" ].index)
df = df.drop(df[df['compo_fascio'] == "(14-13)x2" ].index)
df = df.drop(df[df['compo_fascio'] == "3-4-5-4" ].index)


print(df['compo_fascio'].unique())


df.to_csv("composizione_fasci_cleaned.csv", index=False)