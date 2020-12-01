#include <SoftwareSerial.h>
#define DO_RLed 13 //D7
#define DO_GLed 12 //D6
SoftwareSerial ESPserial(3, 1);

void setup(){
  pinMode(DO_RLed, OUTPUT);
  pinMode(DO_GLed, OUTPUT);  
  digitalWrite(DO_RLed, HIGH);
  delay(2000);
  digitalWrite(DO_RLed, LOW);
}

viod loop(){
  while (Serial.available()) {
      delay(1);
      char c = Serial.read();
      payload += c;
      payload1 = c;
    }  
    if(payload != ""){
      if(payload1 == "L"){
        Stop();
      }
      else{
        Serial.print(payload);
        turn = payload.toInt();
        Stearing.write(CurrentServoAngle-turn);
        //digitalWrite(DO_GLed, HIGH);
        //delay(500);
        //digitalWrite(DO_GLed, LOW);
        payload = "";
      }
    } 
} 
