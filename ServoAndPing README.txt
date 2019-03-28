ServoAndPing.py README

No outside libraries are needed.

This is the code for the servo motors and the 
ultrasonic (ping) sensor. There are four methods,
look at the comments in the code for descriptions.
The pi does not nativaly run more than one servo,
so I had to research a work around which has a 
few bugs, but works. DO NOT CHANGE THE 
VALUES IN THE METHODS! It took me a while to
calibrate them. Distance is in cm.
 
I think this file is where we should add our main code.
I added an infinite loop at the end that reads the distance.
Within this loop, we can check for if an object is less than
x cm away (default to trash opening), between x and y (start
taking pics and image process), and greater than y (ignore
the camera readings or turn off the camera).
---Jared