import pandas as pd
import requests

url = 'https://github.com/BSData/wh40k/blob/master/Aeldari%20-%20Craftworlds.cat'

s=requests.get(url).content
