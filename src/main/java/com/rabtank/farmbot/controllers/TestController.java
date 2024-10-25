package com.rabtank.farmbot.controllers;

import org.springframework.http.MediaType;
import org.springframework.web.bind.annotation.PostMapping;
import org.springframework.web.bind.annotation.RequestBody;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.RestController;

@RestController
public class TestController {
    @PostMapping(value = "/farmbot/", consumes = MediaType.APPLICATION_JSON_VALUE)
    public String handleCallback(@RequestBody String callbackData) {
        System.out.println("Received callback data: " + callbackData);
        return "Callback received and printed.";
    }
    @RequestMapping("/hello")
    public String test2(){
        return "hello";
    }
}
