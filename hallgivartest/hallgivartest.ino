#include <Servo.h>
#define pwm_b 5 // D1 Speed
#define dir_b1 0 // D3
Servo Stearing; // 0=Höger , 180=Vänster , 93=Rakt

void setup() {
  Serial.begin(9600);
  pinMode(dir_b1, OUTPUT);
  pinMode(pwm_b, OUTPUT);
  Stearing.attach(15); //D8 Servo
  Stearing.write(93);
  delay(1000);
}

void loop() {
  Stearing.write(93);
  analogWrite(pwm_b, 0);
  delay(4000);
  analogWrite(pwm_b, 300);
  digitalWrite(dir_b1, LOW); // Framåt
  TurnL();
}

void TurnL(){
  Stearing.write(150);
  delay(2600);
}

