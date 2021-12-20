int sensorval = 0;
void setup() {  
  Serial.begin(9600); 
}

void loop() {
  sensorval = analogRead(A1);
  Serial.write(sensorval);
  delay(1000);
}
