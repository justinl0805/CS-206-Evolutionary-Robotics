import pybullet as p
import pybullet_data
import time

physicsClient = p.connect(p.GUI)
p.setAdditionalSearchPath(pybullet_data.getDataPath())

p.setGravity(0, 0, -9.8)
planeId = p.loadURDF("plane.urdf")

p.loadSDF("boxes.sdf")

for x in range(12000):
    p.stepSimulation()
    print(x)
    time.sleep(1/60)

p.disconnect()