# Database tables for devices at Epic software company
# Jane Karina
# jak0818@arastudent.ac.nz
# Please open and execute EpicDevicesData.sql for mock data to add into the database

#Drop database EpicDevices;
CREATE DATABASE IF NOT EXISTS EpicDevices;
USE EpicDevices;

CREATE TABLE Device (
	deviceID int auto_increment primary key,
	deviceName varchar(20),
    deviceType varchar (30),
    deviceOS varchar (10),
    OSVersion varchar (10),
    deviceRam varchar (7),
    deviceCPU varchar (30),
    deviceBit varchar (2),
    deviceResolution varchar (30),
    deviceGrade varchar (10),
    deviceUUID varchar (50),
    device varchar (20),
    deviceCost varchar (10),
    deviceActive varchar(3)
);

CREATE TABLE Staff (
	staffID int auto_increment primary key,
    staffFName varchar (15),
    staffLName varchar (15),
    staffLocation varchar (20),
    staffEmail varchar (25),
    role varchar (25),
    staffActive varchar (3)
);

CREATE TABLE Loan (
	deviceID int auto_increment,
    staffID int,
    loanDate timestamp,
    expiryDate timestamp NULL,
    loanReturned timestamp NULL,
    foreign key (deviceID) references Device (deviceID),
    foreign key (staffID) references Staff (staffID)
);

CREATE TABLE Hold (
	deviceID int,
    staffID int,
    holdDate timestamp,
    primary key (deviceID, staffID),
    foreign key (deviceID) references Device (deviceID),
    foreign key (staffID) references Staff (staffID)
);
