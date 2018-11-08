import requests
class RunMethod:
    def post_res(self,url,data=None,header=None):
        res=requests.get(url=url,data=data,headers=header)
        return res
    def get_pos(self,url,data=None,header=None):
        res = requests.post(url=url, data=data, headers=header)
        return res
    def run_res(self,url,method,data=None,header=None):
        if method=='post':
            res = self.post_res(url,data,header)
        else:
            res = self.get_pos(url, data, header)
        return res

if __name__ == '__main__':
    url=''
    data={}
    header={}
    res=RunMethod()
    print(res.get_pos(url,data,header))
    print(res.post_res(url, data, header))