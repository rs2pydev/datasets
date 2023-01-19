#!/usr/bin/env python
# coding: utf-8

#######################################################
# Code used for creating these smaller CSV files.
#######################################################

#######################################################
## Import required libraries. 
#######################################################
import os 
import pandas as pd 

#######################################################
## 1. Split a large CSV file into smaller fragments. 
#######################################################
pwd = os.getcwd()
file_name = "okcupid_profiles.csv"
file_path = os.path.join(pwd, file_name)
print(file_path) 
print('\n')

total_df = pd.read_csv(file_path)
print(total_df.shape) 
print()
print(total_df.head())
print()
print(total_df.tail())
print('\n')

def create_small_dataframes(df, file_name, n_rows):
    base_name = file_name.split(".")[0]
    base_extn = file_name.split(".")[1]
    pwd = os.getcwd()
    files = []
    for counter in range(10):
        start = n_rows * counter
        end =  n_rows * (counter + 1)
        sub_df = df.iloc[start:end, 0:]
        fname = base_name + '_' + str(f'set{counter+1:d}') + str('.') + base_extn
        fpath = os.path.join(pwd, fname)
        files.append(fname)
        sub_df.to_csv(fname, index=False)
    return files

files = create_small_dataframes(total_df, "okcupid_profiles.csv", 6000)
print(type(files))
print()
print(files)
print('\n')

#######################################################
## 2. Merge smaller CSV files to create a large CSV file.
#######################################################
def create_large_dataframe(fnames, concat_axis=0):
    pwd = os.getcwd()
    large_df = pd.DataFrame()
    for fname in fnames:
        file_path = os.path.join(pwd, fname) 
        sub_df = pd.read_csv(file_path)
        large_df = pd.concat([large_df, sub_df], axis=concat_axis, ignore_index=True)
    return large_df

big_df = create_large_dataframe(files)
print(big_df.head())
print()
print(big_df.tail())
print()
print(final_df.shape)
print('\n')