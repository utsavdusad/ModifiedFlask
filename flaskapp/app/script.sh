#!/bin/sh
awk '/Concurrency Level:/{print $3}' abresult >temp4concurrencylevel.txt
awk '/Time per request:/{print $4}' abresult >temp4tperqst.txt
head -1 temp4tperqst.txt| cat >>temp4concurrencylevel.txt
tr '\n' '\t\t\t' < temp4concurrencylevel.txt|cat >tempcombined.txt
awk 'BEGIN{print"concurrency  time"}{print}' tempcombined.txt >>finalop.txt
