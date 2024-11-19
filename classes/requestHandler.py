import json

from flask import request


class RequestHandler:
    def __init__(self):
        self.body = None
        self.signature_hex = None
        self.signature_timestamp = None
        self.plain_token = None
        self._parse_request()

    def _parse_request(self):
        # 解析请求体
        if request.is_json:
            self.body = request.json
            if "d" in self.body and "plain_token" in self.body["d"]:
                self.plain_token = self.body["d"]["plain_token"]

        # 解析请求头部
        self.signature_hex = request.headers.get("X-Signature-Ed25519")
        self.signature_timestamp = request.headers.get("X-Signature-Timestamp")

    def get_body(self):
        return self.body

    def get_signature_hex(self):
        return self.signature_hex

    def get_signature_timestamp(self):
        return self.signature_timestamp

    def get_plain_token(self):
        return self.plain_token

    def get_op(self):
        return self.body["op"]

    def print_all(self):
        print("Request Headers:")
        for header_name, header_value in request.headers:
            print(f"{header_name}: {header_value}")
        # 打印请求体（如果有的话）
        if request.method == "POST":
            if request.is_json:
                print("Request Body (JSON):")
                print(json.dumps(request.json))
            else:
                print("Request Body (Form Data):")
                print(request.form)
        else:
            print("No request body to print.")
