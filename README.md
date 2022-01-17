# arduino source lux
```C
int Cds =0;

void setup() {
  Serial.begin(9600);
  pinMode(A1,INPUT);
}

void loop() {
  Cds = analogRead(A1);
  Serial.println(Cds);
  delay(1000);
}
```
