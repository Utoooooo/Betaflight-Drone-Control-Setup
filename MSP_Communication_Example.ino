#include <HardwareSerial.h>
#include <MSP.h>

MSP msp;
unsigned long myTime;
HardwareSerial Telemetry(2);

void setup() {
  Telemetry.begin(115200,SERIAL_8N1,25,26);
  Serial.begin(9600);
  msp.begin(Telemetry);
}

void loop() {
  msp_rc_t rc;
  if (msp.request(MSP_RC, &rc, sizeof(rc))) {
    
    uint16_t roll     = rc.channelValue[0];
    uint16_t pitch    = rc.channelValue[1];
    uint16_t yaw      = rc.channelValue[2];
    uint16_t throttle = rc.channelValue[3];
    Serial.println(roll);
  }
}
