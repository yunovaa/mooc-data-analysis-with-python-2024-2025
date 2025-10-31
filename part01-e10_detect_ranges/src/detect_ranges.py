#!/usr/bin/env python3

def detect_ranges(l):
  n = []
  l = sorted(l)
  i = 0
  while i < len(l):
    start = l[i]
    j = i
    while j + 1 < len(l) and l[j+1] - l[j] == 1:
      j += 1
    end = l[j]

    if start == end:
      n.append(start)
    else:
      n.append((start, end+1))

    i = j + 1
  return n

def main():
    L = [2, 5, 4, 8, 12, 6, 7, 10, 13]
    result = detect_ranges(L)
    print(result)

if __name__ == "__main__":
    main()
