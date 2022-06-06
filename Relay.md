#2022_06_06

```
int Relay = 3;

void setup() {
  Serial.begin(9600);
  pinMode(Relay,OUTPUT);
}  

void loop() {
  int cds = analogRead(A1);
  Serial.println(cds);

  if(cds < 270){
    digitalWrite(Relay,HIGH);
    delay(500);
  }
  
  else{
    digitalWrite(Relay,LOW);
   delay(500);
  }
}
```
