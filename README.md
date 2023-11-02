# readingMTAipFromRegistry
idk it might be useful
# Registry
![image](https://github.com/SwagAPI/readingConnectedMTAServeripFromRegistry/assets/108799236/93d9e11e-d403-49fc-92d2-34bca7093cee)
# Explanation
mta sa is storing the connected server ip when u join a server in the regedit path Computer\HKEY_LOCAL_MACHINE\SOFTWARE\WOW6432Node\Multi Theft Auto: San Andreas All\1.6\Settings\general
![image](https://github.com/SwagAPI/readingConnectedMTAServeripFromRegistry/assets/108799236/46f79373-c417-41c4-ac40-d6d3d62c344b)
# Code
The function first checks if the decimal number is within the valid range of IPv4 addresses (-2147483648 to 4294967295). If it's not, it returns the string "Invalid IP Address".
If the decimal number is negative, the function adds 4294967296 to it to convert it to a positive number.
Next, the function extracts the individual octets (1st, 2nd, 3rd, and 4th) of the IP address by performing bitwise operations. It uses bitwise right shift (>>) and bitwise AND (&) operations to extract the respective octets.
Finally, the function constructs the IP address string by concatenating the octets in the format "octet4.octet3.octet2.octet1"
# Whats the point ? 
its simple now dicscord rich presence is supported in mta sa 
(https://github.com/multitheftauto/mtasa-blue/commit/fdaa3aca3e233c7aba69d0fd5f85e78288a4401a)
i was thinking about making an external launcher integrated with mta sa but with an discord rpc to show what server u are currently playing on 
name / players are fetched with (https://mtasa.com/api/)
