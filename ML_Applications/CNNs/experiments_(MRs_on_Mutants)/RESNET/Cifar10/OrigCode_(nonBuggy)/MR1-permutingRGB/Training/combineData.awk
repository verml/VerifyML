BEGIN{
	noCols= -1;
	noRows = 0;
	noFiles = 1;
	FS = ",";
	noFields = 0;
	
}
{
	if(NR == FNR){
		if(FNR == 1){
			noCols = NF;
			noFields = NF;
			fName = FILENAME;
			split(fName, a, ".");
			
			if(index(a[2],"\\") > 0){
				split(a[2],b,"\\");
				file[0]=b[length(b)];
			}else{
				file[0]=a[1];
			}
		}
		for(i = 1; i <= NF; i++){
			data[noRows,i-1] = $i;
		}
		noRows++;
	}else{
		if(FNR == 1){
			noRows = 0;
			fName = FILENAME;
			split(fName, a, ".");
			if(index(a[2],"\\") > 0){
				split(a[2],b,"\\");
				file[noFiles]=b[length(b)];
			}else{
				file[noFiles]=a[1];
			}
			
			noFiles++;
			prevCols = noCols-1;
			noCols += NF;
		}
		for(i = 1; i <= NF; i++){
			data[noRows,prevCols+i] = $i;
		}
		noRows++;
	}
}
END{
	#print "No Rows: "noRows;
	#print "No Files: "noFiles;
	#print "No. Cols. "noCols;
	#for(i = 0; i < noFiles; i++)
	#	print file[i];
		
	#for(j = 0; j < noCols; j++)
	#	print data[0,j];
		
	str = data[0,0]"_"file[0];
	for(j = 1; j < noCols; j++)
		str = str","data[0,j]"_"file[int(j/noFields)];
	print str;
	
	
	for(i = 1; i < noRows; i++){
		str = data[i,0];
		for(j = 1; j < noCols; j++)
			str = str","data[i,j];
		print str;
	}	
}
