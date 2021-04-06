# Estadística para Datos Univariados

Datos univariados (o data univariada) son datos que se describen con una sola variable. Por ejemplo, las alturas de los compñaeros de clase son datos univariados. El propósito principal del análisis de datos univariados es la descripción de los datos. 

El análisis de datos univariados no considera relaciones entre distintas variables, como podría ser la relación entre la altura y el peso de los compañeros de clase.

import math
import random
import numpy as np
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

### Frecuencia Acumulada

Los siguientes datos muestran el número de veces que 50 estudiantes perdieron un lápiz durante la semana:

lapices = [5, 9, 10, 5, 9, 9, 8, 4, 9, 8, 5, 7, 3, 10, 7, 7, 8, 7, 6, 6, 9, 6, 4,
           4, 10, 5, 6, 6, 3, 8, 7, 8,3, 4, 6, 6, 5, 7, 5, 4, 3, 5, 2, 4, 2, 8, 1,0, 3, 5]

Vamos a construir una tabla de frecuencia acumulada, es decir, en cada fila vamos a anotar el número de lápices perdidos y el número de alumnos que ha perdido ese número de lápices o menos:

frec_acum = [(i, sum([lapices.count(j) for j in range(i+1)])) for i in range(11)]
df_frec_acum = pd.DataFrame(
    frec_acum,
    columns=['num_lapices', 'Número de alumnos que perdió num_lapices o menos lápices'])
df_frec_acum

Vamos a dibujar el gráfico de la fecuencia acumulada:

fig = px.line(
    df_frec_acum,
    x='num_lapices',
    y=['Número de alumnos que perdió num_lapices o menos lápices',],
    title=f'Gráfico de la Frecuencia Acumulada')

fig.update_traces(mode='markers+lines')
fig.show()

- El menor valor en el eje $y$ del gráfico es 1 y el mayor valor es 50, que coincide con el número de alumnos.
- Dado que para cada nuevo valor de la variable `num_lapices`, agregamos más alumnos, el gráfico nunca puede ser decreciente.

Cuando se dispone de toda la data (*raw data*) se puede utilizar la fórmula:

$$mediana=\left(\frac{n+resto\left(n,2\right)}{2}\right)esimo\space valor$$

para calcular la mediana y los cuartiles cuando la data se ordena de forma ascendente. Aquí, $resto\left(n,2\right)$ es el resto de la división entera de $n$ por 2, por lo tanto será 0 si $n$ es par y 1 si $n$ es impar. Para muestras con muchos datos, esta distinción se hace muy poco significativa.

Sin embargo, cuando se dispone de data agrupada, puede ser difícil determinar la mediana o un cuartil cuando ese valor está en el medio de uno de los grupos.

Las curvas de frecuencia acumulada permiten estimar la mediana y los cuartiles a partir de data acumulada. Por ejemplo, para encontrar la mediana, se dibuja una línea horizontal que cruza el eje $y$ en el $\frac{n}{2} esimo$ valor y desde la intersección de esa línea con el gráfico de frecuencia acumulada, se traza una línea vertical hacia abajo. El punto donde esta línea intersecta el eje $x$, corresponde a la mediana.

Por ejemplo, en el caso anterior:

fig = px.line(
    df_frec_acum,
    x='num_lapices',
    y=['Número de alumnos que perdió num_lapices o menos lápices'],
    title=f'Gráfico de la Frecuencia Acumulada con Cálculo de Mediana')
fig.update_traces(mode='lines')
fig.add_hline(y=25, annotation_text=' y=25', line_color='green')
fig.add_vline(x=5.3, annotation_text=' x=5.3 => mediana=5.3\n', line_color='red')
fig.show()

### Percentiles

Un *percentil* es un número tal que un porcentaje de los datos están por debajo de del percentil. Por ejemplo, si el percentil 10% es $P_{10}$ esto significa que un 10% de los datos de la muestra están por debajo de $P_{10}$. 

Veamos un ejemplo con una muestra de 500 datos con números aleatorios entre 1 y 100 (que podrían representar los puntajes en una prueba tomada por 500 alumnos).

np.random.seed(123456)
notas = np.random.lognormal(0, 1, 500) * 40
notas = [int(min(nota, 100)) for nota in notas]
notas_frec_acum = [(i, sum([notas.count(j) for j in range(i+1)])) for i in range(101)]
df_notas_frec_acum = pd.DataFrame(
    notas_frec_acum,
    columns=['nota', 'Número de alumnos con nota igual o inferior'])

Veamos las primeras 12 filas de la tabla con las frecuencias acumuladas:

df_notas_frec_acum.head(12)

Podemos observar que hay 5 alumnos (un 1.0%) con puntaje igual o menor a 2 y 7 (1.4%) alumnos con un puntaje igual a 3. Esto nos indica que el percentil 1% de esta muestra está "entremedio" de estos dos valores y que el percentil 1% no es un puntaje posible de obtener (así como la media, muchas veces, no corresponde a ningún resultado de la medición).

```{admonition} Cálculo de Percentil
:class: tip
En estas situaciones, existen varias maneras de calcular un percentil y es importante tener claro, según el contexto, cuál se está utilizando y cómo se calcula.
```

Por ejemplo en este caso:

percentil = 1

metodo = 'lower'
print(f'Percentil {percentil/100:.1%}, método={metodo}: {np.percentile(notas, percentil, interpolation=metodo):.4f}')

metodo = 'higher'
print(f'Percentil {percentil/100:.1%}, método={metodo}: {np.percentile(notas, percentil, interpolation=metodo):.4f}')

metodo = 'midpoint'
print(f'Percentil {percentil/100:.1%}, método={metodo}: {np.percentile(notas, percentil, interpolation=metodo):.4f}')

metodo = 'linear'
print(f'Percentil {percentil/100:.1%}, método={metodo}: {np.percentile(notas, percentil, interpolation=metodo):.4f}')

En este ejemplo estamos usando la función `percentile` de `numpy`, que tiene la siguiente documentación. Lo referido al parámetro `interpolation` explica el funcionamiento de los distintos métodos.

print(np.percentile.__doc__)

### Varianza y Desviación Estándar

El rango y los cuartiles son buenas medidas de cuan dispersa está una muestra de datos respecto a su mediana, pero no utilizan toda la data disponible. Por otro lado, la **varianza** es una métrica de dispersión que utiliza todos los datos de la muestra. Es una métrica que refleja qué tan lejanos están, en promedio, cada uno de los datos de la media.

Para ejemplificar, volvamos a considerar el ejemplo de los resultados de 32 alumnos en una prueba con puntajes entre 0 y 10. Los datos eran los siguientes:

print(f'Notas de 32 alumnos: {resultados}')

Tabulemos esta data y vamos calculando paso a paso la varianza:

df_resultados = pd.DataFrame(resultados, columns=['nota',])
df_resultados

Se calcula la media:

media = np.mean(df_resultados['nota'])
print(f'La media es: {media:.2f}')

Se calcula la distancia de cada nota a la media:

df_resultados['(nota - media)'] = df_resultados['nota'] - media
df_resultados

Se calcula ahora el cuadrado de la distancia:

df_resultados['(nota - media)^2'] = df_resultados['(nota - media)'] ** 2
df_resultados

Elevar al cuadrado la distancia logra dos objetivos:

- evitar que las distancias negativas se compensen con las positivas dando así un falsa idea de la dispersión.
- ponderar más en el promedio final las distancias mayores.

Finalmente, la varianza, que usualmente se denota con $\sigma^2$ está dada por:

$$\sigma^2=\frac{1}{n}\sum_{i=1}^n{\left(x_i-\mu\right)^2}$$

Aquí, $\mu$ es la media de los datos.

En el ejemplo, la variaza resulta ser:

print(f"Varianza es: {np.mean(df_resultados['(nota - media)^2']):.2f}")

Dado que la unidad en la que se mide la **varianza** no coincide con la unidad de los datos, también se define la desviación estándar, que se denota con $\sigma$, como:

$$\sigma=\sqrt{\frac{1}{n}\sum_{i=1}^n{\left(x_i-\mu\right)^2}}=\sqrt{\sigma^2}$$

#### Propiedades de la Desviación Estándar

- La **desviación estándar** sólo se utiliza para medir dispersión alrededor de la media.
- La **varianza** y la **desviación estándar** son siempre positivas.
- La **desviación estándar** es sensible a los *outliers*. Un sólo *outlier* puede cambiar significativamente su valor.
- Para muestras de datos con una **media** similar, mientras más dispersión en los datos mayor es la **desviación estándar**.