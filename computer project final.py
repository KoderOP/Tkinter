from tkinter import *
from tkinter import messagebox
import mysql.connector as mysql
pd=''

def database():
    global pd
    pd = input("Enter the password of your SQL: ")
    cn = mysql.connect(host='localhost', user='root', password=pd)
    keys = cn.cursor()
    create_db_cmd = "CREATE DATABASE IF NOT EXISTS airline_reservation"
    keys.execute(create_db_cmd)
    keys.execute("USE airline_reservation")
    
    cmd_flight = "CREATE TABLE IF NOT EXISTS flight (fid INT PRIMARY KEY, fc VARCHAR(60), sl VARCHAR(25), dest VARCHAR(30), dt VARCHAR(30), at VARCHAR(12), eco FLOAT, bus FLOAT, ests INT, bsts INT)"
    keys.execute(cmd_flight)

    cmd_passengers = "CREATE TABLE IF NOT EXISTS passengers (pid INT PRIMARY KEY AUTO_INCREMENT, name VARCHAR(100), flight_id INT, FOREIGN KEY (flight_id) REFERENCES flight(fid))"
    keys.execute(cmd_passengers)

    cn.close()

def add():
    frame_add = Toplevel(frame)
    frame_add.geometry("600x500")
    frame_add.title("Add a Flight")

    lblFlightComp = Label(frame_add, text="Enter flight company:")
    txtFlightComp = Entry(frame_add, width=20)

    lblStartLoc = Label(frame_add, text="Enter starting location:")
    txtStartLoc = Entry(frame_add, width=20)

    lblDestination = Label(frame_add, text="Enter destination:")
    txtDestination = Entry(frame_add, width=20)

    lblDepart = Label(frame_add, text="Enter departure time:")
    txtDepart = Entry(frame_add, width=20)

    lblArrive = Label(frame_add, text="Enter arrival time:")
    txtArrive = Entry(frame_add, width=20)

    lblEconomic = Label(frame_add, text="Enter price of economic class:")
    txtEconomic = Entry(frame_add, width=20)

    lblBusiness = Label(frame_add, text="Enter price of business class:")
    txtBusiness = Entry(frame_add, width=20)

    lblSeatsEco = Label(frame_add, text="Enter no. of seats in economic class:")
    txtSeatsEco = Entry(frame_add, width=20)

    lblSeatsBus = Label(frame_add, text="Enter no. of seats in business class:")
    txtSeatsBus = Entry(frame_add, width=20)

    lblFid = Label(frame_add, text="Enter Flight ID:")
    txtFid = Entry(frame_add, width=20)

    btnSave = Button(frame_add, text="Save Flight", command=lambda: save(
        txtFlightComp.get(), txtStartLoc.get(), txtDestination.get(),
        txtDepart.get(), txtArrive.get(), txtEconomic.get(),
        txtBusiness.get(), txtSeatsEco.get(), txtSeatsBus.get(), txtFid.get()
    ))

    lblFlightComp.grid(row=0, column=0, pady=5, padx=10)
    txtFlightComp.grid(row=0, column=1, pady=5, padx=10)
    lblStartLoc.grid(row=1, column=0, pady=5, padx=10)
    txtStartLoc.grid(row=1, column=1, pady=5, padx=10)
    lblDestination.grid(row=2, column=0, pady=5, padx=10)
    txtDestination.grid(row=2, column=1, pady=5, padx=10)
    lblDepart.grid(row=3, column=0, pady=5, padx=10)
    txtDepart.grid(row=3, column=1, pady=5, padx=10)
    lblArrive.grid(row=4, column=0, pady=5, padx=10)
    txtArrive.grid(row=4, column=1, pady=5, padx=10)
    lblEconomic.grid(row=5, column=0, pady=5, padx=10)
    txtEconomic.grid(row=5, column=1, pady=5, padx=10)
    lblBusiness.grid(row=6, column=0, pady=5, padx=10)
    txtBusiness.grid(row=6, column=1, pady=5, padx=10)
    lblSeatsEco.grid(row=7, column=0, pady=5, padx=10)
    txtSeatsEco.grid(row=7, column=1, pady=5, padx=10)
    lblSeatsBus.grid(row=8, column=0, pady=5, padx=10)
    txtSeatsBus.grid(row=8, column=1, pady=5, padx=10)
    lblFid.grid(row=9, column=0, pady=5, padx=10)
    txtFid.grid(row=9, column=1, pady=5, padx=10)
    btnSave.grid(row=10, column=0, columnspan=2, pady=10)

def save(fc, sl, dest, dt, at, eco, bus, ests, bsts, fid):
    try:
        eco = float(eco)
        bus = float(bus)
        ests = int(ests)
        bsts = int(bsts)
        fid = int(fid)
        cn = mysql.connect(host='localhost', user='root', password=pd, database='airline_reservation')
        keys = cn.cursor()
        query_flight = "INSERT INTO flight VALUES({}, '{}', '{}', '{}', '{}', '{}', {}, {}, {}, {})".format(
            fid, fc, sl, dest, dt, at, eco, bus, ests, bsts)
        keys.execute(query_flight)
        cn.commit()
        cn.close()
        messagebox.showinfo("Success", "Data saved")
    except Exception as e:
        messagebox.showerror("Error", str(e))

def book():
    frame_book = Toplevel(frame)
    frame_book.geometry("600x400")
    frame_book.title("Book a Flight")

    lblFlightID = Label(frame_book, text="Enter Flight ID:")
    txtFlightID = Entry(frame_book, width=20)
    lblPassengerName = Label(frame_book, text="Enter Passenger Name:")
    txtPassengerName = Entry(frame_book, width=20)
    btnBook = Button(frame_book, text="Book Flight", command=lambda: perform_booking(
        txtFlightID.get(), txtPassengerName.get()
    ))
    btnCancelBook = Button(frame_book, text="Cancel", command=frame_book.destroy)

    lblFlightID.pack(pady=10)
    txtFlightID.pack(pady=10)
    lblPassengerName.pack(pady=10)
    txtPassengerName.pack(pady=10)
    btnBook.pack(pady=10)
    btnCancelBook.pack(pady=10)

def perform_booking(flight_id, passenger_name):
    try:
        flight_id = int(flight_id)
        cn = mysql.connect(host='localhost', user='root', password=pd, database='airline_reservation')
        keys = cn.cursor()
        query_booking = "INSERT INTO passengers (name, flight_id) VALUES('{}', {})".format(passenger_name, flight_id)
        keys.execute(query_booking)
        cn.commit()
        cn.close()
        messagebox.showinfo("Success", "Booking successful")
    except Exception as e:
        messagebox.showerror("Error", str(e))

def cancel():
    frame_cancel = Toplevel(frame)
    frame_cancel.geometry("600x140")
    frame_cancel.title("Cancel a Flight")

    lblPid = Label(frame_cancel, text="Enter Flight ID to be cancelled:")
    txtPid = Entry(frame_cancel, width=20)
    btnBook = Button(frame_cancel, text="Cancel", command=lambda: go(
        txtPid.get()
    ))

    lblPid.grid(row=0, column=0, pady=5, padx=10)
    txtPid.grid(row=0, column=1, pady=5, padx=10)
    btnBook.grid(row=1, column=0, columnspan=2, pady=10)

def go(passenger_id):
    try:
        passenger_id = int(passenger_id)
        cn = mysql.connect(host='localhost', user='root', password=pd, database='airline_reservation')
        keys = cn.cursor()
        query_cancel = "DELETE FROM passengers WHERE pid={}".format(passenger_id)
        keys.execute(query_cancel)
        cn.commit()
        cn.close()
        messagebox.showinfo("Success", "Flight cancelled")
    except Exception as e:
        messagebox.showerror("Error", str(e))

def modify():
    frame_modify = Toplevel(frame)
    frame_modify.geometry("600x500")
    frame_modify.title("Modify Flight")

    lblFid = Label(frame_modify, text="Enter Flight ID to modify:")
    txtFid = Entry(frame_modify, width=20)
    btnModify = Button(frame_modify, text="Modify Flight", command=lambda: modify_flight(txtFid.get()))
    btnCancelModify = Button(frame_modify, text="Cancel", command=frame_modify.destroy)

    lblFid.pack(pady=10)
    txtFid.pack(pady=10)
    btnModify.pack(pady=10)
    btnCancelModify.pack(pady=10)
 

def modify_flight(flight_id):
    try:
        flight_id = int(flight_id)
        cn = mysql.connect(host='localhost', user='root', password=pd, database='airline_reservation')
        keys = cn.cursor()
        query_fetch = "SELECT * FROM flight WHERE fid={}".format(flight_id)
        keys.execute(query_fetch)
        flight_data = keys.fetchone()

        if flight_data:
            frame_modify_details = Toplevel(frame)
            frame_modify_details.geometry("600x500")
            frame_modify_details.title("Modify Flight Details")

            lblFlightComp = Label(frame_modify_details, text="Enter modified flight company:")
            txtFlightComp = Entry(frame_modify_details, width=20)
            txtFlightComp.insert(0, flight_data[1]) 

            lblStartLoc = Label(frame_modify_details, text="Enter modified starting location:")
            txtStartLoc = Entry(frame_modify_details, width=20)
            txtStartLoc.insert(0, flight_data[2])  

            lblDest = Label(frame_modify_details, text="Enter modified destination:")
            txtDest = Entry(frame_modify_details, width=20)
            txtDest.insert(0, flight_data[3])  

            lblDepart = Label(frame_modify_details, text="Enter modified departure time:")
            txtDepart = Entry(frame_modify_details, width=20)
            txtDepart.insert(0, flight_data[4]) 

            lblArrive = Label(frame_modify_details, text="Enter modified arrival time:")
            txtArrive = Entry(frame_modify_details, width=20)
            txtArrive.insert(0, flight_data[5]) 

            lblEconomic = Label(frame_modify_details, text="Enter modified price of economic class:")
            txtEconomic = Entry(frame_modify_details, width=20)
            txtEconomic.insert(0, flight_data[6])

            lblBusiness = Label(frame_modify_details, text="Enter modified price of business class:")
            txtBusiness = Entry(frame_modify_details, width=20)
            txtBusiness.insert(0, flight_data[7])  

            lblSeatsEco = Label(frame_modify_details, text="Enter modified no. of seats in economic class:")
            txtSeatsEco = Entry(frame_modify_details, width=20)
            txtSeatsEco.insert(0, flight_data[8]) 

            lblSeatsBus = Label(frame_modify_details, text="Enter modified no. of seats in business class:")
            txtSeatsBus = Entry(frame_modify_details, width=20)
            txtSeatsBus.insert(0, flight_data[9])  

            btnSaveModification = Button(frame_modify_details, text="Save Modification",
                                         command=lambda: save_modification(
                                             flight_id, txtFlightComp.get(), txtStartLoc.get(), txtDest.get(),
                                             txtDepart.get(), txtArrive.get(), txtEconomic.get(), txtBusiness.get(),
                                             txtSeatsEco.get(), txtSeatsBus.get()))

            lblFlightComp.pack(pady=10)
            txtFlightComp.pack(pady=10)
            lblStartLoc.pack(pady=10)
            txtStartLoc.pack(pady=10)
            lblDest.pack(pady=10)
            txtDest.pack(pady=10)
            lblDepart.pack(pady=10)
            txtDepart.pack(pady=10)
            lblArrive.pack(pady=10)
            txtArrive.pack(pady=10)
            lblEconomic.pack(pady=10)
            txtEconomic.pack(pady=10)
            lblBusiness.pack(pady=10)
            txtBusiness.pack(pady=10)
            lblSeatsEco.pack(pady=10)
            txtSeatsEco.pack(pady=10)
            lblSeatsBus.pack(pady=10)
            txtSeatsBus.pack(pady=10)

            btnSaveModification.pack(pady=10)
        else:
            messagebox.showerror("Error", "Flight with ID {} not found.".format(flight_id))

        cn.close()

    except Exception as e:
        messagebox.showerror("Error", str(e))


def save_modification(flight_id, modified_flight_comp, modified_start_loc, modified_dest, modified_dt, modified_at,
                      modified_eco, modified_bus, modified_ests, modified_bsts):
    try:
        modified_eco = float(modified_eco)
        modified_bus = float(modified_bus)
        modified_ests = int(modified_ests)
        modified_bsts = int(modified_bsts)

        cn = mysql.connect(host='localhost', user='root', password=pd, database='airline_reservation')
        keys = cn.cursor()

        query_update = "UPDATE flight SET fc='{}', sl='{}', dest='{}', dt='{}', at='{}', eco={}, bus={}, ests={}, bsts={} " \
                       "WHERE fid={}".format(modified_flight_comp, modified_start_loc, modified_dest, modified_dt,modified_at, modified_eco, modified_bus, modified_ests, modified_bsts, flight_id)
        keys.execute(query_update)
        cn.commit()
        cn.close()
        messagebox.showinfo("Success", "Flight details modified")
    except Exception as e:
        messagebox.showerror("Error", str(e))


frame = Tk()
frame.title("Airline Reservation System")
frame.geometry("400x300")

btnAdd = Button(frame, text="Add Flight", command=add)
btnBook = Button(frame, text="Book Flight", command=book)
btnCancel = Button(frame, text="Cancel Flight", command=cancel)
btnModify = Button(frame, text="Modify Flight", command=modify)  

btnAdd.pack(pady=10)
btnBook.pack(pady=10)
btnCancel.pack(pady=10)
btnModify.pack(pady=10)

database()


frame.mainloop()


