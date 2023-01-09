import re

if __name__ == "__main__":
    devices = dict()
    faults =  dict()

    invalid_imeis = invalid_events = 0

    f = open("test_data.txt", "r")
    
    for x in f:
        parts = x.split()
        if len(parts) == 3:
            # Check invalid event
            if parts[0] != "SEND" and parts[0] != "RECV":
                invalid_events += 1

            # Check invalid imei
            if re.match(r'^\d{15}$', parts[1]) == None:
                invalid_imeis += 1

            # Get the devices' count
            if parts[2] in devices:
                devices[parts[2]] += 1
            else:
                devices[parts[2]] = 1
        elif len(parts) == 2:
            # Get fault code mapping
            if parts[0] not in faults:
                faults[parts[0]] = parts[1]

    print('Iventory:')
    for key, value in devices.items():
        print(key, value)

    print("Invalid records:", invalid_imeis, "Invalid IMEI,", invalid_events, "Invalid event")

    print('Fault code mapping:')
    for key, val in faults.items():
        print(key, val)