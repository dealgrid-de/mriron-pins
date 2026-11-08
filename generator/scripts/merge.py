import json,sys,os
out='/home/claude/pinterest/work/meta_part2.json'
d=json.load(open(out)) if os.path.exists(out) else {}
new=json.load(sys.stdin)
d.update(new)
json.dump(d,open(out,'w'),ensure_ascii=False,indent=1)
print(len(d))
