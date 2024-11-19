import flask
from api.rootApi import root_bt

app = flask.Flask(__name__)
app.register_blueprint(root_bt)  # 注册蓝图

# 按装订区域中的绿色按钮以运行脚本。
if __name__ == "__main__":
    app.run(port=7860)
