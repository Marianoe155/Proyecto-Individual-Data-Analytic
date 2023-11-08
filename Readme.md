<p align=center><img src=https://d31uz8lwfmyn8g.cloudfront.net/Assets/logo-henry-white-lg.png><p>

# <h1 align=center> **PROYECTO INDIVIDUAL N°2** </h1>

<p align="center">
  <img src="imagenes\2acd894fafe24336a4a319ad07b34f1f (2).png" alt="Privacidad" width="50%"/>
</p>

# <h1 align=center> **Introducción** </h1>

En este segundo proyecto individual, nos enfrentamos al desafío de realizar un análisis exhaustivo de una diversidad de conjuntos de datos que abarcan información integral sobre telecomunicaciones. Exploraremos datos relacionados con la conectividad, velocidad de Internet, tecnologías emergentes y su impacto en diferentes regiones. A medida que nos sumergimos en este análisis, buscaremos descubrir tendencias, patrones y relaciones significativas en los datos, con el objetivo de extraer conocimientos valiosos que puedan guiar decisiones estratégicas y mejorar la calidad de los servicios de telecomunicaciones. Este proyecto promete brindar una comprensión profunda de un sector vital en constante evolución y contribuir al desarrollo de soluciones innovadoras en el ámbito de las telecomunicaciones.

# <h1 align=center> **Desarrollo del Proyecto**</h1>

## **Análisis Exploratorio de Datos** (EDA)

Para dar inicio a nuestro [análisis exploratorio de datos (EDA)](EDA.ipynb), es fundamental comenzar por la base sólida de la limpieza y validación preliminar de los datos. Esta etapa es esencial para garantizar la integridad y confiabilidad de nuestra información antes de sumergirnos en la formulación de preguntas, la obtención de conclusiones y la toma de decisiones basadas en datos.

En esta fase inicial, nuestro objetivo principal es identificar y abordar cualquier valor faltante, incorrecto o atípico que pueda comprometer la calidad de los datos. La calidad de los datos es un factor crítico en cualquier análisis, ya que los resultados y las conclusiones dependerán en gran medida de la calidad de los datos subyacentes.

Para la detección de valores atípicos, hemos empleado una función específica denominada "Z score," la cual se encuentra implementada en un archivo de código llamado [funcion.py](funcion.py). El Z score es una métrica estadística que evalúa la distancia entre un valor de datos y la media de una distribución en términos de desviaciones estándar. Valores Z score altos o bajos pueden indicar cuán lejos está un punto de datos de la media y si se considera un valor atípico.

<p align="center">
  <img src="imagenes\Captura.PNG" alt="Privacidad"  width="50%"/>
</p>

Una vez que hayamos completado la limpieza y validación preliminar de los datos, estaremos en una posición sólida para explorar los patrones, relaciones y tendencias presentes en los datos, lo que nos permitirá obtener una comprensión más profunda y significativa de nuestro conjunto de datos. A través del EDA, podremos formular preguntas relevantes, realizar análisis estadísticos y visuales, y llegar a conclusiones que respalden la toma de decisiones informadas.

## Focos de Análisis

Luego de una elaborada lectura para formar una idea respecto a factores de importancia, enfocamos el estudio en ciertas premisas:

+ **Número total de accesos al servicio de Internet fijo por banda ancha.**

<p align="center">
  <img src="imagenes\Banda ancha por año.PNG" alt="Privacidad"  width="70%"/>
</p>

Lo que se puede observar es un constante crecimiento en el acceso a Internet fijo a través de banda ancha a lo largo de los años, a nivel nacional.
Este desarrollo podría ser un indicador de una mayor infraestructura de telecomunicaciones y una mayor conciencia sobre la importancia de la conectividad de banda ancha, lo que, en última instancia, podría contribuir al progreso y desarrollo tecnológico en el país.

+ **Número de accesos al servicio de Internet fijo por tipo de tecnología.**

<p align="center">
  <img src="imagenes\Tipo de tecnología.PNG" alt="Privacidad"  width="70%"/>
</p>

Es evidente a simple vista cómo las nuevas tecnologías, como la "Fibra óptica", muestran un notable potencial de crecimiento en comparación con las tecnologías existentes. Este ascenso en la adopción de la fibra óptica puede atribuirse a su capacidad superior de transmisión de datos y mayor velocidad, lo que la convierte en una opción atractiva para los usuarios que buscan una conectividad de alta calidad.

+ **Número de accesos al servicio de Internet fijo por cada 100 hogares por provincia.**

<p align="center">
  <img src="imagenes\100 hogares por provincia.PNG" alt="Privacidad"  width="70%"/>
</p>

En este gráfico, es evidente que, a pesar de una inversión limitada en Tierra del Fuego, esta provincia se sitúa en la segunda posición en términos de acceso a Internet por cada 100 hogares. Estos datos subrayan cómo una gestión efectiva de los recursos puede llevar a resultados notablemente positivos en el ámbito de la conectividad.

+ **Ingresos trimestrales por la prestación del servicio de Internet fijo.**

<p align="center">
  <img src="imagenes\Ingresos por año.PNG" alt="Privacidad"  width="70%"/>
</p>

Observamos que nuestros ingresos por la prestación de servicios se mantienen de manera estable y positiva a lo largo del tiempo, sin mostrar tendencias significativas de cambio. Esta consistencia en los ingresos refleja la confiabilidad y la demanda constante de nuestros servicios, lo que puede ser un indicativo de una base de clientes sólida y una gestión efectiva de la calidad de los servicios ofrecidos.

## Conclusión

Después de un análisis completo, hemos llegado a conclusiones significativas. Observamos que nos hemos posicionado de manera estable y efectiva en el mercado. Para mantener este posicionamiento, hemos definido KPIs que reflejan un crecimiento constante en el acceso a hogares y un objetivo de crecimiento del 2% trimestral.

Para continuar en el sector de las telecomunicaciones y mejorar nuestra calidad de servicio, es vital invertir en tecnologías de vanguardia, con un enfoque particular en la "Fibra óptica". Hemos establecido un KPI que busca lograr un crecimiento del 25% anual en un período de 15 años para alcanzar este objetivo de inversión en infraestructura.

En resumen, nuestras conclusiones indican que estamos comprometidos con un crecimiento sostenible y la mejora continua de nuestros servicios, respaldados por indicadores clave de desempeño que guiarán nuestro progreso en el mercado de las telecomunicaciones.

+ **Podras encontrar más desarrollo de la explicación de nuestros KPI´s [aquí](KPI.ipynb)**

## Fuentes de datos principales

Algunas de las fuentes consultadas para nuestro análisis provinieron de recursos en línea. Puedes encontrar información detallada sobre las fuentes y sus respectivos sitios web a continuación:

+ [Enacom](https://datosabiertos.enacom.gob.ar/dashboards/20000/acceso-a-internet/)

También puede encontrar las fuentes que decidimos utilizar en [datasets](datasets)

## Autor

+ Mariano Emanuel Baigorria
+ [GitHub](https://github.com/Marianoe155)
+ [Linkedin](https://www.linkedin.com/in/mariano-baigorria-b85004282/)
