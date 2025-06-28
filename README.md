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


A pesar de que Home 1 es la posición de referencia establecida por el fabricante y resulta esencial para tareas de calibración, diagnóstico y mantenimiento,para operaciones industriales o simulaciones, Home 2 suele ser más conveniente.

Esto debido a que Home 2 es configurable por el usuario, permitiendo adaptarla al entorno de trabajo, evitar colisiones y optimizar el tiempo de ciclo. Además, su flexibilidad permite que se use como punto de partida o retorno seguro en los programas automáticos.


## 3. Procedimiento para realizar el movimiento manual del manipulador Motoman

A continuación, se describe el procedimiento y las teclas necesarias para controlar manualmente el manipulador **Motoman MH6** desde el **pendant de programación (teach pendant)**, tanto en modo articular como en modo cartesiano.

### 3.1 Movimiento manual por articulaciones (modo Joint)

1. **Activar el modo Teach** en el controlador principal.
2. En el teach pendant, presionar el botón `MODE` y seleccionar la opción **"Joint"**.
3. Mantener presionado el botón de **habilitación del servo (Enable)** en el lateral del teach pendant.
4. Utilizar las teclas de dirección etiquetadas como **`+` y `-`** junto al nombre de cada eje (`J1` a `J6`) para mover individualmente cada articulación.
5. El movimiento se detendrá al soltar el botón o al deshabilitar el servo.



### 3.2 Cambio a movimientos cartesianos

1. Presionar el botón `MODE` en el teach pendant.
2. Seleccionar la opción **"XYZ"** o **"World"** para cambiar al **modo cartesiano**.
3. Asegurarse de tener el servo habilitado.
4. La referencia ahora será la del sistema cartesiano (coordenadas X, Y, Z con rotaciones Rx, Ry, Rz).



### 3.3 Movimiento cartesiano: traslación y rotación

#### Traslación (movimiento lineal)

- Utilizar las teclas de dirección etiquetadas como:
  - `X+` / `X-` → Traslación hacia adelante/atrás en el eje X
  - `Y+` / `Y-` → Traslación lateral derecha/izquierda en el eje Y
  - `Z+` / `Z-` → Traslación hacia arriba/abajo en el eje Z

#### Rotación (movimiento angular)

- Utilizar las teclas de dirección correspondientes a:
  - `Rx+` / `Rx-` → Rotación sobre el eje X
  - `Ry+` / `Ry-` → Rotación sobre el eje Y
  - `Rz+` / `Rz-` → Rotación sobre el eje Z


## 4. Velocidades de movimiento manual y comunicación con RoboDK

### 4.1 Niveles de velocidad del Motoman para movimientos manuales

El robot **Motoman MH6** permite configurar distintos niveles de velocidad para los movimientos manuales (en modo Teach), lo que permite controlar con precisión la velocidad de desplazamiento durante la programación o el ajuste de posiciones.

#### Niveles de velocidad

- El sistema ofrece generalmente **4 niveles de velocidad preestablecidos** para el modo manual:
  - **Velocidad 1**: Muy lenta (precisión máxima)
  - **Velocidad 2**: Lenta
  - **Velocidad 3**: Media
  - **Velocidad 4**: Rápida (máxima permitida en modo manual)

>  La velocidad en modo Teach está limitada por razones de seguridad.

#### Cambio entre niveles de velocidad

- Para cambiar el nivel de velocidad:
  1. Presionar el botón físico o función de pantalla `Speed` o `STEP`.
  2. Usar las teclas de flecha o selección en pantalla para incrementar (`+`) o decrementar (`-`) el nivel.
  3. Confirmar con `ENTER` si es necesario.



### 4.2 Aplicaciones principales de RoboDK

[RoboDK](https://robodk.com) es una plataforma de simulación y programación offline de robots industriales. Se utiliza ampliamente en la industria y la academia para planificar y validar trayectorias sin necesidad de programar directamente en el robot.

#### Principales aplicaciones de RoboDK

- **Simulación de trayectorias** y procesos industriales (soldadura, corte, ensamblaje, pintura, etc.).
- **Programación offline** (OLP) sin detener la producción.
- **Generación automática de código** para múltiples marcas de robots (Yaskawa, ABB, KUKA, FANUC, etc.).
- **Integración con CAD/CAM**, como SolidWorks, Inventor o Fusion 360.
- **Estudios de alcance, colisiones y tiempo de ciclo**.
- **Entrenamiento y docencia en robótica industrial**.

---

### 4.3 Comunicación de RoboDK con el robot Motoman

RoboDK se comunica con el robot Motoman mediante **exportación de código** o **conexión directa por protocolo**, dependiendo del modelo y licencia instalada.

#### Métodos de conexión comunes

1. **Exportación de programas en lenguaje INFORM (JBI)**:
   - RoboDK genera archivos `.JBI` que se cargan en el controlador del Motoman mediante USB, FTP o tarjeta compact flash.

2. **Conexión en línea mediante controlador Yaskawa (MotoCOM o Ethernet/IP)**:
   - Requiere un controlador con funciones habilitadas para comunicación externa.
   - Permite que RoboDK envíe comandos en tiempo real al robot.

---

### 4.4 ¿Qué hace RoboDK para mover el manipulador?

Cuando se utiliza RoboDK para mover un robot Motoman, el software realiza las siguientes acciones:

1. **Genera el plan de trayectoria** en el entorno de simulación.
2. **Convierte la trayectoria en instrucciones de movimiento** específicas para el lenguaje del controlador Motoman (por ejemplo, `MOVJ`, `MOVL`, `MOVC` en formato `.JBI`).
3. **Transfiere el programa** al robot mediante un medio de comunicación compatible.
4. El robot **ejecuta el programa cargado**, realizando los movimientos planificados en el entorno real.
## 5. Comunicación de RoboDK con el manipulador Motoman

La comunicación entre **RoboDK** y el robot **Motoman MH6** puede establecerse mediante distintos métodos, dependiendo del tipo de controlador disponible y las capacidades habilitadas. A continuación, se describen las principales formas de conexión.

### 5.1 Comunicación mediante exportación de programas

RoboDK permite generar trayectorias en su entorno de simulación y exportarlas como archivos de programa en el lenguaje **INFORM** (propio de Yaskawa), con extensión `.JBI`. Estos archivos pueden ser transferidos al controlador del robot mediante:

- Unidad de memoria USB
- Tarjeta Compact Flash
- Conexión FTP (si está habilitada en el controlador)

Una vez transferido, el programa puede ser ejecutado desde el teach pendant como cualquier otro programa nativo del robot.

### 5.2 Comunicación directa en línea (Online Programming)

Si el controlador del robot cuenta con soporte para comunicación externa, como el SDK **MotoCOM** o protocolos industriales como **Ethernet/IP**, es posible establecer una conexión en línea entre RoboDK y el manipulador. Este tipo de conexión permite:

- Envío de trayectorias en tiempo real desde RoboDK
- Control remoto para pruebas, ajustes y validaciones
- Sincronización con periféricos o sensores externos

Este método requiere una configuración previa en el controlador y puede requerir licencias adicionales.

### 5.3 Proceso general de control desde RoboDK

El flujo de trabajo típico de RoboDK para mover un manipulador industrial incluye los siguientes pasos:

1. **Simulación**: El usuario diseña la trayectoria en el entorno virtual de RoboDK.
2. **Generación de código**: RoboDK convierte esa trayectoria en instrucciones en el lenguaje del robot (INFORM).
3. **Transferencia**: El programa se transfiere al controlador, ya sea por exportación de archivo o comunicación en línea.
4. **Ejecución**: El robot ejecuta el programa en el entorno físico, replicando los movimientos simulados.

RoboDK no actúa como un controlador de bajo nivel. Su función principal es la de una herramienta de simulación, planificación y generación de código para facilitar la programación offline de robots industriales.
## 6. Análisis comparativo entre RoboDK y RobotStudio

### 6.1 Diferencias clave

Las herramientas **RoboDK** y **RobotStudio** son ampliamente utilizadas para la simulación y programación offline de robots industriales, aunque presentan diferencias importantes en su enfoque, compatibilidad y lenguaje.

| Característica              | RoboDK                                      | RobotStudio                                   |
|----------------------------|----------------------------------------------|-----------------------------------------------|
| Fabricante                 | Independiente                               | ABB Robotics                                  |
| Compatibilidad             | Multimarca (ABB, KUKA, FANUC, Yaskawa, UR…) | Exclusivo para robots ABB                     |
| Lenguaje                   | Python, exporta a múltiples formatos         | RAPID (lenguaje  de ABB)           |
| Curva de aprendizaje       | Accesible para principiantes                 | Técnica, enfocada a usuarios ABB              |
| CAD/CAM                    | Integración con Fusion 360, SolidWorks, etc. | Integración herramientas ABB y con Fusion 360, SolidWorks, etc.   |
| Licenciamiento             | Versión gratuita limitada; versión de pago   | Licensia paga         |

---

### 6.2 Comparación práctica de funciones

A continuación se presentan diferencias prácticas clave en cuanto a tareas comunes como la creación de trayectorias, definición de objetivos, y configuración del entorno de trabajo:

| Funcionalidad                          | RoboDK                                                  | RobotStudio (ABB)                                       |
|---------------------------------------|----------------------------------------------------------|----------------------------------------------------------|
| Creación de trayectorias              | Interfaz gráfica sencilla con listas de movimiento       | Paths estructurados y WorkObjects                       |
| Definición de targets (objetivos)     | GUI interactiva o scripts en Python                      | Definición precisa en el entorno 3D ABB                  |
| Configuración de herramientas (Tool)  | GUI o scripts Python para definir TCP                    | Definición y validación técnica en el entorno ABB        |
| Configuración de frames (base)        | Asignación sencilla mediante referencia cartesiana       | Alineación con estaciones virtuales reales ABB           |
| Creación de movimientos               | `MoveJ`, `MoveL`, `MoveC`, programables en Python        | `MoveAbsJ`, `MoveL`, `MoveC` programables en RAPID       |
| Interfaz gráfica                      | Intuitiva, compatible con múltiples marcas               | Más compleja y técnica, adaptada a ABB                   |
| Simulación realista                   | Precisa, pero con menor fidelidad física que ABB         | Integración con Virtual Controller de ABB               |
| Exportación de código                 | Multilenguaje: Yaskawa `.JBI`, KUKA `.src`, ABB `.mod`   | Solo RAPID                                               |

---

### 6.3 Usos específicos

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

### 6.4 Reflexión personal

Estas herramientas representan dos aproximaciones distintas a la programación y simulación en robótica industrial:

- **RoboDK** simboliza la **versatilidad** y la **accesibilidad**. Su enfoque multimarca y compatibilidad con Python lo hacen ideal para usuarios que buscan explorar distintos entornos robóticos, realizar simulaciones educativas o validar proyectos de automatización de forma rápida.

- **RobotStudio** representa la **precisión técnica** y la **especialización**. Está orientado a usuarios que ya trabajan en entornos ABB o buscan replicar exactamente los procesos industriales de esa plataforma con fidelidad total al hardware.

Ambas herramientas son fundamentales y complementarias. La elección entre una y otra depende del fabricante del robot, el tipo de aplicación, el entorno académico o industrial, y el nivel de profundidad requerido en la programación.


