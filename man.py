# =*= coding: utf-8 -*-
import random
import os
import sys
########################   fist step: taking one word outof file

     # rand=random.randint(max(open('words.dat').readlines()))
os.system('clear')
language=input('which language do you like? Type 2 for german and 1 for english')
if language==1:
   foo=open('english.txt').readlines()
elif language==2:
   foo=open('deutsch.txt').readlines()
else :
   foo=open('words.txt').readlines()
os.system('clear')
rand=random.randint(0, len(foo))
word=foo[rand]
letter=[word[i] for i in range(len(word)-1)]
test=[ "_" for i in range(len(letter)) ]
for i in range(len(test)): sys.stdout.write("%s"%test[i])
print('')

########################   second: asking player for a letter and make it visible
i=0
while i in range(0,11):
   sugg=raw_input('type in one letter: ')
   control=0
   for j in range(len(letter)):
      if sugg==letter[j]:
         test[j]=sugg
         control=1
   if control==0:
      print('hangman!!!')
      i=i+1
   else:
      if language==1:
         print('The word is: ')
      else:
         print('Was Wort ist: ')
   for j in range(len(test)): sys.stdout.write("%s"%test[j])
   print("")
   control=0
   for k in range(len(letter)) :
      if test[k] is '_' :
         control=1
         continue
   if control==0:
      if language==1:
         print("You have won the game! Congratualtions! ")
      else:
         print("Sie haben Gewonnen! Herzlichen Glückwunsch! ")
      break
if control==1:
   if language==1:
      print('you needed too many tries')
      print('The word that was asked is: %s ' %word)
   else:
      print('Sie haben zu viele Versuche gebraucht')
      print('Das gesuchte Wort ist: %s' %word)
