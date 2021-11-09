from manual import *;

motor1 = Motor(0,1,-1);
motor2 = Motor(1,-1,-1);

motor1.changeLength(1,-1);
motor2.changeLength(1,-1);

print(motor1.length, motor2.length);



