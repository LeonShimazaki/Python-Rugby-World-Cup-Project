# Mock data of devices, staff, and loans at Epic software company
# Jane Karina
# jak0818@arastudent.ac.nz
# Please open and execute EpicDevices.sql for the tables of the database

USE EpicDevices;

Insert into Device Values ('01', 'Q Bert', 'Amazon Fire HD 7', 'Android', '4.5.5', '1 GB', 'Dual-Core 1.5GHz', '?', '800 x 1280 (216ppi)', 'Low', 'None', 'Tablet', '200', 'yes');
Insert into Device(deviceID, deviceName, deviceType, deviceOS, device, deviceCost, deviceActive) Values ('02', 'Pac Man', 'Chromebook', 'Windows', 'Laptop', '1000', 'yes');
Insert into Device(deviceID, deviceName, deviceType, deviceOS, device, deviceCost, deviceActive) Values ('03', 'Princess Zelda', 'Dell E 6400', 'Windows', 'Laptop', '1000', 'yes');
Insert into Device(deviceID, deviceName, deviceType, deviceOS, device, deviceCost, deviceActive) Values ('04', 'Link', 'Dell Laptop', 'Windows', 'Laptop', '1000', 'yes');
Insert into Device Values ('05', 'Bison', 'Galaxy S5', 'Android', '4.4.2', '2 GB', 'Quad-Core 2.5GHz', '?', ' 1080 x 1920 (432ppi)', 'Medium', 'None', 'Phone' , '700', 'yes');
Insert into Device Values ('06', 'Balrog', 'Galaxy S7 Edge', 'Android', '6.0.1', '4 GB', 'Octa-Core 4x2.3 GHz & 4x1.6', '?', '1440x2560 (534ppi)', 'High', 'None', 'Phone', '800', 'yes');
Insert into Device Values ('07', 'E-Honda', 'Galaxy Tab 1', 'Android', '4.0.4', '1 GB', 'Dual-Core 1GHz', '?', '800 x 1280 (149ppi)', 'Low', 'None', 'Tablet', '600', 'yes');
Insert into Device Values ('08', 'Zangief', 'Galaxy Tab 4', 'Android', '5.0.2', '1.5 GB', 'Dual-Core 1.2GHz', '?', '800 x 1280 (216ppi)', 'Low', 'None', 'Tablet', '1000', 'yes');
Insert into Device Values ('09', 'Guile', 'HTC One mini 2', 'Android', '4.4.2', '1 GB', 'Quad-Core 1.2GHz', '?', '720 x 1280 (326ppi)', 'Low', 'None', 'Phone', '200', 'yes');
Insert into Device Values ('10', 'Sonic', 'iPad 2', 'IOS', '8.4.1', '500 MB', 'Dual-Core 1GHz', '32', '768 x 1024 (132ppi)', 'Obsolete', '6745ece4fd066224e05129278e7eb75c562fea28', 'Tablet', '300', 'yes');
Insert into Device Values ('11', 'Dr Robotnik', 'iPad 4', 'IOS', '10.1', '1 GB', 'Dual-Core 1.4GHz', '32', '1536 x 2048 (264ppi)', 'Medium', '3e751193bdbf92b35a440f225318b5498de96c9e', 'Tablet', '400', 'yes');
Insert into Device Values ('12', 'Fox McCloud', 'iPad Air (retina)', 'IOS', '10.3.2', '1 GB', 'DUal-Core 1.3GHz', '64', '1536 x 2048 (264ppi)', 'Medium', '7c7a369fd078c67f1cc123685ad887d3e32a6552', 'Tablet', '800', 'yes');
Insert into Device Values ('13', 'Kratos', 'iPad Air 2', 'IOS', '9.3.4', '2 GB', 'Octa-Core 1.5GHz', '64', '2048 x 1536 (264ppi)', 'High', '0b7886a9d846ea7cd50f80c1eefbeba3ead44b21', 'Tablet', '1000', 'yes');
Insert into Device Values ('14', 'Silver', 'iPad Mini', 'IOS', '9.2', '500 MB', 'Dual-Core 1GHz', '32', '768 x 1024 (163ppi)', 'Obsolete', 'e73f9b4cb93e83f718622016e31d90c06692d782', 'Tablet', '400', 'yes');
Insert into Device Values ('15', 'Vector', 'iPad Mini', 'IOS', '8.4', '500 MB', 'Dual-Core 1GHz', '32', '768 x 1024 (163ppi)', 'Obsolete', 'fc4fde35ea28101e8a11f9a706c3fc4eff4537cf', 'Tablet', '400', 'yes');
Insert into Device Values ('16', 'Espio', 'iPad Mini 2 (retina)', 'IOS', '11.2', '1 GB', 'Dual-Core 1.3GHz', '64', '1536 x 2048 (324ppi)', 'Low', '7ecfbae1544a8d56ccdacd6dc27ed9038196b2f5', 'Tablet', '600', 'yes');
Insert into Device Values ('17', 'Knuckles', 'iPad Mini 2 (retina)', 'IOS', '10 Beta 2', '1 GB', 'Dual-Core 1.3GHz', '64', '1536 x 2048 (324ppi)', 'Low', '82b93d029411bbede53c16523c7f6c58054e526b', 'Tablet', '600', 'yes');
Insert into Device Values ('18', 'Max Payne', 'iPad Mini 4', 'IOS', '10.1', '2 GB', 'Quad-Core 1.5GHz', '64', '2048 x 1536 (326ppi)', 'High', '03d9afd06672d3db910b3330f88d68290119022a', 'Tablet', '800', 'yes');
Insert into Device Values ('19', '???', 'iPad Pro', 'IOS', '11.1', '4 GB', 'Hexa-Core 2.39GHz', '64', '2224 x 1668', 'High', '193ea81981bbc3ea8535688ea1c8b5f6eaa4514e', 'Tablet', '1000', 'yes');
Insert into Device Values ('20', 'Barret', 'iPhone 4', 'IOS', '7.1.2', '500 MB', 'Single-Core 1GHz', '32', '640 x 960 (330ppi)', 'Obsolete', '40b7c83097b9a803b38b193f97124f21682653a4', 'Phone', '300', 'yes');
Insert into Device Values ('21', 'Vincent', 'iPhone 4s', 'IOS', '8.4.0', '500 MB', 'Dual-Core 1GHz', '32', '640 x 960 (326ppi)', 'Obsolete', '369fcdf892d01f490215c4d9e0f2570d707c2f8a', 'Phone', '450', 'yes');
Insert into Device Values ('22', 'Basch', 'iPhone 5', 'IOS', '10.0.1', '1 GB', 'Dual-Core 1.3GHz', '32', '640 x 1136 (326ppi)', 'Low', '086deb3ff832fe09fc492d835f8f539d853a70d5', 'Phone', '500', 'yes');
Insert into Device Values ('23', 'Karen', 'iPhone 5s', 'IOS', '11.1.1', '1 GB', 'Dual-Core 1.3GHz', '64', '640 x 1136 (326ppi)', 'Low', '11c7581c85ca118915b345a2da4fb558bce0cdb7', 'Phone', '550', 'yes');
Insert into Device Values ('24', 'Squall', 'iPhone 6', 'IOS', '10.3.2', '1 GB', 'Dual-Core 1.4GHz', '64', '750 x 1334 (326ppi)', 'Medium', 'a3eb076b6f1d46fa40c3661ed928592df544b945', 'Phone', '600', 'yes');
Insert into Device Values ('25', 'Cid', 'iPhone 6+', 'IOS', '11.2', '1 GB', 'Dual-Core 1.4GHz', '64', '1080 x 1920 (401ppi)', 'Medium', '9cda2720c72ff3e26e82e49ea796c8a4f9246f8e', 'Phone', '650', 'yes');
Insert into Device Values ('26', 'Fran', 'iPhone 6S', 'IOS', '11.2.2', '2 GB', 'Dual-Core 1.85GHz', '64', '1334 x 750 (326ppi)', 'High', '49c2e825d69a758ff9379dd1ba0b9c24913f645e', 'Phone', '650', 'yes');
Insert into Device Values ('27', 'Mr Bones', 'iPhone 7', 'IOS', '10.3.3', '2 GB', 'quad-Core 2.34GHz', '64', '750 x 1334 (326ppi)', 'High', '702c1adf30db79fd37da10e5866eb63157ef7356', 'Phone', '700', 'yes');
Insert into Device Values ('28', 'Lara Croft', 'iPhone 7+', 'IOS', '10.3.2', '3 GB', 'Quad-Core 2.34GHz', '64', '1920 x 1080 (401ppi)', 'High', 'f65ca802c90c9f80669fb4f18d8aa422da594875', 'Phone', '750', 'yes');
Insert into Device Values ('29', 'Mr Pricklepants', 'iPhone 7+', 'IOS', '11.1.2', '3 GB', 'Quad-Core 2.34GHz', '64', '1920 x 1080 (401ppi)', 'Medium', '788e06f1bf0c9da090d5c51ad15034e699f793ce', 'Phone', '750', 'yes');
Insert into Device(deviceID, deviceName, deviceType, deviceOS, OSVersion, deviceRam, deviceCPU, deviceBit, deviceResolution, deviceGrade, device, deviceCost, deviceActive) Values ('30', 'Seifer', 'iPhone 8', 'IOS', '11.0.3', '2 GB', 'Hexa-Core 2.39 GHz', '64', '750 x 1334 (326ppi)', 'High', 'Phone', '800', 'yes');
Insert into Device Values ('31', 'Mr X', 'iPhone X', 'IOS', '11.1.2', '3 GB', 'Hexa-Core 2.39GHz', '64', '2436 x 1125 (458ppi)', 'High', '903e2d8c7291d8d3d386a3a0886f21d969704b54', 'Phone', '2000', 'yes');
Insert into Device Values ('32', 'Gordon Freeman', 'iPod 5', 'IOS', '9.3.5', '500 MB', 'Dual-Core 1GHz', '32', '640 x 1136 (326ppi)', 'Obsolete', '8df683d2213df8bffdb6f8157e38c8b41809fb69', 'Music', '100', 'yes');
Insert into Device(deviceID, deviceName, deviceType, deviceOS, OSVersion, deviceRam, deviceCPU, deviceBit, deviceResolution, deviceGrade, device, deviceCost, deviceActive) Values ('33', 'Guy Brush', 'iPod 5', 'IOS', '9', '500 MB', 'Dual-Core 1GHz', '32', '640 x 1136 (326ppi)', 'Obsolete', 'Music', '100', 'yes');
Insert into Device Values ('34', 'Iggy', 'iPod 5', 'IOS', '8.4.1', '500 MB', 'Dual-Core 1GHz', '32', '640 x 1136 (326ppi)', 'Obsolete', 'ba9ff54ef1d18b27feb179271c49f90a6d813531', 'Music', '100', 'yes');
Insert into Device Values ('35', 'John Marston', 'iPod 5', 'IOS', '8.3.0', '500 MB', 'Dual-Core 1GHz', '32', '640 x 1136 (326ppi)', 'Obsolete', '53ddbab0034331cab54858dd980906cbb457367f', 'Music', '100', 'yes');
Insert into Device Values ('36', 'Lemmy', 'iPod 5', 'IOS', '9.0.2', '500 MB', 'Dual-Core 1GHz', '32', '640 x 1136 (326ppi)', 'Obsolete', 'd4b31d4fef7b969148b9493b32cd53ffa280bf3a', 'Music', '100', 'yes');
Insert into Device Values ('37', 'Toad', 'iPod 5', 'IOS', '8.1.1', '500 MB', 'Dual-Core 1GHz', '32', '640 x 1136 (326ppi)', 'Obsolete', '0395cc76b2f123d2debb5db2d26a8e4b44d44218', 'Music', '100', 'yes');
Insert into Device Values ('38', 'Slippy Toad', 'iPod 6', 'IOS', '10.3', '1 GB', 'Dual-Core 1.4GHz', '64', '750 x 1334 (326ppi)', 'Low', 'cdc1507bc464102fb7321e72273b58d3bee8a6c5', 'Music', '120', 'yes');
Insert into Device Values ('39', 'King', 'Kindle Fire HD', 'Android', '?', '1 GB', 'Dual-Core 1.5GHz', '?', '1200 x 1920 (254ppi)', 'Low', 'None', 'Tablet', '400', 'yes');
Insert into Device Values ('40', 'Glados', 'LG G Pad', 'Android', '4.4.2', '2 GB', 'Quad-Core 1.7GHz', '?', '1200 x 1920 (273ppi)', 'Medium', 'None', 'Tablet', '400', 'yes');
Insert into Device Values ('41', 'Wheatley', 'LG G3', 'Android', '5.0.0', '3 GB', 'QUad-Core 2.5GHz', '?', '1440 x 2560 (538ppi)', 'Medium', 'None', 'Phone', '400', 'yes');
Insert into Device Values ('42', 'Ken', 'Nexus 10', 'Android', '4.4.4', '2 GB', 'Dual-Core 1.7GHz', '?', '1600 x 2560 (259ppi)', 'Low', 'None', 'Tablet', '1000', 'yes');
Insert into Device Values ('43', 'Blanka', 'Nexus 7', 'Android', '5.0.2', '1 GB', 'Quad-Core 1.2GHz', '?', '800 x 1280 (216ppi)', 'Low', 'None', 'Tablet', '700', 'yes');
Insert into Device Values ('44', 'Roach', 'Nexus 9', 'Android', '7 Preview', '2 GB', 'Dual-Core 2.3GHz', '?', '1536 x 2048 (281ppi)', 'Medium', 'None', 'Tablet', '900', 'yes');
Insert into Device(deviceID, deviceName, deviceType, deviceOS, device, deviceCost, deviceActive) Values ('45', '???', 'Rift', 'VR', 'VR', '2000', 'yes');
Insert into Device Values ('46', 'Akuma', 'Samsung Tab A', 'Android', '5.0.2', '2 GB', 'Quad-Core 1.2GHz', '?', '768 x 1024 (132ppi)', 'Low', 'None', 'Tablet', '1500', 'yes');
Insert into Device(deviceID, deviceName, deviceType, deviceOS, device, deviceCost, deviceActive) Values ('47', 'Batman', 'Vive', 'VR', 'VR', '2000', 'yes');
Insert into Device(deviceID, deviceName, deviceType, deviceOS, device, deviceCost, deviceActive) Values ('48', 'Superman', 'Vive', 'VR', 'VR', '2000', 'yes');
Insert into Device(deviceID, deviceName, deviceType, deviceOS, OSVersion, deviceRam, deviceCPU, deviceResolution, deviceGrade, device, deviceCost, deviceActive) Values ('49', 'Kuma', 'W8 Nokia', 'Windows', '8.1', '500 MB', 'Dual-Core 1GHz', '480 x 800 (233ppi)', 'Low', 'Phone', '300', 'yes');
Insert into Device(deviceID, deviceName, deviceType, deviceOS, OSVersion, deviceRam, deviceCPU, deviceResolution, deviceGrade, device, deviceCost, deviceActive) Values ('50', 'Gun Jack', 'W8 Surface', 'Windows', '?', '2 GB', 'Quad-Core 1.3GHz', '768 x 1366 (148ppi)', 'Low - Mid', 'Laptop', '1500', 'yes');

Insert into Staff Values ('01', 'Jane', 'Karina', 'Epic', 'jkarina@epic.com', 'Manager', 'yes');
Insert into Staff Values ('02', 'Aidan', 'Watson', 'Signal', 'awatson@epic.com', 'Manager', 'yes');
Insert into Staff Values ('03', 'Leon', 'Shimazaki', 'Epic', 'lshimazaki@epic.com', 'Employee', 'yes');
Insert into Staff Values ('04', 'Ajiteru', 'Tunde', 'Signal', 'atunde@epic.com', 'Employee', 'yes');
Insert into Staff Values ('05', 'Carl', 'Sagan', 'Signal', 'csagan@epic.com', 'Employee', 'yes');
Insert into Staff Values ('06', 'Sonam', 'Kim', 'Epic', 'skim@epic.com', 'Employee', 'yes');
Insert into Staff Values ('07', 'Amol', 'Sears', 'Epic', 'asears@epic.com', 'Employee', 'yes');

Insert into Loan Values ('01', '05', '2019-05-01 07:00:00', '2019-05-20 07:00:00', '1980-01-01 00:00:01');
Insert into Loan Values ('03', '06', '2019-04-21 07:00:00', '2019-05-21 07:00:00', '1980-01-01 00:00:01');
Insert into Loan Values ('06', '06', '2019-04-30 07:00:00', '2019-05-30 07:00:00', '1980-01-01 00:00:01');
Insert into Loan Values ('13', '06', '2019-05-05 07:00:00', '2019-06-05 07:00:00', '1980-01-01 00:00:01');
Insert into Loan Values ('26', '06', '2019-05-07 07:00:00', '2019-06-07 07:00:00', '1980-01-01 00:00:01');
Insert into Loan Values ('46', '07', '2019-05-11 07:00:00', '2019-06-11 07:00:00', '1980-01-01 00:00:01');
Insert into Loan Values ('47', '07', '2019-05-12 07:00:00', '2019-06-12 07:00:00', '2019-05-27 07:00:00');
Insert into Loan Values ('50', '05', '2019-04-20 07:00:00', '2019-05-20 07:00:00', '2019-05-27 07:00:00');

Insert into Hold Values ('01', '01', '2019-04-20 07:00:00');
Insert into Hold Values ('01', '02', '2019-04-21 07:00:00');
Insert into Hold Values ('10', '02', '2019-04-21 07:00:00');
Insert into Hold Values ('05', '06', '2019-04-19 07:00:00');
Insert into Hold Values ('05', '05', '2019-04-20 07:00:00');
Insert into Hold Values ('01', '03', '2019-04-19 07:00:00');
Insert into Hold Values ('02', '03', '2019-04-19 07:00:00');

#random Queries
/*SELECT deviceID, staffID, holdDate FROM Hold WHERE staffID = '5' ORDER BY holdDate ASC LIMIT 1;
SELECT staffID, holdDate FROM Hold WHERE deviceID = '1' ORDER BY holdDate;
SELECT * FROM Loan WHERE loanReturned = '1980-01-01 00:00:01';
SELECT deviceID FROM Loan WHERE deviceID = '1' AND loanReturned = '1980-01-01 00:00:01';
SELECT * FROM Hold;

select device.*, Loan.staffID, min(loanReturned), hold.staffID from device left join Loan on Loan.deviceID = device.deviceID and loanReturned = '1980-01-01 00:00:01' left join Hold on Device.deviceID = Hold.DeviceID and Hold.holddate = (select holdDate from hold where hold.deviceID = device.deviceID and holddate = (select min(holddate) from hold where hold.deviceID= device.deviceID))group by device.deviceID;

SELECT device.deviceID, Hold.staffID FROM Device LEFT JOIN Hold ON Device.deviceID = Hold.deviceID;
SELECT device.deviceID, deviceName, deviceType, deviceOS, date_format(expiryDate, '%e %M %Y, %h:%i %p') FROM Device LEFT Join Loan on device.deviceID = loan.deviceID WHERE staffID = '5' AND loanReturned = '1980-01-01 00:00:01' GROUP BY device.deviceID;

SELECT * FROM Loan WHERE staffID = '1' GROUP BY deviceID;
SELECT DISTINCT device.deviceID, deviceName, deviceType, deviceOS, OSVersion, deviceRam, deviceCPU, deviceBit, deviceResolution, deviceGrade, deviceUUID, MAX(loanReturned), deviceCost, device, Loan.staffID, loanReturned FROM Device LEFT JOIN Loan on Device.deviceID = Loan.deviceID LEFT JOIN Hold on Device.deviceID = Hold.deviceID AND Hold.deviceID = Loan.deviceID GROUP BY device.deviceID;

/*UPDATE Loan SET loanReturned = now() WHERE deviceID = '1' and loanReturned = '1980-01-01 00:00:01';
SELECT * FROM Loan;

SELECT hold.deviceID, deviceName, deviceType, deviceOS, date_format(holdDate, '%e %M %Y, %h:%i %p') FROM Device LEFT Join Loan on device.deviceID = loan.deviceID Left Join hold on device.deviceID = hold.deviceID  where hold.staffID = '2' GROUP BY device.deviceID;
SELECT DISTINCT device.deviceID, deviceName, deviceType, deviceOS, OSVersion, deviceRam, deviceCPU, deviceBit, deviceResolution, deviceGrade, deviceUUID, MAX(loanReturned), deviceCost, device, loanReturned FROM Device LEFT JOIN Loan on device.deviceID = loan.deviceID GROUP BY device.deviceID;

SELECT * FROM Loan;
SELECT loanReturned FROM Loan WHERE deviceID = '1' ORDER BY loanDate DESC LIMIT 1;
SELECT deviceID, device FROM Device;
SELECT deviceID, deviceCost FROM Device Where deviceCost = "100";

SELECT * FROM Device;
SELECT * FROM Staff;
SELECT * FROM Loan;
SELECT * FROM Hold WHERE deviceID = '1' ORDER BY holdDate;

/*
SELECT Device.deviceID, deviceName, deviceType, deviceOS
FROM Device
LEFT JOIN Loan ON Device.deviceID = Loan.deviceID
WHERE NOT device.deviceID IN (SELECT Loan.deviceID FROM Loan)
ORDER BY device.deviceID;

SELECT staffFName, staffLName, staffID, staffLocation FROM Staff ORDER BY staffID DESC LIMIT 1;

SELECT staffID, concat(staffFName, ' ', staffLName) AS StaffName, staffEmail, staffLocation
FROM Staff
ORDER BY staffID;

SELECT COUNT(deviceID) FROM Loan  WHERE deviceID = "3" GROUP BY deviceID;

DELETE FROM Loan WHERE deviceID = "01";

SELECT * FROM Hold;

SELECT Hold.deviceID, deviceName, concat(staffFName, ' ', staffLName) AS Staff, date_format(holdDate, '%e %M %Y, %h:%i %p') FROM Device, Staff, Hold WHERE Hold.deviceID = Device.deviceID AND Hold.staffID = Staff.staffID;

SELECT COUNT(deviceID) FROM Hold WHERE deviceID = '01' AND staffID = '01';
