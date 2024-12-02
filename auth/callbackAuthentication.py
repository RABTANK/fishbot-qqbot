import binascii
import json
import ed25519
from classes.requestHandler import RequestHandler
from auth import Static
import cryptography.hazmat.primitives.asymmetric.ed25519 as ed25519_cry


def generate_signature_new(
    
    appid, secret, body, signature_hex, signature_timestamp, plain_token
):
    # 如果secret不够长，则重复secret直到达到Ed25519种子大小
    while len(secret) < 32:
        secret += secret
    secret = secret[:32]

    # 使用secret作为种子生成私钥
    signing_key = ed25519_cry.Ed25519PrivateKey.from_private_bytes(
        secret.encode("utf-8")
    )

    # 构造消息
    message = f"{signature_timestamp}{plain_token}".encode("utf-8")

    # 使用私钥对消息进行签名
    signature = signing_key.sign(message)

    # 将签名转换为十六进制字符串
    signature_hex = binascii.hexlify(signature).decode("utf-8")

    # 返回包含签名的响应对象
    response = {"plain_token": plain_token, "signature": signature_hex}

    return json.dumps(response)


def generate_signature(
    appid, secret, body, signature_hex, signature_timestamp, plain_token
):
    # 如果secret不够长，则重复secret直到达到Ed25519种子大小
    while len(secret) < 32:
        secret += secret
    secret = secret[:32]

    # 使用secret作为种子生成私钥
    signing_key = ed25519.SigningKey(secret.encode("utf-8"))

    # 构造消息
    message = f"{signature_timestamp}{plain_token}".encode("utf-8")

    # 使用私钥对消息进行签名
    signature = signing_key.sign(message)

    # 将签名转换为十六进制字符串
    signature_hex = binascii.hexlify(signature).decode("utf-8")

    # 返回包含签名的响应对象
    response = {"plain_token": plain_token, "signature": signature_hex}

    return json.dumps(response)


def build_callback_auth_body(handler: RequestHandler):
    signature = generate_signature_new(
        Static.APPID,
        Static.SECRET,
        handler.get_body(),
        handler.get_signature_hex(),
        handler.get_signature_timestamp(),
        handler.get_plain_token(),
    )
    return signature
