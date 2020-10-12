



def find_nctid(root):
	x=root.find('id_info')
	temp=x.find('nct_id').text
	return temp
def get_status(root):
	temp=root.find('overall_status').text
	return temp
def start_date(root):
	if(root.findall('start_date')):
		temp=root.find('start_date').text
		return temp
	else:
		s='N/A'
		return s

def completion_date(root):
	if(root.findall('completion_date')):
		temp=root.find('completion_date').text
		return temp
	else:
		s='N/A'
		return s
def condition(root):
	t2=[]
	if(root.findall('completion_date')):
		for x in root.findall('condition'):
			y=x.text
			t2.append(y)
		listToStr = ','.join(map(str, t2)) 
		temp=listToStr
		return temp
	else:
		s='N/A'
		return s 

def studydesign(root):
	study=[]
	if(root.findall('study_design_info')):
		#z=root.findall('study_design_info')
		for content in root.find('study_design_info').iter():
			
			if(content.tag!='study_design_info'):
				study.append(content.text)
		temp = ','.join(map(str, study))
		return temp 
	else:
		s='N/A'
		return s
def eligibility(root):
	study=[]
	if(root.findall('eligibility')):
		#z=root.findall('study_design_info')
		for content in root.find('eligibility').iter():
			
			if content.tag =="gender":
				study.append('gender:{}'.format(content.text))
				
			
				
			if content.tag =="minimum_age":
				study.append('Min Age:{}'.format(content.text))
			
			if content.tag =="maximum_age":
				study.append('Max Age:{}'.format(content.text))
			
			if content.tag =="sampling_method":
				study.append('sampling_method:{}'.format(content.text))
			
	
		temp = ','.join(map(str, study))
		#print(st)
		return temp
	else:
		s='N/A'
		return s

def has_expanded_access(root):
	if(root.findall("has_expanded_access")):
		temp=root.find('has_expanded_access').text
		return temp
	else:
		s='N/A'
		return s
def enrollment(root):
	if(root.findall("enrollment")):
		temp=root.find("enrollment").text
		return temp
	else:
		s='N/A'
		return s


import xml.etree.ElementTree as ET 
import csv
import glob

testdata = open('combined2.csv', 'w')
csvwriter = csv.writer(testdata)
csvwriter.writerow(["nct_id","overall_status","start_date",
	"completion_date","condition","Study design info","eligibility","has_expanded_access","enrollment"])


#search_result
data_folder="search_result"
for filename in glob.iglob(data_folder+"/*.xml"):
	tree = ET.parse(filename)
	root = tree.getroot()
	t=[]
	t.append(find_nctid(root))
	t.append(get_status(root))
	t.append(start_date(root))
	t.append(completion_date(root))
	t.append(condition(root))
	t.append(studydesign(root))
	t.append(eligibility(root))
	t.append(has_expanded_access(root))
	t.append(enrollment(root))
	print(t)
	
	csvwriter.writerow(t)