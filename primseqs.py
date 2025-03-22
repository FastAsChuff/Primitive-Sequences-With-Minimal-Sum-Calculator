#Finds Primitive Sequences  With Lowest Sequence Sum
#===================================================
#Author: Simon Goater March 2025
#Free copying, use, and modification with conspicuous attribution permitted for non-commercial use only.
# https://math.stackexchange.com/questions/5047839/finding-a-sequence-of-n-numbers-such-that-the-sum-of-the-values-is-minimized-and

import json

def printminsumseqs(seqs):
  if len(seqs) == 0:
    print(0)
    return
  minsum = 0
  minsumix = -1
  for six in range(len(seqs)):
    ssum = sum(seqs[six])
    if (ssum < minsum) or (minsumix < 0):
      minsum = ssum
      minsumix = six
  print(minsum)
  for six in range(len(seqs)):
    if (sum(seqs[six]) == minsum):
      print(seqs[six])
  
def primitivecheck(x, seq):
  #Returns true if appending x produces a primitive sequence, false otherwise. seq assumed primitive.
  for y in seq:
    if (y % x == 0) or (x % y == 0):
      return False
  return True

def containsmultiple(f, s):
  for x in s:
    if x % f == 0:
      return True
  return False
  
def reservedspace(d, s):
  space = 0
  x = 2  
  if containsmultiple(2, s):
    x = 3
    if containsmultiple(3, s):
      x = 4
  while (d):
    if x not in s:
      space += x
      d -= 1
    x += 1
  return space
  
def primseqs(n, maxn, maxsum):
  resultset = set()
  result = []
  if n == 1:
    for seq in range(maxsum):
      result.append([seq+1])
    return result
  prevseqs = primseqs(n-1, maxn, maxsum)
  for s in prevseqs:
    d = maxn - n
    maxx = maxsum - reservedspace(d, s) - sum(s)
    for x in range(2,maxx+1):
      if primitivecheck(x, s):
        scopy = s.copy()
        scopy.append(x)
        resultset.add(str(json.dumps(sorted(scopy))))
  del prevseqs      
  for x in resultset:
    result.append(list(json.loads(x)))
  del resultset
  return result

n=13 #length of sequence
sumupperbound = 187 #Search for primitive sequences of n elements with sum <= sumupperbound
printminsumseqs(primseqs(n,n,sumupperbound))

#111
#[4, 6, 7, 9, 10, 11, 13, 15, 17, 19]
#134
#[4, 6, 7, 9, 10, 11, 13, 15, 17, 19, 23]
#159
#[4, 6, 7, 9, 10, 11, 13, 15, 17, 19, 23, 25]
#187
#[4, 6, 9, 10, 11, 13, 14, 15, 17, 19, 21, 23, 25]
#216
#[4, 6, 9, 10, 11, 13, 14, 15, 17, 19, 21, 23, 25, 29]
#247
#[4, 6, 9, 10, 11, 13, 14, 15, 17, 19, 21, 23, 25, 29, 31]
