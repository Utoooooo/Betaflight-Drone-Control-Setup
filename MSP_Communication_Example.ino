#include <WiFi.h>
#include <WiFiUdp.h>
#include <HardwareSerial.h>
#include <MSP.h>

//Wifi UDP Settings
const char* ssid = "ground_station";
const char* password = "johnsm1th";
WiFiUDP udp;

MSP msp;
unsigned long myTime;
HardwareSerial Telemetry(2);

void setup() {

  WiFi.begin(ssid, password);
  while (WiFi.status() != WL_CONNECTED) {
    delay(1000);
  }
  pinMode(LED, OUTPUT); 
  Telemetry.begin(115200,SERIAL_8N1,25,26);
  Serial.begin(9600);
  msp.begin(Telemetry);
  udp.begin(8888);
}

void loop() {
  uint8_t buf[5];  // Create a buffer to hold the received data
  // Check if data is available
  int packetSize = udp.parsePacket();
  if (packetSize) {
    // Receive the data into the buffer
    udp.read(buf, 5);
    Serial.println(buf);
  }
  msp_rc_t rc;
  if (msp.request(MSP_RC, &rc, sizeof(rc))) {
    
    uint16_t roll     = rc.channelValue[0];
    uint16_t pitch    = rc.channelValue[1];
    uint16_t yaw      = rc.channelValue[2];
    uint16_t throttle = rc.channelValue[3];
    Serial.println(roll);
  }
}
