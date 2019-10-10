import time,os,random
os.system('echo -e "\033[0;1m"; clear')
print(r''' _   _            _      _   _    _    ____    _
| | | | __ _  ___| | __ | \ | |  / \  / ___|  / \
| |_| |/ _` |/ __| |/ / |  \| | / _ \ \___ \ / _ \
|  _  | (_| | (__|   <  | |\  |/ ___ \ ___) / ___ \
|_| |_|\__,_|\___|_|\_\ |_| \_/_/   \_\____/_/   \_\
''')

for i in range(41):
    ger = '\x1b[7;m '*i
    sp = '.'*(40-i)
    print('\r|%s\x1b[0;m%s| %s%% hacking'%(ger, sp, round(i/40*100)), end='', flush=True)
    time.sleep(random.choice((1,0.1)))

print('\r|%s\x1b[0;m%s| %s%% hacked'%(ger, sp, round(i/40*100)), '\nCongratulation!')
