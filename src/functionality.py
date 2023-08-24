import serial 
import threading
from values_input import takeRGBValues 
from values_input import takeLEDValue

# This is sending a decison of doing something
# if it is value this, execute the function this for eg. Motor on
decisionLED = b'1' 
# OFF_VALUE =b'2'
# RED_VALUE = b'3' 
# GREEN_VALUE =b'4'
# BLUE_VALUE = b'5' 
# RGB_OFF_VALUE =b'6'
MOTOR_ON_VALUE =b'7'
MOTOR_OFF_VALUE =b'8'
decisionRGB =b'9'
decision_turnoff =b'10'

# My task is somehow to send a decison i.e analog.write(decision)
# but also the values analog.write(value)
# Main Task how to do it? Sending decision and value together.




# R_VALUE =b'9'
# G_VALUE =b'10'
# B_VALUE =b'11'


# Open the serial connection
arduino = serial.Serial('COM6', baudrate=115200, timeout=1) 



# def turnOnLed():
#         arduino.write(On_VALUE)
#         print(On_VALUE)
        
        
#         user_input_from_arduino = arduino.readline().decode().strip()
#         print("Received UserInput from Arduino:", user_input_from_arduino)
        

#         recieved_data= arduino.readline().decode().strip()
#         print("Recieved: " , recieved_data)



# def turnOffLed():
#         arduino.write(OFF_VALUE)

#         user_input_from_arduino = arduino.readline().decode().strip()
#         print("Received UserInput from Arduino:", user_input_from_arduino)
        

#         recieved_data= arduino.readline().decode().strip()
#         print("Recieved: " , recieved_data)



# def SET_LED_R():
#         arduino.write(RED_VALUE)
#         arduino_data = arduino.readline()
#         recieved_data= arduino_data.decode().strip()
#         print("Recieved: " , recieved_data)

# def SET_LED_G():
#         arduino.write(GREEN_VALUE)
#         arduino_data = arduino.readline()
#         recieved_data= arduino_data.decode().strip()
#         print("Recieved: " , recieved_data)

# def SET_LED_B():
#         arduino.write(BLUE_VALUE)
#         arduino_data = arduino.readline()
#         recieved_data= arduino_data.decode().strip()
#         print("Recieved: " , recieved_data)

# def SET_LED_OFF():
#         arduino.write(OFF_VALUE)
#         arduino_data = arduino.readline()
#         recieved_data= arduino_data.decode().strip()
#         print("Recieved: " , recieved_data)


def turnOnMotor():
        arduino.write(MOTOR_ON_VALUE)

        user_input_from_arduino = arduino.readline().decode().strip()
        print("Received UserInput from Arduino:", user_input_from_arduino)
        

        recieved_data= arduino.readline().decode().strip()
        print("Recieved: " , recieved_data)




def turnOffMotor():
        arduino.write(MOTOR_OFF_VALUE)
        arduino_data = arduino.readline()
        recieved_data= arduino_data.decode().strip()
        print("Recieved: " , recieved_data)



def sendDecision1():
        off_channels=[0, 0, 0]
        # Calling the function to take input values
        channels = takeLEDValue()
        data_to_send = bytes(channels)
        turn_off_channels = bytes(off_channels)

#Concatinating values of decison and values of channels 

        message = f'{decisionLED.decode()}:{":".join(map(str, data_to_send))}'.encode()
        
        turn_off_message = f'{decision_turnoff.decode()}:{",".join(map(str, turn_off_channels))}'.encode()
        print(f"These values are sent: ", message)
        # print(turn_off_message)
        # message = f'{decision.decode()}:{data_to_send[0]}:{data_to_send[1]}:{data_to_send[2]}'
        # # message = f'{decision.decode()}:{",".join(map(str, data_to_send))}'
        # # message = f'{decision.decode()}:{data_to_send}'
        # turn_off_message= f'{decision_turnoff.decode()}:{",".join(map(str, turn_off_channels))}'
        
        while True: 
               arduino.write(message)

               user_input = input("")
               if user_input:
                  break
        #        user_input_from_arduino = arduino.readline().decode().strip()
        # #        print("Received UserInput from Arduino:", user_input_from_arduino)
        #        user_input = input("Press Enter to exit the loop: ")
        # #        if user_input:
        #         break
       







def sendDeicision():
        off_channels=[0, 0, 0]
        # Calling the function to take input values
        channels = takeRGBValues()
        data_to_send = bytes(channels)
        turn_off_channels = bytes(off_channels)

#Concatinating values of decison and values of channels 

        message = f'{decisionRGB.decode()}:{":".join(map(str, data_to_send))}'.encode()
        
        turn_off_message = f'{decision_turnoff.decode()}:{",".join(map(str, turn_off_channels))}'.encode()
        print(f"These values are sent: ", message)
        # print(turn_off_message)
        # message = f'{decision.decode()}:{data_to_send[0]}:{data_to_send[1]}:{data_to_send[2]}'
        # # message = f'{decision.decode()}:{",".join(map(str, data_to_send))}'
        # # message = f'{decision.decode()}:{data_to_send}'
        # turn_off_message= f'{decision_turnoff.decode()}:{",".join(map(str, turn_off_channels))}'
        
        while True: 
               arduino.write(message)
        #        user_input_from_arduino = arduino.readline().decode().strip()
        #        print("Received UserInput from Arduino:", user_input_from_arduino)
               user_input = input("")
               if user_input:
                  break
        
        
        
        
        
        
        # # Flag to control the loop
        # exit_signal = False

        # def user_input_thread():
        #         global exit_signal
        #         input("Press Enter to turn off the LED: ")
        #         exit_signal = True

        # # Start the user input thread
        # input_thread = threading.Thread(target=user_input_thread)
        # input_thread.start()

        # try:
        #      while not exit_signal:
        #         #Analog write of the concatinated value of decision and channels
        #         arduino.write(message)
        #         # recieved_data= arduino_data.decode().strip()
        #         # arduino_confirmation = arduino.readline().decode().strip()
        #         # print("Arduino Confirmation:", arduino_confirmation)
        # except KeyboardInterrupt:
        #         pass
        # finally:
    
        #         # arduino.write(bytes([0, 0, 0]))
        #         arduino.write(turn_off_message)
        #         input_thread.join()  # Wait for the user input thread to finish
        #         # Read and print the received UserInput value
        # user_input_from_arduino = arduino.readline().decode().strip()
        # print("Received UserInput from Arduino:", user_input_from_arduino)

        # # Close the serial connection
        # arduino.close()




# Approach Two 
# also not working 

# def serialWriteR():
#         arduino.write(R_VALUE)
#         arduino_data = arduino.readline()
#         recieved_data= arduino_data.decode().strip()



# def serialWriteG():
#         arduino.write(G_VALUE)
#         arduino_data = arduino.readline()
#         recieved_data= arduino_data.decode().strip()


# def serialWriteB():
#         arduino.write(B_VALUE)
#         arduino_data = arduino.readline()
#         recieved_data= arduino_data.decode().strip()




# #Approach three 
# # def function():
#         arduino.write(decision)
#         arduino.write(data_to_send)
     