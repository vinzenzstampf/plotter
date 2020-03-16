# parse text

import subprocess
from re import sub
from pdb import set_trace

proc = subprocess.Popen(['python','sync_4Mar20.py'],stdout=subprocess.PIPE)

lines = []
while True:
  lyne = proc.stdout.readline()
  line = lyne.strip(); line = str(line)
  line = sub("'",'',line)
  line = sub('b','',line)
  line = line[11:]
  # set_trace()
  line = sub('\*', '', line)
  for i in range(10):
    line = sub('  ', ' ', line)
    if len(line) and line[0] == ' ': line = line[1:]
  line = line.strip()
  # set_trace()
  if line == '' or 'event' in line: continue
  if 'entries' in line or 'entry' in line: break
  lines.append(line)
  print(line)
  if not lyne: break

with open ('sync_6Mar20_mem_DY17.txt', 'w') as out_file:
  for line in lines:
    out_file.write(line + '\n')

out_file.close()
