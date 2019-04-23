const int trigger1 = 2; //Trigger pin of 1st Sesnor
const int echo1 = 3; //Echo pin of 1st Sesnor

long time_taken;
int dist,distL;

 

void setup() {
Serial.begin(9600); 
  
pinMode(trigger1, OUTPUT); 
pinMode(echo1, INPUT); 
}

/*###Function to calculate distance###*/
void calculate_distance(int trigger, int echo)
{
digitalWrite(trigger, LOW);
delayMicroseconds(2);
digitalWrite(trigger, HIGH);
delayMicroseconds(10);
digitalWrite(trigger, LOW);

time_taken = pulseIn(echo, HIGH);
dist= time_taken*0.034/2;
if (dist>60)
dist = 60;
//Serial.println(dist);
}

void loop() { //infinite loopy
calculate_distance(trigger1,echo1);

if(dist-distL>=4){
  Serial.println("movedback");
}
if(distL-dist>=4){
  Serial.println("movedfront");
}
if(distL==dist){
  Serial.println("Stay");
}
distL=dist;
delay(2000);
}
