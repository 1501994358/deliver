#!/usr/bin/python
# -*- coding: utf-8 -*-
import json
import urllib2, urllib
import hashlib
import ssl

if hasattr(ssl, '_create_unverified_context'):
    ssl._create_default_https_context = ssl._create_unverified_context

APIURL = {'sandboxLoginApi': 'https://sandbox-api.100credit.cn/bankServer2/user/login.action' \
    , 'hainaApi': 'https://api.100credit.cn/HainaApi/data/getData.action' \
    , 'specialListApi': 'https://api.100credit.cn/special_list/v1/upload_data' \
    , 'loanApi': 'https://api.100credit.cn/loanwarn/v1/upload_data' \
    , 'dcpApi': 'https://api.100credit.cn/cobweb/v1/get_data' \
    , 'insureApi': 'https://api.100credit.cn/insureApi/M1000/getData.action' \
    , 'bankServerApi': 'https://api.100credit.cn/bankServer2/data/terData.action' \
    , 'loginApi': 'https://api.100credit.cn/bankServer2/user/login.action' \
    , 'sandboxApi': 'https://sandbox-api.100credit.cn/bankServer2/data/terData.action' \
          }
'''hainaApi单独调用的地址'''
'''bankServerApi打包调用地址'''
'''sandboxLoginApi沙箱测试环境登录地址'''
'''loanApi贷中请求地址'''
'''loginApi登录地址'''
'''sandboxApis沙箱测试请求地址'''


class Client(object):
    """docstring for Client"""

    def __init__(self, username, password, apicode):
        super(Client, self).__init__()
        self.username = username
        self.password = password
        self.apicode = apicode

    def __post(self, url, data):
        '''
        发送post请求
        '''
        req = urllib2.Request(url)
        data = urllib.urlencode(data)
        opener = urllib2.build_opener(urllib2.HTTPCookieProcessor())
        response = opener.open(req, data)
        res = response.read()
        if res:
            return json.loads(res)
        else:
            return None

    def __getMd5Value(self, val):
        '''
        将指定的val字符串转化为md5值
        '''
        md5 = hashlib.md5()
        md5.update(val)
        md5_val = md5.hexdigest()
        return md5_val

    def get_tokenid(self):
        '''
        获取tokenid
        '''
        url = "https://api.100credit.cn/bankServer2/user/login.action"
        res = self.__post(url, {"userName": self.username, "password": self.password, "apiCode": self.apicode})
        return res

    def get_sand_tokenid(self):
        '''
        获取tokenid
        '''
        url = 'https://sandbox-api.100credit.cn/bankServer2/user/login.action'
        res = self.__post(url, {"userName": self.username, "password": self.password, "apiCode": self.apicode})
        tokenid = res["tokenid"]
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
        res = self.__post(url, data)
        return res


if __name__ == '__main__':
    c = Client('zgh', 'zgh', '444333')  # 账号,密码,apicode
    res = c.get_tokenid()
    tokenid = res['tokenid']  # 画像登陆
    # tokenid = c.get_sand_tokenid()           #非画像登陆(sandboxApi)

    data = {"apiName": "bankServerApi",  # 请求的APIURL,在页面最上端。（打包调用）
            "tokenid": tokenid,
            "reqData": {
                "meal": 'ApplyLoan,SpecialList_c'
                , "id": '51102819910802381X'
                , "cell": ["13548640535"]
                , "bank_id": '6217002270008198914'
                , "name": '陆柳芳'
                , "apply_source": 'Counter_application'
                , "flushByApiCode": '3000164'}
            }
    result = c.get_data(json.dumps(data))
    print
    result

# data = {"apiName":"hainaApi",     #请求的APIURL,在页面最上端。(单独调用)
#		"tokenid": tokenid,
#		"reqData":{
#
#			"meal":'IdTwo_photo'
#			,"id":'51102819910802381X'
#			,"cell":["13548640535"]
#			,"bank_id":'6217002270008198914'
#			,"name":'陆柳芳'
#			,"apply_source":'Counter_application'
#			,"flushByApiCode":'3000164'}
#		}
# result=c.get_data(json.dumps(data))
# print result