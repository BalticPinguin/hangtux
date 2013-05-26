import random
import os
import sys
introfile=50
foo=open('introfile.txt', 'r')
for i in range(introfile): print(foo)
os.system('clear')
########################   fist step: taking one word outof file

     # rand=random.randint(max(open('words.dat').readlines()))
rand=random.randint(0,6)
word=open('words.txt').readlines()[rand]
letter=[word[i] for i in range(len(word)-1)]
test=[ "_" for i in range(len(letter)) ]
for i in range(len(test)): sys.stdout.write("%s"%test[i])
print('' )

########################   second: asking player for a letter and make it visible

for i in range(50):
   sugg=raw_input('type in one letter: ')
   control=0
   for i in range(len(letter)):
      if sugg==letter[i]:
         test[i]=sugg
         control=1
   if control==0:
      print('hangman!!!')
   else:
      print('The word is: ')
   for i in range(len(test)): sys.stdout.write("%s"%test[i])
   print("")
   if test[i] is not '_' and i in range(len(letter)) :
      break
print('you needed too many tries')
