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