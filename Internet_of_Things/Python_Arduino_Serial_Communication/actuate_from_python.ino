int duration=1000;// 1 sec == 1000ms            

void check_serial(){
  if (Serial.available()>0){
    byte ch=Serial.read();
    
    if(ch == 49) // LONGER DURATION
    {
      duration*=2;
    }
    else if(ch == 50)  // SHORTER DURATION
    {
      duration/=2;
    }
  }
}


void setup() {  
  DDRB = B00100000;   //SETS PIN13 AS OUTPUT
  Serial.begin(9600); 
}

void loop() {
  PORTB |= B00100000; //SET PIN13 HIGH
  check_serial();
  delay(duration*3);
  
  PORTB &= ~B00100000; //SET PIN13 LOW
  check_serial(); 
  delay(duration);
}
