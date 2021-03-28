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

$\newcommand{\fx}{f\left(x\right)}$
$\newcommand{\gx}{g\left(x\right)}$
$\newcommand{\hx}{h\left(x\right)}$
$\newcommand{\ux}{u\left(x\right)}$
$\newcommand{\vx}{v\left(x\right)}$
$\newcommand{\dfx}{f'\left(x\right)}$
$\newcommand{\dgx}{g'\left(x\right)}$
$\newcommand{\dhx}{h'\left(x\right)}$
$\newcommand{\dux}{u'\left(x\right)}$
$\newcommand{\dvx}{v'\left(x\right)}$
$\newcommand{\ddfx}{f''\left(x\right)}$
$\newcommand{\ddgx}{g''\left(x\right)}$
$\newcommand{\ddhx}{h''\left(x\right)}$
$\newcommand{\ddux}{u''\left(x\right)}$
$\newcommand{\ddvx}{v''\left(x\right)}$

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

print(f'f(-.1) = {f(-.1):.1f}')
print(f'f(-.01) = {f(-.01):.1f}')
print(f'f(-.001) = {f(-.001):.1f}')
print(f'f(-.0001) = {f(-.0001):.1f}')
print(f'f(.0001) = {f(.0001):.1f}')
print(f'f(.001) = {f(.001):.1f}')
print(f'f(.01) = {f(.01):.1f}')
print(f'f(.1) = {f(.1):.1f}')

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
              title=f'f(x)=1 / x^2 , x > 0, lim f(x), x->+inf = 0, x->0 = +inf')

fig.update_traces(mode='lines')
fig.show()

partes = 100
base = 10
data = pd.DataFrame([(i * base , f(i * base)) for i in range(-partes, 0)],
                    columns=['x', 'y'])

fig = px.line(data, x='x', y=['y',],
              title=f'f(x)=1 / x^2 , x < 0, lim f(x), x->-inf = 0, x->0 = +inf')

fig.update_traces(mode='lines')
fig.show()

## La Derivada de una Función

La tasa de cambio promedio (cambio en la función por unidad de cambio en la variable independiente) de una función $f$ entre los valores $x_1$ y $x_2$ está dada por:

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

```{admonition} ... continúa ejemplo
Se observa que cuando $x \to 1$, $\Delta f\left(x\right) \to 2$.

Repitamos ahora el ejercicio para $x=\{.0, .8, .9, .99, .999, .9999\}$:
```

data = [(x, f(x), (f(1)-f(x))/(1 - x)) for x in [0, .8, .9, .99, .999, .9999]]
df = pd.DataFrame(data, columns=['x', 'f(x)', 'gradient'])
df

```{admonition}  ... fin ejemplo
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
Consideremos la función $f\left(x\right)=x^2$ su derivada es $f'\left(x\right)=2x$. El valor del gradiente de la recta tangente en $x=0$ es, por lo tanto, $0$. La ecuación de esa recta es $y=0$, la ecuación de la recta perpendicular es $x=0$. La pendiente de $y=0$ es $0$, mientras que la pendiente de $x=0$ es $\infty$ (que puede pensarse como $\frac{1}{x}$ para $x\to 0$.
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
:class: tip
Consideremos $y=\left(1+x\right)^2$. Para encontrar encontrar $\frac{dy}{dx}$ primero expandimos $y=\left(1+x\right)^2$ y luego derivamos con la regla del polinomio.

$$y=x^2+2x+1\Rightarrow \frac{dy}{dx}=2\left(x+1\right)$$

Escribir $y=\left(1+x\right)^2$ como composición de 2 funciones $f$ y $g$.

$$g\left(u\right)=u^2$$
$$u=f\left(x\right)=1+x$$

Si escribimos $y=g\left(u\right)$ vemos que:

$$\frac{dy}{du}=2u$$

Por otra parte $\frac{du}{dx}=1$.


Calculamos $\frac{dy}{du}\times \frac{du}{dx}$ y expresamos el resultado en términos de $x$.

$$\frac{dy}{du}\times \frac{du}{dx}=2u\cdot 1$$

$$=2\left(1+x\right)\cdot 1$$

$$=2\left(1+x\right)$$

Vemos como este último resultado coincide con el cálculo inicial.
```

```{admonition} Regla de la Cadena:
Si $y=f\left(u\right)$ y $u=g\left(x\right)$ entonces:

$$\frac{dy}{dx}=\frac{dy}{du}\times \frac{du}{dx}$$

Alternativamente, se puede escribir:

$$\left(f\circ g\right)'\left(x\right)=f'\left(g\left(x\right)\right)\cdot g'\left(x\right)$$
```

Una forma intuitiva de pensar y recordar la regla de la cadena es la siguiente. Sea $u=g\left(x\right)$ e $y=f\left(u\right)$, queremos encontrar $\frac{dy}{dx}$.

Recordemos la definición de derivada:

$$\lim_{h\to 0}\frac{f\left(x+h\right)-f\left(x\right)}{h}=f'\left(x\right)$$

Si $y=f\left(x\right)$, podemos expresar esta definición de la siguiente manera:

$$\delta y \approx f'\left(x\right)\delta x$$

para $\delta x$ suficientemente pequeño. En palabras, podemos aproximar la variación de $y$ para una variación pequeña de $x$ multiplicando la derivada de $f$ en $x$ por la variación en $x$.

Volviendo a la regla de la cadena:

$$\delta u \approx g'\left(x\right)\delta x$$

$$\delta y \approx f'\left(u\right)\delta u$$

Por lo tanto,

$$\delta y \approx f'\left(u\right)g'\left(x\right)\delta x$$

$$\delta y \approx f'\left(g\left(x\right)\right)g'\left(x\right)\delta x$$

$$\frac{\delta y}{\delta x} \approx f'\left(g\left(x\right)\right)g'\left(x\right)$$

O sea (y este paso no es del todo riguroso porque no estamos calculando el límite para $\delta x \to 0$.

$$\frac{dy}{dx}=f'\left(g\left(x\right)\right)g'\left(x\right)$$

**Ejemplo**

Sea,

$$y=\left(x^2-4x\right)^3$$

Aquí hay dos funciones encadenadas:

$$u=x^2-4x$$

$$y=u^3$$

Tenemos que:

$$\frac{du}{dx}=2x-4$$

$$\frac{dy}{du}=3u^2$$

Y por lo tanto:

$$\frac{dy}{dx}=\frac{dy}{du}\frac{du}{dx}=3u^2\left(2x-4\right)=3\left(x^2-4x\right)^2\left(2x-4\right)$$

### Regla del Producto

Recordemos, si $y=f\left(x\right)$, podemos escribir $\delta y \approx f'\left(x\right)\delta x$. Además, recordando que $\delta y = f\left(x+\delta x\right)-f\left(x\right)$ tenemos esta segunda expresión:

$$f\left(x+\delta x\right) \approx f\left(x\right) + f'\left(x\right)\delta x$$

Con esta fórmula, veamos como podemos calcular la derivada del producto de dos funciones $y=f\left(x\right)g\left(x\right)$. Comencemos evaluando $\delta y=f\left(x+\delta x\right)g\left(x+\delta x\right)-f\left(x\right)g\left(x\right)$.

$$\delta y=f\left(x+\delta x\right)g\left(x+\delta x\right)-f\left(x\right)g\left(x\right)$$

$$=\left(f\left(x\right) + f'\left(x\right)\delta x\right)\left(g\left(x\right) + g'\left(x\right)\delta x\right)-f\left(x\right)g\left(x\right)$$

$$=f'\left(x\right)g\left(x\right)\delta x + g'\left(x\right)f\left(x\right)\delta x + f'\left(x\right)g'\left(x\right)\delta x^2
$$

De esto sigue que:

$$\frac{\delta y}{\delta x}=f'\left(x\right)g\left(x\right) + g'\left(x\right)f\left(x\right)+ f'\left(x\right)g'\left(x\right)\delta x
$$

Y por lo tanto, haciendo que $\delta x \to 0$ obtenemos que:

$$\frac{dy}{dx}=f'\left(x\right)g\left(x\right) + g'\left(x\right)f\left(x\right)$$

```{admonition} Regla del Producto
$$\frac{d\left(f\left(x\right)g\left(x\right)\right)}{dx}=f'\left(x\right)g\left(x\right) + g'\left(x\right)f\left(x\right)$$
```

```{admonition} Ejemplo

$$f\left(x\right)=\left(x^3+3x^2+6\right)\left(2x-1\right)$$

$$f\left(x\right)=u\left(x\right)v\left(x\right)$$

$$u\left(x\right)=x^3+3x^2+6$$

$$v\left(x\right)=2x-1$$

$$u'\left(x\right)=3x^2+6x$$

$$v'\left(x\right)=2$$

$$\frac{df\left(x\right)}{dx}=u'\left(x\right)v\left(x\right)+v'\left(x\right)u\left(x\right)=$$

$$=\left(3x^2+6x\right)\left(2x-1\right)+2\left(x^3+3x^2+6\right)$$

$$=8x^3+15x^2-6x+12$$
```

### Regla del Cociente

- Consideremos la función $Q\left(x\right)=\frac{u\left(x\right)}{v\left(x\right)}$
- Calculemos $Q'\left(x\right)$ usando la regla del producto:

$$Q\left(x\right)v\left(x\right)=u\left(x\right)$$

$$Q'\left(x\right)v\left(x\right)+v'\left(x\right)Q\left(x\right)=u'\left(x\right)$$

$$Q'\left(x\right)=\frac{u'\left(x\right)-v'\left(x\right)Q\left(x\right)}{v\left(x\right)}$$

$$Q'\left(x\right)=\frac{u'\left(x\right)v\left(x\right)-v'\left(x\right)u\left(x\right)}{v\left(x\right)^2}$$

```{admonition} Regla del Cociente
Si $f\left(x\right)=\frac{u\left(x\right)}{v\left(x\right)}$, $v\left(x\right)\neq 0$ entonces:

$$f'\left(x\right)=\frac{u'\left(x\right)v\left(x\right)-v'\left(x\right)u\left(x\right)}{v\left(x\right)^2}$$
```

```{adminition} Ejemplo
$$y=\frac{x^2-3}{3x-x^2}$$

$$u\left(x\right)=x^2-3 \Rightarrow u'\left(x\right)=2x$$

$$v\left(x\right)=3x-x^2 \Rightarrow v'\left(x\right)=3-2x$$

Aplicando la regla del cociente a $y=\frac{u\left(x\right)}{v\left(x\right)}$ se obtiene:

$$y'=\frac{2x\left(3x-x^2\right)-\left(3-2x\right)\left(x^2-3\right)}{\left(3x-x^2\right)^2}$$

Simplificar. Puede ser necesario expandir el numerador, pero el denominador puede dejarse sin expandir (forma factorizada).

$$y'=\frac{3x^2-6x+9}{\left(3x-x^2\right)^2}$$
```

## Interpretación Gráfica de la Primera y Segunda Derivada

### Funciones Crecientes y Decrecientes

- Una función $y=f\left(x\right)$ se dice **creciente** en un intervalo si cuando $x$ aumenta dentro del intervalo $y$ también aumenta. Si $I$ es el intervalo, lo anterior se escribe como:

$$x_1 \in I \land x_2 \in I : x_1 < x_2 \Rightarrow f\left(x_1\right) < f\left(x_2\right)$$

- Una función $y=f\left(x\right)$ se dice **decreciente** en un intervalo si cuando $x$ disminuye dentro del intervalo $y$ también disminuye.

$$x_1 \in I \land x_2 \in I : x_1 > x_2 \Rightarrow f\left(x_1\right) > f\left(x_2\right)$$

La función $y=x^2$ es **decreciente** en el intervalo $(-\infty,0]$ y **creciente** en el intervalo $[0,\infty)$.

Tenemos además que $y'=2x$ y por lo tanto:

- $y'<0$ si $x \in (-\infty,0)$
- $y'>0$ si $x \in (0,\infty)$.

Se tiene el siguiente resultado:

- Si $f'\left(x\right)>0$ $\forall x \in \left(a,b\right)$ entonces $f$ es creciente en $\left(a,b\right)$.
- Si $f'\left(x\right)<0$ $\forall x \in \left(a,b\right)$ entonces $f$ es decreciente en $\left(a,b\right)$.

Considerar la función $y=x^3-3x+4$. Queremos indentificar en qué intervalos la función es creciente y en cuáles es decreciente. Partamos investigando el gráfico.

def f(x):
    return x**3 - 3*x + 4

izquierda = -3
derecha = 3
partes = 10
steps = (derecha - izquierda) * partes
data = pd.DataFrame([(izquierda + i/partes, f(izquierda + i/partes), f(-1), f(1)) for i in range(steps + 1)],
                    columns=['x', 'y', 'df/dx=0 (1)', 'df/dx=0 (2)'])

fig = px.line(data, x='x', y=['y', 'df/dx=0 (1)', 'df/dx=0 (2)'],
              title="f(x)=x^3 - 3x + 4, tangentes a los puntos donde df/dx=0")


fig.update_yaxes(
    scaleanchor = "x",
    scaleratio = 1/4,
  )
fig.show()

Se observa como la función es creciente ($f'>0$) desde $-\infty$ hasta el primer punto donde $f'=0$. Luego es decreciente ($f'<0$) hasta el segundo punto donde $f'=0$. Finalmente, vuelve a ser creciente ($f'>0$) a la derecha del segundo punto donde $f'=0$.

Para calcular esos puntos, hay que calcular la derivada de la función y luego encontrar los puntos en los que la derivada tiene valor 0.

- $f'\left(x\right)=3x^2-3=3\left(x-1\right)\left(x+1\right)$
- $f'\left(x\right)=0\Rightarrow x=\pm 1$

**Conclusión:** para determinar los intervalos donde la función es creciente (decreciente), se calcula su derivada y luego los valores de $x$ en los cuales la derivada es igual a 0. Finalmente, determinamos el signo de la derivada a la derecha y a la izquierda de sus ceros, recordando que $f'\left(x\right)>0$ significa que la función es creciente y $f'\left(x\right)<0$ significa que la función es decreciente.

**Importante:** Una función puede ser creciente (decreciente) a ambos lados de un punto donde su derivada es igual a 0. Esto se llama punto de inflexión y lo veremos un poco más adelante. El ejemplo más sencillo es $y=x^3$ en $x=0$ su derivada, ($3x^2$), es 0 y la función es creciente a ambos lados de $x=0$.

El ejercicio anterior lleva naturalmente a establecer las siguientes definiciones. Sea $Dom$ el dominio de la función $y=\fx$.

- $A$ es un **mínimo global** de la función $\fx$, si $f\left(A\right)<\fx$ $\forall x \in Dom \land x \neq A$.


- $B$ es un **máximo local** de la función $\fx$ si:
  - $f'\left(B\right)=0$ y
  - $f'\left(x\right)>0$ para todos los valores $x<B$ suficientemente cerca de $B$ y
  - $f'\left(x\right)<0$ para todos los valores $x>B$ suficientemente cerca de $B$


- $C$ es un **mínimo local** de la función $\fx$ si:
  - $f'\left(B\right)=0$ y
  - $f'\left(x\right)<0$ para todos los valores $x<C$ suficientemente cerca de $C$ y
  - $f'\left(x\right)>0$ para todos los valores $x>C$ suficientemente cerca de $C$


- $D$ es un **máximo global** de la función $\fx$, si $f\left(D\right)>\fx$ $\forall x \in Dom \land x \neq D$.

### Derivada Segunda

Si $y=f\left(x\right)$ y existe la derivada $f'\left(x\right)$ se puede tratar de calcular la derivada de la derivada, si ésta existe se llama **derivada segunda** de $f$ y se denota con $f''\left(x\right)$. También se usa la notación $f''\left(x\right)=\frac{d^2 f}{dx^2}$.

¿Para qué calcular la derivada segunda de una función?

- Algunas cantidades físicas se modelan naturalmente con la derivada segunda. Por ejemplo, si $x=x\left(t\right)$, la velocidad corresponde a $\frac{dx}{dt}$ y la **aceleración** (cuanto cambia la velocidad en una unidad o instante de tiempo) corresponde a $\frac{d^2x}{dt^2}$.
- Como veremos en los siguientes ejemplos, los puntos de una función en los cuales $f''\left(x\right)=0$ son los puntos donde la curvatura de la función cambia (de cóncava a convexa o de convexa a cóncava). 

Ejemplo:

- Consideremos $f\left(x\right)=x^2$.
- La derivada es $2x$ (que tiene un único 0 en $x=0$).
- La derivada segunda es 2. La función es siempre convexa, su curvatura es hacia arriba.

def f(x): return x**2
def g(x): return 2*x
def h(x): return 2


data = [(x, f(x), g(x), h(x)) for x in range(-5, 6)]
df = pd.DataFrame(data, columns=['x', 'y=x^2', 'y=2x', 'y=2'])
fig = px.line(
    df,
    x='x',
    y=['y=x^2', 'y=2x', 'y=2'],
    title=f'f(x)= x^2, primera y segunda derivada')

fig.update_traces(mode='markers+lines')
fig.show()

Ejemplo:

- Por otro lado si $f\left(x\right)=-x^2$ entonces
- La derivada es $-2x$ (que tiene un único 0 en $x=0$).
- La derivada segunda es -2. La función es siempre cóncava, su curvatura es hacia abajo.

def f(x): return -x**2
def g(x): return -2*x
def h(x): return -2


data = [(x, f(x), g(x), h(x)) for x in range(-5, 6)]
df = pd.DataFrame(data, columns=['x', 'y=-x^2', 'y=-2x', 'y=-2'])
fig = px.line(
    df,
    x='x',
    y=['y=-x^2', 'y=-2x', 'y=-2'],
    title=f'f(x)= -x^2, primera y segunda derivada')

fig.update_traces(mode='markers+lines')
fig.show()

Ejemplo

- Finalmente, consideremos $f\left(x\right)=x^3$ entonces
- La derivada es $3x^2$ (que tiene un único 0 en $x=0$).
- La derivada segunda es $6x$ (que también tiene un único 0 en $x=0$). La función es siempre cóncava a la izquierda de 0 y siempre convexa a la derecha de 0.

def f(x): return x**3
def g(x): return 3*x**2
def h(x): return 6*x


data = [(x, f(x), g(x), h(x)) for x in range(-5, 6)]
df = pd.DataFrame(data, columns=['x', 'y=x^3', 'y=3x^2', 'y=6x'])
fig = px.line(
    df,
    x='x',
    y=['y=x^3', 'y=3x^2', 'y=6x'],
    title=f'f(x)= x^3, primera y segunda derivada')

fig.update_traces(mode='markers+lines')
fig.show()

**Test de la Segunda Derivada para Máximos y Mínimos**

- Si $f'\left(c\right)=0$ y $f''\left(c\right)<0$ entonces $f\left(x\right)$ tiene un máximo local en $x=0$.
- Si $f'\left(c\right)=0$ y $f''\left(c\right)>0$ entonces $f\left(x\right)$ tiene un mínimo local en $x=0$.
- Si $f'\left(c\right)=0$ y $f''\left(c\right)=0$ entonces no se puede concluir si $c$ es máximo o mínimo local. En este caso hay que revisar el signo de la derivada primera a ambos lados de $c$.

**Definiciones**

- $f$ es cóncava (*concave down*) en un intervalo $\left(a,b\right)$ si $f\left(x\right)<0$, $\forall x \in \left(a,b\right)$.
- $f$ es convexa (*concave up*) en un intervalo $\left(a,b\right)$ si $f\left(x\right)>0$, $\forall x \in \left(a,b\right)$.
- Un punto de **inflexión** de $f\left(x\right)$ corresponde a un cambio en la curvatura del gráfico de $f$ (de cóncavo a convexo o viceversa).
  - Se puede demostrar que si $f$ tiene un punto de inflexión en $x=c$ entonces $f''\left(c\right)=0$.
- Si $f$ tiene un punto de inflexión en $x=c$ y $f'\left(c\right)=0$, el punto $c$ se dice **punto de inflexión horizontal**, porque la recta tangente a $f$ en $x=c$ es paralela al eje $x$.

## Aplicaciones: Optimización y Cinemática

Consideremos un tarro de bedida. El volumen usual de estos tarros es 330 ml. Dado que las compañías que producen los tarros quieren usar la menor cantidad de material posible, vamos a calcular que altura y diámetro deben tener para minimizar su superfice total y por lo tanto la cantidad de material utilizado en su fabricación.

- La superficie del cilindro está dada por $S=2\pi rh + 2\pi r^2$. El primer término corresponde a la parte curva y el segundo a la suma de las partes de arriba y abajo.
- Por otro lado, el volumen del cilindro es $V=\pi r^2 h$.
- Queremos que $V=330 ml$, por lo tanto $\pi r^2 h=330$ y a su vez, queremos que la superficie total sea la mínima.
- Tenemos que $h=\frac{330}{\pi r^2}$ y por lo tanto, $S\left(r\right)=2\pi r \frac{330}{\pi r^2}+ 2\pi r^2=\frac{660}{r}+ 2\pi r^2$.
- $S'\left(r\right)=-\frac{660}{r^2}+4\pi r$

def s(r): return 660.0 / r + 2.0 * math.pi * r**2


data = [(r, s(r)) for r in [1, 1.5, 2, 2.5, 3, 3.5, 3.6, 3.7, 3.8, 3.9, 4]]
df = pd.DataFrame(data, columns=['r', 'S(r)'])
fig = px.line(
    df,
    x='r',
    y=['S(r)'],
    title=f'Superficie del cilindro en función de r')

fig.update_traces(mode='markers+lines')
fig.show()

El gráfico nos muestra que el mínimo está entre 3.6 y 3.8. Vamos a calcular de forma precisa ese punto resolviendo la ecuación $S'\left(r\right)=0$.

$$-\frac{660}{r^2}+4\pi r=0$$
$$-660 + 4\pi r^3=0$$
$$r^3= \frac{600}{4\pi}$$
$$r=\left(\frac{600}{4\pi}\right)^{\frac{1}{3}}$$

r_opt = (660.0 / (4.0 * math.pi))**(1./3.)
print(f'El valor de r debe ser: {r_opt:.8f}')

Veamos ahora un ejemplo de cinemática. Supongamos que Ben corre en línea recta desde el punto A al punto B. Cuando alcanza el punto B, se da la vuelta y corre de regreso al punto B. Cuando llega de vuelta a A, se gira nuevamente y regresa al punto B.

La posición $s$ de Ben, medida desde el punto A en cualquier instante de tiempo $t$ (donde $t \in\left[0,4\right]$ está dada por:

$$s\left(t\right)=t^3-6t^2+9t$$

El gráfico del desplazamiento en función del tiempo es el siguiente:

def s(t): return t**3 - 6*t**2 + 9*t


data = [(t * .25, s(t * .25)) for t in range(17)]
df = pd.DataFrame(data, columns=['t', 'S(t)'])
fig = px.line(
    df,
    x='t',
    y=['S(t)'],
    title=f'Desplazamiento de Ben en función de t')

fig.update_traces(mode='markers+lines')
fig.show()

La velocidad de Ben está dada por $s'\left(t\right)=3t^2-12t+9$. El gráfico de la velocidad es:

def sp(t): return 3*t**2 - 12*t + 9


data = [(t * .25, sp(t * .25)) for t in range(17)]
df = pd.DataFrame(data, columns=['t', "S'(t)"])
fig = px.line(
    df,
    x='t',
    y=["S'(t)"],
    title=f'Velocidad de Ben en función de t')

fig.update_traces(mode='markers+lines')
fig.show()

- Para $t\left[0,1\right]$ Ben está yendo hacia B.
- Para $t\in\left(1,3\right)$ Ben está volviendo hacia A, por eso la velocidad tiene signo negativo.
- Finalmente, para $t\in\left[3,4\right]$ Ben está yendo nuevamente hacia B, por eso la velocidad vuelve a ser positiva.
- Los momentos en los que la velocidad de Ben es $=0$ son los instantes en los que Ben se devuelve, primero de B a A y luego de A a B.