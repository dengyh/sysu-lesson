# -*- coding: utf-8 -*-
import pycurl
import urllib
import re
import json
import uuid
import os

from config import userId, password

try:
    from cStringIO import StringIO
except:
    from StringIO import StringIO

loginHeader = [
    'Accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
    'Accept-Language: en-US,en;q=0.8,zh-CN;q=0.6,zh;q=0.4',
    'Cache-Control: max-age=0',
    'Connection: keep-alive',
    'Host: uems.sysu.edu.cn',
    'Origin: http://uems.sysu.edu.cn',
    'User-Agent: Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.99 Safari/537.36',
    'Content-Type: application/x-www-form-urlencoded',
    ]

getHeader = [
    'Accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
    'Accept-Language: en-US,en;q=0.8,zh-CN;q=0.6,zh;q=0.4',
    'Connection: keep-alive',
    'Host: uems.sysu.edu.cn',
    'User-Agent: Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.99 Safari/537.36',
]

postHeader = [
    'Accept: */*',
    'ajaxRequest: true',
    'render: unieap',
    'Content-Type: multipart/form-data',
    'User-Agent: Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 6.3; WOW64; Trident/7.0; .NET4.0E; .NET4.0C; InfoPath.3; .NET CLR 3.5.30729; .NET CLR 2.0.50727; .NET CLR 3.0.30729; Shuame)',
    'Host: uems.sysu.edu.cn',
    'Connection: Keep-Alive',
    'Cache-Control: no-cache',
]

cookiePattern = re.compile(r'(?<=Set-Cookie:\ )(.+?)(?=;)')
codePattern = re.compile(r'(?<=HTTP/1.1\ )(.+?)(?=\ )')
rnoPattern = re.compile(r'(?<=rno\"\ value=)(.+?)(?=\>)')

class Sysuer:
    def __init__(self, *args, **kwargs):
        self.cookie = kwargs.get('cookie', None)
        self.username = kwargs.get('username', None)
        self.password = kwargs.get('password', None)
        self.image = 'captcha/' + uuid.uuid1().hex + '.jpg'
        self.rno = None
        self.urls = {
            'login': 'http://uems.sysu.edu.cn/jwxt/j_unieap_security_check.do',
            'cookie': 'http://uems.sysu.edu.cn/jwxt/',
            'image': 'http://uems.sysu.edu.cn/jwxt/jcaptcha',
            'student': 'http://uems.sysu.edu.cn/jwxt/xscjcxAction/xscjcxAction.action?method=judgeStu',
            'score': 'http://uems.sysu.edu.cn/jwxt/xscjcxAction/xscjcxAction.action?method=getKccjList',
            'grade': 'http://uems.sysu.edu.cn/jwxt/xscjcxAction/xscjcxAction.action?method=getAllJd',
            'credit': 'http://uems.sysu.edu.cn/jwxt/xscjcxAction/xscjcxAction.action?method=getAllXf',
            'totalCredit': 'http://uems.sysu.edu.cn/jwxt/xscjcxAction/xscjcxAction.action?method=getZyxf',
            'lesson': 'http://uems.sysu.edu.cn/jwxt/xscjcxAction/xscjcxAction.action?method=getCjlcList',
            'detail': 'http://uems.sysu.edu.cn/jwxt/xscjcxAction/xscjcxAction.action?method=getFxcj',
            'school': 'http://uems.sysu.edu.cn/jwxt/quanxianLd/qxldAction.action?method=getYxxxList',
            'department': 'http://uems.sysu.edu.cn/jwxt/quanxianLd/qxldAction.action?method=getAllXsxxList',
            'profession': 'http://uems.sysu.edu.cn/jwxt/quanxianLd/qxldAction.action?method=getAllZyxxList',
            'direction': 'http://uems.sysu.edu.cn/jwxt/quanxianLd/qxldAction.action?method=getNdzyfxmcByzyfxmView',
            'courses': 'http://uems.sysu.edu.cn/jwxt/ZxxkmdtzModule/ZxxkmdtzAction.action?method=getAllJxbxx',
            'selection': 'http://uems.sysu.edu.cn/jwxt/xstk/xstk.action?method=getXsxkjgxxlistByxh',
            'table': 'http://uems.sysu.edu.cn/jwxt/KcbcxAction/KcbcxAction.action?method=getList',
        }

    def getData(self, url, headerCallback, callback):
        connect = pycurl.Curl()
        connect.setopt(connect.URL, url)
        connect.setopt(connect.HTTPHEADER, getHeader)
        connect.setopt(connect.HEADERFUNCTION, headerCallback)
        connect.setopt(connect.WRITEFUNCTION, callback)
        connect.setopt(connect.COOKIE, self.cookie)
        connect.perform()
        connect.close()

    def postData(self, url, header, data, headerCallback, callback):
        try:
            data = urllib.urlencode(data)
        except:
            pass
        connect = pycurl.Curl()
        connect.setopt(connect.URL, url)
        connect.setopt(connect.HTTPHEADER, header)
        # connect.setopt(connect.FOLLOWLOCATION, True)
        connect.setopt(connect.POST, True)
        connect.setopt(connect.POSTFIELDS, data)
        connect.setopt(connect.COOKIE, self.cookie)
        connect.setopt(connect.HEADERFUNCTION, headerCallback)
        connect.setopt(connect.WRITEFUNCTION, callback)
        connect.perform()
        connect.close()

    def passHeader(self, headerLine):
        pass

    def passWrite(self, data):
        pass

    def rnoWrite(self, data):
        result = rnoPattern.search(data)
        if result:
            self.rno = result.group()

    def saveImage(self, data):
        path = 'media/' + self.image
        file = open(path, 'wb')
        file.write(data)
        file.close()

    def loginHeader(self, headerLine):
        result = codePattern.search(headerLine)
        if result is not None:
            if result.group() != '302':
                self.cookie = None
                raise Exception('The username or password is not correct')

    def cookieHeaderFunction(self, headerLine):
        field = headerLine.split(':')[0]
        if field == 'Set-Cookie':
            cookie = cookiePattern.search(headerLine).group()
            self.cookie = cookie

    def getLoginData(self):
        self.getCookie()
        self.getImage()
        self.getRno()

    def getCookie(self):
        self.getData(self.urls['cookie'],
            self.cookieHeaderFunction, self.passWrite)

    def getImage(self):
        self.getData(self.urls['image'],
            self.passHeader, self.saveImage)

    def getRno(self):
        self.getData(self.urls['cookie'],
            self.passHeader, self.rnoWrite)

    def login(self, captcha, rno):
        if self.cookie is None:
            raise Exception('The cookie is emtpy')
        self.postData(self.urls['login'], loginHeader, {
            'j_username': self.username,
            'j_password': self.password,
            'rno': rno,
            'jcaptcha_response': captcha,
            }, self.loginHeader, self.passWrite)

    def getStudentInformation(self):
        if self.cookie is None:
            self.login()
        buffer = StringIO()
        data = '''{header:{"code": -100, "message": {"title": "", "detail": ""}},body:{dataStores:{},parameters:{"args": [], "responseParam": "result"}}}'''
        self.postData(self.urls['student'], postHeader, data, self.passHeader, buffer.write)
        return buffer.getvalue()

    def getScore(self, year='', term='', type='', yearCondition='=', termCondition='=', typeCondition='='):
        if self.cookie is None:
            self.login()
        if year == '':
            year = 'none'
            yearCondition = '!='
        if term == '':
            term = 'none'
            termCondition = '!='
        if type == '':
            type = 'none'
            typeCondition = '!='
        buffer = StringIO()
        data = '''{header:{"code": -100, "message": {"title": "", "detail": ""}},body:{dataStores:{kccjStore:{rowSet:{"primary":[],"filter":[],"delete":[]},name:"kccjStore",pageNumber:1,pageSize:100,recordCount:0,rowSetName:"pojo_com.neusoft.education.sysu.xscj.xscjcx.model.KccjModel",order:"t.xn, t.xq, t.kch, t.bzw"}},parameters:{"kccjStore-params": [{"name": "Filter_t.pylbm_0.6220199986403405", "type": "String", "value": "'%s'", "condition": " %s ", "property": "t.pylbm"}, {"name": "Filter_t.xn_0.17289099200582425", "type": "String", "value": "'%s'", "condition": " %s ", "property": "t.xn"}, {"name": "Filter_t.xq", "type": "String", "value": "'%s'", "condition": " %s ", "property": "t.xq"}], "args": ["student"]}}}''' % (type, typeCondition, year, yearCondition, term, termCondition)
        self.postData(self.urls['score'], postHeader, data, self.passHeader, buffer.write)
        return buffer.getvalue()

    def getGrade(self, year='', term='', type=''):
        if self.cookie is None:
            self.login()
        buffer = StringIO()
        data = '''{header:{"code": -100, "message": {"title": "", "detail": ""}},body:{dataStores:{jdStore:{rowSet:{"primary":[],"filter":[],"delete":[]},name:"jdStore",pageNumber:1,pageSize:2147483647,recordCount:0,rowSetName:"pojo_com.neusoft.education.sysu.djks.ksgl.model.TwoColumnModel"}},parameters:{"args": ["%s", "%s", "%s", "%s"]}}}''' % (self.username, year, term, type)
        self.postData(self.urls['grade'], postHeader, data, self.passHeader, buffer.write)
        return buffer.getvalue()

    def getCredit(self, year='', term='', type=''):
        if self.cookie is None:
            self.login()
        buffer = StringIO()
        data = '''{header:{"code": -100, "message": {"title": "", "detail": ""}},body:{dataStores:{xfStore:{rowSet:{"primary":[],"filter":[],"delete":[]},name:"xfStore",pageNumber:1,pageSize:2147483647,recordCount:0,rowSetName:"pojo_com.neusoft.education.sysu.djks.ksgl.model.TwoColumnModel"}},parameters:{"args": ["%s", "%s", "%s", "%s"]}}}''' % (self.username, year, term, type)
        self.postData(self.urls['credit'], postHeader, data, self.passHeader, buffer.write)
        return buffer.getvalue()

    def getCreditByProfession(self, type, grade, profession):
        if self.cookie is None:
            self.login()
        buffer = StringIO()
        data = '''{header:{"code": -100, "message": {"title": "", "detail": ""}},body:{dataStores:{zxzyxfStore:{rowSet:{"primary":[],"filter":[],"delete":[]},name:"zxzyxfStore",pageNumber:1,pageSize:2147483647,recordCount:0,rowSetName:"pojo_com.neusoft.education.sysu.djks.ksgl.model.TwoColumnModel"}},parameters:{"zxzyxfStore-params": [{"name": "pylbm", "type": "String", "value": "'%s'", "condition": " = ", "property": "x.pylbm"}, {"name": "nj", "type": "String", "value": "'%s'", "condition": " = ", "property": "x.nj"}, {"name": "zyh", "type": "String", "value": "'%s'", "condition": " = ", "property": "x.zyh"}], "args": []}}}''' % (type, grade, profession)
        self.postData(self.urls['totalCredit'], postHeader, data, self.passHeader, buffer.write)
        return buffer.getvalue()

    def getLessonDetail(self, lessonID, unknow="('2','99')"):
        if self.cookie is None:
            self.login()
        buffer = StringIO()
        data = '''{header:{"code": -100, "message": {"title": "", "detail": ""}},body:{dataStores:{cjlcStore:{rowSet:{"primary":[],"filter":[],"delete":[]},name:"cjlcStore",pageNumber:1,pageSize:2147483647,recordCount:0,rowSetName:"pojo_com.neusoft.education.sysu.xscj.cj.entity.CjlcEntity",order:"resource_id"}},parameters:{"cjlcStore-params": [{"name": "kch", "type": "String", "value": "'%s'", "condition": " = ", "property": "kch"}, {"name": "cjztQuery", "type": "String", "value": "%s", "condition": " in ", "property": "cjzt"}], "args": []}}}''' % (lessonID, unknow)
        self.postData(self.urls['lesson'], postHeader, data, self.passHeader, buffer.write) 
        return buffer.getvalue()

    def getScoreDetail(self, scoreId):
        if self.cookie is None:
            self.login()
        buffer = StringIO()
        data = '''{header:{"code": -100, "message": {"title": "", "detail": ""}},body:{dataStores:{fxcjStore:{rowSet:{"primary":[],"filter":[],"delete":[]},name:"fxcjStore",pageNumber:1,pageSize:2147483647,recordCount:0,rowSetName:"pojo_com.neusoft.education.sysu.xscj.cj.entity.FxcjEntity"}},parameters:{"args": ["%s"]}}}''' % (scoreId)
        self.postData(self.urls['detail'], postHeader, data, self.passHeader, buffer.write)
        return buffer.getvalue()

    def getAllSchools(self):
        if self.cookie is None:
            self.login()
        buffer = StringIO()
        data = '''{header:{"code": -100, "message": {"title": "", "detail": ""}},body:{dataStores:{yxxxStore:{rowSet:{"primary":[],"filter":[],"delete":[]},name:"yxxxStore",pageNumber:1,pageSize:2147483647,recordCount:0,rowSetName:"pojo_com.neusoft.education.sysu.common.util.entity.ZzjgEntity",order:"yxsh asc"}},parameters:{"args": []}}}'''
        self.postData(self.urls['school'], postHeader, data, self.passHeader, buffer.write)
        return buffer.getvalue()

    def getAllDepartments(self):
        if self.cookie is None:
            self.login()
        buffer = StringIO()
        data = '''{header:{"code": -100, "message": {"title": "", "detail": ""}},body:{dataStores:{allxsStore:{rowSet:{"primary":[],"filter":[],"delete":[]},name:"allxsStore",pageNumber:1,pageSize:2147483647,recordCount:0,rowSetName:"pojo_com.neusoft.education.sysu.common.util.entity.ZzjgEntity",order:"yxsh asc"}},parameters:{"args": []}}}'''
        self.postData(self.urls['department'], postHeader, data, self.passHeader, buffer.write)
        return buffer.getvalue()

    def getAllProfessions(self):
        if self.cookie is None:
            self.login()
        buffer = StringIO()
        data = '''{header:{"code": -100, "message": {"title": "", "detail": ""}},body:{dataStores:{zyxxStore:{rowSet:{"primary":[],"filter":[],"delete":[]},name:"zyxxStore",pageNumber:1,pageSize:2147483647,recordCount:0,rowSetName:"pojo_com.neusoft.education.sysu.common.util.entity.ZyEntity"}},parameters:{"args": []}}}'''
        self.postData(self.urls['profession'], postHeader, data, self.passHeader, buffer.write)
        return buffer.getvalue()

    def getAllDirections(self):
        if self.cookie is None:
            self.login()
        buffer = StringIO()
        data = '''{header:{"code": -100, "message": {"title": "", "detail": ""}},body:{dataStores:{zyfxtranscodeStroe:{rowSet:{"primary":[],"filter":[],"delete":[]},name:"zyfxtranscodeStroe",pageNumber:1,pageSize:2147483647,recordCount:0,rowSetName:"pojo_com.neusoft.education.sysu.xk.zxxk.entity.NdzyTranscodeEntity"}},parameters:{"args": []}}}'''
        self.postData(self.urls['direction'], postHeader, data, self.passHeader, buffer.write)
        return buffer.getvalue()

    # Magic, don't touch it
    def getCourses(self, kkdw='-1', kch='', jxbh='', xnd='2013-2014', xq='', jxbmc='', kcmc='', lsmc=''):
        if self.cookie is None:
            self.login()
        buffer = StringIO()
        data = '''{header:{"code": -100, "message": {"title": "", "detail": ""}},body:{dataStores:{mdtzDataStore:{rowSet:{"primary":[],"filter":[],"delete":[]},name:"mdtzDataStore",pageNumber:1,pageSize:100000,recordCount:1938,rowSetName:"pojo_com.neusoft.education.sysu.xk.zxxkgg.model.KkblbModel",order:"  a.jxbh,a.resource_id desc "}},parameters:{"mdtzDataStore-params": [{"name": "Filter_kkdw_0.1794278455136572", "type": "String", "value": "'%s'", "condition": " != ",
        "property":"kkdw"}, {"name": "Filter_xnd_0.16680808189385443", "type": "String", "value": "'%s'", "condition": " = ", "property": "xnd"}], "args": []}}}''' % (kkdw, xnd)
        self.postData(self.urls['courses'], postHeader, data, self.passHeader, buffer.write)
        return buffer.getvalue()

    def getResultOfCourseSelection(self, year=None, term=None, yearCondition='=', termCondition='='):
        if self.cookie is None:
            self.login()
        buffer = StringIO()
        if year is None:
            yearCondition = '!='
        if term is None:
            termCondition = '!='
        data = '''{header:{"code": -100, "message": {"title": "", "detail": ""}},body:{dataStores:{xsxkjgStore:{rowSet:{"primary":[],"filter":[],"delete":[]},name:"xsxkjgStore",pageNumber:1,pageSize:1000,recordCount:0,rowSetName:"pojo_com.neusoft.education.sysu.xk.xkjg.entity.XkjgxxEntity",order:"xkjg.xnd desc,xkjg.xq desc, xkjg.jxbh"}},parameters:{"xsxkjgStore-params": [{"name": "xnd", "type": "String", "value": "'%s'", "condition": " %s ", "property": "xkjg.xnd"}, {"name": "xq", "type": "String", "value": "'%s'", "condition": " %s ", "property": "xkjg.xq"}], "args": []}}}''' % (year, yearCondition, term, termCondition)
        self.postData(self.urls['selection'], postHeader, data, self.passHeader, buffer.write)
        return buffer.getvalue()

    def getCourseTable(self, year, term):
        if self.cookie is None:
            self.login()
        buffer = StringIO()
        data = '''{header:{"code": -100, "message": {"title": "", "detail": ""}},body:{dataStores:{},parameters:{"args": ["%s", "%s"], "responseParam": "rs"}}}''' % (term, year)
        self.postData(self.urls['table'], postHeader, data, self.passHeader, buffer.write)
        return buffer.getvalue()

if __name__ == '__main__':
    dengyh = Sysuer(userId, password)
    #dengyh.getLoginData()
    # print dengyh.getStudentInformation()
    # print dengyh.getScore('2014-2015', '2', '01')
    # print dengyh.getGrade()
    # print dengyh.getCredit()
    # print dengyh.getCreditByProfession('01', '2012', '08061101')
    # print dengyh.getLessonDetail('62000249')
    # print dengyh.getScoreDetail('7162329121')
    # print dengyh.getAllSchools()
    # print dengyh.getAllDepartments()
    # print dengyh.getAllProfessions()
    # print dengyh.getAllDirections()
    # print dengyh.getResultOfCourseSelection()
    # print dengyh.getCourseTable('2014-2015', '2')
    # print dengyh.getCourses()
