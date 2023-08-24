#include <Arduino.h>

#define led_turned_on "Led is turned On"
#define led_turned_off "Led is turned off"

#define ledPin    10  // 10
// int ledPin = 10;

void Input_SETUP_LED() {
    pinMode(ledPin,  OUTPUT);

}

void write_functionLED(int value1, int value2, int value3) {
    analogWrite(ledPin,   value1);
    // Serial.print("Displayed color with value 1 is "); // Print the string
    // Serial.println(value1); // Print the value and move to a new line

    // analogWrite(PIN_GREEN, value2);
    // Serial.print("Displayed color with value 2 is "); // Print the string
    // Serial.println(value2); // Print the value and move to a new line

    // analogWrite(PIN_BLUE,  value3);
    // Serial.print("Displayed color with value 3 is "); // Print the string
    // Serial.println(value3); // Print the value and move to a new line
    
    
    // Serial.println(led_turned_on);

}

void mainFunctionLED(uint8_t values[3]){
    int convertedValues[3];
        for (int i = 0; i < 3; i++) {
            convertedValues[i] = values[i]; // Convert uint8_t to int
            }

            write_functionLED(convertedValues[0], convertedValues[1], convertedValues[2]);



    // //    write_function(values[0], values[1], values[2]);

    //         // Send confirmation back to Python with changed values
    //         Serial.print("Values changed to: ");
    //         Serial.print(convertedValues[0]);
    //         Serial.print(", ");
    //         Serial.print(convertedValues[1]);
    //         Serial.print(", ");
    //         Serial.println(convertedValues[2]);
        
    
    
    
}




// #include <Arduino.h>

// #define led_turned_on "Led is turned On"
// #define led_turned_off "Led is turned off"




// // void LED_SETUP() {
// //   pinMode(ledPin, OUTPUT);
// //   pinMode(LED_BUILTIN, OUTPUT);
// // }


// // void Led_On() {
    
// //     digitalWrite(ledPin, HIGH);
// //     digitalWrite(LED_BUILTIN, HIGH);
// //     Serial.print(led_turned_on);


// // }

// // void Led_Off() {
    
// //       digitalWrite(ledPin, LOW);
// //       digitalWrite(LED_BUILTIN, LOW);
// //       Serial.print(led_turned_off);  Serial.print("\n");

// // }


