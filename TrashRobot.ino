
#include <Servo.h>

Servo myservoTrash; 
Servo myservoCompost;
Servo myservoRecycle;
const int trigPin = 4;
const int echoPin = 3;
long duration;
int distance;

void setup() {
  pinMode(5,OUTPUT);
  pinMode(trigPin, OUTPUT); 
  pinMode(echoPin, INPUT);
  pinMode(2,OUTPUT);
  myservoTrash.attach(11);  
  myservoCompost.attach(10);  
  myservoRecycle.attach(9);
  pinMode(8,INPUT);
  pinMode(7,INPUT);
  pinMode(6,INPUT); 
  digitalWrite(5,HIGH);
  digitalWrite(2,LOW); 
}

void loop() {
  /*
  myservoTrash.write(90);
  myservoCompost.write(90);
  myservoRecycle.write(90);
  delay(3000);
  myservoTrash.write(180);
  myservoCompost.write(0);
  myservoRecycle.write(0);
  delay(3000);
  */
  delay(200);
  myservoTrash.write(90);
  myservoCompost.write(90);
  myservoRecycle.write(90);
  delay(100);
  

  digitalWrite(trigPin, LOW);
  delayMicroseconds(2);
  
  digitalWrite(trigPin, HIGH);
  delayMicroseconds(10);
  digitalWrite(trigPin, LOW);
  
  duration = pulseIn(echoPin, HIGH);

  distance= duration*0.034/2;

  if(distance<12){
     myservoTrash.write(180);
    delay(3000);
    myservoTrash.write(90);
    myservoCompost.write(90);
    myservoRecycle.write(90);
    delay(1300);
  }  
  if(digitalRead(8)){
    myservoTrash.write(180);
    delay(3000);
    myservoTrash.write(90);
    myservoCompost.write(90);
    myservoRecycle.write(90);
    delay(1300);
  }
  
  if(digitalRead(7)){
    myservoCompost.write(0);
    delay(3000);
    myservoTrash.write(90);
    myservoCompost.write(90);
    myservoRecycle.write(90);
    delay(1300);
  }
 
  if(digitalRead(6)){
    myservoRecycle.write(0);
    delay(3000);
    myservoTrash.write(90);
    myservoCompost.write(90);
    myservoRecycle.write(90);
    delay(1300);
  }

  delay(100);
  
 
  
}
