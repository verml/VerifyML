BEGIN{
}
{
print "cd "$1;
print "copy C:\\Users\\raghotham.m.rao\\Desktop\\Exp_AD\\CifarDATA\\Results\\MR-2\\CIFAR\\"$1"\\* ."
print "cd .."
}