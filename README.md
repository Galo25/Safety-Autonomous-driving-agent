# Safety-Autonomous-driving-agent
Reinforcement learning (RL) has become a powerful learning framework now capable of learning complex policies in high dimensional environments. This repository demonstrates deep reinforcement learning (DRL) algorithms, provides a taxonomy of automated driving tasks.


Requirements: 

Install carla, FOLLOW THE steps at : https://carla.readthedocs.io/en/latest/

Take all files in this reposetories and drop/replace into CARLA folder at:  /PythonAPI/examples

Insall packages:

tensorflow-gpu==1.12.0

numpy

scipy

tensorboard==1.14.0

------------------------
Deep dive into the code: 
------------------------
Check out our PPT that 

----------------
Run Carla demo : 
----------------
 1.Run CarlaUE4.exe
 
 2.Open folder /PythonAPI/examples and open CMD on this location. (Type CMD at the folder path)
 
 3.In order to Add 80 cars : type: py -3.7 spawn_npc.py -n 80 
 
 4.Manual control : open another CMD and type : py -3.7 manual_control.py

----------------
Run Agent : 
----------------
Run test agent : py -3.7 tutorial-video-2.py            
Run main : py -3.7 main.py

----------------
View results : 
----------------
Check tensorBoard : CMD in examples and type : tensorboard --logdir=logs/

Then open browser and type: localhost:6006 


----------------
Credits : 
----------------
Msc. Project in "Autonomou Vehicle".

Team:  Gal Inbar, Eliav Shalelashvili, Shay Dondik 

Implementation of article : "Autonomous Highway Driving using Deep Reinforcement Learning".
https://www.researchgate.net/publication/332140365_Autonomous_Highway_Driving_using_Deep_Reinforcement_Learning



