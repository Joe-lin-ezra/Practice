package com.example.repository;

import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.jdbc.core.JdbcTemplate;
import org.springframework.stereotype.Repository;

import com.example.model.StaffModel;

@Repository
public class StaffRepository {
    
    @Autowired
    private JdbcTemplate jdbcTemplate;

    public void addStaff(StaffModel staff) {
        System.out.println("Insert a new staff");
        jdbcTemplate.update("INSERT INTO memberaccount2019(PASSWORD, EMAIL, ADDRESS, CELLPHONE, CREATE_DATE) " + "VALUES (?, ?, ?, ?, NOW())",
            staff.getPassword(), staff.getEmail(), staff.getPosition(), staff.getPhone());
    }
}
