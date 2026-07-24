UNIVERSIDAD DE SANTIAGO DE CHILE

FACULTAD DE INGENIERÍA

Departamento de Ingeniería Informática

WealthQuest: un juego serio para apoyar la educación financiera

aplicando el framework Blended Games

Jonathan Ignacio Soto Aguilar

Profesor Guía:

Roberto González Ibáñez

Profesor Co-Guia:

                         Karina Chandia

Tesis para optar al título de Ingeniero de

Ejecución en Computación e Informática

Santiago - Chile

2024

Este documento ha utilizado modelos de lenguaje GPT de OpenAI para asistencia en revisión
de ortografía y gramática.

RESUMEN

La  alfabetización  financiera  es  parte  esencial  de  la  educación  que  deben  recibir
todas  las personas actualmente, dado que la comprensión de las finanzas personales impacta
directamente  en  el  bienestar  individual  y  colectivo.  Este  trabajo  aborda  la  problemática  de  la
baja  alfabetización  financiera  en  Chile,  destacando  la  deficiente  comprensión  de  conceptos
financieros básicos. Ante esta situación, se vuelve importante realizar los esfuerzos necesarios
para  mejorar  competencias  en  este  dominio.  En  este  contexto,  se  propone  el  juego  serio
WealthQuest,  el  cual  se  diseña  con  propósitos  educativos  más  allá  del  entretenimiento  y
desarrolla  adoptando  una  metodología  mixta  inspirada  en  Rapid  Application  Development
(RAD)  y  Scrum,  aplicando  adicionalmente  el  framework  Blended  Games  (bGames),  con  el
objetivo de ofrecer una alternativa formativa en el ámbito de la educación financiera, orientada
al  aprendizaje  de  conceptos  básicos  de  finanzas  personales  de  una  manera  entretenida  y
lúdica.

Palabras  clave:  alfabetización  financiera,   Blended  Games,  educación

financiera,  juego serio.

ⅰ

AGRADECIMIENTOS

Quiero expresar mi más profundo agradecimiento a diversas personas que me han

apoyado a lo largo de este proceso.

En  primer  lugar,  agradezco  a  mis  profesores  por  todo  aquel  conocimiento  y
enseñanzas  que  me  entregaron,  con  mención  a  mis  profesores  guías  Roberto  Gonzalez  y
Karina Chandia por su apoyo durante la etapa final de mi formación.

A  mis  amigos,  por  su  compañía  y  aliento  durante  el  proceso.  Su  apoyo  y
disposición  para  pruebas  de  software  me  han  sido  de  suma  importancia  para  mejorar  y
perfeccionar este proyecto.

Finalmente, a mi madre, cuyo amor, sacrificio y dedicación han sido la base de mis

valores y formación. Siendo la inspiración para superar los obstáculos durante este camino.

A todos ellos, les expreso mi más sincero agradecimiento.

ⅱ

TABLA DE CONTENIDOS

CAPÍTULO 1. INTRODUCCIÓN

1.1. ANTECEDENTES Y MOTIVACIÓN
1.2. PLANTEAMIENTO DEL PROBLEMA
1.3. SOLUCIÓN PROPUESTA

1.3.1. Característica general de la solución
1.3.2. Evaluación de la solución
1.3.3. Propósito de la solución

1.4. OBJETIVOS Y ALCANCES DEL PROYECTO

1.4.1. Objetivo general
1.4.2. Objetivos específicos
1.4.3. Alcances

1.5.  METODOLOGÍAS Y HERRAMIENTAS UTILIZADAS

1.5.1. Metodología
1.5.2. Herramientas de desarrollo
1.6. ORGANIZACIÓN DEL DOCUMENTO

CAPÍTULO 2. MARCO TEÓRICO

2.1. MARCO CONCEPTUAL

2.1.1. Blended Games (bGames)
2.1.2. Unity
2.1.3. Juego serio
2.1.4. Alfabetización financiera

2.2 ESTADO DEL ARTE

2.2.1. La educación financiera nacional
2.2.2. La educación financiera internacional
2.2.3. La educación financiera desde los juegos

2.3. RESUMEN

CAPÍTULO 3. DISEÑO DEL VIDEOJUEGO (GDD)

3.1 OBJETIVOS DEL JUEGO
3.2 MECÁNICAS DEL JUEGO
2.2.1. Reglas generales
2.2.2. Sistema de contenidos
2.2.3. Sistema de progresión
2.2.4. Interacción del jugador
2.2.5. Economía del juego
2.2.6. Sistema de puntaje

3.3 DISEÑO DE MUNDO
3.4 INTERFAZ DE USUARIO (UI)
3.5 CONTROL Y ACCESIBILIDAD

1
1
2
3
3
6
6
6
6
7
7
8
8
9
11
12
12
12
13
14
14
14
15
17
18
20
21
21
21
21
22
22
23
24
25
26
26
28

ⅲ

3.6 ESTILO ARTÍSTICO Y SONIDO
3.7 MODOS DE JUEGO
3.8 ADMINISTRACIÓN DE PARTIDAS Y GUARDADO
3.9 RESUMEN
CAPÍTULO 4. ANÁLISIS
4.1. REQUISITOS

4.1.1. Requisitos funcionales
4.1.2. Requisitos no funcionales

4.2. PROTOTIPADO

4.2.1. Prototipo 1: escena tablero
4.2.2. Prototipo 2: sistema de turnos multijugador local
4.2.3. Prototipo 3: sistema de casillas y preguntas
4.2.4. Prototipo 4: menú de inicio
4.2.5. Prototipo 5: sistema de guardado
4.2.6. Prototipo 6: historial de partidas
4.2.7. Prototipo 7: integración de bGames
4.2.8. Prototipo 8: multijugador en línea
4.2.9. Prototipo 9: sensor blended games

4.3. RESUMEN

CAPÍTULO 5. DISEÑO E IMPLEMENTACIÓN

5.1. ARQUITECTURA

5.1.1. Arquitectura de software con Blended Games
5.1.2. Vista de desarrollo: organización de recursos
5.1.3. Vista lógica: diagrama de clases
5.1.4. Vista de proceso: diagrama de secuencia
5.1.5. Vista física: diagrama de despliegue
5.1.6. Vista de escenarios: casos de uso

5.2. IMPLEMENTACIÓN

5.2.1. Flujo general del juego
5.2.2. Administración de partidas
5.2.3. Obtención de puntos de bGames
5.2.4. Conexión con bGames y consumo de puntos
5.2.5. Multijugador en línea
5.2.6. Creación y administración de contenidos
5.2.7. Distribución de contenidos
5.2.8. Contenido inicial
5.2.9. Publicación del videojuego

5.4. RESUMEN

CAPÍTULO 6. EVALUACIÓN

6.1. PRUEBAS DE SOFTWARE
6.1.1. Ambientes de prueba

28
28
29
29
30
30
31
33
33
34
36
37
40
42
44
45
47
49
52
55
55
55
56
59
59
60
61
63
63
66
68
70
73
76
80
81
83
85
86
86
86

ⅳ

6.1.2. Pruebas de compatibilidad
6.1.3. Pruebas de rendimiento
6.2. EXPERIENCIA DE USUARIO

6.2.1. Jugabilidad
6.2.2. Mecánicas
6.2.3. Usabilidad
6.2.4. Preguntas libres

6.3. PRUEBAS DE ACEPTACIÓN
6.4. RESUMEN

CAPÍTULO 7. CONCLUSIONES

7.1. OBJETIVOS

7.1.1. Objetivos Específicos
7.1.2. Objetivo General

7.2. IMPLICACIONES
7.3. ALCANCES Y LIMITACIONES
7.4. TRABAJO FUTURO

7.4.1. Compatibilidad a otras plataformas
7.4.2. Restauración del módulo cloud bGames
7.4.3. Estudio de impacto
7.5. REFLEXIONES FINALES

GLOSARIO
REFERENCIAS BIBLIOGRÁFICAS
ANEXO A. CARTA DE PATROCINIO
APÉNDICE A. PREGUNTAS MÓDULO FINANCIERO INICIAL
APÉNDICE B. DETALLES DE IMPLEMENTACIÓN

Apéndice B.1 Interfaces del videojuego
Apéndice B.2 Sistema de guardado

APÉNDICE C. DETALLES DE EVALUACIÓN

Apéndice C.1 Detalles de pruebas de compatibilidad
Apéndice C.2 Preguntas evaluación HEP
Apéndice C.3 Detalles de pruebas de aceptación

APÉNDICE D. USO DE LENGUAJE GPT

Apéndice D.1. Prompt para revisión de ortografía y gramática
Apéndice D.2. Prompt para generación de imágenes para videojuego

APÉNDICE E. ARCHIVO DE DESPLIEGUE DE BGAMES
APÉNDICE F. RECURSOS UTILIZADOS

87
88
91
92
93
94
95
96
98
99
99
99
100
101
101
102
102
102
102
103
104
105
107
108
136
136
142
146
146
147
151
159
159
160
161
165

ⅴ

ÍNDICE DE TABLAS

Tabla 1.1: Características generales del juego

Tabla 2.1: Sistematización del estado del arte.
Tabla 2.2: Finanzas en videojuegos tradicionales.

Tabla 4.1: Requisitos funcionales - Parte I.
Tabla 4.2: Requisitos funcionales - Parte II.
Tabla 4.3: Requisitos no funcionales.
Tabla 4.4: Resumen del prototipo escena tablero.
Tabla 4.5: Resumen del prototipo sistema de turnos multijugador local.
Tabla 4.6: Resumen del prototipo sistema de casillas y preguntas.
Tabla 4.7: Resumen del prototipo menú de inicio.
Tabla 4.8: Resumen del prototipo perfil de usuario.
Tabla 4.9: Resumen del prototipo historial de partidas.
Tabla 4.10: Resumen del prototipo de integración de bGames.
Tabla 4.11: Resumen del prototipo multijugador en línea.
Tabla 4.12: Resumen del prototipo de sensor blended games.
Tabla 4.13: Resumen de prototipos y requerimientos funcionales abarcados.
Tabla 4.14: Resumen de prototipos y requerimientos no funcionales abarcados.

Tabla 5.1: Estructura de pregunta.

Tabla 6.1: Especificaciones técnicas del ordenador principal.
Tabla 6.2: Especificaciones técnicas del ordenador secundario.
Tabla 6.3: Resultados de las pruebas de compatibilidad.
Tabla 6.4: Resultados de las pruebas de rendimiento.
Tabla 6.5: Rango de aceptación de pruebas.
Tabla 6.6: Resumen de las pruebas de aceptación - Parte I.
Tabla 6.7: Resumen de las pruebas de aceptación - Parte II.

Tabla A.1: Pregunta para el banco inicial Q01.
Tabla A.2: Pregunta para el banco inicial Q02.
Tabla A.3: Pregunta para el banco inicial Q03.
Tabla A.4: Pregunta para el banco inicial Q04.
Tabla A.5: Pregunta para el banco inicial Q05.

5

15
19

31
32
33
34
36
38
41
43
45
47
49
51
54
55

78

87
88
88
90
97
97
98

109
109
110
110
111

ⅵ

Tabla A.6: Pregunta para el banco inicial Q06.
Tabla A.7: Pregunta para el banco inicial Q07.
Tabla A.8: Pregunta para el banco inicial Q08.
Tabla A.9: Pregunta para el banco inicial Q09.
Tabla A.10: Pregunta para el banco inicial Q10.
Tabla A.11: Pregunta para el banco inicial Q11.
Tabla A.12: Pregunta para el banco inicial Q12.
Tabla A.13: Pregunta para el banco inicial Q13
Tabla A.14: Pregunta para el banco inicial Q14.
Tabla A.15: Pregunta para el banco inicial Q15.
Tabla A.16: Pregunta para el banco inicial Q16.
Tabla A.17: Pregunta para el banco inicial Q17.
Tabla A.18: Pregunta para el banco inicial Q18.
Tabla A.19: Pregunta para el banco inicial Q19.
Tabla A.18: Pregunta para el banco inicial Q20.
Tabla A.21: Pregunta para el banco inicial Q21.
Tabla A.22: Pregunta para el banco inicial Q22.
Tabla A.23: Pregunta para el banco inicial Q23.
Tabla A.24: Pregunta para el banco inicial Q24.
Tabla A.25: Pregunta para el banco inicial Q25.
Tabla A.26: Pregunta para el banco inicial Q26.
Tabla A.27: Pregunta para el banco inicial Q27.
Tabla A.28: Pregunta para el banco inicial Q28.
Tabla A.29: Pregunta para el banco inicial Q29.
Tabla A.30: Pregunta para el banco inicial Q30.
Tabla A.31: Pregunta para el banco inicial Q31.
Tabla A.32: Pregunta para el banco inicial Q32.
Tabla A.33: Pregunta para el banco inicial Q33.
Tabla A.34: Pregunta para el banco inicial Q34.
Tabla A.35: Pregunta para el banco inicial Q35.
Tabla A.36: Pregunta para el banco inicial Q36.
Tabla A.37: Pregunta para el banco inicial Q37.
Tabla A.38: Pregunta para el banco inicial Q38.
Tabla A.39: Pregunta para el banco inicial Q39.
Tabla A.40: Pregunta para el banco inicial Q40.
Tabla A.41: Pregunta para el banco inicial Q41.
Tabla A.42: Pregunta para el banco inicial Q42.
Tabla A.43: Pregunta para el banco inicial Q43.

111
112
112
113
113
114
114
115
115
116
116
117
117
118
118
119
119
120
120
121
121
122
122
123
123
124
124
125
125
126
126
127
127
128
128
129
129
130

ⅶ

Tabla A.44: Pregunta para el banco inicial Q44.
Tabla A.45: Pregunta para el banco inicial Q45.
Tabla A.46: Pregunta para el banco inicial Q46.
Tabla A.47: Pregunta para el banco inicial Q47.
Tabla A.48: Pregunta para el banco inicial Q48.
Tabla A.49: Pregunta para el banco inicial Q49.
Tabla A.50: Pregunta para el banco inicial Q50.
Tabla A.51: Pregunta para el banco inicial Q51.
Tabla A.52: Pregunta para el banco inicial Q52.
Tabla A.53: Pregunta para el banco inicial Q53.
Tabla A.54: Pregunta para el banco inicial Q54.
Tabla A.55: Pregunta para el banco inicial Q55.
Tabla A.56: Pregunta para el banco inicial Q56.

Tabla C.1: Prueba de aceptación PA-01.
Tabla C.2: Prueba de aceptación PA-02.
Tabla C.3: Prueba de aceptación PA-03.
Tabla C.4: Prueba de aceptación PA-04.
Tabla C.5: Prueba de aceptación PA-05.
Tabla C.6: Prueba de aceptación PA-06.
Tabla C.7: Prueba de aceptación PA-07.
Tabla C.8: Prueba de aceptación PA-06.
Tabla C.9: Prueba de aceptación PA-09.

Tabla F.1: Recursos utilizados durante el desarrollo del proyecto - Parte I.
Tabla F.2: Recursos utilizados durante el desarrollo del proyecto - Parte II.

130
131
131
132
132
133
133
134
134
135
135
136
136

152
153
153
154
155
156
157
158
159

166
167

ⅷ

ÍNDICE DE ILUSTRACIONES

Figura 2.1: Diagrama de contexto del módulo cloud de bGames.
Figura 2.2: Iniciativas de educación financiera en la banca.
Figura 2.3: Sitio oficial de CMF Educa.
Figura 2.4: Sitio oficial de My Classroom Economy.

Figura 3.1: Diagrama navegación interfaces.
Figura 3.2: Paleta de colores.

Figura 4.1: Tablero de juego básico.
Figura 4.2: Objeto dado.
Figura 4.3: Objeto prefabricado del jugador.
Figura 4.4: Casilla de inversión.
Figura 4.5: Sistema de preguntas.
Figura 4.6: Menú inicial.
Figura 4.7: Popup reanudación de partida.
Figura 4.8: Registro de partidas finalizadas.
Figura 4.9: Conexión con bGames.
Figura 4.10: Popup de canjeo de puntos bGames.
Figura 4.11: Arquitectura host-cliente con unity relay.
Figura 4.12: Objetivo en Fintual.
Figura 4.13: Aplicación de escritorio para sensor de Fintual.

Figura 5.1: Diagrama conceptual de la solución.
Figura 5.2: Diagrama de recursos del proyecto.
Figura 5.3: Diagrama de organización de recursos del proyecto.
Figura 5.4: Diagrama clases de los objetos principales en una partida.
Figura 5.5: Diagrama de secuencia primera conexión.
Figura 5.6: Diagrama de despliegue.
Figura 5.7: Diagrama de caso de uso durante la partida.
Figura 5.8: Diagrama de caso de uso en menú principal.
Figura 5.9: Diagrama de caso de uso en aplicación para sensor Fintual.
Figura 5.10: Diagrama de turno del jugador.
Figura 5.11: Interfaz de pregunta.
Figura 5.12: Interfaz del dado.
Figura 5.13: Interfaz de selección de tarjeta.

13
16
17
18

27
28

35
35
37
39
40
42
44
46
47
48
50
52
53

56
58
59
60
61
62
63
63
64
65
66
66
67

ⅸ

Figura 5.14: Interfaz perfil.
Figura 5.15: Sala en línea.
Figura 5.16: Partida en línea.
Figura 5.17: Interfaz de creación de contenido.
Figura 5.18: Interfaz de contenidos.
Figura 5.19: Página de WealthQuest en itch.io.

Figura 6.1: Resultados de rendimiento de uso de recursos.
Figura 6.2: Resultados de rendimiento general.
Figura 6.3: Resultados de encuesta jugabilidad.
Figura 6.4: Resultados de encuesta mecánicas.
Figura 6.5: Resultados de encuesta usabilidad.
Figura 6.6: Resultados de las pruebas de aceptación.

Figura B.1: Interfaz de inicio de sesión.
Figura B.2: Interfaz de registro.
Figura B.3: Interfaz de recuperación de contraseña.
Figura B.4: Interfaz de inicio..
Figura B.5: Interfaz de contenido.
Figura B.6: Interfaz de crear contenido.
Figura B.7: Interfaz de perfil de usuario.
Figura B.8: Interfaz de opciones.
Figura B.9: Interfaz de modos.
Figura B.10: Interfaz de modos multijugador local.
Figura B.11: Interfaz de modos multijugador en línea.
Figura B.12: Interfaz de sala en línea.

Figura C.1: Interfaz del videojuego en Linux Ubuntu.
Figura C.2: Interfaz del videojuego en Windows 11.
Figura C.3: Preguntas evaluación HEP de jugabilidad.
Figura C.4: Preguntas evaluación HEP de mecánicas.
Figura C.5: Preguntas evaluación HEP de usabilidad.
Figura C.6: Preguntas evaluación HEP libres.

Figura D.1: Sprite para tarjeta del videojuego.

69
76
77
79
81
86

91
91
93
94
95
99

137
137
138
138
139
139
140
140
141
141
142
142

147
147
148
149
150
151

161

ⅹ

ÍNDICE DE CÓDIGOS

Código 5.1: Funcionalidad de encriptado.
Código 5.2: Cálculo de porcentaje de cumpliento de meta mensual.
Código 5.3: Direcciones apis y diccionario de consultas url.
Código 5.4: Login perfil bGames.
Código 5.5: Consumo de puntos bGames.
Código 5.6: Crear sala en línea.
Código 5.7: Unirse a sala en línea.
Código 5.8: Contenido en formato .json.

Código B.1: Archivo de guardado de partida en curso sin encriptado  - Parte I.
Código B.2: Archivo de guardado de partida en curso sin encriptado  - Parte II.
Código B.3: Archivo de guardado de partida en curso sin encriptado  - Parte III.
Código B.3: Archivo de guardado de partida finalizada sin encriptado.

Código E.1: Despliegue local del entorno bGames para WealthQuest - Parte I.
Código E.2: Despliegue local del entorno bGames para WealthQuest - Parte II.
Código E.3: Despliegue local del entorno bGames para WealthQuest - Parte III.
Código E.4: Despliegue local del entorno bGames para WealthQuest - Parte IV.

68
71
72
73
74
75
76
80

143
144
145
146

162
163
164
165

ⅹⅰ

ÍNDICE DE ECUACIONES

Ecuación 3.1: Fórmula de cálculo del puntaje final
Ecuación 3.2: Fórmula de cálculo de la evaluación

25
25

xiⅰ

CAPÍTULO 1. INTRODUCCIÓN

En este capítulo se introduce la problemática abordada por el proyecto, incluyendo

los antecedentes y motivación que condujeron a su desarrollo. Se define el problema abordado,

junto  con  una  solución  propuesta,  detallando  sus  características,  objetivos,  alcances  y

metodologías para su implementación.

1.1. ANTECEDENTES Y MOTIVACIÓN

A  pesar  de  la  alta  bancarización  en  Chile,  donde  el  98%  de  la  población  adulta

tiene  acceso  a  algún  instrumento  financiero  (SBIF,  2016),  aún  persisten  deficiencias  en  las

habilidades necesarias para gestionarlos adecuadamente. Según los resultados de la Encuesta

de  Capacidades  Financieras  realizada  por  la  Comisión  para  el  Mercado  Financiero  y  la

Corporación  Andina  de  Fomento  (CMF-CAF),  casi  la  mitad  de  la  población  con  educación

superior  carece  de  los  conocimientos  básicos  necesarios  para  acceder  y  utilizar  de  manera

apropiada  los  productos  y  servicios  financieros  disponibles  en  el  mercado  (CMF,  2023).  Esta

situación refleja la facilidad con la que se puede acceder a productos financieros, pero también

revela  una  brecha  existente  en  las  capacidades  necesarias  para  utilizar  dichos  productos  de

manera  adecuada.  La  razón  de  esta  brecha  se  puede  atribuir  a  tres factores definidos por la

Organización para la Cooperación y el Desarrollo Económico (OCDE) en su kit de herramientas

International  Network  on  Financial  Education  (INFE),  el  cual  se  utiliza  en  las encuestas de la

CMF-CAF.  En  primer  lugar,  el  conocimiento,  necesario  para  que  los  consumidores  puedan

comparar productos y servicios y tomar decisiones financieras apropiadas y bien informadas. En

segundo lugar, el comportamiento, determinante en el bienestar financiero de las personas, en

aspectos  como  la  planificación  y  el  ahorro,  la  precaución  al  adquirir  productos  y  servicios

financieros, y el manejo del dinero. Finalmente, las actitudes, las cuales influyen en la decisión

de actuar o no desde el punto de vista financiero (CMF, 2023).

El  conocimiento  financiero  es  importante  para  comprender  y  manejar  productos

financieros.  La  OCDE  define  como  parte  del conocimiento necesario: el valor del dinero en el

tiempo,  la  inflación,  la  tasa  de  interés,  el  cálculo  de  interés  simple  e  interés  compuesto,  y el

riesgo y diversificación del riesgo (CMF, 2023). Estos conocimientos son los básicos necesarios

para desenvolverse sin mayores complicaciones en el campo financiero. En este aspecto, en el

1

año 2023, según las encuestas de la CMF-CAF, en una escala del 0 al 7, el promedio nacional

de  la  población  adquiere  un  puntaje  de  4,32,  siendo  inferior  al  promedio  de  los  países  de la

OCDE (4,6) y de Latinoamérica (4,4) (CMF, 2023).

El comportamiento financiero es determinante para el bienestar de las personas y

se  refleja  principalmente  a  través  de  tres  dimensiones:  (1)  el  ahorro y la planificación a largo

plazo,  (2)  el  cuidado  al  adquirir  productos  y  servicios  financieros,  y  (3)  el  manejo  del  dinero

(CMF,  2023).  En  este  aspecto,  el  puntaje  promedio  del  comportamiento  financiero  a  nivel

nacional obtenido en 2023 fue de 4,9, ubicándose por debajo del promedio de la OCDE (5,3) y

del obtenido en el año 2016 (6,1), pero por encima del de Latinoamérica (4,7) (CMF, 2023).

En  cuanto a las actitudes financieras, estas reflejan la forma en que las personas

enfrentan  la  vida.  Aquellos que muestran una actitud más orientada hacia el presente podrían

enfrentar dificultades financieras en el futuro al no preocuparse por las posibles consecuencias.

Por  otro  lado,  aquellos  que  muestran  actitudes  más  positivas  hacia  el largo plazo y el ahorro

tienden  a  desarrollar  una  situación  financiera  más  estable  (CMF, 2023). En el año 2023, esta

capacidad se tradujo en un puntaje de 3,01 a nivel nacional, similar a la medición de 2016, pero

ligeramente inferior al promedio de la OCDE y de Latinoamérica (3,1) (CMF, 2023).

A  pesar  de  que  el  Ministerio de Educación ha realizado avances en incorporar la

educación  financiera  en  los  currículums  educacionales,  los  datos  expuestos  anteriormente

evidencian  una  situación  desfavorable en términos financieros dentro del país, lo que muestra

que  el  problema  aún  se  mantiene.  Por  lo  tanto,  resulta  importante  realizar  los  esfuerzos

necesarios para mejorar en este campo.

1.2. PLANTEAMIENTO DEL PROBLEMA

A  partir  de  la  información  presentada  anteriormente,  se  desprende  una situación

preocupante  en  el  ámbito  financiero  de  la  población.  La  existencia  de  bajos  niveles  de

alfabetismo financiero puede acarrear costos importantes para el bienestar de las personas, ya

que  puede  conducir  a  la  toma  de  decisiones  desfavorables,  como  adquirir  créditos  con  altas

tasas de interés o no ahorrar lo suficiente para la jubilación (Álvarez & Ruiz-Tagle, 2016).

A pesar de las múltiples iniciativas surgidas en los últimos años, todavía existe una

brecha importante por superar para alcanzar el nivel financiero de otros países. Según el INFE,

en el año 2023, la alfabetización financiera nacional alcanzó un puntaje de 12,2, superando así

el umbral de los 12 puntos y equivalente al 58% del puntaje máximo (21 puntos). Sin embargo,

2

este puntaje resultó ser inferior al promedio de los países de la OCDE (13) y también menor que

el obtenido en 2016 (13,1) (CMF, 2023).

Esta  disminución  en  el  puntaje  sugiere  que  la nueva generación de jóvenes está

mostrando  menos  interés  en  su  educación  financiera, lo que indica que la problemática sigue

siendo relevante en la población. En este sentido, surge la pregunta: ¿De qué manera se puede

apoyar el desarrollo de la alfabetización financiera en los jóvenes?

1.3. SOLUCIÓN PROPUESTA

Dada  la  magnitud  del  problema  financiero identificado, se propone el aprendizaje

mediante  juegos  como  el  enfoque  adecuado  para  abordarlo,  debido  a  su  eficacia  y

sostenibilidad  a  largo  plazo.  A  pesar  de  que  el  desarrollo  de  un  videojuego  requiere  una

inversión inicial considerable, su mantenimiento resulta mucho menos exigente en comparación

con enfoques más tradicionales como los programas educativos. Además, los videojuegos son

considerablemente más atractivos en comparación con propuestas como los portales web, que

dependen en gran medida de la motivación y autodisciplina de los usuarios.

De  acuerdo  con  un  estudio  elaborado  por  el  Instituto  Nacional  de  la  Juventud

(INJUV),  8  de  cada  10  jóvenes  afirman  haber  jugado  alguna  vez  un  juego  en  línea  o  haber

utilizado plataformas donde observan a otras personas jugar (streaming). En promedio, dedican

7  horas semanales a jugar en línea y 6 horas a ver a otros jugar en plataformas de streaming

(INJUV,  2024).  Esto  convierte  a  los  videojuegos  en  una  herramienta  idónea  para  atraer  a

jóvenes. Su inclusión en contextos educativos podría estimular significativamente su motivación

y participación, lo que a su vez mejoraría el rendimiento académico (Cerezo, 2022).

En consecuencia, se propone el desarrollo del videojuego serio WealthQuest como

una solución interactiva y lúdica para fomentar el aprendizaje de conceptos básicos de finanzas

personales. Esta propuesta permite focalizar los esfuerzos en la población joven (18-34 años),

uno  de  los  grupos  clave  para  abordar  la  problemática  financiera  en  Chile,  según  estudios

realizados en 2017 (Centro UC, 2017).

1.3.1. Característica general de la solución

La  solución  propuesta  consiste  en  un  producto  de  software  para  la  plataforma

Windows llamado WealthQuest, un juego serio de género educativo y financiero diseñado para

3

facilitar  el  aprendizaje  de  conceptos  financieros  a  través  de  una  experiencia  atractiva  y

dinámica, orientada a un amplio público, especialmente a niños y jóvenes.

WealthQuest  se  estructura  como  un  juego  de  tablero  para  hasta  4  jugadores,

inspirado  en  juegos  de  mesa  tradicionales,  donde  el  jugador  avanza  por  casillas  y  enfrenta

diferentes  escenarios  relacionados  a  las  finanzas  durante  una  cierta  cantidad  de  turno

representados  por  años,  así  hasta  llegar  al  final  simbolizado  por  la  jubilación.  Este  estilo  fue

escogido  debido  a  su  simplicidad,  lo  que  permite  una  comprensión  rápida  de  las  reglas  y

mecánicas,  facilitando  la  integración  de  conceptos  educativos  sin  abrumar  al  jugador.  Los

juegos  de  mesa  son  efectivos  para  enseñar  porque  fomentan  la  toma  de  decisiones

estratégicas  y  ofrecen  un  formato  accesible  para  personas  de  diferentes edades y niveles de

experiencia con videojuegos (Garrido-Sánchez & Crisol-Moya, 2023).

Para  captar  la  atención  del  público  objetivo, el juego implementará elementos de

diseño que incluyen gráficos atractivos, recompensas por logros, y desafíos progresivos. Estas

mecánicas  están  diseñadas  para  mantener  el  interés  del  jugador  y  reforzar  el  aprendizaje

continuo, lo que es especialmente efectivo en entornos educativos, como se señala en estudios

sobre gamificación (Borrás Gené, 2017).

El  juego contará un contenido dividido en temáticas que cubren áreas clave de la

educación  financiera,  como  conocimiento,  comportamiento  y  actitud  financiera.  Cada  tema

cuenta  con  preguntas  o  situaciones  ante  las  cuales  el  jugador  debe responder, las cuales se

vuelven  más  desafiantes  a  medida  que  el  jugador  avanza,  y  otorga  puntaje  de acuerdo a su

dificultad. Estas preguntas se enfocan en términos y conceptos fundamentales necesarios para

comprender  los  productos  y  servicios  financieros  del  mercado,  ayudando  a  los  jugadores  a

tomar decisiones informadas en su vida cotidiana.

El  sistema  de  puntos  mide  el  progreso  del  jugador  y  cuantifica  el  nivel  de

alfabetización financiera que posee el jugador en base a su puntaje final obtenido. Este sistema

permite  evaluar  el  aprendizaje  del  jugador,  analizando  cómo  las  decisiones  y  respuestas  del

jugador varían con cada partida.

4

El juego integrará además el framework bGames, desarrollado por el laboratorio de

investigación InTeracción de la Universidad de Santiago de Chile. Este framework personaliza la

experiencia de juego en función del perfil multidimensional del jugador, el cual recopila datos del

entorno  del  usuario  a  través  de  sus  sensores,  otorgándoles  un  puntaje  relacionado  el  cual

puede  ser  consumido  para  modificar  mecánicas  del  juego.  Para  el  caso  de  WealthQuest,  se

implementa uno que mide el ahorro de los usuarios, premiando a aquellos que más ahorran con

intentos  extras  para  responder  las  preguntas  que  enfrente,  lo  cual  puede  representar  una

ventaja inicial que influirá en la trayectoria del jugador a lo largo de la partida, volviendo así  la

experiencia  educativa  más  personalizada  y  premiando  este  buen  hábito  financiero.  Sin

embargo,  el  uso  de  bGames  es  opcional;  los  jugadores  pueden  disfrutar  de WealthQuest sin

necesidad  de  utilizar  este  agregado,  aunque  quienes opten por usarlo obtendrán esta ventaja

adicional.

Tabla 1.1: Características generales del juego.

Fuente: elaboración propia, 2024.

Tipo de juego

Juego serio sobre finanzas

Plataforma

Escritorio/PC (Windows)

Principales

●  Juego de tablero para hasta 4 jugadores.

características

●  Contenido  divididos  por  temáticas  y  por  niveles  que  se  vuelven

más desafiantes a medida que el jugador avanza.

●  Posibilidad de expandir contenido base y/o generar nuevos.

●  Sistema  de  puntos  para  medir  el  progreso  y  nivel  del  jugador

durante las partidas y el historial de juegos.

●  Conexión opcional con bGames para obtener ventajas por buenos

hábitos de ahorro.

5

1.3.2. Evaluación de la solución

La evaluación de la solución se realizará a través de:

●  Pruebas  de  software:  se  realizarán pruebas de rendimiento para evaluar los

tiempos  de  respuesta,  el  uso  de  CPU  y  el  uso  de  memoria  del  juego  en  la

plataforma de Windows.

●  Experiencia  de  usuario:  se  evaluará  la  jugabilidad,  las  mecánicas,  su

efectividad educativa y la usabilidad a través de pruebas de juego realizadas a

un grupo acotado de usuarios de confianza.

●  Verificación y validación: se llevarán a cabo pruebas de aceptación donde el

o  los  evaluadores  evaluarán  el  cumplimiento  de  los  requisitos  formulados.

También  se  evaluará  la  validez  del  sensor  implementado  y  de  los  conceptos

financieros abordados en el juego, esto último en base a juicio experto.

1.3.3. Propósito de la solución

El propósito a corto plazo de la solución es ofrecer una alternativa formativa en el

ámbito  de  la  educación  financiera,  orientada  al aprendizaje de conceptos básicos de finanzas

personales  de  una  manera  entretenida  y  lúdica. A mediano y largo plazo, se espera que esta

alternativa contribuya a mejorar el bienestar financiero de los usuarios, apoyándolos en la toma

de  decisiones  informadas  y  desarrollando  una  mejor  comprensión  de los conceptos y riesgos

financieros básicos.

1.4. OBJETIVOS Y ALCANCES DEL PROYECTO

A  continuación,  se  define  el  objetivo  general  del  proyecto,  detallando  aquellos

objetivos  específicos  que  guían  el  desarrollo  para  su  cumplimiento.  Además,  se  detallan  los

alcances y limitaciones del mismo.

1.4.1. Objetivo general

Desarrollar  el  videojuego  serio  WealthQuest  utilizando  el  motor  de  videojuegos

Unity y el framework Blended Games, para proporcionar una alternativa educativa interactiva y

lúdica orientada al aprendizaje de conceptos básicos de finanzas personales.

6

1.4.2. Objetivos específicos

1.  Elaborar  el  documento  de  diseño  del  juego  (GDD)  para  el  videojuego

WealthQuest,  incluyendo  las  mecánicas  afectadas  por  el  perfil  de  usuario  de

Blended Games (bGames).

2.

Implementar  el  videojuego  a  partir  del  GDD,  asegurando  la  funcionalidad

básica y la integración del framework bGames en la plataforma Windows.

3.  Desarrollar al menos un sensor para el framework de Blended Games para

alimentar  el  perfil  multidimensional  bGames  del  jugador  con datos financieros
reales.

1.4.3. Alcances

El  alcance  de  la  solución  delimita  al  desarrollo  de  un  videojuego  serio educativo

utilizando  el  motor  de  videojuegos  Unity,  orientado  específicamente  a  la  plataforma  de

Windows.  La  elección  de  Windows  se  basa  en  su  amplia  adopción  a  nivel  Global,  siendo  el

segundo sistema operativo más utilizado después de Android (StatCounter, 2024). A pesar de la

popularidad  de  Android,  la  decisión  de  enfocarse  en  Windows  responde  a  la  naturaleza  del

desarrollo y las limitaciones de tiempo del proyecto, ya que Windows proporciona un entorno de

desarrollo y testing más robusto y familiar, pues permite aprovechar herramientas de depuración

avanzadas y mayor capacidad de procesamiento. Sin embargo, al estar desarrollado con Unity,

se  deja  abierta  la  posibilidad  de  expansión  futura  a  otras  plataformas,  como  Android  (Unity,

2024).

Además,  la  solución  integrará datos financieros de los usuarios a través del perfil

de  Blended  Games,  permitiendo  personalizar  las  mecánicas  del  juego  de  acuerdo  al

comportamiento  financiero  real  de  los  jugadores.  No  obstante,  queda  fuera  del  alcance  la

medición exhaustiva de la efectividad educativa del juego, dado que las pruebas de experiencia

de usuario se realizarán a un grupo acotado por razones de tiempo. Asimismo, no se abordará

la  adopción  de  Blended  Games  en  la  comunidad  de  desarrolladores  de  videojuegos,  ni  los

objetivos  propios  del  framework,  como  mitigar  los  efectos  negativos  de  los  videojuegos  o

mejorar la salud de las personas.

7

1.5.  METODOLOGÍAS Y HERRAMIENTAS UTILIZADAS

Para  desarrollar  el proyecto, es necesario definir una metodología de desarrollo y

las  herramientas necesarias para su implementación. En este apartado, se detallan las etapas

de  la  metodología  empleada,  además  de  presentar  las  herramientas  de  hardware  y  software

empleadas.

1.5.1. Metodología

  Para  el  desarrollo  del  proyecto  se  utilizó  una  metodología  mixta  de  Rapid

Application  Development  (RAD)  y  Scrum.  Esta  metodología  de  desarrollo  permitió  generar

prototipos  funcionales,  realizar  pruebas  y  correcciones  a  corto  plazo.  Esta  metodología  fue

llevada a cabo en 3 etapas:

Análisis  y diseño: esta etapa inicial se enfoca en comprender el público objetivo

(niños  y  jóvenes),  analizando  sus  necesidades,  comportamientos  y  nivel  de  conocimientos

financieros. Con base en este análisis, se establecen los objetivos educativos específicos y se

elabora  el  documento  de  diseño  del  juego  (GDD),  que  servirá  como  guía  detallada  para  el

desarrollo  del  juego.  Además,  se  aplican  principios  de  RAD  para  crear  prototipos  rápidos  en

Unity, lo que permite iterar sobre idea y refinar el diseño para avanzar al desarrollo, facilitando

la  validación

temprana  de

idea,  permitiendo  cambios  ágiles  y  rápidos  en  base  a

retroalimentación temprana.

Desarrollo  e  implementación:  a  partir  de  los  mejores  prototipos  creados  en  la

etapa anterior, se procede a la construcción del juego utilizando un enfoque iterativo basado en

Scrum.  Esta  etapa  implica  el  desarrollo  del  juego  de  manera  incremental,  con  sprints  que

permiten ajustes continuos y mejoras en las funcionalidades. Para ello se asumen los roles de

Scrum  Master,  encargado  de  establecer  y  mantener  la  metodología,  y  Equipo  de  Desarrollo,

encargado  de  la  implementación  técnica del juego y gestión del código. También se integra el

framework  Blended  Games  (bGames) para personalizar la experiencia de juego, incorporando

datos financieros reales de los jugadores.

Evaluación:  la  etapa  final  se  centra  en  evaluar  el  impacto  educativo  y  la

funcionalidad  del  juego.  En  esta  fase,  se  llevarán  a  cabo  tres  tipos  de pruebas: (1) software,

para  evaluar  el  rendimiento  y  la  compatibilidad  de  la  solución;  (2)  usabilidad,  utilizando  el

evaluación  heurística  para  la  jugabilidad  (HEP)  con  un  grupo  acotado  y  de  confianza  para

evaluar  la  interacción  de  los  usuarios  con  el  juego,  midiendo  su  experiencia  en  jugabilidad,

8

mecánicas  y  usabilidad;  y  (3)  aceptación,  para  verificar  el  cumplimiento  de  los  requisitos

funcionales.

1.5.2. Herramientas de desarrollo

Para el desarrollo del proyecto, se utilizó las siguientes herramientas de desarrollo,

seleccionadas por su capacidad para soportar el desarrollo eficiente y efectivo de videojuegos:

Herramientas de hardware:

●  Computador principal:

○  Procesador: 12th Gen Intel(R) Core(TM) i5-12400 2.50 GHz.

○  RAM instalada: 32,0 GB.

○  Tipo de sistema: sistema operativo de 64 bits, procesador x64.

○  Tarjeta gráfica: NVIDIA GeForce RTX 3050.

○  Monitor: 1920 x 1080, 165Hz.

○  Sistema operativo: Windows 11 Pro (versión 23H2).

●  Computador secundario:

○  Procesador: AMD Ryzen 5 2500U with Radeon Vega Mobile Gfx 2.00

GHz.

○  RAM instalada: 12.0 GB.

○  Tipo de sistema: sistema operativo de 64 bits, procesador x64.

○  Tarjeta gráfica: Radeon RX 560 Series.

○  Monitor: 1920 x 1080, 60Hz.

○  Sistema operativo: Windows 11 Enterprise (version 22H2)

Herramientas de software:

●  Unity: un motor de desarrollo de videojuegos altamente versátil y robusto, que

permite  crear  juegos  multiplataforma  con  gráficos  de  alta  calidad  y  físicas

9

realistas.  Unity  será  el  principal  entorno  de  desarrollo  para  el  proyecto,

escogido  por  su  amplia  adopción  en  la  industria,  comunidad  activa  y

documentación  abundante,  permitiendo  la  creación  de  un  juego  interactivo  y

educativo.

●  Visual  Studio  Code:  un  entorno  de  desarrollo  ligero  y  flexible  que  ofrece

soporte completo para la programación en C#, el lenguaje principal utilizado en

Unity.  Visual  Studio  Code  proporciona  herramientas  avanzadas  para

depuración,  pruebas  y  gestión  del  código,  facilitando  un  desarrollo  más

eficiente.

●  GitHub: una plataforma de control de versiones basada en Git, que permitirá la

gestión  del  código  fuente.  GitHub  es  esencial  para  el  seguimiento  de  los

cambios, la colaboración y la integración continua, asegurando que el proyecto

se desarrolle de manera organizada y controlada.

●  Postman: una herramienta para probar y validar la API que se utilizará para la

integración  de  datos

financieros.  Postman  permitirá

realizar  pruebas

exhaustivas  de  la API, asegurando que los datos se integren correctamente y

se utilicen de manera efectiva en el juego.

●  Google  Drive: una plataforma para la gestión de documentos y archivos, que

facilitará el almacenamiento y el acceso a documentos relevantes del proyecto,

asegurando  que  toda  la  información  necesaria  esté  centralizada  y  sea

fácilmente accesible.

●

Itch.io:  una  plataforma  de  distribución  digital  enfocada  en

juegos

independientes,  que  se  utilizará  para  publicar  y  compartir  el  proyecto

desarrollado. El motivo de su selección se debe a su facilidad de uso y porque

permite  publicar  de

forma  gratuita,

lo  que

lo  vuelve  accesible  para

desarrolladores independientes.

Este equipo proporcionó el rendimiento y la capacidad necesaria para desarrollar y

probar el proyecto de manera eficiente.

10

1.6. ORGANIZACIÓN DEL DOCUMENTO

El documento se organiza en seis capítulos, incluyendo este. El resto son:

●  Capítulo  2:

titulado

“Marco  Teórico”,

introduce  el  marco  conceptual,

presentando  los  términos  fundamentales  para  comprender  el  contenido

expuesto  en  los  capítulos  posteriores.  Además,  se  incluye  una  revisión  del

estado del arte, donde se detallan algunas soluciones alternativas al problema

que aborda este proyecto.

●  Capítulo  3:  denominado  “Diseño  del  videojuego  (GDD)”,  presenta  la  idea  y

base  general  del  videojuego  a  desarrollar,  presentando  los  conceptos  más

fundamentales para su construcción, como el objetivo, mecánicas, estilo, entre

otros aspectos.

●  Capítulo  4:  denominado  “Análisis”,  presenta  los  requisitos  funcionales  y  no

funcionales  para el desarrollo del proyecto, junto con los prototipos realizados

para validar dichos requerimientos.

●  Capítulo  5:    titulado  “Diseño  e  Implementación”,  describe  la  arquitectura  del

sistema  precisando  la  estructura, comportamiento, componentes y despliegue

de  la  solución  diseñada, además de detallar la implementación de la solución

propuesta.

●  Capítulo  6:  denominado  “Evaluación”,  en  este  capítulo  se  compara  la

ejecución  del  videojuego  en  distintos  ámbitos  con  el  objetivo  de  verificar  su

ajuste a los requerimientos establecidos.

●  Capítulo  7:  titulado  “Conclusiones”,  se presentan las conclusiones finales del

proyecto, evaluando el cumplimiento de los objetivos y ofreciendo lineamientos

para futuros trabajos.

11

CAPÍTULO 2. MARCO TEÓRICO

En  este  capítulo  se  definen  conceptualmente  ciertos  conceptos  y  términos

relevantes dentro del desarrollo del proyecto. Además se exponen las diferentes investigaciones
y proyectos realizados para abordar la problemática de la alfabetización financiera.

2.1. MARCO CONCEPTUAL

A  continuación,  se  definen  los  conceptos  y  términos  más  importantes  para

comprender la problemática abordada y la implementación de la solución propuesta.

2.1.1. Blended Games (bGames)

Blended  Games  (bGames)  es  un  proyecto  desarrollado  en  el  Interaction  Lab,

perteneciente  al  Departamento  de  Ingeniería  Informática  de  la  Universidad  de  Santiago  de

Chile, cuyo objetivo principal es crear un framework de código abierto para diseñar videojuegos

que  incentiven  el  equilibrio  entre  las  actividades  cotidianas  y  el  entretenimiento  digital.  Para

lograrlo, bGames ofrece la posibilidad de obtener ventajas dentro de los videojuegos a partir de

información  del  entorno  del  usuario,  tales  como  el  ejercicio  físico  que  realiza,  cursos

completados en plataformas web (como Udemy), entre otros.

Este  framework  se  gestiona  los perfiles de los jugadores, obteniendo información

del  entorno  del  usuario  a  través  de  sus  diferentes  sensores  y  normalizando  estos  datos  en

puntaje  para  sus  distintas  dimensiones  (Afectivo, Cognitivo, Físico, Lingüístico y Social), cada

una  con  con  atributos  específicos  relacionados.  De  este  modo  la  obtención  de puntos queda

registrada y relacionada a su actividad obtenida por un sensor (por ejemplo, kilometros recorrido

o cursos completados).

El desarrollo de este framework ha pasado por varias iteraciones, empezando por

una  versión  inicial  del  módulo  cloud  construida  como  una  aplicación  de  escritorio  la  cual

permitía  el  acceso  a  los  perfiles,  sensores  y  permite  su  integración  con  herramientas  de

desarrollo como Unity (Calistro, 2019).

12

La  segunda  iteración,  realizada  por  Mahu  (2020),  integró  su  despliegue  como

microservicios, mejora áreas como seguridad e interoperabilidad e incluye una plataforma web

para la administración de perfiles.

La  tercera  y  última  iteración  realizada  reparó  fallos  e  inconsistencias  que

presentaba  el  módulo  a  través  de  una  depuración  y  rastreo  de  errores,  permitiendo  su

despliegue (Zelada,2023).

Figura 2.1: Diagrama de contexto del módulo cloud de bGames.

Fuente: Zelada, 2023.

Actualmente  el  framework  de  bGames  se  expande  constantemente  con  nuevos

sensores  para  alimentar  el  perfil  multidimensional  de  los  usuarios,  además  de  desarrollarse

nuevos juegos que lo integran.

2.1.2. Unity

Unity  es  un  motor  de  videojuegos  multiplataforma  lanzado  en  2005  por  Unity

Technologies,  es  ampliamente  reconocido  por  su  aprendizaje  accesible,  comunidad  activa  y

gran  repertorio de recursos tanto gratuitos como de pago (Unity Technologies, 2023). También

destaca  por  su  constante  evolución  a  lo  largo  de  los  años,  en las cuales se han incorporado

múltiples  herramientas  como  el  renderizado  (URP,  HDRP),  nuevos  sistemas  de  físicas,  o  el

Multiplayer Center para multijugador online lanzado el presente año para su versión Unity 6.

13

Existen  variados  motores  para  desarrollar videojuegos, uno altamente reconocido

es Unreal Engine, desarrollado por Epic Games, el cual trabaja con el lenguaje   C++, y el cual

se  orienta  a  producciones  de  mayor  escala  (AAA)  (Epic  Games,  2023).  Otro  caso  es  el  de

Godot,  un  motor  de  software  libre  con  un  ecosistema  más  reducido, pero que apuesta por la

simplicidad  y  la  accesibilidad,  ofreciendo  lenguajes  de  scripting  propios  y  C#  (Godot  Engine,

2023).  Tanto  Godot  como  Unity  resultan  motores  atractivos  para  el  desarrollo  independiente

pero,  por  su  parte  Unity,  equilibra  la flexibilidad y la usabilidad, permitiendo desarrollar juegos

tanto para el ámbito independiente como para proyectos de mayor escala.

2.1.3. Juego serio

Un  juego  serio  es  aquel  que  integra  elementos  lúdicos  y  mecánicas  de

entretenimiento  con  el  fin  de  transmitir  conocimientos  o  entrenar  habilidades,  más  allá  de  la

mera  diversión  (Zhonggen,  2019).  A  diferencia  de los videojuegos tradicionales, cuyo objetivo

principal  es  el  ocio,  los  juegos  serios  priorizan  propósitos  educativos  o  formativos, ya sea en

formato  físico  o  virtual.  De  este  modo,  resultan  útiles  en  diversos  ámbitos,  al  ofrecer

experiencias  interactivas  que  facilitan  la comprensión de conceptos y la aplicación práctica de

los mismos.

2.1.4. Alfabetización financiera

La alfabetización financiera refiere a la combinación de conocimientos, habilidades,

actitudes  y comportamientos que permiten a una persona tomar decisiones financieras sólidas

y,  con  ello,  alcanzar  un  bienestar  financiero  individual  (Álvarez  & Ruiz-Tagle, 2016). Según la

Comisión  para  el Mercado Financiero (CMF, 2023), esta comprende elementos fundamentales

como  el  manejo  adecuado  de  productos  financieros,  la  capacidad  de  gestionar  riesgos  y  la

disposición a planificar en función de metas personales o familiares.

2.2 ESTADO DEL ARTE

Una  vez  comprendida  la  problemática  a  tratar,  resulta  necesario  revisar  las

diversas propuestas de organizaciones y académicos desarrolladas en los últimos años sobre el

tema en cuestión, con el fin de comprender los distintos enfoques existentes para abordarla. En

este  caso,  se  presta  especial  atención  a las iniciativas destinadas a promover y desarrollar la

educación financiera en la población.

14

Esta  información  se  divide  en  tres  categorías,  según  el  sector  al  que  se  dirigen

estas  propuestas.  Estas  categorías  son:  educación  financiera  nacional,  educación  financiera

internacional y educación financiera a través de juegos.

Tabla 2.1: Sistematización del estado del arte.

Fuente: elaboración propia, 2024.

Categoría

Título

La educación financiera
Nacional

Estrategia Nacional de Educación
Financiera

Educación financiera en Chile,
realidad y propuestas

Educación financiera en Chile
Diagnóstico e iniciativas

Autores

CAPIF

ABIF

ABIF

Curso para Docentes Educación
para el Consumo en la Escuela 2020

SERNAC

Comisión culmina actividades del
Mes de la Educación Financiera con
lanzamiento de nueva versión de su
sitio CMF Educa

CMF

Mi barrio Financiero

ABIF & Universidad
de Chile

La educación financiera
Internacional

Educación financiera en Chile,
realidad y propuestas

Descripción de My Classroom
Economy

ABIF

Vanguard

La educación financiera desde
los videojuegos

A Meta-Analysis of Use of Serious
Games in Education over a Decade

Yu Zhonggen

2.2.1. La educación financiera nacional

A  nivel nacional, han surgido numerosas iniciativas con el propósito de mejorar la

alfabetización  financiera  en  el  país,  tanto  por parte del sector público como del privado. En el

ámbito  público, se destaca la Estrategia Nacional de Educación Financiera (ENEF), creada en

2014  por  la  presidenta  Michelle  Bachelet,  cuyo  objetivo  es  que  la  ciudadanía  comprenda  y

maneje  conceptos  y  productos

financieros  y  previsionales  (CAPIF,  2016).  Asimismo,

15

encontramos  el  programa  "Central  en  tu  Vida"  y  el  curso  para  docentes  "La  Ciudad  de  las

Oportunidades", lanzados por el Banco Central (ABIF, 2020), además del curso "Educación para

el  Consumo  en  la  Escuela",  impulsado  por  el  Servicio  Nacional  del  Consumidor  (SERNAC,

2020).

En  el  ámbito  privado,  la  Asociación  de  Bancos  en  cooperación  (ABIF)  con  la

Universidad  de  Chile  lanzó  en  2021  "Mi  Barrio  Financiero",  una  plataforma  web  que  ofrece

cursos  y cápsulas audiovisuales de educación financiera (ABIF & Universidad de Chile, 2021).

Otras  iniciativas  destacadas  son  aquellas  realizadas  por  los  bancos,  que  incluyen  charlas  y

talleres  financieros  dirigidos  a  estudiantes  secundarios  y universitarios, representando el 25%

de todas sus propuestas (ABIF, 2022).

Figura 2.2: Iniciativas de educación financiera en la banca.
Fuente: Asociación de Bancos (ABIF) en base a información de bancos, 2022.

Entre  las  iniciativas  nacionales  mencionadas  y  otras  existentes, cabe destacar el

portal  CMF  Educa,  lanzado  en  2012 por la Comisión para el Mercado Financiero (CMF). Este

portal  web  tiene  como  objetivo  proporcionar  información  a  la  ciudadanía  para  mejorar  sus

conocimientos  sobre  productos  y  servicios  financieros,  contribuyendo  así  a  la  inclusión  y

educación financiera. Comprometido con la educación financiera, el portal ofrece una variedad

de  herramientas,  consejos  y  cápsulas  de  información  que  se  han  ido  actualizando  con  el

tiempo.  Su  versión  más reciente, lanzada en 2021, incluye novedades como "Momentos de la

Vida",  que  proporciona  información  útil  sobre  las  principales  decisiones  financieras  de  las

16

personas,  una  nueva  sección  sobre  "Créditos  Hipotecarios"  y  datos  actualizados  dirigidos  a

estudiantes, entre otros (CMF, 2021). Todo esto convierte al portal no solo en un instrumento de

educación financiera, sino también en una herramienta útil para evaluar la situación económica

personal gracias a las múltiples herramientas que ofrece.

Figura 2.3: Sitio oficial de CMF Educa.

Fuente: Comisión para el Mercado Financiero (CMF), 2024.

2.2.2. La educación financiera internacional

Una  de  las  iniciativas  más  reconocidas  es  My  Classroom  Economy  (MyCE),

lanzada inicialmente en el año 2011 por Vanguard, una de las firmas de inversión más grandes

a nivel mundial. Este programa de educación financiera gratuita tiene como objetivo inculcar la

responsabilidad  financiera  básica  y  enseñar  el  valor  de  la  gratificación. En él, los estudiantes

ganan y gastan dinero en una microeconomía simulada. A medida que avanzan en los niveles

de grado, se incorporan conceptos financieros adicionales. Está cuidadosamente diseñado para

complementar,  no  interrumpir,  el  plan  de  estudios,  por  lo  que  puede  ser  implementado  por

cualquier profesor, en cualquier materia (Vanguard, 2011).

17

Figura 2.4: Sitio oficial de My Classroom Economy.

Fuente: My Classroom Economy, 2024.

2.2.3. La educación financiera desde los juegos

Con  el  objetivo  de  modernizar  el  aprendizaje  y  disminuir  las  percepciones

negativas  sobre  los  juegos  (considerados  como  pérdida  de  tiempo  o  inadecuados  para  la

educación),  se  propuso  la  creación  y  desarrollo  de  los  juegos  serios.  Esta  subcategoría  se

refiere  a  herramientas  de  entretenimiento  con  un  propósito  educativo  (Zhonggen,  2019).  De

esta  manera,  los  juegos  serios  se  convierten  en  una  herramienta  enriquecedora  para  el

bienestar humano, ya que promueven el aprendizaje de una forma dinámica y entretenida.

Dentro de los juegos serios, existe una variedad cuyo objetivo principal es enseñar

conceptos  básicos  sobre  finanzas.  Algunos  en  formato  físico:  Monopoly,  Cashflow  101,  The

Game  of  Life.  Y  otros  en  formato  virtual:  Financial  Playground,  Money  Savvy  Pig,  Pocket

Money, Stock Ticker, Inflation Fighter.

18

Además,  existen  numerosos  videojuegos  tradicionales  que  integran  conceptos

financieros  sin  tener  como  objetivo  principal  educar.  A  través  de  estos  juegos,  los  jugadores

pueden adquirir conocimientos sobre temas financieros. Algunos ejemplos son Monopoly Plus,

Cities: Skylines, Zoo Tycoon y The Game of Life 2.

Tabla 2.2: Finanzas en videojuegos tradicionales.

Fuente: elaboración propia, 2024.

Nombre  PEGI

Género

Precio  Plataforma  Más
info

Sistema de
finanzas

Monopoly
Plus

3

Estrategia
Juego de
Mesa

$9.900  PlayStation
, Windows,
Nintendo
Switch,
Xbox

Monop
oly Plus
(ubi.co
m)

Cities:
Skylines

3

Construcción
de ciudades,
Construcción
y Gestión

$21.100  Windows,
macOS,
Linux,
Xbox,
PlayStation
, Nintendo
Switch

Cities:
Skyline
s
(steam.
com)

Zoo
Tycoon

3

Simulación
económica,
Gestión

$7.700

PC, Mac
OS,
Nintendo
Switch

Zoo
Tycoon
(steam.
com)

The game
of life 2

3

$7.000

Casual,
Estrategia,
Juedo de
Mesa

Nintendo
Switch,
PlayStation
, Android,
Xbox,
Windows

TheGa
meOfLif
e2
(steam.
com)

Compra de
Terrenos, Alquiler
de Terrenos,
Compra de
Ferrocarriles,
Trueque de
Propiedades entre
Jugadores

Construcción de
Edificios,
Carreteras,
Fábricas,
Monumentos,
Contratos

Contratos con
Empleados,
Cimientos de
Edificios,
Mantenimiento y
Adquisición de
Animales para el
Zoo, Servicios de
Electricidad y Agua

Salario, Impuestos,
Gastos, Ahorro,
Educación, Familia.

19

2.3. RESUMEN

En  el  presente  capítulo  se  da  a  conocer  un  marco  conceptual  de  los  conceptos

necesarios para el correcto entendimiento del contenido y contexto del proyecto, definiendo qué

es  y  para  que  se  utiliza  bGames,  las  fortalezas  de  el  motor  de  videojuegos  Unity, que es un

juego serio y la importancia de la alfabetización financiera.

Seguido  se  abordó  algunos  de  los principales proyectos y soluciones que se han

implementado a nivel nacional e internacional para mejorar la alfabetización financiera. Además

de  mencionar  algunos  videojuegos  que  contribuyen  a  este  aprendizaje,  sea  o  no  su  objetivo

principal.

20

CAPÍTULO 3. DISEÑO DEL VIDEOJUEGO (GDD)

En  este capítulo se detalla el documento de diseño del videojuego (GDD), el cual

explica toda la información sobre su desarrollo. Documento que fue utilizado como modelo para

su  creación,  sirviendo  como  referencia  para  comprender la visión general del videojuego y su

funcionamiento.

3.1 OBJETIVOS DEL JUEGO

El  videojuego  tiene  como  objetivo  mejorar  la  alfabetización  financiera  de  las

personas,  teniendo  como  público  objetivo  a  la  población  joven  (18-34  años).  Para  ello,  el

videojuego  estará  constituido  como  uno  de  tablero  de  mesa,  el  cual  presentará  al  jugador

diferentes desafíos que pondrán a prueba sus conocimientos financieros a través de preguntas

y toma de decisiones que afectarán sus finanzas. Esto se logrará mediante tarjetas a elegir, las

cuales  evaluarán  su  comportamiento  y  actitud  financiera. A medida que el nivel financiero del

jugador progrese, se enfrentará a preguntas más desafiantes.

Adicionalmente, el videojuego contará con el componente opcional Blended Games

(bGames), el cual permitirá personalizar la experiencia de juego a través de sus sensores, que

obtendrán  datos  del  entorno  real  del  usuario  y  los  transformarán  en  puntos  para  su  perfil

multidimensional virtual, los cuales podrán ser canjeados en el videojuego por alguna ventaja.

3.2 MECÁNICAS DEL JUEGO

En  este  apartado  se  definen  las  principales  mecánicas  y  funcionalidades  que

contará  el  videojuego,  sirviendo  como  referencia  para  recordar  ideas  y  detalles  para  su

implementación.

2.2.1. Reglas generales

El  videojuego  es  de  tablero  de  mesa  en  el  cual  el  jugador  avanza  a  través  de

diferentes casillas. En cada turno, se presenta una pregunta financiera de acuerdo con el nivel

actual  del  jugador,  las  preguntas  se  conforman  de  3  alternativas y se relacionan a conceptos

fundamentales  de  las  finanzas,  tales  como:  indicadores  económicos,  planificación  financiera,

21

presupuesto y deudas. El jugador contará con dos intentos para responder preguntas por turno,

con la posibilidad de expandirse a tres si se encuentra conectado a bGames y posee puntos. Si

el jugador responde correctamente, se le presentará un dado giratorio al cual debe golpear con

un  salto  para  detenerlo.  Tras ello, avanzará una cantidad de casillas igual al número obtenido

del dado. Al detenerse, se le presentarán dos tarjetas de acuerdo con el tipo de casilla en la que

se encuentre, teniendo que decidir cuál de las dos escoger según sus finanzas actuales.

Tras  cumplir  una  cantidad  X  de  turnos  seleccionados  previamente  al  crear  la

partida,  representada  en  el  videojuego  como  “años”,  la  partida  se  dará  por  concluida,

presentando  los  puntajes  finales  de  cada  jugador  y  proporcionando  una  evaluación  del  nivel

obtenido en función de las preguntas respondidas.

2.2.2. Sistema de contenidos

El  videojuego  cuenta  con  un  sistema  de  paquetes  de  preguntas  llamados

contenidos.  De  estos  paquetes,  se  puede escoger uno para utilizar en cada partida, de forma

que se presenten las preguntas que lo conforman. Este sistema permite actualizar paquetes de

preguntas  existentes o crear nuevos paquetes con temáticas específicas o más generales, las

cuales no están limitadas a conceptos financieros.

Estos paquetes también tienen la posibilidad de disponibilizar su descarga a todos

los  usuarios  a  través  de  la  interfaz,  pero  es  una  funcionalidad  disponible  solo  para

desarrolladores, ya que únicamente ellos cuentan con permisos para acceder al repositorio que

los almacena. Por lo anterior, se incorpora adicionalmente la posibilidad de exportar contenidos

generados  e  importarlos,  a  fin  de  ofrecer  la  opción  de  que  sean  compartidos  por  medios

externos al videojuego.

2.2.3. Sistema de progresión

Cada  jugador  cuenta con un perfil de usuario que lo identifica y que almacena su

historial  de  partidas  y  estadísticas,  como  mejor  puntaje,  puntaje  promedio,  partidas  jugadas,

experiencia y nivel financiero. De estas, se destacan la experiencia y el nivel financiero, siendo

la primera el puntaje acumulado entre todas sus partidas, mientras que el segundo representa

el  nivel  de conocimiento general actual del jugador. Este nivel se obtiene inicialmente a través

de una prueba de diagnóstico de seis preguntas realizada al crear el perfil y se repite cada cinco

partidas para su revaluación, siempre que no haya alcanzado el máximo.

22

Dentro  de  las  partidas,  cada  vez  que  el  jugador  responda  correctamente  una

pregunta, obtiene puntos financieros de acuerdo con la dificultad de la misma. Esta dificultad se

basa en el nivel financiero del jugador en la partida, tomando como referencia su nivel financiero

general del perfil para partidas locales, de modo que empieza con preguntas de su nivel actual,

mientras  que  en  modalidad  en  línea  todos  empiezan  nivel  1  para  balancear  el  comienzo.  A

medida  que  su  puntaje  en  la  partida  aumenta,  también  lo  hace  temporalmente  su  nivel,

presentando preguntas más desafiantes hasta alcanzar el nivel máximo de dificultad.

Además de los puntos, a lo largo de la partida, el jugador también debe administrar

el  dinero  obtenido  con  el  fin de acumular la mayor cantidad posible al final de la partida. Este

dinero se ve afectado por las tarjetas presentadas en cada casilla, las cuales ponen a prueba su

comportamiento y actitud financiera al tener que escoger entre dos posibles opciones.

2.2.4. Interacción del jugador

Durante  las  partidas,  el  jugador  cuenta  con  una  serie  de  acciones  que  puede

realizar. Estas son:

●  Responder  pregunta:  cada  jugador  debe  responder  preguntas  durante  su

turno,  teniendo  dos  intentos  de  base  y  obteniendo  puntos  financieros  al

responder una correctamente.

●  Saltar:  tras  responder  correctamente  una  pregunta,  se  presenta  un  dado

giratorio, el cual el jugador debe golpear con un salto para detenerlo y avanzar

casillas según el número obtenido.

●  Escoger tarjeta: tras detener su movimiento en una casilla, se presentan dos

tarjetas,  de  las  cuales  el  jugador  debe  escoger  una  de  acuerdo  con  lo  que

considere mejor para sus finanzas en la partida.

●  Canjear  intento  extra  (opcional):  adicionalmente,  si  el  jugador  cuenta  con

una  sesión  de  bGames  activa  y  puntos de bGames para canjear, en caso de

responder  incorrectamente  las  preguntas  durante  su  turno  en dos ocasiones,

se  presenta  la posibilidad de canjear un intento extra por única vez por turno,

consumiendo  un  punto  de  bGames. Esto otorga una ventaja a quien utilice el

componente, siendo un incentivo atractivo, pero no tan significativo como para

afectar en gran medida la experiencia de los demás jugadores que no lo usan.

23

2.2.5. Economía del juego

Durante  las  partidas,  el  jugador  cuenta  con  un  capital  de  dinero  que  debe

administrar  a  fin  de  obtener  la  mayor  cantidad  posible.  Este  capital  se  compone  de  los

siguientes elementos:

●  Dinero: es el dinero líquido que posee el jugador, utilizable para pagar gastos o

invertir.

●

Inversión: es el capital que el jugador tiene invertido en activos; representa el

total invertido junto con sus ganancias.

●  Deuda:  representa  la  suma  de  los gastos pendientes que tiene el jugador en

total.

●

Ingreso por turno: representa la cantidad de dinero que obtiene el jugador en

cada turno. Este se compone de un salario base de $1.000.

●  Egreso por turno: representa la cantidad de dinero que el jugador debe pagar

en cada turno con base en sus gastos actuales. En caso de no pagar, el gasto

se mantiene y se aplica interés a la deuda.

Además,  el  capital  del  jugador  se  ve  afectado  de  acuerdo  con  las  tarjetas

escogidas, de las cuales existen cuatro tipos según la casilla en la que se ubiquen. Estas son:

●  Casilla  de  ingreso:  presenta  al  jugador  dos  tarjetas,  las  cuales  pueden

otorgarle  una  cantidad  de  dinero  fija  o  un  aumento  porcentual  en  su  salario

actual, aumentando su ingreso por turno.

●  Casilla  de  egreso:  presenta  al  jugador  dos  tarjetas  de  gasto,  las  cuales

pueden hacer que el jugador pague una cantidad de dinero fija por única vez o

adjudicar un gasto recurrente por una cierta cantidad de turnos, convirtiéndose

en una deuda. En caso de escoger una tarjeta de gasto fijo y no contar con el

dinero, esta se convierte en deuda con interés aplicado.

●  Casilla  de  evento:  presenta  al  jugador  dos  tarjetas  que  pueden  otorgar  o

quitar una cantidad fija de dinero a todos los jugadores de la partida.

●  Casilla de inversión: presenta al jugador dos tarjetas que representan activos

en  los  cuales puede invertir. Esta casilla, adicionalmente, posee un campo de

entrada  para  ingresar  el  monto  de  la  inversión  con base en su dinero actual.

Asimismo,  es  la  única  casilla  que  cuenta  con  la  posibilidad  de  no  escoger

ninguna tarjeta en caso de no desear invertir en los activos presentados.

24

2.2.6. Sistema de puntaje

El  sistema  de  puntaje  de  las  partidas  representa  el  rendimiento  del jugador y se

utiliza para calcular las posiciones en el modo multijugador. El puntaje final se compone de dos

elementos.

En primer lugar, se tienen los puntos financieros obtenidos al responder preguntas

correctamente  en  cada  turno,  siendo  el  factor  que  más  impacto  tiene  para  obtener  un  buen

resultado. En segundo lugar, se tiene el capital, el cual es la suma del dinero líquido del jugador

y su capital invertido, menos las deudas pendientes. Este monto actúa como una bonificación,

disminuyendo su impacto a medida que la cantidad crece.

De esta manera, el puntaje final se calcula siguiendo la siguiente fórmula:

(𝑐𝑎𝑝𝑖𝑡𝑎𝑙_𝑓𝑖𝑛𝑎𝑙  +  1)
𝑝𝑢𝑛𝑡𝑎𝑗𝑒  = 𝑝𝑢𝑛𝑡𝑜𝑠  +  𝑙𝑜𝑔
2

Ecuación 3.1: Fórmula de cálculo del puntaje final.

Fuente: elaboración propia, 2024.

Además  del  puntaje  obtenido,  se  presenta  una  evaluación  del  nivel  financiero

alcanzado  en  la  partida.  Esta  evaluación  se  basa  en  el  puntaje  final  obtenido,  calculado

siguiendo la siguiente fórmula:

𝑒𝑣𝑎𝑙𝑢𝑎𝑐𝑖ó𝑛  =   𝑝𝑢𝑛𝑡𝑎𝑗𝑒

6

+  1

Ecuación 3.2: Fórmula de cálculo de la evaluación.

Fuente: elaboración propia, 2024.

De  esta  manera,  el  jugador  obtiene una evaluación general del rendimiento en la

partida  con  base  en  el  nivel  calculado  a  partir  de  su  puntaje,  obteniendo  los  siguientes

resultados:

●  Nivel 1: principiante.

●  Nivel 2: intermedio bajo.

●  Nivel 3: intermedio alto.

●  Nivel 4: avanzado.

25

3.3 DISEÑO DE MUNDO

El  mundo de WealthQuest es un tablero de mesa ambientado en la época actual,

representando  una  ciudad  que  busca  reflejar  un  entorno  social  y  laboral.  Este  mundo  se

compone de varias casillas por las cuales el jugador avanza de manera cíclica, teniendo como

objetivo en cada partida avanzar a lo largo del tablero y acumular la mayor cantidad posible de

puntos financieros y capital.

3.4 INTERFAZ DE USUARIO (UI)

La  interfaz  de usuario del videojuego está compuesta por dos grandes interfaces.

La primera es el menú principal, que es el primer vistazo del usuario al ingresar al juego. Esta

interfaz  se  compone  de  varias  vistas,  cuya  navegación  se  representa  en  la Figura 3.1. Estas

vistas son:

●

Inicio de sesión: interfaz donde usuario inicia sesión con su cuenta de usuario

de WealthQuest.

●  Registro  de  usuario:  interfaz  donde  el  usuario  puede  registrar  una  cuenta

para ingresar y jugar WealthQuest con su perfil respaldado en la nube.

●  Recuperar  contraseña:  interfaz  donde  el  usuario  puede  restablecer  la

contraseña de su cuenta usando su correo en caso de que se haya olvidado.

●  Menú de inicio: interfaz inicial al ingresar al juego que permite navegar por las

demás interfaces.

●  Menú  de  contenidos:  interfaz  de  administración  de  contenidos del usuarios,

donde se puede descargar, eliminar e importar los mismos.

●  Crear contenido: interfaz de creación o modificación de contenidos original del

usuario.

●  Perfil: interfaz de visualización de historial y perfil del jugador, con opción para

modificar nombre y conectar/desconectar cuenta de bGames.

●  Opciones: interfaz para modificar audio y gráficos del juego.

●  Modos de juego: interfaz para escoger la modalidad a jugar.

●  Multijugador  local:  interfaz  para  escoger  la  modalidad  multijugador  a  jugar,

siendo estas: Pasar y jugar y Multi-mando.

●  Multijugador  en  línea:  interfaz  para  crear  una  sesión  de  juego  en  línea  o

conectarse a una sala existente.

26

●  Sala  local:  interfaz  de  creación  de partida local donde se escoge la cantidad

de  turnos  a  jugar  y  el  paquete  de  contenido.  Además,  cada  jugador  puede

escoger su personaje y modificar temporalmente su nombre.

●  Sala Online:   interfaz de creación de partida en línea donde el host escoge la

cantidad de turnos a jugar y el paquete de contenido.

Figura 3.1: Diagrama navegación interfaces.

Fuente: elaboración propia, 2024.

La segunda gran interfaz es la que se visualiza durante una partida, la cual cuenta

con los siguientes elementos:

●  HUDs: interfaz que muestra visualmente el capital y un puntaje actual de cada

jugador.

●  Footer:  interfaz  que  muestra  el  año  en  cursos  y  las  acciones  que  puede

realizar el jugador con la tecla o botón para realizar.

●  Menú  de  pausa:    interfaz  para  modificar  opciones  del  juego,  volver al menú

principal o salir del juego.

●  Siguiente jugador: interfaz visualizada al cambiar el jugador en turno.

●  Siguiente año: interfaz visualizada al cambiar el año de la partida.

●  Fin  del  juego:  interfaz  visualiza  al  terminar  el  juego  la  cual  muestra  los

resultados de cada jugador en la partida.

27

3.5 CONTROL Y ACCESIBILIDAD

El videojuego se desarrolla con compatibilidad para el sistema Windows, contando

con un esquema de controles enfocado principalmente en jugar y navegar con teclado y mouse.

Adicionalmente,  se  incorpora  la  posibilidad  de  jugar  con  un  gamepad  para  aumentar  las

opciones del usuario, contando además con una guía visual de los botones a accionar en cada

turno para ejecutar las acciones disponibles.

3.6 ESTILO ARTÍSTICO Y SONIDO

El  videojuego  cuenta  con  un  estilo  visual  en  3D,  con  gráficos  y  modelos

caricaturescos,  y  una  paleta  de  colores vibrante, conformada principalmente por anaranjado y

violeta. Tanto la interfaz como los personajes cuentan con una serie de animaciones y sonidos

para hacer la experiencia de juego más atractiva y dinámica.

Figura 3.2: Paleta de colores.

Fuente: elaboración propia, 2024.

3.7 MODOS DE JUEGO

El  videojuego  cuenta  con  un  total  de  tres  modalidades  que  dependen  de  la

cantidad de jugadores y la conexión deseada. Estos modos son:

28

●  Un jugador: modalidad para jugar una partida en solitario

●  Multijugador local:

○  Pasar  y  jugar:  modalidad  para  jugar  de  2-4  personas  en  un  mismo

dispositivo y con un único periférico compartido por los jugadores.

○  Multi-mando:  modalidad  para  jugar  de  2  a  4  personas  en  un  mismo

dispositivo,  con  cada  jugador  utilizando  un  periférico  único  (teclado,

mouse o gamepad).

●  Multijugador en línea: modalidad para jugar de 2-4 personas cada uno en un

dispositivo diferente, permitiendo usuarios de redes externas al host.

3.8 ADMINISTRACIÓN DE PARTIDAS Y GUARDADO

El  videojuego  cuenta  con  un  sistema  de  guardado  que  permite  almacenar  una

única  sesión  de  juego  para  modalidades  de  juego  local.  De  esta  manera,  el  jugador  puede

reanudar  su  sesión  en  cualquier  momento  o  comenzar  una  nueva,  eliminando  la  partida

guardada.

Además,  cada  vez  que  el jugador finaliza una partida, ya sea local o en línea, se

almacena un registro de los resultados en el dispositivo local sincronizalo con el respaldo en la

nube, actualizando las estadísticas del perfil del jugador, a fin de mantener un registro histórico

de su rendimiento.

3.9 RESUMEN

En  el  presente  capítulo se da a conocer las bases de los principales conceptos y

funcionamientos  del  videojuego  a  desarrollar,  de  esta  manera  se  tiene  una  idea  general  de

cómo funcionará el videojuego, sus características y su objetivo principal.

29

CAPÍTULO 4. ANÁLISIS

En  este  capítulo  se  detalla  el  proceso  de  levantamiento  de  requisitos,  tanto

funcionales  como  no  funcionales.  Además  se  detalla  el  proceso  de  desarrollo  de  prototipos
utilizados para probar y evaluar aspectos del diseño y funcionalidades.

4.1. REQUISITOS

Para  desarrollar  WealthQuest,  es  necesario  definir  de  manera clara y precisa los

requisitos del proyecto. Estos requisitos se han identificado considerando tanto las necesidades

funcionales  del  sistema  como  las  restricciones  técnicas  que  guiarán  su  implementación  y

desarrollo.

La especificación de requisitos se realiza con la intención de organizar los periodos

de trabajo, establecer un marco claro de desarrollo y definir los objetivos del proyecto. Para ello,

se  utilizará  la  siguiente  nomenclatura  en  la  identificación  de  los requisitos: XX_nn, donde XX

representa el tipo de requisito (RF para requisitos funcionales y RNF para no funcionales) y nn

indica  el  número  secuencial  del  requisito.  Estos  requisitos,  tanto  funcionales  como  no

funcionales, son fundamentales para guiar el diseño y desarrollo del videojuego.

Un  requisito  funcional  hace  referencia  a  los  comportamientos  esperados  del

sistema, es decir, describe lo que el sistema debe hacer, mientras que un requisito no funcional

describe

las  propiedades  del  sistema,  como

rendimiento,  seguridad  o  accesibilidad

(Sommerville, 2011, 84-85). Para WealthQuest, los requisitos funcionales están orientados a las

mecánicas  del  juego,  la  interacción  del  jugador  con  el  sistema  y  la  integración  con  bGames,

mientras que los no funcionales están enfocados en la plataforma, la experiencia del usuario y

la eficiencia del sistema.

En  las  tablas  siguientes  se  presentan  los  requisitos  funcionales  y no funcionales

que  se  han  definido  para  WealthQuest.  Estos  serán  utilizados  como  guía  para  dirigir  el

desarrollo  del  proyecto  y  como  referencia  para  verificar  el  progreso  y  el  cumplimiento  de  los

objetivos durante el ciclo de vida del desarrollo.

30

4.1.1. Requisitos funcionales

A continuación se encuentra el listado de requisitos funcionales.

Tabla 4.1: Requisitos funcionales - Parte I.

Fuente: elaboración propia, 2024.

Id

Nombre

Descripción

RF_001

Tablero de juego

El sistema debe poseer un tablero de juego dinámico donde

los jugadores avancen en cada turno por sus casillas hasta la

meta.

RF_002

Cámara de juego

El  sistema  debe  incorporar  una  cámara  que  muestre  al

jugador en turno.

RF_003

HUD de juego

El  sistema  debe  mostrar  visualmente  los  datos  de  los

jugadores.

RF_004

Modos de juego

El  juego  debe  ofrecer  modalidad  de  juego:  individual  y

multijugador (hasta 4 jugadores), de manera local o en línea.

RF_005

Sistema de turnos  El  sistema  debe  administrar  los  turnos  de  los  jugadores,

pasando  al  siguiente  turno  automáticamente  al  finalizar  las

acciones.

RF_006

Lanzamiento del

El  sistema  debe  incorporar  el  lanzamiento  de un dado para

dado

avanzar según su resultado.

RF_007

Sistema de

El  sistema  debe  presentar  diferentes  preguntas  mostradas

preguntas

durantes  cada  partida  las  cuales  escalan  en  dificultad

durante el trayecto.

RF_008

Sistema de

El  sistema  debe  presentar diferentes casillas que presenten

casillas

situaciones financieras a afrontar.

31

Tabla 4.2: Requisitos funcionales - Parte II.

Fuente: elaboración propia, 2024.

Id

Nombre

Descripción

RF_009

Sistema de

El  sistema  debe  medir  el  progreso  del jugador mediante un

puntuación

sistema  de  puntos  que  refleje  el  desempeño  en  las

respuestas.

RF_010

Sistema de

El  sistema  debe  permitir  crear  e  importar  paquetes  de

contenidos

preguntas para las partidas.

RF_011

Menú inicial

El sistema debe contar con un menú inicial para navegar por

las configuraciones, perfil, contenidos y modos de juego.

RF_012

Sistema de

El  sistema  debe  permitir  guardar  y  reanudar  partidas  para

guardado

cada modalidad de juego.

RF_013

Historial

El sistema debe almacenar el registro de partidas finalizadas

por el usuario.

RF_014

Perfil de bGames

El  sistema  debe  permitir  conectar  el  perfil  multidimensional

del framework de Blended Games y consumir puntos.

RF_015

Sensor de

Se  debe  incluir  un  sensor  para  la  captura  de  datos  del

bGames

entorno  financiero  del  usuario  que  se normalizan en puntos

para el perfil de bGames.

RF_016

Perfil de usuario

El  sistema  debe  contar  con  un  perfil  del  usuario  con

estadísticas generales según sus partidas.

32

4.1.2. Requisitos no funcionales

A continuación se encuentra el listado de requisitos no funcionales.

Tabla 4.3: Requisitos no funcionales.

Fuente: elaboración propia, 2024.

Id

Nombre

Descripción

RNF_001  Plataforma

de

El  sistema  debe  estar  disponible  exclusivamente  para  la

Windows

plataforma Windows en su primera fase de desarrollo.

RNF_002  Compatibilidad

El  sistema  debe  ser  compatible  con dispositivos de entrada:

con periféricos

gamepads, teclados y ratones en la escena de juego.

RNF_003  Motor

de

El  sistema  debe  ser  construido  utilizando  el  motor  de

videojuegos Unity

videojuegos Unity.

RNF_004  Compatibilidad de

El  sistema  debe  ser  compatible  con  la  modificación  de

bGames

mecánicas de bGames.

RNF_005  Ventajas

por

El  sistema  debe  otorgar  beneficios  por  el  uso  de  puntos  de

puntos bGames

bGames.

4.2. PROTOTIPADO

El  proceso  de  desarrollo  de  WealthQuest  se  basó  en  una  serie  de  prototipos

iterativos,  con  el  objetivo  de  validar  y  ajustar  los  requisitos  antes  de  proceder  al  desarrollo

completo.  En  cada  prototipo  se  evaluaron  diversas mecánicas y componentes del juego, y se

abordaron  problemas  técnicos  y  de  diseño  a medida que surgían. Esta etapa fue crucial para

identificar soluciones tempranas y realizar ajustes antes de la implementación final.

A  continuación,  se  presenta  el  análisis  de  los  prototipos  y  las  iteraciones

realizadas.

33

4.2.1. Prototipo 1: escena tablero

Tabla 4.4: Resumen del prototipo escena tablero.

Fuente: elaboración propia, 2024.

ID prototipo

P01

Objetivo

Desarrollar la escena básica del tablero de juego con piezas de jugadores,

dado, cámaras y HUD para la interacción inicial.

Descripción

El  tablero  desarrollado  cuenta  con  casillas, piezas de jugador, sistema de

dado,  cámaras  para  seguimiento del dado y de los jugadores, además de

un HUD básico que muestra el puntaje y el turno actual.

RF

RNF

RF_001, RF_002, RF_003, RF_004

RNF_001, RNF_003

El desarrollo del primer prototipo permitió visualizar la estructura básica del juego,

donde se establecieron las bases para las interacciones principales entre el jugador, el dado, y

el tablero. En esta iteración, se generó:

●  Generación del tablero: el tablero consta de un camino lineal de casillas en el

que los jugadores avanzan en base al lanzamiento de un dado.

●  Casillas: se crearon las bases para las diferentes casillas a implementar.

●  Piezas  del  jugador:  se  añadieron  unas  piezas  iniciales  para  representar  al

jugador a lo largo del tablero.

●  Sistema  dados:  se  creó  una  función  para  el  lanzamiento  de  un  dado  que

mueve al jugador en base a su resultado.

●  Cámara:  se  incluyó  una  cámara  dinámica  que  sigue  los  movimientos  del

jugador en turno.

●  HUD:  se  integró un HUD básico que muestra el puntaje acumulado y nombre

del jugador en turno.

34

Figura 4.1: Tablero de juego básico.

Fuente: elaboración propia, 2024.

Durante  la  implementación  de  este  prototipo,  se  enfrentaron  algunos  problemas,

principalmente  relacionados  con  el  lanzamiento  del  dado,  el  cual  no  reconocía  su  cara

mostrada. También el HUD no estaba optimizado, pues se actualizaba en cada frame y no solo

al realizar un cambio.

Para  solucionar  estos  problemas,  se  creó  dentro  del  dado  objetos  hijos  vacíos

posicionados  en  cada  una  de  sus  caras  para  representarlas,  con  ello  detectando  la  cara

mostrada  en  cámara.  Asimismo,  el  HUD  fue  optimizado  para  actualizarse  solo  cuando  el

jugador realiza una acción que modifica sus datos.

Figura 4.2: Objeto dado.

Fuente: elaboración propia, 2024.

35

Para evaluar este primer prototipo se realizó una prueba observando la interacción

del dado, la pieza del jugador y el tablero, así como la sincronización del HUD y la cámara. Las

pruebas realizadas permitieron establecer la base inicial de los requerimientos más básicos del

videojuego, tales como el movimiento del jugador y su interacción con el tablero.

4.2.2. Prototipo 2: sistema de turnos multijugador local

Tabla 4.5: Resumen del prototipo sistema de turnos multijugador local.

Fuente: elaboración propia, 2024.

ID prototipo

P02

Objetivo

Implementar  el  sistema  de  turnos  multijugador  local  para  que  solo  el

jugador en turno pueda realizar acciones y responder preguntas.

Descripción

El  sistema  de  turnos  desarrollado  permite  que  solo  el  jugador  en  turno

lance  el  dado  y  responda  preguntas.  El  turno  se  pasa  automáticamente

cuando el jugador completa su movimiento y responde la pregunta.

RF

RNF

RF_001, RF_004, RF_005, RF_006

RNF_001, RNF_002, RNF_003

El segundo prototipo desarrollado se centró en la implementación de un sistema de

turnos  multijugador  local,  con  el  objetivo  de  permitir  que  los  jugadores  tomen  turnos  para

responder preguntas y lanzar el dado. Este sistema garantiza que solo el jugador en turno tenga

la  capacidad  de  realizar  acciones de juego, y que, una vez completada sus acciones, el turno

pase automáticamente al siguiente jugador.

El prototipo establece la lógica básica de los turnos, permitiendo que los jugadores

respondan  preguntas,  lancen  el  dado,  se  muevan  en  el  tablero, y, posteriormente, se pase el

turno  de  forma  automática.  Sin embargo, durante el desarrollo inicial se enfrentó un problema

relacionado con los periféricos, donde cualquier jugador podía realizar acciones de juego, lo que

afectaba la jugabilidad.

Para solucionar este problema, se utilizó el componente Player Input Manager para

la  generación  de  los  jugadores en base a un objeto prefabricado, y Multiplayer Event System,

para  asignar  cada  periférico  exclusivamente  a  un jugador, permitiendo interactuar únicamente

36

con su respectiva interfaz. Con esta solución, solo el jugador en turno puede realizar acciones

de juego obteniendo así una experiencia de juego ordenada y fluida.

Figura 4.3: Objeto prefabricado del jugador.

Fuente: elaboración propia, 2024.

Para  evaluar  su  funcionamiento  se  realizó  una  prueba  con  múltiples  jugadores

utilizando distintos periféricos. Se verificó que la lógica de turnos operará correctamente y que

únicamente el jugador en turno pueda interactuar con el juego.

37

4.2.3. Prototipo 3: sistema de casillas y preguntas

Tabla 4.6: Resumen del prototipo sistema de casillas y preguntas.

Fuente: elaboración propia, 2024.

ID prototipo

P03

Objetivo

Implementar un sistema de casillas para representar situaciones financieras

y un sistema de preguntas para representar conocimiento financiero.

Descripción

Las  casillas  desarrolladas  muestran  tarjetas  las  cuales  representan

situaciones  financieras  que  benefician  o  perjudican  al jugador, agregando

una  interfaz  para  seleccionar  un  monto  exclusivamente  para  la  casilla de

inversión.  Además  del  desarrollo  del  sistema  de  preguntas  usando  el

mismo  mecanismo  de  tarjetas  para las opciones, con ello demostrando el

conocimiento  teórico,  obteniendo  puntaje  y  un  dado  para  lanzar  al

responder correctamente.

RF

RNF

RF_001, RF_007, RF_008, RF_009, RF_010

RNF_001, RNF_002, RNF_003

El  tercer  prototipo  estableció  las bases para el sistema de casillas que el jugador

activa  al  posicionarse  sobre  una.  Al  activarse  una  casilla  se  presenta  al  jugador  una  o  más

tarjetas que representan situaciones que impactan en las finanzas del jugador de forma positiva

o  negativa.  Durante  su  desarrollo  se  crearon  las  diferentes  casillas  que  tendrá  el  tablero  de

juego. En esta iteración, se generó:

●  Casilla  de  ingreso:  se  presenta  al  jugador  una  situación  que  lo  beneficia

financieramente, obteniendo una suma de dinero o aumentando su salario.

●  Casilla  de  gasto:  se  presenta  al  jugador  una  situación  que  lo  perjudica

financieramente,  desembolsando  dinero  por  un  monto  fijo  o  adquiriendo  un

gasto recurrente de dinero por n años(turnos).

●  Casilla  de evento: se presenta a los jugadores una situación que impacta en

sus finanzas, ya sea a favor o en contra.

38

●  Casilla  de  inversión:  se  presenta  al  jugador  una  serie  de  oportunidades  de

inversión,  de  las  cuales  debe  decidir  si  tomar  o  pasar,  impactando  en  sus

finanzas de forma positiva o negativa.

Figura 4.4: Casilla de inversión.

Fuente: elaboración propia, 2024.

También  utilizando  el  mismo  mecanismo  de  cartas  de  las  casillas  se  creó  un

sistema que presenta al jugador una pregunta relacionada a las finanzas, mostrando diferentes

opciones  de  las  cuales  una  es  correcta,  otorgando  puntaje  a  aquellos  que  respondan  bien  y

permitiendo el lanzamiento del dado para avanzar por el tablero. De este modo se representa el

conocimiento  financiero  teórico  del  jugador  a  través  de  su  puntaje,  adquiriendo  ciertos

beneficios cuanto mayor sea, como mejor tasa de interés, mejores oportunidades, entre otros.

39

Figura 4.5: Sistema de preguntas.

Fuente: elaboración propia, 2024.

Su evaluación se realizó mediante pruebas funcionales centradas en la activación

de  las  diferentes  casillas  y  la  interacción  con  su  interfaz.  Se  verificó  que  cada tipo de casilla

presentará  sus  correspondientes

tarjetas  y  que  el  sistema  de  preguntas  respondiera

correctamente a la selección del jugador, asignando su correspondiente puntaje.

40

4.2.4. Prototipo 4: menú de inicio

Tabla 4.7: Resumen del prototipo menú de inicio.

Fuente: elaboración propia, 2024.

ID prototipo

P04

Objetivo

Implementar  un menú inicial para navegar por las diferentes opciones que

ofrece el juego.

Descripción

El  menú  desarrollado  cuenta  con  apartados  para  las  configuraciones  del

juego, perfil del usuario, contenido descargable y modos de juego.

RF

RNF

RF_011, RF_016

RNF_001, RNF_002, RNF_003

El  desarrollo  del  cuarto  prototipo  permitió  presentar  y  navegar  por  las  diferentes

funcionalidades que ofrece el juego. En esta iteración, se generó:

●  Menú  inicio:  apartado  inicial  mostrado  al  ejecutar,  presenta  las  opciones  de

menú  iniciales:  juego,  contenido,  opciones,  perfil.  Agregando  la  opción  para

cerrar el juego.

●  Menú contenido: apartado para ver los contenidos disponibles local y online.

●  Menú  opciones:  apartado  para las configuraciones del juego, como volumen,

tamaño vista, entre otros.

●  Menú  perfil:  apartado  para  el  perfil  del  usuario,  presentando  su  información

permitiendo  modificarla,  además  de  su  historial  de  partidas  y  opcionalmente

conexión con bGames.

●  Menú  de  juego:  apartado  para  escoger  el  modo  de  juego,  siendo  estos:  un

jugador, multijugador local y multijugador en línea.

●  Menu lobby: apartado para la conexión y gestión de jugadores para la partida.

Estos  menús  permiten  al  jugador  navegar  de  manera  clara  y  fluida  por  los

mecanismos dispuestos por el juego para la creación de partidas y configuración del mismo.

41

Figura 4.6: Menú inicial.

Fuente: elaboración propia, 2024.

La  evaluación  de  este  prototipo  se  realizó  mediante  pruebas  de  navegación,

comprobando  la  correcta  transición  entre  las  distintas  secciones  del  menú  y  verificando  que

cada una muestre su correspondiente información.

42

4.2.5. Prototipo 5: sistema de guardado

Tabla 4.8: Resumen del prototipo perfil de usuario.

Fuente: elaboración propia, 2024.

ID prototipo

P05

Objetivo

Implementar un sistema de guardado para la reanudación de partidas

Descripción

El  sistema  de  guardado  almacena  los  datos  de  la partida en curso en un

archivo  .json,  el  cual  es  encriptado  y  guardado  automáticamente  durante

las sesiones de juego, existiendo un único archivo por modo de juego.

RF

RNF

RF_004, RF_012, RF_016

RNF_001, RNF_003

Este quinto prototipo permite a los jugadores interrumpir o detener sus sesiones de

juego  sin  la  necesidad  de  mantenerlo  ejecutándose  y  consumiendo  recursos,  pues  con  este

sistema se guardan los datos de la partida automáticamente mientras juegas en un archivo .json

encriptado, permitiendo cerrar la instancia de juego y reanudar la sesión en cualquier momento

o eliminarla para comenzar una nueva.

Este  sistema  cuenta  con  2  archivos  de  guardado,  funcionando  únicamente  para

modalidades locales, siendo estos: un jugador, multijugador local. En caso de existir una partida

en curso guardada se presenta al jugador la opción de reanudar la sesión de juego o crear una

nueva  partida  eliminando  la  anteriormente  en  curso.  Además,  al  concluir  en  su  totalidad  una

partida, será borrado automáticamente su archivo de guardado correspondiente.

43

Figura 4.7: Popup reanudación de partida.

Fuente: elaboración propia, 2024.

Su  evaluación  consistió  en  pruebas  funcionales  en  las  cuales  se  interrumpieron

partidas en distintos puntos del juego para verificar la correcta persistencia y restauración de los

datos.  Además,  se  comprobó  que  el  archivo  .json  estuviera  correctamente  encriptado  para

evitar su fácil lectura.

44

4.2.6. Prototipo 6: historial de partidas

Tabla 4.9: Resumen del prototipo historial de partidas.

Fuente: elaboración propia, 2024.

ID prototipo

P06

Objetivo

Implementar  un  sistema  de  historial  para  las  partidas  terminadas  en  su

totalidad.

Descripción

El  historial  de  partidas  es  un  registro  histórico  de  todos  los  juegos

concluidos  por  el  usuario  (jugador  principal). Guardados en archivos .json

personalizados y encriptados.

RF

RNF

RF_004, RF_013, RF_016

RNF_001, RNF_003

El  sexto  prototipo  añade  la  funcionalidad  de  almacenar  y  revisar  el  historial  de

partidas  finalizadas.  Al  concluir  un  juego,  se  genera  automáticamente  un  archivo  .json

encriptado con los datos de la partida concluida, siendo estos datos: años jugados, nombre del

contenido, fecha finalización, duración del juego y puntaje final. El .json correspondiente a este

archivo de guardado se encuentra en el Apéndice B.2.

Con  este  sistema  el  usuario  puede  revisar  y  analizar  sus  partidas  anteriores  en

cualquier  momento,  sin  riesgo  de  sobrescribir  o  perder  información  de  los juegos concluidos.

Además, se complementa el prototipo de sistema de guardado para las partidas en curso, en el

cual al finalizar se elimina dicha sesión pues se transfiere el juego al historial.

45

Figura 4.8: Registro de partidas finalizadas.

Fuente: elaboración propia, 2024.

Ademas, cabe mencionar que el sistema de este prototipo almacena el perfil y las

partidas únicamente de forma local, por lo que si se desea transferir los datos a otro dispositivo

o  si  se  desea  formatear  el  computador,  se  debe  realizar  una  copia  de  respaldo  de  forma

manual.

La evaluación de este sistema se llevó a cabo mediante la finalización de múltiples

partidas  distintas,  verificando  la  correcta  generación  del  archivo  de  guardado  y  su  correcta

encriptación. Se revisó también su correcta lectura y visualización en la interfaz, comprobando

que no exista archivos duplicados ni sobrescritura de las partidas terminadas.

46

4.2.7. Prototipo 7: integración de bGames

Tabla 4.10: Resumen del prototipo de integración de bGames.

Fuente: elaboración propia, 2024.

ID prototipo

P07

Objetivo

Implementar  el  perfil  multidimensional  de  bGames  en  las  mecánicas  del

juego.

Descripción

Conexión   del  perfil  de  bGames  para  el  consumo  de puntos por ventajas

adicionales que modifican mecánicas base del juego.

RF

RNF

RF_0014, RF_016

RNF_001, RNF_003, RNF_004, RNF_005

El séptimo prototipo agrega la posibilidad de conectar el perfil multidimensional del

usuario  en  el  framework  de  bGames.  Al  conectarlo  el  usuario  visualizará  dicha conexión y el

puntaje  que  posee  para  utilizar  dentro  del  juego.  Los  puntos  visualizados  y  que  se  permiten

consumir, pertenecen a la dimensión cognitiva, debido a que es la dimensión se relaciona con el

atributo de conocimientos financieros el cual conforma a la alfabetización financiera.

Figura 4.9: Conexión con bGames.

Fuente: elaboración propia, 2024.

47

Durante  las  sesiones  de  juegos, cada que es turno del jugador se le presenta un

pregunta  que  pone  a  prueba  sus  conocimientos  en el contenido seleccionado para la partida,

por  cada  turno el jugador cuenta con 2 intentos para responder, al responder erróneamente la

pregunta  es  cambiada  por  otra  de  la  misma  area  o  temática,  si  responde  en ambos intentos

erróneamente se termina su turno sin la posibilidad de avanzar.

Pero  en  caso  de  conectar  el  perfil  de  bGames  y  de  contar  con  puntos  para

consumir,  tras  responder  erróneamente  y  perder  sus  2  intentos  se  le  ofrece  la  opción  de

consumir  uno  de  sus  puntos  de  bGames  por  un  intento  extra.  Al  canjear  este  intento  podrá

volver a afrontar una pregunta del área, para de este modo avanzar si responde correctamente

o perder su turno si se equivoca nuevamente.

Figura 4.10: Popup de canjeo de puntos bGames.

Fuente: elaboración propia, 2024.

Esto  otorga  una  ventaja  extra a los jugadores que conectan su perfil, volviendo a

bGames un atractivo interesante de utilizar por los jugadores, pero sin ser una ventaja excesiva

que  desbalancee  el  juego  o  que  vaya  en  contra  del  objetivo  de  aprendizaje.  Para  no

desbalancear partidas en línea, bGames solo es funcional para partidas locales.

Su evaluación se realizó mediante la conexión del perfil del usuario de bGames y la

ejecución  de  múltiples  partidas  locales.  En  ellas  se  verificó  la  correcta  visualización  de  los

puntos  actuales  de  bGames  y  su  correcto  canje,  permitiendo  un  intento  adicional  para

responder y restando un punto al perfil de bGames.

48

4.2.8. Prototipo 8: multijugador en línea

Tabla 4.11: Resumen del prototipo multijugador en línea.

Fuente: elaboración propia, 2024.

ID prototipo

P08

Objetivo

Implementar la modalidad de juego en línea para hasta 4 jugadores.

Descripción

Se emplea la librería Mirror para configurar el servidor en el dispositivo (PC)

de  uno  de  los  jugadores,  que  actúa  como  host  (cliente  +  servidor).  A  su

vez,  se  integra  Unity  Relay  como  servicio  en  la  nube  para  gestionar  las

conexiones y facilitar la comunicación entre host y clientes.

RF

RF_001,  RF_002,  RF_003,  RF_004,  RF_005,  RF_006,  RF_007,  RF_008,

RF_009

RNF

RNF_001, RNF_002, RNF_003

Este  octavo  prototipo  hace  uso  de  la  librería  Mirror para implementar un entorno

multijugador  con  arquitectura  cliente-servidor,  en el cual uno de los jugadores asume el rol de

host, alojando y participando en la partida de manera simultánea.

Para  facilitar  la  conexión  de  los  demás jugadores sin requerir configuraciones de

puertos  o  exponer  la  IP  del  host,  se  incorporó  el  servicio  Unity  Relay,  que  actúa  como

intermediario  en  la nube. De este modo, Unity Relay administra las conexiones, estableciendo

rutas  seguras  y  directas  entre  los  dispositivos,  lo que elimina la necesidad de realizar ajustes

avanzados  de  red  (por  ejemplo,  NAT  punchthrough  o  reenvío  de  puertos).  Esto,  a  su  vez,

garantiza una experiencia de juego fluida y accesible para todos los participantes.

Una vez establecida la conexión, fue necesario adaptar el código existente para la

arquitectura  cliente-servidor,  puesto  que  en  un  juego  local  todos  los  eventos  ocurren  en  un

mismo  dispositivo.  En  contraste,  en  un  juego  en  línea,  cada  acción  realizada  por  un  jugador

debe  ser comunicada y autorizada por el servidor (host), quien posteriormente notifica a todos

los participantes para que sincronicen los cambios de manera simultánea, tal como se ilustra en

la Figura 4.11. Esto garantiza la coherencia de la partida y evita discrepancias entre los clientes.

49

Figura 4.11: Arquitectura host-cliente con unity relay.

Fuente: elaboración propia, 2024.

La  evaluación de este prototipo se llevó a cabo mediante la ejecución de partidas

multijugador  en  línea  con  distintos  dispositivos,  tanto  en  una  misma  red  local como en redes

diferentes.  Durante  estas  sesiones  se  comprobó  la  correcta  conexión  entre  el  host  y  sus

clientes,  la  sincronización  de  eventos  en  tiempo real y el correcto funcionamiento del flujo del

videojuego.  A  través  de  estas  pruebas  se  detectaron  errores  de  sincronización,  los  cuales

fueron corregidos para asegurar la estabilidad de la conexión y la integridad del juego en línea.

50

4.2.9. Prototipo 9: sensor blended games

Tabla 4.12: Resumen del prototipo de sensor blended games.

Fuente: elaboración propia, 2024.

ID prototipo

P09

Objetivo

Implementar un sensor para la capturas de datos financieros normalizados

a puntos de bGames

Descripción

Se crea un sensor para capturar el porcentaje de cumpliento de las metas

de ahorro establecidas en la plataforma de Final normalizadas a puntos de

bGames  perteneciente  a

la  dimensión  cognitiva  y  al  atributo  de

alfabetización financiera.

RF

RNF

RF_014, RF_015

RNF_001, RNF_004

El noveno y último prototipo generado busca alimentar el perfil multidimensional de

bGames  con  datos  del  entorno  financiero  del  usuario  obtenidos  mediante  sus  llamados

sensores. Se considera como un posible sensor a toda aplicación, API o plataforma que permita

obtener  información  del  entorno  del  usuario.  Con  esta  finalidad,  se  revisaron  múltiples

propuestas  para  obtener  información  de  sus  usuarios,  tales  como  apps  de  gestión de gastos

(Wallet  Budget,  YNAB),  plataformas  de  cursos  financieros  (Coursera),  plataformas  de  fondos

ahorro (Fintual).

De lo revisado, las apps de gestión de gasto que contaban con APIs no resultaban

lo suficientemente robustas para realizar un análisis de sus datos y además resultan muy fáciles

de  manipular  al  ser  los  mismos  usuarios  quienes  generan  sus  registros.  En  cuanto  a  las

plataformas  de  cursos  se  revisó  la  de  Udemy  la  cual  su  API  de  usuarios  quedó  obsoleta  en

Enero  del  2025  y  la  de  Coursera  solo  era  para  organizaciones  o  empresas,  por  lo  que  se

terminaron descartando.

Finalmente,  se  optó  por  la  API  de  la  plataforma  chilena  Fintual,  la  cual  permite

invertir en diferentes fondos de ahorro y acciones en la bolsa de Estados Unidos. En particular,

se  enfocó  en  los  fondos de ahorro los cuales utilizan la funcionalidad de “Objetivos”, donde el

usuario  puede  establecer  un  monto  de  depósito  mensual  al  crearlo  (sin  posibilidad  de

51

modificarlo  posteriormente).  A  partir  de  esta  información,  la  API  expone  los  datos  de  dichos

objetivos los cuales se utilizan para calcular el porcentaje de cumplimiento de la meta de ahorro

durante  el  mes  en curso, lo que se normaliza en forma de puntos bGames, asignados al área

cognitiva  y  al  atributo  de  alfabetización  financiera.  De  este  se  premia a quienes cumplen sus

metas de ahorro independientemente del monto asignado, pues se premia al hábito y no al valor

depositado.

Figura 4.12: Objetivo en Fintual.

Fuente: elaboración propia, 2024.

  Para  conectarse  con  la  API  y  obtener  puntos  de  bGames,  se  implementó  un

sensor  donde el usuario ingresa sus credenciales de Fintual; así, se obtiene y almacena en la

base de datos de bGames el token para consultar dicha API. Con ello, se accede a los objetivos

del usuario, se calcula el porcentaje de ahorro del mes y se convierte automáticamente a puntos

de  bGames  sin  almacenar  información  sensible  sobre  saldos.  El  sensor  permite  “reclamar”

estos puntos una vez al mes, asumiendo que el ahorro se realiza tras recibir el salario.

Para probar este sensor, se desarrolló temporalmente una aplicación de escritorio

con  Vue  y  Electron,  dado  que  Vue  es  el  mismo  framework  utilizado  en  la  aplicación web del

52

módulo  cloud  (actualmente  inoperativo).  De  esta  manera,  cuando  el  módulo  cloud  vuelva  a

estar desplegado, se podrá integrar el sensor de Fintual sin mayores complicaciones.

Figura 4.13: Aplicación de escritorio para sensor de Fintual.

Fuente: elaboración propia, 2024.

La  evaluación  de  este  último  prototipo  se  realizó  mediante  la  aplicación  de

escritorio desarrollada, en la cual se verificó la conexión con el perfil de bGames y la asociación

con  la  cuenta  de  Fintual.  Durante  esta  prueba  se  comprobó  el  correcto  almacenamiento  del

token  para  las  solicitudes a la API de Fintual, así como el cálculo adecuado del porcentaje de

ahorro y la correcta obtención y registro de los puntos.

4.3. RESUMEN

En  este  capítulo  se  presentaron  en  detalle  todos los requerimientos identificados

para el proyecto, tanto los funcionales como los no funcionales. El objetivo fue asegurar que el

resultado final cumpla con las necesidades de los usuarios y respete los estándares de calidad

establecidos (rendimiento, usabilidad, fiabilidad, etc.).

Además,  se  describieron  los  diferentes  prototipos  desarrollados  durante  la  fase

inicial del proyecto, cada uno acompañado de una tabla resumen que especifica su ID, objetivo,

descripción  y  los  requerimientos  (funcionales  y  no  funcionales)  implicados.  Dichos  prototipos

53

muestran  la  evolución  del  proyecto,  desde  aspectos  básicos  como  la  gestión  de  perfiles  y  el

guardado  de  partidas,  hasta

funcionalidades  más  complejas  como  la  habilitación  de

multijugador en línea y la integración de bGames.

Por último, se exponen de manera global los requerimientos que fueron trabajados

o perfeccionados en cada prototipo. De este modo, se proporciona una visión general de cómo

cada prototipo fue sumando nuevas funcionalidades o refinando lo ya construido.

Tabla 4.13: Resumen de prototipos y requerimientos funcionales abarcados.

Fuente: elaboración propia, 2024.

Requerimiento

P01

P02

P03

P04

P05

P06

P07

P08

P09

/Prototipo

RF_001

RF_002

RF_003

RF_004

RF_005

RF_006

RF_007

RF_008

RF_009

RF_010

RF_011

RF_012

RF_013

RF_014

RF_015

RF_016

X

X

X

X

X

X

X

X

X

X

X

X

X

X

X

X

X

X

X

X

X

X

X

X

X

X

X

X

X

X

X

X

X

X

54

Tabla 4.14: Resumen de prototipos y requerimientos no funcionales abarcados.

Fuente: elaboración propia, 2024.

Requerimiento/

P01

P02

P03

P04

P05

P06

P07

P08

P09

Prototipo

RNF_001

RNF_002

RNF_003

RNF_004

RNF_005

X

X

X

X

X

X

X

X

X

X

X

X

X

X

X

X

X

X

X

X

X

X

X

X

55

CAPÍTULO 5. DISEÑO E IMPLEMENTACIÓN

En  este  capítulo  se  presenta  la  implementación  del  proyecto  del  videojuego,

detallando los elementos más importantes que constituyen su arquitectura. Además, se explora

la  implementación  final  de  las  funcionalidades  diseñadas  en  el  GDD  y  evaluadas  durante  la
etapa de prototipado.

5.1. ARQUITECTURA

En  esta  sección  se  detalla la arquitectura del software desarrollado, revisando su

integración  con  Blended  Games  y  explorando  sus  diferentes  vistas,  que  son:  de  desarrollo,

lógica, de proceso, física y de escenario.

5.1.1. Arquitectura de software con Blended Games

La  solución  propuesta  por el proyecto se encuentra constituida por un videojuego

serio,  WealthQuest,  que  forma  parte  de  una  arquitectura  que  incluye  una  base  de  datos

relacional  en  MySQL,  la  cual  se  accede  y  modifica  a  través  del  módulo  cloud  de  bGames,

compuesto  actualmente  por  diez  microservicios  desarrollados  en  Node.js.  Esta  estructura

conforma la arquitectura de la solución, representada en la Figura 5.1.

Figura 5.1: Diagrama conceptual de la solución.

Fuente: elaboración propia adaptado de Ternero (2022), 2024.

56

A continuación se detallan los elementos presentados en el diagrama:

●  Videojuego  serio  (WealtQuest):  videojuego  desarrollado  utilizando  el  motor

de  desarrollo  Unity,   seleccionado  debido  a  su  versatilidad  para  crear

videojuegos  multiplataforma  y  su  capacidad  para  proyectos

tanto

independientes  como  de  mayor  escala  (AAA).  Asimismo,  el  laboratorio

Interaction  Lab  cuenta  con  trabajos  previos  realizados  con  este  motor,  los

cuales  sirven  como  referencia  y  guía  para  el  desarrollo  del  proyecto.  Cabe

destacar que la comunicación del videojuego con los microservicios del módulo

cloud se realiza mediante su API REST, garantizando una interacción eficiente

y estructurada

●  Módulo  cloud:  entorno  desarrollado  en  Node.js,  el  cual  es  un  sistema

heredado que actualmente opera de manera local, ya que no está desplegado

en  la  nube.  El  módulo  incluye  diez microservicios que permiten la interacción

con  el  perfil  multidimensional  del  usuario  en  Blended  Games,  así  como  la

obtención y consumo de puntos asociados al jugador.

●  Base de datos relacional (MySQL): base de datos heredada y reconstituida a

partir del trabajo Zelada (2023), con la incorporación de datos específicos para

la  obtención  de  puntos  a  través  del  sensor  de  Fintual  y  para  el  consumo de

puntos dentro del videojuego serio WealthQuest.

5.1.2. Vista de desarrollo: organización de recursos

Si  bien no existe una organización estándar para los proyectos en Unity, estos se

gestionan mediante los diversos recursos que ofrece el motor para la creación de videojuegos,

los cuales se pueden agrupar según sus componentes, como se muestra en la Figura 5.2.

57

Figura 5.2: Diagrama de recursos del proyecto.

Fuente: elaboración propia, 2024.

Si bien los recursos utilizados varían según cada proyecto, es importante describir

de manera general cada recurso para comprender su utilidad e importancia:

●  Animation:  recursos  utilizados  para  animar  personajes,  objetos  y  otros

elementos del juego como clips (.anim), controladores (.controller) y máscaras

de animación (.mask).

●  Audio:  sonidos  utilizados  en  el  juego,  desde música hasta efectos sonoros y

diálogos (.mp3, .wav, .ogg).

●

Input:  entrada  del  jugador,  incluyendo  mapeos  para  teclas  y  mandos.  Los

recursos incluyen archivos de entrada (.inputactions).

●  Material:  renderizado  de  las  superficies  de  los  objetos,  controlando texturas,

colores, brillo y más (.mat).

●  Model:  modelos  3D  del  juego,  como  personajes  y  estructuras.  Los  formatos

comunes son (.fbx, .obj, .dae).

●  Object:  prefabricados  reutilizables  que  pueden  ser  objetos  normales  o  de  la

interfaz  (Canvas),  así  como  Scriptable  Objects  para  almacenar  datos

persistentes o configuraciones. Recursos en formato (.prefab, .asset).

58

●  Resources:  recursos  cargados dinámicamente en tiempo de ejecución, como

texturas, sonidos o configuraciones (.png, .txt, .json, .asset).

●  Scene:  niveles  o  estados  del  juego.  Cada  escena  gestiona luces, cámaras y

objetos del entorno (.unity).

●  Scripts:  código  fuente  del  proyecto  para  la  lógica  del  juego,  interfaz  y  otros

sistemas en C#. Recursos en (.cs).

●  Sprite: gráficos 2D utilizados en interfaces o ambientaciones (.png, .jpg, .svg).

●  StreamingAssets:  datos  accesibles  sin  compresión  durante  el  juego,  como

vídeos o configuraciones externas (.mp4, .txt, .json).

●  Timeline:  secuencias  para  eventos  animados  o  cinemáticas  del  juego

(.playable, .asset).

Para  el  desarrollo  de  la  solución,  el  proyecto  se  organizó  en  distintas  carpetas

dentro  de  la  carpeta  Assets,  con  el  objetivo  de  optimizar  la  gestión  y  la  navegación  de  los

recursos, como se muestra en la Figura 5.3.

Figura 5.3: Diagrama de organización de recursos del proyecto.

Fuente: elaboración propia, 2024.

59

5.1.3. Vista lógica: diagrama de clases

El  diagrama  de  la  Figura  5.4  muestra  los  principales  objetos  involucrados  en  el

funcionamiento de una partida, facilitando la comprensión de sus relaciones y dependencias.

Figura 5.4: Diagrama clases de los objetos principales en una partida.

Fuente: elaboración propia, 2024.

5.1.4. Vista de proceso: diagrama de secuencia

La  Figura  5.5  muestra  la  secuencia  de  procesos  dentro  del  sistema  durante  la

primera  conexión  al  juego,  permitiendo  al  jugador  vincular  su  perfil  de  bGames  e  iniciar  una

60

partida.  Para  simplificar,  se  considera  que MenuManager representa a todos los objetos de la

interfaz.

Figura 5.5: Diagrama de secuencia primera conexión.

Fuente: elaboración propia, 2024.

5.1.5. Vista física: diagrama de despliegue

El  diagrama  de  la  Figura  5.6  representa  la  relación  entre  el  usuario,  la  solución

desarrollada,  el  módulo  cloud  local  de  bGames  y  la  conexión  con  Firebase  para  una  mejor

comprensión de su despliegue.

61

Figura 5.6: Diagrama de despliegue.

Fuente: elaboración propia, 2024.5.1.6. Vista de escenarios: casos de uso

A  continuación  se  presentan  tres  diagramas  que  ilustran  la  forma  en  que  los

usuarios  interactúan con la solución desarrollada durante su interacción con el menú principal,

durante una partida y dentro de la aplicación de escritorio para conectar el sensor de Fintual.

1.

Interacción del usuario durante su turno en el transcurso de una partida.

62

Figura 5.7: Diagrama de caso de uso durante la partida.

Fuente: elaboración propia, 2024.

2.

Interacción del usuario con el menú principal del videojuego.

Figura 5.8: Diagrama de caso de uso en menú principal.

Fuente: elaboración propia, 2024.

63

3.

Interacción  del  usuario  dentro  de  la  aplicación de escritorio para la obtención

de puntos bGames a través del sensor de Fintual.

Figura 5.9: Diagrama de caso de uso en aplicación para sensor Fintual.

Fuente: elaboración propia, 2024.

5.2. IMPLEMENTACIÓN

En  este  apartado  se  detallan  los  aspectos  más  relevantes  de  la  solución

desarrollada, detallando su funcionamiento lógico, flujo e importancia.

5.2.1. Flujo general del juego

El  flujo  de  juego  que  cada  jugador  debe  seguir  durante  su  turno  ilustrado  en  la

Figura 5.10 , se conforma de 3 acciones principales: responder pregunta, lanzar dado (saltar) y

recoger  tarjeta.  Este  flujo  permite  un  experiencia  de  juego  simple  y  fácil de comprender para

cada jugador, contando además con guías visuales que lo apoyan.

64

Figura 5.10: Diagrama de turno del jugador.

Fuente: elaboración propia, 2024.

La  primera  acción  que debe realizar un jugador cuando es su turno es responder

una pregunta. Esta pregunta es escogida del conjunto de preguntas pertenecientes al contenido

seleccionado para la partida, siendo una que no haya sido respondida correctamente y acorde

al  nivel  actual  del  jugador  en  la  partida.  El  nivel  del  jugador  toma  como  base  inicial  el  nivel

financiero del perfil del usuario en partidas locales para comenzar con preguntas acordes a su

perfil  actual,  mientras  que  en  partidas  en  línea  todos  empiezan  en  nivel  1  para  balancear  el

comienzo,  y  aumenta  temporalmente  en  el  transcurso  de  la  partida  a  medida  que  obtiene

puntos financieros al responder correctamente, hasta alcanzar el nivel máximo.

En cada turno, el jugador cuenta con dos intentos para responder preguntas de su

nivel,  con  la  posibilidad  de expandirse a tres intentos si utiliza bGames en partidas locales. Al

iniciar  su  turno,  se  presenta  la  pregunta  con  tres  posibles  respuestas,  de  las  cuales  una  es

correcta.  Si  responde  incorrectamente,  pierde un intento y se le presenta una nueva pregunta

del mismo nivel. Si se le acaban los intentos, el jugador termina su turno sin avanzar. En caso

65

de responder correctamente, obtiene puntos financieros de acuerdo con el nivel de la pregunta

y  se  le  habilita  el  dado  para  avanzar.  En  la  Figura  5.11  se  puede  apreciar  esta  interfaz  de

preguntas.

Figura 5.11: Interfaz de pregunta.

Fuente: elaboración propia, 2024.

Tras  responder  la  pregunta  correctamente,  se  le  presenta  al  jugador  un dado, el

cual  puede  detener  ejecutando  la  acción  de  salto,  avanzando  las  casillas  equivalentes  al

número obtenido, tal como se muestra en la Figura 5.12.

Figura 5.12: Interfaz del dado.

Fuente: elaboración propia, 2024.

66

Por último, tras lanzar el dado y ejecutarse el movimiento, el jugador se detiene en

una  casilla,  la  cual  le  presenta  dos  tarjetas  a  escoger,  que  pueden  ser  de  ingreso,  egreso,

evento o inversión. Estas tarjetas pueden modificar de diferentes maneras el capital del jugador,

ya sea aumentando o disminuyendo su dinero, inversión, deuda, ingreso por turno o egreso por

turno. Las tarjetas mencionadas se ilustran en la Figura 5.13.

Figura 5.13: Interfaz de selección de tarjeta.

Fuente: elaboración propia, 2024.

5.2.2. Administración de partidas

El  sistema  de  partidas  del  videojuego  se  diseñó  de  forma  que  el  jugador  pueda

interrumpir su sesión de juego sin perder el progreso actual de su partida. Durante una sesión,

cada que se finaliza un turno el sistema guarda automáticamente el progreso de la partida hasta

dicho momento, de esta forma el jugador puede reanudarla en cualquier momento.

El progreso de cada partida almacena los datos esenciales en binario a través de

un  archivo  .json,  el  cual  es  modificado  y encriptado resultando en uno de extensión .save, tal

como  se  muestra  en  el  Código  5.1.  Estos  archivos  se  almacenan  en

la  carpeta

InTeractiOn/WealthQuest/Saves  ubicada  en  persistent  Data  Path  (en  Windows  es  la  carpeta

LocalLow).  De  esta  manera,  se  ocultan  los  datos  de  la  partida,  evitando  el  acceso  a  las

respuestas  de  las  preguntas  por  parte  de  los  usuarios.  El  sistema  es  el  encargado  de

desencriptar los datos para reanudar la sesión.

67

private static byte[] EncryptStringToBytes_Aes(string plainText)
{
    byte[] encrypted;
    using (Aes aesAlg = Aes.Create())
    {
        aesAlg.Key = aesKey;
        aesAlg.IV = aesIV;
        ICryptoTransform encryptor = aesAlg.CreateEncryptor(aesAlg.Key,
        aesAlg.IV);
        using (MemoryStream msEncrypt = new MemoryStream())
        {
            using (CryptoStream csEncrypt = new CryptoStream(msEncrypt,
            encryptor, CryptoStreamMode.Write))
            {
                using (StreamWriter swEncrypt = new
                StreamWriter(csEncrypt))
                {
                    swEncrypt.Write(plainText);
                }
                encrypted = msEncrypt.ToArray();
            }
        }
    }
    return encrypted;
}

Código 5.1: Funcionalidad de encriptado.

Fuente: elaboración propia, 2024.

Este  sistema  permite  2  archivos de guardado: modo solitario y multijugador local.

Cada  que  se  detecta  la  existencia  de  uno  de  estos  archivos  se  consulta  al  jugador  si desea

reanudar  la  partida  o  comenzar  una  nueva,  eliminando  el  progreso  de  la  partida  guardada

anteriormente si se encoje la segunda opción.

Además  de  guardar  partidas en curso, el sistema también almacena los datos de

aquellas  partidas  finalizadas,  conocido  como el historial de juegos. Similar al sistema anterior,

cada que se finaliza en su totalidad una partida, el sistema encripta y almacena sus datos en un

archivo  de  extensión  .save,  pero  esta  vez  en  la  carpeta  InTeractiOn/WealthQuest/History.  De

esta  manera  el  jugador  puede  visualizar  el  registro  completo  de  sus  partidas,  permitiendo

comparar su progreso a lo largo del tiempo y el tiempo de juego dedicado para cada sesión.

68

Además cada que se termina una partida, el jugador obtiene puntos de experiencia

en  base  a  su  puntaje  final  y  se  actualiza  las  métricas  del  jugador:  puntaje  promedio,  mejor

puntaje y número de partidas finalizadas. Todo lo anterior puede ser visualizado a través de la

interfaz Perfil del videojuego ilustrado en la Figura 5.14.

Figura 5.14: Interfaz perfil.

Fuente: elaboración propia, 2024.

Cabe destacar que el videojuego ahora cuenta con un sistema de registro e inicio

de  sesión  de  usuarios  mediante  Firebase  Authentication,  el  cual  requiere  conexión  a internet

solo  la  primera  vez  que  se  crea  o  accede  a  un usuario. Además, los datos del perfil de cada

jugador  y  su  historial  de  partidas  se  guardan  de  forma  local  y  se  respaldan  de  manera

asincrónica  en  Firebase  Firestore  Database  cuando  se  detecta  conexión  a  internet.  Esto

garantiza  que

la

información  esté  siempre  disponible

localmente  y  se  sincronice

automáticamente con su respaldo en la nube.

5.2.3. Obtención de puntos de bGames

Además del videojuego desarrollado, se utiliza el entorno heredado del framework

Blended Games (bGames) para integrar su perfil multidimensional y modificar mecánicas base

del videojuego.

69

El perfil de usuario de bGames cuenta con puntos asociados a cinco dimensiones

principales:  Social,  Física,  Afectiva,  Cognitiva  y  Lingüística. Estos puntos se generan a través

de  sensores,  sistemas  que  recopilan  información  del  entorno  del  usuario  y  la  normalizan  en

puntos bGames pertenecientes a alguna de estas dimensiones.

En el caso del videojuego desarrollado, al ser un juego serio educativo centrado en

la  alfabetización  financiera,  los  puntos  obtenidos  y  consumidos  se  enfocan  en  la  dimensión

cognitiva. Para ello, se desarrolló un sensor específico que captura información relacionada con

los hábitos de ahorro del usuario. Tras revisar diversas opciones, se optó por utilizar la API de

Fintual  para  recopilar  métricas  de  ahorro,  dado  que  estas  ofrecen  un  indicio  claro  del

comportamiento  financiero  del  jugador,  un  rasgo  clave  para evaluar su nivel de alfabetización

financiera.

Dentro  de  la plataforma de Fintual, los usuarios pueden crear diferentes objetivos

de ahorro y definir montos de depósito mensual asociados a cada uno. Este monto representa

una  meta  mensual  que  el  usuario  se  propone  cumplir. El sensor desarrollado se conecta a la

API  de  Fintual  para  calcular  el  porcentaje  de  cumplimiento  de  estas  metas,  otorgando  una

mayor  cantidad  de  puntos  a  aquellos  jugadores  que  estén  más  cerca  de  cumplirlas.  Esto

asegura  que  se  premie  el  hábito  de  ahorro  constante  y  no  exclusivamente  la  cantidad

depositada.

El  sensor  calcula  el  porcentaje  de  cumplimiento  de  la meta mensual mediante la

siguiente función:

70

Función getSavingsPercentage(email, token):
INICIO
    // Obtener objetivos de ahorro
    goals[1 .. n] = getGoals(email, token);
    // Inicializar meta y monto depositado total
    totalGoalSavings = 0;
    totalDeposited = 0;
    nGoals = n;

    MIENTRAS (nGoals > 0)
        // Obtener meta y monto depositado por objetivo
        goalSaving = getSaving(goals[n])
        goalDeposited = getDeposited(goals[n])
        // Sumar montos al total
        totalGoalSavings +=  goalSaving;
        totalDeposited += goalDeposited;
        nGoals--;
    FIN_MIENTRAS

    // Obtener porcentaje de cumpliento demeta
    percentage = totalDeposited / totalGoalSavings;
FIN

Código 5.2: Cálculo de porcentaje de cumpliento de meta mensual.

Fuente: elaboración propia, 2024.

La  API  de  Fintual  se  utiliza  mediante un token generado tras la autenticación del

usuario. Este enfoque garantiza que no se almacenen credenciales ni información confidencial

como  saldos.  El  sensor  únicamente  utiliza  los  datos  necesarios  para  calcular  los  hábitos  de

ahorro del usuario y convertirlos en puntos para bGames.

Con  esta  integración,  se  fomenta  el  hábito  de  ahorro  y  refuerza  la  dimensión

cognitiva  del  perfil  del  jugador,  vinculando las métricas financieras reales con una experiencia

educativa personalizada.

5.2.4. Conexión con bGames y consumo de puntos

Para  conectar  el  perfil  de  bGames  y  consumir  los  puntos  obtenidos  en  el

videojuego,  se  utiliza  la  clase  UnityWebRequest  de  Unity,  la cual permite consultar y manejar

respuestas HTTP. Con esta herramienta se facilitan las consultas e intercambio de información

con los diferentes microservicios del módulo cloud de bGames, actualmente trabajado de forma

71

local.  Para  conexión  y  consumo  de  puntos  de  bGames  se  utilizaron  cuatro  microservicios:

userService, getService, sensorService y spendService, ademas se creo un diccionario para las

diferentes  consultas  utilizadas  de  su  API,  de  este  modo se puede realizar una fácil transición

una vez el módulo cloud este desplegado, tal como se muestra en el Código 5.3.

private static readonly string userService = "http://localhost:3010";
private static readonly string getService = "http://localhost:3001";
private static readonly string sensorService = "http://localhost:3007";
private static readonly string spendService = "http://localhost:3008";
private static readonly string videogame = “WealthQuest”;

private static Dictionary<string, string> urlDictionary = new
Dictionary<string, string>
{
    { "login", $"{userService}/player/" },
    { "getPlayerById", $"{userService}/players/" },
    { "getPlayerAttributes", $"{getService}/player_all_attributes/" },
    { "videogames", $"{sensorService}/videogames" },
    { "mechanicsOfVideogame", $"{sensorService}/mechanics_of_videogame/" },
    { "spendAttributes", $"{spendService}/spend_attributes_apis" }
};

Código 5.3: Direcciones apis y diccionario de consultas url.

Fuente: elaboración propia, 2024.

Para  realizar

la  conexión  del  perfil  de  bGames,  se  utilizan  3  consultas,

primeramente con el nombre y contraseña se autentica nuestra cuenta de bGames obteniendo

nuestro identificador único, el cual se guarda en el videojuego a través de la clase PlayerPrefs

utilizada para guardar datos persistentes, de este modo se puede autenticar y obtener nuestro

perfil  sin  la  necesidad  de  volver  a loguearse en cada sesión de juego. Con el ID obtenido, se

consulta los datos del perfil y finalmente los puntos poseídos, tal como se muestra en el Código

5.4.

72

public static async Task<bool> Login(string name, string password)
{
    try
    {
        // Primera solicitud: Obtener el ID del perfil
        int playerId = await GetPlayerId(name, password);
        if (playerId < 0) return false;
        // Segunda solicitud: Obtener los datos del perfil
        BGamesProfile profile = await GetPlayerData(playerId);
        if (profile != null)
        {
            // Tercera solicitud: Obtener puntos del perfil
            int points = await GetPlayerPoints(playerId);
            profile.points = points;
            ProfileUser.SaveBGamesPlayer(profile);
            return true;
        }
        else
        {
            Debug.LogError("No se pudo obtener los datos del jugador.");
            return false;
        }
    }
    catch (System.Exception ex)
    {
        Debug.LogError($"Error en Login: {ex.Message}");
        return false;
    }
}

Código 5.4: Login perfil bGames.

Fuente: elaboración propia, 2024.

Una  vez  el  perfil  está  conectado,  el  jugador  puede  consumir  puntos  durante sus

partidas  para  obtener  un  intento  extra  para  responder  las  preguntas  presentadas,  siempre  y

cuando  posea  puntos  en  la  dimensión  cognitiva.  Para  su  consumo  se  utiliza  3  consultas,

primero  con  el ID del perfil almacenado se obtiene el ID del videojuego en base a su nombre,

con ese dato luego se consulta por el ID de la mecánica a modificar relacionada al videojuego,

con estos datos obtenidos se envía la solicitud para consumir los puntos, tal como se muestra

en el Código 5.5.

73

public static async Task<bool> SpendPoints(int points)
{
    try
    {
        // Obtener el ID del perfil del jugador
        int idPlayer = ProfileUser.BGamesProfile.id;
        // Paso 1: Obtener el ID del videojuego
        int idVideogame = await GetVideogameId(videogame);
        if (idVideogame < 0) return false;
        // Paso 2: Obtener el ID de la mecánica modificable
        int idModifiableMechanic = await
                                   GetModifiableMechanicId(idVideogame);
        if (idModifiableMechanic < 0) return false;
        // Paso 3: Realizar el POST para consumir los puntos
        bool success = await PostSpendAttributes(idPlayer, idVideogame,
                       idModifiableMechanic, points);
        if (success)
        {
            Debug.Log("Puntos consumidos exitosamente.");
            ProfileUser.BGamesProfile.points--;
            return true;
        }
        else
        {
            Debug.LogError("No se pudieron consumir los puntos.");
            return false;
        }
    }
    catch (System.Exception ex)
    {
        Debug.LogError($"Error en SpendPoints: {ex.Message}");
        return false;
    }
}

Código 5.5: Consumo de puntos bGames.

Fuente: elaboración propia, 2024.

74

5.2.5. Multijugador en línea

Para  implementar  el  modo  multijugador  en  linea  se  utilizo  la  herramienta  de

networking de Mirror, la cual permite crear instancias multijugador en línea donde un dispositivo

actúa  como  host  (cliente  y  servidor),  esto  resulta  útil  para  una modalidad de juego estilo p2p

(peer-to-peer),  donde  los  jugadores  (clientes)  se conectan directamente a otro dispositivo que

aloja la partida.

Este  modalidad  p2p  resulta  útil  para juegos independientes al no necesitar de un

servidor  centralizado  que  aloje  las  sesiones  en  línea,  el  problema  es  que  para  permitir

conexiones  directas  es  necesario  configurar  opciones  del  router  como  NAT punchthrough y/o

reenvío  de  puertos,  configuraciones necesarias que no poseen todos los routers o que vienen

por defecto desactivadas en algunos. Para evitar estas complicaciones y permitir que todos los

jugadores  puedan  disfrutar de esta modalidad, se implementa el servicio de Unity Relay como

intermediario,  este  servicio  se  encarga  de  administrar  las  conexiones  estableciendo  rutas

seguras  y  directas  entre  los  dispositivos,  lo  que  elimina  la  necesidad  de  realizar  ajustes

avanzados de red.

Esta   modalidad  funciona  de  forma  que  un  jugador  crea  una  sala  de  juego,  tal

como se muestra en la Figura 5.15, esta acción notifica al servicio de relay el cual se encarga

de  almacenar  la  sesión  con  la  dirección  del host, asignándole además un código de 6 dígitos

para conectarse, tal como se muestra en el Código 5.6.

public async Task<bool> StartRelayHostAsync(int maxPlayers, string region)
{
    TaskCompletionSource<bool> tcs = new TaskCompletionSource<bool>();
    utpTransport.useRelay = true;
    utpTransport.AllocateRelayServer(maxPlayers, region,
    (string joinCode) =>
    {
        relayJoinCode = joinCode;
        StartHost();
        tcs.SetResult(true);
    },
    () => { tcs.SetResult(false); });
    return await tcs.Task;
}

Código 5.6: Crear sala en línea.

Fuente: elaboración propia, 2024.

75

Figura 5.15: Sala en línea.

Fuente: elaboración propia, 2024.

El host puede compartir el código de la sala creada con los demás participantes a

través de canales externos, de manera que puedan ingresar este código para unirse, tal como

se  ilustra  en la Figura 5.16. Esta acción envía una solicitud de ingreso al servicio relay el cual

asocia  el  código  a  sala  del  host  y  redirige  la  conexión  directamente  hacia  ese  dispositivo,

estableciendo una conexión directa, tal como se muestra en el Código 5.7. De esta manera, se

garantiza una conexión estable, fluida y accesible para todos los participantes.

public async Task<bool> JoinRelayServerAsync(string joinCode)
{
    relayJoinCode = joinCode;
    if (string.IsNullOrEmpty(relayJoinCode))  return false;
    TaskCompletionSource<bool> tcs = new TaskCompletionSource<bool>();
    utpTransport.useRelay = true;
    utpTransport.ConfigureClientWithJoinCode(relayJoinCode,
    () =>
    {
        StartClient();
        tcs.SetResult(true);
    },
    () => { tcs.SetResult(false); });
    return await tcs.Task;
}

Código 5.7: Unirse a sala en línea.

Fuente: elaboración propia, 2024.

76

Figura 5.16: Partida en línea.

Fuente: elaboración propia, 2024.

5.2.6. Creación y administración de contenidos

El  sistema  de  preguntas  implementado  en  el  juego  cuenta  con  la  capacidad  de

abarcar variadas temáticas. Para alimentarlo se debe generar bancos de preguntas, nombrados

en  el  juego  como  contenido,  los  cuales  requieren  de  un  enfoque  estructurado  que  combine

principios pedagógicos sólidos con información confiable y contextualizada. Este proceso debe

alinearse  con  los  objetivos  de  aprendizaje,  las  características  de  los  jugadores  y  las

necesidades  específicas  del  entorno  en el que se implementará. A continuación, se describen

los aspectos clave para construir un banco de preguntas efectivo.

El  primer  paso  es  definir  los  objetivos  de  aprendizaje.  Es  fundamental  tener

claridad sobre qué conocimientos se busca desarrollar en los jugadores. Además, el diseño de

las preguntas debe considerar el perfil de los jugadores, adaptando la dificultad y el lenguaje al

nivel educativo y cultural de la audiencia objetiva.

Otro  paso  crucial  es  la  selección  de  fuentes  de  información  confiables  para

garantizar  la  calidad.  Las  preguntas  deben  contar  con  conceptos  universales  y básicos útiles

para  cualquier  contexto,  para  ello  es  recomendable basarse en investigaciones académicas y

literatura  científica,  como  los  trabajos  de  Lusardi  y  Mitchell  en  alfabetización  financiera.

Asimismo, se deben incluir datos y conceptos del contexto local de la audiencia objetiva, como

77

indicadores económicos relevantes, como el IPC y PIB en Chile, los cuales se pueden obtener

de  organismos  oficiales,  como  bancos  centrales  y  ministerios  de  economía.  Con  estas

referencias no solo aumenta la credibilidad del contenido, sino que también asegura una mayor

aplicabilidad práctica.

El  diseño  de  las  preguntas  debe  seguir  principios  validados  a  nivel  internacional

como  el  planteado  por  Lusardi  y  Mitchell  (2011),  que  incluyen:  (1)  la  simplicidad,  (2)  la

relevancia,  (3)  la  brevedad  y  (4)  la  capacidad  de  diferenciación.  Para  cumplir  con  ello,  se

establece para las preguntas la siguiente estructura:

Tabla 5.1: Estructura de pregunta.

Fuente: Elaboración propia, 2024.

Pregunta

Enunciado pregunta.

Alternativas

Opciones de respuestas (deben ser 3).

Respuesta

Respuesta correcta de las opciones.

Temática

Clasificación por temática.

Sub-Temática  Subclasificación por temática.

Nivel

La dificultad de las preguntas se organiza en un rango del 1 al 3, donde 1

(Dificultad)

corresponde  al  nivel  más  básico,  diseñado  para  abordar  preguntas

conceptuales  y  de  diagnóstico.  Los  niveles 2 y 3 se destinan a preguntas

prácticas,  orientadas a la aplicación de los conocimientos adquiridos en el

nivel 1.

De  este  modo  se  organiza  el  contenido  en  torno  a  temáticas  clave  y  niveles  de

dificultad,  a  fin  de  mantener  al  jugador  dentro  un  mismo  nivel  y  tema  en  caso  de  no

comprenderlo,  reforzando  sus  debilidades  antes  de  cambiar  de  tema  o  avanzar  en dificultad.

Esta estructura progresiva, permite un aprendizaje gradual y enfocado, comenzando con temas

básicos y avanzando hacia escenarios más complejos.

Con  este  enfoque  sistemático se garantiza la creación de un banco de preguntas

robusto  y  efectivo,  el  cual  contribuye  en  el  desarrollo educativo y financiero de los jugadores,

además de ser una herramienta útil para evaluar su nivel de conocimientos.

78

Estas  preguntas  pueden  ser  generadas  dentro  del mismo videojuego a través de

su  interfaz  de  creación  y  no  están  limitadas  a  abordar  solo  temas  financieros,  tal  como  se

muestra en la Figura 5.17. Tras definirlas se crea el contenido generando un archivo encriptado

de  extensión  .content,  el  cual  es  almacenado  en  la  carpeta  InTeractiOn/WealthQuest/Content

ubicada  en  persistent  Data  Path  (en  Windows  es  la carpeta LocalLow), además de poder ser

exportado y compartido con otros usuarios.

Figura 5.17: Interfaz de creación de contenido.

Fuente: elaboración propia, 2024.

Para  que  usuarios  más  avanzados,  con  conocimientos  en  programación  básica,

puedan generar contenidos de forma ágil, se implementa la opción de crearlos desde un archivo

.json, el cual es convertido a un .content. El archivo .json debe seguir el siguiente formato:

79

[
    {
        "question": "¿Qué significa la sigla IPC?",
        "answers": [
            "Índice de Producción Comercial",
            "Indicador de Progreso del Capital",
            "Índice de Precios al Consumidor"
        ],
        "indexCorrectAnswer": 2,
        "topic": "Indicadores económicos",
        "subTopic": "Inflación",
        "level": 1
    },
    {
        "question": "¿Qué es la inflación?",
        "answers": [
            "La disminución de la producción",
            "El aumento generalizado de los precios",
            "El aumento del PIB"
        ],
        "indexCorrectAnswer": 1,
        "topic": "Conceptos fundamentales",
        "subTopic": "Inflación",
        "level": 1
    }
]

Código 5.8: Contenido en formato .json.

Fuente: elaboración propia, 2024.

Además  el  videojuego  dispone de una interfaz para administrar estos contenidos,

la  cual  incluye:  buscar  y  filtrar,  modificar  (solo  si  se  es su autor), exportar, importar desde un

archivo  .json  o .content, descargar (contenidos aprobados y disponibles en la nube) y eliminar

(excepto el contenido inicial), tal como se muestra en la Figura 5.18.

80

Figura 5.18: Interfaz de contenidos.

Fuente: elaboración propia, 2024.

5.2.7. Distribución de contenidos

A fin de disponibilizar los contenidos para los jugadores, el videojuego cuenta con

un  sistema  los  almacena  y  obtiene  de  la  nube,  con  la  posibilidad  de  descargarlos  o

actualizarlos. Estos contenidos son almacenados en una rama de GitHub, en la cual se suben

estos archivos .content creados en el videojuego. Los archivos subidos son visualizados por los

jugadores en la interfaz de “Contenidos”, con un botón para descargarlos.

Dado  que  los  contenidos  creados  solo  pueden  ser  modificados  por  su  autor,  los

usuarios  que  los  descarguen  no  tienen  permisos  para  alterarlos.  Además,  al  estar  el  archivo

encriptado,  no  pueden  visualizar  fácilmente  las  respuestas,  de  manera  que  solo  pueden  ser

utilizados para cargarlos y jugar en las partidas.

Cabe  mencionar  que  el  sistema  también  posee  una  función  de  actualización  de

contenidos. Esta función opera con la versión del archivo, la cual aumenta en uno cada vez que

se  modifica.  Tras  modificarlo  y  subir  al  repositorio  la  nueva  versión,  los  usuarios  que

81

previamente  lo  tenían  descargado  visualizarán  un  botón  con  la  opción  para  actualizar.  Este

sistema  permite  a  los  desarrolladores  disponibilizar  y  actualizar  material  educativo  del

videojuego de manera sencilla, sin tener que realizar nuevas compilaciones del videojuego.

5.2.8. Contenido inicial

A  fin  de  entregar  una  solución  completa,  se  generó  un  banco  de  preguntas

financieras inicial construido como una herramienta educativa diseñada para evaluar y mejorar

la  alfabetización

financiera  de

los

jugadores,  abordando  dimensiones  clave  como  el

conocimiento,  las  actitudes  y  el  comportamiento  financiero.  Este  banco  se  fundamenta en un

diseño  progresivo  que  permite avanzar desde conceptos básicos hacia aplicaciones prácticas,

asegurando un aprendizaje gradual y enfocado.

El diseño del banco se inspira en estudios que destacan la alfabetización financiera

como una habilidad esencial para la toma de decisiones económicas informadas. Según Lusardi

y Mitchell (2011), “la alfabetización financiera está estrechamente vinculada con la planificación

de la jubilación y la acumulación de riqueza durante la jubilación” (p. 498). Además, el enfoque

progresivo  de las preguntas, junto con un sistema de retroalimentación inmediata, refuerza los

conceptos  en  los  que  los  jugadores  presentan  debilidades  antes  de  avanzar  a  niveles  más

complejos.

La  alfabetización  financiera  se  identifica  como  un  medio  para  aumentar  el

conocimiento  y  guiar  los  comportamientos,  especialmente  en  áreas  como  la  elaboración  de

presupuestos  y  el  ahorro  (Popovich,  Loibl,  Zirkle  y  Whittington,  2020,  p.  1).  Investigadores

señalan  que  esta  abarca  dos  dimensiones  principales:  (i)  la  adquisición  de  conocimientos  y

habilidades  financieras,  y  (ii)  la  modificación  del  comportamiento  financiero  (Thomas  &

Subhashree,  2019,  p.  482).  Ambas  dimensiones,  influenciadas  por  diversos  factores,  son

abordadas por las preguntas generadas, cubriendo los siguientes aspectos:

1.  Conocimiento financiero: incluye la comprensión de conceptos básicos como

la  tasa de interés, la inflación y la diversificación de riesgos. Según Thomas y

Subhashree  (2020),  “el  conocimiento financiero facilita y enriquece el nivel de

alfabetización  financiera  y  mejora  la  capacidad  para  participar  en  la  toma de

decisiones financieras” (p. 483).

2.  Actitud  financiera:  aborda  la  disposición  hacia  el  dinero  y  las  metas

financieras de las personas. Thomas y Subhashree (2020) indican que “si uno

82

valora  la  adquisición  de dinero y está decidido a alcanzar metas materialistas

(financieras),  se  esforzará  por  lograr  una  mayor  alfabetización  financiera”  (p.

483).

3.  Comportamiento  financiero:  se  centra  en  la  aplicación  práctica  de  los

conocimientos  adquiridos,  como  la  planificación  del  ahorro,  la  gestión  de

presupuestos  y  el  manejo  de deudas, elementos esenciales para el bienestar

financiero a largo plazo. Según Thomas y Subhashree (2019), “la alfabetización

financiera  influye  en  el  comportamiento  financiero,  y  el  comportamiento

financiero influye en la alfabetización financiera” (p. 483).

Las  preguntas  diseñadas  siguieron  principios  validados  a  nivel  internacional

planteados por Lusardi y Mitchell (2011), que incluyen la simplicidad, la relevancia, la brevedad

y la capacidad de diferenciación. Además, se integran conceptos fundamentales, universales y

aplicables  en  cualquier  contexto  económico,  tales  como  las  "Big  Three"  de Lusardi y Mitchell

(2011), siendo estos: (1) la aritmética en relación con la capacidad de realizar cálculos de tasas

de interés y comprender la capitalización de los intereses; (2) la comprensión de la inflación; y

(3) la comprensión de la diversificación del riesgo.

Por otra parte, con el fin de contextualizar el aprendizaje en la realidad económica

chilena y asegurar su aplicabilidad práctica, se incorporaron indicadores económicos relevantes

a  nivel  nacional,  como  el  IPC  y  el  PIB  (Massad,  2004).  Asimismo,  cabe  mencionar  que  el

contenido  inicial  fue  desarrollado  con  el  apoyo  de  la  profesora  co-guía  Karina  Chandia

Troncoso,  Magíster  en  Finanzas  y  especialista  en  contabilidad  y  finanzas,  lo  cual  permitió

garantizar la pertinencia y rigor de los conceptos económicos incluidos.

El contenido de las preguntas se organizó en torno a temáticas clave demostradas

como esenciales para la alfabetización financiera:

1.  Conceptos  fundamentales:  incluyen  conceptos  como  la  tasa  de  interés,  la

inflación y la diversificación de riesgos, que son conceptos base para la mayoría

de las decisiones financieras (Lusardi, 2019, p. 1).

2.

Indicadores  económicos:  adaptados  al contexto local, con indicadores como

el IPC y el PIB, relevantes para la economía chilena (Massad, 2004).

3.  Planificación  financiera  (ahorro  e  inversión):  este  aspecto  destaca  la

importancia  del  ahorro  y  la  inversión  estratégica  como  pilares  fundamentales

83

para  el  bienestar  financiero  a  largo  plazo,  fomentando  comportamientos

financieros  positivos.  Según  Lusardi  (2019),  “la  alfabetización  financiera

también  está  asociada  con  mayores  retornos  sobre  inversiones  e inversiones

en activos más complejos” (p. 5).

4.  Gestión  de  presupuestos  y  deudas:  esta  temática  abarca  habilidades

prácticas  como  la  planificación  del  gasto  y  la  comprensión  de  las  tasas  de

interés en créditos, elementos fundamentales para manejar desafíos financieros

cotidianos.  Según  Lusardi  y  Tufano  (2009),  las  personas  con  bajo  nivel  de

alfabetización  tienen  más  probabilidades  de  tener  deudas  de  alto  costo  y

problemas con las deudas.

El  aprendizaje  y

la  práctica  de  estos  conceptos  y  habilidades  impactan

significativamente la calidad de vida de las personas, mejorando su capacidad para planificar el

futuro,  gestionar  recursos  limitados  y  tomar  decisiones  informadas.  Según  Lusardi  y  Mitchell

(2011),  “quienes  han  calculado  cuánto  necesita  ahorrar  para su propia jubilación llegan a esa

edad  con  una  riqueza  hasta  tres  veces  mayor  que  quienes  no  han  hecho  esos  cálculos”  (p.

506).

De  esta  manera,  el  banco  financiero  inicial  implementado  representa  una

herramienta  integral  para  mejorar  la  alfabetización  financiera.  Su  diseño,  basado  en  estudios

previos, y su enfoque progresivo e interactivo permiten una experiencia de aprendizaje efectiva,

fomentando  decisiones

financieras

informadas  y  responsables.  Además,  al

incorporar

conceptos  de  la  realidad  económica  chilena,  permite  también  a  los  jugadores  comprender  y

enfrentar  desafíos  económicos  dentro  del  contexto  nacional.  Para  un  mayor  detalle sobre las

preguntas generadas y utilizadas en el juego, se puede consultar el Apéndice A.

5.2.9. Publicación del videojuego

Para  la  publicación  del  videojuego,  existen  múltiples  plataformas  de  distribución

digital compatibles con Windows, como Epic Games Store, Steam, entre otras. El problema con

estas  plataformas  más  populares  es  que  requieren  pagar  una  cuota  de  publicación,  la  cual

generalmente asciende a alrededor de $100 (Steam y Epic Games). Además, estas plataformas

exigen  pasar  por  una  evaluación  de  seguridad  y  calidad,  cuya  rigurosidad  varía  según  cada

caso, siendo Steam una de las más permisivas en este aspecto.

84

Dado  que  la  solución  implementada  será  de  acceso  gratuito  y  no  generará

ingresos, se buscó una plataforma alternativa, seleccionando Itch.io. Esta plataforma permite la

distribución  de  contenido  digital,  incluidos  videojuegos  y recursos para desarrolladores. Itch.io

es  conocida  como  una  plataforma  "de  desarrolladores  para  desarrolladores"  y  ofrece  la

posibilidad  de  publicar  contenido  de  manera  gratuita,  además  de  aceptar  donativos  de  los

usuarios (opción que, en este caso, no se implementó).

Con  la  plataforma  de  distribución  seleccionada,  se  procedió  a  empaquetar  el

proyecto y publicarlo. Para publicar en Itch.io, es necesario crear una cuenta en la plataforma,

confirmar  el  correo  electrónico  y  seleccionar  el  método  de  pago  para  donativos.  Una  vez

registrado,  se  debe  acceder  a  la  opción  "Subir  nuevo  proyecto"  para  abrir  la  interfaz  de

publicación.  En  esta  interfaz,  es  necesario  completar  un  formulario  de  registro  que  incluye

información como: nombre, descripción, clasificación, precios (en este caso, sin pagos), género,

etiquetas,  comunidad y visibilidad. También se debe seleccionar el tipo de proyecto y subir los

archivos del juego. Los formatos más comunes son:

●  Descargable:  Permite  descargar  el

juego  para  el  sistema  operativo

especificado.

●  HTML:  Permite  jugar  directamente  desde  el  navegador  en  Itch.io  (requiere

compilación en WebGL).

Dado que la solución implementada utiliza Firebase para el manejo de usuarios, el

juego  se  publica  como  descargable  para  la  plataforma  de  Windows,  ya  que  Firebase  no  es

compatible  de  forma  nativa  con  compilaciones  WebGL.  De  esta  manera,  el  juego  quedó

disponible al público bajo el nombre WealthQuest.

85

Figura 5.19: Página de WealthQuest en itch.io.

Fuente: elaboración propia, 2024.

5.4. RESUMEN

En  este  capítulo  se  presentaron

los  aspectos  de  diseño,  arquitectura  e

implementación  del  proyecto  basados  en  el  GDD  y  en  los  requerimientos  funcionales  y  no

funcionales  establecidos  inicialmente,  detallando  los  aspectos  más  relevantes  del  proceso, la

implementación y los resultados.

86

CAPÍTULO 6. EVALUACIÓN

En  este  capítulo  se  presentan  los  resultados  obtenidos  por  las  evaluaciones

realizadas al proyecto, siendo estas: pruebas de software, experiencia de usuario y aceptación.

Estas  pruebas  se  hicieron  con  el  objetivo  de  evaluar  el  diseño  y  desempeño  del videojuego,
además de verificar su aspecto funcional.

6.1. PRUEBAS DE SOFTWARE

Las pruebas de software realizadas tienen el objetivo de evaluar el desempeño del

videojuego  y  se  componen  de  dos  pruebas:  prueba  de  compatibilidad,  para  comprobar  su

funcionamiento  en  la  plataforma  de  Windows,  y  prueba  de  rendimiento,  para  evaluar  su

desempeño en el sistema principal, Windows.

6.1.1. Ambientes de prueba

Para  las  pruebas  de  software  se  utilizaron  2  computadoras,  un  ordenador  de

escritorio  (principal)  y un notebook (secundario) con las especificaciones técnicas descritas en

la Tabla 6.1 y 6.2

Tabla 6.1: Especificaciones técnicas del ordenador principal.

Fuente: elaboración propia, 2024.

Identificador

PC - 01

Tipo de ordenador

Computador de escritorio personal

CPU

GPU

Ram

12th Gen Intel(R) Core(TM) i5-12400 2.50 GHz

NVIDIA GeForce RTX 3050

32.0 GB

Sistema Operativo

Windows 11 Pro 24H2

87

Tabla 6.2: Especificaciones técnicas del ordenador secundario.

Fuente: elaboración propia, 2024.

Identificador

PC - 02

Tipo de ordenador

Computadora notebook personal

CPU

GPU

Ram

AMD Ryzen 5 2500U with Radeon Vega Mobile Gfx 2.00 GHz

Radeon RX 560 Series

12.0 GB

Sistema Operativo

Windows 11 Enterprise 22H2

6.1.2. Pruebas de compatibilidad

Para  las  pruebas  de  compatibilidad  se  crearon  ejecutables  enfocados  para  cada

una  de  las  plataformas,  para  ello  se  utilizó  la  funcionalidad  de  compilado  y  empaquetado de

videojuegos  del  motor  Unity,  la  cual  crear  una  carpeta  con  los  archivos  del  juego  y  un

ejecutable, cuya extensión varía según la plataforma.

Se  sintetizan  los  resultados  obtenidos  en  la  Tabla  6.3,  donde  se  especifica  el

estado de la ejecución del juego y cualquier observación pertinente.

Tabla 6.3: Resultados de las pruebas de compatibilidad.

Fuente: elaboración propia, 2024.

Plataforma

Estado

Observación

Windows 11

Operativo (O).

Funciona sin problemas.

Ubuntu 24.04
(Linux)

Operativo (O).

Funciona sin problemas.

WebGL

No Operativo (NO).  No compatible de forma nativa con Firebase.

88

6.1.3. Pruebas de rendimiento

Para la evaluación del rendimiento del videojuego se utilizaron métricas que miden

la  eficiencia  para  gestionar  los  recursos  del  dispositivo  en  que  se  ejecuta  y  el  rendimiento

general del videojuego. Las métricas medidas fueron las siguientes:

●  Fotogramas  por  segundo  promedio  (Avg  FPS):  representa el promedio de

cuadros  por  segundo,  utilizando  métricas  de  programación  de  FPS

renderizadas. Es una de las tres métricas clave para evaluar un juego (NVIDIA

Corporation, 2022).

●  1%  más  bajo  de  fotogramas  por  segundo  (1% Low FPS): toma el 1 % de

cuadros  más  lentos  y  calcula  el  promedio.  Esta  métrica  permite  identificar

caídas de rendimientos u microtirones (stuttering). Es una de las tres métricas

clave para evaluar un juego (NVIDIA Corporation, 2022).

●  Fotogramas por segundo mínimo (Min FPS): representa la velocidad mínima

de  cuadros  por  segundo.  Indica  el  peor  rendimiento  registrado  y  es  útil  para

detectar caídas severas en el rendimiento.

●  Fotogramas  por  segundo  máximo  (Max  FPS):  representa  la  velocidad

máxima  de  cuadros  por  segundo.  Indica  el  mejor  rendimiento  posible

registrado, aunque no refleja la fluidez real del juego.

●  Utilización  CPU  (CPU  Util  %):  Indica  el  porcentaje  de  uso  de  la  Unidad

Central de Procesamiento (CPU) durante la sesión de juego. Un alto porcentaje

de  uso puede indicar que existen muchas tareas en simultáneo, lo que puede

afectar la fluidez del juego.

●  Utilización  GPU  (GPU  Util  %):  Indica  el  porcentaje  de  uso  de  la  Unidad de

Procesamiento  Gráfico  (GPU).  Un  bajo  porcentaje  de  uso  puede  indicar  que

otros componentes como la CPU o RAM están limitando el rendimiento.

Para  la  obtención  de  estos  datos  existen  diferentes  técnicas  y  software  que

permiten  capturarlos,  para  esta  evaluación  se  utilizó  la  herramienta  de  Nvidia  FrameView,  el

cual  permite  capturar  estas métricas durante las sesiones del juego con costes mínimos en el

rendimiento  a  fin  de  obtener  datos  lo  más  fiable  posible.  El  procedimiento  realizado  para

capturar  esta  información  del  videojuego  se  constituyó  de  2  pruebas en cada ordenador, una

actuando como host y otra como cliente de una partida en línea, siendo los escenarios posibles

del videojuego.

89

Previo  a  la  prueba,  se  reiniciaron  los  equipos  a  fin  de  liberar  todos  los  recursos

posibles  y se configuró el videojuego con Vsync desactivado, resolución 1920x1080 y gráficos

en  calidad  alta.  Además,  en  el  ordenador  secundario  (PC  -  02),  la  prueba  como  cliente  se

realizó  sin  cargador  conectado,  a  fin  de  simular  el  peor  escenario  de  rendimiento  posible,

mientras  que  su  prueba  como  host se realizó con cargador para obtener el mejor rendimiento

posible y realizar la comparativa de ambos.

Con  los datos obtenidos por la evaluación se generan 2 gráficos comparativos de

la  métricas  de  eficiencia  de  uso  de  los  recursos  de  sistema  y  del  rendimiento  general  del

videojuego en las Figuras 6.1 y 6.2 respectivamente, resumidas en la Tabla 6.4.

Tabla 6.4: Resultados de las pruebas de rendimiento.

Fuente: elaboración propia, 2024.

Ordenador  CPU Util

%

GPU Util
%

Avg FPS  Max FPS  Min FPS

1% Low
FPS

PC - 01
(Host)

PC - 01
(Client)

PC - 02
(Host)

PC - 02
(Client)

24,738

35,451

164,782

748,671

10,184

132,462

21,294

28,839

164,783

971,062

11,605

135,693

46,625

56,179

59,698

106,626

2,858

37,978

45,039

92,675

119,892

277,146

1,309

56,963

90

Figura 6.1: Resultados de rendimiento de uso de recursos.

Fuente: elaboración propia, 2024.

Figura 6.2: Resultados de rendimiento general.

Fuente: elaboración propia, 2024.

91

Los  resultados  observados  en las métricas permiten identificar el comportamiento

del  videojuego  durante  una  sesión  de juego tanto como host como cliente. A continuación, se

detallan sus principales implicaciones:

●  Uso  de  CPU:  el  uso  de  CPU  utilizado  como  host  fue  mayor  que  el utilizado

como  cliente,  el  cual  es  un  resultado  esperable  debido  a  las  tareas  y

sincronización  de  red  que  debe  realizar  el  host.  Sin  embargo,  que  el  uso de

CPU  también  sea  elevado  como  cliente  sugiere  que  existen  tareas  locales

costosas que podrían optimizarse.

●  Uso de GPU: el uso de GPU fue considerablemente mayor en el PC-02, lo cual

se  debe  a  su  hardware  de  menor  rendimiento  y  a  que  operaba  sin  estar

conectado al cargador, lo cual limita la GPU por ahorro energético. Esto indica

que  la carga gráfica del videojuego no satura completamente las capacidades

del  hardware,  pero  es  recomendable  una  GPU  dedicada  para  mantener  una

buena fluidez.

●  Rendimiento  FPS  (Avg,  Min,  Max,  1%  Low):  la  tasa  de  fotogramas  por

segundo  resultó  generalmente  alta,  con  valores  promedios  sobre  100  fps,  lo

que indica la fluidez del juego. A pesar de la buena media, los valores de Min

FPS  y 1% Low FPS indican que existen momentos de caídas de rendimiento,

lo cual puede provocar microtirones perceptibles para el jugador.

6.2. EXPERIENCIA DE USUARIO

La  evaluación  de  la  experiencia  de  usuario  se  realizó  mediante  la  evaluación

heurística  para  la  jugabilidad  (HEP),  el  cual  es un método ya utilizado en varios proyectos de

videojuegos  previos  de  bGames,  como el de Ternero (Ternero, 2022), Lizama (Lizama, 2022),

entre otros, lo cual data de su eficacia y utilización.

Este  método  permite  diagnosticar  fortalezas  y  debilidades  del  diseño  mediante

criterios  heurísticos  y  consiste  en  un  cuestionario  que  se  realiza  a  los  participantes  luego de

probar el videojuego, teniendo como objetivo evaluar, en términos de experiencia del usuario, 3

aspectos  principales:  jugabilidad,  mecánicas  y  usabilidad.  Además  de  incorporar  preguntas

libres para una retroalimentación más personalizada de cada participante.

La  evaluación  realizada  se  conformó  por  4  integrantes  de  edades  entre  19  y  25

años, con experiencia previa en videojuegos en general, siendo usuarios de confianza respecto

al  desarrollo  del  videojuego  y  participantes  activos  en  el  testeo  desde  sus  inicios.  Esta

92

evaluación se compuso por 9 preguntas distribuidas en tres categorías: jugabilidad, mecánicas

y  usabilidad,  cada  una  con  tres  preguntas  (ver  Apéndice  C.2).  Con  ellas  se  busca  evaluar

aspectos  como  el  progreso,  la dificultad, la claridad de la interfaz, el balance, entre otros. Los

participantes  calificaron  cada  una  en  una  escala  de  Likert  del  1  al  5, donde 1 corresponde a

“muy  en  desacuerdo”  y  5  a  “muy  de  acuerdo”.  Adicionalmente,  se  incluyeron  tres  preguntas

abiertas al final del cuestionario para obtener retroalimentación cualitativa personalizada.

Cabe mencionar que las pruebas realizadas por este grupo acotado de usuarios de

confianza, tienen como único objetivo obtener una retroalimentación preliminar de la experiencia

de  usuario  y  funcionamiento  del  videojuego  para  una  eventual  conducción  de  estudios

posteriores  con  usuarios  adicionales  incorporando  los  protocolos  del  comité  de  ética  de  la

universidad, lo cual escapa al alcance y tiempos del proyecto y memoria.

En  las  siguientes  subsecciones  se presentan las respuestas obtenidas para cada

pregunta de la evaluación, acompañadas del análisis correspondiente a cada categoría.

6.2.1. Jugabilidad

Figura 6.3: Resultados de encuesta jugabilidad.

Fuente: elaboración propia, 2024.

93

Respecto  a  los  resultados  obtenidos  sobre  la  jugabilidad,  se  aprecia  una  clara

reacción positiva acerca del control del videojuego, refiriéndose a las decisiones tomadas por el

jugador,  y  el  cómo  este  presenta  el  progreso  de  manera  adecuada  a  lo  largo  de  la  partida.

Mientras  que  se  evidencia  una  opinión  promedio  neutra  acerca  de  la  curva  de  dificultad

progresiva,  la  cual  se  basa  en  las  preguntas  presentadas  durante  el turno de cada jugador y

que  actualmente  se divide en 3 niveles de dificultad. Esto da lugar a una área de mejora para

futuros trabajos, con una posible solución una mayor división de los niveles de dificultad para un

aumento más paulatino.

6.2.2. Mecánicas

Figura 6.4: Resultados de encuesta mecánicas.

Fuente: elaboración propia, 2024.

En cuanto a las mecánicas del videojuego se evidencia una clara reacción positiva

acerca  de  los  controles  utilizados,  que  puede  ser  teclado,  mouse  o  gamepad, los cuales son

relevantes  para  una  experiencia  de  juego  fluida.  En  cuanto  a  las  acciones  del  jugador  se ve

reacción  neutra  sobre  las  mismas,  principalmente  por  las  animaciones  ejecutadas  por  el

personaje,  las  cuales se vieron limitadas al utilizar assets públicos para su creación, debido al

tiempo acotado para el proyecto y el escaso conocimiento del modelado 3D y animación digital,

lo que deja abierto una área de mejora para posibles trabajos futuros. Por último, en cuanto al

94

balance  de  los  turnos  del  jugador,  conformados  por  los  intentos  y  recursos  obtenidos,  se

evidencia una reacción neutra, principalmente a causa de ciertas tarjetas que otorgan ventajas

o desventajas consideradas muy elevadas, lo que da lugar a una área a mejorar a través de la

incorporación  de  nuevas  tarjetas  a fin de reducir la probabilidad de aparición de aquellas más

beneficiosas o perjudiciales, a su vez de la posibilidad de modificar las mismas para reducir su

impacto.

6.2.3. Usabilidad

Figura 6.5: Resultados de encuesta usabilidad.

Fuente: elaboración propia, 2024.

En  cuanto  a  la  usabilidad  se  ve  una  clara  reacción  positiva,  esto  se  debe  a  la

simplicidad  y  fluidez  por  la  que  se  navega  a  través de las diferentes interfaces que cuenta el

videojuego,  con animaciones fluidas y breves. Además de contar durante las partidas con una

interfaz  de  usuario  clara  que  presenta  de  forma  eficiente  los  recursos  de  cada  jugador, y las

acciones que pueden realizar en su turno.

95

6.2.4. Preguntas libres

Por  último,  la  encuesta  incorporó  tres  preguntas  libres,  las  cuales  tienen  el

propósito  de  obtener  información  más  personalizada  de  cada  usuario,  acerca  de  sus

percepciones y valoración personal.

1.  ¿Qué cosas le gustaron del videojuego?

Se  menciona  el  atractivo  de  la  jugabilidad  y  competitividad  para  la  modalidad

multijugador,  la  cual  incentiva  el  obtener  el  mejor  puntaje  posible,  puntaje  que  depende  del

progreso que puede realizar cada jugador por cuenta propia sin verse afectado por los demás,

lo  que  resultó  entretenido  para  partidas  breves  con  amigos.  También  se destacó su curva de

dificultad  progresiva,  la  cual  mantiene  concentrados  a  los  jugadores  para  lograr  responder

correctamente la mayoría de las preguntas.

2.  ¿Qué  aspectos  del  videojuego  resultaron  frustrantes,  confusos  o  poco

claros?

Se  menciona  que  las  primeras  partidas pueden resultar algo frustrante, debido al

desconocimiento  acerca  de  la  temática  tratada,  pero  a  lo  largo  de  las diferentes sesiones de

juegos,  su  percepción  mejora  al  adquirir  los  conocimientos  presentados  y  mejorar  su

rendimiento, resultado en una experiencia que resulta más satisfactoria a medida que el jugador

progresa  de  forma  personal.  Lo  cual  data  de  un  diseño  de  juego  correcto,  pues  balancea  la

dificultad,  la  cual  aumenta  de  forma  constante  a  medida  que  el jugador progresa, de manera

que  no  sea  ni  muy  sencilla,  para  no  aburrir  al  jugador,  ni  muy  elevada,  para  no  frustrar

considerablemente, sino que lo suficiente para incentivar a que mejore.

3.  ¿Qué aspectos crees que se podría mejorar en el videojuego?

En  cuanto  a  posibles  mejoras  comentadas  por  los  encuestados,  se  menciona  la

incorporación  de  nuevas  animaciones  para  los  personajes,  a  fin  de  hacerlo  más  dinámico  y

atractivo.  También  se  menciona  la  incorporación  de  nuevos  mapas  y  dados  para  una  mayor

diversidad  en  las  partidas.  Otro  punto  a  destacar  mencionada fue la incorporación de nuevos

Contenidos  para

jugar,  siendo

la  creación  de  estos  paquetes  una  funcionalidad  ya

implementada, pero que se limitó a la creación inicial de solo un paquete debido a los tiempos

acotados  del  proyecto  y  el  enfoque  a  las  finanzas  personales  básicas,  dejando  abierto  la

posibilidad de incorporar nuevos contenidos a futuro, tanto de parte de los desarrolladores como

de los mismos jugadores.

96

6.3. PRUEBAS DE ACEPTACIÓN

Esta  evaluación  tiene  como  objetivo  verificar  que  el  videojuego  desarrollado

cumple con los requisitos funcionales y no funcionales del proyecto, actuando como mandante

el profesor guía del proyecto.

Para  realizar  esta  evaluación  se  utiliza  un  criterio  de  aceptación  definido  por  el

rango  de  A  a  la  E,  de  mayor  a  menor  cumplimiento,  detallado  en  la  Tabla  6.5.  Además  de

incorporar observaciones de ser pertinente.

Tabla 6.5: Rango de aceptación de pruebas.

Fuente: elaboración propia, 2024.

Evaluación

Significado

Porcentaje de cumplimiento

A

B

C

D

E

Aprobada.

85% - 100%

Aprobada con observaciones.

60% - 84.9%

Incompleta.

Insuficiente.

No aceptada.

45% - 59.9%

15% - 44.0%

0% - 14.9%

Los  resultados  de  las  pruebas  de  aceptación  se  resumen  en la Tabla 6.6, con el

detalle de cada prueba en el Apéndice C.2.

Tabla 6.6: Resumen de las pruebas de aceptación - Parte I.

Fuente: elaboración propia, 2024.

ID

Nombre

Descripción

Evaluación

PA-01

PA-02

Registrar  e Iniciar sesion de
perfil de juego

Prueba  encargada  de verificar el flujo
de creación y conexión de usuarios.

Autenticación  de  usuario  y
puntos
visualización
bGames

de

Prueba  encargada  de  verificar  que el
usuario se conecta correctamente con
bGames.

B

A

PA-03

Creación de contenido

Prueba encargada de verificar que los
Contenidos se creen exitosamente.

A

97

Tabla 6.7: Resumen de las pruebas de aceptación - Parte II.

Fuente: elaboración propia, 2024.

PA-04

Descargar contenido

Prueba  encargada  de verificar que los
Contenidos  en  la  nube se descarguen
correctamente.

PA-05

Creación de partida local

PA-06

Mecánicas  de  jugador  en
turno

PA-07

Consumo
bGames por intento extra

de

puntos

PA-08

Creación  de  partida  en
línea

PA-09

Cerrar sesión de bGames

Prueba  encargada  de verificar que las
creen
partidas
exitosamente.

locales

se

Prueba  encarga  de  verificar
mecánicas  del
turno:
dado, escoger tarjeta, HUD jugador.

las
jugador  durante  un
lanzar

responder  pregunta,

Prueba  encarga  de  verificar  que  los
puntos  de  bGames  se  consuman  de
forma  adecuada  y  modifique
la
mecánica determinada (intento extra).

Prueba encargada de verificar la
correcta creación y conexión durante
una partida en línea.

Prueba encargada de verificar la
correcta desconexión de la cuenta de
bGames.

A

A

B

B

C

A

A  fin  de  visualizar  de mejor forma los resultados obtenidos se presenta el gráfico

de  la  Figura  6.6.  En  este  puede  observar  que  la  gran  mayoría  de  las  pruebas  realizadas

cuentan  con  una  evaluación  entre  A  y  B,  destacando  que  las  observaciones  entregadas  son

principalmente acerca de ajustes a elementos gráficos como apoyo para el usuario.

98

Figura 6.6: Resultados de las pruebas de aceptación.

Fuente: elaboración propia, 2024.

6.4. RESUMEN

En  este  capítulo  se  describe  la  etapa  de  evaluación  de  la  solución desarrollada,

donde se incluyen los métodos utilizados para las pruebas y los resultados de las evaluaciones

realizadas, analizando de manera preliminar sus implicaciones. Los aspectos evaluados fueron:

(1)  la  compatibilidad  y rendimiento en diferentes plataformas, (2) la experiencia del usuario en

jugabilidad,  mecánicas  y  usabilidad,  y  (3)  el  cumplimiento  de  los  requisitos  funcionales  y  no

funcionales.

99

CAPÍTULO 7. CONCLUSIONES

En  este  capítulo  se  presentan  las  conclusiones  del  proyecto  desarrollado,

evaluando  el  grado  de  cumplimiento  de  los  objetivos  planteados,  así  como las implicaciones,

alcances y limitaciones que hubo durante el desarrollo, y el trabajo futuro posible a realizar para

mejorar el videojuego. Además, para finalizar, se entrega una reflexión final.

7.1. OBJETIVOS

Como  parte  de  todo  proyecto,  durante  su  etapa  inicial,  se  define  un  objetivo

general con el cual se orienta el desarrollo, además de objetivos específicos que proporcionan

una  guía  para  cumplirlo.  A  continuación,  se  detallan  y  verifican  el  grado  de  cumplimiento  de

estos objetivos planteados en el Capítulo 1.

7.1.1. Objetivos Específicos

1.  Elaborar  el  documento  de  diseño  del  juego  (GDD)  para  el  videojuego

WealthQuest, incluyendo las mecánicas afectadas por el perfil de usuario

de Blended Games (bGames): se generó un GDD que presenta los aspectos y

conceptos  base  del  videojuegos,  tales  como  los datos del jugador, casillas de

juego, atributos del jugador, sistema de puntos, entre otros. Esto permitió sentar

una  base  clara  del  diseño  y  aspecto  que  se  buscaba  para  el  videojuego,

permitiendo  desarrollar  de  una  forma  ordenada  y clara. Este documento pasó

por varias versiones durante el transcurso del desarrollo al surgir nuevas ideas

que  implementar,  permitiendo  integrarlas  de  manera  clara  y  sin  mayores

dificultades dentro del diseño.

2.

Implementar  el  videojuego  a partir del GDD, asegurando la funcionalidad

básica y la integración del framework bGames en la plataforma Windows:

a  traves  del  analisis de requerimientos, del GDD generado y del desarrollo de

los  diferentes  prototipos  se  logró  identificar  e  implementar  las  técnicas

esenciales  que  debe  contar  un  juego  de tablero y lo necesario para transmitir

conceptos  educativos  de  manera efectiva y lúdica. El resultado corresponde a

un juego que permite realizar desde partidas rápidas hasta de mayor duración,

100

en  las  cuales  el  jugador  se  enfrenta  a  diferentes  preguntas  que  ponen  sus

conocimientos  financieros  y  a  diferentes  situaciones  que  ponen  a  prueba  su

comportamiento  y  actitud  financiera,  relacionado  al  manejo  del  dinero.  Se

destaca además por la posibilidad de jugar en modalidad multijugador, tanto de

forma  local  como  en  línea,  lo  cual  permite un aprendizaje en conjunto ya sea

con  amigos  o  familia,  lo  que  resulta  importante  al  ser  finanzas  no  solo  algo

llevado de forma personal sino que en varias se manejan en conjunto con otros

integrantes.

3.  Desarrollar al menos un sensor para el framework de Blended Games para

alimentar  el  perfil  multidimensional  bGames  del  jugador  con  datos

financieros reales: se permite el consumo de puntos del perfil de bGames de

los usuarios para la obtención de intentos extras para responder las preguntas

presentadas  dentro  del  videojuego.  Para  ello  se  implementó  un  sensor  que

capturase  datos  relacionados  a  las  finanzas  del  usuario,  siendo  la  API  de

Fintual  la  seleccionada,  pues  permite  calcular  el  porcentaje  de  cumpliento de

las  metas  de  ahorro  propuestas  por  el  mismo  usuario,  obteniendo  en  base a

ello puntos de bGames, de esta se alimenta el perfil en base datos financieros

reales y se incentiva el hábito del ahorro recompensado con puntos a utilizar el

videojuegos que utilizan el framework.

7.1.2. Objetivo General

Desarrollar  el  videojuego  serio  WealthQuest  utilizando  el  motor  de

videojuegos  Unity  y  el  framework  Blended  Games,  para  proporcionar  una  alternativa

educativa interactiva y lúdica orientada al aprendizaje de conceptos básicos de finanzas

personales.

El  objetivo  general  es  cumplido  a  través  del  cumplimiento  de  los  objetivos

específicos  establecidos,  detallados  anteriormente.  Esto  incluye  la creación de un GDD como

una guía del diseño y estructura del videojuego, el se utilizo en conjunto con los requerimientos

funcionales  y  no  funcionales  establecidos  para  desarrollar  el  videojuego  serio  WeatlhQuest,

integrando  mecánicas  claves  de  los  juegos  de  tablero  e  integrando  conceptos  educativos

basados en la literatura de forma clara y concisa. De esta forma, el videojuego se convierte en

un producto que aborda los principales conceptos de la alfabetización financiera y los transmite

de  una  manera  tan  entretenida  como  lúdica, que en conjunto con el sensor desarrollado para

101

bGames,  el  cual  incentiva  y  premia  los  buenos  hábitos  de  ahorro,  se  obtiene  un  producto

completo para apoyar al mejoramiento del nivel de alfabetización financiera.

7.2. IMPLICACIONES

A  partir  de  los  resultados  obtenidos  por  la  solución,  se  considera  el  producto

generado  como  una  herramienta  útil  para  apoyar  el  aprendizaje  y  mejorar  la  alfabetización

financiera  de  los  jóvenes.  Por  otra  parte  permite  expandir  y  dar  a  conocer  el  framework  de

bGames, aunque debido a que el módulo cloud se encuentra aún en fase desarrollo, a la fecha
de publicación del videojuego, aún no podrá ser utilizado por el público general.

7.3. ALCANCES Y LIMITACIONES

Con  respecto  a  los  alcances  más  importantes  se  considera  principalmente  el

carácter  autónomo  y capacidad de fácil expansión de la solución, pues aunque cuenta con un

contenido  inicial  bastante  completo,  la  solución  cuenta  con  la  posibilidad  de  cargar  mas

contenido de manera sencilla y disponerlo a sus usuarios, además de integrar la posibilidad de

que  ellos  mismos  creen  sus  propios  paquetes  de  preguntas  y  los  compartan  de  manera

autónoma por canales externos.

No  obstante  existieron  algunas  limitaciones.  Debido  a  limitaciones  de  tiempo,  se

dejó  fuera  de  los  objetivos  del  proyecto  la  evaluación  exhaustiva  de  la  eficacia  del producto,

disponiendo  así  una  herramienta  útil  para  cargar  y  presentar  contenidos  académicos,

principalmente de alfabetización financiera, pero dejando de lado el estudio de su impacto.

 Aunque Unity permite la exportación del videojuego en múltiples plataformas tales

como Mac, Linux o dispositivos móviles, se enfocó su desarrollo exclusivamente para Windows

al ser la segunda más utilizada y ser un entorno ya trabajó anteriormente, a fin de entregar un

producto  en  completo  y  con  buenos  rendimientos,  pero  dejando  abierta  la  posibilidad  de

expandirlo a más plataformas.

Otra limitante fue el aspecto gráfico del videojuego, pues al ser un juego en 3D se

requiere  de  conocimientos  avanzados  en  modelado  para  crear  diseños  de  personajes  y

escenarios desde cero, por lo que se tuvo que optar por utilizar assets gratuitos y de pago para

socavar  esta  área.  Además  de  utilizar  diferentes  assets  gráficos  y  sonoros  para  el  apartado

artísticos  a fin de optimizar el tiempo y enfocar los esfuerzos en el correcto funcionamiento de

102

sus  mecánicas  y  rendimiento  general. Resultando en un apartado gráfico y artístico aceptable

para una adecuada experiencia de juego, pero con la posibilidad de mejora.

Además, a pesar de que   desarrolló un sensor e implementó dentro del videojuego

el  framework  de  bGames,  al  estar  el  módulo  cloud  aún  en  fase  de  desarrollo,  su  uso queda

actualmente  disponible  únicamente  para  entornos de prueba, limitando su uso para el usuario

final.

7.4. TRABAJO FUTURO

A  pesar  de  que  el  proyecto  realizado  implementa  todo  lo planteado inicialmente,

existen  diversos  aspectos  que  pueden  expandir  o mejorar el videojuego, los cuales no fueron

abordados  durante  desarrollo  debido  a  diversas  limitaciones.  A  continuación,  se  detallan  los

más relevantes.

7.4.1. Compatibilidad a otras plataformas

Dado el tiempo dispuesto para el desarrollo del proyecto, se enfocó los esfuerzos a

hacerlo  compatible  con  buen  rendimiento  para  la  plataforma  de  Windows,  siendo  este  el

segundo  sistema  más  utilizado  a  nivel  mundial  (StatCounter,  2024),  quedando  como  trabajo

futuro  el  expandirlo  a  las  demás  plataformas,  principalmente  a  Android,  el  cual es el sistema

operativo más utilizado (StatCounter, 2024).

7.4.2. Restauración del módulo cloud bGames

Dado  a  que  el  módulo  cloud  del  framework  de  bGames  fue  utilizado  de  manera

local  debido  a  ciertos  problema  que  tiene  la  plataforma  para  operar  durante  el  desarrollo del

proyecto,  dejando  implementado  su  uso  dentro  del  videojuego  pero  quedando  pendiente  la

modificación  de  su API una vez esté finalmente desplegado, de forma que pueda ser utilizado

por el usuario final.

7.4.3. Estudio de impacto

Debido  a  las limitaciones de tiempo del proyecto, se dejó fuera del alcance inicial

todo lo referente a la evaluación del impacto del producto dejando su análisis como un trabajo

futuro que permita dar cuenta de la eficacia de este tipo de soluciones para enfrentar los bajos

índices de alfabetización financiera en el país.

103

7.5. REFLEXIONES FINALES

Este  proyecto  de tesis y memoria consiste en un videojuego serio enfocado en el

aprendizaje  de  conocimientos  financieros  básicos  y  sus  aplicaciones,  a  su  vez que integra el

perfil  multidimensional  del  framework  de  bGames  con  el  que  se  busca  personalizar  la

experiencia de juego e incentivar los buenos hábitos y actividades del entorno del usuario.

La  metodología  de  este  proyecto  siguió  una  planificación  establece  previo  a  su

comienzo,  comenzando  con  la  etapa  de  análisis  y  diseño  en  la  cual  se  diseñaron  e

implementaron  los  prototipos  para  las  mercancías  base  del  videojuego,  fase  la  cual  fue

excedida  por 3 semanas debido a complicación en la integración de la modalidad de juego en

línea, sin embargo la etapa de implementación y testeo se pudo realizar sin complicaciones y de

forma  ágil  abarcando  todos  los  requerimientos  establecidos  gracias  a los correctos prototipos

realizados  en  la  primera  etapa,  de  forma  que  se  recomienda  su  uso  para  estos  tipos  de

proyectos pues permite un trabajo eficiente e incremental.

Se  espera  que  este  proyecto  sirva  como  una  herramienta  que  apoye  la

alfabetización  financiera  en  la  población  joven,  con  el  propósito  de  mejorar,  a  largo  plazo,  la

calidad de vida de las personas a través de una mejor situación financiera obtenida mediante la

adquisición  de  nuevos  conocimientos,  así  como  de  mejores  comportamientos  y  actitudes

financieras.  Además,  se  espera  que  el  proyecto  sea  útil  para  el  trabajo  futuro  realizado  con

Blended  Games  del  laboratorio  Interaction,  a  fin  de  darlo a conocer y alcanzar su objetivo de

adopción en la comunidad de desarrolladores.

104

GLOSARIO

Alfabetización financiera: refiere a la combinación de conocimiento, habilidades,
actitudes  y  comportamientos  financieros  que  una  persona  necesita  para  tomar  decisiones
financieras sólidas y alcanzar el bienestar financiero individual.

Blended  Games  (bGames):  marco  de  trabajo  que  ofrece  un  ambiente  de
desarrollo  de  videojuegos  alimentados  por  acciones  realizadas  en  la  vida  cotidiana  fuera  del
mundo virtual, fomentando una experiencia de juego interactiva y educativa.

Comportamiento financiero: estudio del comportamiento humano en relación con
el manejo del dinero, incluyendo cómo las personas toman decisiones financieras y los factores
psicológicos que influyen en estas decisiones.

Educación  financiera:  proceso  continuo  a  lo  largo  de  la  vida  por  el  cual  las
personas  mejoran  su  entendimiento  del  mundo  financiero  y  desarrollan  habilidades  para
gestionar los riesgos y oportunidades financieras, mejorar su bienestar y el de la sociedad.

Framework: también conocido como esquema o marco de trabajo, es un ambiente
de desarrollo que facilita la creación de aplicaciones y programas, proporcionando estructuras y
herramientas estandarizadas.

Juego  serio:  subcategoría  de  juegos  diseñados con un propósito educativo, que
puede  ser  físico  o  virtual,  y  que  busca  enseñar  o  entrenar  a  los  usuarios  más  allá  del
entretenimiento.

Productos  financieros:  instrumentos  ofrecidos  por  entidades  financieras  que
permiten a los usuarios invertir, ahorrar o financiar bienes y servicios, ajustándose a sus perfiles
de riesgo y rentabilidad.

Riesgo  financiero:  potencial de pérdida económica asociado a las decisiones de
inversión.  Comprender  este  riesgo  es  crucial  para  tomar  decisiones  informadas  y  gestionar
adecuadamente las finanzas personales.

105

REFERENCIAS BIBLIOGRÁFICAS

ABIF. (2022). Educación financiera en Chile: Diagnóstico e iniciativas. ABIF Informa, Nº187.
https://www.abif.cl/abifinforma/abif-informa-no187-alfabetizacion-financiera/
ABIF. (2020). Educación financiera en Chile, realidad y propuestas. Asociación de Bancos e

Instituciones Financieras de Chile.

ABIF & Universidad de Chile. (2021). Mi Barrio Financiero. https://mibarriofinanciero.cl
Almonte, M., & Bravo, J. (2016). Gamificación y e-learning: estudio de un contexto universitario

para la adecuación de su diseño. Revista Tecnología, Ciencia Y Educación.
https://doi.org/10.51302/tce.2016.78

Álvarez, R., & Ruiz-Tagle, J. (2016). Alfabetismo Financiero, Endeudamiento y Morosidad de los

Hogares en Chile. Repositorio Académico de la Universidad de Chile.
https://repositorio.uchile.cl/handle/2250/140521

Borrás Gené, O. (2017). Fundamentos de la gamificación. Rectorado (UPM).

https://oa.upm.es/44745/

Calistro Cayuqueo, D., & González Ibáñez, R. I. (2019). b-Games: framework enfocado en el

desarrollo de servicios de datos para videojuegos mapeando fuentes de información al
perfil de un usuario. Universidad de Santiago de Chile.
https://repositorio.usach.cl/permalink/56USACH_INST/avqbj0/alma991885671606116

CAPIF. (2016). Estrategia Nacional de Educación Financiera. Biblioteca Digital Mineduc.

https://bibliotecadigital.mineduc.cl/handle/20.500.12365/2167

Centro UC. (2017). Estudio de alfabetización y comportamiento financiero en Chile.

https://politicaspublicas.uc.cl/publicacion/estudio-de-alfabetizacion-y-comportamiento-fin
anciero-en-chile/

Cerezo, I. (2022). La gamificación como metodología innovadora en el ámbito educativo.

https://dialnet.unirioja.es/servlet/articulo?codigo=8582784

Comisión para el Mercado Financiero (CMF). (2023). Capacidades Financieras en América

Latina: Chile 2023. Comisión para el Mercado Financiero.
https://www.cmfchile.cl/portal/estadisticas/617/w3-article-76205.html

Comisión para el Mercado Financiero (CMF). (2021). Comisión culmina actividades del Mes de

la Educación Financiera con lanzamiento de nueva versión de su sitio CMF Educa.
https://www.cmfchile.cl/portal/prensa/615/w3-article-49693.html

Comisión para el Mercado Financiero (CMF). (2016). Informe de Inclusión Financiero en Chile

2016. Comisión para el Mercado Financiero.
https://www.cmfchile.cl/portal/estadisticas/617/w3-article-38695.html

Desurvire, H., Caplan, M., & Toth, J. (2004). Using heuristics to evaluate the playability of game.
Epic Games. (2024). Unreal Engine Documentation. https://docs.unrealengine.com/
Garrido Sánchez, A. B., & Crisol Moya, E. (2023). Revisión sistemática: beneficios de los juegos
de mesa en el ámbito de la educación social con menores de entre 6 y 18 años.
Education in the Knowledge Society (EKS). https://doi.org/10.14201/eks.28528

Godot Engine. (2024). Godot Engine Documentation. https://docs.godotengine.org/
Instituto Nacional de la Juventud (INJUV). (2024). Juventudes y juegos.

https://www.injuv.gob.cl/personas/noticias/8-de-cada-10-jovenes-declara-que-ha-jugado-
o-visto-juegos-online-alguna-vez-en-su-vida

Lizama Hernández, E. A. (2022). Street Blocks: videojuego Beat ‘em up aplicando el framework

blended games. Universidad de Santiago de Chile.

106

Lusardi, A. (2019). Financial literacy and the need for financial education: Evidence and

implications. Swiss Journal of Economics and Statistics. 155(1), 1-8.

Lusardi, A., & Mitchell, O. S. (2011). Financial literacy around the world: An overview. Journal of

Pension Economics and Finance. 10(4), 497-508.

Lusardi, A., & Tufano, P. (2015). Debt literacy, financial experiences, and overindebtedness.
NBER Working Paper No. 14808. National Bureau of Economic Research.
https://doi.org/10.3386/w14808

Mahu Urbina, L. K. (2020). Ambiente para el almacenamiento y disponibilización ubicua de

perfiles de usuario del framework BlendedGames. Universidad de Santiago de Chile.

Martin, J. (1991). Rapid application development. Macmillan Publishing.
Massad, C. (2004). Economía para todos. Banco Central de Chile.
NVIDIA Corporation. (2022). FrameView Integrated Frame Benchmarking & Power Tool User

Guide.
https://images.nvidia.com/content/geforce/technologies/frameview/frameview-1-4-user-g
uide-web-version.pdf.

Plump, C., & LaRosa, J. (2017). Using Kahoot! in the Classroom to Create Engagement and
Active Learning: A Game-Based Technology Solution for eLearning Novices.
ResearchGate.
https://www.researchgate.net/publication/313418401_Using_Kahoot_in_the_Classroom
_to_Create_Engagement_and_Active_Learning_A_Game-Based_Technology_Solution_
for_eLearning_Novices

Popovich, J. J., Loibl, C., Zirkle, C., & Whittington, M. S. (2020). Community college students’

response to a financial literacy intervention: An exploratory study. International Review
of Economics Education. 34. 100182

Rus Arias, E. (2024). Producto financiero.

https://economipedia.com/definiciones/producto-financiero.html

Schwaber, K., & Sutherland, J. (2020). The Scrum Guide. Scrum Alliance.

https://scrumguides.org/scrum-guide.html

SERNAC. (2020). Curso para Docentes Educación para el Consumo en la Escuela 2020.

Servicio Nacional del Consumidor.
https://www.sernac.cl/portal/607/w3-article-58287.html

Sommerville, I. (2011). Ingeniería de requerimientos. En Ingeniería de software (pp. 84-91).
StatCounter. (2024). Operating System Market Share Worldwide.

https://gs.statcounter.com/os-market-share#monthly-202307-202407
Ternero Silva, G. A. (2022). Village Defender : videojuego de estrategia multiplataforma

aplicando el framework Blended Games. Universidad de Santiago de Chile.
Thomas, B., & Subhashreeb, P. (2020). Factors that Influence the Financial Literacy among

Engineering Students. 172, 480-487.

Unity. (2024). Unity Documentation. https://docs.unity3d.com/Manual/PlatformSpecific.html
Vanguard. (2011). Descripción de My Classroom Economy. My Classroom Economy.

https://myclassroomeconomy.org/overview

Zelada Korze, N. G. (2023). Restauración del módulo cloud de bGames. Universidad de

Santiago de Chile.

Zhonggen, Y. (2019). A Meta-Analysis of Use of Serious Games in Education over a Decade.

1-8. https://www.hindawi.com/journals/ijcgt/2019/4797032/

107

ANEXO A. CARTA DE PATROCINIO

108

APÉNDICE A. PREGUNTAS MÓDULO FINANCIERO INICIAL

Tabla A.1: Pregunta para el banco inicial Q01.

Fuente: elaboración propia, 2024.

ID

Q01

Pregunta

¿Qué significa la sigla IPC?

Alternativas

(a) Índice de Producción Comercial
(b) Indicador de Progreso del Capital
(c) Índice de Precios al Consumidor

Respuesta

(c) Índice de Precios al Consumidor

Temática

Indicadores económicos

Sub-Temática

Inflación

Nivel
(Dificultad)

1

Tabla A.2: Pregunta para el banco inicial Q02.

Fuente: elaboración propia, 2024.

ID

Q02

Pregunta

¿Qué es la inflación?

Alternativas

(a) La disminución de la producción
(b) El aumento generalizado de los precios
(c) El aumento del PIB

Respuesta

(b) El aumento generalizado de los precios

Temática

Conceptos fundamentales

Sub-Temática

Inflación

Nivel
(Dificultad)

1

109

Tabla A.3: Pregunta para el banco inicial Q03.

Fuente: elaboración propia, 2024.

ID

Q03

Pregunta

¿Qué representa el PIB (Producto Interno Bruto)?

Alternativas

(a) El ingreso promedio por persona
(b) Los gastos de las familias
(c) La suma del valor total de bienes y servicios producidos en un país

Respuesta

(c) La suma del valor total de bienes y servicios producidos en un país

Temática

Indicadores económicos

Sub-Temática  Economía

Nivel
(Dificultad)

1

Tabla A.4: Pregunta para el banco inicial Q04.

Fuente: elaboración propia, 2024.

ID

Q04

Pregunta

¿Qué significa "ahorrar"?

Alternativas

(a) Invertir en acciones
(b) Guardar dinero para usos futuros
(c) Gastar menos de lo que ganas

Respuesta

(b) Guardar dinero para usos futuros

Temática

Planificación financiera

Sub-Temática  Ahorro

Nivel
(Dificultad)

1

110

Tabla A.5: Pregunta para el banco inicial Q05.

Fuente: elaboración propia, 2024.

ID

Q05

Pregunta

¿Qué es un presupuesto?

Alternativas

(a) Un plan para gestionar ingresos y gastos
(b) Un registro de deudas acumuladas
(c) Un documento que detalla impuestos

Respuesta

(a) Un plan para gestionar ingresos y gastos

Temática

Gestión de presupuestos y deudas

Sub-Temática  Presupuesto

Nivel
(Dificultad)

1

Tabla A.6: Pregunta para el banco inicial Q06.

Fuente: elaboración propia, 2024.

ID

Q06

Pregunta

¿Qué significa "diversificación" en finanzas?

Alternativas

(a) Usar solo un tipo de activo financiero
(b) Incrementar la deuda para invertir
(c) Distribuir inversiones en diferentes tipos de activos para reducir el riesgo

Respuesta

(c) Distribuir inversiones en diferentes tipos de activos para reducir el riesgo

Temática

Conceptos fundamentales

Sub-Temática

Inversión

Nivel
(Dificultad)

1

111

Tabla A.7: Pregunta para el banco inicial Q07.

Fuente: elaboración propia, 2024.

ID

Q07

Pregunta

¿Qué es un gasto fijo?

Alternativas

(a) Un gasto opcional
(b) Un gasto que no varía mes a mes, como el arriendo
(c) Un gasto que cambia cada mes

Respuesta

(b) Un gasto que no varía mes a mes, como el arriendo

Temática

Gestión de presupuestos y deudas

Sub-Temática  Presupuesto

Nivel
(Dificultad)

1

Tabla A.8: Pregunta para el banco inicial Q08.

Fuente: elaboración propia, 2024.

ID

Q08

Pregunta

¿Qué es la tasa de interés?

Alternativas

(a) El porcentaje que pagas o ganas sobre una cantidad de dinero
(b) El precio de las acciones en la bolsa
(c) El valor de una moneda en otro país

Respuesta

(a) El porcentaje que pagas o ganas sobre una cantidad de dinero

Temática

Conceptos fundamentales

Sub-Temática

Interés

Nivel
(Dificultad)

1

112

Tabla A.9: Pregunta para el banco inicial Q09.

Fuente: elaboración propia, 2024.

ID

Q09

Pregunta

¿Qué es el interés compuesto?

Alternativas

(a) Intereses generados sobre el capital inicial
(b) Intereses generados sobre el capital inicial y sobre los intereses
acumulados
(c) Un tipo de impuesto

Respuesta

(b) Intereses generados sobre el capital inicial y sobre los intereses
acumulados

Temática

Conceptos fundamentales

Sub-Temática

Interés

Nivel
(Dificultad)

1

Tabla A.10: Pregunta para el banco inicial Q10.

Fuente: elaboración propia, 2024.

ID

Q10

Pregunta

¿Qué es el crédito?

Alternativas

(a) Dinero que ahorras
(b) Dinero que te presta una entidad o persona
(c) Un tipo de inversión en bonos"

Respuesta

(b) Dinero que te presta una entidad o persona

Temática

Gestión de presupuestos y deudas

Sub-Temática  Deuda

Nivel
(Dificultad)

1

113

Tabla A.11: Pregunta para el banco inicial Q11.

Fuente: elaboración propia, 2024.

ID

Q11

Pregunta

¿Qué es el fondo de emergencia?

Alternativas

(a) Dinero destinado a inversiones de riesgo
(b) Dinero reservado para gastos inesperados
(c) Dinero destinado a pagar impuestos

Respuesta

(b) Dinero reservado para gastos inesperados

Temática

Planificación financiera

Sub-Temática  Ahorro

Nivel
(Dificultad)

1

Tabla A.12: Pregunta para el banco inicial Q12.

Fuente: elaboración propia, 2024.

ID

Q12

Pregunta

¿Qué es el historial crediticio?

Alternativas

(a) Una lista de tus cuentas bancarias
(b) Un registro de tus actividades y comportamientos financieros con el
crédito
(c )Una cuenta de ahorros

Respuesta

(b) Un registro de tus actividades y comportamientos financieros con el
crédito

Temática

Gestión de presupuestos y deudas

Sub-Temática  Deuda

Nivel
(Dificultad)

1

114

Tabla A.13: Pregunta para el banco inicial Q13.

Fuente: elaboración propia, 2024.

ID

Q13

Pregunta

¿Qué significa “invertir”?

Alternativas

(a) Guardar todo el dinero sin usarlo
(b) Destinar recursos a un proyecto esperando generar beneficios
(c) Gastar en bienes innecesarios

Respuesta

(b) Destinar recursos a un proyecto esperando generar beneficios

Temática

Planificación financiera

Sub-Temática

Inversión

Nivel
(Dificultad)

1

Tabla A.14: Pregunta para el banco inicial Q14.

Fuente: elaboración propia, 2024.

ID

Q14

Pregunta

¿Qué es la TPM (Tasa de Política Monetaria)?

Alternativas

(a) Tasa a la cual el Banco Central le presta a los bancos comerciales
(b) Un impuesto aplicado a la inversión extranjera
(c) El porcentaje de ingresos destinado al ahorro

Respuesta

(a) Tasa a la cual el Banco Central le presta a los bancos comerciales

Temática

Indicadores económicos

Sub-Temática  Economía

Nivel
(Dificultad)

1

115

Tabla A.15: Pregunta para el banco inicial Q15.

Fuente: elaboración propia, 2024.

ID

Q15

Pregunta

¿Qué es el IVA (Impuesto al Valor Agregado)?

Alternativas

(a) Un impuesto que se aplica al consumo de bienes y servicios
(b) Un impuesto directo sobre los ingresos personales
(c) Un descuento aplicado por el gobierno

Respuesta

(a) Un impuesto que se aplica al consumo de bienes y servicios

Temática

Indicadores económicos

Sub-Temática  Economía

Nivel
(Dificultad)

1

Tabla A.16: Pregunta para el banco inicial Q16.

Fuente: elaboración propia, 2024.

ID

Q16

Pregunta

¿Qué es una deuda?

Alternativas

(a) Dinero que una persona o entidad debe pagar
(b) Un ahorro destinado a emergencias
(c) Un ingreso generado por inversiones

Respuesta

(a) Dinero que una persona o entidad debe paga

Temática

Gestión de presupuestos y deudas

Sub-Temática

Inversión

Nivel
(Dificultad)

1

116

Tabla A.17: Pregunta para el banco inicial Q17.

Fuente: elaboración propia, 2024.

ID

Q17

Pregunta

¿Qué es una acción (stock)?

Alternativas

(a) Una unidad que representa propiedad parcial en una empresa
(b) Un impuesto aplicado a los ingresos empresariales
(c) Un tipo de préstamo personal

Respuesta

(a) Una unidad que representa propiedad parcial en una empresa

Temática

Planificación financiera

Sub-Temática

Inversión

Nivel
(Dificultad)

1

Tabla A.18: Pregunta para el banco inicial Q18.

Fuente: elaboración propia, 2024.

ID

Q18

Pregunta

¿Qué es un dividendo?

Alternativas

(a)  Una  parte  de  las  ganancias  de  una  empresa  que  se  distribuye  a  sus
accionistas
(b) Un impuesto aplicado a los ahorros personales
(c) El valor de una acción en el mercado

Respuesta

(a)  Una  parte  de  las  ganancias  de  una  empresa  que  se  distribuye  a  sus
accionistas

Temática

Planificación financiera

Sub-Temática

Inversión

Nivel
(Dificultad)

1

117

Tabla A.19: Pregunta para el banco inicial Q19.

Fuente: elaboración propia, 2024.

ID

Q19

Pregunta

¿Qué es un gasto hormiga?

Alternativas

(a) Pequeños gastos diarios que parecen insignificantes pero que se
acumulan con el tiempo
(b) Una inversión de bajo riesgo
(c) Un gasto fijo como el arriendo

Respuesta

(a) Pequeños gastos diarios que parecen insignificantes pero que se
acumulan con el tiempo

Temática

Gestión de presupuestos y deudas

Sub-Temática  Presupuesto

Nivel
(Dificultad)

1

Tabla A.18: Pregunta para el banco inicial Q20.

Fuente: elaboración propia, 2024.

ID

Q20

Pregunta

¿Qué es la UF (Unidad de Fomento)?

Alternativas

(a) Una medida de inflación utilizada para ajustar valores en Chile
(b) Un impuesto sobre los ingresos altos
(c) El salario mínimo mensual

Respuesta

(a) Una medida de inflación utilizada para ajustar valores en Chile

Temática

Indicadores económicos

Sub-Temática  Economía

Nivel
(Dificultad)

1

118

Tabla A.21: Pregunta para el banco inicial Q21.

Fuente: elaboración propia, 2024.

ID

Q21

Pregunta

¿Qué es el poder adquisitivo?

Alternativas

a) La cantidad de bienes o servicios que puedes comprar con tu dinero
(b) El interés generado por una cuenta de ahorros
(c) El total de tus ingresos mensuales

Respuesta

(a) La cantidad de bienes o servicios que puedes comprar con tu dinero

Temática

Conceptos fundamentales

Sub-Temática

Inflación

Nivel
(Dificultad)

1

Tabla A.22: Pregunta para el banco inicial Q22.

Fuente: elaboración propia, 2024.

ID

Q22

Pregunta

¿Qué es un ETF (Exchange-Traded Fund)?

Alternativas

(a) Un fondo que se negocia en la bolsa y sigue el rendimiento de un índice
o activo
(b) Un tipo de bono emitido por el gobierno
(c) Una cuenta de ahorro especial

Respuesta

(a) Un fondo que se negocia en la bolsa y sigue el rendimiento de un índice
o activo

Temática

Planificación financiera

Sub-Temática

Inversión

Nivel
(Dificultad)

1

119

Tabla A.23: Pregunta para el banco inicial Q23.

Fuente: elaboración propia, 2024.

ID

Q23

Pregunta

¿Qué es un fondo mutuo?

Alternativas

(a)  Un  conjunto  de  dinero  de  varios  inversionistas  que  se invierte en una
variedad de activos
(b) Un tipo de cuenta de ahorro con altas tasas de interés
(c) Una empresa que otorga préstamos a corto plazo

Respuesta

(a)  Un  conjunto  de  dinero  de  varios  inversionistas  que  se invierte en una
variedad de activos

Temática

Planificación financiera

Sub-Temática

Inversión

Nivel
(Dificultad)

1

Tabla A.24: Pregunta para el banco inicial Q24.

Fuente: elaboración propia, 2024.

ID

Q24

Pregunta

¿Qué es un Depósito a Plazo (DAP)?

Alternativas

(a)  Una  inversión  donde  se  deposita  dinero  en  un  banco  por  un  tiempo
definido y se recibe un interés
(b) Un préstamo otorgado por una entidad financiera
(c) Una cuenta corriente con acceso inmediato al dinero

Respuesta

(a)  Una  inversión  donde  se  deposita  dinero  en  un  banco  por  un  tiempo
definido y se recibe un interés

Temática

Planificación financiera

Sub-Temática  Ahorro

Nivel
(Dificultad)

1

120

Tabla A.25: Pregunta para el banco inicial Q25.

Fuente: elaboración propia, 2024.

ID

Q25

Pregunta

¿Qué diferencia principal existe entre un bono y una acción?

Alternativas

(a) Los bonos representan deuda y las acciones propiedad
(b) Las acciones tienen tasas de interés fijas
(c) Los bonos no generan rendimientos

Respuesta

(a) Los bonos representan deuda y las acciones propiedad

Temática

Planificación financiera

Sub-Temática

Inversión

Nivel
(Dificultad)

1

Tabla A.26: Pregunta para el banco inicial Q26.

Fuente: elaboración propia, 2024.

ID

Q26

Pregunta

¿Qué es la demanda en economía?

Alternativas

(a)  La  cantidad  de  bienes  y  servicios  que  los  consumidores  desean
comprar
(b) La cantidad de productos ofrecidos por las empresas
(c) El precio de un bien en el mercado

Respuesta

(a)  La  cantidad  de  bienes  y  servicios  que  los  consumidores  desean
comprar

Temática

Indicadores económicos

Sub-Temática  Economía

Nivel
(Dificultad)

1

121

Tabla A.27: Pregunta para el banco inicial Q27.

Fuente: elaboración propia, 2024.

ID

Q27

Pregunta

¿Qué es la oferta en economía?

Alternativas

(a) El precio máximo que los consumidores están dispuestos a pagar
(b) La cantidad de bienes y servicios que las empresas están dispuestas a
vender
(c) Los gastos del gobierno en el mercado

Respuesta

(b) La cantidad de bienes y servicios que las empresas están dispuestas a
vender

Temática

Indicadores económicos

Sub-Temática  Economía

Nivel
(Dificultad)

1

Tabla A.28: Pregunta para el banco inicial Q28.

Fuente: elaboración propia, 2024.

ID

Q28

Pregunta

¿Qué es el patrimonio en términos financieros?

Alternativas

(a) La suma de todos los ingresos mensuales
(b)  La  diferencia  entre  los  activos  (lo  que  posees)  y  los  pasivos  (lo  que
debes)
(c) El dinero guardado en una cuenta de ahorro

Respuesta

(b)  La  diferencia  entre  los  activos  (lo  que  posees)  y  los  pasivos  (lo  que
debes)

Temática

Planificación financiera

Sub-Temática

Inversión

Nivel
(Dificultad)

1

122

Tabla A.29: Pregunta para el banco inicial Q29.

Fuente: elaboración propia, 2024.

ID

Q29

Pregunta

Supongamos  que  tienes  $100  en  una cuenta de ahorros con una tasa de
interés del 2% anual. Después de 5 años, ¿cuánto dinero tendrías si dejas
que crezca?

Alternativas

(a) Más de $102
(b) Exactamente $102
(c) Menos de $102

Respuesta

(a) Más de $102

Temática

Planificación financiera

Sub-Temática  Ahorro

Nivel
(Dificultad)

2

Tabla A.30: Pregunta para el banco inicial Q30.

Fuente: elaboración propia, 2024.

ID

Q30

Pregunta

Si la tasa de interés de tu cuenta de ahorros es del 1% anual y la inflación
es  del  2% anual, ¿qué ocurre con el poder adquisitivo del dinero después
de un año?

Alternativas

(a) Aumenta
(b) Se mantiene igual
(c) Disminuye

Respuesta

(c) Disminuye

Temática

Conceptos fundamentales

Sub-Temática

Inflación

Nivel
(Dificultad)

2

123

Tabla A.31: Pregunta para el banco inicial Q31.

Fuente: elaboración propia, 2024.

ID

Q31

Pregunta

¿Qué  sucede  con  el  riesgo  de perder dinero al invertir en diferentes tipos
de activos en lugar de solo uno?

Alternativas

(a) Aumenta
(b) Disminuye
(c) Permanece igual

Respuesta

(b) Disminuye

Temática

Planificación financiera

Sub-Temática

Inversión

Nivel
(Dificultad)

2

Tabla A.32: Pregunta para el banco inicial Q32.

Fuente: elaboración propia, 2024.

ID

Q32

Pregunta

¿Es más seguro comprar acciones de una sola empresa o un fondo mutuo
diversificado?

Alternativas

(a) Comprar acciones de una sola empresa
(b) Comprar un fondo mutuo
(c) Ambas son igual de seguras

Respuesta

(b) Comprar un fondo mutuo

Temática

Planificación financiera

Sub-Temática

Inversión

Nivel
(Dificultad)

2

124

Tabla A.33: Pregunta para el banco inicial Q33.

Fuente: elaboración propia, 2024.

ID

Q33

Pregunta

¿Qué inversión tiende a ser más riesgosa en el corto plazo?

Alternativas

(a) Bonos
(b) Cuentas de ahorro
(c) Acciones

Respuesta

(c) Acciones

Temática

Planificación financiera

Sub-Temática

Inversión

Nivel
(Dificultad)

2

Tabla A.34: Pregunta para el banco inicial Q34.

Fuente: elaboración propia, 2024.

ID

Q34

Pregunta

Considerando  un  período  de  10  a  20  años,  ¿qué  activo  generalmente
ofrece el mayor retorno?

Alternativas

(a) Cuentas de ahorro
(b) Bonos
(c) Acciones

Respuesta

(c) Acciones

Temática

Planificación financiera

Sub-Temática

Inversión

Nivel
(Dificultad)

2

125

Tabla A.35: Pregunta para el banco inicial Q35.

Fuente: elaboración propia, 2024.

ID

Q35

Pregunta

Si  compras  un  producto  que cuesta $1.000 y pagas el 19% de IVA, ¿cuál
es el monto total a pagar?

Alternativas

(a) $1.090
(b) $1.190
(c) $1.210

Respuesta

(b) $1.190

Temática

Indicadores económicos

Sub-Temática

Impuestos

Nivel
(Dificultad)

2

Tabla A.36: Pregunta para el banco inicial Q36.

Fuente: elaboración propia, 2024.

ID

Q36

Pregunta

Si  utilizas  tu  tarjeta  de  crédito  y  pagas  solo  el  mínimo  cada  mes,  ¿qué
ocurre con los intereses que debes pagar?

Alternativas

(a) Aumentan
(b) Se mantienen igual
(c) Disminuyen

Respuesta

(a) Aumentan

Temática

Gestión de presupuestos

Sub-Temática  Deudas

Nivel
(Dificultad)

2

126

Tabla A.37: Pregunta para el banco inicial Q37.

Fuente: elaboración propia, 2024.

ID

Q37

Pregunta

Un dividendo de $500 por acción es anunciado por una empresa en la que
tienes 10 acciones. ¿Cuánto recibirás en total?

Alternativas

(a) $5.000
(b) $50
(c) $500

Respuesta

(a) $5.000

Temática

Planificación financiera

Sub-Temática

Inversión

Nivel
(Dificultad)

2

Tabla A.38: Pregunta para el banco inicial Q38.

Fuente: elaboración propia, 2024.

ID

Q38

Pregunta

Si  un  bien  aumenta  de  precio  debido  a  que  más  personas  quieren
comprarlo, ¿qué está ocurriendo?

Alternativas

(a) Disminución de la demanda
(b) Aumento de la demanda
(c) Disminución de la oferta

Respuesta

(b) Aumento de la demanda

Temática

Indicadores económicos

Sub-Temática  Economía

Nivel
(Dificultad)

2

127

Tabla A.39: Pregunta para el banco inicial Q39.

Fuente: elaboración propia, 2024.

ID

Q39

Pregunta

Si  la  Tasa  de  Política  Monetaria  (TPM)  aumenta,  ¿cómo  afecta  esto  al
costo de los créditos bancarios?

Alternativas

(a) Los hace más baratos
(b) No los afecta
(c) Los hace más caros

Respuesta

(c) Los hace más caros

Temática

Indicadores económicos

Sub-Temática  Economía

Nivel
(Dificultad)

2

Tabla A.40: Pregunta para el banco inicial Q40.

Fuente: elaboración propia, 2024.

ID

Q40

Pregunta

¿Qué  ocurre  con el precio de un activo si la oferta de ese activo aumenta
significativamente?

Alternativas

(a) El precio aumenta
(b) El precio disminuye
(c) El precio no se ve afectado

Respuesta

(b) El precio disminuye

Temática

Indicadores económicos

Sub-Temática  Economía

Nivel
(Dificultad)

2

128

Tabla A.41: Pregunta para el banco inicial Q41.

Fuente: elaboración propia, 2024.

ID

Q41

Pregunta

¿Cuáles son los 5 factores que influyen en su historial crediticio?

Alternativas

(a) Monto de la deuda, la tasa de interés más alta, número de tarjetas de
crédito, morosidad, excedentes
(b) Historial de pago, índice de utilización, aplicaciones de crédito nuevas,
duración del uso del crédito, tipos de crédito en su historial
(c) Linda sonrisa, actitud ganadora, prometer ser más responsable, el
encantamiento correcto para un puntaje de crédito, ojo de tritón

Respuesta

(b) Historial de pago, índice de utilización, aplicaciones de crédito nuevas,
duración del uso del crédito, tipos de crédito en su historial

Temática

Gestión de presupuestos y deudas

Sub-Temática  Créditos

Nivel
(Dificultad)

2

Tabla A.42: Pregunta para el banco inicial Q42.

Fuente: elaboración propia, 2024.

ID

Q42

Pregunta

Si tienes una deuda con una tasa de interés variable y la TPM sube, ¿qué
pasa con tu pago mensual?

Alternativas

(a) Disminuye
(b) Aumenta
(c) Se mantiene igual

Respuesta

(b) Aumenta

Temática

Gestión de presupuestos y deudas

Sub-Temática  Deudas

Nivel
(Dificultad)

2

129

Tabla A.43: Pregunta para el banco inicial Q43.

Fuente: elaboración propia, 2024.

ID

Q43

Pregunta

En un período de alta inflación, ¿qué ocurre con el valor real de los ahorros
en efectivo?

Alternativas

(a) Aumenta
(b) Disminuye
(c) No se ve afectado

Respuesta

(b) Disminuye

Temática

Conceptos fundamentales

Sub-Temática

Inflación

Nivel
(Dificultad)

2

Tabla A.44: Pregunta para el banco inicial Q44.

Fuente: elaboración propia, 2024.

ID

Q44

Pregunta

Si  decides  ahorrar  en  una  cuenta  en  UF,  ¿qué  beneficio  tiene  esto  en
comparación con una cuenta en pesos?

Alternativas

a) Protege los ahorros de la inflación
(b) Genera mayores tasas de interés
(c) Evita pagar impuestos

Respuesta

(a) Protege los ahorros de la inflación

Temática

Indicadores económicos

Sub-Temática

Inflación

Nivel
(Dificultad)

2

130

Tabla A.45: Pregunta para el banco inicial Q45.

Fuente: elaboración propia, 2024.

ID

Q45

Pregunta

Si  una  persona  invierte  en  una  acción  que  paga  dividendos,  pero  decide
reinvertir esos dividendos, ¿qué sucede con su inversión?

Alternativas

(a) Se mantiene igual
(b) Aumenta más rápidamente
(c) Disminuye lentamente

Respuesta

(b) Aumenta más rápidamente

Temática

Planificación financiera

Sub-Temática

Inversión

Nivel
(Dificultad)

2

Tabla A.46: Pregunta para el banco inicial Q46.

Fuente: elaboración propia, 2024.

ID

Q46

Pregunta

Si  tienes  un  fondo  de  emergencia  equivalente  a  6  meses  de  gastos  y
pierdes tu empleo, ¿qué ventaja tiene este fondo?

Alternativas

(a) Reduce la necesidad de usar tarjetas de crédito o pedir préstamos
(b) Garantiza empleo nuevo inmediato
(c) Aumenta tus ingresos mensuales

Respuesta

(a) Reduce la necesidad de usar tarjetas de crédito o pedir préstamos

Temática

Planificación financiera

Sub-Temática  Ahorro

Nivel
(Dificultad)

2

131

Tabla A.47: Pregunta para el banco inicial Q47.

Fuente: elaboración propia, 2024.

ID

Q47

Pregunta

Compras  un  ETF  por  $100  y  después  de  un  año  el  valor  del  índice  que
replica  sube  un  8%.  Además,  el  ETF  pagó  un  dividendo  anual  del  2%.
¿Cuál es el rendimiento total?

Alternativas

(a) 8%
(b) 10%
(c) 12%

Respuesta

(b) 10%

Temática

Planificación financiera

Sub-Temática

Inversión

Nivel
(Dificultad)

3

Tabla A.48: Pregunta para el banco inicial Q48.

Fuente: elaboración propia, 2024.

ID

Q48

Pregunta

Un  crédito  hipotecario  tiene  una  tasa  fija  anual  del  4%  y  un  plazo  de  15
años. Si pides $50.000, ¿cuánto pagarás de intereses totales?

Alternativas

(a) $15.000
(b) $30.000
(c) $20.000

Respuesta

(b) $30.000

Temática

Gestión de presupuestos y deudas

Sub-Temática  Créditos

Nivel
(Dificultad)

3

132

Tabla A.49: Pregunta para el banco inicial Q49.

Fuente: elaboración propia, 2024.

ID

Q49

Pregunta

Compras 100 acciones a $15 cada una y las vendes a $20 cada una. ¿Cuál
es tu ganancia total?

Alternativas

(a) $400
(b) $500
(c) $600

Respuesta

(b) $500

Temática

Planificación financiera

Sub-Temática

Inversión

Nivel
(Dificultad)

3

Tabla A.50: Pregunta para el banco inicial Q50.

Fuente: elaboración propia, 2024.

ID

Q50

Pregunta

Compras  50  acciones  de  una  empresa  a  $20  cada  una.  Después  de  un
año,  las acciones valen $25 cada una y la empresa paga un dividendo de
$2 por acción. ¿Cuál es tu ganancia total?

Alternativas

(a) $250
(b) $350
(c) $300

Respuesta

(b) $350

Temática

Planificación financiera

Sub-Temática

Inversión

Nivel
(Dificultad)

3

133

Tabla A.51: Pregunta para el banco inicial Q51.

Fuente: elaboración propia, 2024.

ID

Q51

Pregunta

Si  decides  diversificar  una  inversión  de  $10.000  distribuyendose  en  50%
acciones (6% anual), 30% bonos (3% anual) y 20% en efectivo (1% anual),
¿cuál es el rendimiento promedio esperado al cabo de un año?

Alternativas

(a) 4,1%
(b) 5%
(c) 4,8%

Respuesta

(a) 4,1%

Temática

Planificación financiera

Sub-Temática

Inversión

Nivel
(Dificultad)

3

Tabla A.52: Pregunta para el banco inicial Q52.

Fuente: elaboración propia, 2024.

ID

Q52

Pregunta

Inviertes $10.000 en un ETF con un rendimiento del 9% anual, pero pagas
un 1% de costos. ¿Cuál es tu ganancia neta?

Alternativas

(a) $800
(b) $900
(c) $1.000

Respuesta

(a) $800

Temática

Planificación financiera

Sub-Temática

inversión

Nivel
(Dificultad)

3

134

Tabla A.53: Pregunta para el banco inicial Q53.

Fuente: elaboración propia, 2024.

ID

Q53

Pregunta

Si  la  inflación  sube  por  encima  del  10%  y  tus  ahorros  están  en  efectivo,
¿qué ocurre con tu poder adquisitivo?

Alternativas

(a) Mejora significativamente
(b) Se mantiene igual
(c) Disminuye drásticamente

Respuesta

(c) Disminuye drásticamente

Temática

Conceptos fundamentales

Sub-Temática

Inflación

Nivel
(Dificultad)

3

Tabla A.54: Pregunta para el banco inicial Q54.

Fuente: elaboración propia, 2024.

ID

Q54

Pregunta

¿Qué puede indicar una Tasa de Política Monetaria (TPM) en aumento?

Alternativas

(a) Que el banco central quiere estimular la economía
(b) Que el banco central busca frenar la inflación
(c) Que los bancos necesitan más liquidez

Respuesta

(b) Que el banco central busca frenar la inflación

Temática

Indicadores económicos

Sub-Temática  Economía

Nivel
(Dificultad)

3

135

Tabla A.55: Pregunta para el banco inicial Q55.

Fuente: elaboración propia, 2024.

ID

Q55

Pregunta

Si tu índice de utilización de crédito es alto, ¿cómo afecta esto a tu historial
crediticio?

Alternativas

(a) Lo mejora
(b) Lo empeora
(c) No tiene ningún efecto

Respuesta

(b) Lo empeora

Temática

Gestión de presupuestos y deudas

Sub-Temática  Créditos

Nivel
(Dificultad)

3

Tabla A.56: Pregunta para el banco inicial Q56.

Fuente: elaboración propia, 2024.

ID

Q56

Pregunta

Si  inviertes  en  un  fondo  de  renta  variable,  ¿qué  puedes  esperar  en
comparación con uno de renta fija?

Alternativas

(a) Mayor volatilidad pero también mayor potencial de retorno
(b) Mayor estabilidad y menores rendimientos
(c) No hay diferencia significativa

Respuesta

(a) Mayor volatilidad pero también mayor potencial de retorno

Temática

Planificación financiera

Sub-Temática

Inversión

Nivel
(Dificultad)

3

136

APÉNDICE B. DETALLES DE IMPLEMENTACIÓN

Apéndice B.1 Interfaces del videojuego

Figura B.1: Interfaz de inicio de sesión.

Fuente: elaboración propia, 2024.

Figura B.2: Interfaz de registro.

Fuente: elaboración propia, 2024.

137

Figura B.3: Interfaz de recuperación de contraseña.

Fuente: elaboración propia, 2024.

Figura B.4: Interfaz de inicio.

Fuente: elaboración propia, 2024.

138

Figura B.5: Interfaz de contenido.

Fuente: elaboración propia, 2024.

Figura B.6: Interfaz de crear contenido.

Fuente: elaboración propia, 2024.

139

Figura B.7: Interfaz de perfil de usuario.

Fuente: elaboración propia, 2024.

Figura B.8: Interfaz de opciones.

Fuente: elaboración propia, 2024.

140

Figura B.9: Interfaz de modos.

Fuente: elaboración propia, 2024.

Figura B.10: Interfaz de modos multijugador local.

Fuente: elaboración propia, 2024.

141

Figura B.11: Interfaz de modos multijugador en línea.

Fuente: elaboración propia, 2024.

Figura B.12: Interfaz de sala en línea.

Fuente: elaboración propia, 2024.

142

Apéndice B.2 Sistema de guardado

{
    "initialPlayerIndex": 0,
    "yearsToPlay": 10,
    "mode": 1,
    "currentYear": 1,
    "turnPlayer": 0,
    "timePlayed": "00:00:00",
    "content": "Contenido Básico",
    "allQuestionList": [
        {
            "question": "¿Qué significa la sigla IPC?",
            "answers": [
                "Índice de Producción Comercial",
                "Indicador de Progreso del Capital",
                "Índice de Precios al Consumidor"
            ],
            "indexCorrectAnswer": 2,
            "topic": "Indicadores económicos",
            "subTopic": "Inflación",
            "level": 1
        }
    ],
    "questionList": [
        {
            "question": "¿Qué es la inflación?",
            "answers": [
                "La disminución de la producción",
                "El aumento generalizado de los precios",
                "El aumento del PIB"
            ],
            "indexCorrectAnswer": 1,
            "topic": "Conceptos fundamentales",
            "subTopic": "Inflación",
            "level": 1
        }
    ],

Código B.1: Archivo de guardado de partida en curso sin encriptado - Parte I.

Fuente: elaboración propia, 2024.

143

    "playersData": [
        {
            "uid": "player_001",
            "nickName": "PlayerOne",
            "characterID": 1,
            "finalScore": 1500,
            "position": 5,
            "points": 200,
            "level": 2,
            "money": 1000,
            "invest": 500,
            "debt": 200,
            "income": 1200,
            "expense": 300,
            "investments": [
                {
                    "nameInvestment": "Real Estate",
                    "turns": 5,
                    "capital": 1000,
                    "pctChanges": [
                        0.05,
                        0.03,
                        0.07
                    ],
                    "pctDividend": [
                        0.02,
                        0.02,
                        0.03
                    ]
                }
            ],
            "expenses": [
                {
                    "turns": 3,
                    "cost": 100
                }
            ]
        }
    ],

Código B.2: Archivo de guardado de partida en curso sin encriptado  - Parte II.

Fuente: elaboración propia, 2024.

144

    "expenseCards": [
        {
            "title": "Costo de luz",
            "image": "path/to/image.png",
            "duration": 12,
            "cost": 100
        }
    ],
    "investmentCards": [
        {
            "title": "Inversión en acciones",
            "image": "path/to/image.png",
            "duration": 10,
            "startYear": 2025,
            "pctChangePrevious": [ 5.2,  7.3, -2.1, 4.5 ],
            "pctChange": [ 3.5, 6.0, 2.1 ],
            "pctDividend": [ 0.03, 0.02, 0.04 ]
        }
    ],
    "incomeCards": [
        {
            "title": "Aumento de salario",
            "image": "path/to/image.png",
            "affectIncome": true,
            "incomeChange": 500,
            "income": 0
        }
    ],
    "eventCards": [
        {
            "title": "Evento inesperado",
            "image": "path/to/image.png",
            "amount": -200
        }
    ]
}

Código B.3: Archivo de guardado de partida en curso sin encriptado  - Parte III.

Fuente: elaboración propia, 2024.

145

{
  "userId": "1",
  "gameID": 123,
  "years": 5,
  "timePlayed": "2:30:00",
  "date": "2025-04-08",
  "content": "Contenido Básico",
  "score": 100,
  "grade": "intermedio alto"
}

Código B.4: Archivo de guardado de partida finalizada sin encriptado.

Fuente: elaboración propia, 2024.

146

APÉNDICE C. DETALLES DE EVALUACIÓN

Apéndice C.1 Detalles de pruebas de compatibilidad

Figura C.1: Interfaz del videojuego en Linux Ubuntu.

Fuente: elaboración propia, 2024.

Figura C.2: Interfaz del videojuego en Windows 11.

Fuente: elaboración propia, 2024.

147

Apéndice C.2 Preguntas evaluación HEP

Figura C.3: Preguntas evaluación HEP de jugabilidad.

Fuente: elaboración propia, 2024.

148

Figura C.4: Preguntas evaluación HEP de mecánicas.

Fuente: elaboración propia, 2024.

149

Figura C.5: Preguntas evaluación HEP de usabilidad.

Fuente: elaboración propia, 2024.

150

Figura C.6: Preguntas evaluación HEP libres.

Fuente: elaboración propia, 2024.

151

Apéndice C.3 Detalles de pruebas de aceptación

Tabla C.1: Prueba de aceptación PA-01.

Fuente: elaboración propia, 2024.

Nombre

Registrar e Iniciar sesion de perfil de juego

ID

PA-01

Requerimientos
pertinentes

Precondiciones

RF: RF_011, RF_014, RF_016

RNF: RNF_001, RNF_004

●  Primera vez en iniciar juego.
●  Tener conexión a internet.

Secuencias de
pasos de la pruebas

1.  Presionar texto “Crear cuenta”.
2.  Completar formulario (nombre, correo y contraseña).
3.  Presionar botón “Registrar”.
4.  En la interfaz del menú de juego “Iniciar sesión” ingresar

credenciales (correo y contraseña).

5.  Presionar botón “Iniciar sesión”.

Resultados
esperados

Se crea el perfil y se redirige al menú principal del juego. El perfil es
guardado en firebase.

Evaluación

B

Observación

Falta un indicador general en todas las pantallas que indique si está
logueado o no en bGames

No funciona el tab para pasar de campo en campo al momento de crear
cuenta o loguearse

152

Tabla C.2: Prueba de aceptación PA-02.

Fuente: elaboración propia, 2024.

Nombre

Autenticación de usuario y visualización de puntos bGames

ID

PA-02

Requerimientos
pertinentes

Precondiciones

Secuencias de
pasos de la pruebas

Resultados
esperados

RF: RF_011, RF_014, RF_016

RNF: RNF_001, RNF_004

●  Estar en la interfaz del menú principal “perfil”.
●  Entorno de bGames desplegado y poblado.

1.  Presionar botón “configuración” (icono tuerca).
2.  Presionar botón “inicio sesión bGames” (icono enchufe).
3.
Ingresar credenciales del usuario (nombre y contraseña).
4.  Presionar botón “iniciar sesión”.

Usuario autenticado, perfil bGames y puntos visualizados en la interfaz.

Evaluación

A

Observación

Tabla C.3: Prueba de aceptación PA-03.

Fuente: elaboración propia, 2024.

Nombre

Creación de contenido

ID

PA-03

Requerimientos
pertinentes

RF: RF_010, RF_011

RNF: RNF_001

Precondiciones

●  Estar en la interfaz del menú principal “contenido”.

Secuencias de
pasos de la pruebas

1.  Presionar botón “importar” (icono “flecha hacia arriba”).
2.  Seleccionar el script .json de las preguntas.

Resultados
esperados

Se recarga la interfaz del menú principal “Contenido” y se visualiza el
contenido creado con permiso para modificarlo al ser su autor.

Evaluación

A

Observación

153

Tabla C.4: Prueba de aceptación PA-04.

Fuente: elaboración propia, 2024.

Nombre

Descargar contenido

ID

PA-04

Requerimientos
pertinentes

RF: RF_010, RF_011

RNF: RNF_001

Precondiciones

●  Tener conexión a internet.

Secuencias de
pasos de la pruebas

1.  Abrir el juego y en el menú principal presionar el botón “Contenido”.
2.  Se abre la interfaz “Contenido”.
3.  En  el  panel  del  contenido  deseado,  presionar  botón  “descargar

contenido” (icono de flecha verde apuntando hacia abajo).

a.  Opcionalmente  se  presiona  el  botón  “filtrar”  (icono  de
cuadrados)  para  filtrar  los  contenidos,  con  filtro  para
mostrar solo repositorios en remoto.

Resultados
esperados

Se descarga el contenido correctamente (Ya no se visualiza botón para
descargar). Si se es su autor, permite modificarlo.

Evaluación

A

Observación

Asegurarse que los flujos de disponibilización en GitHub estén bien
descritos

154

Tabla C.5: Prueba de aceptación PA-05.

Fuente: elaboración propia, 2024.

Nombre

Creación de partida local

ID

PA-05

Requerimientos
pertinentes

RF: RF_004, RF_010, RF_011, RF_012

RNF: RNF_001

Precondiciones

●  Estar en la interfaz del menú principal “Jugar”.

Secuencias de
pasos de la pruebas

1.  Seleccionar una de las modalidades locales del juego (“Un

jugador”, “Pasar y jugar” o “Multi-Mando”).

2.  Si  existe  una  partida  en  curso  se  muestra  interfaz  de  carga  de

partida.

a.  Presionar  botón  “Nueva  partida”  y  luego  botón  “Si”  para

confirmar y crear una  nueva partida.

b.  Presionar  botón  “Cargar  partida” para reanudar partida en
curso  (No  permite  modificar  nada,  solo  habilita  botón
“Empezar”).

3.  Conectar  a  todos  los  jugadores  (Uno  para  modo  “Un  jugador”  y

mínimo 2 para modos “Pasar y jugar” o “Multi-Mando”).

a.  Para  modo

“Multi-Mando”  se  deben  conectar  más
periféricos  (gamepads).  El  jugador  principal  siempre  usa
teclado y ratón.

b.  Para  modo  “Pasar  y  jugar”  presionar  botón  “Agregar

jugador”.

4.  Presionar dropdown “Contenido” y elegir contenido para la partida.
5.  Presionar dropdown “Años“ y elegir duración de la partida (los años

representan los turnos).

6.  Presionar  botón  de  “cambiar  personaje”  (flecha  verde  izquierda  o
derecha) en los banner de cada jugador para cambiar el personaje.

7.  Presionar el botón “Comenzar” para iniciar la partida.

Resultados
esperados

Se cambia la escena a la del tablero, mostrando la cinemática de inicio y
comenzado el turno del primero jugador mostrando la pregunta tras
terminar la cinemática.

Evaluación

A

Observación

155

Tabla C.6: Prueba de aceptación PA-06.

Fuente: elaboración propia, 2024.

Nombre

Consumo de puntos bGames por intento extra

ID

PA-06

Requerimientos
pertinentes

Precondiciones

RF: RF_001, RF_003, RF_005, RF_007, RF_014, RF_016

RNF: RNF_001, RNF_004, RNF_005

●  Haber iniciado una partida (escena de juego tablero).
●  Ser jugador en turno y fallar en 2 intentos al responder preguntas.
●  Entorno de bGames desplegado y poblado con datos del juego.
●  Tener sesión de bGames activa y tener puntos.

Secuencias de
pasos de la pruebas

1.  Confirmar consumo presionando botón “Si”.

Resultados
esperados

Se consume 1 punto de bGames y se otorga un intento extra para
responder otra pregunta en el mismo turno.

Evaluación

B

Observación

No indica cuantos puntos se van a canjear.

156

Tabla C.7: Prueba de aceptación PA-07.

Fuente: elaboración propia, 2024.

Nombre

Mecánicas de jugador en turno

ID

PA-07

Requerimientos
pertinentes

RF: RF_001, RF_002, RF_003, RF_005, RF_006, RF_007, RF_008,
RF_009, RF_012, RF_014

RNF: RNF_001, RNF_002, RNF_005, RF_013

Precondiciones

●  Haber iniciado una partida (escena de juego tablero).
●  Ser jugador en turno.

Secuencias de
pasos de la pruebas

1.  Se  visualiza  en

la

interfaz  una  pregunta  y  3  alternativas

encapsuladas en tarjetas.

a.  Al  presionar  una  tarjeta  con  la  alternativa  incorrecta  se
pierde  un  intento  y  se  muestra  una  nueva  pregunta  (Con
uso de puntos bGames se tiene hasta 3 intentos).

2.  Presionar una tarjeta con la alternativa correcta.
3.  Aparece un dado sobre el personaje del jugador.
4.  Presionar  la  tecla  “Espacio”  o  botón  derecho  inferior  (gamepad)

para saltar y avanzar según el número obtenido del dado.

5.  Esperar que termine el movimiento del jugador.
6.  Al detener movimiento se activa la casilla ubicada y se muestran de

1-2 tarjetas

7.  Presionar una tarjeta de las tarjeta en la interfaz.

a.  Si son tarjetas de inversión, previo a presionar la tarjeta se
puede  modificar  el  monto  a  invertir  presionando  el  botón
“+” o “-” (mínimo $100).

b.  Si  son  tarjetas  de inversión y no se desea invertir o no se

tiene fondos, presionar el botón “No invertir”.

Resultados
esperados

Se modifica el HUD del jugador en base a las tarjetas seleccionadas, se
guarda la partida en progreso y se pasa al siguiente jugador.

Evaluación

B

Observación

En las tarjetas los textos están muy pegados a los bordes. Regular
márgenes. No está explicitado que saltar es la forma de parar el dado.

No es intuitivo por qué uno debe escoger una tarjeta. Según la explicación
entregada en pruebas se indicó que es aquella que sea más favorable,
pero esto debería indicarse al usuario de forma explícita.

Faltan tooltips en los distintos iconos para indicar su significado. Ej. Haber,
Inversión, Deuda.

157

Tabla C.8: Prueba de aceptación PA-06.

Fuente: elaboración propia, 2024.

Nombre

Creación de partida en línea

ID

PA-08

Requerimientos
pertinentes

Precondiciones

Secuencias de
pasos de la pruebas

RF: RF_010, RF_011

RNF: RNF_001

●  Estar en la interfaz del menú principal “Partida en línea”.
●  Tener conexión a internet.
●  Al menos 2 dispositivos Windows.

1.  Presionar botón crear partida.

a.  Compartir  código  de  sala  con  los  demás  jugadores  por

canales externos.

b.  Los  demás jugadores deben ingresar el código de sala en

el InputField y presionar el botón “Unirse partida”.
2.  Host debe presionar dropdown “Contenido” y elegir contenido para

la partida.

3.  Host  debe  presionar  dropdown  “Años“  y  elegir  duración  de  la

partida (los años representan los turnos).

4.  Cada  jugador  debe  presionar  el  botón  de  “cambiar  personaje”
(flecha  verde  izquierda  o  derecha) en los banner de cada jugador
para cambiar el personaje.

5.  Cada jugador debe presionar el botón “Listo” para iniciar la partida.
6.  La partida empieza cuando todos estén “Listos”.

Resultados
esperados

Se cambia la escena a la del tablero, mostrando la cinemática de inicio y
comenzado el turno del primero jugador mostrando la pregunta tras
terminar la cinemática.

Evaluación

C

Observación

Problemas de comunicación durante la partida. Falta algún tipo de mensaje
o procedimientos para poder detectar fallos de conexión con host.
Tolerancia a fallos o medidas de recuperación. Faltan mecanismos de
recuperación. Revisar si el problema detectado realmente es de conexión,
pues en el ejercicio pudimos ver que la conexión si estaba. identificar el
fallo.

158

Tabla C.9: Prueba de aceptación PA-09.

Fuente: elaboración propia, 2024.

Nombre

Cerrar sesión de bGames

ID

PA-09

Requerimientos
pertinentes

Precondiciones

RF: RF_011, RF_014, RF_016

RNF: RNF_001, RNF_004

●  Estar en la interfaz del menú principal “perfil”.
●  Entorno de bGames desplegado y poblado.
●  Tener sesión de bGames activa.

Secuencias de
pasos de la pruebas

1.  Presionar botón “configuración” (icono tuerca).
1.  Presionar botón “desconectar bGames” (icono salida).
2.  Presionar botón “confirmar”.

Resultados
esperados

Usuario desconectado, perfil bGames y puntos ya no se visualizan en la
interfaz.

Evaluación

A

Observación

159

APÉNDICE D. USO DE LENGUAJE GPT

Apéndice D.1. Prompt para revisión de ortografía y gramática

Para la escritura del presente documento, se utilizó el modelo de lenguaje GPT 4o

de  OpenAI,  para  asistir  en  tareas  de  revisión  de  ortografía,  gramática  y  ajuste  de  estilo.  El

prompt utilizado es el siguiente:

Prompt: “Revisa el texto para corregir únicamente errores de ortografía, gramática

y  puntuación,  respetando  el  estilo  de  escritura  del  autor.  Asegúrate  de  que  la  redacción  sea

clara  y  formal,  evitando  el lenguaje coloquial. Verifica el uso correcto de los tiempos verbales,

manteniéndolos  en  tercera  persona  singular  o  neutro  según  corresponda.  Indica  los  cambios

realizados y justifica si es necesario. Texto:”.

Ejemplo de uso:

●  Entrada  (prompt  +  texto):  “Se  espera  que  este  proyecto  sirva  como  una

herramienta  que  apoye  la  alfabetización  financiera  en  la  población  joven,

buscando  mejorar  a largo plazo la calidad de vida de las personas a través

de una mejor situación financiera obtenida a partir de la adquisición de nuevos

conocimientos,  mejores comportamientos y actitudes financieras. Además se

espera  que  el  proyecto  sea  útil  para  el  trabajo  futuro realizado con Blended

Games  del  laboratorio  Interaction,  a  fin  darlo  a  conocer  y  de  alcanzar  su

objetivo de adopción en la comunidad de desarrolladores.”

●  Salida: “Se espera que este proyecto sirva como una herramienta que apoye la

alfabetización financiera en la población joven, con el propósito de mejorar, a

largo plazo, la calidad de vida de las personas a través de una mejor situación

financiera  obtenida  mediante  la  adquisición  de  nuevos  conocimientos,  así

como  de  mejores  comportamientos  y  actitudes  financieras.  Además,  se

espera  que  el  proyecto  sea  útil  para  el  trabajo  futuro realizado con Blended

Games  del  laboratorio  Interaction,  a  fin  de  darlo  a  conocer  y  alcanzar  su

objetivo de adopción en la comunidad de desarrolladores.”

160

Apéndice D.2. Prompt para generación de imágenes para videojuego

Para  el  desarrollo  del  videojuego,  se  utilizó  el  modelo  de  lenguaje  GPT  image

generator  por  naif de OpenAI, para asistir en la creación de sprites (imágenes) utilizadas para

las tarjetas del videojuego. El prompt utilizado es el siguiente:

Prompt: “Generate an icon-style image with a pure white background of:”.

Ejemplo de uso:

●  Entrada (prompt + texto): “Salary”.

●  Salida:

Figura D.1: Sprite para tarjeta del videojuego.

Fuente: elaboración propia, 2024.

161

APÉNDICE E. ARCHIVO DE DESPLIEGUE DE BGAMES

Dado que el framework de Blended Games se encuentra a fecha de publicación del

videojuego  aún  en  desarrollo,  se  provee  un  archivo  docker-compose.yml  para  desplegar  el

entorno de manera local. Esto con el fin de dar la posibilidad de probar sus funcionalidades en

el videojuego. Para dichas pruebas se provee del siguiente usuario:

●  usuario: user

●  contraseña: asd123

El script para el despliegue es el siguiente:

services:
  db:
    image: jonathansotoa/bgames_db_wealthquest:v1.0
    restart: always
    ports:
      - "3307:3306"
    environment:
      MYSQL_ROOT_PASSWORD: rootpassword
      MYSQL_DATABASE: bgames
      MYSQL_USER: user
      MYSQL_PASSWORD: userpassword
    volumes:
      - db-data:/var/lib/mysql

  redis:
    image: redis:alpine
    restart: always
    ports:
      - "6379:6379"

Código E.1: Despliegue local del entorno bGames para WealthQuest - Parte I.

Fuente: elaboración propia, 2024.

162

get-routes:
    image: jonathansotoa/bgames_get_service:v1.0
    ports:
      - "3001:3001"
    restart: always
    environment:
      DB_HOST: db
      DB_PORT: 3306
      DB_USER: user
      DB_PASSWORD: userpassword
      DB_DATABASE: bgames
    depends_on:
      - db

  post-routes:
    image: jonathansotoa/bgames_post_service:v1.0
    ports:
      - "3002:3002"
    restart: always
    environment:
      DB_HOST: db
      DB_PORT: 3306
      DB_USER: user
      DB_PASSWORD: userpassword
      DB_DATABASE: bgames
    depends_on:
      - db

  user-routes:
    image: jonathansotoa/bgames_user_service:v1.0
    ports:
      - "3010:3010"
    restart: always
    environment:
      DB_HOST: db
      DB_PORT: 3306
      DB_USER: user
      DB_PASSWORD: userpassword
      DB_DATABASE: bgames
    depends_on:
      - db

Código E.2: Despliegue local del entorno bGames para WealthQuest - Parte II.

Fuente: elaboración propia, 2024.

163

standard-routes:
    image: jonathansotoa/bgames_standard_service:v1.0
    ports:
      - "3009:3009"
    restart: always
    environment:
      DB_HOST: db
      DB_PORT: 3306
      DB_USER: user
      DB_PASSWORD: userpassword
      DB_DATABASE: bgames
    depends_on:
      - db

  management-routes:
    image: jonathansotoa/bgames_management_service:v1.0
    ports:
      - "3007:3007"
    restart: always
    environment:
      DB_HOST: db
      DB_PORT: 3306
      DB_USER: user
      DB_PASSWORD: userpassword
      DB_DATABASE: bgames
    depends_on:
      - db

  spend-routes:
    image: jonathansotoa/bgames_spend_service:v1.0
    ports:
      - "3008:3008"
    restart: always
    environment:
      DB_HOST: db
      DB_PORT: 3306
      DB_USER: user
      DB_PASSWORD: userpassword
      DB_DATABASE: bgames
    depends_on:
      - db

Código E.3: Despliegue local del entorno bGames para WealthQuest - Parte III.

Fuente: elaboración propia, 2024.

164

  online-routes:
    image: jonathansotoa/bgames_online_service:v1.0
    ports:
      - "3005:3005"
    restart: always
    environment:
      DB_HOST: db
      DB_PORT: 3306
      DB_USER: user
      DB_PASSWORD: userpassword
      DB_DATABASE: bgames
      REDIS_HOST: redis
      REDIS_PORT: 6379
    depends_on:
      - db
      - redis

volumes:
  db-data:

Código E.4: Despliegue local del entorno bGames para WealthQuest - Parte IV.

Fuente: elaboración propia, 2024.

165

APÉNDICE F. RECURSOS UTILIZADOS

Tabla F.1: Recursos utilizados durante el desarrollo del proyecto - Parte I.

Fuente: elaboración propia, 2024.

Nombre

Descripción

AllSky Free - 10
Sky / Skybox Set

Contiene 10 cielos del conjunto AllSky para
usar en tus entornos.

Autor

Enlace

rpgwhitelock

Enlace

Buttons Set

Conjunto de botones para juego.

KartInnka

Enlace

DatePicker for
UnityUI

DatePicker es un potente control para la
selección de fechas mediante UnityUI.

Digital Legacy
Games

Enlace

FlatPoly: Board
Game Assets

Un paquete de recursos de juego de mesa 3D
de bajo polígono y aspecto elegante y plano.

Zololgo

Enlace

Footsteps -
Essentials

Paquete de sonidos con 479 sonidos de
calidad.

Nox_Sound

Enlace

Free 2D
Adventure
Beach
Background

Free Music
Tracks For
Games

Fondos de playa y gráficos de plataformas en
2D preparados para un juego de aventuras en
2D.

Super Brutal
Assets

Enlace

9 pistas de música gratis que puedes usar en
tus proyectos.

Rizwan Ashraf  Enlace

FREE Casual
Game SFX Pack

Colección de efectos de sonido originales
hechos a mano.

Dustyroom

Enlace

Free UI Click
Sound Pack

Efectos de sonido nítidos, limpios y diversos
que cubren todas las interacciones.

SwishSwoosh  Enlace

Game Input
Controller Icons
Free

Iconos del controlador de entrada de juego de
varios dispositivos de entrada, como teclado,
mouse, etc.

Amanz

Enlace

Hierarchy
Designer

Herramienta de edición diseñada para
mejorar su ventana de jerarquía y mejorar su
flujo de trabajo.

Pedro Verpha  Enlace

166

Tabla F.2: Recursos utilizados durante el desarrollo del proyecto - Parte II.

Fuente: elaboración propia, 2024.

Nombre

Descripción

Inspector
Gadgets Lite

Optimice su flujo de trabajo de desarrollo con
estas mejoras del Editor de Unity.

Autor

Enlace

Kybernetik

Enlace

LeanTween

Motor de interpolación eficiente.

Dented Pixel

Enlace

Mirror

PlayerPrefs
Editor

El servidor y el cliente son UN proyecto para
lograr la máxima productividad.

Mirror
Networking

Enlace

Permite acceder fácilmente a las preferencias
del jugador a través de una interfaz de
usuario sencilla.

BG Tools

Enlace

POLYGON City -
Low Poly 3D Art
by Synty

Paquete de recursos de bajo polígono con
personajes, edificios, accesorios, vehículos y
recursos ambientales para crear un juego de
estilo poligonal basado en una ciudad.

Synty Studios  Enlace

Simple Tooltip

Permite agregar un componente de
información sobre herramientas a cualquier
objeto.

Norb

Enlace

Simple UI &
icons

Interfaz de usuario y iconos 2D simples.

madder

Enlace

UnityStandalone
FileBrowser

Un contenedor simple para cuadros de
diálogo de archivos nativos en
Windows/Mac/Linux.

Gökhan
Gökçe

Enlace

unity-relay-mirror
-sample

El ejemplo de espejo de Unity Relay
demuestra cómo utilizar el paquete de
transporte de Unity, el servicio de Unity Relay
y la biblioteca de redes de espejo juntos.

JamesMarcil

Enlace

Versatile Game
Sound Effects

Paquete que contiene 101 efectos de sonido
musicales brillantes para usar en muchos
propósitos, como UI, elementos, acciones y
notificaciones.

FoggySoft

Enlace

Violet Themed
UI

Interfaz de usuario con temática violeta para
juegos móviles con paisajes y creación rápida
de prototipos.

Giniel
Villacote

Enlace

Xbox Buttons

Colección de elementos de solicitud de
botones GUI específicamente para
controladores XBOX.

Arks

Enlace

167

