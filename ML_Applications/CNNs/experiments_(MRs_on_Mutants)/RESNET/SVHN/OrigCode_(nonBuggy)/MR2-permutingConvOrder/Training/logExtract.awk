BEGIN{
FS = ","
noCE = 0;
noTA = 0;
noST = 0;
noL = 0;
}
/^INFO:tensorflow/{
  if(index($0,"global_step") > 0){
  }  
  else{
#    print $0
    for(i = 1; i <= NF; i++){
      split($i,a,"=");
      if(length(a) != 2)
        continue;
      split(a[2],b," ");
      if(index(a[1],"cross_entropy") > 0){
        crossEntropy[noCE++] = b[1];
      }
      if(index(a[1],"train_accuracy") > 0){
        trainAccuracy[noTA++] = b[1];
      }
      if(index(a[1],"step") > 0){
        step[noST++] = b[1];
      }
      if(index(a[1],"loss") > 0){
        loss[noL++] = b[1];
      }
    }      
  }
}
END{
#print noCE" "noTA" "noST" "noL
print "step, cross_entropy, loss, train_accuracy"
for(i = 0; i < noCE; i++){
  print step[i]","crossEntropy[i]","loss[i]","trainAccuracy[i];
}
}