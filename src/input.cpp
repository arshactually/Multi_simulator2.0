#include <Arduino.h>

// RGB_DEFINES
#define Display_color "The RGB is displaying the required color"

// RGB_PINS
int myPins[] = {0x0F, 0x10, 0x11};

#define PIN_RED    myPins[0]         //15 // GPIO23
#define PIN_GREEN  myPins[1]         //16 // GPIO22
#define PIN_BLUE   myPins[2]         //17 // GPIO21

void Input_SETUP() {
    pinMode(PIN_RED,   OUTPUT);
    pinMode(PIN_GREEN, OUTPUT);
    pinMode(PIN_BLUE,  OUTPUT);
}

void write_function(int value1, int value2, int value3) {
    analogWrite(PIN_RED,   value1);
    // Serial.print("Displayed color with value 1 is "); // Print the string
    // Serial.println(value1); // Print the value and move to a new line

    analogWrite(PIN_GREEN, value2);
    // Serial.print("Displayed color with value 2 is "); // Print the string
    // Serial.println(value2); // Print the value and move to a new line

    analogWrite(PIN_BLUE,  value3);
    // Serial.print("Displayed color with value 3 is "); // Print the string
    // Serial.println(value3); // Print the value and move to a new line
    
    
    Serial.println(Display_color);

}

void mainFunction(uint8_t values[3]){
    int convertedValues[3];
        for (int i = 0; i < 3; i++) {
            convertedValues[i] = values[i]; // Convert uint8_t to int
            }

            write_function(convertedValues[0], convertedValues[1], convertedValues[2]);



    // //    write_function(values[0], values[1], values[2]);

    //         // Send confirmation back to Python with changed values
    //         Serial.print("Values changed to: ");
    //         Serial.print(convertedValues[0]);
    //         Serial.print(", ");
    //         Serial.print(convertedValues[1]);
    //         Serial.print(", ");
    //         Serial.println(convertedValues[2]);
        
    
    
    
}

