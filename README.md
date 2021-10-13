# Parse Xml into dataframe

### Task1:
```
def get_exchange_rate(source: str, target: str = "EUR") -> pd.DataFrame
```
This will get_exchange_rate from the link and parse it to DataFrame 


### Task2:
```
def get_raw_data(identifier: str) -> pd.DataFrame
```
This will get_raw_data from the link and parse it to DataFrame 


### Task3:
```
def get_data(identifier: str, target_currency: str = None) ->pd.DataFrame:
```
This will get_raw_data from the link and parse it to DataFrame if no target_currency will be given to it.
Else this will provide get_exchange_rate if we give target_currency

```
For example:
get_data('M.N.I8.W1.S1.S1.T.N.FA.F.F7.T.EUR._T.T.N') will return get_raw_data as DataFrame
get_data('M.N.I8.W1.S1.S1.T.N.FA.F.F7.T.EUR._T.T.N','GBP') will return get_exchange_rate as DataFrame
```

#### prereqsite libraries:
```
xml.etree.ElementTree
urllib
pandas 
```

### Step to execute:
```
import task3 as t3
t3.get_data('M.N.I8.W1.S1.S1.T.N.FA.F.F7.T.EUR._T.T.N') 
t3.get_data('M.N.I8.W1.S1.S1.T.N.FA.F.F7.T.EUR._T.T.N','GBP')
```
           
