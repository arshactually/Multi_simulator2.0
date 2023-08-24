#include <Arduino.h>
// MOTOR_INCLUDES
#include <Stepper.h>
#include <StringSplitter.h>
#include <motor_module.h>
#include <led_module.h>
#include <rgb_module.h>
#include <input.h>
// #include <function.h>
// #error
char UserInput[30];  

void setup() {
  Serial.begin(115200);
  Serial.setTimeout(1);
  // RBG_SETUP();
  Input_SETUP_LED();
  // MOTOR_SETUP();
  Input_SETUP();

}


void loop() {

  if (Serial.available() > 0) {
    int bytesRead = Serial.readBytesUntil('\n', UserInput, sizeof(UserInput) - 1);
    // Serial.print("1. Received bytes: ");
    // Serial.println(bytesRead);


    if (bytesRead > 0) {
      UserInput[bytesRead] = '\0';  // Null-terminate the string

      char decision = UserInput[0];
      // Serial.print("2. Received decision: ");
      // Serial.println(decision);


      String valuesStr = String(UserInput).substring(2);  // Remove the first character (decision) and the colon

      StringSplitter splitter(valuesStr, ':', 4);  // Split using ':' and limit to 4 tokens
      int numValues = splitter.getItemCount();
      // Serial.print("3. Received numValues: ");
      // Serial.println(numValues);

      if (numValues == 3) {
        uint8_t values[3];
        for (int i = 0; i < 3; i++) {
          String token = splitter.getItemAtIndex(i);
          values[i] = token.toInt();
          // Serial.print("4. Received values: ");
          // Serial.println(values[i]);
        }
      // UserInput[bytesRead] = '\0';  // Null-terminate the string

      // // Split the message into decision and value
      // char decision = UserInput[0];
      // uint8_t values = atoi(UserInput + 2);
      

    // UserInput = Serial.read();
    //switch cases
    switch (decision)
    {
    case '1':
      mainFunctionLED(values);
      break;
    case '2':
      // Led_Off();
      break;
    case '3':
      // SET_RGB_R();
      break;

    case '4':
      // SET_RGB_G();
      break;
    
    case '5':
      // SET_RGB_B();
      break;

    case '6':
      // SET_RGB_OFF();
      break;

    case '7':
      // Motor_On();
      break;
    
    case '8':
      // Motor_Off();
      break;
    case '9':
      mainFunction(values);
      break;
    default:
          //unsupported decision
      break;

        }
      }
    }
  }
}
// // =============================================================
// #include <Arduino.h>
// // MOTOR_INCLUDES
// #include <Stepper.h>

// #include <motor_module.h>
// #include <led_module.h>
// #include <rgb_module.h>


// char UserInput;



// void setup() {
//   Serial.begin(115200);
//   Serial.setTimeout(1);
  
//   // RBG_SETUP();
//   LED_SETUP();
//   MOTOR_SETUP();
  
  


// }

// void loop() {

//   if(Serial.available()>0) {

//     UserInput = Serial.read();
//         // Print the value of UserInput to the serial monitor
//     Serial.print("Received UserInput: ");
//     Serial.println(UserInput);
//     //switch cases
//     switch (UserInput)
//     {
//     case '1':
//       Led_On();
//       break;
//     case '2':
//       Led_Off();
//       break;
//     case '3':
//       SET_RGB_R();
//       break;

//     case '4':
//       SET_RGB_G();
//       break;
    
//     case '5':
//       SET_RGB_B();
//       break;

//     case '6':
//       SET_RGB_OFF();
//       break;

//     case '7':
//       Motor_On();
//       break;
    
//     case '8':
//       Motor_Off();
//       break;
//       }

//   }
  
// }




