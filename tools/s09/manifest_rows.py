import json,csv
CDN='https://cdn.shopify.com/s/files/1/0871/5413/1219/files/'
rows=[]
u1=json.load(open('upload.json'))
v208={'in-vivo-car-t','digital-banking','fraud-prevention','carbon-removal'}
for r in u1:
    rows.append((r['handle'],r['filename'],CDN+r['filename']+'?v='+('1794334208' if r['handle'] in v208 else '1794334209'),r['gid'],r['alt']))
u2=json.load(open('upload2.json'))
v176=set('off-grid-solar agricultural-biologicals physical-security buy-now-pay-later mortgage-technology pos-software carbon-credit quantum-sensing optical-interconnect ai-medical-scribe advanced-geothermal autonomous-trucking post-quantum-cryptography virtual-power-plant earned-wage-access sodium-ion-battery ai-agent-observability ai-tutoring'.split())
for i,r in enumerate(u2):
    if i<48: gid=47829804613907+32768*i; v='1794336110'
    else: gid=47829807792403+32768*(i-48); v='1794336176' if r['handle'] in v176 else '1794336175'
    rows.append((r['handle'],r['filename'],CDN+r['filename']+'?v='+v,'gid://shopify/MediaImage/%d'%gid,r['alt']))
# spot checks against query output
chk={'battery-recycling':47829806154003,'ev-charging-infrastructure':47829807792403,'psychedelic-therapeutics':47829808480531,'ai-companion':47829809299731,'quantum-sensing':47829808546067,'carbon-credit':47829808414995}
for h,g,*_ in [(r[0],r[3]) for r in rows]:
    if h in chk: print(h, g.endswith(str(chk[h])))
json.dump(rows,open('manifest_rows.json','w'))
print(len(rows))
