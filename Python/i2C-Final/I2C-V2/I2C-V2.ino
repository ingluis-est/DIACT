//============================================================config I2C
#include <Wire.h>
#define I2C_SLAVE_ADDRESS 11 //
#define I2C_SLAVE2_ADDRESS 12 //
#define I2C_SLAVE3_ADDRESS 13 //
#define PAYLOAD_SIZE 2
//============================================================config I2C
//============================================================config ultrasonicos SEC1
#include "NewPing.h"      // include NewPing library
//===============Ultra Izquierdo
int trigPin = 2;      // trigger pin
int echoPin = 3;      // echo pin
int distance=0;
//===============Ultra Frontal
int trigPinF = 4;      // trigger pin
int echoPinF = 5;      // echo pin
int distanceF=0;
//===============Ultra Derecho
int trigPinR = 11;      // trigger pin
int echoPinR = 12;
int distanceR=0;
//===============Definimos los ultra

int dist[]={distance, distance, distance};

NewPing sonar(trigPin, echoPin);
NewPing sonarF(trigPinF, echoPinF);
NewPing sonarR(trigPinR, echoPinR);

//============================================================config ultrasonicos SEC1

void setup() {
  Wire.begin(I2C_SLAVE_ADDRESS);
  Serial.begin(9600);
  Serial.println("arduino nano esclavo");
  Wire.onRequest(requestEvents);
  Wire.onReceive(receiveEvents);

}
void loop(){
  distance = sonar.ping_cm();
  distanceF = sonarF.ping_cm();
  distanceR = sonarR.ping_cm();
  Serial.println(distance);
  Serial.println(distanceF);
  Serial.println(distanceR);
  delay(2000);
  }

void requestEvents(){
  Wire.write(distance);
  Wire.write(distanceF);
  Wire.write(distanceR);

}

void receiveEvents(int numBytes){
  //Serial.println(F("evento recibido"));
  //Serial.print(distance);
  //Serial.print(distanceF);
  //Serial.print(distanceR);
}
