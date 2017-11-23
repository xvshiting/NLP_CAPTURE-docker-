# -*- coding: utf-8 -*-
# from logger import logger
function_dict=dict()


def record_function(func):
	function_dict[func.__name__]=func
	def wrapper(rule,value):
		return func(rule,value)
	return wrapper

@record_function
def add(rule,value):
	if type(value)!=list :
		value=[value]
	# print("In add")
	sum=0
	for v in value:
		sum=int(v)+sum
	k=interval(rule,[sum])
	return interval(rule,[sum])

@record_function
def interval(rule,value):
	# logger().info("In interval")
	for k,v in rule.items():
			# print (value)
		if len(v)==1:
			if int(value[0])>v[0]:
				# print("Should return K:   "+str(k))
				return k
		elif v[0]<=int(value[0]) and int(value[0])<v[1]:
			return k
