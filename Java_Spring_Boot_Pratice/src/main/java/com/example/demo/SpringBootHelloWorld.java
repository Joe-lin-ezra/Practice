package com.example.demo;

import org.springframework.stereotype.Controller;
import org.springframework.web.bind.annotation.GetMapping;

@Controller
// @RequestMapping(value = "", method = RequestMethod.GET)
public class SpringBootHelloWorld {

	public static void main(String[] args) {
		// TODO Auto-generated method stub

	}
	
	@GetMapping()
	public String demo() {
		return "Hello World";
	}

	@GetMapping("/indexx")
	public String hello() {
		return "index";
	}

}