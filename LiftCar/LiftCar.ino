#include <Servo.h>
#define pwm_b 5 //D1
#define dir_b1 0 //D3
Servo Stearing; // 0=Vänster , 180=Höger
Servo Gripp;
Servo Lift;


void setup() {
  Serial.begin(9600);
  pinMode(dir_b1, OUTPUT);
  pinMode(pwm_b, OUTPUT);
  
  Stearing.attach(15); //D8
  Lift.attach(13); //D7
  Gripp.attach(12); //D6
 
  Stearing.write(88);
  Gripp.write(0); //öppen
  
}

void loop() {
  /*Serial.println("Ner");
  Lift.write(0);
  delay(1600);
  Lift.write(90);
  Grip.write(70); //stängd
  delay(1000);
  Serial.println("Upp");
  Lift.write(180);
  delay(2000);
  Serial.println("Stop");
  Lift.write(90);
  Grip.write(0); //öppen
  delay(1000);*/
  Grip();
}

void Grip(){
  Serial.println("Ner");
  Lift.write(0);
  delay(1600);
  Lift.write(90);
  Gripp.write(70); //stängd
  delay(1000);
  Serial.println("Upp");
  Lift.write(180);
  delay(2000);
  Serial.println("Stop");
  Lift.write(90);
  Gripp.write(0); //öppen
  delay(1000);
}


/*
  analogWrite(pwm_b, 500);
  digitalWrite(dir_b1, HIGH);
  Serial.print("go");
  delay(1000);
  digitalWrite(dir_b1, LOW);
  analogWrite(pwm_b, 500);
  Serial.print("stop");
  delay(1000);*/
