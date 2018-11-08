class CaseModel:
    case_id=0
    is_run = 1
    tittle=2
    url=3
    method=4
    has_header=5
    depend_data=6
    data=7
    result=8

    def get_id(self):
        return self.case_id
    def get_run(self):
        return self.is_run
    def get_tittle(self):
        return self.tittle
    def get_url(self):
        return self.url
    def get_method(self):
        return self.method
    def get_header(self):
        return self.has_header
    def get_depend(self):
        return self.depend_data
    def get_data(self):
        return self.data
    def get_result(self):
        return self.result

if __name__ == '__main__':
    model=CaseModel()
    print(model.get_data())

