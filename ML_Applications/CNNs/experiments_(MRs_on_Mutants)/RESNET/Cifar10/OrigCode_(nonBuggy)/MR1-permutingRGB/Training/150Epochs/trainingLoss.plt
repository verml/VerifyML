set terminal wxt
set size square
unset key
set key font "courier,22"
set key noenhanced
set datafile separator ","
#set title 'Cifar Data MR1 Original 150 Epochs' font ",22"
set xlabel 'steps' font ",22" offset 0,-1
set ylabel 'training loss' font ",22" offset -1,0

#set key maxcols 3 height 3
#set key inside autotitle columnheader
set key inside top right autotitle columnheader maxcols 2 maxrows 3
set colors classic

set for[i=1:10] linetype i dashtype  1


#set xrange [*:*]
set autoscale x
#set xtics 2000 offset 0, -0.5
set xtics 1000 font ",22" offset 0,-0.5


#set yrange [*:*]
set autoscale y
set ytics 0.5 font ",22" offset -0.5,0

plot 'combinedData.csv' using 1:3 w lp lw 2 lt 1 pt 2  ps 1.25 lc 0,\
     'combinedData.csv' using 5:7 w  lp lw 2 lt 2 pt 4  ps 1.25 lc 1,\
	 'combinedData.csv' using 9:11 w lp lw 2 lt 3 pt 6  ps 1.25 lc 3,\
	 'combinedData.csv' using 13:15 w lp lw 2  lt 4 pt 5  ps 1.25 lc 2,\
	 'combinedData.csv' using 17:19 w lp lw 2 lt 5 pt 12  ps 1.25  lc 7,\
	 'combinedData.csv' using 21:23 w lp lw 2 lt 6 pt 1  ps 1.25  lc 4
#	 'combinedData.csv' using 25:27 w lp lw 2 lt 7 pt 7  ps 1.25  lc 8,\
#	 'combinedData.csv' using 29:31 w lp lw 2 lt 8 pt 8  ps 1.25  lc 14