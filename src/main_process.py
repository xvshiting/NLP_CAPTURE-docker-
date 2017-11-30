import tools
from capture import capture
import json
import logging
import os
def process(records):
	# print(param)
	records=json.loads(records)
	res=dict()
	for record in records:
		temp_dict=dict()
		key_ID,contents=tools.record_parse(record)
		# with open("./record.txt","a") as f:
		# 	f.write("\n\n\n"+key_ID+"\n\n")
		# 	f.write(contents+"\n")
		# print(contents)
		capture_content=capture().parse_re(contents)
		res[key_ID]=tools.content2dict(capture_content)
	return res
def listJson():
	res=''
	return list(capture().re_dict.keys())
def getJson(name):
	res=''
	try:
		res=capture().re_dict[name]
	except Exception as e:
		logging.exception("try to get an none exits json file")
	return res
def UpdateJson(name,content):
	if name not in capture().re_dict:
		return "Failed! Do not have this json!"
	capture().re_dict[name]=content
	file_path=os.sep.join([capture().re_config_dir,name+'.json'])
	with open(file_path,'w')as f:
		json.dump(content,f)
	return "Successful!"
def AddJson(name,content):
	#	update the memory
	if name in capture().re_dict:
		return "Add Json Failed! Already have this json,you can get and update that file, or delet it first and try again! "
	capture().re_dict[name]=content
	#update local
	# print(type(content))
	file_path=os.sep.join([capture().re_config_dir,name+'.json'])
	with open(file_path,'w')as f:
		json.dump(content,f)
	return "Successful!"
def DeletJson(name):
	#del in memory
	if name not in capture().re_dict:
		return "Failed! Do not have this json!"
	del(capture().re_dict[name])
	# del in local
	file_path=os.sep.join([capture().re_config_dir,name+'.json'])
	os.remove(os.sep.join([capture().re_config_dir,name+'.json']))
	return "Successful!"
