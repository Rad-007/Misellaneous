

import datetime 
import schedule
import time
t=datetime.datetime.now().strftime("%a,%d,%B,%Y,%H,%M,%S").split(',')

print(t)


def bam():
    n=datetime.datetime.now().strftime("%a,%d,%B,%Y,%H,%M,%S").split(',')
    print('bam')
    print(n)


schedule.every(1).minutes.do(bam)

#schedule.every(30).day.at("10:30").do(job)

while True:
    schedule.run_pending()
    time.sleep(1)
    
    
        
    



