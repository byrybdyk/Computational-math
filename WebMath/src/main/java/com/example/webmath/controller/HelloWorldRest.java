package com.example.webmath.controller;

import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.RestController;
@RestController
public class HelloWorldRest {
    @GetMapping("/hello")
    public String hello() {
        return "Hello, World!";
    }
}
