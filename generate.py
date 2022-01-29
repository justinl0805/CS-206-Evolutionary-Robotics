import pyrosim.pyrosim as pyrosim


def Create_World():
    pyrosim.Start_SDF("world.sdf")

    x = -2
    y = 0.5
    z = 3

    length = 1
    width = 1
    height = 1

    pyrosim.Send_Cube(name="Box", pos=[x, z, y], size=[length, width, height])
    pyrosim.End()


def Create_Robot():
    pyrosim.Start_URDF("body.urdf")

    length = 1
    width = 1
    height = 1

    pyrosim.Send_Cube(name="Link0", pos=[0, 0, 0.5], size=[length, width, height])

    pyrosim.Send_Joint(name="Link0_Link1", parent="Link0", child="Link1", type="revolute", position=[0, 0, 1])

    pyrosim.Send_Cube(name="Link1", pos=[0, 0, 0.5], size=[length, width, height])

    pyrosim.Send_Joint(name="Link1_Link2", parent="Link1", child="Link2", type="revolute", position=[0, 0, 1])

    pyrosim.Send_Cube(name="Link2", pos=[0, 0, 0.5], size=[length, width, height])

    pyrosim.Send_Joint(name="Link2_Link3", parent="Link2", child="Link3", type="revolute", position=[0, 0.5, 0.5])

    pyrosim.Send_Cube(name="Link3", pos=[0, 0.5, 0], size=[length, width, height])

    pyrosim.Send_Joint(name="Link3_Link4", parent="Link3", child="Link4", type="revolute", position=[0, 0.5, 0])

    pyrosim.Send_Cube(name="Link4", pos=[0, 0.5, 0], size=[length, width, height])

    pyrosim.Send_Joint(name="Link4_Link5", parent="Link4", child="Link5", type="revolute", position=[0, 0.5, -0.5])

    pyrosim.Send_Cube(name="Link5", pos=[0, 0, -0.5], size=[length, width, height])

    pyrosim.Send_Joint(name="Link5_Link6", parent="Link5", child="Link6", type="revolute", position=[0, 0, -0.5])

    pyrosim.Send_Cube(name="Link6", pos=[0, 0, -0.5], size=[length, width, height])

    pyrosim.Send_Joint(name="Link6_Link7", parent="Link6", child="Link7", type="revolute", position=[0, 0, -0.5])

    pyrosim.Send_Cube(name="Link7", pos=[0, 0, -0.5], size=[length, width, height])

    pyrosim.End()


Create_Robot()
Create_World()

'''
for k in range(0, 5):
    x_offset = 1.1 * k
    for j in range(0, 5):
        z_offset = 1.1 * j

        stored = 1
        for i in range(0, 10):
            y_offset = 1.1 * i

            x = 0 + x_offset
            y = 0.5 + y_offset
            z = 0 + z_offset

            stored = stored * 0.9

            length = stored
            width = stored
            height = stored

            pyrosim.Send_Cube(name="Box2", pos=[z, x, y], size=[length, width, height])'''

'''x = 1
y = 0
z = 1.5

length = 1
width = 1
height = 1

pyrosim.Send_Cube(name="Box2", pos=[x, y, z], size=[length, width, height])
'''
