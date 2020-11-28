import glob
import os
import sys
try:
    sys.path.append(glob.glob('../carla/dist/carla-*%d.%d-%s.egg' % (
        sys.version_info.major,
        sys.version_info.minor,
        'win-amd64' if os.name == 'nt' else 'linux-x86_64'))[0])
except IndexError:
    pass
import carla

import random
import time
import numpy as np
import cv2

IM_WIDTH = 640
IM_HEIGHT = 480


def process_img(image,l_images):
    i = np.array(image.raw_data) 
    # print(i.shape)
    i2 = i.reshape((IM_HEIGHT, IM_WIDTH, 4)) #rgba, a for alpha
    i3 = i2[:, :, :3] # /255.0 # entire height, entire width, only rgb (no alpha)
    print(i3[1 , 1, :])
    #import pdb; pdb.set_trace()
    #cv2.imshow("image", i3)
    #cv2.waitKey(0)
    l_images.append(i3)
    return #i3/255.0 # normalize the data


l_images = []
actor_list = []
try:
    client = carla.Client('localhost', 2000)
    client.set_timeout(10.0)

    world = client.get_world()

    blueprint_library = world.get_blueprint_library()

    bp = blueprint_library.filter('model3')[0]
    print(bp)

    spawn_point = random.choice(world.get_map().get_spawn_points())

    vehicle = world.spawn_actor(bp, spawn_point)
    vehicle.apply_control(carla.VehicleControl(throttle=1.0, steer=0.0))
    # vehicle.set_autopilot(True)  # if you just wanted some NPCs to drive.

    actor_list.append(vehicle)

    # https://carla.readthedocs.io/en/latest/cameras_and_sensors
    # get the blueprint for this sensor
    blueprint = blueprint_library.find('sensor.camera.rgb')
    # change the dimensions of the image
    blueprint.set_attribute('image_size_x', f'{IM_WIDTH}')
    blueprint.set_attribute('image_size_y', f'{IM_HEIGHT}')
    blueprint.set_attribute('fov', '110')

    # Adjust sensor relative to vehicle
    spawn_point = carla.Transform(carla.Location(x=2.5, z=0.7))

    # spawn the sensor and attach to vehicle.
    sensor = world.spawn_actor(blueprint, spawn_point, attach_to=vehicle)

    # add sensor to list of actors
    actor_list.append(sensor)

    # do something with this sensor
    sensor.listen(lambda data: process_img(data,l_images))

    time.sleep(5)
    sensor.stop()

    for im in l_images:
        cv2.imshow('image', im)
        cv2.waitKey(16)

finally:
    print('destroying actors')
    for actor in actor_list:
        actor.destroy()
    print('done.')
