package com.example.demo;

import org.springframework.stereotype.Controller;
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.RequestMapping;

@Controller
@RequestMapping("/qq")
// @RequestMapping(value = "/qq", method = RequestMethod.GET)
public class SpringBootHelloWorld {

	public static void main(String[] args) {
		// TODO Auto-generated method stub

	}
	
	@GetMapping("/x")
	public String hello(){
		return "Hey, Spring Boot 的 Hello World !";
	}
	
	@GetMapping("/indexx")
	public String helloIndex(){
		return "index";
	}

}