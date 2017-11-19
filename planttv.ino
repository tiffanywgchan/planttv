
#include <ESP8266WiFi.h>
#include <ESP8266HTTPClient.h>

const char* ssid     = "cisc340";
const char* password = "L0gica1@";
 
const char* host = "planttv.herokuapp.com";

const int analogPin = 17;

// the setup function runs once when you press reset or power the board
void setup() {
  Serial.begin(9600);
  delay(100);
 
  // We start by connecting to a WiFi network
 
  Serial.println();
  Serial.println();
  Serial.print("Connecting to ");
  Serial.println(ssid);
  
  WiFi.begin(ssid, password);
  
  while (WiFi.status() != WL_CONNECTED) {
    delay(500);
    Serial.print(".");
  }
 
  Serial.println("");
  Serial.println("WiFi connected");  
  Serial.println("IP address: ");
  Serial.println(WiFi.localIP());
}

// the loop function runs over and over again forever
void loop() {
  int val = analogRead(analogPin);
  
  Serial.println(String("") + "Sending POST request with value " + val + ".");
  HTTPClient http;
  http.begin(String("") + "http://" + host + "/data/");
  http.addHeader("Content-Type", "application/x-www-form-urlencoded");
  http.POST(String("") + "analog_value=" + val);
  http.writeToStream(&Serial);
  http.end();
  
  delay(5000);
}