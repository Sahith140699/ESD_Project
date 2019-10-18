int d_pin[8]; //Data Pins
int data[8]; // Current Values
int pdata[8]; //Previous Values

unsigned long lastDebounceTime[8] ;  // the last time the output pin was toggled
unsigned long debounceDelay = 25;    // the debounce time; increase if the output flickers

int i = 0;
int r,c;
byte pb,pb_prev,mode,mode_prev;
int num = 0;

void setup() {
  pb_prev = 40;
  mode_prev = 1;
  d_pin[6] = 2;
  d_pin[7] = 3;
  for(i=0;i<6;i++)
  { d_pin[i]=i+4;
    lastDebounceTime[i] = 0;
    pinMode(d_pin[i],INPUT_PULLUP);
    pdata[i] = HIGH;
  }
  lastDebounceTime[6] = 0;
  lastDebounceTime[7] = 0;
  pinMode(d_pin[6],INPUT_PULLUP);
  pinMode(d_pin[7],INPUT_PULLUP);
  Serial.begin(9600);
}

void loop() {
  int j = 0;
  for(j=0; j<8; j++)
  {
    int reading = digitalRead(d_pin[j]);
    if (reading != pdata[j]) {
    // reset the debouncing timer
    lastDebounceTime[j] = millis();
  }
  if ((millis() - lastDebounceTime[j]) > debounceDelay) {
    // if the button state has changed:
    if (reading != data[j]) {
      data[j] = reading;
    }
  }
  pdata[j] = reading;
  }
  if(data[0]==0)
r=0;
else if(data[1]==0)
r=1;
else if(data[2]==0)
r=2;
else
r=10;

if(data[3]==0)
c=0;
else if(data[4]==0)
c=1;
else if(data[5]==0)
c=2;
else
c=10;

for(i=0;i<6;i++)
{
  num += data[i];
}

pb=3*r+c;
if(pb != pb_prev && num == 4)
{
//  Serial.write(data);  
Serial.println(pb);
}
pb_prev = pb;
num = 0;
}
