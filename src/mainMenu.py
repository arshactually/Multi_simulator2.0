# from numberBlink import numberLed


from numMotor import motorFunction
from functionality import sendDeicision
from functionality import sendDecision1


def menuFunction():
    options = [0x00,0x01,0x02,0x03,0x04,0x05]
    ans=True
    while ans:
      print ("1.Stimulate LED\n2.Stimulate Motor\n3.RGB Simulator\n4.Exit/Quit")

      ans=int(input("What would you like to do?"))
      
      if ans==options[1]:  #1
        print("\nEntered LED Simulation") 
        #LED NUMBER
        sendDecision1()  
      elif ans==options[2]:  #3
        print("\nEntered Motor Simulation") 
        motorFunction()
      elif ans==options[3]:  #3
        print("\nEntered RGB Simulattion") 
        sendDeicision()

      elif ans==options[4]:  #4
        print("\n Goodbye") 
        exit(options[0])    #0
      elif ans !="":
        print("\n Not Valid Choice Try again") 
  


        