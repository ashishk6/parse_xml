import xml.etree.ElementTree as ET
import urllib.request
import pandas as pd


def get_raw_data(identifier: str) -> pd.DataFrame:
    url="https://sdw-wsrest.ecb.europa.eu/service/data/BP6/{}?detail=dataonly".format(identifier)

    file_name = url.split('/')[-1].split('?')[0]
    print(file_name)

    with urllib.request.urlopen(url) as response:
        html = response.read()

    tree=ET.ElementTree(ET.fromstring(html))
    root=tree.getroot()
 
    # Initializing DataFrame
    df = pd.DataFrame({'TIME_PERIOD': [], 'OBS_VALUE': []})   

    # Parsing the dataset
    obsDimension=root.iterfind(".//{http://www.sdmx.org/resources/sdmxml/schemas/v2_1/data/generic}ObsDimension")
    obsValue=root.iterfind(".//{http://www.sdmx.org/resources/sdmxml/schemas/v2_1/data/generic}ObsValue")

    for x,y in zip(obsDimension,obsValue):
        df = df.append({'TIME_PERIOD': x.attrib['value'], 'OBS_VALUE': float(y.attrib['value'])}, ignore_index=True)
    
    #print(df)
    return df

get_raw_data('M.N.I8.W1.S1.S1.T.N.FA.F.F7.T.EUR._T.T.N')