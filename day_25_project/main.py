import pandas as pd
df = pd.read_csv("2018_Central_Park_Squirrel_Census_-_Squirrel_Data_20250704.csv")
gray_far = len(df[df["Primary Fur Color"]=="Gray"])
red_far = len(df[df["Primary Fur Color"]=="Cinnamon"])
black_far = len(df[df["Primary Fur Color"]=="Black"])

squirrel_dict  = {
    "Fur Color" : ["Gray","Cinnamon","Black"],
    "Count" : [gray_far,red_far,black_far]
}
df = pd.DataFrame(squirrel_dict)
df.to_csv("squirrel far.csv")



