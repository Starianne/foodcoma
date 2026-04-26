const int buttonPins[] = {2, 3, 4};
const int trigPin = 9;
const int echoPin = 10;

long duration;
int distance;

const int numButtons = 3;
bool lastState[3] = {LOW, LOW, LOW};

#define ANALOG_X_PIN A2
#define ANALOG_Y_PIN A3

#define ANALOG_X_CORRECTION 128
#define ANALOG_Y_CORRECTION 128
#define DEADZONE 20

struct button
{
    byte pressed = 0;
};

struct analog
{
    short x, y;
    button button;
};

void setup()
{
    Serial.begin(9600);
    for (int i = 0; i < numButtons; i++)
    {
        pinMode(buttonPins[i], INPUT);
    }
    pinMode(trigPin, OUTPUT);
    pinMode(echoPin, INPUT);
}

void loop()
{
    for (int i = 0; i < numButtons; i++)
    {
        bool state = digitalRead(buttonPins[i]);
        if (state == HIGH && lastState[i] == LOW)
        {
            Serial.println("B" + String(i));
        }

        lastState[i] = state;
    }

    digitalWrite(trigPin, LOW);
    delayMicroseconds(2);
    digitalWrite(trigPin, HIGH);
    delayMicroseconds(10);
    digitalWrite(trigPin, LOW);

    duration = pulseIn(echoPin, HIGH, 30000);

    if (duration == 0)
    {
        delay(50);
        return;
    }
    distance = duration * 0.034 / 2;
    if (distance < 20)
    {
        Serial.println("D20");
    }
    else if (distance < 50)
    {
        Serial.println("D50");
    }
    else if (distance < 100)
    {
        Serial.println("D100");
    }
    else
    {
        Serial.println("D200");
    };

    analog analog;

    analog.x = readAnalogAxisLevel(ANALOG_X_PIN) - ANALOG_X_CORRECTION;
    analog.y = readAnalogAxisLevel(ANALOG_Y_PIN) - ANALOG_Y_CORRECTION;

    bool xHigh = analog.x > DEADZONE;
    bool xLow = analog.x < -DEADZONE;
    bool yHigh = analog.y > DEADZONE;
    bool yLow = analog.y < -DEADZONE;

    if (xLow)
    {
        Serial.println("JL");
    }
    else if (xHigh)
    {
        Serial.println("JR");
    }
    else if (yLow)
    {
        Serial.println("JU");
    }
    else if (yHigh)
    {
        Serial.println("JD");
    }

    delay(50); // Simple debounce
}

byte readAnalogAxisLevel(int pin)
{
    return map(analogRead(pin), 0, 1023, 0, 255);
}

bool isAnalogButtonPressed(int pin)
{
    return digitalRead(pin) == 0;
}