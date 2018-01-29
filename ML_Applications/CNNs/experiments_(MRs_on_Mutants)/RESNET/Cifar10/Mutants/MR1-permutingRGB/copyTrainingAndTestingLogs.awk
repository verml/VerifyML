BEGIN{
}
{
gsub("/","\\",$1)
#split($1,a,"c")
#print $a[1]
#print $a[2]
print "cd "$1;
print "cd Training"
print "cd 150Epochs"
print "copy C:\\Users\\raghotham.m.rao\\Desktop\\Exp_AD\\CifarDATA\\Results\\MR-1\\CIFAR\\"$1"\\logs\\150Epochs\\* ."
#print "ren *rgb.out logs_cifar10_data_small_mr3_originalData.out"
print "cd ..\\.."
print "cd Testing"
print "cd 150Epochs"
print "copy C:\\Users\\raghotham.m.rao\\Desktop\\Exp_AD\\CifarDATA\\Results\\MR-1\\CIFAR\\"$1"\\results\\150Epochs\\* ."
#print "ren *rgb.out results_cifar10_data_small_mr3_originalData.out"
print "cd ..\\..\\.."
}