import subprocess
from make2FGLxml import *
#import xml.dom.minidom 
import cfg

import os, sys

def genxmlfunc(healpix,ra,dec,week1,week2):
	
	if week1!=week2:
		identity="%06d_%d_%d_w%03d_w%03d" %(healpix,ra,dec,week1,week2)
		ltcube="%s/lat_ltcube_weekly_w%03d_w%03d_p203_v001.fits" %(cfg.home,week1,week2)
	else:
		identity="%06d_%d_%d_w%03d" %(healpix,ra,dec,week1)
		ltcube="%s/lat_spacecraft_weekly_w%03d_p203_v001_ltcube.fits" %(cfg.home,week1)

	region_filtered="%s_region_filtered_gti.fits" %(identity)
	fermisources="%s_fermisources_model.xml" %(identity)
	makexmllog="%s_output_makexml.log" %identity
	
	

	with open(makexmllog,'w') as outputFile:
		subprocess.call(['%s'%(cfg.pythoncommand),'makesyfunc.py', '%s' %(region_filtered), '%s' %fermisources],stdout=outputFile)


if __name__ == "__main__":
	import sys
	genxmlfunc(float(sys.argv[1]),float(sys.argv[2]),float(sys.argv[3]),int(sys.argv[4]),int(sys.argv[5]))

