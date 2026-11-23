import sys, os, csv, shutil, datetime as dt, collections
HERE=os.path.dirname(os.path.abspath(__file__)); sys.path.insert(0, HERE)
import ig_pins
REPO="/home/claude/mriron-pins"; R="https://raw.githubusercontent.com/dealgrid-de/mriron-pins/main/pins/"
P=f"{REPO}/csv/QUEUE_GESAMT.csv"
rows=list(csv.reader(open(P,encoding="utf-8"))); h,rows=rows[0],rows[1:]
seen=set(r[0] for r in rows)
pool=list(ig_pins.X)
for x in pool:
    t=x['title']; k=2
    while x['title'] in seen: x['title']=t[:88]+f" ({k})"; k+=1
    seen.add(x['title'])
SLOTS=['05:30','07:00','07:30','09:15','10:00','11:45','13:15','14:30','18:45','20:30']
last=collections.defaultdict(list)
for r in rows: last[r[5]].append(dt.date.fromisoformat(r[6][:10]))
taken=set(r[6][:16] for r in rows); perday=collections.Counter(r[6][:10] for r in rows)
ok=lambda l,d: all(abs((d-x).days)>=10 for x in last[l])
day=dt.date(2026,12,22); nr=701; new=[]
while pool and day<dt.date(2027,3,1):
    for s in SLOTS:
        if perday[day.isoformat()]>=10 or not pool: break
        t=f"{day.isoformat()}T{s}"
        if t in taken: continue
        for i,x in enumerate(pool):
            if ok(x['link'],day):
                x=pool.pop(i); last[x['link']].append(day); taken.add(t); perday[day.isoformat()]+=1
                fn=f"{nr}_{x['tag']}_I.jpg"; shutil.copy(f"{HERE}/igp/{x['tag']}.jpg",f"{REPO}/pins/{fn}")
                new.append([x['title'],R+fn,x['board'],"",x['desc'],x['link'],t+":00",x['kw']]); nr+=1; break
    day+=dt.timedelta(days=1)
rows=sorted(rows+new,key=lambda r:r[6])
w=csv.writer(open(P,'w',encoding='utf-8',newline='')); w.writerow(h); w.writerows(rows)
print(len(new),"Rest",len(pool), sorted(collections.Counter(r[6][:10] for r in new).items()))
