import sys, os, csv, shutil, glob, datetime as dt, collections
HERE=os.path.dirname(os.path.abspath(__file__)); sys.path.insert(0, HERE)
import arts, mats
REPO="/home/claude/mriron-pins"; R="https://raw.githubusercontent.com/dealgrid-de/mriron-pins/main/pins/"
P=f"{REPO}/csv/QUEUE_GESAMT.csv"
rows=list(csv.reader(open(P,encoding="utf-8"))); h,rows=rows[0],rows[1:]
seen=set(r[0] for r in rows)
# Pool
A=[dict(kind="art",img=f"{HERE}/art/{a['slug']}.jpg",tag=a['slug'],title=a['title'],board="Unterrichtsideen & Tipps für Lehrkräfte",desc=a['desc'],link=a['url'],kw=a['kw']) for a in arts.A]
M=[]
for i,j in enumerate(mats.jobs()):
    m=j['m']
    if m['id']=='2347304': continue
    img=glob.glob(f"{HERE}/matp/{i:03d}_{j['kind']}_{m['id']}.jpg")[0]
    board="Kostenlose Arbeitsblätter" if j['kind']=="freebie" else ("Deutsch Klasse 5 und 6" if j['kind']=="togo" else mats.B.board_for(m,'A'))
    kw=", ".join(mats.T.keywords(m)) if isinstance(mats.T.keywords(m),list) else mats.T.keywords(m)
    M.append(dict(kind=j['kind'],img=img,tag=m['id'],title=mats.seo_title(m,j['kind']),board=board,desc=mats.desc(m,j['kind']),link=m['url'],kw=kw))
# unique titles
for x in A+M:
    t=x['title']; k=2
    while x['title'] in seen: x['title']=(t[:92]+f" ({k})"); k+=1
    seen.add(x['title'])
# interleave kinds
Q={k:[x for x in A+M if x['kind']==k] for k in ["art","foto","freebie","togo"]}
pat=["art","foto","art","freebie","foto","art","foto","togo","art","freebie"]
pool=[]
while any(Q.values()):
    for k in pat:
        if Q[k]: pool.append(Q[k].pop(0))
SLOTS=['05:30','07:00','07:30','09:15','10:00','11:45','13:15','14:30','18:45','20:30']
last=collections.defaultdict(list)
for r in rows: last[r[5]].append(dt.date.fromisoformat(r[6][:10]))
taken=set(r[6][:16] for r in rows); perday=collections.Counter(r[6][:10] for r in rows)
def ok(link,d): return all(abs((d-x).days)>=10 for x in last[link])
day=dt.date(2026,12,21); nr=521; new=[]
while pool and day<dt.date(2027,3,1):
    for s in SLOTS:
        if perday[day.isoformat()]>=10 or not pool: break
        t=f"{day.isoformat()}T{s}"
        if t in taken: continue
        for i,x in enumerate(pool):
            if ok(x['link'],day):
                x=pool.pop(i); last[x['link']].append(day); taken.add(t); perday[day.isoformat()]+=1
                fn=f"{nr}_{x['tag']}_{ {'art':'A','foto':'F','freebie':'G','togo':'T'}[x['kind']] }.jpg".replace(" ","")
                shutil.copy(x['img'],f"{REPO}/pins/{fn}")
                assert len(x['title'])<=100
                new.append([x['title'],R+fn,x['board'],"",x['desc'],x['link'],t+":00",x['kw']]); nr+=1; break
    day+=dt.timedelta(days=1)
rows=sorted(rows+new,key=lambda r:r[6])
w=csv.writer(open(P,'w',encoding='utf-8',newline='')); w.writerow(h); w.writerows(rows)
print(len(new),"eingeplant; Rest im Pool:",len(pool),"; von",new[0][6],"bis",max(r[6] for r in new))
print(collections.Counter(x[6][:10] for x in new).most_common(3))
