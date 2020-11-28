
* Install carla, FOLLOW THE steps at : https://carla.readthedocs.io/en/latest/

----------------
Run demo : 
----------------
 1.load carla
 2.Open PythonAPI/examples and run CMD
 3.Add 80 cars : type: py -3.7 spawn_npc.py -n 80 
 4.Manual control : open another CMD in examples and type : py -3.7 manual_control.py


Run test agent : py -3.7 tutorial-video-2.py
Run main : py -3.7 main.py


Check tensorBoard : CMD in examples and type : tensorboard --logdir=logs/
Then open : localhost:6006 in browser 