# Cálculo Integral

Podemos encontrar la velocidad de un objeto en movimiento calculando la derivada de la función que mide su desplazamiento. Consideremos ahora el proceso inverso, podemos encontrar la función de desplazamiento de un objeto en movimiento cuando conocemos su velocidad, calculando la *antiderivada*, aquella función cuya derivada es el desplazamiento.

El proceso de encontrar la *antiderivada* de una función se llama **integración**.

## Antiderivadas y la Integral Indefinida

La función $F$ se dice la *antiderivada* de $f$ si $F'\left(x\right)=f\left(x\right)$.

**Antiderivada de $x^n$**

La *antiderivada* de $f\left(x\right)=x^n$ está dada por $F\left(x\right)=\frac{1}{n+1}x^{n+1}+C$, donde $C\in\mathbb{R}$.

Esto es fácil de comprobar si recordamos la regla para calcular la derivada $F$. Esta es $F'\left(x\right)=\frac{n+1}{n+1}x^n$ (se baja el exponente y el nuevo exponente es igual al viejo menos 1). Recordar además que la derivada de una función constante es igual a 0 (esto es muy intuituitivo porque una función constante tiene siempre un gradiente igual a 0).

**Ejemplo**

Calculemos la antiderivada ($F\left(x\right)$ de:

- $f\left(x\right)=x^8$ ---> $F\left(x\right)=\frac{1}{9}x^9+C$


- $f\left(x\right)=\frac{1}{x^3}$ ---> $f\left(x\right)=x^{-3}$ ---> $F\left(x\right)=-\frac{1}{2}x^{-2}+C$


- $f\left(x\right)=\sqrt[5]{x^3}$  --->  $f\left(x\right)=x^{\frac{3}{5}}$  ---> $F\left(x\right)=\frac{5}{8}x^{\frac{8}{5}}+C$

La **antidiferenciación** (encontrar la antiderivada) también se conoce como **integración indefinida** y se denota con el símbolo de integral:

$$\int dx$$

Por ejemplo:

$$\int x^8 dx = \frac{1}{9}x^9+C$$

```{admonition} Nomenclatura
:class: tip
Si $F'\left(x\right)=f\left(x\right)$ se escribe $\int f\left(x\right)dx=F\left(x\right)+C$.
La expresión $\int f\left(x\right)dx$ se conoce como la integral indefinida.
$\int f\left(x\right)dx$ se lee como *la integral de $f$ con respecto a $x$*.
```

```{admonition} La Integral Indefinida es una Operación Lineal
:class: tip
$$\int \left[\alpha f\left(x\right)+\beta g\left(x\right)\right]dx=\alpha\int f\left(x\right)dx+\beta\int g\left(x\right)dx$$

donde $\alpha,\beta\in\mathbb{R}$.
```