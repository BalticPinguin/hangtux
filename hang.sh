#!/bin/bash
if [[ $LINES -gt "48" ]] && [[ $COLUMNS -gt "137" ]]
   then 
   cat introfile.txt
elif [[ $LINES -gt "13" ]] && [[ $COLUMNS -gt "46" ]]
   then
   cat introsmall
else
   echo 'hangman!'
fi

read -sn1
python man.py
