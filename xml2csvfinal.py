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
	s1=''

	
	t=[]
	t2=[]
	x=root.find('id_info')
	nct=x.find('nct_id').text
	t.append(nct)
	temp=root.find('overall_status').text
	t.append(temp)
	if(root.findall('start_date')):
		temp=root.find('start_date').text
		t.append(temp)
	else:
		t.append("NAN")
	if(root.findall('completion_date')):
		temp=root.find('completion_date').text
		t.append(temp)
	else:
		t.append("NAN")
	print(filename)
	

	for x in root.findall('condition'):
		y=x.text
		t2.append(y)
	listToStr = ','.join(map(str, t2)) 
	t.append(listToStr)
	study=[]
	if(root.findall('study_design_info')):
		#z=root.findall('study_design_info')
		for content in root.find('study_design_info').iter():
			
			if(content.tag!='study_design_info'):
				study.append(content.text)
		st = ','.join(map(str, study))
		study.clear()	
		t.append(st) 
	else:
		t.append("NAN")

	if(root.findall('eligibility')):
		#z=root.findall('study_design_info')
		for content in root.find('eligibility').iter():
			
			if content.tag =="gender":
				study.append('gender:{}'.format(content.text))
				print(x.text)
			
				
			if content.tag =="minimum_age":
				study.append('Min Age:{}'.format(content.text))
			
			if content.tag =="maximum_age":
				study.append('Max Age:{}'.format(content.text))
			
			if content.tag =="sampling_method":
				study.append('sampling_method:{}'.format(content.text))
			
	
		st = ','.join(map(str, study))
		#print(st)
		t.append(st) 
		study.clear()
	else:
		t.append("N/A")

	
	if(root.findall("has_expanded_access")):
		temp=root.find('has_expanded_access').text
		t.append(temp)
	else:
		t.append("NAN")
	if(root.findall("enrollment")):
		temp=root.find("enrollment").text
		t.append(temp)
	else:
		t.append("NAN")
	print(t)
	csvwriter.writerow(t)

