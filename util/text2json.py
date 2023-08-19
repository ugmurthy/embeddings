import os
import re
from datetime import datetime, timedelta
from tqdm.notebook import tqdm
from time import sleep


## Helper function converts dd/mm/yy hh:mm:ss AM|PM string to UTC 
def convert_to_utc(timestamp_string):
    pattern = r"\[(\d{1,2}/\d{1,2}/\d{2}, \d{1,2}:\d{2}:\d{2} [APap][Mm])\]"
    match = re.search(pattern, timestamp_string)
    
    if match:
        timestamp = match.group(1)
        dt_format = "%d/%m/%y, %I:%M:%S %p"
        dt_object = datetime.strptime(timestamp, dt_format)

        # Check if it's PM and adjust the hour
        if "PM" in timestamp.upper():
            dt_object += timedelta(hours=12)
        
        utc_dt = dt_object - timedelta(hours=dt_object.hour)
        return utc_dt
    else:
        return None
        
## Helper to assemble news item or bunched news items from an agency for a particular day      
def make_news(ldt,id,itms,agency,**kwargs):
    ITEMWISE = kwargs.get("itemwise",False)
    _news = []
    if ITEMWISE:
        for i,itm in enumerate(itms):
            _tmp = {"ids":[id+str(i+1)],"documents":[itm],"metadatas":{"source":agency,"date":ldt}}
            #print(_tmp)
            _news.append(_tmp)
    else:
        _tmp = {"ids":[id],"documents":",".join(itms),"metadatas":{"source":agency,"date":ldt}}
        _news.append(_tmp)
        #print(_tmp)
    return _news

# Returns an array of json containing news in a structure suitable add to a vector database (chroma in this case)

def get_news(fname,**kwargs):
    ## Some constants for news pre processing
    ITEMWISE=kwargs.get("itemwise",False)
    DATE = "["
    DATE_FILTER ="Raghu"
    NEWS_AGENCY = "*"
    NEWS_ITEM = "📝"
    NEW_LINE = "\n"
    SHOW = False
    
    news=[]
    rejects=0
    _items=[]
    try:
        with open(fname,"r") as file:
            for line in file:
                if line[0] in [DATE, NEWS_AGENCY, NEWS_ITEM]:
                    match line[0]:
                        case "[":
                            if "Raghu" in line:
                                if len(_items)!=0:
                                    news.append(make_news(last_date,_id,_items,news_agency,itemwise=ITEMWISE))
                                    _items=[]
                                   
                                last_date = str(convert_to_utc(line.strip()))[0:10]
                                #print("Date",last_date)
                        case "*":
                            if len(_items)!=0:
                                news.append(make_news(last_date,_id,_items,news_agency,itemwise=ITEMWISE))
                                _items=[]       
                            news_agency = line[1:-2]
                            acronym="".join(list(map(lambda a: a[0],news_agency.split())))
                            _id = last_date+acronym
    
                        case "📝":
                            _items.append(line[1:].strip())
                else:
                    rejects +=1
            news.append(make_news(last_date,_id,_items,news_agency,itemwise=ITEMWISE))
                    
    except FileNotFoundError:
        print(f"File '{fname}' not found.")
    except Exception as e:
        print(f"An error occurred: {e}")
    
    print(f"Rejected lines : {rejects}")
    print(f"News Items : {len(news)}")
    news = [item for sublist in news for item in sublist]
    return news

