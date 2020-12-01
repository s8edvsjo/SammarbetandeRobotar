#include <Wire.h>
#include <VL53L0X.h>
#include <SoftwareSerial.h>
#include "EspMQTTClient.h"
VL53L0X sensor;
int DistanceSensor;

void onConnectionEstablished();
EspMQTTClient client(
 "ABB_Indgym",                               // Wifi ssid
  "7Laddaremygglustbil",                                  // Wifi password Welcome2abb
  "maqiatto.com",                                // MQTT broker ip
  1883,                                         // MQTT broker port
  "victor.fagerstrom@abbindustrigymnasium.se", // MQTT username
  "hejhej",                                   // MQTT password
  "Edvin",                                   // Client name
  onConnectionEstablished,                  // Connection established callback
  true,                                    // Enable web updater
  true                                    // Enable debug messages
);

void onConnectionEstablished(){
  client.subscribe("victor.fagerstrom@abbindustrigymnasium.se/Hinder", [] (const String &payload){
  });
}



void setup() {
  Serial.begin(9600);
  Wire.begin(10, 14);
  sensor.init();
  sensor.setTimeout(500);
  sensor.startContinuous();
}

void loop() {
  client.loop();
  DistanceSensor = sensor.readRangeContinuousMillimeters();
  Serial.print(DistanceSensor);
  if (DistanceSensor < 70){
  Grip(); 
  }
  Serial.print(sensor.readRangeContinuousMillimeters());
  if (sensor.timeoutOccurred()) { Serial.print(" TIMEOUT"); }
    Serial.println();

}

void Grip(){
  client.publish("victor.fagerstrom@abbindustrigymnasium.se/Hinder", "LG");
}

