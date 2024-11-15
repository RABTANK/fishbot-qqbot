import json
import os
import asyncio
import requests
import time
class Static:
    APPID=102074147
    SECRET="1RrHh8Z0RsJkCe6Y0SuNqJmFiBe8c6a4"
    TOKEN="rhmCA4CLSCqAPDfc1Zo1ldMO0KlsjjhB"
    WORKPATH=os.getcwd()
    
    def __init__(self) -> None:
        pass

    async def get_access_token(self):
        file_path = os.path.join(self.WORKPATH, "static/access_token.json")
        if not os.path.exists(file_path):
            file=open(file_path, 'w')
            file.close()
        if os.path.getsize(file_path) == 0:
            await self._update_access_token()
        
        file=open(file_path,'r')
        access_token=json.load(file)
        if access_token['get_time']+int(access_token['expires_in'])<time.time():
            await self._update_access_token()
        
        return access_token['access_token']
    
    async def _update_access_token(self):
        file_path = os.path.join(self.WORKPATH, "static/access_token.json")
        params = {
            'appId': str(self.APPID),  # 替换为实际的参数值
            'clientSecret': str(self.SECRET)   # 替换为实际的参数值
        }
        headers = {
            'Content-Type': 'application/json'
        }
        print("ok")
        try:
            response = requests.post("https://bots.qq.com/app/getAppAccessToken", data=json.dumps(params),headers=headers)
            response.raise_for_status()  # 检查请求是否成功
            response_data:dict = response.json()
            response_data.update({"get_time":time.time()})
            with open(file=file_path,mode='w',encoding='utf-8') as file:
                json.dump(response_data,file,ensure_ascii=False,indent=4)
                file.close()
        except Exception as e:
            print(f"Error: {e}")
        

sta=Static()

a=asyncio.run(sta.get_access_token())
print(a)