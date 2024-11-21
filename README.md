# fishbot-qqbot

## 简介

这是一个基于 python3.11 与 flask 的试水之作，仅用于个人学习和娱乐，QQ 开放了群机器人的个人申请，原本可以使用 websocket 方法连接控制，但官方文档显示，websocket 在 2024 年即将下线，介于官方 PythonSDK 没有更新 webhook，这里打算自己搓个轮子

### 注

没有相关开发经验代码结构可能紊乱，欢迎大佬指点

## 文件或者模块解释

<details>

<summary> 文件或者模块解释 </summary>

### /api/
>flask 的蓝图文件，鉴于 webhook 方式仅仅会向一个特定的 url 发送通知，所有只有一个文件，可以理解为回调入口

### /auth/
内部有两个重要文件

static.py

> static.py 的 Static 类封装了一些静态数据,并包含有定期获取 access_token 的方法（webhook 仅能接收通知，一切机器人操作根据文档只能通过 openapi，而用 openapi 就需要在 https 请求的 headers 里加入 access_token,而 token 具有时效性）

callbackAuthentication.py

> callbackAuthentication 仅仅包含回调验证的方法，在/api/rootApi.py 中调用，一般只有第一次认证需要使用
> ![图片](/readme-assets/img1.png)

### /classes/

> 各种类，目前重要的有：  
> requestHandler，用于处理 QQbot 的回调请求  
> messageSender，用于发送消息  
> commandHandler，用于识别和调用命令  
> messageHandler，用来处理接收到的消息

### /functions/

> 机器人的命令，写各种模块的

### /functions/\*/

> 机器人的命令模块，每一个模块需要在**init**中导入方法并制作触发词和对应函数的 dict，方法仅需要满足输入参数 args:list,仅返回字符串即可，见/functions/example-function/

### /utils/

> 封装了一些个人习惯的常用代码，不太必要

### /config.json

> 保存了 bot 的"APPID"，和"SECRET"，以及"TOKEN"等参数，见/config_example.json,源文件仓库不给出（毕竟是自己的 BOT）

### /main.py

> 程序入口

### /test.py

> 测试用，不必要

</details>
