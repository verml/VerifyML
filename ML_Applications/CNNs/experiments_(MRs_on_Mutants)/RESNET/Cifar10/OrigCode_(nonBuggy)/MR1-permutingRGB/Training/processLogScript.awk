BEGIN{
}
{
#./116/logs/150Epochs/logs_cifar_mut116_150MR1bgr.out
gsub("/","\\",$1);
#print $1;

split($1,a,"\\");
fileName = a[length(a)];
parentDir = a[1];
for(i = 2; i < length(a); i++)
	parentDir = parentDir"\\"a[i];
#print "Parent Dir: "parentDir;
#print "FileName: "fileName

split(fileName,b,"_");
outFileName = b[3]"_"b[4];
gsub(".out",".csv",outFileName);

print "awk -f logExtract.awk "$1" > "parentDir"\\"outFileName
}
END{
}