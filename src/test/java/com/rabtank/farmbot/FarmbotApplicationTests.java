package com.rabtank.farmbot;

import com.rabtank.farmbot.methon.authentication.KeyGenerator;
import org.junit.jupiter.api.Test;
import org.springframework.boot.test.context.SpringBootTest;

@SpringBootTest
class FarmbotApplicationTests {
	KeyGenerator k;
	@Test
	void contextLoads() {
		k=new KeyGenerator("naOC0ocQE3shWLAfffVLB1rhYPG7");
		System.out.println(k.getPrivateKey());
		System.out.println(k.getPublicKey());
	}

}
