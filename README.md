# Laboratorio No.03
**Juliana Gongora Rasmussen**


_Ingeniería Mecatrónica_

Correo: jugongorar@unal.edu.co

---


**Gerhaldine Alejandra Suárez Bernal**
  
  _Ingeniería Mecatrónica_

Correo: gesuarezb@unal.edu.co
## 1. Cuadro Comparativo entre Motoman MH6 y IRB140
| Item | Motoman MH6| IRB140 |
| :---         |     :---:      |          ---: |
| Carga Máxima    | 6 kg     | 5 kg    |
| Número de grados de liberad  | 6       | 6      |
| Velocidad    |      |     |
| Eje 1   | 140 °/s     | 200°/s    |
| Eje 2    | 130 °/s     | 200 °/s    |
| Eje 3    | 135 °/s     | 260 °/s    |
| Eje 4    | 270 °/s     | 360 °/s    |
| Eje 5    | 270 °/s    | 360 °/s    |
| Eje 6    | 400 °/s     | 450 °/s    |
| Aplicaciones típicas    |     |     |
| 1   | Manipulación de materiales     | Manipulación de alta precisión    |
| 2   | Empaque y paletizado     | Pruebas de calidad o inspección con cámaras|    
| 3   |   Ensamblaje de componentes medianos o livianos  | Atención de máquinas para piezas pequeñas    |
| 4   | Soldadura por arco     | Montaje electrónico o mecánico    |
| 5   | Pulido y desbarbado con herramientas abrasivas     |  Pulido o acabado superficial de piezas pequeñas   |
| 6   | Aplicación de adhesivos o selladores     |  Aplicación de pintura o recubrimientos en espacios reducidos   |
| Alcance  | 1422 mm     |  810 mm   |
| Consumo de potencia | 1.5 kVA | 4.5 kVA|
| Masa | 130 kg | 98 kg |
| Protección IP |  Muñeca: IP67 , Cuerpo: IP54   |  Muñeca: IP67 , Cuerpo: IP30  | 
| Software de simulación | RobotStudio | RoboDK |
| Repetibilidad | ± 0.08 mm | ± 0.03 mm |

## 2. Descripción de las diferencias entre Home 1 y Home 2 del robot Motoman MH6

El robot Motoman MH6 dispone de dos posiciones de referencia comúnmente utilizadas en programación y operación: Home 1 y Home 2. Estas posiciones cumplen funciones distintas dentro del entorno de trabajo del robot. A continuación se describen sus principales diferencias:

### Home 1

- Es la posición de origen predeterminada de fábrica.
- Se utiliza como referencia para calibración, mantenimiento y verificación de ejes.
- No puede ser modificada por el usuario.
- En esta posición, los ejes del robot se ubican en una configuración estándar definida por el fabricante, que no necesariamente corresponde a 0° en todos los ejes articulare como lo evidenciamos en la imagen aunque se sue asumir valores ceracnos a 0.
- Representa una postura segura y conocida del robot, con el brazo extendido o retraído, dependiendo del modelo.
- Es ideal como punto de partida o retorno en procedimientos técnicos y de diagnóstico.

<h4 align="center">Home 1</h4>
<p align="center">
  <img src="https://github.com/user-attachments/assets/bdb6ba41-6711-4c51-8986-fc62d6c4a46e" alt="Home 1 - Imagen 1" height="250"/>
  <img src="https://github.com/user-attachments/assets/b1943b1a-a8e9-426d-9856-4e80f13911a1" alt="Home 1 - Imagen 2" height="250"/>
</p>


### Home 2

- Es una posición configurada por el usuario, adaptada a las necesidades específicas de la aplicación.
- Se utiliza comúnmente como posición inicial, final o de espera durante ciclos automáticos.
- Puede ser modificada libremente desde el controlador del robot.
- Permite mayor flexibilidad en entornos industriales y puede adaptarse al diseño de la celda de trabajo.
- Se accede mediante programación, por ejemplo:

<h4 align="center">Home 2</h4>
<p align="center">
  <img src="https://github.com/user-attachments/assets/65f7a10c-e22b-4dd8-83ad-3340dd79f1ff" alt="Home 2 - Imagen 1" height="250"/>
  <img src="https://github.com/user-attachments/assets/72280dc0-ad2c-4c02-b569-d3f1f37af88a" alt="Home 2 - Imagen 2" height="250"/>
</p>
Aunque Home 1 es la posición predeterminada del fabricante y resulta clave para tareas como calibración, diagnóstico y mantenimiento, en la práctica suele ser más útil trabajar con Home 2, especialmente en entornos industriales o simulaciones. Al poder configurarse según las necesidades del usuario, Home 2 se adapta mejor al espacio de trabajo, ayuda a evitar colisiones y permite optimizar los tiempos del ciclo operativo. Además, su flexibilidad la convierte en una excelente opción como punto de partida o de retorno en programas automáticos.




## 3. Procedimiento para realizar el movimiento manual del manipulador Motoman

### Movimiento manual por articulaciones

1. Activar el modo Teach en el controlador principal.
2. En el teach pendant, presionar el botón MODE y seleccionar la opción Joint.
3. Mantener presionado el botón de habilitación del servo (Enable) en el lateral del teach pendant.
4. Utilizar las teclas de dirección etiquetadas como + y - junto al nombre de cada eje (J1 a J6) para mover individualmente cada articulación.
5. Para detener el movimiento se suelta el botón o al deshabilitar el servo.



### Cambio a movimientos cartesianos

1. Presionar el botón MODE en el teach pendant.
3. Seleccionar la opción XYZ o World para cambiar al modo cartesiano.
4. Asegurarse de tener el servo habilitado.
5. La referencia ahora será la del sistema cartesiano 


### Movimiento cartesiano: traslación y rotación

#### Traslación 
- Utilizar las teclas de dirección etiquetadas como:
  - X+ / X- -> Traslación hacia adelante/atrás en el eje X
  - Y+ / Y- -> Traslación lateral derecha/izquierda en el eje Y
  - Z+ / Z- -> Traslación hacia arriba/abajo en el eje Z

#### Rotación 

- Utilizar las teclas de dirección correspondientes a:
  - Rx+ / Rx- -> Rotación sobre el eje X
  - Ry+ / Ry- -> Rotación sobre el eje Y
  - Rz+ / Rz- -> Rotación sobre el eje Z


## 4. Velocidades de movimiento manual y comunicación con RoboDK

### Niveles de velocidad del Motoman para movimientos manuales

#### Niveles de velocidad

- El sistema ofrece generalmente 4 niveles de velocidad preestablecidos para el modo manual:
  - Muy lenta (Very slow)
  - Lenta (Slow)
  - Media (Medium)
  - Rápida (Fast)

La velocidad en modo Teach está limitada por razones de seguridad.

#### Cambio entre niveles de velocidad

- Para cambiar el nivel de velocidad:
  1. Presionar el botón físico o función de pantalla Speed o STEP.
  2. Usar las teclas de flecha o selección en pantalla para incrementar (+) o decrementar (-) el nivel.
  3. Confirmar con ENTER si es necesario.
#### Identificación del nivel en la interfaz
El nivel de velocidad seleccionado se muestra en la pantalla del teach pendant, generalmente en una zona visible de la interfaz principal. Puede aparecer como un ícono, un número o una palabra clave (SLOW, MEDIUM, etc.).



---



---
## 5. Principales funcionalidades y comunicación de RoboDK con el manipulador Motoman

### Principales funcionalidades
- Simulación 3D precisa de manipuladores, herramientas y herramientas de trabajo.
- Compatibilidad con múltiples marcas y modelos de robots industriales
- Programación offline, reduciendo los tiempos de parada del robot real.
- Diseño y edición de trayectorias personalizadas, optimizadas para tareas específicas como soldadura, ensamblaje o paletizado.
- Generación automática de código en el lenguaje nativo del robot 


### Comunicación entre el manipulador Motoman MH6 y RoboDK

RoboDK puede comunicarse con el robot de dos formas principales, dependiendo de la infraestructura del controlador:

1. Exportación de programas 
RoboDK genera archivos de programa con extensión .JBI, escritos en lenguaje INFORM, que es nativo de Yaskawa/Motoman., estos archivos pueden transferirse al controlador mediante:

- Unidad USB

- Tarjeta Compact Flash

- Conexión FTP (si está habilitada)

El operador ejecuta el archivo desde el teach pendant, como cualquier otro programa.



2. Comunicación en línea 
Si el controlador del robot está habilitado para comunicación externa (con MotoCOM SDK o Ethernet/IP),esto se hace mediante la opcion Remote y seleccionando la opcion Conectar robot, RoboDK puede establecer una conexión en tiempo real con el manipulador.


Esto permite:

- Enviar comandos o trayectorias directamente desde el PC.

- Realizar pruebas o ajustes sin necesidad de cargar programas manualmente.

- Sincronizar acciones con otros dispositivos, sensores o sistemas industriales.


## 6. Análisis comparativo entre RoboDK y RobotStudio

### Diferencias clave

| Característica              | RoboDK                                      | RobotStudio                                   |
|----------------------------|----------------------------------------------|-----------------------------------------------|
| Fabricante                 | Independiente                               | ABB Robotics                                  |
| Compatibilidad             | Multimarca (ABB, KUKA, FANUC, Yaskawa, UR , etc.) | Exclusivo para robots ABB                     |
| Lenguaje                   | Python, exporta a múltiples formatos         | RAPID (lenguaje  de ABB)           |
| Curva de aprendizaje       | Accesible para principiantes                 | Técnica, enfocada a usuarios ABB              |
| CAD/CAM                    | Integración con Fusion 360, SolidWorks, etc. | Integración herramientas ABB y con Fusion 360, SolidWorks, etc.   |
| Licenciamiento             | Versión gratuita limitada y versión de pago   | Licensia paga         |

---

### Comparación de funciones

A continuación se presentan diferencias prácticas clave en cuanto a tareas comunes como la creación de trayectorias, definición de objetivos, y configuración del entorno de trabajo:

| Funcionalidad                          | RoboDK                                                  | RobotStudio (ABB)                                       |
|---------------------------------------|----------------------------------------------------------|----------------------------------------------------------|
| Creación de trayectorias              | Interfaz gráfica sencilla con listas de movimiento       | Paths estructurados y WorkObjects                       |
| Definición de targets     | GUI interactiva o scripts en Python                      | Definición precisa en el entorno 3D ABB                  |
| Configuración de herramientas | GUI o scripts Python para definir TCP                    | Definición y validación técnica en el entorno ABB        |
| Configuración de frames     | Asignación sencilla mediante referencia cartesiana       | Alineación con estaciones virtuales reales ABB           |
| Creación de movimientos               | MoveJ, MoveL, MoveC, programables en Python        | MoveAbsJ, MoveL, MoveC programables en RAPID       |
| Interfaz gráfica                      | Intuitiva, compatible con múltiples marcas               | Más compleja y técnica, adaptada a ABB                   |
| Simulación realista                   | Precisa, pero con menor fidelidad física que ABB         | Integración con Virtual Controller de ABB               |
| Exportación de código                 | Multilenguaje: Yaskawa .JBI, KUKA .src, ABB .mod   | Solo RAPID                                               |

---

### Aplicaciones

#### RoboDK

- Simulación de trayectorias con múltiples marcas de robots
- Generación y exportación de código en diferentes lenguajes
- Formación en robótica industrial sin necesidad de hardware
- Integración con entornos CAD/CAM (SolidWorks, Inventor, Fusion 360)
- Programación offline sin detener la producción
- Validación de colisiones y ciclos de trabajo

#### RobotStudio

- Simulación precisa con controladores virtuales ABB
- Desarrollo y depuración de programas en RAPID
- Validación y sincronización con hardware real ABB
- Configuración detallada de celdas y periferia ABB
- Entrenamiento avanzado en la plataforma ABB
- Comprobación de errores y ajustes de parámetros del sistema

---

## Video

