import subprocess


def tsfunc(healpix,ra,dec,week1,week2,distance):

	
	if week1!=week2:
		identity="%06d_%d_%d_w%03d_w%03d" %(healpix,ra,dec,week1,week2)
		
	else:
		identity="%06d_%d_%d_w%03d" %(healpix,ra,dec,week1)
		

	gtlikefile="%s_output_gtlike.log" % (identity)
	TSFile="TS_%s.txt" %(identity)
	TS25List="TS25List.txt"
	#gtfile="%s_gtlike_output.txt" %identity




	with open("%s" %(gtlikefile),"r") as f:
			linecnt=0
			for line in f:
				if line.startswith("%f_%f:" % (ra,dec)):
					
					out="%s" %(TSFile) #writes the lines after the ra and dec of your source. We want this to get info of TS value.
					outputFile=open(out,'w')
        	                        outputFile.write(line)
					linecnt=8
					
				if linecnt>0:
					outputFile.write(line)
					linecnt=linecnt-1
					if linecnt==0:
						outputFile.close()

	with open(TSFile) as hh:
		for line in hh:
			if line.startswith("TS"): #get TS value
				x=line
				
				m,k,c,=x.split(' ')
				print c
		
						
				ts=float(c)
				if ts > 25:
					#append to a file so that we can use this list for future analysis 

					with open(TS25List,"a+") as outsyFile:
						outsyFile.write("%d %f %f %d %d %f %f\n" %(healpix,ra,dec,week1,week2,distance,ts))




'''
if __name__ == "__main__":
	import sys
	tsfunc(float(sys.argv[1]),float(sys.argv[2]),float(sys.argv[3]),int(sys.argv[4]),int(sys.argv[5]),float(sys.argv[6]))
'''
