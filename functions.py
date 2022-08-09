import requests
from bs4 import BeautifulSoup

import os
import json 
import pandas as pd
import numpy as np 

import srtm
import zipfile
import shutil




# -----------------------------------------------------------------------------
def init():
    global dir_root, dir_data, dir_tmp, dir_report, dir_download
    dir_root = os.path.abspath(os.getcwd())
    create_structure()

def create_structure():
    globals()["dir_data"] = globals()["dir_root"]+'/data/'
    os.makedirs(globals()["dir_data"], exist_ok = True)

    globals()["dir_tmp"] = globals()["dir_root"]+'/tmp/'
    globals()["dir_download"] = globals()["dir_tmp"]+'/download/'
    os.makedirs(globals()["dir_download"], exist_ok = True)

    globals()["dir_report"] = globals()["dir_root"]+'/report/'
    os.makedirs(globals()["dir_report"], exist_ok = True)

# -----------------------------------------------------------------------------
def file_put_contents(filename, content,mode="w"):
    with open(filename, mode) as f_in: 
        f_in.write(content)

def file_get_contents(filename, mode="r"):
    with open(filename, mode) as f_in: 
        return f_in.read()      

# -----------------------------------------------------------------------------
def export_to_csv(data, file_path):
    ds = pd.DataFrame(data)
    ds.to_csv(file_path, index = False, header = None)

def download(url):
    file_name = os.path.basename(url)
    file_path = globals()["dir_download"]+file_name
    if not os.path.isfile(file_path) :
        r = requests.get(url)  
        file_put_contents(file_path, r.content, "wb")
    return file_path

# -----------------------------------------------------------------------------
elevation_data = srtm.get_data()


def unzip_to(file, dir):
    with zipfile.ZipFile(file, 'r') as zip_ref:
        zip_ref.extractall(dir)

# Check if is NaN
def is_nan(x):
    return (x != x)

def get_elevation(lat, lon):
    if is_nan(lat):
        return ''
    if is_nan(lon):
        return ''
    
    return elevation_data.get_elevation(lat,lon,approximate=True)




# https://www.usna.edu/Users/oceano/pguth/md_help/html/srtm.htm
# http://viewfinderpanoramas.org/Coverage%20map%20viewfinderpanoramas_org3.htm 
def installSRTM_data():
    HOME = os.path.expanduser('~')
    SRTM_HOME = HOME+"/.cache/srtm"

    for f in ['SG21','SG22',   'SH21','SH22',  'SI21','SI22',  'SJ21']:
        print("Downloading ",f)

        file_path = download("http://viewfinderpanoramas.org/dem3/"+f+".zip")
        unzip_to(file_path, SRTM_HOME)
    
        dir_f = SRTM_HOME+'/'+ f.replace('S','')
        for file in os.listdir(dir_f):
            shutil.move(dir_f+'/'+file, SRTM_HOME+'/'+file)
        os.removedirs(dir_f)


def addAltitud(file_path):
    installSRTM_data()

    df = pd.read_csv(file_path)
    df['alt'] = df.apply(lambda x: get_elevation(x['lat'], x['lon']), axis=1)
    estaciones_labels = df.columns
    estaciones = df.values
    
    return np.vstack((estaciones_labels.values, estaciones))






