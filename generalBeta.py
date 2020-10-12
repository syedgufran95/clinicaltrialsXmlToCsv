# def findtext(root, arg):

# def findtag():
# def check(root , arg):
# def list2string(list,string):
# def findneted(root,arg):
import xml.etree.ElementTree as ET 
import csv
import glob

def parser(data,tags):
	tree=ET.iterparse(data)
	for event, node in tree:
		if node.tag in tags:
			if node.tag in tags:
				yield node.tag,node.text

def fun(root,path,levels):
	i=0;
	p=root
	for x in range(5):
		if(p==root):
			p=root.find(path[i])
			q=p.find(path[i+1])
		else:
			p=q
			q=p.find(path[i+1])
		i+=1

		print('p and q in i {} iteration is : {} {}'.format(i,p.tag,q.tag))


# testdata = open('combined2.csv', 'w')
# csvwriter = csv.writer(testdata)
# csvwriter.writerow(["nct_id","overall_status","start_date",
# 	"completion_date","condition","Study design info","eligibility","has_expanded_access","enrollment"])

# with open('./abc/NCT03852537.xml','r')as myFile:
# 	results=parser(myFile,{'sponsors','agency'})
# 	print(type(results))
# 	for tag, text in results:
# 		print("\n",tag,"\n",text)
#search_result
data_folder="abc"
for filename in glob.iglob(data_folder+"/*.xml"):
	tree = ET.parse(filename)
	root = tree.getroot()
	path=['stuff-list','stuff','item-list','item','item-type','moreinfo','evenmoreinfo']
	#path=['sponsors','lead_sponsor','agency']
	levels=5
	fun(root,path,levels)
