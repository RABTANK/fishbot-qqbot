from flask import Blueprint,request
root_bt=Blueprint('root',__name__)


@root_bt.route('/farmbot', methods=['GET', 'POST'])
def root():
    # 打印请求头
    print("Request Headers:")
    for header_name, header_value in request.headers:
        print(f"{header_name}: {header_value}")
    # 打印请求体（如果有的话）
    if request.method == 'POST':
        if request.is_json:
            print("Request Body (JSON):")
            print(request.json)
        else:
            print("Request Body (Form Data):")
            print(request.form)
    else:
        print("No request body to print.")
    return "Request processed."

