package com.example.controller;

import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.web.bind.annotation.RestController;
import org.springframework.web.bind.annotation.RequestMapping;

import com.example.model.StaffModel;
import com.example.service.StaffService;

@RestController
public class StaffController {
    
    @Autowired
    StaffModel staffModel;
    @Autowired
    StaffService staffService;

    @RequestMapping("/addStaff")
    public String hello() {
        staffModel = new StaffModel();
        staffModel.setPassword("1234");
        staffModel.setEmail("email@email.com");
        staffModel.setPhone("22334455");
        staffModel.setPosition("Manager");
        staffService.addStaff(staffModel);
        return "New Staff added";
    }
}
