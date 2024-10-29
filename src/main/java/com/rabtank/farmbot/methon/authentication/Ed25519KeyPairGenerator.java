package com.rabtank.farmbot.methon.authentication;

import java.io.ByteArrayInputStream;
import java.io.IOException;
import java.math.BigInteger;
import java.security.*;

import org.bouncycastle.crypto.AsymmetricCipherKeyPair;
import org.bouncycastle.crypto.generators.HKDFBytesGenerator;
import org.bouncycastle.crypto.params.Ed25519PrivateKeyParameters;
import org.bouncycastle.crypto.params.Ed25519PublicKeyParameters;
import org.bouncycastle.jcajce.spec.EdDSAParameterSpec;
import org.bouncycastle.jce.provider.BouncyCastleProvider;
import org.bouncycastle.util.encoders.Hex;

public class Ed25519KeyPairGenerator {

    private static final int SEED_SIZE = 32; // Ed25519 Seed size in bytes

    private byte[] publicKey;
    private byte[] privateKey;

    public Ed25519KeyPairGenerator(String botSecret) throws NoSuchProviderException, NoSuchAlgorithmException, IOException, InvalidAlgorithmParameterException {
        Security.addProvider(new BouncyCastleProvider());

        // Ensure the seed is at least SEED_SIZE long by repeating it if necessary
        String seed = repeatToLength(botSecret, SEED_SIZE * 2); // Multiply by 2 to account for hex encoding
        byte[] seedBytes = Hex.decode(repeatToLength(seed, SEED_SIZE * 2));

        // Create a SecureRandom instance from the seed
        SecureRandom secureRandom = SecureRandom.getInstanceStrong();
        secureRandom.setSeed(seedBytes);

        // Initialize and generate the key pair
        KeyPairGenerator keyGen = KeyPairGenerator.getInstance("Ed25519", "BC");
        keyGen.initialize(new EdDSAParameterSpec("Ed25519"), secureRandom);
        KeyPair keyPair = keyGen.generateKeyPair();

        // Extract public and private keys
        this.publicKey = keyPair.getPublic().getEncoded();
        this.privateKey = keyPair.getPrivate().getEncoded();
    }

    private String repeatToLength(String str, int length) {
        StringBuilder sb = new StringBuilder(length);
        while (sb.length() < length) {
            sb.append(str);
        }
        return sb.toString();
    }

    public byte[] getPublicKey() {
        return publicKey;
    }

    public byte[] getPrivateKey() {
        return privateKey;
    }

    public static void main(String[] args) {
        try {
            Ed25519KeyPairGenerator generator = new Ed25519KeyPairGenerator("botSecret");
            System.out.println("Public Key: " + Hex.toHexString(generator.getPublicKey()));
            System.out.println("Private Key: " + Hex.toHexString(generator.getPrivateKey()));
        } catch (NoSuchProviderException | NoSuchAlgorithmException | IOException | InvalidAlgorithmParameterException e) {
            e.printStackTrace();
        }
    }
}