set terminal png
set output "ApacheBenchmarkResults.png"
set title "Benchmark from Server X"
set size 1,0.5
set key left top
set xlabel 'request'
set ylabel 'ms'
plot "ud2.txt" using 10 with lines title 'Benchmark from Server X'
exit
