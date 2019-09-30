#!/usr/bin/env python
# encoding: utf-8
import getpass
import time
import os
import teslajson

password = getpass.getpass('Tesla Password:')

TESLA_EMAIL = "manse@sky.com"
TESLA_PASSWORD = password


def establish_connection(token=None):
    conn = teslajson.Connection(email=TESLA_EMAIL, password=TESLA_PASSWORD, access_token=token)
    return conn

def get_charge(c, car):
    charge = None
    for v in c.vehicles:
        if v["display_name"] == car:
            charge = v.data_request('charge_state')
            #charge = int(d["battery_level"])
    return charge


conn = establish_connection()
print("Thank you for logging in, we are checking your Tesla...")
while True:
    #n = raw_input("Type 'exit' to end:")
    chargeState = get_charge(conn, "Rocket")
    battLevel = int(chargeState["battery_level"])
    charging = chargeState["charging_state"]
    status = "Tesla is currently " + charging +  " and battery is at " + str(battLevel) + "%"
    if charging == "Charging":         
        if battLevel > 95:
            alert = "Tesla charge status is now at " + str(battLevel) + "%"
            os.system('say %s' % (alert))
        else: 
            print(status)
            time.sleep(30)
    else:
        print(status)
        break

# qnQzg%NCE5Rv94L