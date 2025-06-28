# Laboratorio_No._03
**Juliana Gongora Rasmussen**


_Ingeniería Mecatrónica_

Correo: jugongorar@unal.edu.co

---


**Gerhaldine Alejandra Suárez Bernal**
  
  _Ingeniería Mecatrónica_

Correo: gesuarezb@unal.edu.co
## 1. Cuadro Comparativo entre Motoman MH6 y IRB140


## 2. Descripción de las diferencias entre Home 1 y Home 2 del robot Motoman MH6

El robot **Motoman MH6** dispone de dos posiciones de referencia comúnmente utilizadas en programación y operación: `Home 1` y `Home 2`. Estas posiciones cumplen funciones distintas dentro del entorno de trabajo del robot. A continuación se describen sus principales diferencias:

### 2.1 Home 1

- Es la **posición de origen predeterminada de fábrica**.
- Se utiliza como referencia para **calibración, mantenimiento y verificación de ejes**.
- **No puede ser modificada** por el usuario.
- En esta posición, **todos los ejes del robot (J1 a J6) están en 0 grados**, es decir, las configuraciones articulares están en cero.
- Representa una postura estándar y segura del robot, con el brazo extendido hacia el frente o completamente retraído.
- Es ideal como punto de partida o retorno en procedimientos técnicos y de diagnóstico.

### 2.2 Home 2

- Es una **posición configurada por el usuario**, adaptada a las necesidades específicas de la aplicación.
- Se utiliza comúnmente como **posición inicial, final o de espera** durante ciclos automáticos.
- Puede ser modificada libremente desde el controlador del robot.
- Permite mayor flexibilidad en entornos industriales y puede adaptarse al diseño de la celda de trabajo.
- Se accede mediante programación

  
### 2.3 Resumen comparativo

| Característica              | Home 1                               | Home 2                                |
|-----------------------------|---------------------------------------|----------------------------------------|
| Definición                  | Posición de fábrica                   | Posición definida por el usuario       |
| Configuración               | Fija, no editable                     | Editable y personalizable              |
| Valores articulares         | Todos las articulaciones en 0         | Definidos por el usuario               |
| Propósito principal         | Calibración y diagnóstico             | Operación y producción                 |
| Acceso                      | Sistema predeterminado                | Mediante programación                  |

  
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
.


