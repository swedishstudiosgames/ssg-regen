import os,itertools,string,time
os.system("title License Plate Generator")
print("Please wait... While i'm generating this file for you.")
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