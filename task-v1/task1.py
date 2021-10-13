import xml.etree.ElementTree as ET
import urllib.request
import pandas as pd

def get_exchange_rate(source: str, target: str = "EUR") -> pd.DataFrame:
    url = "https://sdw-wsrest.ecb.europa.eu/service/data/EXR/M.{}.{}.SP00.A?detail=dataonly".format(source,target)
    print(url)
    file_name = url.split('/')[-1].split('?')[0]
    print(file_name)

    with urllib.request.urlopen(url) as response:
        temp_xml = response.read()

    # Parsing Xml file
    tree=ET.ElementTree(ET.fromstring(temp_xml))
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

get_exchange_rate("PLN")