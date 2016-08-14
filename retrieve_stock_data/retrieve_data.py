import requests
import datetime
import pandas as pd
import numpy as np

def retrieve_data(stock):
    url_prefix = "https://www.quandl.com/api/v3/datasets/WIKI"
    #api_key = "WHenP4n-2ZBkpxMoxCPN"
    
    today = datetime.date.today()
    start_date = today - datetime.timedelta(30)
    
    call_string = "%s/%s.json?start_date=%s&end_date=%s"%(url_prefix,stock,start_date,today)
    r = requests.get(call_string)

    df0 = pd.read_json(r.text)['dataset']
    df  = pd.DataFrame(df0['data'],columns=df0['column_names'])
    df['Date'] = pd.to_datetime(df['Date'])
    
    return df.loc[:,['Date','Close','Adj. Close','Open','Adj. Open']]
    
if __name__=="__main__":


    stock = "GOOG"
    df = retrieve_data(stock)
    import IPython
    IPython.embed()