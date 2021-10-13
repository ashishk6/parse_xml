import pandas as pd
import task2 as t2
import task1 as t1

def get_data(identifier: str, target_currency: str = None) ->pd.DataFrame:
    
    result=None
    if target_currency is None:
        result=t2.get_raw_data(identifier)
    else:
        result=t1.get_exchange_rate(target_currency)
    
    return result

print(get_data('M.N.I8.W1.S1.S1.T.N.FA.F.F7.T.EUR._T.T.N'))
print(get_data('M.N.I8.W1.S1.S1.T.N.FA.F.F7.T.EUR._T.T.N','GBP'))
print(get_data('M.N.I8.W1.S1.S1.T.N.FA.F.F7.T.EUR._T.T.N','PLN'))