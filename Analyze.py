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

  return d


def popularWords(d):
  popular_words = sorted(d, key = d.get, reverse = True)
  return [ (w, d.get(w)) for w in popular_words]


def popularDict(d, count):
  w = popularWords(d)
  return dict(w[:count])

def letterPattern(letter, words):
  conn = sqlite3.connect(DB.name)
  c = conn.cursor()
  c.execute('SELECT Nam, Text FROM {tn} WHERE Nam="{n}"'.\
          format(tn=DB.tname, n='{fn}.html'.format(fn=letter)))
  for r in c.fetchall():
    nam=r[0]
    text=r[1]
    words_letter = text.split()
    pat = []
    for w in [w[0] for w in words]:
      pat.append(words_letter.count(w))
    return pat


d = wordDict()

w = popularWords(d)

# d10 = popularDict(d,10)


