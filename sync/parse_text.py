# parse text

import subprocess
from re import sub
from pdb import set_trace

# proc = subprocess.Popen(['python','sync_17Feb20.py'],stdout=subprocess.PIPE)
proc = subprocess.Popen(['python','sync_2Mar20.py'],stdout=subprocess.PIPE)

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
  if line == '' or 'run' in line: continue
  if 'entries' in line: break
  lines.append(line)
  # print(line)
  if not lyne: break

with open ('sync_3Mar20_eem_OS_M4Vp0029.txt', 'w') as out_file:
  for line in lines:
    out_file.write(line + '\n')

out_file.close()
