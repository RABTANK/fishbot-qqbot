from idlelib.iomenu import encoding
from cryptography.hazmat.primitives import serialization
from cryptography.hazmat.primitives.asymmetric import ed25519
import sys


def print_private_key_bytes(private_key):
    # 获取私钥的原始字节
    private_bytes = private_key.private_bytes(
        encoding=serialization.Encoding.Raw,
        format=serialization.PrivateFormat.Raw,
        encryption_algorithm=serialization.NoEncryption()
    )

    # 将每个字节转换为整数，并构建列表
    int_list = [int(byte) for byte in private_bytes]

    # 打印私钥的整数列表
    print("privateKey: [{}]".format(' '.join(map(str, int_list))))
def print_public_key(public_key):
    # 获取公钥的原始字节
    public_bytes = public_key.public_bytes(
        encoding=serialization.Encoding.Raw,
        format=serialization.PublicFormat.Raw
    )

    # 将每个字节转换为整数，并构建列表
    int_list = [int(byte) for byte in public_bytes]

    # 打印公钥的整数列表
    print("publicKey: [{}]".format(' '.join(map(str, int_list))))
def generate_ed25519_key_pair(bot_secret):
    # 确保seed长度至少为ed25519种子长度（应该是32字节）
    seed = bot_secret
    while len(seed) < 32:
        seed = seed * 2  # 重复字符串直到达到所需长度

    # 取种子的前32字节作为实际种子
    seed = seed.encode()[:32]

    # 使用种子生成密钥对
    private_key = ed25519.Ed25519PrivateKey.from_private_bytes(seed)
    public_key = private_key.public_key()

    return public_key, private_key


# 输入的secret
bot_secret = "naOC0ocQE3shWLAfffVLB1rhYPG7"

# 生成公钥和私钥
public_key, private_key = generate_ed25519_key_pair(bot_secret)
print_public_key(public_key)
print_private_key_bytes(private_key)

