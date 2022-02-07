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
# influxdb install
```
sudo apt update
sudo apt upgrade

wget -qO- https://repos.influxdata.com/influxdb.key | sudo apt-key add -

echo "deb https://repos.influxdata.com/debian stretch stable" | sudo tee /etc/apt/sources.list.d/influxdb.list

sudo apt update
sudo apt install influxdb

sudo systemctl unmask influxdb
sudo systemctl enable influxdb
sudo systemctl start influxdb
```
#grafana databases install

```
생성 : influx
[ex) >create database <database>]
확인 : show databases 
```

# grafana install
```
wget -q -O - https://packages.grafana.com/gpg.key | sudo apt-key add -

echo "deb https://packages.grafana.com/oss/deb stable main" | sudo tee -a /etc/apt/sources.list.d/grafana.list

sudo apt update
sudo apt install grafana
```
# grafana start
```
sudo service grafana-server start
구글가서 127.0.0.1:3000
```
#in Grafana

```
1.  datasourse 만들기
2.  panel 만들기
```
