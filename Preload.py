import sys
import subprocess
import re
import os

p = subprocess.Popen(['find', 'data/raw', '-name', '[0-9]*.html'], stdout=subprocess.PIPE)
stdout,stderr = p.communicate()
letters =  stdout.split('\n')

def findSubString(raw_string, start_marker, end_marker):
  return re.sub(
      r'(?<={}).*?(?={})'.format(re.escape(start_marker),
        re.escape(end_marker)),
      lambda m: m.group().strip().replace(' ', '_'),
      raw_string)

for l in letters:
  with open(l,'r') as f:
    cnt = f.read()
    try:
      r = re.search(
            '.*' +
            re.escape('<!--beginarticle-->') +
            '(.*)' +
            re.escape('<!--endarticle-->') +
            '.*',
            cnt, re.DOTALL)

      text = r.group(1)

      text_notags = re.sub(re.compile('<.*?>'), '', text)

      print ("letter %s headline %s" % (l,text_notags[:15]))

      with open('data/clean1/' + os.path.basename(l) ,'w') as fw:
        fw.write(text_notags)

    except:
      e = sys.exc_info()[0]
      print "Exception occured: %s" % e

