import pandas as pd
import numpy as np

print ("welcome home")

#myfile = pd.read_csv("http://localhost/Data/students.csv",index_col=0)

myfile = pd.read_csv("http://localhost/Data/students.csv",header=0,usecols=['ID','Last Name','First Name','City','State','Gender'],index_col=['City'])

#print(myfile.head())

#print(myfile.dtypes)

myfile.to_csv("student_sample.csv",index_label='City/Town')

df = pd.read_csv("student_sample.csv")

print(df.head())




