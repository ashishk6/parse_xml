import xml.etree.ElementTree as ET
import urllib.request
import pandas as pd

def get_exchange_rate(source: str, target: str = "EUR") -> pd.DataFrame:
    url = "https://sdw-wsrest.ecb.europa.eu/service/data/EXR/M.{}.{}.SP00.A?detail=dataonly".format(source,target)

    file_name = url.split('/')[-1].split('?')[0]
    print(file_name)

    with urllib.request.urlopen(url) as response:
        html = response.read()

 
    tree=ET.ElementTree(ET.fromstring(html))
    root=tree.getroot()

    df = pd.DataFrame({'TIME_PERIOD': [], 'OBS_VALUE': []})    
    for i in range(2,270):
        df = df.append({'TIME_PERIOD': root[1][0][i][0].attrib['value'], 'OBS_VALUE': float(root[1][0][i][1].attrib['value'])}, ignore_index=True)

    #print(df)
    return df

get_exchange_rate("GBP")