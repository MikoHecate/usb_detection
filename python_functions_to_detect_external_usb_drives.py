import wmi

"""Function to get all connected usb devices"""


def get_all_connected_usb_devices():
    c = wmi.WMI()
    usb_devices = []

    for device in c.Win32_USBControllerDevice():
        usb_device = device.Dependent
        usb_devices.append(usb_device)

    return usb_devices


"""Function to print all connected devices"""


def print_all_connected_devices():
    # Example usage
    usb_devices = get_all_connected_usb_devices()
    if usb_devices:
        print("USB devices connected:")
        for device in usb_devices:
            print("Device ID:", device.DeviceID)
            print("Description:", device.Description)
            print("Manufacturer:", device.Manufacturer)
            print("Product Name:", device.Name)
            print("---")
    else:
        print("No USB devices found.")


"""Function to get a list of external usb drives"""


def get_external_usb_drives():
    c = wmi.WMI()
    external_usb_drives = []

    for device in c.Win32_USBControllerDevice():
        usb_device = device.Dependent
        if usb_device:
            if usb_device.Caption.startswith("USB Mass Storage"):
                external_usb_drives.append(usb_device)
    return external_usb_drives


"""Function to print usb drives"""


def print_usb_drives():
    external_drives = get_external_usb_drives()
    if external_drives:
        print("External USB drives connected:")
        for device in external_drives:
            print("Device ID:", device.DeviceID)
            print("Description:", device.Description)
            print("Manufacturer:", device.Manufacturer)
            print("Product Name:", device.Name)
            print("---")
    else:
        print("No external USB drives found.")