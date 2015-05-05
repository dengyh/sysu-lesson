# SYSU-LESSON API documents

### Comment App

| 功能 | 接口URL | 接口类型 | 必选项 | 可选项 | 响应类型|响应内容 |
|:---:|:------:|:-------:|:-----:|:-----:|:-----:|:-----:|
|发布评论|/comment/create/|HTTP/POST|lessonID(string)<br>content(string)|followID(string)|HTTP/JSON|result(boolean)<br>message(string)<br>commentID(string)|

--------------------

### Exchange App

| 功能 | 接口URL | 接口类型 | 必选项 | 可选项 | 响应类型|响应内容 |
|:---:|:------:|:-------:|:-----:|:-----:|:-----:|:-----:|
|发布“交易”|/exchange/create/|HTTP/POST|lessonID(string)<br>phone(string)<br>email(string)||HTTP/HTML|刷新页面吧|
|完成“交易”|/exchange/finish/|HTTP/POST|exchangeID(string)||HTTP/JSON|result(boolean)<br>message(string)|
|取消“交易”|/exchange/cancel/|HTTP/POST|exchangeID(string)||HTTP/JSON|result(boolean)<br>message(string)|

-----------------------------

### Grade App

| 功能 | 接口URL | 接口类型 | 必选项 | 可选项 | 响应类型|响应内容 |
|:---:|:------:|:-------:|:-----:|:-----:|:-----:|:-----:|

------------------------------

### Lesson App

| 功能 | 接口URL | 接口类型 | 必选项 | 可选项 | 响应类型|响应内容 |
|:---:|:------:|:-------:|:-----:|:-----:|:-----:|:-----:|

----------------------------------

### Meterial App

| 功能 | 接口URL | 接口类型 | 必选项 | 可选项 | 响应类型|响应内容 |
|:---:|:------:|:-------:|:-----:|:-----:|:-----:|:-----:|

------------------------------------

### School App

| 功能 | 接口URL | 接口类型 | 必选项 | 可选项 | 响应类型|响应内容 |
|:---:|:------:|:-------:|:-----:|:-----:|:-----:|:-----:|
