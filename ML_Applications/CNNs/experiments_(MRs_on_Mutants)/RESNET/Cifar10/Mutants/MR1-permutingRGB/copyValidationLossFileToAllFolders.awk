BEGIN{
}
{
#gsub("/","\\",$1)
print "cd "$1;

#mutant = $1;
#print mutant
#gsub("\\.","",mutant);
#gsub("\\\\","",mutant);
#print mutant

print "cd Testing"
print "cd 5Epochs"
print "copy C:\\Users\\raghotham.m.rao\\Desktop\\Exp_AD\\CifarDATA\\Results\\plots\\validationLoss.plt .";
print "cd .."
#print "sed -i s/\"MR1\"/\"MR1 Mutant "mutant" 5Epochs\"/g validationLoss.plt"
print "cd 150Epochs"

print "copy C:\\Users\\raghotham.m.rao\\Desktop\\Exp_AD\\CifarDATA\\Results\\plots\\validationLoss.plt .";
#print "sed -i s/\"MR1\"/\"MR1 Mutant "mutant" 150Epochs\"/g validationLoss.plt"
print "cd ..\\..\\..\\"
}