# Sistema de Gestión de Restaurante Básico (POO)

**Estudiante:** Karen Antonela Chango Luna  
**Materia:** Programación Orientada a Objetos  

## Descripción del Sistema
Este proyecto implementa un sistema básico y modular para la gestión de un restaurante utilizando Python. El software permite representar de manera abstracta elementos clave como productos (platillos/bebidas) y clientes, administrándolos de manera centralizada a través de un servicio logístico, sin necesidad de interfaces complejas ni menús interactivos.

## Estructura del Proyecto
El proyecto se organiza bajo una arquitectura modular para separar las responsabilidades de datos y lógica:

- `modelos/`: Contiene las clases fundamentales del dominio (`Producto` y `Cliente`) encargadas de almacenar estados individuales.
- `servicios/`: Contiene la clase `Restaurante`, encargada de agrupar, procesar y listar los datos.
- `main.py`: Archivo principal encargado de orquestar la creación de instancias, inserción en colecciones y salida en consola.

## Tipos de Datos Utilizados
Se emplearon estrictamente los tipos solicitados junto con anotaciones de tipo explícitas:
- **`str`**: Para cadenas de texto descriptivas (`nombre`, `nombre_completo`).
- **`float`**: Para valores monetarios de precisión (`precio`).
- **`int`**: Para identificadores numéricos discretos (`numero_mesa`).
- **`bool`**: Para flags y estados lógicos de control (`disponible`, `es_frecuente`).
- **`list` (Tipo Compuesto)**: Colecciones dinámicas optimizadas para almacenar múltiples objetos e iterar sobre ellos (`lista_productos`, `lista_clientes`).

---

## Reflexión Académica

### Importancia de los Identificadores Descriptivos y Convenciones de Nombres
El uso de identificadores descriptivos (como `nombre_completo` en lugar de una variable genérica `n` o `x`) reduce drásticamente la carga cognitiva al leer el código. Al acatar las convenciones de la comunidad de Python (`PascalCase` para clases y `snake_case` para variables y métodos), el diseño se vuelve estándar, profesional y legible para cualquier desarrollador externo, transformando el código en "autodocumentado".

### Pertinencia en la Selección de Tipos de Datos
Elegir el tipo de dato correcto previene fallas de lógica de negocio en etapas tempranas. Por ejemplo, definir el precio como un `float` permite operaciones matemáticas financieras precisas, mientras que un estado booleano (`bool`) simplifica condicionales del sistema de forma eficiente sin recurrir a textos ambiguos como `"sí"` o `"no"`.

### Utilidad de las Listas en Proyectos Modulares
En la programación modular, las listas actúan como contenedores dinámicos y flexibles de objetos complejos. Al encapsular colecciones dentro de una clase de servicio (`Restaurante`), logramos separar el molde individual de la lógica de negocio grupal. Esto asegura que el sistema sea escalable; añadir un nuevo producto no rompe la estructura del programa, permitiendo procesar eficientemente cientos de registros mediante bucles simples.