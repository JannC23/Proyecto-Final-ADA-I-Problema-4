# Motor de Consultas sobre Datos Comprimidos por Rangos

## 1. Descripción General

Implementación de un motor de consultas para procesar datos comprimidos por rangos. El proyecto permite trabajar con secuencias representadas mediante rangos sin necesidad de expandir completamente la secuencia en memoria.

Por ejemplo, una secuencia como `1 1 1 1 1 3 3 3 2 2 2 2` se representa como:
- 1 aparece de la posición 1 a la 5
- 3 aparece de la posición 6 a la 8
- 2 aparece de la posición 9 a la 12

Este enfoque permite procesar datos dispersos o comprimidos de manera eficiente, tanto en tiempo de ejecución como en uso de memoria.

## 2. Problema Resuelto

**Problema 4: Motor de consultas sobre datos comprimidos por rangos**

El sistema debe:
- Leer datos comprimidos por rangos desde un archivo
- Procesar consultas y operaciones sobre estos rangos
- Generar resultados sin expandir la secuencia completa
- Soportar rangos muy grandes (hasta 10^9)
- Procesar hasta 200,000 operaciones de manera eficiente

## 3. Integrantes del Equipo

Este proyecto fue desarrollado como parte del curso de Análisis y Diseño de Algoritmos I.

## 4. Estructuras de Datos Implementadas

### 4.1 Árbol Rojo-Negro
**Archivo**: `structures/arbol_rojinegro.py`

Estructura balanceada que mantiene los rangos ordenados por su posición inicial. Proporciona operaciones eficientes de inserción, eliminación y búsqueda.

**Justificación**: 
- Mantiene rangos ordenados automáticamente
- Garantiza búsqueda en O(log N)
- Balanceo automático evita degeneración del árbol
- Permite búsquedas recursivas eficientes

**Operaciones principales**:
- `insertar(nodo)`: O(log N) - Inserta un rango ordenadamente
- `buscar(inicio)`: O(log N) - Busca un rango por su posición inicial
- `eliminar(inicio)`: O(log N) - Elimina un rango

### 4.2 Nodo de Rango
**Archivo**: `structures/nodo_rango.py`

Estructura básica que representa un rango comprimido con sus atributos.

**Atributos**:
- `valor`: Valor que contiene el rango
- `inicio`: Posición inicial del rango
- `fin`: Posición final del rango
- `color`: Color para el árbol Rojo-Negro (rojo o negro)
- `padre`: Referencia al nodo padre
- `left`: Referencia al hijo izquierdo
- `right`: Referencia al hijo derecho

### 4.3 Motor de Consultas
**Archivo**: `core/motor_consultas.py`

Orquesta todas las operaciones sobre los rangos comprimidos usando el árbol Rojo-Negro como estructura base.

## 5. Formato de Entrada y Salida

### 5.1 Entrada (entrada.txt)
```
N
valor1 inicio1 fin1
valor2 inicio2 fin2
...
Q
OPERACION parametros
OPERACION parametros
...
```

Donde:
- N: cantidad de rangos iniciales
- Q: cantidad de operaciones

### 5.2 Salida (salida.txt)
```
OPERACION parametros = resultado
OPERACION parametros = resultado
...
```

## 6. Operaciones Soportadas

### VALUE posicion
Retorna el valor almacenado en una posición específica.
- **Entrada**: VALUE 10
- **Salida**: VALUE 10 = 2
- **Complejidad**: O(log N)

### SUM inicio fin
Calcula la suma de todos los valores en un rango de posiciones.
- **Entrada**: SUM 1 10
- **Salida**: SUM 1 10 = 21
- **Complejidad**: O(N)

### UPDATE inicio fin valor
Actualiza todas las posiciones en un rango con un nuevo valor. Realiza fusión automática de rangos consecutivos con el mismo valor.
- **Entrada**: UPDATE 6 8 5
- **Salida**: UPDATE 6 8 5 = OK
- **Complejidad**: O(N)

### FREQUENCY valor
Cuenta cuántas posiciones contienen un valor específico.
- **Entrada**: FREQUENCY 2
- **Salida**: FREQUENCY 2 = 6
- **Complejidad**: O(N)

### MAX_RANGE inicio fin
Encuentra el valor máximo en un rango de posiciones.
- **Entrada**: MAX_RANGE 1 20
- **Salida**: MAX_RANGE 1 20 = 8
- **Complejidad**: O(N)

### MIN_RANGE inicio fin
Encuentra el valor mínimo en un rango de posiciones.
- **Entrada**: MIN_RANGE 1 20
- **Salida**: MIN_RANGE 1 20 = 1
- **Complejidad**: O(N)

### DECOMPRESS inicio fin
Expande un rango de posiciones mostrando todos los valores de forma descomprimida.
- **Entrada**: DECOMPRESS 1 12
- **Salida**: DECOMPRESS 1 12 = 1 1 1 1 1 5 5 5 2 2 2 2
- **Complejidad**: O(N + M) donde M es la cantidad de elementos en el rango

### COUNT_RANGES
Retorna la cantidad total de rangos en el árbol.
- **Entrada**: COUNT_RANGES
- **Salida**: COUNT_RANGES = 5
- **Complejidad**: O(N)

### MERGE
Fusiona rangos consecutivos que contengan el mismo valor, comprimiendo aún más la representación.
- **Entrada**: MERGE
- **Salida**: MERGE = OK
- **Complejidad**: O(N)

## 7. Estrategia Divide y Vencer

### Operación: VALUE (Búsqueda Recursiva en Árbol)

**Problema**: Encontrar eficientemente el valor almacenado en una posición específica dentro de un árbol de rangos.

**Caso Base**: 
- Si el nodo es None, retornar None (posición no existe)
- Si la posición está dentro del rango del nodo actual, retornar el valor del nodo

**División del Problema**:
1. Comparar la posición buscada con el rango del nodo actual
2. Si posición < nodo.inicio: buscar en el subárbol izquierdo
3. Si posición > nodo.fin: buscar en el subárbol derecho
4. Si nodo.inicio ≤ posición ≤ nodo.fin: se encontró, retornar valor

**Combinación de Resultados**:
La recursión retorna automáticamente el resultado encontrado en cualquier subárbol. No requiere combinación explícita porque cada rama retorna un resultado único.

**Complejidad Temporal**:
- **Solución Divide y Vencer**: O(log N) en promedio, O(N) en peor caso
- **Solución Ingenua** (búsqueda lineal): O(N) siempre
- **Mejora**: En árboles balanceados, se reduce búsqueda lineal a logarítmica

**Por qué es mejor**:
1. Elimina 50% de los rangos en cada comparación
2. Evita recorrer todos los rangos secuencialmente
3. En datos grandes (N=1,000,000), pasa de 1,000,000 operaciones a ~20

**Implementación**:
```
function value(posicion):
    return value_aux(raiz, posicion)

function value_aux(nodo, posicion):
    if nodo es None:
        return None
    
    if nodo.inicio ≤ posicion ≤ nodo.fin:
        return nodo.valor
    
    if posicion < nodo.inicio:
        return value_aux(nodo.izquierda, posicion)
    else:
        return value_aux(nodo.derecha, posicion)
```

## 8. Análisis de Complejidad

| Operación | Complejidad Esperada | Justificación |
|-----------|-------------------|---------------|
| Insertar rango | O(log N) | Inserción en árbol Rojo-Negro |
| VALUE (Divide y Vencer) | O(log N) promedio | Búsqueda binaria en árbol balanceado |
| SUM | O(N) | Recorre todos los rangos una vez |
| UPDATE | O(N) | Procesa cada rango afectado + inserción |
| FREQUENCY | O(N) | Itera sobre todos los rangos |
| MAX_RANGE | O(N) | Busca máximo en todos los rangos del rango |
| MIN_RANGE | O(N) | Busca mínimo en todos los rangos del rango |
| DECOMPRESS | O(N + M) | Recorre rangos (N) y expande elementos (M) |
| COUNT_RANGES | O(N) | Recorrido inorden del árbol |
| MERGE | O(N) | Recorre y fusiona rangos consecutivos |

Donde:
- **N**: cantidad total de rangos en el árbol
- **M**: cantidad de elementos en el rango de descompresión

## 9. Comparación con Solución Ingenua

### Almacenamiento Ingenuo
**Enfoque**: Almacenar la secuencia completa sin compresión

```
Secuencia: 1 1 1 1 1 3 3 3 2 2 2 2
Arreglo: [1, 1, 1, 1, 1, 3, 3, 3, 2, 2, 2, 2]
Posiciones: 1 a 12
```

**Problemas**:
- Si el rango es 10^9: requiere 10^9 elementos en memoria
- Para N=1,000,000 con posiciones hasta 10^9: impracticable
- Cada operación requiere iterar sobre todos los elementos

### Nuestra Solución: Compresión por Rangos
```
Rangos:
- Rango 1: valor=1, inicio=1, fin=5
- Rango 2: valor=3, inicio=6, fin=8
- Rango 3: valor=2, inicio=9, fin=12
```

**Ventajas**:
- Almacena solo 3 nodos en lugar de 12 elementos
- Soporta posiciones hasta 10^9 sin expandir
- VALUE: O(log 3) = O(1) vs O(12) = O(N) ingenua
- FREQUENCY: O(3) = O(N) vs O(12) = O(N), pero N es mucho menor
- Memoria: O(N rangos) vs O(10^9 posiciones)

### Ejemplo de Mejora en Datos Grandes

**Escenario**: Posición 999,999,999 en una secuencia de 10^9 elementos

| Enfoque | Tiempo | Memoria |
|---------|--------|---------|
| Ingenuo (arreglo) | O(10^9) - No viable | O(10^9) - No viable |
| Ingenuo (lista) | O(10^9) recorrido | O(10^9) |
| Nuestra Solución | O(log N) = O(log 1000000) ~20 ops | O(N rangos) |

## 10. Casos de Prueba y Casos Límite Considerados

### Entrada de Prueba Proporcionada
```
5
1 1 5
3 6 8
2 9 14
8 15 16
4 17 20
7
VALUE 10
SUM 1 10
UPDATE 6 8 5
FREQUENCY 2
MAX_RANGE 1 20
DECOMPRESS 1 12
COUNT_RANGES
```

### Casos Límite Considerados

#### 1. Rangos Consecutivos con Mismo Valor
**Prueba**: MERGE fusiona automáticamente rangos consecutivos
```
Antes: 1-5 (valor 1), 6-10 (valor 1)
MERGE
Después: 1-10 (valor 1)
```

#### 2. Actualizaciones que Dividen Rangos
**Prueba**: UPDATE sobre rango que está contenido parcialmente
```
Rango original: 1-20 (valor 5)
UPDATE 5 15 3
Resultado: 1-4 (valor 5), 5-15 (valor 3), 16-20 (valor 5)
```

#### 3. Posiciones Extremas
**Prueba**: Rangos en posiciones muy grandes (cercanas a 10^9)
```
999999999 999999999 999999999999999999
```

#### 4. Operaciones sobre Posiciones Inexistentes
**Prueba**: Consultar VALUE en posición sin valor
```
VALUE en posición 2500 (entre 14 y 15): Retorna None
```

#### 5. Rango Único
**Prueba**: Sistema con un solo rango
```
1
1 1 1000000000
COUNT_RANGES: Retorna 1
```

#### 6. Descompresión de Rango Pequeño
**Prueba**: DECOMPRESS de solo algunos elementos
```
DECOMPRESS 1 3: Retorna "1 1 1"
```

#### 7. Rango Vacío en Consultas
**Prueba**: SUM sobre rango que no intersecta ningún rango
```
SUM 2500 2999: Retorna 0 (ninguna intersección)
```

## 11. Instrucciones de Compilación y Ejecución

### Requisitos
- Python 3.6 o superior
- No requiere librerías externas

### Ejecución
```bash
python main.py
```

El programa:
1. Lee el archivo `entrada.txt`
2. Carga los rangos iniciales
3. Procesa todas las operaciones en orden
4. Genera el archivo `salida.txt` con los resultados

### Estructura del Proyecto
```
.
├── README.md                    # Este archivo
├── LICENSE                      # Licencia MIT
├── main.py                      # Punto de entrada
├── entrada.txt                  # Datos de entrada
├── salida.txt                   # Resultados generados
├── core/
│   └── motor_consultas.py      # Lógica principal
└── structures/
    ├── arbol_rojinegro.py      # Árbol Rojo-Negro
    └── nodo_rango.py           # Nodo de rango
```

## 12. Conclusiones

### Logros Alcanzados
1. Implementación exitosa de un motor de consultas sobre datos comprimidos
2. Uso efectivo de estructura Rojo-Negro para mantener rangos ordenados
3. Aplicación de estrategia Divide y Vencer en búsqueda de posiciones
4. Manejo eficiente de rangos grandes (hasta 10^9) sin expansión completa
5. Todas las operaciones requeridas implementadas y funcionales

### Mejoras Implementadas
- Búsqueda recursiva O(log N) en lugar de lineal
- Fusión automática de rangos para mayor compresión
- Manejo correcto de actualizaciones que dividen/fusionan rangos
- Soporte para coordenadas extremadamente grandes

### Validación
- Programa compila y ejecuta sin errores
- Formato de entrada/salida validado
- Casos de prueba pequeños, medianos y grandes funcionan correctamente
- Casos límite considerados y manejados adecuadamente
- Complejidad temporal documentada y justificada

## 13. Licencia

Este proyecto está bajo la licencia MIT.
