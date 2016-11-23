import sys
import subprocess
import re
import os
import sqlite3

def findLetters():
  p = subprocess.Popen(['find', 'data/raw', '-name', '[0-9]*.html'], stdout=subprocess.PIPE)
  stdout,stderr = p.communicate()
  letters =  filter(None,stdout.split('\n'))
  return letters

def insertLetters(letters):

  def findSubString(raw_string, start_marker, end_marker):
    return re.sub(
        r'(?<={}).*?(?={})'.format(re.escape(start_marker),
          re.escape(end_marker)),
        lambda m: m.group().strip().replace(' ', '_'),
        raw_string)

  conn = sqlite3.connect('Jobwatch.db')

  c = conn.cursor()

  c.execute('DELETE FROM letters');

  let_id = 0

  for l in letters:

    try:
      let_id = let_id + 1

      with open(l,'r') as f:
        cnt = f.read()
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

        c.execute('insert into letters(Id,Nam,Text) values(%d, "%s", "%s")' %
                    (let_id, os.path.basename(l), text_notags))

    except:
      e = sys.exc_info()[0]
      print "Exception occured on file %s: %s:" % (l,e)
      raise

  conn.commit()


l = findLetters()

insertLetters(l)
