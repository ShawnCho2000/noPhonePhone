const int ledPin = 9;  //pin 9 has PWM funtion
const int potPin = A0; //pin A0 to read analog input

//Variables:
int value; //save analog value


void setup(){
  Serial.begin(9600);
  pinMode(LED_BUILTIN, OUTPUT);
}

void loop(){
  int sensorValue = analogRead(A0);
  if (sensorValue > 600) {
    digitalWrite(LED_BUILTIN, HIGH);
  } else if (sensorValue < 100) {
    digitalWrite(LED_BUILTIN, LOW);
  }
  Serial.println(sensorValue);
//  Serial.println(value++);
  delay(1);//Small delay

}