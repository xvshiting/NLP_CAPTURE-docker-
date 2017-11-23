# -*- coding: utf-8 -*-
import json
# from logger import logger
def record_parse(content):
	# print(content)
	ID=list(content.keys())[0]
	return ID,content_parse(content.get(ID))
def content_parse(content):
	res=[]
	if content==None:
		# logger().info("record is empty")
		return " "
	for c in content:
		temp_str=""
		role=list(c.keys())[0]
		Text=c[role]['text']
		temp_str=role+" : "+Text
		res.append(temp_str)
	return "\n".join(res)
def content2dict(content):
	d=dict()
	for c in content:
		d[c[0]]=c[1]
	# logger().info("In content2json")
	return d
