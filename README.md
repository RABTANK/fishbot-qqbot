# fishbot-qqbot
## 简介
这是一个基于python3.11与flask的试水之作，仅用于个人学习和娱乐，QQ开放了群机器人的个人申请，原本可以使用websocket方法连接控制，但官方文档显示，websocket在2024年即将下线，介于官方PythonSDK没有更新webhook，这里打算自己搓个轮子
### 注
没有相关开发经验代码结构可能紊乱，欢迎大佬指点

## 文件或者模块解释
### /api/
flask的蓝图文件，鉴于webhook方式仅仅会向一个特定的url发送通知，所有只有一个文件，可以理解为程序入口
### /auth/
内部有两个重要文件

 static.py  
>static.py的Static类封装了一些静态数据,并包含有定期获取access_token的方法（webhook仅能接收通知，一切机器人操作根据文档只能通过openapi，而用openapi就需要在https请求的headers里加入access_token,而token具有时效性）  

 callbackAuthentication.py
> callbackAuthentication仅仅包含回调验证的方法，在/api/rootApi.py中调用，一般只有第一次认证需要使用
> ![图片](/readme-assets/img1.png)

### /classes/
>各种类，目前重要的有：  
requestHandler，用于处理QQbot的回调请求  
messageSender，用于发送消息  
commandHandler，用于识别和调用命令  
messageHandler，用来处理接收到的消息

### /functions/ 
> 机器人的命令，写各种模块的

### /functions/*/
> 机器人的命令模块，每一个模块需要在__init__中导入方法并制作触发词和对应函数的dict，方法仅需要满足输入参数args:list,仅返回字符串即可，见/functions/example-function/

### /utils/
> 封装了一些个人习惯的常用代码，不太必要

### /config.json
> 保存了bot的"APPID"，和"SECRET"，以及"TOKEN"等参数，见/config_example.json,源文件仓库不给出（毕竟是自己的BOT）

### /main.py
> 程序入口

### /test.py
> 测试用，不必要
    