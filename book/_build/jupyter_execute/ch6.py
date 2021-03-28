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

**Ejemplo:**

Encontrar la mediana de 7, 12, 1, 4, 17, 9, 11, 16, 10, 18.

datos = [7, 12, 1, 4, 2, 17, 9, 11, 16, 10, 18]
datos.sort()
print(f'Los datos ordenados son: {datos}')

Son 11 elementos, el número del medio es entonces el número 6. Por lo tanto la mediana es:

print(f'mediana: {datos[6]}')