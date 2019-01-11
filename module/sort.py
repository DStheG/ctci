#!/usr/bin/python
def quick_sort(s):
  p = 0; l = 1
  r = len(s) - 1

  if(r <= 0):
    return ''.join(s)

  while (l <= r):
    while ((s[p] >= s[l]) and (l < r)):
      l = l + 1
    while ((s[p] < s[r]) and (l < r)):
      r = r - 1
    if(l == r):
      if(s[p] > s[l]):
        s[p], s[l] = s[l], s[p]
      else:
        s[p], s[l-1] = s[l-1], s[p]
      break;
    else:
      s[l], s[r] = s[r], s[l]

  return ''.join(quick_sort(s[:l])) + ''.join(quick_sort(s[l:]))

def merge_sort(s):
  l = len(s)
  if(l <= 1):
    return s

  s1 = merge_sort(s[:l/2])
  s2 = merge_sort(s[l/2:])

  ret = []
  for i in range(l):
    if(len(s1) == 0):
      ret = ret + s2
      break;
    if(len(s2) == 0):
      ret = ret + s1
      break;
    if(s1[0] < s2[0]):
      min_value = s1.pop(0)
    else:
      min_value = s2.pop(0)
    ret.append(min_value)

  return ret

