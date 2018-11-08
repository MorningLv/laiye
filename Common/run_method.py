import requests
class RunMethod:
    def post_res(self,url,data=None,header=None):
        res=requests.post(url=url,data=data,headers=header)
        return res
    def get_res(self,url,data=None,header=None):
        res = requests.get(url=url, data=data, headers=header)
        return res
    def run_res(self,url,method,data=None,header=None):
        if method=='post':
            res = self.post_res(url, data, header)
        else:
            res = self.get_res(url, data, header)
        return res

if __name__ == '__main__':
    url='http://dev.hunliji.com/p/wedding/index.php/Admin/APILiveChannelReport/live_report_protocol'
    data={
        "live_type":1
    }
    header={
        "Cookie":"HUNLIJI_MERCHANT_AUTH=362165%2C1539159071%2C6873f52e2c4da8adcee26e11be4df93d;"
    }
    res=RunMethod()
    print(res.run_res(url=url,method='get',data=data,header=header).json())

