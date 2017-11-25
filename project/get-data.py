#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
i523 Big Data Application and Analytics

Created on Fri Nov 24 15:08:09 2017
@author: seanshiverick
"""
# get_data function retrieves datafiles from URL, unzips files, extracts data
# Reads `NSDUH-2015-DS0001-data-excel.tsv` file, converts to dataFrame object
# Print data frame shape, and exports dataframe to CSV file as 'nsduh15-dataset.csv'

import requests, zipfile, io
import pandas as pd

URL = 'http://samhda.s3-us-gov-west-1.amazonaws.com/s3fs-public/field-uploads-protected/studies/NSDUH-2015/NSDUH-2015-datasets/NSDUH-2015-DS0001/NSDUH-2015-DS0001-bundles-with-study-info/NSDUH-2015-DS0001-bndl-data-tsv.zip'

def get_data():

    r = requests.get('http://samhda.s3-us-gov-west-1.amazonaws.com/s3fs-public/field-uploads-protected/studies/NSDUH-2015/NSDUH-2015-datasets/NSDUH-2015-DS0001/NSDUH-2015-DS0001-bundles-with-study-info/NSDUH-2015-DS0001-bndl-data-tsv.zip')
    r.ok

    z = zipfile.ZipFile(io.BytesIO(r.content))
    z.extractall()

    file = pd.read_table('~/NSDUH-2015-DS0001-bndl-data-tsv/NSDUH-2015-DS0001-data/NSDUH-2015-DS0001-data-excel.tsv', low_memory=False)
    data = pd.DataFrame(file)

    print(data.shape)
    data.to_csv('nsduh15-dataset.csv', sep=',', encoding='utf-8')
    
get_data()