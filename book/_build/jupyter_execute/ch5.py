# Midiendo del cambio: la diferenciación

La tasa de cambio entre dos variables observables, por ejemplo:

- ¿cuántos kilómetros por hora está recorriendo un auto en un instante de tiempo?
- ¿cuánta energía se requiere para subir la temperatura de un material en 1 grado celsius?
- ¿cuánto cambia el nivel de un lago dependiendo de la cantidad de agua que recibe?
- ¿cómo cambia la tasa de contagio del COVID-19 en función de la movilidad de las personas?

El cálculo diferencial provee un paradigma para interpretar, modelar y hacer predicciones sobre este tipo de fenómenos. El cálculo diferencial fue desarrollado en el siglo XIX por Leibniz y Newton y es probablemente, hasta el día de hoy, la herramienta matemática de mayor uso y utilidad.

import math
import pandas as pd
import plotly.express as px

## Límites y Convergencia

Un límite describe el resultado de una función a medida que el input (variable independiente) se acerca a un cierto valor.

Si $f\left(x\right)$ se acerca cada vez más al número real $L$ a medida que $x$ se acerca cada vez más al número real $a$ (desde arriba y desde abajo, o sea, $x<a$ y $a<x$ entonces decimos que el límite de $f\left(x\right)$ cuando $x$ *tiende* a $a$ es $L$. Se escribe como:

$$\lim_{x\to a}f\left(x\right)=L$$

Es importante recordar que para que el límite exista para $x\to a$, es necesario que el valor del límite sea el mismo ya sea que $x$ tienda a $a$ desde arriba ($a<x$) o desde abajo ($x<a$).

En el caso que los límites desde arriba y desde abajo existan, pero sean distintos se escribe:

$$\lim_{x\to a^+}f\left(x\right)=M$$
$$\lim_{x\to a^-}f\left(x\right)=N$$

Entonces, $L$ es el límite de la función $f$ para $x$ que tiene a $a$ si y sólo si $\lim_{x\to a^+}f\left(x\right)=L$ y $\lim_{x\to a^-}f\left(x\right)=L$.

**Ejemplo**

- Graficar la función $y=\frac{3^x-1}{x}$, $x\neq 0$.
- Encontrar los límites para $x$ que tiende a 0 desde arriba y desde abajo. Entregar el resultado con 1 decimal.

def f(x):
    return (3**x - 1) / x

partes = 30
data = pd.DataFrame([(i / partes, f(i / partes)) for i in range(-partes, partes + 1) if i != 0],
                    columns=['x', 'y'])

fig = px.line(data, x='x', y=['y',],
              title=f'f(x)=(3^x - 1) / x , lim f(x), x->0 = {(f(-1 / partes) + f(1 / partes)) / 2:.1f}')

fig.update_traces(mode='markers+lines')
fig.show()

math.log(3)

### Límites al Infinito ($\infty$)

El concepto de límite nos ayuda a entender el comportamiento de las funciones para valores extremos de $x$.

La **asíntota horizontal** $y=k$ indica el comportamiento de la función para valores de $x$ muy grandes, $x\to -\infty$ o $x\to\infty$.

La **asíntota vertical** $x=c$ describe el comportamiento de la función cuando $x$ tiende a $c$ cuando $c$ no es parte del dominio de la función.

Usemos como ejemplo la función:

$$f\left(x\right)=\frac{1}{x^2}$$

def f(x):
    return 1 / x**2

partes = 100
base = 10
data = pd.DataFrame([(i * base, f(i * partes + base)) for i in range(1, partes)],
                    columns=['x', 'y'])

fig = px.line(data, x='x', y=['y',],
              title=f'f(x)=1 / x^2 , lim f(x), x->inf = {f(partes * base):.1f}')

fig.update_traces(mode='markers+lines')
fig.show()

partes = 100
base = 10
data = pd.DataFrame([(i * base , f(i * base)) for i in range(-partes, 0)],
                    columns=['x', 'y'])

fig = px.line(data, x='x', y=['y',],
              title=f'f(x)=1 / x^2 , lim f(x), x->inf = {f(-partes * base):.1f}')

fig.update_traces(mode='markers+lines')
fig.show()

## La Derivada de una Función

La tasa de cambio promedio de una función $f$ entre los valores $x_1$ y $x_2$ está dada por:

$$\frac{\Delta y}{\Delta x}=\frac{f\left(x_2\right)-f\left(x_1\right)}{x_2-x_1}$$

Si la función $f$ es lineal. el gradiente entre dos puntos es constante y por lo tanto, la tasa de cambio también es constante.

Este no es el caso de las funciones que no son lineales.

Sea $f\left(x\right)=x^2$ y sean $A\left(1,1\right)$ un punto que pertenece al gráfico de $y=f\left(x\right)$ y $B\left(x,x^2\right)$ otro punto cualquiera del gráfico.

Sea $\left(AB\right)$ la línea *secante* que une los puntos $A$ y $B$.

**Ejercicio**

- Para $x=\{2, 1.5, 1, 1.01, 1.001\}$ calcular $f\left(x\right)$ y el gradiente de $f\left(x\right)$ entre 1 y $x$.

def f(x):
    return x**2

data = [(x, f(x), (f(1)-f(x))/(1 - x)) for x in [2, 1.5, 1.1, 1.01, 1.001, 1.0001]]
df = pd.DataFrame(data, columns=['x', 'f(x)', 'gradient'])
df

data = [(x, f(x), (f(1)-f(x))/(1 - x)) for x in [0, .8, .9, .99, .999, .9999]]
df = pd.DataFrame(data, columns=['x', 'f(x)', 'gradient'])
df

Podemos ver como el gradiente de $f\left(x\right)\to 2$ cuando $x \to 1$.