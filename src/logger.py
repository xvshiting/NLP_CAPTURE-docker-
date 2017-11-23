# import sys
# import os
# #Singleton
# class logger(object):
# 	_instance=None
# 	def __init__(self):
# 		pass
# 	def __new__(cls,*args,**kwd):
# 		if logger._instance is None:
# 			logger._instance=object.__new__(cls,*args,**kwd)
# 			logger._instance.file_path="../log/log.txt"
# 		return logger._instance
# 	def info(self,msg):
# 		with open(self.file_path,'a')as f:
# 			m='INFO:====> '+msg+'\n'
# 			# f.write(m)
# 			print(m)
# 	def debuge(self,msg):
# 		with open(self.file_path,'a')as f:
# 			m='DEBUG:====> '+msg+'\n'
# 			f.write(m)
# 	def error(self,msg):
# 		with open(self.file_path,'a')as f:
# 			m='ERROR:====> '+msg+'\n'
# 			f.write(m)
