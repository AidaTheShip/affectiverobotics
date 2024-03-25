int pulse_sensor = A0;   // we are detecing an analog signal

int signal;                
int threshold = 550;       // when is something a beat 

void setup() {
	pinMode(LED_BUILTIN,OUTPUT);  // Built-in LED will blink to your heartbeat
	Serial.begin(9600);           // Set comm speed for serial plotter window
}

void loop() {

	Signal = analogRead(pulse_sensor); // Read the sensor value

	Serial.println(signal);                // writing out the signal 

	if(signal > thershold){                // If the signal is above threshold, turn on the LED
		digitalWrite(LED_BUILTIN,HIGH);
	} else {
		digitalWrite(LED_BUILTIN,LOW);     // Else turn off the LED
	}
	delay(10);
}