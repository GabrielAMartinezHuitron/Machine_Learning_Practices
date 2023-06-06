#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jun  2 15:09:54 2023

@author: gabriel
"""

import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test, X,dataset,y = None, None, None, None, None, None, None

def loadData(name):
    global X_train, X_test, y_train, y_test, X, dataset, y
    dataset = pd.read_csv(name)
    X = dataset.iloc[:, :-1].values
    y = dataset.iloc[:, 1].values
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 1/3, random_state = 0)
    
def main():
    loadData("Salary_Data.csv")
    
main()
