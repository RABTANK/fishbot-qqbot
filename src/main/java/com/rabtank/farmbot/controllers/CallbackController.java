package com.rabtank.farmbot.controllers;

import org.springframework.web.bind.annotation.RequestBody;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.RestController;
import org.springframework.http.ResponseEntity;
import org.springframework.web.bind.annotation.*;

import java.util.Map;

@RestController
public class CallbackController {

    // 注意：这里使用 Map 来接收请求头信息，实际使用中你可以定义一个 POJO 类来更好地匹配你的请求头格式。
    @RequestMapping("/farmbot")
    public ResponseEntity<String> root(@RequestBody String requestBody, @RequestHeader Map<String, String> headers) {
        System.out.println("Request Body: " + requestBody);
        System.out.println("Request Headers:");
        for (Map.Entry<String, String> entry : headers.entrySet()) {
            System.out.println(entry.getKey() + ": " + entry.getValue());
        }
        // 可以返回一个简单的响应信息确认接收到数据
        return ResponseEntity.ok("Received request body and headers");
    }
}