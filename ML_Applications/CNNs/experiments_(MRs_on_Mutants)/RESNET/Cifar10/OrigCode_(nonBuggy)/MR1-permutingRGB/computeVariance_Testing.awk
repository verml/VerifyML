BEGIN{
FS=","
noRows = 0;
noCols = 0;
}
{
fName = FILENAME;
if($0 !~ /[a-zA-z]+/){
noCols = 0;
for(i = 2; i <= NF; i+= 3){
	loss[noRows, noCols++] = $i; 
}
noCols = 0;
for(i = 3; i <= NF; i+= 3){
	accuracy[noRows, noCols++] = $i; 
}

noRows++;
}
}
END{
#print "No Rows: "noRows;
#print "No Cols: "noCols;




for(i = 0; i < noRows; i++){
	sumLoss[i] = 0;
	sumAccuracy[i] = 0;
	for(j = 0; j < noCols; j++){
		sumLoss[i] += loss[i,j];
		sumAccuracy[i] += accuracy[i,j]; 
	}
	
#	print sumLoss[i]" "sumAccuracy[i];
}



for(i = 0; i < noRows; i++){
	meanLoss[i] = sumLoss[i]/noCols;
	meanAccuracy[i] = sumAccuracy[i]/noCols;
}

for(i = 0; i < noRows; i++){
	varLoss[i]  = 0;
	varAccuracy[i] = 0;
	
	for(j = 0; j < noCols; j++){
		varLoss[i] += (loss[i,j] - meanLoss[i])*(loss[i,j] - meanLoss[i]);
		varAccuracy[i] += (accuracy[i,j] - meanAccuracy[i])*(accuracy[i,j] - meanAccuracy[i]);
	}
	
	varLoss[i] /= (noCols-1);
	varAccuracy[i] /= (noCols-1);
	
	stdLoss[i] = sqrt(varLoss[i]);
	stdAccuracy[i] = sqrt(varAccuracy[i]);
}

#for(i = 0; i < noRows; i++)
#	print meanLoss[i]" "stdLoss[i]" "meanAccuracy[i]" "stdAccuracy[i];

sumVarLoss = 0;
meanVarLoss = 0;
varVarLoss = 0;

sumVarAccuracy = 0;
meanVarAccuracy = 0;
varVarAccuracy = 0;	
for(i = 0; i < noRows; i++){
	sumVarLoss += varLoss[i];
	sumVarAccuracy += varAccuracy[i];
}

meanVarLoss = sumVarLoss/noRows;
meanVarAccuracy = sumVarAccuracy/noRows;


#print meanVarLoss" "meanVarAccuracy;

for(i = 0; i < noRows; i++){
	varVarLoss += (varLoss[i]-meanVarLoss)*(varLoss[i]-meanVarLoss);
	varVarAccuracy += (varAccuracy[i]-meanVarAccuracy) * (varAccuracy[i]-meanVarAccuracy);
}

varVarLoss /= (noRows-1);
varVarAccuracy /= (noRows-1);

stdDevVarLoss = sqrt(varVarLoss);
stdDevVarAccuracy = sqrt(varVarAccuracy);	

#print meanVarLoss" "meanVarAccuracy
#print stdDevVarLoss" "stdDevVarAccuracy

sumStdLoss = 0;
meanStdLoss = 0;
varStdLoss = 0;

sumStdAccuracy = 0;
meanStdAccuracy = 0;
varStdAccuracy = 0;	
for(i = 0; i < noRows; i++){
	sumStdLoss += stdLoss[i];
	sumStdAccuracy += stdAccuracy[i];
}

meanStdLoss = sumStdLoss/noRows;
meanStdAccuracy = sumStdAccuracy/noRows;


#print meanStdLoss" "meanStdAccuracy;

for(i = 0; i < noRows; i++){
	varStdLoss += (stdLoss[i]-meanStdLoss)*(stdLoss[i]-meanStdLoss);
	varStdAccuracy += (stdAccuracy[i]-meanStdAccuracy) * (stdAccuracy[i]-meanStdAccuracy);
}

varStdLoss /= (noRows-1);
varStdAccuracy /= (noRows-1);

stdDevStdLoss = sqrt(varStdLoss);
stdDevStdAccuracy = sqrt(varStdAccuracy);	

#print meanStdLoss" "meanStdAccuracy
print fName","stdDevStdLoss","stdDevStdAccuracy
}