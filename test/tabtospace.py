import sys
filename = sys.argv[1]
with open(filename+'.py', 'r') as input, open(filename+'_temp.py', 'w') as output:
  for line in input:
    output.write(line.replace('\t', '  '))
