from robodk.robolink import *    # API para comunicarte con RoboDK
from robodk.robomath import *    # Funciones matemáticas
import math

#------------------------------------------------
# 1) Conexión a RoboDK e inicialización
#------------------------------------------------
RDK = Robolink()

# Elegir un robot (si hay varios, aparece un popup)
robot = RDK.ItemUserPick("Selecciona un robot", ITEM_TYPE_ROBOT)
if not robot.Valid():
    raise Exception("No se ha seleccionado un robot válido.")

#------------------------------------------------
# 2) Cargar el Frame (ya existente)
#------------------------------------------------
frame_name = "Frame_from_Target1"
frame = RDK.Item(frame_name, ITEM_TYPE_FRAME)
if not frame.Valid():
    raise Exception(f'No se encontró el Frame "{frame_name}" en la estación.')
#------------------------------------------------
frame_name_3 = "Frame_3"
frame_3 = RDK.Item(frame_name_3, ITEM_TYPE_FRAME)
if not frame_3.Valid():
    raise Exception(f'No se encontró el Frame "{frame_name_3}" en la estación.')

# Asignamos este frame al robot
robot.setPoseFrame(frame)
robot.setPoseTool(robot.PoseTool())

# Ajustes de velocidad y blending
robot.setSpeed(300)   # mm/s
robot.setRounding(5)  # blending (radio de curvatura)

#------------------------------------------------
# 3) Parámetros de la figura
#------------------------------------------------
num_points = 300
scale = 40
z_surface = 0
z_safe = 50
offset_y = 150

#------------------------------------------------
# 4) Calcular primer punto 
#------------------------------------------------
t0 = 0
theta0 = 2 * math.pi * t0 * 4
r0 = math.exp(math.sin(theta0)) - 2 * math.cos(4 * theta0) + math.sin((2 * theta0 - math.pi) / 24)**5
r0 *= scale
x0 = r0 * math.cos(theta0)
y0 = r0 * math.sin(theta0)
x_rot0 = y0
y_rot0 = -x0 + offset_y

# Movimiento al primer punto (sin dibujar)
robot.MoveJ(transl(x_rot0, y_rot0, z_surface + z_safe))
robot.MoveJ(transl(x_rot0, y_rot0, z_surface))  # bajar sin dibujar

#------------------------------------------------
# 5) Dibujar la figura (mariposa polar rotada -90°)
#------------------------------------------------
for i in range(num_points + 1):
    t = i / num_points
    theta = 2 * math.pi * t 

    sin_theta = math.sin(theta)
    cos_4theta = math.cos(4 * theta)
    sin_inner = math.sin((2 * theta - math.pi) / 24)
    
    r = math.exp(sin_theta) - 2 * cos_4theta + sin_inner**5
    r *= scale

    x = r * math.cos(theta)
    y = r * math.sin(theta)

    x_rot = y
    y_rot = -x + offset_y

    robot.MoveL(transl(x_rot, y_rot, z_surface))

#------------------------------------------------
# 6) Subir a altura segura y terminar
#------------------------------------------------
robot.MoveL(transl(x_rot, y_rot, z_surface + z_safe))
# Asignamos este frame al robot
robot.setPoseFrame(frame_3)
robot.setPoseTool(robot.PoseTool())
robot.MoveJ(transl(0, 0, 100))  # Movimiento relativo al nuevo Frame_3
