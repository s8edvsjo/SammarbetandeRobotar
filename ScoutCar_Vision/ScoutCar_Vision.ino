#include <SoftwareSerial.h>
#include <Servo.h>
#include "EspMQTTClient.h"

#define Hallgivare 14 // D5
#define pwm_b 5 // D1 Speed
#define dir_b1 0 // D3
#define DO_RLed 13 //D7
#define DO_GLed 12 //D6

Servo Stearing; // 0=Höger , 180=Vänster , 93=Rakt
SoftwareSerial ESPserial(3, 1);

String payload;
int turn;
int CurrentServoAngle = 93;
float distanceCm = 0;
float hjulvarv = 0;
float signals = 0;

void setup() {
  Serial.begin(9600);
  pinMode(12, INPUT); // Hallgivare Signal pin
  pinMode(dir_b1, OUTPUT);
  pinMode(pwm_b, OUTPUT);
  pinMode(DO_RLed, OUTPUT);
  pinMode(DO_GLed, OUTPUT);
  Stearing.attach(15); //D8 Servo
  attachInterrupt(digitalPinToInterrupt(Hallgivare), HtoL, FALLING); // Interupt 
}




void loop() {
  analogWrite(pwm_b, 300);
  digitalWrite(dir_b1, LOW); // Framåt
  Serial.print("go");
  
  hjulvarv = signals / 135;
  distanceCm = hjulvarv * 3.7 * PI;
  Serial.print("Distance= ");
  Serial.println(distanceCm);
  
  while (Serial.available()) {
    delay(1);
    char c = Serial.read();
    payload += c;  
  }
  
  if(payload != ""){
    Serial.println(payload);
    turn = payload.toInt();
    Stearing.write(CurrentServoAngle-turn);
    digitalWrite(DO_GLed, HIGH);
    payload = "";
  }
}



ICACHE_RAM_ATTR void HtoL(){signals++;} // räknar varv med hjälp av interupt funktionen.

void onConnectionEstablished();
EspMQTTClient client(
 "ABB_Indgym_Guest",                           // Wifi ssid
  "Welcome2abb",                              // Wifi password
  "maqiatto.com",                            // MQTT broker ip
  1883,                                     // MQTT broker port
  "edvin.sjogren@abbindustrigymnasium.se", // MQTT username
  "sjogren",                              // MQTT password
  "Edvin",                               // Client name
  onConnectionEstablished,              // Connection established callback
  true,                                // Enable web updater
  true                                // Enable debug messages
);



void onConnectionEstablished(){
  client.publish("edvin.sjogren@abbindustrigymnasium.se/Matrix", [] (const String &payload){
  });
}
