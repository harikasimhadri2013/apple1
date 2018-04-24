#!/usr/bin/python
import os
import datetime
import shutil

def main(path):
  print path
  count = 0
  past_date=(datetime.date.today() - datetime.timedelta(30))
  print past_date
  contents=os.listdir(path)
  for item in contents:
    #if item.startswith('build-') or (item.startswith('turn-') and item.endswith('.tar.gz')):
    total_path=path+"/"+item
    ctime = os.path.getctime(total_path)
    temp=str(datetime.datetime.fromtimestamp(ctime)).split(' ')[0]
    created_date=(datetime.datetime.strptime(temp,'%Y-%m-%d')).date()
    if created_date <= past_date:
      if os.path.isfile(total_path):
        os.remove(total_path)
        count+=1
      else:
        shutil.rmtree(total_path)
        count+=1
  print str(count)+" items are removed from "+path
paths = ['/tmp']
for path in paths:
  if os.path.exists(path):
    main(path)
  else:
    print path+" is not found."
	
