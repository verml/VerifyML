BEGIN{
}
{
if(FNR>1){

gsub("/","\\",$1)
print "cd "$1;

mutant = $1;
print mutant
gsub("\\.","",mutant);
gsub("\\\\","",mutant);
#print mutant

print "cd logs"
#print "cd 5Epochs"
#print "copy C:\\Users\\raghotham.m.rao\\Desktop\\Exp_AD\\CifarDATA\\Results\\plots\\trainingLoss.plt .";
#print "sed -i s/\"MR1 Mutant 9 150 Epochs\"/\"MR1 Mutant "mutant" 5Epochs\"/g trainingLoss.plt"
print "cd 150Epochs"

print "copy C:\\Users\\raghotham.m.rao\\Desktop\\Exp_AD\\CifarDATA\\Results\\plots\\trainingLoss.plt .";
#print "sed -i s/\"MR1 Mutant 9 150 Epochs\"/\"MR1 Mutant "mutant" 150Epochs\"/g trainingLoss.plt"
print "cd ..\\..\\..\\"
}
}