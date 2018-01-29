set terminal wxt
set size square
unset key
set key font "courier,17"
set key noenhanced
set datafile separator ","
#set title 'Cifar Data MR1 Original 150 Epochs' font ",18"
set xlabel 'steps' font ",22" offset 0,-1
set ylabel 'test loss' font ",22" offset -1,0
set tics font ",22"


set key inside autotitle columnheader maxcols 1 maxrows 8
set colors classic

set for[i=1:10] linetype i dashtype  1


#set xrange [*:*]
set xtics 1000 offset 0,-0.5
set autoscale x
#set yrange [*:*]
set autoscale y
set ytics 2 offset -0.5,0
plot 'combinedData.csv' using 1:2 w lp lw 2 lt 1 pt 2  ps 1.25 lc 0,\
     'combinedData.csv' using 4:5 w  lp lw 2 lt 2 pt 4  ps 1.25 lc 1,\
	 'combinedData.csv' using 7:8 w lp lw 2 lt 3 pt 6  ps 1.25 lc 3,\
	 'combinedData.csv' using 10:11 w lp lw 2  lt 4 pt 5  ps 1.25 lc 2,\
	 'combinedData.csv' using 13:14 w lp lw 2 lt 5 pt 12  ps 1.25  lc 7,\
	 'combinedData.csv' using 16:17 w lp lw 2 lt 6 pt 1  ps 1.25  lc 4,\
	 'combinedData.csv' using 19:20 w lp lw 2 lt 7 pt 7  ps 1.25  lc 8,\
	 'combinedData.csv' using 22:23 w lp lw 2 lt 8 pt 8  ps 1.25  lc 14