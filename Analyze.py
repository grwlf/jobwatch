import sqlite3

import DB



def wordDict():

  conn = sqlite3.connect(DB.name)
  c = conn.cursor()
  c.execute('SELECT Nam, Text FROM {tn}'.\
          format(tn=DB.tname))

  d = {}
  for r in c.fetchall():
    nam=r[0]
    text=r[1]
    for w in text.split():
      try:
        d[w] = d[w]+1
      except:
        d[w] = 1

  popular_words = sorted(d, key = d.get, reverse = True)

  return [ (w, d.get(w)) for w in popular_words]


