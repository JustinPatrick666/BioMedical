from fastapi import FastAPI
from pydantic import BaseModel
#实现请求体需要导入的包
app = FastAPI()

@app.get("/")##"/"可以改成其他的例如 /helloWorld/ 这样的，只是改了浏览器的地址
             #同时，get方法可以使用delete 或者post方法或者put方法

async def root():
    return {"message": "Hello World!!!"}
"""
假设现在你有一个路径操作：/files/{file_path}，但是你需要 file_path 本身包含一个 路径， 比如 home/johndoe/myfile.txt.
因此, 文件路径可能是: /files/home/johndoe/myfile.txt
在这种情况，我们使用Path转换器就可以进行转换了。使用以下方法声明值是路径的路径参数。
/files/{file_path:path}
语句表示的意思是：参数的名字是 file_path，:path说明参数file_path对应的类型是 path 类型.
from fastapi import FastAPI
app = FastAPI()
@app.get("/files/{file_path:path}")
def read_user_me(file_path):
    return {"file_path": file_path}
"""
