import json
p='allotment_data.json'
with open(p,encoding='utf-8') as f:
    data=json.load(f)
print('Total records:',len(data))
# search by name words
name='SWAPNALI BALAJI DAREKAR'
found=[r for r in data if name in (str(r.get('name','')).upper())]
print('By exact full upper:', len(found))
found2=[r for r in data if all(w in str(r.get('name','')).upper() for w in name.split())]
print('By all words:', len(found2))
# search by app id
app='DSE26104051'
found3=[r for r in data if str(r.get('application_id','')).upper().replace('DSE','DSE').upper().endswith(app.replace('DSE','')) or str(r.get('application_id','')).upper()==app.upper()]
print('By app id:', len(found3))
if found2:
    r=found2[0]
    print('College:', r.get('college_name'))
    print('Branch:', r.get('branch_name'))
    print('Candidate:', r.get('name'))
    print('Merit No:', r.get('merit_no'))
    print('Merit Score:', r.get('merit_score'))
    print('Application ID:', r.get('application_id'))
else:
    print('No exact word-match record found')
