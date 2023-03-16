
#include <WiFi.h>
#include <WiFiUdp.h>
#include <HardwareSerial.h>

//Wifi UDP Settings
const char* ssid = "ground_station";
const char* password = "johnsm1th";
WiFiUDP udp;

//Sync LED
int LED = 33;
int16_t buffer = 0;

void setup() {

  WiFi.begin(ssid, password);
  while (WiFi.status() != WL_CONNECTED) {
    delay(1000);
  }
  pinMode(LED, OUTPUT); 
  Serial.begin(9600);
  udp.begin(8888);
}


void loop() {
  uint8_t buf[5];  // Create a buffer to hold the received data
  // Check if data is available
  int packetSize = udp.parsePacket();
  if (packetSize) {
    // Receive the data into the buffer
    udp.read(buf, 5);
    Serial.print("Received array: [");
    for (int i = 0; i < 5; i++) {
      Serial.print(buf[i]);
      if (i < 4) {
        Serial.print(", ");
      }
    }
    Serial.println("]");
    if (buf[0]==1){
      digitalWrite(LED, HIGH);
    }
    else{digitalWrite(LED, LOW);
    }
  }
}
