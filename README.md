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
| Acceso                      | Sistema predeterminado                | Mediante programación (`MOVJ HOME2`)   |

  

