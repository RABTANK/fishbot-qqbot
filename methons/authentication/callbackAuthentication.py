import os
import io
import string
import ed25519

def generate_ed25519_key_pair(bot_secret):
    # 确保seed长度至少为ed25519种子长度（应该是32字节）
    seed = bot_secret
    while len(seed) < ed25519.SEED_SIZE:
        seed = seed * 2  # 重复字符串直到达到所需长度

    # 取种子的前32字节作为实际种子
    seed = seed.encode()[:ed25519.SEED_SIZE]

    # 使用种子生成密钥对
    rand = io.BytesIO(seed)
    private_key = ed25519.SigningKey.generate(os.urandom(ed25519.SEED_SIZE), backend=None)
    private_key = ed25519.SigningKey(seed)
    public_key = private_key.get_verifying_key()

    return public_key, private_key

# 输入的secret
bot_secret = "naOC0ocQE3shWLAfffVLB1rhYPG7"

# 生成公钥和私钥
public_key, private_key = generate_ed25519_key_pair(bot_secret)

# 打印公钥和私钥
print("Public Key:", public_key.to_bytes().hex())
print("Private Key:", private_key.to_bytes().hex())
