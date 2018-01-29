BEGIN{
FS=",";
noLines = 0;
endv = "false";
}
{
if(endv == "false"){
	for(i = 1; i <= NF; i++){
    gsub("}","",$i);
		split($i,a,":");
		if(index(a[1],"global_step") > 0){
			steps[noLines] = a[2];
		}else if(index(a[1],"loss") > 0){
      loss[noLines] = a[2];
		}else if(index(a[1],"accuracy") > 0){
			accuracy[noLines] = a[2];
		}
	}

	noLines++;
  if(index($0,"[") > 0){
		endv = "true";
  }
	
}
}
END{
print "step, loss, accuracy";
for(j = 0; j < noLines-1; j++){
	print steps[j]", "loss[j]", "accuracy[j];
}
}