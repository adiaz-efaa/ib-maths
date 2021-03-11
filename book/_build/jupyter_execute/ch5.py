# Midiendo el Cambio: la Derivada de una Función

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

```{admonition} Ejemplo
Vamos a investigar el gradiente de $f\left(x\right)=x^2$ ...

Para $x=\{2, 1.5, 1, 1.01, 1.001\}$ calcular $f\left(x\right)$ y el gradiente de $f\left(x\right)$ entre 1 y $x$.
```

def f(x):
    return x**2

data = [(x, f(x), (f(1)-f(x))/(1 - x)) for x in [2, 1.5, 1.1, 1.01, 1.001, 1.0001]]
df = pd.DataFrame(data, columns=['x', 'f(x)', 'gradient'])
df

```{admonition} ...
Se observa que cuando $x \to 1$, $\Delta f\left(x\right) \to 2$.

Repitamos ahora el ejercicio para $x=\{.0, .8, .9, .99, .999, .9999\}$:
```

data = [(x, f(x), (f(1)-f(x))/(1 - x)) for x in [0, .8, .9, .99, .999, .9999]]
df = pd.DataFrame(data, columns=['x', 'f(x)', 'gradient'])
df

```{admonition}  ... fin
También en este caso, se observa que $\Delta f\left(x\right)\to 2$ cuando $x \to 1$.

Escribamos ahora la expresión del gradiente para $A\left(x,x^2\right)$ y $B\left(x+h,\left(x+h\right)^2\right)$:

$$\Delta f\left(x\right) =\frac{\left(x+h\right)^2-x^2}{x+h-x}$$

$$\Delta f\left(x\right)= \frac{x^2+2xh+h^2-x^2}{h}$$

$$\Delta f\left(x\right)= \frac{h\left(2x+h\right)}{h}$$

$$\Delta f\left(x\right)= 2x+h$$

Vemos entonces que si $h \to 0$, $\Delta f\left(x\right)\to 2x$.
```

El gradiente de línea de la línea secante $AB$ es $\frac{f\left(x+h\right)-f\left(x\right)}{h}$.

Este gradiente es una medida de **la tasa de cambio promedio** de $f\left(x\right)$ entre $x$ y $x+h$.

Cuando $B \to A$, el gradiente de $(AB)$ tiende al gradiente de la línea recta tangente al gráfico de la función $x$.

```{admonition} Definición

El gradiente de la recta tangente al gráfico (o curva) en $A$ es la tasa de cambio instantánea de $f\left(x\right)$ en $A$. Esta tasa de cambio instantánea se llama la derivada de $f$ con respecto a $x$.

Se usan las siguientes notaciones: $f'\left(x\right)$, $\frac{df\left(x\right)}{dx}$, $\frac{dy}{dx}$.
```

## Primeras Reglas para Calcular Derivadas

**Resultados:**

- Derivada de un monomio:
  - Si $n \in \mathbb{R}$ (es un número real) y $f\left(x\right)=x^n$, entonces $f'\left(x\right)=nx^{n-1}$.


- Derivada de una función constante:
  - Si $f\left(x\right)=c$ donde $c \in \mathbb{R}$, entonces $f'\left(x\right)=0$
  - Se puede deducir de la derivada de un monomio si se escribe $c=cx^0$.
  
  
- Derivada de una función lineal:
  - Si $f\left(x\right)=mx+c$ donde $m,c \in \mathbb{R}$, entonces $f'\left(x\right)=m$
  - Sigue de la regla para el monomio y para la función constante.
  
  
- La derivada es una **operación lineal**:
  - Si $h\left(x\right)=af\left(x\right)+bg\left(x\right)$ con $a,b\in\mathbb{R}$ entonces $h'\left(x\right)=af'\left(x\right)+bg'\left(x\right)$


- Derivada de un polinomio:

$$f\left(x\right)=\sum_{i=0}^na_ix^i\Rightarrow f'\left(x\right)=\sum_{i=1}^nia_ix^{i-1}$$

```{admonition} Ejemplo
Encontrar la derivada de las siguientes funciones:

- $f\left(x\right)=\frac{3}{x^{12}}$
  - Se puede escribir $f\left(x\right)=3x^{-12}$ y aplicamos la regla para un monomio. Se obtiene $f'\left(x\right)=-36x^{-13}$.
  
- $f\left(x\right)=\frac{2x^4-3x^3+1}{x^2}$

$$f\left(x\right)=x^{-2}\left(2x^4-3x^3+1\right)$$

$$f\left(x\right)=2x^2-3x+x^{-2}$$

$$\Rightarrow f'\left(x\right)=4x-3-2x^{-3}$$

```

## Tangentes y Normales

**Motivación:** ¿Cuánto puede inclinarse una moto al tomar una curva con peralte sin caerse? Para que la moto se mantenga en una trayectoria circular, se requiere una fuerza que evite que se "arranque por la tangente". Esta fuerza debe ser perpendicular a la tangente (la derivada) de la trayectoria.

https://www.youtube.com/watch?v=MT3tC4BlCEU

```{admonition} Ejemplo 1
Consideremos la función $f\left(x\right)=x^2$ su derivada es $f'\left(x\right)=2x$. El valor del gradiente de la recta tangente en $x=0$ es, por lo tanto $0$. La ecuación de esa recta es $y=0$, la ecuación de la recta normal es $x=0$. La pendiente de $y=0$ es $0$, mientras que la pendiente de $x=0$ es $\infty$ (que puede pensarse como $\frac{1}{x}$ para $x\to 0$.
```

def f(x): return x**2


data = [(x, f(x), 0) for x in range(-5, 6)]
df = pd.DataFrame(data, columns=['x', 'f(x)', 'y=0'])
fig = px.line(
    df,
    x='x',
    y=['f(x)', 'y=0'],
    title=f'f(x)= x^2 y tangente en x=0')

fig.update_traces(mode='markers+lines')
fig.show()

```{admonition} Ejemplo 2
Consideremos la misma función anterior, pero calculemos el gradiente de la recta tangente en $x=1$, en este caso el resultado es $2$ y la pendiente de la recta perpendicular a la tangente en $x=1$ es $-\frac{1}{2}$.
```

def f(x): return x**2
def g(x): return 2*x - 1
def h(x): return -1/2*x+3/2


data = [(x, f(x), g(x), h(x)) for x in range(-5, 6)]
df = pd.DataFrame(data, columns=['x', 'f(x)', 'y=2x - 1', 'y=-1/2x+3/2'])
fig = px.line(
    df,
    x='x',
    y=['f(x)', 'y=2x - 1', 'y=-1/2x+3/2'],
    title=f'f(x)= x^2 y tangente y perpendicular en x=1')

fig.update_traces(mode='markers+lines')
fig.update_yaxes(
    scaleanchor = "x",
    scaleratio = 1,
  )
fig.show()

```{admonition} Resultado
Si la recta tangente a un punto de la curva tiene pendiente $m$, entonces la recta perpendicular tiene pendiente igual a  $\frac{-1}{m}$.

## Más Reglas para Calcular Derivadas

Veremos reglas (fórmulas) para encontrar la derivada de una función compuesta $h\left(x\right)=f\left(g\left(x\right)\right)$, para el producto de dos funciones $h\left(x\right)=f\left(x\right)g\left(x\right)$ y para el cociente de dos funciones $h\left(x\right)=\frac{f\left(x\right)}{g\left(x\right)}$.

### La Regla de la Cadena

La función $y=\left(3-x\right)^3$ puede ser escrita como la composición de dos funciones $g$ y $f$ tales que $y=f\left(g\left(x\right)\right)$ o $\left(f \circ g\right)\left(x\right)$ donde $g\left(x\right)=3-x$ y $f\left(x\right)=x^3$.

```{admonition} Intuición
Expandir $y=\left(1+x\right)^2$ y encontrar $\frac{dy}{dx}$.

$$y=x^2+2x+1\Rightarrow \frac{dy}{dx}=2\left(x+1\right)$$

Escribir $y=\left(1+x\right)^2$ como composición de 2 funciones $f$ y $g$.

$$g\left(x\right)=x^2$$
$$f\left(x\right)=1+x$$

Sea $u=g\left(x\right)$, encontrar $\frac{du}{dx}$.

$$\frac{du}{dx}=2x$$

Escribir $y$ en términos de la variable $u$ y encontrar $\frac{dy}{du}$.

$$y=f\left(u\right)$$
$$y=1+u\Rightarrow \frac{dy}{du}=1$$

Calcular $\frac{dy}{du}\times \frac{du}{dx}$ y expresar el resultado en términos de $x$.

$$\frac{dy}{du}\times \frac{du}{dx}=2u\cdot 1$$

$$=2\left(1+x\right)\cdot 1$$

$$=2\left(1+x\right)$$

Vemos como este último resultado coincide con el cálculo inicial.
```

**Regla de la Cadena:** Si $y=f\left(u\right)$ y $u=g\left(x\right)$ entonces:

$$\frac{dy}{dx}=\frac{dy}{du}\times \frac{du}{dx}$$

Alternativamente, se puede escribir:

$$\left(f\circ g\right)'\left(x\right)=f'\left(g\left(x\right)\right)\cdot g'\left(x\right)$$