import json
p='allotment_data.json'
with open(p,encoding='utf-8') as f:
    data=json.load(f)
print('Total records:',len(data))
# find by application id
app='DSE26104051'
found=[r for r in data if str(r.get('application_id','')).upper().replace('DSE','DSE').upper().endswith(app.replace('DSE','')) or str(r.get('application_id','')).upper()==app.upper()]
print('By app id:', len(found))
if found:
    r=found[0]
    print('College:', r.get('college_name'))
    print('Branch:', r.get('branch_name'))
    print('Candidate:', r.get('name'))
    print('Round:', r.get('round'))
    print('Merit No:', r.get('merit_no'))
    print('Merit Score:', r.get('merit_score'))
# find by name
name='SWAPNALI BALAJI DAREKAR'
found2=[r for r in data if name in (str(r.get('name','')).upper())]
print('By name exact upper:', len(found2))
# fuzzy name search: all words
words=name.split()
found3=[r for r in data if all(w in str(r.get('name','')).upper() for w in words)]
print('By name words:', len(found3))
