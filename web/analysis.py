import requests

class Analysis:
    #获取用例信息
    def __init__(self,casename,interfacename,requesturl,method,header,body,relparameter,checkpoint):
        self.casename=casename
        self.interfacename=interfacename
        self.requesturl=requesturl
        self.method=method
        self.header=header
        self.body=body
        self.relparameter=relparameter
        self.checkpoint=checkpoint

    #根据用户信息发送请求,获得response
    def derequest(self):
        if self.method == post:
            responseinfo=requests.post(self.requesturl,data=self.body)

        else:
            responseinfo=requests.get(self.requesturl,header=self.header,params=self.body)
    #解析response，做检查点校验
    def checkresponse(self):






