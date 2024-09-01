import pandas as pd

a = [9,5,4,11,7,3,3,9]
result = pd.Series(a)
#print(result)
myLabel = pd.Series(a, 
index = ["ORANGE","TOMATO","WATERMELON","APPLE","PEANUT","BURRY","LYNCHEE","COCONUT"])
print(myLabel)