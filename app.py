# app.py as an intermediary between Epic Devices database and the website

from flask import Flask, render_template, request, redirect, session
import mysql.connector
import datetime
from datetime import datetime as DateTime, timedelta as TimeDelta
from datetime import timedelta

#configure db
mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    passwd="password",
    database="EpicDevices"
)

app = Flask(__name__)

#placeholders
successmsg=""
count = 0
Manager = False

#Shortcut for Device List
def devices():
    mycursor = mydb.cursor()
    result = mycursor.execute("SELECT * FROM Device;")
    device = mycursor.fetchall()
    mydb.commit()
    mycursor.close()
    return device

#Shortcut for Available devices
def av_devices():
	mycursor = mydb.cursor()
	result = mycursor.execute(
            "SELECT device.*, Loan.staffID, min(loanReturned), hold.staffID, a.staffLocation, \
            concat(a.staffFName ,' ', a.staffLName) AS LoanName, concat(b.staffFName ,' ', b.staffLName) AS HoldName \
            FROM device \
            left join Loan on Loan.deviceID = device.deviceID and loanReturned = '1980-01-01 00:00:01'\
            left join Hold on Device.deviceID = Hold.DeviceID and Hold.holddate = \
            (select holdDate from hold where hold.deviceID = device.deviceID and holddate = (select min(holddate) from hold where hold.deviceID= device.deviceID)) \
            left join Staff a on a.staffID = Loan.StaffID \
            left join staff b on b.staffID = hold.staffID \
            where deviceActive = 'yes' group by device.deviceID")
	device = mycursor.fetchall()
	mydb.commit()
	mycursor.close()
	return device

#Shortcut for Hold queue	
def hold_queue(ID):
	mycursor = mydb.cursor()
	result = mycursor.execute(
            "SELECT hold.deviceID, hold.staffID, date_format(holdDate, '%e %M %Y, %h:%i %p'), concat(staff.staffFName ,' ', staff.staffLName) AS FullName \
            FROM hold inner join staff on hold.staffID = staff.staffID where deviceID = {} order by holdDate".format(ID))
	hold = mycursor.fetchall()
	mydb.commit()
	mycursor.close()
	return hold	

#Shortcut for staff devices
def sta_devices(ID):
	mycursor = mydb.cursor()
	result = mycursor.execute(
            "SELECT device.deviceID, deviceName, deviceType, deviceOS, date_format(expiryDate, '%e %M %Y, %h:%i %p') \
            FROM Device LEFT Join Loan on device.deviceID = loan.deviceID WHERE staffID = {} AND loanReturned = '1980-01-01 00:00:01' GROUP BY device.deviceID;".format(ID))
	device = mycursor.fetchall()
	mydb.commit()
	mycursor.close()
	return device

#Shortcut for staff current held devices
def staheld_devices(ID):
	mycursor = mydb.cursor()
	result = mycursor.execute(
            "SELECT device.deviceID, deviceName, deviceType, deviceOS, date_format(holdDate, '%e %M %Y, %h:%i %p') \
            FROM Device LEFT Join Loan on device.deviceID = loan.deviceID Left Join hold on device.deviceID = hold.deviceID  where hold.staffID = {} \
            GROUP BY device.deviceID".format(ID))
	print(ID)
	held = mycursor.fetchall()
	mydb.commit()
	mycursor.close()
	return held

#Shortcut for 1 specific device
def spe_device(ID):
	mycursor = mydb.cursor()
	result = mycursor.execute("SELECT * from device where deviceID = {}".format(ID))
	device = mycursor.fetchall()
	mydb.commit()
	mycursor.close()
	return device
    
#Shortcut for Full Staff list
def staff_list():
	mycursor = mydb.cursor()
	result = mycursor.execute("SELECT concat(staffFName ,' ', staffLName) AS FullName, staffID FROM Staff WHERE staffActive = 'yes'")
	staff = mycursor.fetchall()
	mydb.commit()
	mycursor.close()
	return staff

#Shortcut for Specific Staff member info
def spe_staff(ID):
	mycursor = mydb.cursor()
	result = mycursor.execute("SELECT concat(staffFName ,' ', staffLName) AS FullName, staffID, role FROM Staff where staffID = {}".format(ID))
	staff = mycursor.fetchall()
	mydb.commit()
	mycursor.close()
	return staff

#############################
####Index/Home/Device page###
#############################
@app.route('/', methods=['GET', 'POST'])
def main():
    mycursor = mydb.cursor()
    av_devices()
    device = av_devices()
    #print(device)
    staff_list()
    staff = staff_list()
    mydb.commit()
    #Only Manager can see hidden functions
    global Manager
    manager = False
    if request.method == 'POST':
        global count
        holdAvailable = ""
        #Semi Login System
        if count == 0:
            try:
                Staffdetails = request.form
                sta_id = int(Staffdetails['ID'])
                if sta_id == 0:
                    error = "Please select a user!"
                    return render_template('index.html', device = device, staff = staff, count = count, error = error)  
                mycursor = mydb.cursor()
                av_devices()
                device = av_devices()
                staff_list()
                staff = staff_list()
                mydb.commit()
                spe_staff(sta_id)
                ind = (spe_staff(sta_id)[0][0])
                indID = (spe_staff(sta_id)[0][1])
                role = (spe_staff(sta_id)[0][2])
                if role == "Manager":
                    Manager = True
                #print(ind)
                count = 1
                holdStatus = ""
                mycursor.execute("SELECT deviceID FROM Hold WHERE staffID = %s ORDER BY holdDate",(sta_id,))
                #gets the devices that the user has on hold
                checkHold = mycursor.fetchall()
                if len(checkHold) > 0:
                    loanAvailable = []
                    #checks if any of those devices have been returned
                    for y in checkHold:
                        mycursor.execute("SELECT deviceID FROM Loan WHERE deviceID = %s AND loanReturned = '1980-01-01 00:00:01'",(y[0],))
                        checkLoanUser = mycursor.fetchall()
                        if len(checkLoanUser) == 0:
                            loanAvailable.append(y[0])
                    if len(loanAvailable) > 0:
                        holdAvailable = []
                        #check who has the first hold on device & check if it is current user
                        for x in loanAvailable:
                            mycursor.execute("SELECT staffID FROM Hold WHERE deviceID = %s ORDER BY holdDate ASC LIMIT 1",(x,))
                            checkHoldUser = mycursor.fetchall()
                            #checks which user is first in queue for item
                            if (checkHoldUser[0][0] == sta_id):
                                holdAvailable.append(x)
                            #holdAvailable holds all the devices that the current user has put on hold & can now loan out
                        if len(holdAvailable) > 0:
                            holdStatus = ("You can now loan out your held devices, ID:")
                return render_template('index.html', device = device, staff = staff, ind = ind, sta_id = sta_id, manager = Manager, \
                                       holdStatus = holdStatus, holdAvailable = holdAvailable, count = count)
            except:
                return render_template('index.html', device = device, staff = staff, manager = Manager, count = count)
            
        #Logged into a User
        else:
            try:
                id = request.args.get('SID')
                sta_devices(id)
                device = sta_devices(id)
                mycursor = mydb.cursor()
                result = mycursor.execute("SELECT * FROM staff where staffID = {}".format(id))
                staff = mycursor.fetchall()
                print(device)
                if len(device) != 0:
                    count = 0
                    manager = False
                    return render_template('staffmem.html', staff = staff, device = device, sta_id = sta_id, manager = Manager)
                else:
                    count = 0
                    manager = False
                    errormsg = "No current loans for that staff member"
                    return render_template('staffmem.html',error=errormsg, staff = staff, device = device, manager = Manager)
            except:
                count = 0
                print ("no selection made")
                return render_template('index.html', device = device, staff = staff, manager = Manager, count = count)
    else:
        count = 0
        return render_template('index.html', device = device, staff = staff, manager = manager, count = count)

#Specific Details of Devices
#Confirming loan/hold/return
@app.route('/confirm', methods=['GET', 'POST'])
def confirm():
    did = request.args.get('DID')
    sid = request.args.get('SID')
    status = request.args.get('ST')
    t = DateTime.today()
    date_now = t.strftime("%d-%b-%Y")
    x = t + TimeDelta(days=3)
    if request.method == 'POST':
        dreturn = request.form
        ret_date = dreturn['return_date']
        comma = ","
        first_com = ret_date.find(comma)
        date_return = ret_date[:first_com]
        time_str = ret_date[first_com: ]             
        change = True
    else:    
        date_return = x.strftime("%d-%b-%Y")
        change = False
    y = datetime.datetime.now()
    time = (y.strftime("%I:%M:%p"))
    spe_staff(sid)
    staff = spe_staff(sid)
    if staff[0][2] == "Manager":
        global Manager
        Manager = True
    mycursor = mydb.cursor()
    result = mycursor.execute("SELECT * FROM Device where deviceID = {}".format(did))
    dev = mycursor.fetchall()
    result2 = mycursor.execute(
        "SELECT device.deviceID, deviceName, deviceType, deviceOS, OSVersion, deviceRam, deviceCPU, deviceBit, deviceResolution, deviceGrade, deviceUUID, expiryDate \
        FROM Device LEFT Join Loan on device.deviceID = loan.deviceID where device.deviceID = {}".format(did))
    dev2 = mycursor.fetchall()
    print (dev2[0][11])
    mycursor.execute("SELECT concat(staffFName, ' ', staffLName)\
                        AS Staff, date_format(loanDate, '%e %M %Y, %h:%i %p'), date_format(expiryDate, '%e %M %Y, %h:%i %p'), expiryDate+0, Now()+0\
                        from Loan\
                        Inner join Device on Loan.deviceID = Device.deviceID\
                        Inner join staff on Loan.staffID = Staff.staffID\
                        Where loan.deviceID= {} AND loanReturned = '1980-01-01 00:00:01'".format(did))
    showLoan = mycursor.fetchall();
    hold_queue(did)
    showHold = hold_queue(did)
    return render_template('confirm.html',dev = dev, dev2 = dev2, showLoan = showLoan, status = status, staff = staff, \
                           date_now = date_now, date_return = date_return, time = time, manager = Manager, showHold = showHold, change = change)

#Page for Staff list
@app.route('/stafflist', methods=['GET', 'POST'])
def stafflist():
    global Manager
    Manager = False
    mycursor = mydb.cursor()
    result = mycursor.execute("SELECT staffID, concat(staffFName, ' ', staffLName) AS StaffName, staffEmail, role, staffLocation \
                                FROM Staff WHERE staffActive = 'yes' ORDER BY staffID")
    staffList = mycursor.fetchall()
    return render_template('stafflist.html',staffList = staffList, manager = Manager)

#Page for Staff infomation. e.g. Loans/Holds
@app.route('/staffmem', methods=['GET', 'POST'])
def staffmem():
    global Manager
    Manager = False
    sid = request.args.get('SID')
    did = request.args.get('DID')
    ret_date = request.args.get('T')
    success = ""
    status = request.args.get('ST')
    y = datetime.datetime.now()
    time = (y.strftime("%H:%M:%S"))
    mycursor = mydb.cursor()
    result = mycursor.execute("SELECT * FROM staff where staffID = {}".format(sid))
    staff = mycursor.fetchall()
    if status == "L":
        date_str = ret_date
        mycursor = mydb.cursor()
        t = DateTime.today()
        date_now = t.strftime("%d-%b-%Y")
        x = t + TimeDelta(days=3)
        cor_dat_format = DateTime.strptime(date_str,("%d-%b-%Y"))
        print (cor_dat_format)
        date_return = cor_dat_format.strftime("%Y-%m-%d")
        print (date_return)    
        mycursor.execute("SELECT loanReturned FROM Loan WHERE deviceID = %s ORDER BY loanDate DESC LIMIT 1", (did,))
        checkLoan = mycursor.fetchall()
        print (checkLoan)
        if len(checkLoan) > 0:
            print (str(checkLoan[0]))
            print (str(checkLoan[0]) == '(datetime.datetime(1980, 1, 1, 0, 0, 1),)')
            if (str(checkLoan[0]) == '(datetime.datetime(1980, 1, 1, 0, 0, 1),)'):
                errormsg = ("This item is currently on loan! You need to hold it instead.")
                return render_template('staffmem.html',error=errormsg, staff = staff)
        #check if device is on hold by someone
        mycursor.execute("SELECT deviceID FROM Hold WHERE deviceID = %s", (did,))
        checkDeviceHold = mycursor.fetchall()
        #check if device on hold is by the current user & can be loaned out
        if len(checkDeviceHold) > 0:
            mycursor.execute("SELECT staffID FROM Hold WHERE deviceID = %s ORDER BY holdDate", (did,))
            checkUserHold = mycursor.fetchall()
            if (checkUserHold[0][0] != int(sid)):
                errormsg = ("This item is on hold for someone else! You need to hold it instead.")
                return render_template('staffmem.html',error=errormsg, staff = staff)
            #if user can now take out device that they put on hold earlier
            elif (checkUserHold[0][0] == int(sid)):
                mycursor.execute("DELETE FROM Hold WHERE deviceID = %s AND staffID = %s", (did, sid,))
        mycursor.execute("Insert into Loan(deviceID, staffID, loanDate, expiryDate, loanReturned) \
                        Values (%s, %s, NOW(), %s %s %s, '1980-01-01 00:00:01')", (did, sid, date_return, " ", time))
        spe_device(did)
        loan_device = spe_device(did)[0][1]
        mydb.commit()
        success = "You have loaned out {}. Please ensure that the device has been returned before or on the return date.".format(loan_device)
    elif status == "R":
        mycursor.execute("UPDATE Loan SET loanReturned = now() WHERE deviceID = %s AND loanReturned = '1980-01-01 00:00:01'", (did,))
        spe_device(did)
        ret_device = spe_device(did)[0][1]
        mydb.commit()
        #Success
        success=""
        success = "You have successfully returned this Device"
        success = "You have returned {}. Please ensure that the device has been returned to the device table.".format(ret_device)
    elif status == "H":
        try:
            mycursor.execute("Insert into Hold (deviceID, staffID, holdDate) Values (%s, %s, NOW())", (did, sid))
            mydb.commit()
            success = "You have placed a hold on this item."
        except:
            success = "You already have a hold placed on this item! Please wait until it has been returned."
    elif status == "CH":
        try:
            mycursor.execute("DELETE FROM Hold WHERE deviceID = %s AND staffID = %s", (did, sid,))
            mydb.commit()
            success = "You have cancelled your hold on this device."
        except:
            print ("cannot cancel hold")
    sta_devices(sid)
    device = sta_devices(sid)
    staheld_devices(sid)
    held = staheld_devices(sid)
    mycursor = mydb.cursor()
    result = mycursor.execute("SELECT * FROM staff where staffID = {}".format(sid))
    staff = mycursor.fetchall()
    if len(device) != 0 or len(held) != 0:
        if len(device) != 0 and len(held) == 0:
            no_hold = "No current holds for this staff member"

            return render_template('staffmem.html',staff = staff, device = device, held = held, no_hold = no_hold, manager = Manager, success = success)
        elif len(held) != 0 and len(device) == 0 :
            no_loan = "No current loans for this staff member"
            return render_template('staffmem.html',staff = staff, device = device, held = held, no_loan = no_loan, manager = Manager, success = success)

        else:
            return render_template('staffmem.html', staff = staff, device = device, held = held, manager = Manager, success = success)
    else:
        errormsg = "No current loans or holds for this staff member"

        return render_template('staffmem.html',error=errormsg, staff = staff, device = device, held = held, manager = Manager, success = success)

#Page for adding a New Staff to database
@app.route('/newstaff', methods=['GET', 'POST'])
def newstaff():
    mycursor = mydb.cursor()
    global Manager
    Manager = True
    if request.method == 'POST':
        Staffdetails = request.form
        firstname = Staffdetails['staffFName'].capitalize().strip()
        lastname = Staffdetails['staffLName'].capitalize().strip()
        email = Staffdetails['staffEmail']
        role = Staffdetails['role']
        location = Staffdetails['staffLocation']
        #Error Handling
        errormsg=""
        if not (firstname.isalpha() and lastname.isalpha()):
                errormsg = "Name must contain alphabets only. \n"
        if not (lastname.count("", 0,-1) < 100 or firstname.count("", 0,-1) < 100):
                errormsg = errormsg + "Name cannot include more than 100 characters. \n"
        if (lastname.count("", 0,-1) == 1 or firstname.count("", 0,-1) == 1):
                errormsg = errormsg + "Name must be more than 1 character long. \n"
        if errormsg != "":
                return render_template('newstaff.html', error=errormsg, manager = Manager)
        #Successful Insert of New Staff
        try:
                mycursor = mydb.cursor()
                mycursor.execute("INSERT INTO Staff (staffFName, staffLName, staffEmail, role, staffLocation, staffActive) VALUES(%s, %s, %s, %s, %s, 'yes')",(firstname, lastname, email, role, location))
                mydb.commit()
                #Success
                successmsg=""
                successmsg = "You have successfully added a Staff member"
                #show user ID on success
                mycursor = mydb.cursor()
        except:
                errormsg="One of the fields is not correctly formatted - please try again"
                return render_template('newstaff.html', error=errormsg, manager = Manager)
        #Show Added new Staff after Success
        mycursor.execute("SELECT staffID, staffFName, staffLName, staffEmail, role, staffLocation FROM Staff ORDER BY staffID DESC LIMIT 1")
        showID = mycursor.fetchall()
        return render_template('newstaff.html', success=successmsg, showID=showID, manager = Manager)
    mydb.commit()
    return render_template('newstaff.html', manager = Manager)

#Page to ADD a New device to the database
@app.route('/newdevice', methods=['GET', 'POST'])
def newdevice():
    #Check if manager
    Manager = True
    #Keep login saved in count
    global count
    dcount = 0   
    if request.method == 'POST':
        dcount = dcount +1
        Devicedetails = request.form
        deviceName = Devicedetails['DeviceName'].title()
        deviceType = Devicedetails['DeviceType']
        deviceOS = Devicedetails['DeviceOS'].title()
        device = Devicedetails['Device']
        OSVersion = Devicedetails['OSVersion']
        deviceRam = Devicedetails['DeviceRam']
        deviceCPU = Devicedetails['DeviceCPU']
        deviceBit = Devicedetails['DeviceBit']
        deviceResolution = Devicedetails['DeviceResolution']
        deviceGrade = Devicedetails['DeviceGrade'].title()
        deviceUUID = Devicedetails['DeviceUUID']
        deviceCost = Devicedetails['DeviceCost']
        #exception handling from incorrect inputs
        errormsg=""
        errorlist = []
        if (len(deviceName)< 1 or len(deviceType)< 1 or len(deviceOS)< 1 or len(device)< 1):
            errorlist.append("Minimum fields required is Device Name, Device Type, Device OS and Device")
        mycursor = mydb.cursor()            
        mycursor.execute("select COUNT(DeviceName) from Device where DeviceName = %s", (deviceName,))
        namecheck = mycursor.fetchall()
        if len(namecheck) > 1:
            print(len(namecheck))
            errorlist.append("Device Name already exists")
        if (len(deviceName) > 20):
            errorlist.append("Device Name - max letter count 20")
        if (len(deviceType) > 30):
            errorlist.append("DeviceType - max letter count 30")
        if (len(deviceOS) > 10):
            errorlist.append("deviceOS - max letter count 10")
        if (len(OSVersion) > 10):
            errorlist.append("OSVersion - max letter count 10")
        if (len(deviceRam) > 7):
            errorlist.append("deviceRam - max letter count 7")
        if (len(deviceCPU) > 30):
            errorlist.append("deviceCPU - max letter count 30")
        if (len(deviceBit) > 2):
            errorlist.append("deviceBit - max letter count 2")
        if (len(deviceResolution) > 30):
            errorlist.append("deviceResolution - max letter count 30")
        if (len(deviceGrade) > 10):
            errorlist.append("deviceGrade - max letter count 10")
        if (len(deviceUUID) > 50):
            errorlist.append("deviceUUID - max letter count 50")
        if (len(deviceCost) > 10):
            errorlist.append("deviceCost - max letter count 10")
        if deviceCost.isalpha():
            errorlist.append("Device Cost can only have numbers")
        if len(errorlist) > 0:
            return render_template('newdevice.html', error=errorlist, manager = Manager, count = dcount)
        #If successful Insert form data into Database
        mycursor = mydb.cursor()
        mycursor.execute("INSERT INTO Device (deviceName, deviceType, deviceOS, device, OSVersion, deviceRam, deviceCPU, deviceBit, deviceResolution, deviceGrade, deviceUUID, deviceCost, deviceActive)\
        VALUES(%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, 'yes')",(deviceName, deviceType, deviceOS, device, OSVersion, deviceRam, deviceCPU, deviceBit, deviceResolution, deviceGrade, deviceUUID, deviceCost))
        mydb.commit()
        #Success
        successmsg=""
        successmsg = "You have successfully added a Device"
        #show Device ID on success
        mycursor = mydb.cursor()
        mycursor.execute("SELECT deviceID, deviceName, deviceType, deviceOS, device, OSVersion, deviceRam, deviceCPU, deviceBit, deviceResolution, deviceGrade, deviceUUID, deviceCost FROM Device ORDER BY deviceID DESC LIMIT 1")
        showID = mycursor.fetchall()
        mydb.commit()
        return render_template('newdevice.html', success=successmsg, showID=showID, manager = Manager, count = dcount)
    return render_template('newdevice.html', manager = Manager, count = dcount)

#function to remove a device permanently from the database
@app.route('/removedevice', methods=['GET', 'POST'])
def removedevice():
    global Manager
    Manager = True
    mycursor = mydb.cursor()
    mycursor.execute("SELECT deviceID, deviceName FROM Device WHERE deviceActive = 'yes'")
    deviceDets = mycursor.fetchall()
    if request.method == 'POST':
        removedeviceDetails = request.form
        deviceID = removedeviceDetails['device_ID']
        spe_device(deviceID)
        showID = spe_device(deviceID)
        #check if device is in the device list
        mycursor.execute("SELECT COUNT(deviceID) FROM Device WHERE deviceID = %s", (deviceID,))
        checkDevice = mycursor.fetchone()
        if checkDevice[0] > 0:
            mycursor.execute("SELECT COUNT(deviceID) FROM Loan WHERE deviceID = %s AND loanReturned = '1980-01-01 00:00:01'", (deviceID,))
            checkLoan = mycursor.fetchone()
            mycursor.execute("SELECT COUNT(deviceID) FROM Hold WHERE deviceID = %s", (deviceID,))
            checkHold = mycursor.fetchone()
            if (checkLoan[0] > 0) or (checkHold[0] > 0):
                on_loan = "Cannot delete this device, it is currently on loan!"
                return render_template('removedevice.html', on_loan = on_loan, showID = showID, deviceDets = deviceDets, manager = Manager)
            else:
                mycursor.execute("UPDATE Device SET deviceActive = 'no' WHERE deviceID = %s", (deviceID,))
                mydb.commit()
                #Success
                successmsg = "You have successfully removed this device."
                mycursor.execute("SELECT deviceID, deviceName FROM Device WHERE deviceActive = 'yes'")
                deviceDets = mycursor.fetchall()
                return render_template('removedevice.html', successmsg = successmsg, showID = showID, deviceDets = deviceDets, manager = Manager)
        else:
            no_id =  "There is no item of this device ID."
            return render_template('removedevice.html', no_id = no_id, deviceDets = deviceDets, manager = Manager)
    mydb.commit()
    return render_template('removedevice.html', deviceDets = deviceDets, manager = Manager)

#function to remove a staff permanently from the database
@app.route('/removestaff', methods=['GET', 'POST'])
def removestaff():
    global Manager
    Manager = True
    mycursor = mydb.cursor()
    staff_list()
    staff = staff_list()
    if request.method == 'POST':
        removestaffDetails = request.form
        staffID = removestaffDetails['ID']
        spe_staff(staffID)
        showID = spe_staff(staffID)
        print(showID)
        print ("ID:",showID[0][1])
        #check if staff is in the staff list
        mycursor.execute("SELECT COUNT(staffID) FROM Staff WHERE staffID = %s", (staffID,))
        checkStaff = mycursor.fetchone()
        if checkStaff[0] == 0:
            no_id =  "There is no staff of this staff ID."
            return render_template('removestaff.html', no_id = no_id, staff = staff, manager = Manager)
        #check if staff has any holds or loans
        mycursor.execute("SELECT COUNT(deviceID) FROM Loan WHERE staffID = %s AND loanReturned = '1980-01-01 00:00:01'", (staffID,))
        checkLoan = mycursor.fetchone()
        mycursor.execute("SELECT COUNT(deviceID) FROM Hold WHERE staffID = %s", (staffID,))
        checkHold = mycursor.fetchone()
        if (checkLoan[0] > 0) or (checkHold[0] > 0):
            no_id = "Cannot delete this staff member, they currently have an item out on loan!"
            return render_template('removestaff.html', no_id = no_id, staff = staff, manager = Manager)
        else:
            mycursor.execute("UPDATE Staff SET staffActive = 'no' WHERE staffID = %s", (staffID,))
            mydb.commit()
            #Success
            successmsg = "You have successfully removed this staff."
            staff_list()
            staff = staff_list()
            return render_template('removestaff.html', successmsg = successmsg, showID = showID, staff = staff, manager = Manager)
    mydb.commit()
    return render_template('removestaff.html', staff = staff, manager = Manager)

#Page for editing a current device
@app.route('/editdevice', methods=['GET', 'POST'])
def editdevice():
    Manager = True
    mycursor = mydb.cursor()
    mycursor.execute("SELECT * FROM Device")
    deviceDets = mycursor.fetchall()
    successmsg = ""
    showID = ""
    errormsg=""
    if request.method == 'POST':
        Devicedetails = request.form
        deviceID = Devicedetails['device_ID']
        deviceName = Devicedetails['device_name'].title()
        deviceType = Devicedetails['device_type']
        deviceOS = Devicedetails['device_os'].title()
        device = Devicedetails['device']
        OSVersion = Devicedetails['os_version']
        deviceRam = Devicedetails['device_ram']
        deviceCPU = Devicedetails['device_cpu']
        deviceBit = Devicedetails['device_bit']
        deviceResolution = Devicedetails['device_resolution']
        deviceGrade = Devicedetails['device_grade'].title()
        deviceUUID = Devicedetails['device_uuid']
        deviceCost = Devicedetails['device_cost']
        deviceActive = Devicedetails['device_active']
        #check if device is currently on loan or on hold
        #all error messages related to ensuring proper inputs
        errorlist = []
        if (len(deviceName)< 1 or len(deviceType)< 1 or len(deviceOS)< 1 or len(device)< 1):
            errorlist.append("Minimum fields required is Device Name, Device Type, Device OS and Device")
        if (len(deviceName) > 20):
            errorlist.append("Device Name - max letter count 20")
        if (len(deviceType) > 30):
            errorlist.append("Device Type - max letter count 30")
        if (len(deviceOS) > 10):
            errorlist.append("device OS - max letter count 10")
        if (len(OSVersion) > 10):
            errorlist.append("OS Version - max letter count 10")
        if (len(deviceRam) > 7):
            errorlist.append("device Ram - max letter count 7")
        if (len(deviceCPU) > 30):
            errorlist.append("device CPU - max letter count 30")
        if (len(deviceBit) > 2):
            errorlist.append("device Bit - max letter count 2")
        if (len(deviceResolution) > 30):
            errorlist.append("device Resolution - max letter count 30")
        if (len(deviceGrade) > 10):
            errorlist.append("device Grade - max letter count 10")
        if (len(deviceUUID) > 50):
            errorlist.append("device UUID - max letter count 50")
        if (len(deviceCost) > 10):
            errorlist.append("device Cost - max letter count 10")
        if deviceCost.isalpha():
            errorlist.append("Device Cost can only have numbers")
        if len(errorlist) > 0:
            return render_template('editdevice.html', error=errorlist, manager = Manager, deviceDets = deviceDets)
        mycursor.execute("UPDATE Device SET deviceName = %s, deviceType = %s, deviceOS = %s, device = %s, OSVersion = %s, deviceRam = %s, deviceCPU = %s, deviceBit = %s, deviceResolution = %s, deviceGrade = %s, deviceUUID = %s, deviceCost = %s, deviceActive = %s WHERE deviceID = %s",(deviceName, deviceType, deviceOS, device, OSVersion, deviceRam, deviceCPU, deviceBit, deviceResolution, deviceGrade, deviceUUID, deviceCost, deviceActive, deviceID))
        mydb.commit()
        #Success
        successmsg=""
        successmsg = "You have successfully edited a device."
        #show Device ID on success
        mycursor = mydb.cursor()
        mycursor.execute("SELECT * FROM Device WHERE deviceID = %s", (deviceID,))
        showID = mycursor.fetchall()
        mydb.commit()
        return render_template('editdevice.html', success=successmsg, showID=showID, manager = Manager, deviceDets = deviceDets)
    return render_template('editdevice.html', manager = Manager, deviceDets = deviceDets)

if __name__=="__main__":
    app.run(debug=True)
