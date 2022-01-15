package com.example.service;

import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Service;

import com.example.model.StaffModel;
import com.example.repository.StaffRepository;

@Service
public class StaffService {
    
    @Autowired
    StaffRepository staffRepository;

    public void addStaff(StaffModel staff) {
        staffRepository.addStaff(staff);
    }
}
