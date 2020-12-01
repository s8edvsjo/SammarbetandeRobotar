#include "EspMQTTClient.h"
#include <Servo.h>
#include <SoftwareSerial.h>
#define pwm_b 5
#define dir 0
#define hallGivarPin 12
#define DO_RLed 13 //D7
#define DO_GLed 12 //D6

String payload;
SoftwareSerial ESPserial(3, 1);

/*void onConnectionEstablished();
EspMQTTClient client(    
  "ABB_Indgym_Guest",
  "Welcome2abb",
  "maqiatto.com",
  1883,
  "victor.fagerstrom@abbindustrigymnasium.se",
  "hejhej",
  "Scoutbil", //Olika för varje bil
  onConnectionEstablished,
  true,
  true    
);*/

//setup
 
void setup() {
  Serial.begin(9600);
  pinMode(DO_RLed, OUTPUT);
  pinMode(pwm_b, OUTPUT);
  digitalWrite(DO_RLed, HIGH);
  delay(2000);
  digitalWrite(DO_RLed, LOW);
}

/*void onConnectionEstablished(){
  client.subscribe("victor.fagerstrom@abbindustrigymnasium.se/POS", [] (const String &payload){
  });
  client.subscribe("victor.fagerstrom@abbindustrigymnasium.se/Hinder", [] (const String &payload){
    if (payload == "LG"){
      //Hinder =true;
      Stop();
      Serial.println("Stop");
    }else {
      //Hinder =false;
    }
  });
}*/

 void Stop(){
  analogWrite(pwm_b, 0);
  digitalWrite(DO_RLed, HIGH);
  delay(3000);
  digitalWrite(DO_RLed, LOW);
}
 
void loop() { 
  //client.loop();
  //Serial.println(payload);
  analogWrite(pwm_b, 350);
  //client.publish("victor.fagerstrom@abbindustrigymnasium.se/POS","hej");   
  if (Serial.available()) {
    delay(1);
    char c = Serial.read();
    payload = String(c);
    Serial.println(payload);
    if(payload == "L") {
      Stop();  
    }
  }
}
  

   

