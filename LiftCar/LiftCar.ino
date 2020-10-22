#include <Servo.h>
#include <VL53L0X.h>
#include <Wire.h>
#define pwm_b 5 //D1
#define dir_b1 0 //D3
Servo Stearing; // 0=Vänster , 180=Höger
Servo Gripp;
Servo Lift;
VL53L0X sensor;
int DistanceSensor;

 

void setup() {
  Serial.begin(9600);
  Wire.begin(10, 14);
  sensor.init();
  sensor.setTimeout(500);
  sensor.startContinuous();
  pinMode(dir_b1, OUTPUT);
  pinMode(pwm_b, OUTPUT);
  Stearing.attach(15); //D8
  Lift.attach(13); //D7
  Gripp.attach(12); //D6
  Stearing.write(88);
  Gripp.write(0); //öppen
}
void loop() {
  analogWrite(pwm_b, 700);
  digitalWrite(dir_b1, LOW);
  DistanceSensor = sensor.readRangeContinuousMillimeters();
  Serial.print(DistanceSensor);
  if (DistanceSensor < 70){
    analogWrite(pwm_b, 0);
    Grip(); 
  }
  Serial.print(sensor.readRangeContinuousMillimeters());
  if (sensor.timeoutOccurred()) { Serial.print(" TIMEOUT"); }
    Serial.println();
}

 

void Grip(){
  Serial.println("Ner");
  Gripp.write(0); //öppen
  Lift.write(0); //Ner
  delay(1700);
  Lift.write(90); //stanna
  Gripp.write(70); //stängd
  delay(1000);
  Serial.println("Upp");
  Lift.write(180);
  delay(2000);
  Serial.println("Stop");
  Lift.write(90);
}
