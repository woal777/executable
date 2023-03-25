#!/home/jinho93/bin/python3
import os

buf = os.popen('qstat -u "*"')
out: str = buf.read()
arr = [r.split()[7:9] for r in out.split('\n')][2:-1]
a = {'8180.q':56, '8170.q':52, '6142.q':64,'7501.q': 64, '2695.q': 56,
        '8870.q': 72,'6248.q':48, 'all.q':12}
arr = [r for r in arr if len(r) >1]

for i, j in arr:
    a[i.split('@')[0]] -= int(j)

print(a)

