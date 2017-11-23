# -*- coding: utf-8 -*-
#should be a class
# sigle pattern load re-model config at the server first running
import json
import os
import tools
import re
import logging
import function
from collections import OrderedDict
import sys
if sys.version.startswith('2'):
	reload(sys)
	sys.setdefaultencoding('utf-8')
class capture(object):
	_instance=None
	def __init__(self):
		pass
	def __new__(cls,*args,**kwd):
		if capture._instance is None:
			capture._instance=object.__new__(cls,*args,**kwd)
			root_dir=os.sep.join(["config","re_config"])
			logging.warning('loading regular config from dir :'+os.sep.join(sys.path[0].split(os.sep)[:-1])+os.sep+os.sep.join(["config","re_config"]))
			capture._instance.re_config_dir=root_dir
			#load_re
			re_dict=dict()
			re_file_list=os.listdir(root_dir)
			for re_file in re_file_list:
				if re_file.endswith(".json")and not re_file.startswith("."):
					with open(root_dir+os.sep+re_file,'r') as f:
					# contents=f.readlines()
						# print(re_file)
						re_dict[re_file.split(".")[0]]=json.load(f,object_pairs_hook=OrderedDict)
						# re_dict[re_file.split(".")[0]]=json.load(f)
			capture._instance.re_dict=re_dict
			capture._instance.interval=0
			capture._instance.function_dict=function.function_dict
		return capture._instance
	def parse_re(self,contents="a123"):
		res=[]
		for k,v in self.re_dict.items():
			# print(k)
			temp_res=self.parse_with_function(v,contents)
			if temp_res!=None :
				# print(float(temp_res))
				res.append((k,temp_res))
			#else:
				#res.append((k,v.get('default',None)))
				# logger().info("No Match!")
		return res
	def parse_with_function(self,regular_dict,contents):
		# logger().info("parse_with_function")
		for v,regular in regular_dict['re'].items():
			for re in regular:
				res=self.do_parse(re,contents)
				if res:
					func=self.function_dict.get(v,v)
					if callable(func):
						return func(regular_dict[v+"_rule"],res)
					else:
						return func
		return None
	def do_parse(self,regular,contents):
		# logger().info("In do_parse")
		g=re.findall(regular,contents)
		return g
