# Estadística para Datos Univariados

Datos univariados (o data univariada) son datos que se describen con una sola variable. Por ejemplo, las alturas de los compñaeros de clase son datos univariados. El propósito principal del análisis de datos univariados es la descripción de los datos. 

El análisis de datos univariados no considera relaciones entre distintas variables, como podría ser la relación entre la altura y el peso de los compañeros de clase.

import math
import pandas as pd
import plotly.express as px

## Muestreo (Sampling)

**Definiciones**

- **Población:** el grupo entero del que queremos estudiar una característica. Por ejemplo, todos las mujeres de Chile, todos los hogares de la comuna de Providencia.
- **Muestra (Sample):** el subgrupo de la población que se utiliza para inferir propiedades de la población. Por ejemplo, para estudiar alguna propiedad de las mujeres de Chile, utilizamos una muestra de mujeres que consiste en 10 mujeres de cada comuna de Chile.

### Técnicas de Muestreo

- **Muestreo por Conveniencia (convenience sampling):** se seleccionan aquellos miembros de la población que son de más fácil acceso. Por ejemplo, para el ejemplo de las mujeres de Chile, utilizo como muestra a las mujeres de mi colegio.
- **Muestro Aleatorio Simple (simple random sampling):** cada miembro de la población tiene la misma probabilidad de ser elegido. Por ejemplo, con un generador de números aleatorios genramos RUTs y elegimos los RUTs generados que correspondan a mujeres.
- **Muestreo Sistemático (systematic sampling):** Se listan (ordenan) los miembros de la población y se eligen a partir de un número inicial y un intervalo fijo.
- **Muestreo Estratificado (stratified sampling):** Se divide la población en subgrupos más pequeños (estratos). Los estratos se construyen basándose en características comunes de sus miembros. Luego, se elige una muestra aleatoria de cada estrato.
- **Muestreo por Cuota (quota sampling):** Muy similar al muestro estratificado, pero el tamaño de la muestra de cada estrato depende de la proporción del estrato en la población total.

### Tipos de Datos

- **Datos Discretos:** datos cuyos valore posibles pueden ser contados (incluso si en teoría el número de datos posibles es infinito). Por ejemplo, la talla de zapatos es un dato discreto ya que sólo existe un número finito de tallas posibles.
- **Datos continuos:** datos cuyos valores posibles no pueden ser contados. Generalmente se representan con un número real (con decimales). Por ejemplo, la altura de cada individuo. La temepratura a una cierta hora del día en un lugar preespecificado de la ciudad.

## Presentación de los Datos

Para datos discretos, la herramienta más usual de presentación son la tabla y gráfico de frecuencias.

**Ejemplo:**

Consideremos las notas de 32 alumnos en un test en el cual se puede obtener una nota entera del 0 al 10. Supongamos que los resultados son los siguientes:

resultados = [0, 1, 1, 2, 2, 2, 3, 3, 4, 4, 4, 5, 5, 5, 5, 5, 6, 6, 6, 6, 7, 7, 7, 7, 7, 7, 8, 8, 8, 8, 9, 10]

Contamos cuantas ocurrencias de cada nota hay en la muestra:

frecuencia = [(i, resultados.count(i)) for i in range(11)]
df_frecuencia = pd.DataFrame(frecuencia, columns=['nota', 'frecuencia'])
df_frecuencia

Mostramos los datos de la tabla anterior en un gráfico de barras.

fig = px.bar(df_frecuencia, x='nota', y=['frecuencia',],
              title=f'Frecuencia de Notas')
fig.show()

Para datos contínuos, en cambio, la herramienta más usual es un histograma. Un histograma también representa la frecuencia de ocurrencia de datos, pero, al tratarse de datos contínuos, se representa la frecuencia de ocurrencia de datos en un cierto intervalo.

Veamos en ejemplo considerando una serie histórica de precios del USD en términos del CLP (USDCLP) de 10 años.

df_usdclp = pd.read_excel('data/20210312_10Y_usdclp.xlsx')
fig = px.line(df_usdclp, x='fecha', y=['valor',],
              title=f'Serie Histórica USDCLP')
fig.show()

Podemos ver como los valores están entre 450 y 870 aproximadamente. Vamos a dividir ese intervalo en subintervalos de 10 CLP y luego graficaremos (con un gráfico de barras) la frecuencia de precios observados en cada uno de esos subintervalos.

fig = px.histogram(
    df_usdclp,
    x="valor",
    title='Histograma USDCLP - Frecuencia en Intervalos del 10 CLP')
fig.show()

### Forma del Histograma

Es importante describir la forma del histograma, la principal característica de un histograma es la presencia de sesgo (skew):

df_sim = pd.DataFrame([(0,1), (1,2), (2,3), (3,4), (4,5), (5,6), (6,8), (7,9), (8,11), (9,10), (10,8)],
                     columns=['intervalo', 'frecuencia'])
fig = px.bar(df_sim, x='intervalo', y=['frecuencia',],
              title=f'Sesgo Negativo')
fig.show()

df_sim = pd.DataFrame([(0,8), (1,10), (2,11), (3,9), (4,8), (5,6), (6,5), (7,4), (8,3), (9,2), (10,1)],
                     columns=['intervalo', 'frecuencia'])
fig = px.bar(df_sim, x='intervalo', y=['frecuencia',],
              title=f'Sesgo Positivo')
fig.show()

df_sim = pd.DataFrame([(0,1), (1,2), (2,3), (3,4), (4,5), (5,6), (6,5), (7,4), (8,3), (9,2), (10,1)],
                     columns=['intervalo', 'frecuencia'])
fig = px.bar(df_sim, x='intervalo', y=['frecuencia',],
              title=f'Sin Sesgo')
fig.show()

## Medidas de Tendencia Central

Hasta ahora hemos visto como recopilar y presentar datos. El próximo paso es elegir un único valor que pueda representar la data de forma general. Una medida de tendencia central que nos indica donde está "la mitad" de los datos recopilados. Las medidas más comunes de tendencia central son:

- moda
- media
- mediana

### Moda

**Definición:** la moda es el valor que ocurre con más frecuencia en los datos.

**Tips:**

- Puede haber más de una *moda* si dos o más valores son los que ocurren con mayor frecuencia. 
- Si no hay ningún valor de la muestra que ocurra con mayor frecuencia (todos ocurren sólo una vez) entonces la muestra no tiene *moda*.

**Ejemplo:**

data = [4, 7, 3, 3, 1, 2, 7, 5, 7, 11]

contador =  {elem: data.count(elem) for elem in set(data)}
highest_counter = [(k, v) for k, v in contador.items() if v == max(contador.values())]
print(f'La moda es: {highest_counter[0][0]}')

Cuando los datos se presentan en una tabla de frecuencias, la moda es el grupo que tiene la más alta frecuencia. En el gráfico de barras, es el grupo con la barra más alta.

df_frecuencia = pd.DataFrame.from_dict(contador, orient='index')
df_frecuencia.columns = ['frecuencia']
df_frecuencia

fig = px.bar(df_frecuencia, x=df_frecuencia.index, y=['frecuencia',],
              title=f'Gráfico de Barras Notas')
fig.show()

#### La Clase Modal

Cuando se busca la modal de datos que han sido agrupados, se debe determinar el **grupo** que tiene la mayor frecuencia. A este grupo se le llama la **clase modal**.

Si revisar toda la data, no se puede determinar cula valor dentro de la clase modal es el que tiene la mayor frecuencia.

### Media

La media aritmética, también llamada promedio, es la medida más común de tendencia central. La media es simplemente la suma de todos los valores, dividida por el número total de datos. Usualmente se denota con $\mu$ o $\overline x$. De forma más matemática:

$$\overline x = \frac{\sum_{i=1}^N x_i}{N}$$

Al contrario de la moda, la media, usualmente, es un número que no pertenece a los datos. Por ejemplo, si tus notas son 6, 6, 7 y 7 la media será 6.5 que no coincide con ninguna de las notas obtenidas.

¿Cómo se obtiene la media de los datos a partir de la tabla de frecuencias?

**Respuesta:** en el caso anterior la media se obtiene con la siguiente fórmula.

$$\overline x =\frac{\sum_{i=1}^N f_i\cdot x_i}{\sum_{i=1}^N f_i}$$

donde $f_i$ es la frecuencia de la observación $x_i$.

### Mediana

La mediana es el dato que está justo en el medio cuando los datos se ordenan de forma ascendente. Si el número de datos es par, entonces la mediana es la media de los dos datos que están en el medio.

Esto implica que 50% de los datos están a la izquierda de la mediana y 50% de los datos están a la derecha de la mediana.

**Ejemplo:**

Encontrar la mediana de 7, 12, 1, 4, 17, 9, 11, 16, 10, 18.

datos = [7, 12, 1, 4, 2, 17, 9, 11, 16, 10, 18]
datos.sort()
print(f'Los datos ordenados son: {datos}')

Son 11 elementos, el número del medio es entonces el número 6. Por lo tanto la mediana es:

print(f'mediana: {datos[6]}')

### Resumen

````{panels}
:column: col-4
:card: border-2
Moda
^^^
La **moda** cual es el valor que con más frecuencia ocurre en la muestra.

**Ventajas**

- Los valores extremos no afectan la moda.

**Desventajas**

- No utiliza todos los elementos del conjunto de datos.
- No es necesariamente única. Puede haber más de una **moda**. En estos casos su interpretación se hace difícil.
- La **moda** no está definida cuando ningún valor se repite.
---
Media
^^^
La media es la suma de todos los datos dividida por el número total de datos.

**Ventajas**

- Es la medida más popular y más utilizada.
- Utiliza todos los datos de la muestra.
- Es única y está siempre bien definida.
- Útil para comparar distintas muestras.
- Muy utilizada en cálculos posteriores.

**Desventajas**

- Se ve afectada por los valores extremos de la muestra.
---
Mediana
^^^
Ordenados los datos de la muestra de menor a mayor, la mediana es el dato que está justo al medio de la muestra.

**Ventajas**

- Los valores extremos no la afectan tanto como a la media.
- Útil para comparar distintas muestras.
- Es única y está siempre bien definida.

**Desventajas**

- No considera todos los datos de la muestra.
- Se utiliza poco en cálculos posteriores.
````

## Medidas de Dispersión

### Rango

El **rango** es la diferencia entre el máximo y el mínimo valor de una muestra.

$$Rango=\max\left(x_1,x_2,\ldots ,x_N\right)-\min\left(x_1,x_2,\ldots ,x_N\right)$$

donde $x_1,x_2,\ldots ,x_N$ son los datos de la muestra.

En el ejemplo de las notas de 32 alumnos en un examen con puntajes del 1 al 10 los resultados eran:

print(f'Resultados: {resultados}')

En este caso tenemos que:

min_res = min(resultados)
print(f'La nota mínima es: {min_res}')
max_res = max(resultados)
print(f'La nota máxima es: {max_res}')
rango = max_res - min_res
print(f'Por lo tanto el rango es: {max_res} - {min_res} = {rango} ')

### Cuartiles

Los **cuartiles**, son los valores que dividen la data en cuartos.

- El primer cuartil (llamado cuartil inferior o $Q_1$) es tal que 25% de los datos son inferiores a $Q_1$.
- El segundo cuartil es la mediana, 50% de los datos son inferiores a ella.
- El tercer cuartil (llamado cuartil superior o $Q_3$) es tal que 75% de los datos son inferiores a $Q_3$.
- El último cuartil es el máximo valor de la muestra.

**Observación:** $Q_1$ es la mediana del 50% inferior de la muestra y $Q_3$ es la mediana del 50% superior de la muestra.

### Box Plots

Es posible obtener una idea de la distribución de una muestra de datos examinando el siguiente resumen de 5 números:

- El valor mínimo
- El primer cuartil
- La mediana (segundo cuartil)
- El tercer cuartil
- El valor máximo

Estos 5 números pueden ser representados gráficamente a través de un diagrama de *Caja y Bigotes* (box-and-whisker diagram).

Veamos un ejemplo con datos generados de forma aleatoria.

import plotly.graph_objects as go
import numpy as np

x0 = np.array([-0.01266288, -0.39623657, -2.27460173,  0.26492423, -0.37191596,
       -0.0469952 , -1.12485845,  0.26766143, -1.74320972,  0.58269502,
        0.56357888, -2.16268586,  0.65205293,  0.06388311,  0.86067789,
       -1.19481468, -0.45478148, -0.86976107, -1.9288584 ,  1.28710555,
        0.17671311, -1.19529302,  0.69459011,  0.51450959,  1.81595071,
        0.8890141 , -1.31808439, -1.57484991,  0.2511651 ,  0.64026872,
       -1.04312134,  0.59108169,  0.75979648, -1.44733236,  1.65422606,
       -0.2734052 ,  1.75192239,  1.03558314,  1.01046211,  0.73390352,
       -0.82820519, -1.53824126,  0.58670701, -1.33037958,  1.34250693,
        0.71374556, -0.80025983, -0.75024957, -1.75550578, -1.62384854])

fig = go.Figure()
fig.add_trace(go.Box(x=x0))

fig.show()

La diferencia $Q_3-Q_1$ suele llamarse *rango intercuantil* y se denota con $IQR$.

### Outliers

Los datos extremos de una muestra se llaman **outliers** (en español también se usa la palabra en inglés, no existe una traducción ampliamente aceptada).

```{admonition} Criterio para Identificar un Outlier
Se considera outlier cualquier valor que esté $1.5 \cdot IQR$ veces por debajo de $Q_1$ o por encima de $Q_3$.
```

#### Cuando Rechazar o Mantener un Outlier

Hemos visto un criterio para identificar un outlier. Ahora se debe decidir si se acepta o se rechaza ese outlier (en la práctica esto significa eliminar o mantener el dato en la muestra).

Los outliers pueden tener un efecto importante en medidas estadísticas como la media, pero algunos de ellos son datos válidos y no es aceptable rechazarlos sin una razón bien fundamentada.

Por el contrario, cuando un outlier se produce por un error de medición, éste debe ser eliminado. Por ejemplo, si estamos estudiando la altura de una población, un dato de 3.0 metros es seguramente un error de medición.

Por otra parte, supongamos que los resultados de una prueba de 7 estudiantes son los siguientes: 20%, 22%, 18%, 30%, 26%, 89% y 21%. Si se concluye que el 89% está bien registrado, entonces eliminarlo conduciría a concluir que la prueba era demasiado difícil para los alumnos. Sin embargo, considerando que no hay error de medición, al mantenerlo se podría concluir que el nivel de dificultad de la prueba era el adecuado y que 6 de los 7 alumnos no se prepararon lo suficiente.