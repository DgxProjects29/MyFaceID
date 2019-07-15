//#include <Servo.h>

#include <SoftwareSerial.h>
  
SoftwareSerial mySerial(11,10);// RX,TX 38400

//Servo serv;

int button =  6;
int servo = 5;
const int pinLED = 13;

char DATO = '0';

void setup() {
  mySerial.begin(9600);
  pinMode(button,INPUT);
  pinMode(pinLED, OUTPUT);

  //serv.attach(servo);
  
}

void loop() {
  if(mySerial.available() > 0){
      DATO = mySerial.read();
  }
     
  if(DATO == '1') {
       digitalWrite(pinLED, HIGH);
       //serv.write(90);
  }else{
    digitalWrite(pinLED, LOW);
    //serv.write(0);
  }
  

  //Serial.println("-->  "+digitalRead(button));
  if(digitalRead(button)==HIGH){
    DATO = '0';
    digitalWrite(pinLED, LOW);
    mySerial.println('0');
  }else{
    mySerial.println('2');
  }

  delay(500);

}
