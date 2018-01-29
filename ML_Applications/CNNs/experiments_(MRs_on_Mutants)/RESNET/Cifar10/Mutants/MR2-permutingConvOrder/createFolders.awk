BEGIN{
}
{
print "mkdir "$1
print "cd "$1
print "mkdir Training"
print "cd Training"
print "mkdir 150Epochs"
print "mkdir 5Epochs"
print "cd .."
print "mkdir Testing"
print "cd Testing"
print "mkdir 150Epochs"
print "mkdir 5Epochs"
print "cd ..\\.."

}