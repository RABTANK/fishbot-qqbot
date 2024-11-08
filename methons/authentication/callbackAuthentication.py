import ed25519


def generate_ed25519_key_pair(bot_secret):
    # 确保seed长度至少为ed25519种子长度（应该是32字节）
    seed = bot_secret
    while len(seed) < 32:
        seed = seed * 2  # 重复字符串直到达到所需长度
    # 取种子的前32字节作为实际种子
    seed = seed.encode()[:32]
    # 使用种子生成密钥对
    private_key = ed25519.SigningKey(seed)
    public_key = private_key.get_verifying_key()
    return public_key, private_key


# 输入的secret
bot_secret = "naOC0ocQE3shWLAfffVLB1rhYPG7"

# 生成公钥和私钥
public_key, private_key = generate_ed25519_key_pair(bot_secret)

print(list(public_key.to_bytes()))
print(list(private_key.to_bytes()))
