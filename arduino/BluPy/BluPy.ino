#include <Servo.h>

#include <SoftwareSerial.h>
  
SoftwareSerial mySerial(11,10);// RX,TX 38400

Servo serv;

int button =  6;
int servo = 5;

int led_left_red = 4;
int led_right_red = 2;
int led_center_red = 3;

int led_green_1 = 7;
int led_green_2 = 8;
int led_green_3 = 9;

const int pinLED = 13;
int btState = 12;

char DATO = '2';
boolean button_pas = true;

void setup() {
  mySerial.begin(9600);
  pinMode(button,INPUT);

  pinMode(led_left_red, OUTPUT);
  pinMode(led_right_red, OUTPUT);
  pinMode(led_center_red, OUTPUT);

  pinMode(led_green_1, OUTPUT);
  pinMode(led_green_2, OUTPUT);
  pinMode(led_green_3, OUTPUT);

  pinMode(btState,INPUT);
  pinMode(pinLED, OUTPUT);

  serv.attach(servo);
  
}

void loop() {
  if(mySerial.available() > 0){
      DATO = mySerial.read();
  }

  if(DATO == '0'){

    //Red leds turns on, but servo is off
    digitalWrite(led_left_red, HIGH);
    digitalWrite(led_right_red, HIGH);
    digitalWrite(led_center_red, HIGH);
    serv.write(0);
    //Green Leds turns off
    digitalWrite(led_green_1, LOW);
    digitalWrite(led_green_2, LOW);
    digitalWrite(led_green_3, LOW);

  }else if(DATO == '1'){

    //Open Door
    digitalWrite(led_green_1, HIGH);
    digitalWrite(led_green_2, HIGH);
    digitalWrite(led_green_3, HIGH);
    serv.write(90);
    //Reds Leds turns off
    digitalWrite(led_left_red, LOW);
    digitalWrite(led_right_red, LOW);
    digitalWrite(led_center_red, LOW);

    button_pas = false;
    
  }else if(DATO == '2'){

    if (button_pas){

      //Turn off eveything
      digitalWrite(led_left_red, LOW);
      digitalWrite(led_right_red, LOW);
      digitalWrite(led_center_red, LOW);
      serv.write(0);
      digitalWrite(led_green_1, LOW);
      digitalWrite(led_green_2, LOW);
      digitalWrite(led_green_3, LOW);

    }
    
  }


  if(digitalRead(button)==HIGH){

    //Turn off everything when the buttons is pressed
    button_pas = true;
    DATO = '2';
    digitalWrite(led_left_red, LOW);
    digitalWrite(led_right_red, LOW);
    digitalWrite(led_center_red, LOW);
    serv.write(0);
    digitalWrite(led_green_1, LOW);
    digitalWrite(led_green_2, LOW);
    digitalWrite(led_green_3, LOW);
    
  }

  // Bluetooth state, whether is on or off, it will inform us
  if(digitalRead(btState)==LOW){
     digitalWrite(pinLED, LOW);
  }else{
     digitalWrite(pinLED, HIGH);  
  }

  // It was 500 before
  delay(15);
  
}
