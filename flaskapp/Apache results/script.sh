#!/bin/sh
awk '/Concurrency Level:/{print $3}' Mabresult >Mtemp4concurrencylevel.txt        #2

awk '/Time per request:/{print $4}' Mabresult >Mtemp4tperqst.txt                  #5  
awk '/Time per request:/{print $4}' Oabresult >Otemp4tperqst.txt                  #6 

awk '/Complete requests:/{print $3}' Mabresult >Mtemp4compreqst.txt               #1

awk '/Time taken for tests:/{print $5}' Mabresult >Mtemp4timtak4test.txt          #7         
awk '/Time taken for tests:/{print $5}' Oabresult >Otemp4timtak4test.txt	  #8


awk '/(longest request)/{print $2}' Mabresult >Mtemp4lonreqst.txt                  #3
awk '/(longest request)/{print $2}' Oabresult >Otemp4lonreqst.txt		   #4


head -1 Mtemp4concurrencylevel.txt | cat >>Mtemp4compreqst.txt


head -1 Otemp4lonreqst.txt | cat >>Mtemp4compreqst.txt


tail -1 Otemp4tperqst.txt| cat >>Mtemp4compreqst.txt




head -1 Otemp4timtak4test.txt | cat >>Mtemp4compreqst.txt

head -1 Mtemp4lonreqst.txt | cat >>Mtemp4compreqst.txt
tail -1 Mtemp4tperqst.txt| cat >>Mtemp4compreqst.txt

head -1 Mtemp4timtak4test.txt | cat >>Mtemp4compreqst.txt



#head -1 temp4compreqst.txt | cat >>temp4concurrencylevel.txt
#tail -1 temp4tperqst.txt| cat >>temp4concurrencylevel.txt
#head -1 temp4timtak4test.txt | cat >>temp4concurrencylevel.txt

tr '\n' '\t\t\t' < Mtemp4compreqst.txt|cat >Mtempcombined.txt
#awk 'BEGIN{print"\tComplete requests  concurrency level  longest time for request(ms)   time per request(ms)  total time for tests(s)"}#{printf "\n\nOriginal:%9s %15s %25s %25s %25s",$1,$2,$3,$4,$5}{printf "\nModified:\t\t\t%28s %25s %25s",$6,$7,$8}' Mtempcombined.txt >>finalop.txt
awk '{printf "\n\nOriginal:%9s %15s %25s %25s %25s",$1,$2,$3,$4,$5}{printf "\nModified:\t\t\t%28s %25s %25s",$6,$7,$8}' Mtempcombined.txt >>finalop.txt
