def decimal_to_ip(decimal):
    if decimal < -2147483648 or decimal > 4294967295:
        return "Invalid IP Address"

    if decimal < 0:
        decimal = 0xFFFFFFFF + decimal + 1

    octet1 = (decimal >> 24) & 0xFF
    octet2 = (decimal >> 16) & 0xFF
    octet3 = (decimal >> 8) & 0xFF
    octet4 = decimal & 0xFF

    ip = f"{octet4}.{octet3}.{octet2}.{octet1}"
    return ip



import threading
import winreg
import time
from apiGetServer import *
import os

COLOR = {
    "HEADER": "\033[95m",
    "BLUE": "\033[94m",
    "GREEN": "\033[92m",
    "RED": "\033[91m",
    "ENDC": "\033[0m",
}
def check_registry_value(key_path, value_name,port_name):
    previous_value = None
    while True:
        try:
            # Open the registry key
            key = winreg.OpenKey(winreg.HKEY_LOCAL_MACHINE, key_path)

            # Read the registry value
            value, value_type = winreg.QueryValueEx(key, value_name)
            value1, value_type1 = winreg.QueryValueEx(key, port_name)
            if value != previous_value:
                if value != "0" and value != "1":
                    ip,port,name,players,maxplayers = getServerData(decimal_to_ip(int(value)),int(value1))
    
                    print(f"[System] Detected Connection to server : {name} | Players: {players}/{maxplayers} | IP: {ip}:{port}")
                    
                    previous_value = value
                if value == "1":
                    print("[System] Game is closed...")
                    print("[System] Waiting for proccess : gtasa.exe.")
                    previous_value = value
                if value == "0":
                    print("[System] Proccess Detected...")
                    print("[System] Game is starting up...")
                    previous_value = value
                    
                    
        

        except WindowsError:
            print("Failed to read the registry value.")

        # Sleep for a certain period of time before checking again
        time.sleep(1)

# Example usage:
key_path = r"SOFTWARE\WOW6432Node\Multi Theft Auto: San Andreas All\1.6\Settings\general"
value_name = "last-server-ip"
value_name1 = "last-server-port"
# Create a thread to continuously check the registry value
thread = threading.Thread(target=check_registry_value, args=(key_path, value_name,value_name1))
thread.start()
