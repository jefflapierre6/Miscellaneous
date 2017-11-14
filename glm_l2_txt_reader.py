"""
The purpose of this script is to read in reprocessed GLM L2 data from 
text files produced by D. Mach.

This script takes in the file name as an argument.

GLM data gets written into a dictionary called glmData, which consists
of three keys, 'Flash', 'Group', 'Event'. Each key has their own data
fields, which are listed when each key is initialize using Bunch.

Example:
To access the all the start times of the flashes
glmData['Flash'].time

Written by J. Lapierre
This is a work in progress, so if you have problems, contact me at
jlapierre@earthnetworks.com
"""

import sys
import re

class Bunch:
	"""this is just a simple class to allow me to put several valiables 
	into a grouping, mostly for naming clarity
	"""
	def __init__(self, **kwds):
		self.__dict__.update(kwds)

# Create flash, group, and event classes to combine data
flash = Bunch( flashid=[], start=[], end=[], lat=[], lon=[], energy=[],\
                  area=[], childcnt=[])
                  
group = Bunch( groupid=[], childid=[], start=[], end=[], lat=[], lon=[],\
                  energy=[], area=[], parentid=[],\
                  childcnt=[])
                  
event = Bunch( eventid=[], childid=[], time=[], x=[], y=[], lat=[], \
				lon=[], energy=[], parentid=[])
         
# Create glmData dictionary to combine all the above classes into one dataset
glmData = {}
glmData['Flash'] = flash
glmData['Group'] = group
glmData['Event'] = event

# Regular expression to find floating point, integers, or exponential numbers
regexpflt = '([-+]?\d*\.\d+)'
regexpint = '(\d+)'
regexpe = '([-+]?\d*\.\d+e[-+]?\d+)'

# Read in the file name
fname = str(sys.argv[-1])

# Begin loop which reads every line of the file
with open(fname,'r') as f:
	line = f.readline()
	count = 0 # Used to make sure all the lines get read by comparing the lengths of all three classes
	while line:
		count += 1
		#print line
		# Separate data into Flashes, Groups, and Events
		if 'Flash' in line:
			# Found a Flash, extract data
			#print('Flash Data')
			keyword = 'Flash #'
			idx = line.find(keyword)
			glmData['Flash'].flashid.append(int(re.search(keyword+regexpint,line).group(1)))
			keyword = 'Start Time:'
			idx = line.find(keyword)
			glmData['Flash'].start.append(float(re.search(keyword+regexpflt,line).group(1)))
			keyword = 'End Time:'
			idx = line.find(keyword)
			glmData['Flash'].end.append(float(re.search(keyword+regexpflt,line).group(1)))
			keyword = 'Centroid Lat:'
			idx = line.find(keyword)
			glmData['Flash'].lat.append(float(re.search(keyword+regexpflt,line).group(1)))
			keyword = 'Centroid Lon:'
			idx = line.find(keyword)
			glmData['Flash'].lon.append(float(re.search(keyword+regexpflt,line).group(1)))
			keyword = 'Energy:'
			idx = line.find(keyword)
			glmData['Flash'].energy.append(float(re.search(keyword+regexpe,line).group(1)))
			keyword = 'Footprint:'
			idx = line.find(keyword)
			glmData['Flash'].area.append(float(re.search(keyword+regexpflt,line).group(1)))
			keyword = 'Child_Count:'
			idx = line.find(keyword)
			glmData['Flash'].childcnt.append(int(re.search(keyword+regexpint,line).group(1)))
			#print glmData['Flash'].flashid[-1], glmData['Flash'].start[-1], glmData['Flash'].end[-1], glmData['Flash'].lat[-1], glmData['Flash'].lon[-1], glmData['Flash'].energy[-1], glmData['Flash'].area[-1], glmData['Flash'].childcnt[-1]
		elif 'Group' in line:
			# Found a Group, extract data
			#print('Group Data')
			keyword = 'Group #'
			idx = line.find(keyword)
			glmData['Group'].groupid.append(int(re.search(keyword+regexpint,line).group(1)))
			keyword = 'Child #'
			idx = line.find(keyword)
			glmData['Group'].childid.append(int(re.search(keyword+regexpint,line).group(1)))
			keyword = 'Start Time:'
			idx = line.find(keyword)
			glmData['Group'].start.append(float(re.search(keyword+regexpflt,line).group(1)))
			keyword = 'End Time:'
			idx = line.find(keyword)
			glmData['Group'].end.append(float(re.search(keyword+regexpflt,line).group(1)))
			keyword = 'Centroid Lat:'
			idx = line.find(keyword)
			glmData['Group'].lat.append(float(re.search(keyword+regexpflt,line).group(1)))
			keyword = 'Centroid Lon:'
			idx = line.find(keyword)
			glmData['Group'].lon.append(float(re.search(keyword+regexpflt,line).group(1)))
			keyword = 'Energy:'
			idx = line.find(keyword)
			glmData['Group'].energy.append(float(re.search(keyword+regexpe,line).group(1)))
			keyword = 'Footprint:'
			idx = line.find(keyword)
			glmData['Group'].area.append(float(re.search(keyword+regexpflt,line).group(1)))
			keyword = 'Parent_ID:'
			idx = line.find(keyword)
			glmData['Group'].parentid.append(int(re.search(keyword+regexpint,line).group(1)))
			keyword = 'Child_Count:'
			idx = line.find(keyword)
			glmData['Group'].childcnt.append(int(re.search(keyword+regexpint,line).group(1)))
			#print glmData['Group'].groupid[-1], glmData['Group'].childid[-1], glmData['Group'].start[-1], glmData['Group'].end[-1], glmData['Group'].lat[-1], glmData['Group'].lon[-1], glmData['Group'].energy[-1], glmData['Group'].area[-1], glmData['Group'].parentid[-1], glmData['Group'].childcnt[-1]
		elif 'Event' in line:
			# Found an Event, extract data
			#print('Event Data')
			keyword = 'Event #'
			idx = line.find(keyword)
			glmData['Event'].eventid.append(int(re.search(keyword+regexpint,line).group(1)))
			keyword = 'Child #'
			idx = line.find(keyword)
			glmData['Event'].childid.append(int(re.search(keyword+regexpint,line).group(1)))
			keyword = 'Time:'
			idx = line.find(keyword)
			glmData['Event'].time.append(float(re.search(keyword+regexpflt,line).group(1)))
			keyword = 'X_Pixel:'
			idx = line.find(keyword)
			glmData['Event'].x.append(int(re.search(keyword+regexpint,line).group(1)))
			keyword = 'Y_Pixel:'
			idx = line.find(keyword)
			glmData['Event'].y.append(int(re.search(keyword+regexpint,line).group(1)))
			keyword = 'Lat:'
			idx = line.find(keyword)
			glmData['Event'].lat.append(float(re.search(keyword+regexpflt,line).group(1)))
			keyword = 'Lon:'
			idx = line.find(keyword)
			glmData['Event'].lon.append(float(re.search(keyword+regexpflt,line).group(1)))
			keyword = 'Energy:'
			idx = line.find(keyword)
			glmData['Event'].energy.append(float(re.search(keyword+regexpe,line).group(1)))
			keyword = 'Parent_ID:'
			idx = line.find(keyword)
			glmData['Event'].parentid.append(int(re.search(keyword+regexpint,line).group(1)))
			#print glmData['Event'].eventid[-1], glmData['Event'].childid[-1], glmData['Event'].time[-1], glmData['Event'].x[-1], glmData['Event'].y[-1], glmData['Event'].lat[-1], glmData['Event'].lon[-1], glmData['Event'].energy[-1], glmData['Event'].parentid[-1]
		else:
			print('Not a valid category.')
		line = f.readline()
		
			
			
