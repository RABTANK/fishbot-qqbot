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
> ![图片](/readme-assets/Snipaste_2024-11-20_22-59-43.png)