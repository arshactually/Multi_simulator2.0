# def takeRGBValues():
#      print("Enter the values of channels:")
#      channel1 = int(input(
#        "Enter the value of 1st Channel: "))
     
#      channel2 = int(input(
#        "Enter the value of 2nd Channel: "))
#      channel3 = int(input(
#        "Enter the value of 3rd Channel: "))
#      return channel1, channel2, channel3 



def takeRGBValues():
    print("Enter the values of channels:")
    rgbChannels = []

    for i in range(3):
        channel_value = int(input(f"Enter the value of Channel {i+1}: "))
        if channel_value < 0 or channel_value > 255:
            raise ValueError("Channel values should be between 0 and 255")
        rgbChannels.append(channel_value)
        print(rgbChannels)
    return bytes(rgbChannels)


# def takeLEDValue():
#     print("Please enter the brightness you want: ")
#     brightnessChannels = []
#     for i in range(3):
#         channel_value = int(input(f"Enter the value of Channel {i+1}: "))
#         if channel_value < 0 or channel_value > 255:
#             raise ValueError("Channel values should be between 0 and 255")
#         brightnessChannels.append(channel_value)
#         print(brightnessChannels)
#     return bytes(brightnessChannels)

def takeLEDValue():
    print("Please enter the brightness you want: ")
    brightness = int(input("Enter the brightness value (0-255): "))
    
    if brightness < 0 or brightness > 255:
        raise ValueError("Brightness value should be between 0 and 255")
    
    return bytes([brightness, 0, 0])