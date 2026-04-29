import pandas as pd 

# serie = pd.Series([1,4,9], index=["x","y","z"])

# print(serie)

data ={
    "nombre": ["juan", "maria", "pedro"],
    "edad": [25, 30, 35],
}

df = pd.DataFrame(data)
print(df)