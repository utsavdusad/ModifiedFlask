#!/bin/sh
awk '/Concurrency Level:/{print $3}' abresult >temp4concurrencylevel.txt
awk '/Time per request:/{print $4}' abresult >temp4tperqst.txt
awk '/Complete requests:/{print $3}' abresult >temp4compreqst.txt
awk '/Time taken for tests:/{print $5}' abresult >temp4timtak4test.txt
awk '/(longest request)/{print $2}' abresult >temp4lonreqst.txt


head -1 temp4concurrencylevel.txt | cat >>temp4compreqst.txt
head -1 temp4lonreqst.txt | cat >>temp4compreqst.txt


tail -1 temp4tperqst.txt| cat >>temp4compreqst.txt
head -1 temp4timtak4test.txt | cat >>temp4compreqst.txt


#head -1 temp4compreqst.txt | cat >>temp4concurrencylevel.txt
#tail -1 temp4tperqst.txt| cat >>temp4concurrencylevel.txt
#head -1 temp4timtak4test.txt | cat >>temp4concurrencylevel.txt

tr '\n' '\t\t\t' < temp4compreqst.txt|cat >tempcombined.txt
awk '{print}' tempcombined.txt >>finalop.txt
#awk 'BEGIN{print"t_no   con  lt4req(ms)   t_pr(ms)   tt4tst(s) "}{print}' tempcombined.txt >>finalop.txt
