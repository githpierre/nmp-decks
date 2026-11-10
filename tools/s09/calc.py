import pandas as pd
mk=pd.read_csv('/home/claude/nmp-product-pages/w/nmp_slide_kit/markets_225.csv')
mk['uuid']=pd.to_numeric(mk['uuid'],errors='coerce')
H=mk[(mk.uuid>=101)&(mk.uuid<=130)].sort_values('uuid').handle.tolist()
m=pd.read_csv('markets.csv',low_memory=False); r=pd.read_csv('rounds.csv',low_memory=False)
r=r[(r['is_equity'].astype(str).str.lower()=='true')&(r['aggregate'].astype(str).str.lower()!='true')].copy()
r['d']=pd.to_datetime(r['date'].astype(str).str.slice(0,10),errors='coerce',format='mixed')
