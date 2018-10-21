#!/usr/bin/python
# -*- coding: utf-8 -*-
import json
import urllib
import requests
import hashlib
import urllib3
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

APIURL = {'sandboxLoginApi': 'https://sandbox-api.100credit.cn/bankServer2/user/login.action'
		, 'hainaApi': 'https://api.100credit.cn/HainaApi/data/getData.action'#海纳接口地址
		, 'specialListApi': 'https://api.100credit.cn/special_list/v1/upload_data'#特殊名单
		, 'loanApi': 'https://api.100credit.cn/loanwarn/v1/upload_data'#贷中
		, 'dcpApi': 'https://api.100credit.cn/cobweb/v1/get_data'#失联修复
		, 'insureApi': 'https://api.100credit.cn/insureApi/M1000/getData.action'#保险地址
		, 'bankServerApi': 'https://api.100credit.cn/huaxiang/v1/get_report'#画像地址
		, 'loginApi': 'https://api.100credit.cn/bankServer2/user/login.action'#登录地址
		, 'sandboxApi': 'https://sandbox-api.100credit.cn/bankServer2/data/terData.action'#沙箱地
		, 'strategyApi':'https://api.100credit.cn/strategyApi/v1/hxQuery'#策略地址
		, 'trinityforceApi':'https://api.100credit.cn/trinity_force/v1/get_data'#整合接口地址
		}


class Client(object):
	"""docstring for Client"""
	def __init__(self, username, password, apicode):
		super(Client, self).__init__()
		self.username = username
		self.password = password
		self.apicode = apicode
		self.session = requests.session()

	def __post(self, url, data):
		#发送post请求
		req = self.session.post(url, data = data, verify = False)
		print(req.text)
		if req:
			return json.loads(req.text)
		else:
			return None

	def __getMd5Value(self, val):
		#将指定的val字符串转化为md5值
		md5 = hashlib.md5()
		md5.update(val.encode('utf8'))
		md5_val = md5.hexdigest()
		return md5_val

	def get_tokenid(self):
		'''
		获取tokenid
		'''
		url = "https://api.100credit.cn/bankServer2/user/login.action"
		res = self.__post(url, data = {"userName": self.username, "password": self.password, "apiCode": self.apicode})
		return res

	def get_sand_tokenid(self):
		'''
		获取tokenid
		'''
		url = 'https://sandbox-api.100credit.cn/bankServer2/user/login.action'
		res = self.__post(url, {"userName": self.username, "password": self.password, "apiCode": self.apicode})
		# tokenid = res["tokenid"]
		return tokenid

	def get_data(self, params):
		'''
		获取返回json
		'''
		args = json.loads(params)
		url = APIURL[args["apiName"]]
		tokenid = args["tokenid"]
		reqData = args["reqData"]
		checkCode = self.__getMd5Value(json.dumps(reqData) + self.__getMd5Value(self.apicode + tokenid))
		data = {"tokenid": tokenid, "jsonData": json.dumps(reqData), "checkCode": checkCode, "apiCode": self.apicode}
		res = self.__post(url, data = data)
		# print("res" + res)
		return res


if __name__ == '__main__':
	c = Client('zgh', 'zgh', '444333')    #账号,密码,apicode
	res = c.get_tokenid()
	tokenid = res['tokenid']


	data = {"apiName":"strategyApi",     #请求的APIURL,在页面最上端。
			"tokenid": tokenid,
			"reqData":{
				"strategy_id":'STR0000058' #策略编号
				,"id":''  #身份证号码
				,"cell":""  #手机号码
				#,"bank_id":'6217002270008198914'
				,"name":''  #英明
			}
			}
	'''
    #海纳产品调用
	data = {"apiName":"bankServerApi",     #请求的APIURL,在页面最上端。
			"tokenid": tokenid,
			"reqData":{
				"meal":'SpecialList_c' #模块编号
				,"id":'622722199601261017'  #身份证号码
				,"cell":"13259987392"  #手机号码
				#,"bank_id":'6217002270008198914'
				,"name":'王续成'  #姓名
			}
			}
	#整合产品调用
	'''
	'''
	data = {"apiName":"trinityforceApi",     #请求的APIURL,在页面最上端。
			"tokenid": tokenid,
			"reqData":{
			    "meal":'' #模块编号
				,"id":''  #身份证号码
				,"cell":""  #手机号码
				,"bank_id":''
				,"name":''  #姓名
			}
			}
	'''
	result=c.get_data(json.dumps(data))