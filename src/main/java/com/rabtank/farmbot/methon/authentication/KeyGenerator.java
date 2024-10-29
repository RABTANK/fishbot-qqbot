package com.rabtank.farmbot.methon.authentication;
import java.io.ByteArrayInputStream;
import org.bouncycastle.jce.provider.BouncyCastleProvider;
import java.math.BigInteger;
import java.nio.charset.StandardCharsets;

import java.security.*;
import java.util.Arrays;

public class KeyGenerator {
    private static final int SEED_SIZE = 32;
    private String botSecret;
    private byte[] publicKey;
    private byte[] privateKey;

    public KeyGenerator(String botSecret) {
        this.botSecret = botSecret;
    }
    public void generateKeys() throws NoSuchAlgorithmException, NoSuchProviderException {
        byte[] seed = botSecret.getBytes(StandardCharsets.UTF_8);

        // Ensure seed length is at least SEED_SIZE
        while (seed.length < SEED_SIZE) {
            seed = new BigInteger(1, seed).toString(16).getBytes(StandardCharsets.UTF_8);
            if (seed.length < SEED_SIZE) {
                seed = concatenateByteArrays(seed, seed);
            }
        }
        ByteArrayInputStream rand=createSeedReader(seed);
        KeyPairGenerator keyGen=KeyPairGenerator.getInstance("Ed25519","BC");
    }

    // Helper method to concatenate two byte arrays
    private static byte[] concatenateByteArrays(byte[] first, byte[] second) {
        byte[] result = Arrays.copyOf(first, first.length + second.length);
        System.arraycopy(second, 0, result, first.length, second.length);
        return result;
    }

    public ByteArrayInputStream createSeedReader(byte[] seed) {
        // ed25519.SeedSize等于32，代表种子的长度为32字节
        final int ED25519_SEED_SIZE = 32;

        // 检查seed数组长度是否足够
        if (seed == null || seed.length < ED25519_SEED_SIZE) {
            throw new IllegalArgumentException("Seed must be at least " + ED25519_SEED_SIZE + " bytes long.");
        }

        // 取出前32个字节作为种子
        byte[] seedBytes = new byte[ED25519_SEED_SIZE];
        System.arraycopy(seed, 0, seedBytes, 0, ED25519_SEED_SIZE);

        // 创建一个字节数组输入流
        return new ByteArrayInputStream(seedBytes);
    }

    // Method to get the public key
    public byte[] getPublicKey() {
        return publicKey;
    }

    // Method to get the private key
    public byte[] getPrivateKey() {
        return privateKey;
    }
}