#用户接口类
#定义用户相关接口的PO类、封装接口调用方法、提供测试用例调用接口的入口
from pages.base_api import BaseAPI

class UserAPI(BaseAPI):
    def login(self, username, password):
        """登录接口PO封装"""
        endpoint = "/api/mgr/signin"
        payload = {
            "username": username,
            "password": password
        }
        # 根据接口文档，登录请求使用x-www-form-urlencoded格式
        return self.request.send_request(
            "POST", 
            endpoint, 
            data=payload, 
            headers={"Content-Type": "application/x-www-form-urlencoded"}
        )
    
    def list_customers(self, pagesize, pagenum, keywords=None):
        """列出客户"""
        endpoint = "/api/mgr/customers"
        params = {
            "action": "list_customer",
            "pagesize": pagesize,
            "pagenum": pagenum
        }
        if keywords:
            params["keywords"] = keywords
        return self.request.send_request(
            "GET", 
            endpoint, 
            params=params, 
            headers=self.headers,
            cookies=self.cookies
        )
        
    def add_customer(self, name, phonenumber, address):
        """添加客户"""
        endpoint = "/api/mgr/customers"
        payload = {
            "action": "add_customer",
            "data": {
                "name": name,
                "phonenumber": phonenumber,
                "address": address
            }
        }
        return self.request.send_request(
            "POST", 
            endpoint, 
            json=payload, 
            headers=self.headers,
            cookies=self.cookies
        )