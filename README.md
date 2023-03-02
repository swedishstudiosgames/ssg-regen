# License Plate Generator
```
import os,itertools,string,time
os.system("title License Plate Generator")
print("Please wait...",end=" ",flush=True)
time.sleep(1)
print("While i'm generating this file for you.")
time.sleep(2)
prefixs=[''.join(x)for x in itertools.product(string.ascii_uppercase+string.digits,repeat=3)]
suffixs=[''.join(x)for x in itertools.product(string.ascii_uppercase+string.digits,repeat=3)]
with open('list.txt','w')as f:
    cache=[]
    for prefix in prefixs:
        for suffix in suffixs:
            combo=f"{prefix} {suffix}"
            cache.append(combo)
            if len(cache)==1000:
                f.write('\n'.join(cache)+'\n')
                cache.clear()
    if cache:
        f.write('\n'.join(cache)+'\n')
print("Done! The file 'list.txt' has been generated.")
time.sleep(2)
print("Thank you for your patience, And goodbye! :)")
time.sleep(2)
```
##### Output
```
Please wait... While i'm generating this file for you.
Done! The file 'list.txt' has been generated.
Thank you for your patience, And goodbye! :)
```
---
It took me about 15 minutes and 30 seconds to generate a 18.2GB (19,591,041,024 bytes) file.<br>
### Specs
```
Device name:    DESKTOP-VMWARE
Processor:      Intel(R) Core(TM) i5-7300HQ CPU @ 2.50GHz  2.50GHz
Installed RAM:  8.00 GB (7.89 GB usable)
Device ID:      
Product ID:     
System type:    64-bit operating system, x64-based processor
Pen and touch:  No pen or touch input is available for this display

Edition:        Windows 10 Home
Version:        22H2
Installed on:	  
OS build:       
Experience:     Windows Feature Experience Pack
```
