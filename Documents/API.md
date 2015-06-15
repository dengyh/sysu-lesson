# SYSU-LESSON API documents

### Comment App

| 功能 | 接口URL | 接口类型 | 必选项 | 可选项 | 响应类型|响应内容 |
|:---:|:------:|:-------:|:-----:|:-----:|:-----:|:-----:|
|发布评论|/comment/create/|HTTP/POST|lessonID(string)<br>content(string)|followID(string)|HTTP/JSON|result(boolean)<br>message(string)<br>commentID(string)|

--------------------

### Exchange App

| 功能 | 接口URL | 接口类型 | 必选项 | 可选项 | 响应类型|响应内容 |
|:---:|:------:|:-------:|:-----:|:-----:|:-----:|:-----:|
|“交易”页面|/exchange/|HTTP/GET||page(string)|HTTP/HTML|exchanges(array[Exchange])|
|“我的交易”页面|/exchange/home/|HTTP/GET||page(string)|HTTP/HTML|exchanges(array[Exchange])|
|“新建交易”页面|/exchange/form/|HTTP/GET|||HTTP/HTML||
|发布“交易”|/exchange/create/|HTTP/POST|lessonID(string)<br>phone(string)<br>email(string)||HTTP/HTML|刷新页面吧|
|完成“交易”|/exchange/([0-9]+)/finish/|HTTP/POST|exchangeID(string)||HTTP/JSON|result(boolean)<br>message(string)|
|取消“交易”|/exchange/([0-9]+)/cancel/|HTTP/POST|exchangeID(string)||HTTP/JSON|result(boolean)<br>message(string)|

-----------------------------

### Grade App

| 功能 | 接口URL | 接口类型 | 必选项 | 可选项 | 响应类型|响应内容 |
|:---:|:------:|:-------:|:-----:|:-----:|:-----:|:-----:|
|“个人成绩”页面|/grade/|HTTP/GET|||HTTP/HTML|grades(array[Grade])|

------------------------------

### Lesson App

| 功能 | 接口URL | 接口类型 | 必选项 | 可选项 | 响应类型|响应内容 |
|:---:|:------:|:-------:|:-----:|:-----:|:-----:|:-----:|
|“课程列表”页面|/lesson/|HTTP/GET||page(string)<br>...(筛选项)|HTTP/HTML|lessons(array[Lesson])|
|“课程详情”页面|/lesson/([0-9]+)/|HTTP/GET|||HTTP/GET|lesson(Lesson)|
|“我的课程列表”页面|/lesson/home/|HTTP/GET||page(string)<br>...(筛选项)|HTTP/HTML|lessons(array[Lesson])|
----------------------------------

### Meterial App

| 功能 | 接口URL | 接口类型 | 必选项 | 可选项 | 响应类型|响应内容 |
|:---:|:------:|:-------:|:-----:|:-----:|:-----:|:-----:|
|发布资源|/meterial/create/|HTTP/POST|lessonID(string)<br>year(string)<br>term(string)<br>title(string)<br>file(file)|remark(string)|HTTP/JSON|result(boolean)<br>message(string)<br>meterialID(string)|

------------------------------------

### School App

| 功能 | 接口URL | 接口类型 | 必选项 | 可选项 | 响应类型|响应内容 |
|:---:|:------:|:-------:|:-----:|:-----:|:-----:|:-----:|
