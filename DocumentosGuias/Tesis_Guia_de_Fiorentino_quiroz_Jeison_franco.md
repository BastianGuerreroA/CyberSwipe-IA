UNIVERSIDAD DE SANTIAGO DE CHILE

FACULTAD DE INGENIERÍA

Departamento de Ingeniería Informática

Desarrollo de videojuego de género survivors en Godot con

integración de bGames

Jeison Franco Fiorentino Quiroz

Profesor Guía:

Roberto González Ibáñez

Tesis para optar al título de Ingeniero de
Ejecución en Computación e Informática

Santiago - Chile

2024

RESUMEN

El sedentarismo tecnológico ha incrementado la incidencia de problemas de salud
como la obesidad y el estrés, afectando la calidad de vida. Uno de los enfoques propuestos para
abordar esta problemática es la gamificación, que busca incentivar hábitos saludables a través
de dinámicas propias de los videojuegos. En este contexto, se trabajó con bGames, un framework
que  permite  integrar  datos  reales  del  usuario  en  la  experiencia  lúdica.  Como  parte  de  esta
estrategia, se desarrolló Nightmare Survivor, un videojuego del género survivors que aplica estos
principios  para  fomentar  hábitos  saludables  mediante  la  conexión  entre  el  videojuego  y  el
framework.

El  proyecto  siguió  una  metodología  iterativa  e  incremental,  combinando  Rapid  Application
Development (RAD) con pruebas de rendimiento y usabilidad. Se desarrollaron prototipos para
validar  mecánicas  clave  como  la  generación  de  enemigos,  la  progresión  del  personaje  y  la
interacción con bGames.

Los  principales  resultados  incluyen  la  implementación  de  un  sistema  de  progresión  de
habilidades y niveles, la integración con bGames mediante el canje de puntos y una jugabilidad
fluida  con  optimización  de  rendimiento.  Las  pruebas  demostraron  la  viabilidad  de  conectar  el
motor  de  desarrollo  Godot  Engine  con  bGames,  aunque  las  pruebas  reales  con  sensores
quedaron limitadas a entornos simulados.

En  conclusión,  este  trabajo  muestra  que  los  videojuegos  pueden  ofrecer  una  vía  viable  para
incorporar  dinámicas  de  gamificación  orientadas  al  fomento  de  hábitos  saludables,  al  menos
desde una perspectiva técnica. Sin embargo, queda abierta la posibilidad de futuras mejoras en
contenido,  balance  de  mecánicas  y  validación  empírica  del  impacto  en  la  reducción  del
sedentarismo. Esta memoria corresponde a un proyecto interno de la universidad.

Palabras  clave:  Videojuegos,  Survivors,  bGames,  Godot  Engine,  Sedentarismo  Tecnológico,
Mecánicas, Desarrollo.

i

TABLA DE CONTENIDOS

CAPÍTULO 1. Introducción............................................................................................................. 1
1.1. Antecedentes y motivación ................................................................................................. 1
1.2. Descripción del problema .................................................................................................... 2
1.3. Solución propuesta .............................................................................................................. 2
1.3.1. Características de la solución ....................................................................................... 2
1.3.2. Propósito de la solución ................................................................................................ 3
1.4. Objetivos y alcance del proyecto ......................................................................................... 3
1.4.1. Objetivo general ............................................................................................................ 3
1.4.2. Objetivos específicos .................................................................................................... 4
1.4.3. Alcances y limitaciones ................................................................................................. 4
1.5. Metodología y herramientas utilizadas ................................................................................ 4
1.5.1. Metodología .................................................................................................................. 4
1.5.2. Herramientas de desarrollo .......................................................................................... 5
1.6. Organización del documento ............................................................................................... 6
CAPÍTULO 2. Marco teórico .......................................................................................................... 7
2.1. Marco conceptual ................................................................................................................ 7
2.1.1. Blended Games ............................................................................................................ 7
2.1.2. Géneros de videojuegos ............................................................................................... 8
2.1.3. Motores de desarrollo ................................................................................................. 10
2.2. Estado del arte .................................................................................................................. 10
2.2.1. Frameworks para videojuegos y salud ....................................................................... 10
2.2.2. Evolución del género survivors ................................................................................... 11
2.2.3. Selección de motor de desarrollo ............................................................................... 12
2.2.4. Conclusión .................................................................................................................. 13
2.3. Resumen ........................................................................................................................... 13
CAPÍTULO 3. Análisis .................................................................................................................. 15
3.1. Especificación de requerimientos ...................................................................................... 15
3.2. Prototipado ........................................................................................................................ 18
3.2.1. Prototipado videojuego ............................................................................................... 18
Decisiones previas ............................................................................................................ 18
Prototipo 1: Jugabilidad de nivel ....................................................................................... 21
Prototipo 2: Jugabilidad fuera de los niveles .................................................................... 28
Prototipo 3: Integración con bGames ................................................................................ 34
Prototipo 4: Versiones ....................................................................................................... 36
Prototipo 5: Nivel infinito ................................................................................................... 39

ii

Prototipo 6: Nivel 1 ............................................................................................................ 42
3.2.2. Prototipado sensor ...................................................................................................... 47
Medición de tiempo de pantalla ........................................................................................ 47
Integración con bGames ................................................................................................... 48
Automatización .................................................................................................................. 49
Detalles técnicos ............................................................................................................... 51
3.3. Resumen ........................................................................................................................... 51
CAPÍTULO 4. Diseño e implementación ...................................................................................... 53
4.1. Arquitectura ....................................................................................................................... 53
4.1.1. Vista lógica .................................................................................................................. 53
4.1.2. Vista de desarrollo ...................................................................................................... 55
4.1.3. Vista procesos ............................................................................................................ 57
4.1.4. Vista física ................................................................................................................... 59
4.1.5. Casos de uso .............................................................................................................. 60
4.2. Aspectos de implementación ............................................................................................ 64
4.2.1. Godot Engine .............................................................................................................. 64
Nodos y tipos de nodos ..................................................................................................... 64
Inspector y scripts ............................................................................................................. 66
Autoload y función de guardado ....................................................................................... 68
4.2.2. Generación de enemigos ............................................................................................ 69
4.2.3. Subida de nivel ........................................................................................................... 71
4.2.4. Ataques ....................................................................................................................... 74
4.2.5. Introducción e historia ................................................................................................. 75
4.2.6. bGames ...................................................................................................................... 76
4.2.7. Sistema de versiones ................................................................................................. 77
4.2.8. Sensor ......................................................................................................................... 78
4.3. Resumen ........................................................................................................................... 80
CAPÍTULO 5. Evaluación ............................................................................................................. 81
5.1. Pruebas de software.......................................................................................................... 81
5.1.1. Ambientes de prueba .................................................................................................. 81
5.1.2. Pruebas de compatibilidad ......................................................................................... 81
5.1.3. Pruebas de rendimiento .............................................................................................. 82
5.2. Pruebas de aceptación ...................................................................................................... 88
5.3. Resumen ........................................................................................................................... 94
CAPÍTULO 6. Conclusiones......................................................................................................... 95
6.1. Objetivos ............................................................................................................................ 95
6.1.1. Objetivos específicos .................................................................................................. 95

iii

6.1.2. Objetivo general .......................................................................................................... 96
6.2. Implicaciones ..................................................................................................................... 96
6.3. Alcances y limitaciones ..................................................................................................... 97
6.4. Trabajo futuro .................................................................................................................... 97
6.4.1. Distribución y publicación ........................................................................................... 98
6.5. Reflexiones finales ............................................................................................................ 98
Referencias Bibliográficas .......................................................................................................... 100
A. Anexo ............................................................................................................................. 103

iv

ÍNDICE DE TABLAS

Tabla 3.1: Lista de requisitos funcionales. Fuente: Elaboración propia. ..................................... 15
Tabla 3.2: Lista de requisitos no funcionales. Fuente: Elaboración propia. ................................ 17
Tabla 3.3: Prototipo 00. Fuente: Elaboración propia. .................................................................. 18
Tabla 3.4: Ejemplos de ataques. Fuente: Elaboración propia. .................................................... 19
Tabla 3.5: Ejemplo de evolución de habilidad. Fuente: Elaboración propia. ............................... 20
Tabla 3.6: Prototipo 01. Fuente: Elaboración propia. .................................................................. 21
Tabla 3.7: Prototipo 02. Fuente: Elaboración propia. .................................................................. 28
Tabla 3.8: Prototipo 03. Fuente: Elaboración propia. .................................................................. 34
Tabla 3.9: Prototipo 08. Fuente: Elaboración propia. .................................................................. 39
Tabla 3.10: Distribución de características de enemigos. Fuente: Elaboración propia. .............. 40
Tabla 3.11: Prototipo 09. Fuente: Elaboración propia. ................................................................ 42
Tabla 3.12: Prototipo 04. Fuente: Elaboración propia. ................................................................ 47
Tabla 3.13: Prototipo 05. Fuente: Elaboración propia. ................................................................ 48
Tabla 3.14: Prototipo 10. Fuente: Elaboración propia. ................................................................ 49
Tabla 5.1: Prueba de aceptación 01. Fuente: Elaboración propia. ............................................. 89
Tabla 5.2: Prueba de aceptación 02. Fuente: Elaboración propia. ............................................. 89
Tabla 5.3: Prueba de aceptación 03. Fuente: Elaboración propia. ............................................. 89
Tabla 5.4: Prueba de aceptación 04. Fuente: Elaboración propia. ............................................. 90
Tabla 5.5: Prueba de aceptación 05. Fuente: Elaboración propia. ............................................. 90
Tabla 5.6: Prueba de aceptación 06. Fuente: Elaboración propia. ............................................. 90
Tabla 5.7: Prueba de aceptación 07. Fuente: Elaboración propia. ............................................. 91
Tabla 5.8: Prueba de aceptación 08. Fuente: Elaboración propia. ............................................. 91
Tabla 5.9: Prueba de aceptación 09. Fuente: Elaboración propia. ............................................. 91
Tabla 5.10: Prueba de aceptación 10. Fuente: Elaboración propia. ........................................... 92
Tabla 5.11: Prueba de aceptación 11. Fuente: Elaboración propia. ........................................... 92
Tabla 5.12: Prueba de aceptación 12. Fuente: Elaboración propia. ........................................... 92
Tabla 5.13: Prueba de aceptación 13. Fuente: Elaboración propia. ........................................... 93
Tabla 5.14: Prueba de aceptación 14. Fuente: Elaboración propia. ........................................... 93

v

ÍNDICE DE FIGURAS

Figura 2.1: Microservicios bGames. Fuente: Mahu (2020). ........................................................... 8
Figura 2.2: Mediana de las ganancias de géneros de juego vs la cantidad de ellos lanzados
desde 2019. Fuente: [https://howtomarketagame.com/2022/04/18/what-genres-are-popular-on-
steam-in-2022/] .............................................................................................................................. 9
Figura 3.1: Personaje jugable. Fuente: Elaboración propia......................................................... 21
Figura 3.2: Primera vista de personaje y enemigos. Fuente: Elaboración propia. ...................... 22
Figura 3.3: Primera versión de selección de tarjetas. Fuente: Elaboración propia. .................... 23
Figura 3.4: Cambio en botón de reroll. Fuente: Elaboración propia. ........................................... 24
Figura 3.5: Tarjetas de evolución. Fuente: Elaboración propia. .................................................. 25
Figura 3.6: Primera versión del HUD del nivel. Fuente: Elaboración propia. .............................. 26
Figura 3.7: Versión final del HUD del nivel. Fuente: Elaboración propia. .................................... 26
Figura 3.8: Menú de pausa. Fuente: Elaboración propia. ............................................................ 27
Figura 3.9: Ventana de confirmación de salida. Fuente: Elaboración propia. ............................. 27
Figura 3.10: Vista de resultados. Fuente: Elaboración propia. .................................................... 28
Figura 3.11: Primera versión configuración. Fuente: Elaboración propia. ................................... 30
Figura 3.12: Versión final configuración. Fuente: Elaboración propia. ........................................ 30
Figura 3.13: Pantalla de inicio. Fuente: Elaboración propia. ....................................................... 31
Figura 3.14: Vista de selección de nivel. Fuente: Elaboración propia. ........................................ 31
Figura 3.15: Introducción, nueva cuenta. Fuente: Elaboración propia. ....................................... 32
Figura 3.16: Cinemática inicial. Fuente: Elaboración propia. ...................................................... 32
Figura 3.17: Ventana de tienda de estadísticas permanentes. Fuente: Elaboración propia. ...... 33
Figura 3.18: Credenciales bGames. Fuente: Elaboración propia. ............................................... 34
Figura 3.19: Compra de rerolls bGames. Fuente: Elaboración propia. ....................................... 36
Figura 3.20: Versión del juego en pantalla de inicio. Fuente: Elaboración propia....................... 37
Figura 3.21: Tutorial selección de nivel. Fuente: Elaboración propia. ......................................... 38
Figura 3.22: Ventana de apariencia. Fuente: Elaboración propia. .............................................. 38
Figura 3.23: Mejoras no disponibles. Fuente: Elaboración propia. ............................................. 39
Figura 3.24: Tipos de enemigos. Fuente: Elaboración propia. .................................................... 40
Figura 3.25: Niveles de enemigos. Fuente: Elaboración propia. ................................................. 41
Figura 3.26: Nivel infinito con oleadas y dificultad. Fuente: Elaboración propia. ........................ 42
Figura 3.27: Tileset nivel 1. Fuente: Elaboración propia. ............................................................ 43
Figura 3.28: Parte del mapa nivel 1. Fuente: Elaboración propia. .............................................. 44
Figura 3.29: Mapa pelea contra el jefe nivel 1. Fuente: Elaboración propia. .............................. 44
Figura 3.30: Fases del jefe del nivel 1. Fuente: Elaboración propia. ........................................... 45
Figura 3.31: Spritesheet de ataque del jefe. Fuente: Elaboración propia. .................................. 46
Figura 3.32: Cinemática de pelea contra el jefe. Fuente: Elaboración propia. ............................ 46
Figura 3.33: Spritesheet animación de derrota del jefe. Fuente: Elaboración propia. ................ 47
Figura 3.34: Notificación de canjeo de puntos. Fuente: Elaboración propia. .............................. 50
Figura 3.35: Ventana de permiso uso datos. Fuente: Elaboración propia. ................................. 50
Figura 3.36: Ventana tiempo sin uso de pantalla, más botón de desarrollador. Fuente:
Elaboración propia. ...................................................................................................................... 50
Figura 4.1: Modelo 4+1. Fuente: Elaboración propia................................................................... 53
Figura 4.2: Diagrama de clases. Fuente: Elaboración propia. ..................................................... 54
Figura 4.3: Organización de carpetas del proyecto. Fuente: Elaboración propia........................ 56
Figura 4.4: Proceso de subida de nivel. Fuente: Elaboración propia. ......................................... 57
Figura 4.5: Proceso de menú de pausa. Fuente: Elaboración propia. ........................................ 58
Figura 4.6: Proceso de interacción con bGames. Fuente: Elaboración propia. .......................... 58
Figura 4.7: Diagrama de despliegue. Fuente: Elaboración propia. ............................................. 59
Figura 4.8: Casos de uso menú principal. Fuente: Elaboración propia. ...................................... 61

vi

Figura 4.9: Casos de uso nivel. Fuente: Elaboración propia. ...................................................... 62
Figura 4.10: Casos de uso aplicación. Fuente: Elaboración propia. ........................................... 63
Figura 4.11: Layout de Godot, nodos. Fuente: Elaboración propia. ............................................ 65
Figura 4.12: Layout de Godot, escena y scripts. Fuente: Elaboración propia. ............................ 66
Figura 4.13: Layout de Godot, inspector. Fuente: Elaboración propia. ....................................... 67
Figura 4.14: Autoloads. Fuente: Elaboración propia. .................................................................. 68
Figura 4.15: Spawner en inspector. Fuente: Elaboración propia................................................. 70
Figura 4.16: Proceso de generación de enemigos. Fuente: Elaboración propia. ........................ 71
Figura 4.17: Lógica de subida de nivel y selección de tarjetas. Fuente: Elaboración propia. ..... 73
Figura 4.18: Proceso de ataque. Fuente: Elaboración propia. .................................................... 75
Figura 4.19: Sistema de diálogos. Fuente: Elaboración propia. .................................................. 76
Figura 4.20: Proceso de compra de rerolls por bGames. Fuente: Elaboración propia. .............. 77
Figura 4.21: Proceso de control de versiones. Fuente: Elaboración propia. ............................... 78
Figura 4.22: Interacción con la aplicación. Fuente: Elaboración propia. ..................................... 79
Figura 4.23: Proceso de cobro de puntos. Fuente: Elaboración propia. ..................................... 80
Figura 5.1: Gráfico de rendimiento prueba 1, unidad vs tiempo. Fuente: Elaboración propia. ... 83
Figura 5.2: Gráfico de objetos prueba 2, objetos vs enemigos. Fuente: Elaboración propia. ..... 84
Figura 5.3: Gráfico de Draw Calls prueba 2, cantidad vs enemigos. Fuente: Elaboración propia.
 ..................................................................................................................................................... 84
Figura 5.4: Gráfico de uso de memoria prueba 2, valor vs enemigos. Fuente: Elaboración
propia. .......................................................................................................................................... 85
Figura 5.5: Gráfico de FPS prueba 2, valor vs enemigos. Fuente: Elaboración propia. ............. 85
Figura 5.6: Gráfico de rendimiento prueba 3 unidad vs tiempo. Fuente: Elaboración propia. .... 86
Figura 5.7: Gráfico de FPS prueba 3 valor vs enemigos. Fuente: Elaboración propia. .............. 87
Figura A.0.1: Lista de niveles. Fuente: Elaboración propia. ...................................................... 108
Figura A.0.2: Ficha de Ghoul. Fuente: Elaboración propia. ....................................................... 109
Figura A.0.3: Ficha de Swift Ghoul. Fuente: Elaboración propia. .............................................. 109
Figura A.0.4: Ficha de Bulwark Ghoul. Fuente: Elaboración propia. ......................................... 110
Figura A.0.5: Ficha de Fading Ghoul. Fuente: Elaboración propia............................................ 110
Figura A.0.6: Ficha jefe Shadow King. Fuente: Elaboración propia. ......................................... 111
Figura A.0.7: Ficha jefe Nightweaver. Fuente: Elaboración propia. .......................................... 111
Figura A.0.8: Ficha jefe Crimson Grin. Fuente: Elaboración propia. ......................................... 112
Figura A.0.9: Ficha jefe Nightmare Core. Fuente: Elaboración propia. ..................................... 112
Figura A.0.10: The Binding of Isaac. Fuente :
[https://bindingofisaac.fandom.com/es/wiki/The_Binding_of_Isaac].......................................... 114

vii

CAPÍTULO 1. INTRODUCCIÓN

Este capítulo presenta el contexto general del proyecto, exponiendo la problemática

a  resolver  y  la  justificación  del  estudio.  Se  plantean  los  objetivos  generales  y  específicos,  así

como los alcances y limitaciones. Además, se describe la metodología utilizada y las herramientas

empleadas en el desarrollo del trabajo.

1.1. ANTECEDENTES Y MOTIVACIÓN

Durante los últimos años, ha surgido la condición del ‘sedentarismo tecnológico’,

provocando un aumento considerable de las conductas sedentarias de la población debido a la

masiva implantación de dispositivos tecnológicos en los hogares (Castro-Sánchez et al., 2017, p.

242). Esta situación afecta a una amplia franja de la población, incluidos niños, adolescentes y

adultos, quienes pasan muchas horas frente a pantallas, lo que repercute negativamente en su

salud física y mental.

El sedentarismo tecnológico, como un tipo de sedentarismo, contribuye a sus mismos problemas

para  la  salud,  pues  ha  llevado  a  un  incremento  en  los  problemas  de  salud  física,  como  la

obesidad,

la  diabetes  y

las  enfermedades  cardiovasculares.  Además,  ha

impactado

negativamente  en  el  bienestar  mental  de  las  personas,  contribuyendo  a  problemas  como  la

ansiedad y la depresión, como menciona la página MedlinePlus (s.f.).  Estos problemas pueden

generar una disminución en la calidad de vida.

Frente  a  esta  realidad,  uno  de  los  enfoques  que  ha  cobrado  fuerza  en  los  últimos  años  es  la

gamificación,  que  busca  aplicar  elementos  propios  de  los  videojuegos,  como  recompensas,

niveles o progresión, en contextos no lúdicos con el objetivo de promover cambios positivos en el

comportamiento  (Deterding  et  al.,  2011).  En  este  marco,  herramientas  como  Blended  Games

permiten integrar datos reales del usuario, como la actividad física, el tiempo frente a pantallas o

indicadores fisiológicos, en alguna mecánica de un videojuego, buscando promover un balance

saludable entre los videojuegos y el mundo real (Calistro, 2019).

Esta  clase  de  integración  ha  sido  explorada  en  videojuegos  como  Village  Defender  (Ternero,

2022)  o  Blazing  Duel  (Onetto,  2023),  que  utilizaron  el  framework  bGames  para  adaptar  el

desarrollo  del  juego  según  parámetros  del  mundo  real.  A  su  vez,  existen  antecedentes  más

conocidos  en  el  ámbito  comercial,  como  los  exergames,  entre  ellos  Wii  Fit  y  Just  Dance,  que

promueven  la  actividad  física  mediante  la  interacción  corporal  con  el  videojuego  y  han

1

demostrado  efectos  positivos  tanto  en  la  salud  como  en  la  motivación  del  jugador  (Staiano  &

Calvert, 2011; Oh & Yang, 2010).

En  este  escenario,  los  videojuegos  surgen  no  solo  como  una  fuente  de  entretenimiento,  sino

también  como  un  medio  con  potencial  para  integrarse  a  enfoques  que  promuevan  hábitos

saludables. Si bien no todos los videojuegos están diseñados con un objetivo terapéutico o de

salud,  su  capacidad  de  incorporar  mecánicas  vinculadas  a  la  vida  real  mediante  frameworks

especializados  abre  la  posibilidad  de  nuevas  formas  de  interacción  que  podrían  influir

positivamente  en  el  comportamiento  de  los  usuarios.  Dar  soporte  a  este  tipo  de  propuestas

permite ampliar el alcance de los videojuegos hacia enfoques con impacto potencial en la salud

y el bienestar, aspectos que, como señalan Soto y Failde (2004), pueden contribuir a mejorar la

calidad de vida de la comunidad en general.

1.2. DESCRIPCIÓN DEL PROBLEMA

El sedentarismo tecnológico es una condición emergente derivada del uso intensivo

de dispositivos electrónicos en la vida cotidiana. Esta situación afecta tanto a niños, adolescentes

como  adultos,  y  se  asocia  con  un  aumento  en  los  casos  de  obesidad,  enfermedades

cardiovasculares, ansiedad y depresión. En este contexto, han surgido distintas estrategias para

mitigar  sus  efectos,  entre  las  cuales  destaca  la  gamificación  como  una  forma  innovadora  de

promover hábitos saludables a través de medios digitales.

Sin embargo, la implementación efectiva de esta estrategia requiere explorar nuevas formas de

vincular  datos  del  mundo  real  con  experiencias  lúdicas  digitales,  a  través  de  herramientas  y

marcos de desarrollo que lo permitan. Esta  necesidad plantea una pregunta clave que guía el

presente proyecto: ¿Cómo aportar a la visibilidad y adopción de plataformas de gamificación?

1.3. SOLUCIÓN PROPUESTA

1.3.1. Características de la solución

La  solución  consta  de  un  videojuego  diseñado  para  ser  funcional  de  forma

autónoma, pero con la capacidad de incorporar mecánicas vinculadas a datos del mundo real a

través de una plataforma externa. Esta conexión permite que ciertos comportamientos del usuario

fuera  del  entorno  de  juego  puedan  reflejarse  en  mejoras  dentro  de  la  experiencia  lúdica,

integrando  así  elementos  de  gamificación  con  potencial  para  incentivar  hábitos  saludables.

Aunque dicha integración no es obligatoria para el funcionamiento del videojuego, representa una

2

oportunidad  de  exploración  técnica  que  responde  al  interés  por  evaluar  nuevas  formas  de

interacción entre sistemas digitales y datos personales.

Un elemento clave será la creación de un Game Design Document (GDD), que detallará todos

los aspectos del diseño del juego, incluyendo mecánicas, historia y personajes. El GDD servirá

como una guía estructurada para asegurar una visión clara del producto final y facilitar la toma de

decisiones  durante  el  desarrollo,  manteniendo,  por  ejemplo,  el  proyecto  alineado  con  la

integración  de  un  framework  de  gamificación.  En  este  punto  se  pueden  levantar  algunas

propuestas iniciales para tener una idea de puntos clave a tratar dentro del GDD:

•  Temática:  Al  tratarse  de  un  juego  de  supervivencia  de  oleadas,  hay  temáticas  que  se

ajustan a este estilo, que pueden ser: zombis, espacial, sobrenatural, salvaje, etc.

•  Mecánicas  de  interacción  con  framework  de  gamificación:  Estas  mecánicas  dependen

aún  del  sensor  seleccionado,  pero  algunas  alternativas  pueden  ser:  mecánica  de

velocidad por cantidad de pasos, mecánica relacionada con ritmo cardiaco, mecánica con

interacción de voz.

•  Generación  de  recursos:  Los  assets  o  recursos  tanto  gráficos  como  sonoros  serán

creados  en  su  totalidad  por  el  responsable  del  proyecto  después  de  hacer  estudios

pertinentes de dimensiones ideales para los recursos gráficos y pruebas de sonido para

recursos sonoros.

1.3.2. Propósito de la solución

El  propósito  de  esta  solución  es  demostrar  la  compatibilidad  técnica  y  la

adaptabilidad  del  framework  Blended  Games  (bGames)  en  motores  de  desarrollo  aún  no

explorados y dentro de géneros poco representados en su catálogo actual. Aunque el impacto

directo sobre  la  promoción de  estilos de vida saludables no será  medido en este proyecto, se

busca  sentar  las  bases  técnicas  para  propuestas  futuras,  posicionando  a  bGames  como  una

alternativa viable para el diseño de experiencias lúdicas vinculadas con el comportamiento del

usuario.

1.4. OBJETIVOS Y ALCANCE DEL PROYECTO

1.4.1. Objetivo general

3

Desarrollar  un  juego  de  género  survivors  a  partir  del  engine  Godot  y  framework

bGames para aumentar el catálogo que ofrece este último.

1.4.2. Objetivos específicos

1.  Elaborar un documento de diseño de juego (GDD).

2.

Implementar el juego a partir del GDD.

3.  Aplicar el framework de bGames para la modificación de mecánicas.

4.

Implementar al menos un sensor para captura de datos que alimenten al perfil de usuario

en bGames.

1.4.3. Alcances y limitaciones

Alcances

•  El  producto  a  construir  será  un  videojuego  de  entretenimiento  de  género  “survivors”

creado en el motor de desarrollo Godot Engine.

•  Debe poder ser jugable de forma independiente de la plataforma bGames.

•  Debe ser concebido eligiendo un sensor de bGames para que actúe como puente entre

ambos.

Limitaciones

•  El desarrollo del juego estará limitado por las capacidades y restricciones del motor Godot

en su versión 4.3.

•  Al ser un desarrollo independiente, el contenido del juego se verá limitado a una versión

de demostración (demo).

1.5. METODOLOGÍA Y HERRAMIENTAS UTILIZADAS

1.5.1. Metodología

El  proyecto  se  llevará  a  cabo  en  tres  etapas  principales:  Rapid  Application

Development  (RAD),  desarrollo  iterativo  e  incremental,  y  una  evaluación  formal.  Este  enfoque

metodológico busca favorecer un desarrollo eficiente y flexible del videojuego utilizando Godot y

el framework bGames, asegurando la calidad y efectividad del producto final.

Basada  en  la  metodología  RAD  que  “se  centra  en  la  entrega  rápida  y  continua  de  prototipos,

fomentando la flexibilidad y adaptabilidad a lo largo de todo el ciclo de desarrollo” (Jaulent, 2024,

4

párr.  3),  esta  primera  etapa  se  centra  en  el  análisis  y  refinamiento  de  requisitos  mediante  la

experimentación con prototipos. Se estudiarán videojuegos del género survivors para identificar

sus  componentes  básicos  y  se  desarrollarán  prototipos  constantes  para  visualizar  las

funcionalidades clave del juego y del framework bGames.

La  segunda  etapa  se  basa  en  un  desarrollo  iterativo  e  incremental,  rescatando  los  mejores

resultados  de  los  prototipos  de  la  etapa  anterior.  Esta  etapa  busca  liberar  funcionalidades  de

manera  incremental,  consolidando  un  producto  que  cumpla  con  los  estándares  de  calidad  de

software. Se definirán y desarrollarán los elementos del juego y del conector de bGames, iterando

continuamente para  mejorar las  funcionalidades y  mecánicas  del juego  basadas en  pruebas y

retroalimentación.

La  etapa  final  se  enfoca  en  realizar  pruebas  para  evaluar  distintas  dimensiones  del  software,

incluyendo rendimiento, calidad y jugabilidad. Esta etapa asegura que el producto final cumpla

con  los  estándares  esperados  y  sea  satisfactorio  para  los  usuarios.  Se  realizarán  pruebas

unitarias,  de  integración  y  de  desempeño,  junto  con  evaluaciones  de  usabilidad  y  jugabilidad

utilizando instrumentos validados y protocolos éticos estándar.

La gestión de tareas estará registrada en un tablero Kanban que es “es una técnica de gestión

de proyectos cuyo objetivo es mejorar la eficiencia y el rendimiento. Se basa en el principio de

‘divide  y  vencerás’.  El  método  se  divide  en  varias  fases:  análisis,  planificación,  ejecución  y

seguimiento. Si se utiliza correctamente, Kanban puede ayudar a reducir los costes y mejorar la

calidad  de un proyecto. Y  esto, en el  mundo del videojuego, es  algo  importantísimo ya que  la

mayor  parte  de  estudios,  sobre  todo  los  indies1,  no  disponen  de  presupuesto  para  grandes

equipos.” (Cabezas, 2022, párr. 1, 17). Esto permitirá una visualización clara y manejo eficiente

del flujo de trabajo. Además, se mantendrá una comunicación continua con el cliente, cuyo rol

será  ocupado  por  el  profesor  guía,  a  través  de  reuniones  semanales  grupales.  En  casos

específicos, se establecerán reuniones particulares para discutir aspectos críticos del proyecto.

Este  enfoque  metodológico  está  diseñado  para  maximizar  la  eficiencia  y  adaptabilidad  del

desarrollo del videojuego, asegurando que se puedan agregar nuevas mecánicas sin interrumpir

el flujo del proyecto.

1.5.2. Herramientas de desarrollo

Para el desarrollo del proyecto se utilizará un computador personal, el cual cuenta

con las siguientes características:

1 Referente a estudios o equipos de desarrollo de menor escala e independientes

5

•  Procesador: AMD Ryzen 7 5700

•  Tarjeta gráfica: AMD Radeon RX5500XT Challenger D 4G

•  Memoria RAM: 32GB DDR4

•  Almacenamiento: 2TB HDD, 250GB SSD

•  Con respecto al software se utilizarán las siguientes herramientas:

•  Windows 11 Pro como sistema operativo.

•  Godot 4 como motor de desarrollo y herramienta para codificar.

•  Google Drive para el almacenamiento de archivos relacionados con el proyecto.

•  Aseprite y Clip Studio Paint como herramientas para el diseño de recursos gráficos.

•  LMMS como herramienta de creación de sonidos.

•  Suno.IA como página para la creación de música.

•  Android Studio para la creación de la aplicación.

•  Como  herramienta  adicional  tenemos  bGames  que  usaremos  para  conectar  perfiles  y

trabajar con sensores.

1.6. ORGANIZACIÓN DEL DOCUMENTO

El documento está dividido en seis capítulos, cada uno enfocado en un aspecto clave

del proyecto. El Capítulo 1, la presente sección, introduce el proyecto y su contexto general. El

Capítulo 2 aborda el marco teórico, presentando los conceptos y antecedentes relevantes. En el

Capítulo  3,  se  establecen  los  requerimientos  del  sistema  y  se  detallan  los  prototipos

desarrollados.  El  Capítulo  4  describe  la  arquitectura  del  proyecto  y  profundiza  en  la

implementación de sus principales mecánicas. El Capítulo 5 expone las evaluaciones realizadas,

incluyendo pruebas de rendimiento y aceptación. Finalmente, el Capítulo 6 cierra el documento

con las conclusiones, reflexionando sobre el desarrollo, las posibles mejoras y el trabajo futuro.

6

CAPÍTULO 2. MARCO TEÓRICO

Capítulo  en  el  que  se  establecen  los  fundamentos  conceptuales  y  teóricos  que

sustentan  el  proyecto.  Se  abordan  los  principales  conceptos,  tecnologías  y  antecedentes

relevantes para la investigación. Además, se presenta un análisis del estado del arte, destacando

trabajos previos y soluciones existentes en el área de estudio.

2.1. MARCO CONCEPTUAL

2.1.1. Blended Games

Implementado  inicialmente  por  Calistro  (2019)  como  parte  de  un  proyecto  en  la

Universidad  de  Santiago  de  Chile,  Blended  Games  (bGames)  es  una  iniciativa  del  laboratorio

InTeractiOn  que  busca  integrar  la  recolección  de  datos  del  usuario  y  los  videojuegos  para

fomentar hábitos saludables mediante el uso de sensores y perfiles de usuario. Este sistema tiene

el  potencial  de  vincular  datos  del  mundo  real,  como  la  actividad  física,  el  ritmo  cardiaco  o  la

interacción vocal, con las mecánicas dentro de los videojuegos. Estos datos se transforman en

atributos dentro del juego, incentivando a los jugadores a adoptar comportamientos positivos en

su vida diaria.

El  framework  está  compuesto  por  diversos  servicios  que  incluyen  recolección  de  datos  y  su

aplicación  en  los  juegos  compatibles.  Los  puntos  recolectados  a  través  de  sensores  afectan

dimensiones como lo afectivo, cognitivo, físico, lingüístico y social, permitiendo que cada usuario

tenga una experiencia personalizada. Ejemplos de su implementación incluyen videojuegos como

Village  Defender  (Ternero,  2022)  y  Blazing  Duel  (Onetto,  2023),  que  integran  los  puntos

recolectados para modificar alguna mecánica interna del videojuego.

En  términos  de  arquitectura,  bGames  está  diseñado  bajo  un  modelo  de  microservicios

distribuidos,  organizados  en  tres  capas  principales:  comunicación,  composición  y  datos.  Esta

estructura facilita la interoperabilidad con múltiples fuentes, desde redes sociales hasta sensores

móviles,  y  permite  transformar  la  información  en  atributos  jugables  mediante  un  sistema  de

estandarización y almacenamiento centralizado.  La Figura 2.1 ilustra  la  arquitectura propuesta

por Mahu (2020) para la capa en la nube del framework.

7

Figura 2.1: Microservicios bGames. Fuente: Mahu (2020).

En  el  caso  de  esta  tesis,  bGames  se  presenta  como  una  herramienta  clave  para

explorar  nuevas  formas  de  integración  entre  la  actividad  física  o  conductas  saludables  y  los

videojuegos, expandiendo su catálogo con un juego del género survivors. Esto también permitirá

demostrar  su  versatilidad  en  motores  de  desarrollo  no  explorados  previamente,  como  Godot

Engine.

2.1.2. Géneros de videojuegos

El  concepto  de  género  en  los  videojuegos  permite  clasificar  los  títulos  según  la

estructura de sus mecánicas, dinámicas y objetivos de juego. Esta categorización no es rígida,

pero cumple una función importante tanto en el desarrollo como en la comercialización, ya que

orienta a los diseñadores en la construcción de experiencias coherentes y facilita al jugador la

identificación de juegos que se ajusten a sus preferencias (Apperley, 2006; Esposito, 2005). Los

géneros influyen directamente en aspectos como la narrativa, el diseño de niveles, la interacción

del usuario y el público objetivo. Entre los más reconocidos se encuentran los juegos de rol (RPG),

acción, simulación, estrategia, roguelike y roguelite.

8

El género survivors, en particular, ha ganado popularidad en los últimos años gracias al éxito del

título Vampire Survivors y la aparición de numerosos videojuegos posteriores que replican o se

inspiran  en  sus  mecánicas  principales.  Este  subgénero  combina  elementos  de  acción  y

supervivencia,  enfrentando  al  jugador  con  oleadas  continuas  de  enemigos  mientras  mejora

progresivamente sus habilidades y atributos. Su diseño suele centrarse en la progresión rápida,

la simplicidad de controles y la alta rejugabilidad, lo que lo hace atractivo tanto para jugadores

casuales como experimentados.

Figura 2.2: Mediana de las ganancias de géneros de juego vs la cantidad de ellos lanzados desde 2019.
Fuente: [https://howtomarketagame.com/2022/04/18/what-genres-are-popular-on-steam-in-2022/]

En  la  figura  2.2  se  muestra  una  gráfica  con  la  mediana  de  ganancias  de  algunos  géneros  de

videojuegos  vs  la  cantidad  de  ellos  lanzada  por  la  plataforma  de  distribución  de  videojuegos

Steam entre 2019 y 2022. Se puede apreciar que los géneros más rentables son juegos de mazos

(Ejemplo  popular:  Slay  The  Spire)  y  de  gestión  de  recursos  4X  (Exploración,  Expansión,

Explotación  y  Exterminación).  Otros  a  considerar  del  tramo  más  rentable  pueden  ser  RPGs  o

9

juegos  de  rol  y  los  Roguelike/Roguelite,  en  donde  “roguelike  es  un  juego  en  el  que  juegas,

mueres, pulsas repetir, pero no se guarda nada entre tus intentos. Siempre volverás a jugar el

juego  desde  cero.  En  cambio,  roguelite  puede  agregar  algunas  cosas  como  actualizaciones  y

mejoras permanentes que hacen que tus intentos futuros sean más fáciles y tiene sistemas de

progresión que no existen en los roguelikes”2  (Hilliard, 2024, párr. 3).

En esta tesis, el videojuego desarrollado se posiciona dentro del género survivors, con mecánicas

inspiradas en experiencias roguelite. Esta elección busca aprovechar la popularidad del género

para maximizar el impacto del proyecto y su integración con bGames.

2.1.3.  Motores de desarrollo

Según Canle (2022), un motor de desarrollo de videojuegos, o game engine, es una

herramienta utilizada para componer escenas, animar, dotar de inteligencia artificial y sonido a

los videojuegos. Además, los motores gráficos son responsables de renderizar gráficos, detectar

colisiones, administrar el uso de  la memoria y muchas otras funciones. Por  lo tanto, un  motor

gráfico es un entorno de desarrollo integrado que reúne distintas herramientas para integrar todos

los aspectos de un videojuego en un solo lugar (párr. 4-5).

Los  motores  de  desarrollo  de  videojuegos  son  herramientas  esenciales  que  permiten  a  los

desarrolladores crear y optimizar juegos para distintas plataformas. Entre los más populares se

encuentran Unity, Unreal Engine y Godot Engine. Cada motor ofrece características únicas, como

la facilidad de uso, soporte para gráficos avanzados o acceso a recursos de código abierto.

Lo más común para un desarrollador de videojuegos es utilizar un engine por las facilidades que

brinda,  de  lo  contrario  se  debería  hacer  muchas  funcionalidades  desde  cero  lo  cual  demanda

tiempo que normalmente no se está dispuesto a gastar en algo que ya está hecho.

2.2. ESTADO DEL ARTE

2.2.1. Frameworks para videojuegos y salud

Actualmente existen muchas formas de fomentar un estilo de vida más activo en la

población. Un ejemplo de esto son todas las aplicaciones móviles que van enfocadas al área de

salud y que generalmente se enfocan en el monitoreo de la actividad del usuario. Flores (2020)

entrega ejemplos como Nike Run Club para medir desempeño en caminata o carrera, o  Sleep

2 Traducción propia

10

Cycle  para  mejorar  los  ciclos  de  sueño.  Aunque  también  existen  aparatos  físicos  como  los

Smartwatch que son relojes inteligentes que sirven para registrar cuánto nos movemos y, entre

otras cosas, nos ayudan a contar pasos y que según comenta López (2022) sobre un estudio

publicado en Lancet Digital Health, pueden ser efectivos para bajar de peso. Por otro lado, existen

plataformas que integran la vida saludable al entorno de los videojuegos, en esta categoría entran

los videojuegos activos o  exergames que “permiten el uso, la interpretación de los gestos y la

captación del movimiento en aplicación a los videojuegos. Tecnologías emergentes usadas por

consolas como PlayStation Move de Sony, Xbox Kinect de Microsoft, o Wii de Nintendo, ofrecen

entrada de datos mediante gestos sin contacto con superficies, de manera que los personajes

virtuales, en lugar de ser controlados por los desplazamientos de un botón de comando operado

con los dedos, reconocen y responden a los movimientos de los jugadores” (Ortiz de Murua, 2022,

párr. 5, 6). Existen además otras plataformas que integran los videojuegos con objetivos de salud,

como es el caso de Blended Games, descrito previamente en la sección 2.1.1.

En este contexto, los videojuegos indie, caracterizados por ser desarrollos de menor escala con

equipos reducidos y presupuestos limitados (Kukurelo, 2020, p. 6), han encontrado en bGames

una  plataforma  ideal  para  su  integración.  De  hecho,  el  catálogo  de  bGames  está  compuesto

principalmente por este tipo de juegos, entre los que destacan:

•  Desarrollo  de  videojuego  shooter  multijugador  en  Unreal  Engine  incorporando  el

framework Blended Games (Fernández, 2023).

•  Blazing  Duel:  Videojuego  de  Lucha  con  la  implementación  del  framework  de  Blended

Games (Onetto, 2023).

•  Village  Defender:  Videojuego  de  estrategia  multiplataforma  aplicando  el  framework

Blended Games (Ternero, 2022).

Además de los videojuegos indie,  bGames también ha sido utilizado en la creación de mods o

modificaciones  para  juegos  ya  establecidos,  como  en  el  caso  de  Minecraft,  donde  se  han

desarrollado modificaciones basadas en este framework (Simken, 2023) o el trabajo más reciente

del mod para el videojuego Terraria (Muñoz, 2024).

A pesar de estos avances, bGames no ha sido explorado en el contexto de juegos del género

survivors,  ni  en  su  integración  en  el  motor  de  desarrollo  Godot  Engine,  lo  que  ofrece  una

oportunidad para innovar.

2.2.2. Evolución del género survivors

El  género  survivors  ha  experimentado  un  crecimiento  significativo  desde  el

lanzamiento  de  Vampire  Survivors  en  2021,  título  que  popularizó  una  jugabilidad  basada  en

11

oleadas  de  enemigos,  progresión  constante  y  controles  simplificados  (poncle,  2021).  Este

subgénero  se  caracteriza  por  partidas  dinámicas,  sistemas  de  mejora  continua  y  una  estética

minimalista que permite un desarrollo ágil y creativo.

Algunos títulos destacados que consolidaron y diversificaron el género son:

•  Vampire  Survivors:  Considerado  el  pionero  del  subgénero  moderno,  destaca  por  su

diseño simple, progresión automática y estilo retro, logrando una gran aceptación tanto

en PC como en dispositivos móviles (poncle, 2022).

•  20  Minutes  Till  Dawn:  Introduce  mecánicas  de  disparo  activo  y  un  sistema  de

personalización basado en armas y personajes, ampliando la profundidad estratégica del

modelo base (flanne, 2022).

•  Soulstone  Survivors:  Aporta  un  enfoque  más  complejo,  con  árboles  de  habilidades,

creación de personajes y efectos visuales más elaborados, lo que apunta a una evolución

del género hacia experiencias más técnicas (Game Smithing Limited, 2023).

Recientemente, el éxito del subgénero survivors ha influido incluso en títulos de gran escala. En

2024,  Riot  Games  lanzó  “Horda”,  un  modo  temporal  para  League  of  Legends  centrado  en  el

combate  contra  oleadas  de  enemigos  en  una  estructura  PvE3  con  progresión.  Aunque  no  fue

concebido  explícitamente  como  un  título  del  subgénero  survivors,  sus  características  como  la

acumulación  de  progreso,  el  combate  repetitivo,  la  motivación  por  objetivos  y  el  estilo  en  la

jugabilidad lo alinean con esta tendencia emergente. Riot reconoció que Horda representó una

forma novedosa de juego dentro de su ecosistema y destacó su éxito en términos de participación

y recepción positiva (Riot Cadmus, 2024).

La popularidad de este tipo de mecánicas, unida a su enfoque en la mejora continua del jugador,

las convierte en una base atractiva para explorar integraciones con frameworks como bGames,

permitiendo  nuevas  formas  de  interacción  entre  el  progreso  en  el  juego  y  las  actividades  del

mundo real.

2.2.3. Selección de motor de desarrollo

Los motores de desarrollo desempeñan un rol crucial en la creación de videojuegos,

determinando  la  calidad  técnica  y  las  limitaciones  del  proyecto.  Los  motores  más  comunes

incluyen Unity, Unreal Engine y Godot Engine, cada uno con características únicas.

3 Referido a un estilo de juego en el que el jugador no juega en contra de otros jugadores, sino
que se enfrenta al entorno y los desafíos creados por el desarrollador

12

Entre estas herramientas, Unity es reconocida por su flexibilidad y enfoque multiplataforma, lo

que la hace popular tanto en proyectos móviles como en experiencias en 3D. Unreal Engine, por

su parte, se destaca por ofrecer gráficos de alta calidad y una arquitectura robusta pensada para

grandes  producciones.  Godot,  aunque  menos  masivo  en  términos  de  adopción  comercial,  ha

ganado  terreno  en  entornos  académicos  e  independientes  gracias  a  su  naturaleza  de  código

abierto,  su  ligereza  y  la  facilidad  de  personalización  de  sus  componentes.  Según  GlitchGuru

(2022), si bien Godot presenta ciertas limitaciones frente a Unity o Unreal en términos de efectos

visuales avanzados o herramientas de desarrollo para consolas, compensa con un flujo de trabajo

sencillo, tiempos de compilación reducidos y una comunidad creciente orientada a la innovación.

En el contexto de bGames, la mayoría de las integraciones previas se han realizado en motores

ampliamente  adoptados  como  Unity  y  Unreal  Engine.  Sin  embargo,  Godot  aún  no  ha  sido

explorado  dentro  de  esta  plataforma,  lo  que  representa  una  oportunidad  para  evaluar  su

compatibilidad  y  comprobar  si  su  estructura  y  filosofía  de  desarrollo  facilitan  o  dificultan  la

integración  con  bGames.  Además,  dado  que  Godot  es  un  motor  de  código  abierto  con  una

comunidad  en  crecimiento,  su  incorporación  en  este  tipo  de  frameworks  podría  abrir  nuevas

posibilidades  para  desarrolladores  independientes  que  buscan  opciones  accesibles  y  flexibles

para la creación de videojuegos con enfoques innovadores.

2.2.4. Conclusión

El análisis de frameworks, géneros y motores demuestra que existe un espacio para

innovar en la intersección entre videojuegos, salud y tecnologías inmersivas. El desarrollo de un

juego del género survivors utilizando Godot y bGames no solo aborda esta oportunidad, sino que

también amplía las posibilidades de ambos sistemas en un nuevo contexto técnico y creativo.

2.3. RESUMEN

Este capítulo ha establecido los fundamentos teóricos que sustentan el desarrollo

del  proyecto.  Se  han  definido  conceptos  clave  como  los  Blended  Games,  los  géneros  de

videojuegos y los motores de desarrollo, proporcionando el contexto necesario para comprender

la relevancia del framework bGames en la gamificación de hábitos saludables.

Asimismo, se ha analizado el estado del arte en la relación entre videojuegos y salud, explorando

distintas  iniciativas  y  tecnologías  que  han  integrado  la  actividad  física  en  la  jugabilidad.  Se

identificó que bGames ha sido implementado en diversos videojuegos indie, pero aún no se ha

13

explorado su aplicación en el género survivors, ni su compatibilidad con el motor Godot, lo que

representa  una  oportunidad  para  ampliar  su  alcance  y  evaluar  sus  posibilidades  en  un  nuevo

contexto técnico.

Finalmente, se destacó la importancia de seleccionar un motor de desarrollo adecuado para el

proyecto,  comparando  las  características  de  Unity,  Unreal  Engine  y  Godot.  Se  concluyó  que

Godot,  al  ser  un  motor  de  código  abierto  con  un  enfoque  accesible  para  desarrolladores

independientes, ofrece una plataforma propicia para experimentar con la integración de bGames,

lo que abre nuevas líneas de investigación y desarrollo en este campo.

14

CAPÍTULO 3.  ANÁLISIS

En  este  capítulo  se  detallan  los  requerimientos  del  sistema,  diferenciando  entre

requerimientos funcionales y no funcionales. También se describe el proceso de diseño inicial y

la elaboración de prototipos junto al detalle de desarrollo de cada uno de ellos.

3.1. ESPECIFICACIÓN DE REQUERIMIENTOS

En  este  punto  se  presentan  los  requisitos  funcionales  y  no  funcionales  tanto  del

videojuego desarrollado, ahora denominado como Nightmare Survivor, como de la aplicación que

actuaría  como  el  sensor  de  este  proyecto,  denominada  Screen  Time  Analyzer.  Esto  facilita  la

planificación,  el  diseño  y  la  evaluación  de  cada  componente.  Además,  estos  requisitos  sirven

como base para las decisiones técnicas y creativas del proyecto.

El formato usado para la nomenclatura del identificador del requerimiento es el siguiente: AAA-

BBB-CC, en donde:

•  AAA indica el tipo de requerimiento, usando RF para requerimientos funcionales y RNF

para requerimientos no funcionales.

•  BBB indica el tipo de sistema, siendo NS para el videojuego y STA para el sensor.

•  CC indica la numeración del requerimiento.

Tabla 3.1: Lista de requisitos funcionales. Fuente: Elaboración propia.

ID

Descripción

RF-NS-01  El juego debe contar con un sistema de control que permita al jugador mover al

personaje en las cuatro direcciones.

RF-NS-02  El juego debe contar con un sistema de generación de enemigos en oleadas,

incrementando la dificultad de forma progresiva.

RF-NS-03  El personaje controlado debe contar con parámetros internos que afecten su

comportamiento dentro del juego.

RF-NS-04  El sistema de recompensas debe permitir que los enemigos derrotados suelten

recursos que el jugador pueda recolectar, como puntos o monedas.

RF-NS-05  El juego debe contar con un sistema de experiencia que permita al jugador ganar

niveles al alcanzar umbrales específicos.

15

RF-NS-06  El juego debe contar con un sistema de recompensa al subir de nivel mostrando

una selección de tarjetas aleatorias de mejoras.

RF-NS-07  Se debe permitir cambiar las tarjetas de mejoras mostradas para darle al jugador

un poco más de control del estilo de juego.

RF-NS-08  Se debe contar con mejoras de dos tipos diferenciados: habilidades y atributos.

RF-NS-09

Las habilidades deben aumentar de nivel cuando se seleccionan repetidamente,

mejorando sus características.

RF-NS-10

Las habilidades deben evolucionar al alcanzar su nivel máximo y cuando tienen un

atributo compatible.

RF-NS-11  El nivel debe tener una interfaz de usuario que muestre datos relevantes como:

vida, experiencia actual, monedas y tiempo de la partida.

RF-NS-12

Los enemigos deben tener un indicador de vida actual.

RF-NS-13  El juego debe ser capaz de pausarse en medio de la partida.

RF-NS-14  El menú de pausa debe permitir la configuración básica y reanudar la partida.

RF-NS-15  Se debe permitir al jugador abandonar la partida y volver al menú principal si así lo

desea.

RF-NS-16  El juego debe contar con un sistema de guardado para mantener el progreso.

RF-NS-17  El juego debe tener un menú principal que permita al jugador navegar entre

distintas opciones.

RF-NS-18  El juego debe tener una vista tipo tienda que permita comprar mejoras

permanentes de atributos.

RF-NS-19  El juego debe ofrecer un tutorial cuando el jugador enfrente nuevos escenarios por

primera vez.

RF-NS-20  El juego debe incluir ajustes relacionados con el tamaño de la pantalla.

RF-NS-21  El jugador debe poder ajustar el volumen general del juego, o de manera

individual, el volumen de la música y los efectos de sonido.

RF-NS-22  El juego debe poder conectarse a un perfil de bGames.

RF-NS-23  El jugador debe poder invertir puntos de bGames en mecánicas del juego.

RF-NS-24  El juego debe registrar y mostrar estadísticas de cada partida, permitiendo al

jugador ver su progreso.

16

RF-STA-

El sensor debe ser capaz de medir el tiempo de uso de la pantalla en un rango

01

horario.

RF-STA-

El sensor debe transformar el tiempo de uso de la pantalla en puntos para el perfil

02

de bGames.

RF-STA-

El sensor debe enviar los datos de forma automática al perfil de bGames

03

correspondiente.

RF-STA-

El sensor debe pedir los permisos correspondientes para la obtención de datos del

04

dispositivo móvil.

RF-STA-

El sensor debe enviar los datos incluso sin tener la aplicación abierta.

05

RF-STA-

La aplicación debe mostrar estadísticas relevantes sobre los datos obtenidos el

06

día anterior y el actual.

Tabla 3.2: Lista de requisitos no funcionales. Fuente: Elaboración propia.

ID

Descripción

RNF-NS-
01

El juego debe contar con música de fondo y efectos de sonido que se adapten al
contexto visual y las acciones del jugador para mejorar la inmersión.

RNF-NS-
02

La interfaz debe seguir las heurísticas de Nielsen.

RNF-NS-
03

El juego debe estar vinculado a bGames, asegurando que los puntos no otorguen
grandes ventajas ni desequilibren la jugabilidad.

RNF-NS-
04

El juego debe contener una narrativa o historia coherente que proporcione contexto al
jugador sobre los eventos y el mundo en el que se encuentra.

RNF-NS-
05

El juego debe seguir una única línea temática y contextual, asegurando coherencia
entre los elementos visuales, la historia y la jugabilidad.

RNF-NS-
06

El juego debe contar con un estilo artístico consistente en los recursos gráficos.

RNF-NS-
07

El juego debe mantener un rendimiento mínimo de 60 FPS en dispositivos estándar
para garantizar una experiencia fluida.

RNF-NS-
08

Todos los textos e interfaces deben ser legibles en dispositivos con diferentes
resoluciones y tamaños de pantalla.

RNF-NS-
09

El sistema debe ofrecer una experiencia desafiante que permita a los jugadores
progresar constantemente y completar el nivel tras varios intentos.

RNF-NS-
10

El juego debe tener alta rejugabilidad, con incentivos como recompensas, desafíos o
contenido desbloqueable.

RNF-STA-
01

El sensor debe operar de manera eficiente, sin afectar significativamente el
rendimiento general del dispositivo.

17

RNF-STA-
02

El sensor debe ser compatible con una amplia gama de dispositivos, garantizando su
funcionamiento en la mayoría de los teléfonos.

RNF-STA-
03

La interfaz de la aplicación debe mantener similitudes visuales con el videojuego para
mostrar su relación.

RNF-STA-
04

La aplicación debe ser capaz de proporcionar retroalimentación clara y concisa ante
las acciones del usuario.

3.2. PROTOTIPADO

En esta sección se presentan los  distintos prototipados realizados en  el proyecto,

haciendo una distinción entre los prototipos del videojuego y los prototipos del sensor.

3.2.1. Prototipado videojuego

El  prototipado  del  videojuego  se  centró  en  la  implementación  de  las  mecánicas

principales del género survivors, incluyendo el control del personaje, las oleadas de enemigos y

el  sistema  de  habilidades  y  atributos.  También  se  explora  la  integración  con  el  framework

bGames, para vincular métricas del mundo real con la experiencia de juego.

Decisiones previas

Por comodidad y estilo de trabajo, los prototipados se centraron únicamente en las

mecánicas  del  juego,  ya  que  los  recursos  gráficos  no  pasaron  por  un  proceso  iterativo.  En  la

mayoría de los casos, se diseñaron y utilizaron directamente los recursos definitivos, sin emplear

versiones preliminares o placeholders4.

Tabla 3.3: Prototipo 00. Fuente: Elaboración propia.

ID Prototipo

Nombre

Objetivos

P00

Preparación

Diseñar una estética base y consideraciones

iniciales para el videojuego.

4 Elemento temporal que simula un recurso definitivo en etapas tempranas del desarrollo de
videojuegos.

18

Descripción

Este no es un prototipo como tal, pero engloba las

decisiones previas que se tomaron para el diseño

del juego y a su vez también aborda algunos

requisitos.

Requisitos funcionales abordados

RF-NS-10

Requisitos no funcionales abordados

RNF-NS-05, RNF-NS-06, RNF-NS-10

Tomando en cuenta que el primer prototipo que se presenta en el punto siguiente

corresponde a jugabilidad, antes de hacerlo se tomaron decisiones artísticas, de contexto y de

contenido en una fase previa que vale la pena mencionar.

Una de las decisiones iniciales clave  fue  el contexto  en el que transcurrirá el videojuego, esto

tiene  relación  directa  con  los  requisitos  no  funcionales:  RNF-NS-04  y  RNF-NS-05.  Por  lo  que

surgió  la  idea  de  trabajar  en  un  mundo  de  los  sueños,  más  específicamente  de  pesadillas,

dotando a los enemigos de una estética de miedo, mientras que a las habilidades para combatirlos

se  les  dan  características  positivas  del  sueño  o  relajantes.  En  base  a  esto  nacen  habilidades

como:

Tabla 3.4: Ejemplos de ataques. Fuente: Elaboración propia.

19

Imagen ReferencialNombreDescripciónCloud Breath (Aliento de nube)Basado en la suavidad de una nube, se trata de una habilidad que ataca con un soplido en forma de nube haciendo retroceder a los enemigosGreen Noise (Ruido verde)Basado en las frecuencias que se dice que son relajantes, el ruido verde ataca en area a los enemigos de alrededorLavander Pulse (Pulso lavanda)Basado en el aroma relajante de lavanda, pulso lavanda hace daño en área a los enemigos cercanos y además los ralentiza

La tabla anterior muestra algunos ejemplos de las habilidades creadas no solo de

forma  conceptual  teniendo  un  motivo,  sino  que  además  de  forma  práctica,  pensando  en

comportamientos diferenciados dentro del juego desde su origen, esto se hizo para un total de 12

habilidades.  Luego,  siguiendo  un  poco  lo  que  se  pide  en  el  requisito  funcional  RF-NS-10,  las

habilidades  deben  tener  evolución,  para  lo  que  también  se  hizo  el  mismo  proceso  para  las

evoluciones de las habilidades como una forma potenciada de ellas.

Tabla 3.5: Ejemplo de evolución de habilidad. Fuente: Elaboración propia.

En la tabla se muestra la evolución del aliento de nube, al igual que este ejemplo, se

diseñaron las evoluciones de las 12 habilidades.

Otro punto a tratar el diseño del personaje jugable. En este caso se optó por un enfoque simplista,

en  donde  el  jugador  en  un  inicio  no  tendrá  ninguna  característica  destacable  en  particular.  La

elección de este enfoque tiene 4 motivos:

•  Al estar en un mundo onírico, tiene sentido que el cuerpo del protagonista sea abstracto

o no corpóreo.

•  Da una mayor facilidad para animaciones.

•  Al ser genérico, no obstruye con que el jugador se pueda identificar con el personaje.

•  Permite simples y futuras personalizaciones. Según el requisito no funcional RNF-NS-10,

se puede incluir una tienda que permita personalizar al personaje comprando accesorios

(internamente  serán  imágenes  superpuestas)  con  la  moneda  del  juego,  esto  puede

permitir rejugabilidad.

20

Imagen ReferencialNombreDescripciónFresh Air (Aire fresco)Basado en la lluvia, se trata de una habilidad que hace lo mismo que su predecesora, pero además lanza gotas de agua que hacen daño a los enemigos

Figura 3.1: Personaje jugable. Fuente: Elaboración propia.

El último punto que se pensó mientras se investigaba sobre la temática y se hacían

los diseños anteriores fue la calidad en la que funcionaría o el estilo artístico base que tendría el

juego. Para esto, en base a experiencias previas de anteriores proyectos, se optó por trabajar en

diseño tipo pixelart, que se trata de imágenes de resolución más bien baja. Esto por un nivel de

detalle más bajo en los diseños, pero, para evitar un exceso en simplicidad y darle mayor carácter

y estilo, se optó por usar resoluciones un pocos más altas del estándar, usando líneas de 2 o 3

pixeles de grosor, saliendo del estándar que es de 1 pixel. Esto le da un acabado artístico que lo

deja en punto medio entre el estilo pixelart y el dibujo tradicional.

Junto  con  todo  este  proceso,  comenzó  también  la  construcción  del  Game  Design  Document

(GDD), el cual se encuentra incluido como anexo. Este se elaboró en paralelo al desarrollo y sirvió

como soporte para registrar todas las decisiones clave relacionadas con el diseño del videojuego,

incluyendo  la  ambientación,  mecánicas,  personajes,  progresión,  estilo  artístico  y  sistemas  de

juego.  Su  función  fue  actuar  como  una  guía  viva  y  actualizable  para  el  desarrollador,

modificándose constantemente ante cada nuevo planteamiento, idea o ajuste técnico. Gracias a

este enfoque iterativo, el GDD cumplió un rol fundamental en mantener la coherencia entre las

decisiones creativas y las implementaciones técnicas a lo largo de todo el proyecto.

Prototipo 1: Jugabilidad de nivel

ID Prototipo

Nombre

Objetivos

Tabla 3.6: Prototipo 01. Fuente: Elaboración propia.

P01

Nivel Base

Probar las mecánicas básicas del juego, incluyendo
el movimiento del personaje, generación de
enemigos en oleadas, sistema de recompensas y
experiencia inicial del jugador en el nivel.

21

Descripción

Requisitos funcionales abordados

El prototipo consistió en un nivel simple con espacio
suficiente para que el jugador se desplazara,
enfrentara oleadas de enemigos progresivas y
recolectara recursos al derrotarlos
RF-NS-01, RF-NS-02, RF-NS-03, RF-NS-04, RF-NS-
05, RF-NS-06, RF-NS-07, RF-NS-08, RF-NS-09, RF-
NS-10, RF-NS-11, RF-NS-12, RF-NS-13, RF-NS-14,
RF-NS-15, RF-NS-24

Requisitos no funcionales abordados  RNF-NS-01, RNF-NS-02, RNF-NS-05, RNF-NS-06,
RNF-NS-07, RNF-NS-08, RNF-NS-09, RNF-NS-10

El  primer  prototipo  del  videojuego  Nightmare  Survivor,  se  trata  del  prototipo  más

grande,  pues  tuvo  como  objetivo  principal  establecer  las  bases  de  la  jugabilidad,  integrando

sistemas fundamentales de control, interacción y progresión. Este prototipo se desarrolló a través

de un proceso iterativo en el que se implementaron y ajustaron diversos elementos esenciales

que definieron los pilares del juego.

El desarrollo comenzó con la creación del sistema de movimiento del personaje, diseñado para

ofrecer controles simples y suficientes para la experiencia que se planea. Este sistema permitió

al  jugador  desplazarse  en  las  cuatro  direcciones,  adaptándose  a  escenarios  dinámicos  y  a  la

interacción  constante  con  los  enemigos.  Para  complementar  esta  mecánica,  se  implementó  la

interacción básica con los enemigos, quienes detectaban al jugador y lo perseguían siguiendo un

comportamiento predefinido.

Figura 3.2: Primera vista de personaje y enemigos. Fuente: Elaboración propia.

En  paralelo,  se  integró  un  ataque  básico  automático,  que  serviría  para  futuras

mecánicas  de  combate  más  avanzadas.  Este  ataque  apuntaba  al  enemigo  más  cercano,

permitiendo  al  jugador  centrarse  en  el  posicionamiento  y  la  estrategia  durante  las  oleadas  de

enemigos.  El  sistema  de  generación  de  oleadas  fue  otro  componente  clave,  el  cual  permite

generar  enemigos  alrededor  del  jugador  de  forma  que  el  desarrollador  puede  establecer  la

cantidad y el momento en el que aparezcan, así dejando la posibilidad de ajustar fácilmente la

dificultad de un nivel.

22

Con  estas  mecánicas  fundamentales  establecidas,  se  añadió  un  sistema  de  experiencia  que

permitía al jugador acumular puntos al derrotar enemigos. Este sistema incluyó barras visuales

que mostraban el progreso hacia el siguiente nivel, reforzando la sensación de progreso en la

partida. La progresión del jugador se enriqueció con la implementación del sistema de tarjetas de

mejora, que ofrecía opciones de habilidades y atributos al subir de nivel. Inicialmente, las tarjetas

eran  seleccionadas  de  manera  completamente  aleatoria,  pero  se  integró  posteriormente  una

mecánica  de  cambio  o  reroll5  para  permitir  al  jugador  mayor  control  sobre  las  opciones

presentadas haciendo que se mostraran otras opciones de tarjetas en caso de quererlo. En este

último  punto,  inicialmente  se  podía  hacer  cambio  de  cada  tarjeta  individual  con  un  contador

compartido,  pero  por  simplicidad  para  el  jugador,  se  hizo  el  cambio  haciendo  que  se  pudiera

cambiar las 3 tarjetas en simultaneo pasando de lo que se puede ver en la figura 3.3 a la figura

3.4.

Figura 3.3: Primera versión de selección de tarjetas. Fuente: Elaboración propia.

5 Volver a intentar algo para tener un resultado diferente. Otra tirada.

23

Figura 3.4: Cambio en botón de reroll. Fuente: Elaboración propia.

Además, se seleccionaron y diseñaron habilidades base que definieron los estilos

de  combate  del  jugador.  Estas  habilidades  incluyeron  ataques  en  área,  proyectiles,  y  halos

defensivos, cada uno con características diferenciadas. En paralelo, se definieron atributos clave

del personaje, como velocidad de movimiento, daño y regeneración de vida, que fueron ajustados

iterativamente para equilibrar su impacto en el  gameplay6. Cabe destacar que se dejó espacio

para hasta 12 habilidades distintas y 12 atributos distintos, de los cuales solo se desarrollaron e

implementaron algunos, pero todos quedaron pensados y diseñados. Sumado a lo anterior, se

establece un sistema de colores para diferenciar a los atributos y a las habilidades en cuanto a

las mejoras. Podemos ver en la figura 3.4 que el atributo velocidad de movimiento está destacada

en azul, mientras que las habilidades están destacadas con verde.

La profundidad  del sistema de habilidades se amplió con la implementación de un sistema de

evoluciones.  Estas  evoluciones  se  desbloqueaban  al  cumplir  condiciones  específicas,  como

alcanzar un nivel máximo y tener atributos compatibles, lo que permitió mejorar significativamente

las  habilidades  seleccionadas.  En  la  siguiente  imagen  se  muestra  la  evolución  de  la  habilidad

“Aliento de  nube”, para  este caso se tuvo que elegir  5 veces esta habilidad al subir de nivel y

además  haber  elegido  por  lo  menos  una  vez  el  atributo  correspondiente  a  la  velocidad  de

movimiento, esto quitaría el “Aliento de nube” de las posibles mejoras y agregaría a su evolución

“Aire fresco” que aparece con marco amarillo en la selección de tarjetas que se puede apreciar

en la figura 3.5.

6 Jugabilidad.

24

Figura 3.5: Tarjetas de evolución. Fuente: Elaboración propia.

El  HUD  o  interfaz  de  usuario  del  juego  fue  desarrollada  para  mostrar  información

esencial  de  manera  clara  y  visualmente  coherente.  Este  incluyó  barras  de  vida  y  experiencia,

indicadores  de  habilidades  activas  y  atributos  seleccionados,  tiempo  de  juego  y  monedas

recogidas.  Durante  su  desarrollo,  se  realizaron  ajustes  para  optimizar  la  disposición  de  los

elementos, mejorar los colores y generar una estética visual consistente en todas las interfaces.

25

Figura 3.6: Primera versión del HUD del nivel. Fuente: Elaboración propia.

Figura 3.7: Versión final del HUD del nivel. Fuente: Elaboración propia.

Finalmente,  se  implementaron  un  sistema  de  monedas  y  un  menú  de  pausa.  Las

monedas en este  punto no tienen  una forma  de  obtención  definida  así que se  dejan de forma

26

aleatoria en el escenario, pero finalmente están diseñadas para ser utilizadas en sistemas fuera

del  nivel,  como  mejoras  permanentes.  Por  otro  lado,  el  menú  de  pausa  permitiría  configurar

opciones, reanudar la partida, o salir al menú principal. Además, al finalizar el nivel o abandonar

la partida, se exportaban  métricas clave, como tiempo jugado, si el nivel fue superado o no, y

monedas recogidas, para su análisis y posible uso en futuras recompensas.

Figura 3.8: Menú de pausa. Fuente: Elaboración propia.

Figura 3.9: Ventana de confirmación de salida. Fuente: Elaboración propia.

27

Figura 3.10: Vista de resultados. Fuente: Elaboración propia.

Este  prototipo  estableció  los  fundamentos  técnicos  y  conceptuales  de  Nightmare

Survivor,  permitiendo  validar  las  mecánicas  básicas  y  sentar  las  bases  para  sistemas  más

complejos en las siguientes fases del desarrollo.

Prototipo 2: Jugabilidad fuera de los niveles

ID Prototipo

Nombre

Objetivos

Tabla 3.7: Prototipo 02. Fuente: Elaboración propia.

P02

Menú Principal

Diseñar un menú funcional que permita al jugador

navegar entre las opciones principales del juego,

como iniciar partida, acceder a las configuraciones y

personalizar atributos. Además de apartados

generales para la jugabilidad fuera de los niveles.

Descripción

En este prototipo se desarrolló el sistema de

navegación en el menú principal del juego. Incluyó

botones interactivos para iniciar partidas, ajustar

configuraciones (pantalla y sonido), y acceder a una

tienda para compras permanentes. Además de un

28

sistema de introducción al juego y guardado

automático.

Requisitos funcionales abordados

RF-NS-16, RF-NS-17, RF-NS-18, RF-NS-19, RF-NS-

20, RF-NS-21, RF-NS-24

Requisitos no funcionales abordados  RNF-NS-01, RNF-NS-02, RNF-NS-04, RNF-NS-05,

RNF-NS-06, RNF-NS-08, RNF-NS-09, RNF-NS-10

El  segundo  prototipo  del  videojuego  Nightmare  Survivor  se  centró  en  el  diseño  e

implementación  del  menú  principal,  un  elemento  clave  para  la  navegación  y  configuración  del

juego. Este prototipo buscó establecer una estructura modular y funcional que permitiera añadir

características  futuras  de  forma  sencilla,  asegurando  una  experiencia  de  usuario  fluida  y

coherente con la estética del juego.

El  desarrollo  inició  con  el  diseño  del  menú  principal,  que  incluyó  botones  para  las  funciones

esenciales del juego, como iniciar partida, acceder a configuraciones, y salir al escritorio. Estos

botones se crearon con una estética base consistente, diseñada a la par que la interfaz de usuario

del prototipo anterior. Este proceso pasó por 2 iteraciones grandes; la primera le daba una estética

algo más brillante, usando colores dorados con fondos azules oscuros y violetas, pero se optó

por usar rojo y escala de grises, esto para ir enfocado en una ambientación más tétrica y por lo

tanto consistente con el concepto general del juego. Adicionalmente, se desarrolló un menú de

selección  de  niveles  modular  que  permitiera  agregar  o  eliminar  niveles  de  forma  sencilla,

facilitando futuras expansiones del contenido del juego.

29

Figura 3.11: Primera versión configuración. Fuente: Elaboración propia.

Figura 3.12: Versión final configuración. Fuente: Elaboración propia.

30

Figura 3.13: Pantalla de inicio. Fuente: Elaboración propia.

Figura 3.14: Vista de selección de nivel. Fuente: Elaboración propia.

Como  parte  de  este  prototipo,  se  implementó  un  botón  de  configuración  que  da

acceso a opciones básicas como ajuste de pantalla y volumen (Véase la figura 3.12), las cuales

también van conectadas al menú de pausa dentro del nivel en el prototipo anterior, y un botón de

salida que permitía cerrar el juego de manera directa desde el menú principal.

Otro elemento importante desarrollado en este prototipo fue un sistema de introducción al juego,

que da un contexto inicial al jugador mediante una cinemática breve apoyada en un sistema de

diálogos.  Este  sistema  fue  diseñado  para  ser  reutilizable  en  futuras  interacciones  narrativas

dentro del juego. Sumado a lo anterior se desarrolló el sistema de guardado, un elemento clave

31

que permite almacenar el progreso del jugador de forma persistente. Este sistema fue diseñado

para  registrar  datos  clave,  como  niveles  desbloqueados,  atributos  permanentes  adquiridos,  y

estadísticas generales del juego y también se utiliza para verificar si es la primera vez jugando;

si al iniciar el juego no encuentra datos guardados se mostrará la cinemática inicial, y en caso

contrario, simplemente pasará directamente al menú principal.

Figura 3.15: Introducción, nueva cuenta. Fuente: Elaboración propia.

Figura 3.16: Cinemática inicial. Fuente: Elaboración propia.

Además, se implementó una vista dedicada al aumento de habilidades permanentes,

permitiendo al jugador invertir las monedas recolectadas en las partidas para mejorar atributos

clave del personaje, y aunque no se terminaron de implementar todas las mejoras, de igual forma

32

se  les  deja  su  espacio  correspondiente.  Este  diseño  reforzó  el  carácter  roguelite  del  juego,

proporcionando un sentido de progreso constante incluso tras fallar un nivel.

Figura 3.17: Ventana de tienda de estadísticas permanentes. Fuente: Elaboración propia.

Por último, se dejó un espacio reservado en el menú para la futura personalización

del aspecto del personaje que corresponde al botón “Skin” o “Apariencia” que se puede ver en la

Figura 3.13 y que en este prototipo se dejará desactivado. Esta funcionalidad se planteó como un

medio  para  dar  mayor  uso  a  las  monedas  recolectadas,  promoviendo  la  rejugabilidad  del

videojuego.

Este prototipo no solo estableció una estructura funcional para la navegación en el juego, sino

que  también  sentó  las  bases  para  la  integración  de  nuevas  características  y  expansiones,

asegurando flexibilidad en el desarrollo futuro de Nightmare Survivor.

33

Prototipo 3: Integración con bGames

Tabla 3.8: Prototipo 03. Fuente: Elaboración propia.

ID Prototipo

Nombre

Objetivos

Descripción

Requisitos funcionales abordados

P03

Conexión con bGames

Integrar un sistema que permitirá la sincronización de
datos entre el videojuego y el perfil de bGames.

Este prototipo se centró en la implementación de
funcionalidades que conectan al videojuego con el
perfil de bGames del jugador, permitiendo invertir los
puntos en mejoras dentro del juego.
RF-NS-21, RF-NS-22

Requisitos no funcionales abordados  RNF-NS-02, RNF-NS-03, RNF-NS-06, RNF-NS-08,

RNF-NS-09, RNF-NS-10

El tercer prototipo del videojuego Nightmare Survivor es el prototipo más pequeño,

pues se enfocó en la integración con bGames, estableciendo un sistema que permitiera que el

jugador pudiera gastar los puntos de su perfil de bGames para utilizarlos en mejoras permanentes

dentro del juego.

El desarrollo comenzó con la implementación de una interfaz para que el jugador pudiera iniciar

sesión en su perfil de bGames. Esta interfaz se diseñó con un enfoque en la simplicidad y claridad,

asegurando que el proceso de conexión fuera rápido e intuitivo, además se utilizaron los mismos

recursos gráficos de interfaces creados en etapas anteriores, permitiendo un desarrollo rápido y

consistente  de  la  interfaz  de  usuario.  Una  vez  conectado  con  el  perfil,  el  sistema  permitía

sincronizar los puntos acumulados en la aplicación complementaria.

Figura 3.18: Credenciales bGames. Fuente: Elaboración propia.

34

Un punto importante sobre este prototipo es el enfoque que se pensó para conectar

al videojuego con bGames, habiendo inicialmente 2 opciones a destacar:

•  Modificar  aspectos  del  nivel  mientras  se  juega:  Esto  implicaría  que  los  puntos  de

bGames pudieran usarse en tiempo real dentro de los niveles, por ejemplo, para activar

mejoras temporales o ventajas inmediatas.

•  Modificar  aspectos  del  juego  desde  fuera  del  nivel:  En  esta  opción,  los  puntos  se

gastarían en mejoras permanentes o características accesibles desde el menú principal.

Tras analizar ambas opciones, se optó por  el segundo enfoque, ya que se adecuaba  mejor al

estilo de juego de Nightmare Survivor. Este diseño favorece una progresión separada entre los

niveles  y  el  menú  principal,  eliminando  la  necesidad  de  verificar  constantemente  el  estado  de

conexión del usuario con bGames durante la partida. De este modo, los beneficios de bGames

se  obtienen  exclusivamente  en  el  menú  principal,  reduciendo  posibles  interrupciones  en  la

experiencia de juego.

En  cuanto  al  uso  de  los  puntos  de  bGames,  se  consideraron  diferentes  alternativas  para

garantizar  que  la  integración  no  rompiera  la  mecánica  o  balance  del  juego.  Inicialmente,  se

planteó  la idea  de gastar los puntos en una tienda de mejoras permanentes similar a la figura

3.17. Sin embargo, esta opción presentaba el riesgo de otorgar ventajas desproporcionadas a los

jugadores con acceso a un gran número de puntos, lo que podría perjudicar la experiencia para

otros usuarios, y si para solventar esto se pusieran niveles máximos para una estadística al igual

que se hace en la tienda de mejoras permanentes, al gastar cierta cantidad de puntos ya no se

necesitaría  más  bGames,  quitando  el  incentivo  de  usarla.  Para  resolver  este  problema,  se

implementó un sistema que permitiera gastar los puntos de bGames en una mecánica específica:

los  rerolls.  Esta  función  que  permite  al  jugador  cambiar  las  opciones  de  tarjetas  mostradas  al

subir de nivel, brindando mayor control sobre su estilo de juego sin alterar significativamente el

balance general. Aunque los jugadores sin acceso a bGames dependen más de la suerte, esta

mecánica  no  afecta  directamente  su  capacidad  de  progresar  en  el  juego,  asegurando  una

experiencia justa y equilibrada.

35

Figura 3.19: Compra de rerolls bGames. Fuente: Elaboración propia.

Este  prototipo  consolidó  la  integración  entre  Nightmare  Survivor  y  bGames,

fortaleciendo la narrativa y la progresión del jugador en ambas plataformas. La implementación

de los rerolls como principal mecánica de gasto de puntos aseguró un equilibrio justo, al tiempo

que  proporcionó  a  los  jugadores  de  bGames  una  ventaja  estratégica  sin  comprometer  la

jugabilidad del sistema principal.

Prototipo 4: Versiones

ID Prototipo

Nombre

Objetivos

Descripción

P07

Control de versiones y tutoriales

Poder hacer un control de las versiones del
videojuego para temas de compatibilidad futura junto
con la implementación de tutoriales.

El prototipo consistió en desarrollar un script que
controlara las versiones del juego y trabajara con los
datos almacenados y a la vez generar los tutoriales y
verificar si el usuario los había completado o no.

Requisitos funcionales abordados

RF-NS-16, RF-NS-19

Requisitos no funcionales abordados  RNF-NS-04, RNF-NS-05, RNF-NS-08

36

Al haber tomado la decisión de no implementar las 12 habilidades pensadas en su

completitud y  querer comenzar a integrar los tutoriales del juego, se analizó como se  estaban

almacenando las variables importantes y los datos del jugador. Luego del análisis se plantearon

las siguientes preguntas mientras se hacían pruebas: ¿El sistema cómo sabe cuándo un jugador

ya completó un tutorial o compró una apariencia? La respuesta es sencilla: se almacena en una

variable global. Pero junto con esto nace otra inquietud: Si por ejemplo agrego un nuevo tutorial

¿Cómo  sabe  el  archivo  de  guardado  que  ahora  existe  un  nuevo  tutorial?  Si  se  reemplaza  la

variable  que  almacena  los  tutoriales  el  jugador  perderá  los  datos  cuando  se  hagan  cambios

significativos. Es entonces que nace la solución de un sistema de control de versiones del juego.

Para ello se creó una variable almacenada en los datos del jugados: versión. Aquí se almacena

la versión en al que se creó este archivo de guardado. Y además el programador tiene el deber

de escribir en cuanto se hace un cambio que afecte al archivo de guardado, una nueva versión

en las variables globales del juego. Así, al iniciar, el sistema hace lo siguiente:

•  Encuentra una discrepancia entre la versión almacenada en el archivo de guardado y la

del juego.

•  Genera una nueva estructura con los nuevos datos.

•  Migra los datos almacenados en al archivo de guardado antiguo a la nueva estructura.

•  Guarda la nueva estructura reemplazando a la antigua.

Con  esto,  un  antiguo  jugador,  o  el  mismo  desarrollador  probando  partidas  en  su  entrono  de

pruebas, puede mantener los valores de sus variables, es decir, su progreso, y tener acceso a

las nuevas.

Figura 3.20: Versión del juego en pantalla de inicio. Fuente: Elaboración propia.

Gracias  a  este  sistema,  fue  posible  implementar  los  tutoriales  para  el  juego,  en

donde  se  hizo  especial  enfoque  en  que  fueran  explicativos  con  las  mecánicas  generales  del

juego,  pero  ambientándolas  en  el  contexto  de  este,  todo  para  mayor  inmersión  del  jugador.

Además,  se  agregaron  botones  de  información  en  lugares  clave,  en  donde  se  le  recuerdan  al

jugador  las  mecánicas relacionadas.  Y si el desarrollador  quiere  agregar nuevos tutoriales, un

jugador con una versión antigua no va a tener que volver a hacer los tutoriales que ya completó.

37

Figura 3.21: Tutorial selección de nivel. Fuente: Elaboración propia.

Además, se puedo implementar una vista de apariencia para el jugador, esto influye

en  la  rejugabilidad  del  videojuego.  Por  ejemplo,  el  jugador  puede  ponerse  como  meta  el

desbloquear todas las apariencias disponibles, para ellos debe jugar varias veces y, gracias al

sistema de versiones, el desarrollador puede agregar nuevas apariencias a la tienda sin que el

jugador pierda las que ya tiene compradas.

Figura 3.22: Ventana de apariencia. Fuente: Elaboración propia.

38

El  último  uso  que  se  describirá  del  sistema  de  versiones  es  el  desbloqueo  de

atributos, pues, como no van a estar disponibles todas de inmediato, el sistema va a guardar el

progreso  de  mejora/compra  de  los  atributos  permanentes  de  un  jugador  antiguo  al  ir

desbloqueando atributos que antes no estaban disponibles. Para que fuera claro para el jugador

que estos irán saliendo en el futuro, al igual que las habilidades que aún no están disponibles, se

le muestra de forma explícita como se aprecia en:

Figura 3.23: Mejoras no disponibles. Fuente: Elaboración propia.

Prototipo 5: Nivel infinito

Tabla 3.9: Prototipo 08. Fuente: Elaboración propia.

ID Prototipo

Nombre

Objetivos

Descripción

P08

Nivel infinito

Probar la generación de enemigos infinita para un
nivel.

El prototipo consistió en el diseño de variantes de
enemigos implementados en un nivel infinito y
progresivo en dificultad.

Requisitos funcionales abordados

RF-NS-02, RF-NS-24

Requisitos no funcionales abordados  RNF-NS-01, RNF-NS-05, RNF-NS-06, RNF-NS-07,

RNF-NS-09, RNF-NS-10

39

El  prototipo  P08,  que  corresponde  al  quinto  de  los  prototipos  de  videojuego,  se

centró en desarrollar un nivel infinito. Para ello, se debían contar con una serie de requisitos para

que este nivel fuera lo más completo posible, y estos son:

•  Sistema de generación de enemigos infinito.

•  Sistema de incremento de dificultad.

•  Distintos tipos de enemigos.

Comenzando por el punto de distintos tipos de enemigos, se generaron 3 nuevas variantes del

enemigo  que  ya  se  tenía,  quedando  un  total  de  4  tipos  de  enemigos  diferenciado  por

características:

Figura 3.24: Tipos de enemigos. Fuente: Elaboración propia.

Tabla 3.10: Distribución de características de enemigos. Fuente: Elaboración propia.

Tipo de enemigo  Vida
A
B
C
D

Estándar
Baja
Alta
Muy alta

Velocidad
Estándar
Alta
Baja
Muy Baja

Daño
Estándar
Bajo
Alto
Estándar

Como se aprecia en la Tabla 3.10, los enemigos presentan diferentes características

que los distinguen entre sí. El enemigo tipo A fue diseñado como la base de equilibrio para el

resto  de  los  enemigos,  por  lo  que  sus  parámetros  sirvieron  como  referencia  para  calcular  las

variaciones de los demás tipos. En este contexto, se considera “vida” a la cantidad de daño que

un enemigo puede recibir antes de ser eliminado, “velocidad” a la rapidez con la que se desplaza

hacia el jugador, y “daño” a la cantidad de vida que le resta al jugador al entrar en contacto. El

enemigo tipo B, por ejemplo, es significativamente más rápido que el tipo A, pero tiene menor

vida, lo que lo hace más frágil. Por el contrario, el enemigo tipo C es más lento, pero posee mayor

40

resistencia, aumentando su dificultad de eliminación. Finalmente, el enemigo tipo D representa

un caso especial: es el único que, al morir, no otorga experiencia al jugador, sino que deja caer

monedas, introduciendo una dinámica distinta en el sistema de recompensas.

Además, cada tipo, menos el D, contarán con diferencia de color por niveles (todos con el mismo

patrón de color), y contarán con  niveles del 1  al  5, viendo potenciadas sus características por

algún factor.

Figura 3.25: Niveles de enemigos. Fuente: Elaboración propia.

Tomando en cuenta que tenemos 3 tipos de enemigo con 5 colores y uno especial,

en total tenemos 16  enemigos diferentes, variedad suficiente para poder implementar un nivel

infinito y que no se sienta monótono.

Esto también es útil para el segundo requisito planteado que es la progresión de dificultad. Este

requisito se cubrió a la vez que el de generación de enemigos infinitos. Para esto se  generó un

contador de dificultad el cual aumentaba cada cierto tiempo. Con esto y modificando ligeramente

el sistema de generación de enemigos se logró hacer la generación de enemigos de forma infinita

invocando  grupo  por  grupo.  Además,  se  implementó  un  sistema  dinámico  de  generación  de

enemigos basado en probabilidades y en la dificultad actual del juego. Este sistema determina

qué  enemigos  serán  generados  en  la  siguiente  oleada,  en  qué  cantidad  y  con  qué  nivel.  El

proceso comienza con la selección de un tipo de enemigo, utilizando un método de probabilidad

ponderada  según  los  valores  definidos  en  cada  escena  enemiga.  Luego,  se  calcula  cuántos

enemigos se generarán, ajustando la cantidad en función del nivel de dificultad y aplicando un

límite  máximo  para  evitar  una  sobrecarga.  Finalmente,  se  determina  el  nivel  de  los  enemigos

generados a partir de un conjunto de tablas de probabilidad que varían progresivamente con la

dificultad. A medida que esta aumenta, la frecuencia y dificultad de los enemigos también lo hace,

introduciendo variantes de niveles superiores con mayor frecuencia. Aunque se impone un límite

al número de enemigos simultáneos, tanto la cantidad como la frecuencia de aparición continúan

creciendo a lo largo del tiempo, generando una sensación de escalada constante en el desafío.

Este  enfoque  no  solo  permite  controlar  la  dificultad  de  forma  progresiva,  sino  que  también

introduce variedad y sorpresa en las oleadas, manteniendo al jugador en estado de alerta.

41

Figura 3.26: Nivel infinito con oleadas y dificultad. Fuente: Elaboración propia.

Cabe añadir que, como se tratará en el capítulo 5 de este informe, en el punto de

pruebas de rendimiento, se decidió acotar la cantidad máxima de enemigos según los resultados

obtenidos y este era el prototipo en el cual se estaba trabajando en ese momento.

Prototipo 6: Nivel 1

ID Prototipo

Nombre

Objetivos

Descripción

Tabla 3.11: Prototipo 09. Fuente: Elaboración propia.

P09

Nivel 1

Implementar el primer nivel del videojuego.

El prototipo consistió en un nivel completo, con
oleadas de enemigos y un jefe final.

Requisitos funcionales abordados

RF-NS-02, RF-NS-19, RF-NS-24

Requisitos no funcionales abordados  RNF-NS-01, RNF-NS-04, RNF-NS-05, RNF-NS-06,
RNF-NS-07

El  último  prototipo  generado  es  el  de  la  creación  del  nivel  1,  lo  que  implica  por

primera vez la planificación de un nivel de inicio a fin. Para ello, se pude dividir el nivel en 2 partes:

•  Diseño del nivel base.

42

•  Diseño de la pelea final del nivel.

Para ambos, lo primero fue generar el diseño del mapa. En este caso, se utilizó el sistema de tiles

o baldosas de Godot que permite “pintar” los niveles distribuyendo los elementos dentro de una

cuadricula, esto permite un ahorro de memoria y el resultado queda mucho más elegante para

este tipo de juegos y vista, pues entrega mayor control en la posición de elementos y un mayor

orden.  Para  ello,  se  generó  un  set  de  baldosas  o  tileset7  en  el  que  se  encuentran  todos  los

elementos del escenario y por comodidad, se utilizó el mismo para los elementos tanto del mapa

normal como del de la pelea contra el jefe (Figura 3.27).

Mientras se diseñaba, se creó una historia para darle sentido a los elementos del escenario y al

diseño de estos enemigos y del jefe, en específico de este nivel. Esta historia se encuentra oculta

e implícita en detalles del escenario.

Figura 3.27: Tileset nivel 1. Fuente: Elaboración propia.

7 Conjunto de imágenes cuadradas o tiles que se combinan en una solo imagen más grande

43

Figura 3.28: Parte del mapa nivel 1. Fuente: Elaboración propia.

Figura 3.29: Mapa pelea contra el jefe nivel 1. Fuente: Elaboración propia.

Luego del diseño de los escenarios, por comodidad del desarrollo se comenzó con

el  trabajo  en  el  jefe  antes  que  el  trabajo  en  el  resto  del  nivel.  Esto  pues  así  se  generaba

44

simplemente unos pocos segundos del nivel base y se saltaba directamente a la batalla final, lo

cual facilitaba las pruebas.

Para el jefe se utilizó un diseño que ya se tenía hecho y se fue preparando entre prototipos. Este

jefe se planificó para que contara con 3 fases en las que se volverá cada vez más fuerte, activando

cada una al bajar 1/3 de su vida máxima.

Figura 3.30: Fases del jefe del nivel 1. Fuente: Elaboración propia.

Se le implementó, además, un patrón de movimiento cuya velocidad depende de la

fase y tres ataques diferentes que irán también aumentando su daño y atributos a medida que el

jefe cambia de fase. Estos tres ataques son:

•  Ataque de mano que sale del piso en posiciones aleatorias.

•  Ataque de invocar enemigos básicos tipo A5 (Figura 3.25), es decir, equilibrados de nivel

5.

•  Ataque que dibuja un círculo gigante en el piso y ataca con “láseres”. Este ataque cuenta

a su vez con 3 variantes; 6 láseres saliendo de cierta posición, 6 láseres saliendo de otras

posiciones, y un láser gigante que da vueltas.

45

Todas las animaciones de los ataques y otras se hicieron principalmente con dibujo fotograma

por fotograma.

Figura 3.31: Spritesheet8 de ataque del jefe. Fuente: Elaboración propia.

Y  terminando  con  el  jefe,  se  implementó  una  cinemática  inicial  de  introducción  al

combate  y  una  sencilla  de  término  de  la  pelea  al  conseguir  la  victoria,  esto  sumado  a  una

animación de la derrota del jefe.

Figura 3.32: Cinemática de pelea contra el jefe. Fuente: Elaboración propia.

8 Imagen que compila una serie de imágenes que juntas hacen una animación por fotogramas.

46

Figura 3.33: Spritesheet animación de derrota del jefe. Fuente: Elaboración propia.

Y para finalizar el nivel 1, se hizo una planificación de las oleadas de enemigos para

llenarlo  de  contenido.  Al  tener,  desde  el  prototipo  anterior,  5  niveles  de  enemigos,  se  toman

grupos de estos, mezclando los tipos A, B y C de forma coherente,  quedando secciones de  2

minutos cada una por nivel de enemigo. Obteniendo de base un nivel de 10 minutos, esto sumado

al  tiempo  que  demore  la  pelea  con  el  jefe,  pues  en  ese  momento  el  temporizador  general  se

detiene, así que depende del jugador cuanto más se tarde en superar el nivel.

3.2.2. Prototipado sensor

El prototipado del sensor se orientó hacia el diseño de una  herramienta funcional

que registre y analice el tiempo activo de pantalla del usuario. Esta información no solo sirve para

fomentar hábitos saludables, sino que, como se creó prácticamente a la par que el videojuego,

guarda cierta relación con este último, al menos de manera artística.

Medición de tiempo de pantalla

Tabla 3.12: Prototipo 04. Fuente: Elaboración propia.

ID Prototipo

Nombre

Objetivos

Descripción

P04

Medición de Tiempo de Pantalla

Desarrollar un sistema que registre de manera
precisa el tiempo activo de pantalla del dispositivo
móvil del usuario.
En este prototipo se implementó un sistema de
detección del uso de la pantalla, permitiendo capturar
la cantidad de tiempo que el usuario mantuvo el
dispositivo activo dentro de un rango horario definido.

Requisitos funcionales abordados

RF-STA-01, RF-STA-02, RF-STA-04, RF-STA-06

47

Requisitos no funcionales abordados  RNF-STA-01, RNF-STA-02, RNF-STA-03, RNF-STA-

04

El prototipo P04 se centró en el desarrollo de un sistema para recopilar el tiempo de

uso  de  la  pantalla  del  dispositivo  dentro  de  un  rango  horario  predefinido.  En  lugar  de  medir

directamente el tiempo activo de la pantalla en tiempo real, la aplicación accede a los datos que

el sistema operativo Android ya registra sobre el uso del dispositivo y los procesa para integrarlos

en un único valor.

Para lograr esto, la aplicación obtiene los datos históricos del uso de pantalla y calcula el tiempo

total en que el dispositivo estuvo activo dentro del periodo configurado. Estos datos se almacenan

temporalmente y se presentan al usuario a través de la interfaz de la aplicación.

En este prototipo, la aplicación requería una acción manual del usuario para procesar y canjear

los puntos obtenidos según su tiempo de no uso del dispositivo. Es decir, una vez recopilada la

información  y  llegado  el  periodo  de  cobro,  el  usuario  debía  presionar  un  botón  dentro  de  la

aplicación para validar y más adelante poder enviar los datos a su perfil de bGames.

El  sistema  fue  diseñado  para  operar  con  bajo  consumo  de  recursos,  ya  que  no  realizaba

mediciones en tiempo real, sino que consultaba registros ya disponibles en el sistema. Además,

se  establecieron  los  permisos  necesarios  para  acceder  a  estos  datos,  asegurando  que  la

aplicación pudiera funcionar correctamente sin comprometer la privacidad del usuario.

Integración con bGames

Tabla 3.13: Prototipo 05. Fuente: Elaboración propia.

ID Prototipo

Nombre

Objetivos

Descripción

Requisitos funcionales abordados

P05

Puntos bGames

Sincronizar los datos de tiempo de pantalla
registrados con el sensor al perfil de bGames del
usuario y convertirlos en puntos utilizables en los
videojuegos.
En este prototipo se desarrolló un sistema para
transformar el tiempo registrado por el sensor a
puntos bGames y sincronizar estos datos
automáticamente con el perfil de usuario.
RF-STA-02, RF-STA-03, RF-STA-05

Requisitos no funcionales abordados  RNF-STA-01, RNF-STA-04

48

El prototipo P05 se centró en la integración del sistema de medición de tiempo de

pantalla  con  la  plataforma  bGames,  permitiendo  transformar  los  datos  capturados  en  puntos

utilizables dentro de, por ejemplo, videojuego Nightmare Survivor si se quisiera.

El  desarrollo  inició  con  la  creación  de  un  módulo  que  convertía  el  tiempo  activo  registrado  en

puntos, siguiendo  un algoritmo definido para garantizar una relación justa y proporcional  entre

tiempo  de  pantalla  y  recompensa.  Estos  puntos  eran  almacenados  temporalmente  en  la

aplicación  antes  de  ser  sincronizados  automáticamente  con  el  perfil  del  usuario  en  bGames

mediante peticiones HTTP.

En esta versión, el sistema no operaba de forma completamente automática, ya que requería que

el usuario ingresara a la aplicación y presionara un botón para transferir los puntos a su cuenta

de bGames. No obstante, se implementaron controles para evitar datos duplicados y asegurar

que la cantidad de puntos otorgada fuera precisa.

Automatización

ID Prototipo

Nombre

Objetivos

Descripción

Tabla 3.14: Prototipo 10. Fuente: Elaboración propia.

P10

Sensor programado

Generar un sistema que cobre los puntos generados
de forma automática

El prototipo consistió en sistema que de forma diaria
y programada canjea los puntos según lo recolectado
por el sensor.
RF-STA-03, RF-STA-04, RF-STA-05

Requisitos funcionales abordados

Requisitos no funcionales abordados  RNF-STA-04

El  prototipo  P10  fue  una  evolución  del  sistema  de  integración  con  bGames,

optimizando el proceso de canje de puntos mediante automatización. En versiones anteriores, el

usuario debía ingresar a la aplicación manualmente y presionar un botón para recibir sus puntos.

Sin  embargo,  a  solicitud  del  profesor,  se  implementó  un  sistema  que  realizara  esta  acción  de

forma automática.

Para  lograrlo,  se  desarrolló  un  servicio  en  segundo  plano  que  ejecuta  el  canje  de  puntos

diariamente, sin requerir intervención del usuario. Una vez que el usuario ha iniciado sesión por

primera vez y otorgado los permisos necesarios, el sistema realiza el cálculo y envía los puntos

al perfil de bGames sin necesidad de abrir la aplicación.

49

Se añadieron notificaciones para informar al usuario cuando el canje se ha realizado, indicando

la cantidad de puntos obtenidos en el día. Asimismo, se incorporó una ventana de permisos para

garantizar que la aplicación tuviera acceso a los datos necesarios.

Figura 3.34: Notificación de canjeo de puntos. Fuente: Elaboración propia.

Figura 3.35: Ventana de permiso uso datos. Fuente: Elaboración propia.

Figura 3.36: Ventana tiempo sin uso de pantalla, más botón de desarrollador. Fuente: Elaboración propia.

Para facilitar las pruebas durante el desarrollo, se implementó un botón de reinicio

que  permitía  forzar  manualmente  el  canje  de  puntos,  evitando  la  espera  del  ciclo  diario.  Este

botón solo estuvo disponible en la versión de prueba y no en la versión final de la aplicación.

50

Detalles técnicos

Con todas las funcionalidades implementadas y en funcionamiento, resulta pertinente detallar la

arquitectura  técnica  que  sustenta  este  sistema,  así  como  el  flujo  de  datos  que  permite  la

comunicación entre la aplicación y la plataforma bGames. A continuación, se describe cómo está

estructurado el sistema y qué protocolo se utiliza para sincronizar los puntos obtenidos.

El  sistema  adopta  una  arquitectura  cliente-servidor,  donde  la  aplicación  Android  actúa  como

cliente y se comunica con la API REST de bGames, que opera como servidor. La medición del

tiempo sin uso de pantalla se obtiene a partir de los  registros históricos proporcionados por el

sistema Android, y no mediante monitoreo en tiempo real, lo que reduce el consumo de recursos.

El canje de puntos se realiza de forma automática mediante peticiones HTTP gestionadas con

Retrofit,  una  biblioteca  que  simplifica  la  comunicación  con  servicios  web  desde  Android.  Esta

operación ocurre una vez al día y es programada usando  AlarmManager, un componente del

sistema operativo que permite agendar tareas para que se ejecuten en un momento específico,

incluso  si

la  aplicación  está  cerrada.  Al  activarse

la  alarma,  entra  en  acción  un

BroadcastReceiver,  un  componente  que  escucha  eventos  del  sistema,  encargado  aquí  de

ejecutar el proceso de canjeo en segundo plano.

Los datos enviados al servidor consisten en un payload JSON (estructura de datos enviada en la

solicitud),  que  incluye  el  identificador  del  jugador,  los  atributos  que  deben  actualizarse  y  la

cantidad  de  puntos  a  sumar.  Para  mantener  la  identificación  del  usuario  y  evitar  canjes

duplicados, la aplicación utiliza SharedPreferences, un mecanismo de almacenamiento local que

guarda información sencilla como el ID del jugador y la última fecha de canje.

Finalmente, para mantener informado al usuario, se implementó un sistema de notificaciones que

confirma cuándo el canje se ha realizado exitosamente.

3.3. RESUMEN

En  este  capítulo  se  abordó  el  proceso  de  análisis  y  diseño  inicial  del  videojuego

Nightmare Survivor, detallando los requerimientos del sistema y los prototipos desarrollados. Se

establecieron los requisitos funcionales y no funcionales, proporcionando una base sólida para la

implementación del juego.

El proceso de prototipado permitió validar mecánicas clave, como el movimiento del personaje,

la  generación  de  enemigos,  la  progresión  mediante  experiencia  y  el  sistema  de  mejora  de

habilidades. Se realizaron pruebas iterativas para equilibrar el juego y optimizar la experiencia del

51

usuario. Además, se exploró la integración con bGames, definiendo cómo los puntos obtenidos

en la plataforma afectarían la jugabilidad.

También  se  desarrolló  el  sistema  de  recopilación  de  datos  del  sensor,  determinando  su

funcionamiento y estableciendo su conexión con el perfil de usuario en bGames.

52

CAPÍTULO 4.  DISEÑO E IMPLEMENTACIÓN

Esta  sección  aborda  la  arquitectura  de  la  solución,  explicando  la  estructura  y

componentes  principales  del  sistema.  Se  describen  las  decisiones  de  diseño  adoptadas  y  los

procesos de desarrollo. Además, se detalla la implementación de las funcionalidades clave.

4.1. ARQUITECTURA

La  arquitectura  del  sistema  para  el  proyecto  Nightmare  Survivor  y  la  aplicación

Screen Time Analyzer junto con su integración con bGames se diseñó siguiendo el modelo 4+1

vistas recomendado por Philippe Kruchten (1995), que permite representar distintos aspectos del

sistema desde diferentes perspectivas. Este enfoque facilita la comprensión de la solución técnica

y permite visualizar tanto la estructura estática como el comportamiento dinámico del sistema.

Figura 4.1: Modelo 4+1. Fuente: Elaboración propia.

4.1.1. Vista lógica

53

En la vista lógica se representan las funcionalidades de la solución y la relacionan

de  los  elementos  implementados.  En  este  caso  se  hace  uso  de  un  diagrama  de  clases  para

representar esta vista:

Figura 4.2: Diagrama de clases. Fuente: Elaboración propia.

Este diagrama centrado en el videojuego muestra el comportamiento de un solo nivel eligiendo

elementos importantes y algunos de ejemplo. Se pueden apreciar los siguientes elementos:

•  World: Clase que representa al mundo o mapa. Posee un identificador, tiempo actual de

juego y la cantidad de puntos recogidos.

•  Player: Clase que representa al jugador y contiene todos los atributos necesarios para

describir a un jugador, a destacar: nivel actual de cada atributo y habilidad, así como las

listas de los atributos/habilidades disponibles y las listas de los seleccionados de cada

tipo.

•  Cloud_Breath: Se trata de un ejemplo de ataque/habilidad, ya que, si bien cada ataque

se llamará de la misma forma, cada uno tendrá atributos distintos asociados al tipo de

ataque.

•  Enemy_Spawner: Se trata de la clase que coordina la aparición de enemigos, recibe una

lista de distintos tipos de enemigos y su tiempo de aparición.

•  Enemy: Este es un ejemplo de  enemigo, aunque la  mayoría  de  los enemigos  básicos

comparte  características.  Notamos  que  posee  características  como  el  nivel  de

experiencia a soltar al ser derrotado, su vida actual y vida máxima (esto para mostrar una

54

barra  de  vida)  y  velocidad  de  movimiento  máxima  y  actual  (esto  porque  existe

ralentización, por lo que puede haber variaciones en su velocidad de movimiento).

4.1.2. Vista de desarrollo

Para  la  vista  de  desarrollo,  se  hace  uso  de  un  diagrama  que  represente  la

distribución de las distintas carpetas, ya que esta vista está relacionada con la visión del proyecto

desde el punto de vista del programador.

En el juego, todos los recursos generados fueron almacenados dentro una carpeta base llamada

assets, ya sean recursos gráficos, de sonido, scripts con código del juego, etc.

La organización de carpetas se ve referenciada en el diagrama de la figura 4.3. Dentro de assets

se encuentran las carpetas:

•  Audio:  Carpeta  en  la  que  se  almacena  lo  referente  a  archivos  de  audio,  estos  se

subdividen en Music para música general y SFX para efectos especiales.

•  Enemy: En esta carpeta se encuentra todo lo referente a enemigos. Además, de forma

específica, cada enemigo tiene su propia carpeta.

•  Font: Carpeta para las distintas fuentes de texto que se probaron.

•  Map: Carpeta que contiene los mapas o niveles.

•  NPCs:  Carpeta  para  almacenar  a  los  personajes  no  jugables,  cada  uno  en  su  propia

carpeta.

•  OtherEntities:  Carpeta  para  almacenar  otro  tipo  de  entidades,  por  ejemplo,  la

experiencia, las tarjetas, las monedas, etc.

•  Player:  Dentro  va  todo  lo  referente  al  jugador,  además  aquí  se  encuentran  los

ataques/habilidades.

•  Theme: Se encuentran archivos correspondientes a configuración del tema.

•  UI: Todo lo referente a distintas vistas y menús. Aquí encontramos las subcarpetas de:

Menú principal, Ventana de pausa, Introducción, la interfaz de bGames, etc.

•  Utility: Aquí se encuentran en su mayoría scripts de utilidad para el juego como puede

ser alguna función  general como las funciones generales  de  bGames,  el guardado de

partida, etc.

55

Figura 4.3: Organización de carpetas del proyecto. Fuente: Elaboración propia.

56

4.1.3. Vista procesos

Para  esta  vista  se  presentarán  distintos  diagramas  de  actividad  para  mostrar  el

comportamiento del videojuego en tiempo de ejecución para distintas funciones clave.

La  primera  actividad  corresponde  a  la  subida  de  nivel  en  la  que  se  muestra  la  interacción  del

jugador con las llamadas al sistema. En este caso se inicia con que el jugador recoge experiencia

y en cada recogida el sistema se pregunta si subió o no de nivel. En el caso de que haya subido

de nivel la actividad continúa. En sistema genera las tarjetas aleatorias y las muestra al jugador.

El jugador puede decidir si cambia o no las tarjetas volviendo al paso anterior y haciendo que el

sistema  genere  nuevas  tarjetas  o  elegir  una  de  las  tarjetas.  Al  elegir  una  tarjeta  el  sistema  la

analiza para ver si sube de nivel una habilidad o un atributo y termina esta actividad.

Figura 4.4: Proceso de subida de nivel. Fuente: Elaboración propia.

La  siguiente  activiadad  a  mostrar  corresponde  al  funcionamiento  del  menú  de

pausa. Al igual que la actividad anterior, se trata de una interración en la que participan tanto el

jugador  como  el  sistema.  En  donde,  a  grandes  rasgos,  el  jugador  dispone  de  una  serie  de

opciones y el sistema reacciona en base a la acción que haga el jugador, ya sea que quiera salir

del nivel, ver el menu de configuraciones o reanudar la parida.

57

Figura 4.5: Proceso de menú de pausa. Fuente: Elaboración propia.

La última actividad a presentar se trata de la interacción del usuario con el menú de

bGames en el videojuego. Aquí participa tanto el jugador como el sistema del videojuego además

del servicio de bGames. Inicialmente ocurre toda la interacción inicial en el que el jugador ingresa

con  sus  credenciales  y  el  sistema  las  envía  al  servicio  de  bGames  para  verificarlas.  Luego  el

usuario  puede  comprar  o  no  puntos  en  función  de  si  quiere  y  si  le  alcanzan  sus  puntos  para

posteriormente terminar con la actividad. Cada acción que dependa del servicio de bGames se

consulta y se manejan  los errores que entregue  bGames,  provocando  esto  que se  muestre el

error y se finalice el flujo, mas no necesariamente la actividad.

Figura 4.6: Proceso de interacción con bGames. Fuente: Elaboración propia.

58

4.1.4. Vista física

Para mostrar la vista física se hace uso de un diagrama de despliegue que muestra

la relación entre el módulo cloud y el videojuego y también el módulo cloud con la aplicación. El

diagrama se muestra a continuación:

Figura 4.7: Diagrama de despliegue. Fuente: Elaboración propia.

En este caso, son los componentes dedicados a  bGames que tiene cada sistema,

tanto  videojuego  como  aplicación,  los  que  se  comunican  con  los  distintos  servicios  que  tiene

actualmente bGames para hacer las llamadas que necesiten, tanto para obtener algún dato, como

modificarlo en caso de requerirlo.

59

4.1.5. Casos de uso

La vista de casos de uso o escenarios sirve para representar de forma general las

distintas interacciones que puede tener uno o más actores con el sistema. Para esto se mostrarán

2 diagramas  de casos de  uso, el  primero  orientado  a la  interacción con  el menú principal y el

segundo orientado a la interacción con un nivel de juego.

En el diagrama de casos de uso (Figura 4.8) se pueden apreciar las posibles interacciones de 2

actores con el menú principal; el primer actor corresponde a un jugador que no posee cuenta de

bGames, mientras que el segundo actor corresponde a un jugador que sí posee una cuenta de

bGames. Ambos jugadores tienen posibles interacciones o casos de uso en común, los cuales

son:

•  Seleccionar nivel

•  Comprar mejoras permanentes

•  Cambiar la configuración del juego

•  Salir del juego

Sin embargo, el jugador con cuenta de bGames puede interactuar con la sección correspondiente

a bGames del menú principal, lo que le agrega como casos de uso:

•

Iniciar sesión bGames

•  Canjear puntos bGames

El caso de uso “Canjear Puntos bGames” incluye al caso de uso “Iniciar Sesión bGames”, ya que,

para realizar el canje de puntos, es necesario que el usuario haya iniciado sesión previamente en

el sistema.

60

Figura 4.8: Casos de uso menú principal. Fuente: Elaboración propia.

Por otro lado, en el diagrama (Figura 4.9) que representa la interacción con un nivel

de juego, cuenta con un solo actor ya que la interacción del jugador con el nivel es independiente

al tipo de jugador (tenga cuenta de bGames o no). Aquí el jugador puede:

•  Derrotar enemigos

•  Recolectar recursos

•  Subir de nivel

•  Seleccionar mejora

•  Cambiar las tarjetas / hacer reroll

•  Completar el nivel

•  Pausar el juego

61

En el diagrama se puede apreciar que para  seleccionar una mejora o cambiar las

tarjetas es necesario subir de nivel, y notamos que para que el jugador suba de nivel es necesario

que  el  jugador  recolecte  recursos,  lo  cual  es  posible  solo  si  el  jugador  derrota  enemigos.  Las

acciones de pausar el juego y completar el nivel quedan más independientes, ya que, aunque se

pude pensar que para completar el nivel es necesario derrotar enemigos o subir de nivel, esto no

está estrictamente relacionado, pues depende más de la dificultad del juego que obliga al jugador

a  hacer  las  acciones  de  derrotar  enemigos  y  subir  de  nivel.  Esto  es  debido  a  que  el  nivel  se

completa por tiempo sin que sea necesario derrotar a todos los enemigos cuando esto suceda.

Sumado a lo anterior, si por ejemplo un nivel tuviera un solo enemigo, el jugador simplemente

podría alejarse de él hasta que se acabara el tiempo para completar el nivel con éxito.

Figura 4.9: Casos de uso nivel. Fuente: Elaboración propia.

62

Pasando a los casos de uso de la aplicación, estos solo pueden ser realizados por

un usuario con cuenta  de  bGames, y para  él no hay mucho realmente que  pueda hacer en la

aplicación, pues no es una aplicación pensada en la interacción constante con el usuario, por lo

que solamente podrá:

•

Iniciar sesión con sus credenciales bGames

•  Dar los distintos permisos para que la aplicación envíe notificaciones y además puede

acceder a los datos del móvil. Por lo que esto es solo la primera vez que se ingresa a la

aplicación.

•  Ver el tiempo de uso de la pantalla, lo cual es una acción con poca interacción real con

el usuario.

Por lo cual, como se aprecia en el diagrama (Figura 4.10) la única interacción directa que tiene el

usuario con la aplicación es iniciar sesión y ver sus estadísticas. Esto debido a que finalmente el

cobro de puntos se hará de forma programada y automática.

Figura 4.10: Casos de uso aplicación. Fuente: Elaboración propia.

63

4.2. ASPECTOS DE IMPLEMENTACIÓN

En  esta  sección  se  describen  los  aspectos  técnicos  de  la  implementación  del

videojuego  y  la  aplicación  complementaria.  Se  detallan  los  sistemas  desarrollados  en  Godot

Engine, como la generación de enemigos, la progresión del jugador y la integración con bGames.

Además, se explica el funcionamiento de la aplicación móvil, incluyendo la recopilación de datos

de uso de pantalla y su conexión con el perfil de usuario en bGames.

4.2.1. Godot Engine

Esta  sección  será  utilizada  para  describir  el  funcionamiento  general  de  Godot

Engine, esto ayudará para el entendimiento de los siguientes aspectos de implementación.

Godot Engine se basa en un sistema de nodos y escenas que permite una estructura jerárquica

y  modular  para  el  desarrollo  eficiente  de  videojuegos.  A  continuación,  se  detalla  cómo  se

integraron los elementos clave en el desarrollo del proyecto.

Nodos y tipos de nodos

Godot organiza los componentes del juego mediante un sistema de nodos, que son

las unidades básicas de su estructura. Cada nodo tiene funciones específicas que pueden ser

extendidas o combinadas para crear comportamientos complejos.

Tipos de Nodos Comunes Utilizados:

•  Node2D:  Nodo  base  para  representar  elementos  bidimensionales,  utilizado  para  la

creación de personajes, enemigos y objetos del juego. Contiene configuración espacial

básica como posición, escala, rotación, etc.

•  Area2D:  Maneja  la  detección  de  colisiones  y  señales,  utilizado  para  proyectiles  y

detección de interacción del jugador.

•  Collider2D: Nodo que controla las colisiones entre nodos. Relacionado estrechamente

con Area2D.

•  CharacterBody2D: Implementado para manejar el movimiento del jugador y enemigos,

permitiendo  detectar  colisiones  sin  atravesar  objetos  sólidos.  Relacionado  con

Collider2D.

•  Control: Usado para diseñar interfaces de usuario como menús y HUD.

64

•  Sprite2D:  Nodo  que  controla  las  imágenes,  puede  manejar  imágenes  tipo  spritesheet

para hacer animaciones 2D.

Figura 4.11: Layout9 de Godot, nodos. Fuente: Elaboración propia.

En  la  imagen  anterior  nos  encontramos  en  la  escena  “Player”.  Lo  incluido  en  el

número 1, es un ejemplo de construcción de un personaje, en donde se tiene como base un nodo

CharacterBody2D llamado Player. Uno de sus nodos hijos, por ejemplo, es un Nodo2D llamado

Sprites, este nodo es simplemente utilizado para ordenamiento y organización, ya que no tiene

uso  alguno,  además  este  también  tiene  sus  propios  nodos  hijos  que  son  de  tipo  Sprite2D

tratándose del Aura y la Base del personaje. Otro ejemplo interesante es HurtBox que es de tipo

Area2D, el cual también es una escena como tal, lo que muestra que una escena también es un

nodo que puede ser hijo de otro nodo, dándole más profundidad a este sistema de anidamiento.

La Sección “número 2” de la imagen muestra algunos de los posibles nodos a agregar a la hora

de  añadir  un  nodo  hijo,  los  cuales  se  encentran  agrupados,  pero  se  logra  apreciar  lo  más

generales como Node2D, Control, Node3D, pero este último no es utilizado en el marco de este

proyecto tratándose de un videojuego en 2D, y por el lado de los de tipo Control, estos son usados

para elementos de UI.

9 Disposición de paneles o ventanas en el editor.

65

Inspector y scripts

Otros apartados a de Godot a describir son el inspector del motor y cómo funcionan

los scripts. En Godot, se puede crear un archivo de script para definir las funciones y atributos de

una escena, por lo que se genera un enlace script-escena. Desde este script se puede acceder

o invocar a los distintos nodos hijos (y si se desea, a los nodos padres también) para obtener o

cambiar sus atributos o incluso acceder a sus scripts si los tienen. En la imagen (Figura 4.12) se

puede notar como se hace referencia dentro del script de ExpOrb que corresponde a una Area2D

a uno de sus nodos hijos AnimationPlayer, llamándolo “animation” y pudiendo después acceder

a sus propiedades si se desea.

Figura 4.12: Layout de Godot, escena y scripts. Fuente: Elaboración propia.

Luego, el otro apartado a tratar es el inspector que posee Godot Engine. El inspector

se trata de una vista creada para el desarrollador que permite ver todos los atributos que tiene de

base  un  nodo  o  elemento.  Por  ejemplo,  un  nodo  de  tipo  colisión  permite  cambiar  la  forma  y

orientación de la colisión desde el editor sin necesidad de usar un script para determinarlo, en

cambio, un nodo de tipo imagen va a permitir seleccionar una imagen a mostrar y su posición,

orientación, si es o no una imagen múltiple (animación de spritesheet), su transparencia, etc. En

la imagen (Figura 4.13) podemos ver un ejemplo de vista de inspector en el que se encuentran

diferenciadas 2 secciones, la sección 2 muestra los parámetros que trae para editar por defecto

el  tipo  de  nodo  trabajado,  en  cambio,  la  sección  1  muestra  otra  característica  que  tiene  el

inspector, pues desde el script del nodo se pueden exportar características/atributos para que se

66

puedan  editar  desde  el  inspector,  en  este  caso  desde  el  script  se  crearon  atributos  editables

correspondientes a nivel de tipo numérico y de colores de tipo selección de color lo cual se ve

reflejado en el editor. Esto da facilidades al desarrollador para pruebas sin tener que cambiar el

código o para, como se verá en otra sección, invocar a otro nodo desde el nodo, de forma que

solo habrá que arrastrarlo.

Figura 4.13: Layout de Godot, inspector. Fuente: Elaboración propia.

67

Autoload y función de guardado

Otra característica a destacar de Godot Engine se trata de la función de Autoload.

Esta se encuentra en un menú de configuración de Godot, en una sección del mismo nombre. La

función  principal  de  Autoload  es  tener  precargados  ciertos  archivos  de  forma  automática  para

poder acceder a ellos en cualquier momento y desde cualquier archivo/nodo/script.

Haciendo uso de la función de  autoload se pudo implementar un sistema de guardado para el

videojuego.  Para  ello  se  generó  un  archivo  para  almacenar  las  variables  globales  llamado

GLOBAL.gd el cual es un script que tiene los siguientes elementos principales:

•  Estructura para almacenar datos: Se trata de una estructura de datos que puede ser por

ejemplo  una  serie  de  listas  anidadas  para  poder  almacenar  las  variables  de  forma

ordenada,  estas  pueden  ser:  nivel  de  atributos,  avance  de  niveles,  monedas

recolectadas, etc.

•  Archivo de guardado: Archivo en que se cargan y guardan los datos de la estructura,

•  Función  de  guardado  de  datos:  Función  que  ayuda  a  almacenar  los  datos  que  se

encuentren en la estructura antes mencionada en el archivo específico, si el archivo no

se encuentra, lo crea.

•  Función de cargado de datos: Función que recupera los datos almacenados en el archivo

de guardado (de existir) y los coloca en la estructura de datos según corresponde.

Figura 4.14: Autoloads. Fuente: Elaboración propia.

Gracias a esta forma de implementar el guardado y cargado de datos se pudo hacer

que se pudieran guardar  los datos por  ejemplo saliendo  de cada nivel, y además se tuvo que

ajustar  el  código  para  que,  en  vez  de  usar  parámetros  locales  por  ejemplo  para  atributos,  se

tuvieran  que  usar  los  parámetros  que  se  encuentran  en  el  archivo  global  que  son  los  que  se

almacenan al guardar y cargar partida, unificando la forma de tratar a los parámetros importantes.

68

4.2.2. Generación de enemigos

Comenzando con los sistemas desarrollados, uno de estos se encarga de generar

enemigos  en  oleadas.  Para  ello  se  generó  un  archivo  enemy_spawner  que  genera  enemigos

alrededor del jugador de en posiciones aleatorias desde fuera de su rango de visión para darle

factor  sorpresa  y  se  desarrolló  de  forma  lo  suficientemente  modular  para  que  fuera  capaz  de

gestionar cualquier oleada de enemigos utilizando el mismo archivo. Para ello, el archivo creado

contiene  un  arreglo  que  pide  elementos  de  tipo  spawn_info,  spawn_info  corresponde  a  otro

archivo creado para este sistema, este se encarga de darle la información de la oleada actual a

enemy_spawner, mientras que enemy_spawner se encarga de gestionar y coordinar las distintas

oleadas. Por su parte, spawn_info cuenta con los siguientes parámetros:

•  Time Start: Indica en qué segundo va a generarse el primer enemigo de la oleada.

•  Time End: Indica en qué momento se van a dejar de generar enemigos en la oleada.

•  Enemy: Aquí se ingresa el nodo que contiene al enemigo a generar.

•  Enemy Number: Cantidad de enemigos que saldrán al mismo tiempo

•  Enemy Spawn Delay: Tiempo a esperar entre enemigos. Por ejemplo, si Enemy Number

es 3 y Enemy Spawner Delay es 10, esto va a hacer que cada 10 segundos se generen

3 enemigos a la vez, y seguirá generándolos cada 10 segundos hasta Time End.

Si hay por ejemplo 2 spawn_info en el arreglo, para ajustar las oleadas debemos hacer que el

Time End del primero coincida con el Time Start del segundo, a menos que queramos que haya

algún momento en el que no se generen oleadas de enemigos o que una oleada de enemigos se

genere al mismo tiempo que hay otra. Esto último es útil si queremos que en una misma oleada

se generen 2 tipos distintos de enemigos a la vez.

El enemy_spawn permite modificar las oleadas de enemigos desde el editor, permitiendo cambiar

el  tamaño  del  arreglo  de  enemigos  y  arrastrar  o  crear  un  nuevo  spawn_info  para  luego  poder

modificar cada atributo de la oleada. Esto le entrega al desarrollador un control total de las oleadas

de enemigos.

69

Figura 4.15: Spawner en inspector. Fuente: Elaboración propia.

70

Figura 4.16: Proceso de generación de enemigos. Fuente: Elaboración propia.

Lo que hace el sistema es, gracias a una variable interna tiempo, cuyo valor aumenta

cada  segundo,  revisa  oleada  por  oleada  cuál  se  encuentra  dentro  de  ese  segundo,  es  decir,

verificamos si el valor de tiempo actual se encuentra entre el Time Start y el Time End de cada

grupo de enemigos, si se encuentra, revisa si tiene  Delay, en el caso de tenerlo, no genera al

enemigo, pero internamente aumenta una variable auxiliar que comienza  en  0 dentro de cada

enemigo,  hasta  que  ese  valor  sea  igual  al  Delay,  una  vez  alcanzado  genera  la  cantidad  de

enemigos indicados en Enemy Number, y reinicia la auxiliar a 0 para volver a realizar la espera.

La generación de enemigos de forma infinita, por otro lado, no recibe la misma lista de enemigos,

sino que es más bien una lista de probabilidad de enemigo y una lista de probabilidad de nivel,

trabajando con estas listas puede encadenar oleadas de enemigo infinitas.

4.2.3. Subida de nivel

Cada vez que se sube un nivel en una etapa del juego el jugador debe elegir entre

3 tarjetas aleatorias. La gestión de estás tarjetas está hecha en base a un sistema de listas que

se puede ver en el diagrama de la figura 4.17. Internamente, el script encargado de la gestión del

jugador cuenta, entre otras cosas, con 4 listas; dos de ellas se encargan de almacenar los IDs10

de los atributos y habilidades posibles disponibles, y las otras dos listas se encargan de almacenar

10 ID o IDs corresponde a un identificador

71

los IDs de las habilidades y atributos seleccionados. Además, se cuenta con una lista auxiliar que

junta los IDs de habilidades y atributos disponibles.

En  el  momento  en  el  que  el  jugador  sube  de  nivel,  los  valores  almacenados  en  las  listas  de

posibles candidatos para elegir al subir de nivel se juntan en la lista auxiliar y se extraen 3 IDs

aleatorios, estos corresponden a las tarjetas que se muestran en pantalla. Si el jugador hace un

reroll, se vuelven a seleccionar 3 IDs aleatorios. Cabe aclarar que los IDS que se muestran entre

rerolls pueden repetirse, pero las 3 tarjetas siempre serán distintas entre sí.

Luego  el  jugador  debe  elegir  una  tarjeta,  cuyo  ID  se  almacenará  en  la  lista  que  corresponda:

habilidad del jugador o atributo del jugador. Independiente del tipo de tarjeta, el sistema evalúa 2

cosas:

•  El nivel de la habilidad/atributo seleccionado: En caso de llegar al nivel 5, lo elimina de la

lista de candidatos correspondiente, pues este se trata del nivel máximo.

•  Las condiciones de evolución de la habilidad. Todas las habilidades tienen las mismas

condiciones de evolución, pero con distintos atributos, estas son:

o  Habilidad nivel 5: Lo que quiere decir que la habilidad que se desea evolucionar

debe haber sido elegida 5 veces.

o  Atributo  correspondiente  seleccionado:  Además  de  la  habilidad  en  nivel  5  se

debe haber seleccionado al atributo necesario para evolucionar por lo menos una

vez (es decir, que esté mínimo nivel 1). Por ejemplo, para evolucionar la habilidad

Aliento de Nube se requiere de haber seleccionado velocidad de movimiento en

algún momento.

Si las condiciones se cumplen, el sistema agregará la evolución a la lista de posibles habilidades,

por lo que su aparición también depende de la suerte, y si la habilidad evolucionada le aparece y

la  selecciona,  se  eliminará  a  la  habilidad  anterior  de  la  lista  de  habilidades  del  jugador  y  se

reemplazará  con  su  versión  evolucionada  evitando  duplicados  de  habilidad.  En  cambio,  si  las

condiciones  no  se  cumplen  el  sistema  no  hace  nada  y  sigue  evaluando  si  se  cumplen  las

condiciones,  ya  sea  subiendo  de  nivel  a  la  habilidad  que  corresponde  o  eligiendo  el  atributo

necesario.

Cabe añadir que el límite máximo de atributos distintos es 5 al igual que el de habilidades distintas.

Por lo que llegado al límite de habilidades estas dejan de aparecer y solo aparecen atributos y lo

mismo  viceversa.  Cuando  se  llega  al  límite  de  ambas  y  se  sigue  subiendo  de  nivel,  solo

aparecerán opciones para recuperar vida al instante (ya que se asume que se encuentra en una

fase avanzada del nivel, por lo que es una ayuda) o monedas (como alternativa, por si el jugador

tiene gran parte de su vida y las monedas le ayudan a la progresión fuera del nivel). Este sistema

puede hacer que el jugador no seleccione o no le aparezca el atributo o la habilidad que quiere

72

subir, y llenando sus espacios no podrá evolucionarlos, lo que agrega un paso extra de dificultad

combinado con suerte, aunque esto no es un impedimento para terminar un nivel.

Figura 4.17: Lógica de subida de nivel y selección de tarjetas. Fuente: Elaboración propia.

73

4.2.4. Ataques

Los ataques o habilidades del juego son la forma que tiene el jugador de derrotar a

los enemigos, ganar experiencia, subir de nivel, derrotar a enemigos más numerosos y fuertes y

completar una etapa. En Nightmare Survivors, los ataques se realizan de forma automática, la

mayoría  apuntando  al  enemigo  más  cercano,  por  lo  que  el  jugador  solo  debe  preocuparse  de

estar a la mejor distancia posible según su set de ataques (ponerse más cerca de los enemigos

si elige ataques de corto alcance o al revés en caso contrario).

El funcionamiento de los ataques se muestra en la figura 4.18. Básicamente, estos funcionan con

temporizadores que son nodos de tiempo de Godot. Al finalizar el contero del temporizador, es

hace 2 cosas: Realiza la función de ataque y se reinicia. Esto provoca que los ataques sean un

bucle infinito, lo que tiene sentido, pues el jugador no dejará de atacar hasta terminar una etapa,

ya sea por completarla o por perder.

El tiempo de los temporizadores de ataque se asigna en una combinación de 2 factores:

•  Tiempo de ataque base: No todos los ataques tienen de base o de tiempo de recarga

el  mismo  tiempo,  los  más  poderosos  o  que  hacen  más  daño  tienen  más  tiempo  de

recarga que uno que no.

•  Tiempo dependiente de la velocidad de ataque del jugador: Algunos atributos del

jugador  afectan  a  todas  las  habilidades,  como  el  daño,  la  velocidad  de  ataque,  la

cantidad de proyectiles, etc. Es la velocidad de ataque un factor que se agrega al tiempo

de ataque base, o, mejor dicho, se le resta, aumentando la frecuencia de los ataques.

Este factor es variable y depende del tipo de habilidad, pues no a todas les afecta de la

misma manera.

Son tanto los atributos como el nivel del ataque mismo los que afectan las características de cada

habilidad.  Pero  cabe  aclarar  que  no  todos  los  atributos  afectan  a  todas  las  habilidades.  Por

ejemplo,  a  un  ataque  en  área  alrededor  del  jugador  no  le  afectará  el  atributo  “cantidad  de

proyectiles”, ya que no sería aplicable.

74

Figura 4.18: Proceso de ataque. Fuente: Elaboración propia.

4.2.5. Introducción e historia

Ya implementado el sistema de guardado, ahora el sistema es capaz de detectar si

el juego es abierto por primera vez, validando si existe un archivo de guardado o no.  Se puede

usar esta información para que el sistema sepa si debe mostrar o no una introducción al juego.

Para  crear  la  introducción  se  optó  por  un  enfoque  sencillo,  que  consiste  que  un  personaje

introduzca parte de la historia al jugador. Para ello son necesarios 2 elementos:

•  Narrador: Para el narrador se debe crear un personaje no jugable o NPC que inicialmente

será el puente entre el jugador y el juego.

•  Sistema de diálogos: Se necesita alguna forma de hacer que el NPC se comunique con

el jugador en forma de texto.

Ya que el crear un NPC no es más que idear un personaje que tenga sentido en el contexto del

juego,  el foco estará  en el sistema  de  diálogos.  Para hacer el sistema de diálogos se creó un

algoritmo que toma en orden cada uno de los elementos de una lista (cada elemento es un string),

de los cuales va leyendo carácter por carácter. Como se puede ver en la figura 4.19, inicialmente

el sistema separa el string en 4 según las primeras comas que encuentre (El uso de estas comas

es completamente obligatorio), estas comas actúan como separadores de texto, de forma que la

primera sección del string corresponde a si el globo de texto tiene la punta que indica al hablante,

la segunda sección contiene al icono a mostrar, la tercera corresponde al nombre y la cuarta al

dialogo.

75

El  sistema  de  dialogo  está  hecho  de  forma  que  se  muestra  carácter  por  carácter,  dándole  un

efecto de “máquina de escribir”, esto sumado a que con cada carácter también se emite un sonido,

dándole más vida a este recurso. Otra forma de darle vida fue reservando un carácter especial

“%” el cual en el caso de ser leído por el sistema este no le escribirá, en cambio lo que hará será

esperar unos segundos para luego seguir leyendo la cadena. Esto último es especialmente útil

en casos en donde existe un punto seguido, de forma que le da más naturalidad y ritmo al sistema

de texto.

Figura 4.19: Sistema de diálogos. Fuente: Elaboración propia.

Con todo lo anterior descrito, el sistema de diálogos quedó con un enfoque modular,

lo que permite su reutilización en cualquier aspecto que lo requiera, por ejemplo, los tutoriales de

juego o la necesidad de contar partes de la historia importantes para enriquecer la experiencia y

la inmersión en el mundo creado.

4.2.6. bGames

Para implementar bGames en el videojuego, la idea era hacer un componente que

fuera lo más independiente posible y que fuera encargado directo de la conexión con  bGames.

76

Debido a ello, se hizo uso de un autoload al igual que como se hizo para las variables globales

en el sistema de guardado del punto 4.2.1.3, pero este, aunque con la posibilidad de poder ser

ingresado desde cualquier parte del proyecto, su acceso en la  práctica estará limitado al nodo

encargado de la vista de bGames. Por lo tanto, se cuenta con un nodo autoload encargado de

todas las llamadas http con los endpoint11 correspondientes y actuales. Esto para que, si llega al

momento de  actualizar los  endpoints o las URL base, se  pueda acceder al  nodo encargado y

hacer las modificaciones solo ahí.

Fue  necesario  crear  nodos  hijos  para  este  autoload  (lo  cual  es  posible  porque  el  autoload  se

carga como un nodo, al fin y al cabo) pues en Godot los llamados HTTP se hacen con un nodo

dedicado a esto llamado HTTPRequest. La figura 4.20 muestra su funcionamiento.

Figura 4.20: Proceso de compra de rerolls por bGames. Fuente: Elaboración propia.

4.2.7. Sistema de versiones

El sistema de control de versiones funciona gracias a modificar el script de guardado

y  cargado  que  se  tenían  anteriormente,  así  que  están  directamente  relacionados.  El  proceso

sigue la  lógica  que ya  tenía el sistema de guardado  y cargado de datos,  pero  se le agrega el

componente de control de versión.

La versión del juego es un valor que desde aquí comenzaría a estar guardado en los datos que

se almacenan del jugador, así como en el propio juego. Al cargar la partida, el juego compara

11 Punto de acceso en una API donde se realizan las solicitudes HTTP.

77

estos valores y si son distintos hace una migración de los datos de la versión antigua a la nueva,

lo que conserva cualquier variable importante que sirva para demostrar el avance del jugador. En

el  proceso  de  migración,  el  sistema  toma  el  valor  almacenado,  rescata  su  identificador,  y  lo

deposita en su lugar correspondiente en la nueva versión de datos de guardado.

Es  de  responsabilidad  del  desarrollador  que,  al  hacer  un  cambio  que  afecte  a  los  datos

almacenados, el valor de la versión del juego sea cambiado. Al no cambiarlo, el juego no detectará

la discrepancia entre los valores de la versión y el juego podría intentar a acceder a un valor que

el jugador no posee.

Figura 4.21: Proceso de control de versiones. Fuente: Elaboración propia.

4.2.8. Sensor

Como  ya  se  ha  mencionado,  el  sensor  fue  implementado  para  que  finalmente

trabajara  de  forma  automática  y  programada.  Para  ello,  el  jugador  al  iniciar  la  aplicación  por

primera vez debe dar algunos permisos, como de notificación, uso de datos, etc. Luego de su

ingreso con las credenciales de bGames, el sistema almacena los datos del usuario y comienza

a programar el canjeo de puntos. Este canjeo da una recompensa de 20 puntos por cada hora

sin utilizar el celular, esto se puede limitar por parte del programador, por ejemplo, con un límite

de 200 puntos, es decir, 10 horas. Esto para limitar abuso de la mecánica como puede ser dejando

un celular que no se use nunca. Esto no se puede evitar, pero se puede acotar con este sistema.

78

Figura 4.22: Interacción con la aplicación. Fuente: Elaboración propia.

Para la automatización de la tarea, el sistema inicia una alarma interna que le avisa

según este programado, a qué hora revisar el uso de pantalla, hacer la transformación a puntos

y canjearlos. Todo esto es gestionado internamente, por lo que el usuario no debe hacer nada

más. Aunque el sistema, a la hora de canjear los puntos, le mostrará una notificación al usuario

para que este tenga una retroalimentación de que los puntos se canjearon y cuantos fueron ese

día. Aquí también se gestiona la otra variable de seguridad y es que los puntos solo se pueden

canjear  una  vez  al  día,  aunque  esto  sirve  como  una  segunda  capa,  pues  de  por  sí  la  alarma

interna estará programada a una hora específica y por lo mismo, no se debería poder canjear

más de una vez al día, pero le entrega a la aplicación un poco más de robustez.

79

Figura 4.23: Proceso de cobro de puntos. Fuente: Elaboración propia.

4.3. RESUMEN

Este capítulo presenta la arquitectura e implementación del videojuego, describiendo

su estructura técnica y los elementos clave del desarrollo. Se utilizó el modelo 4+1 vistas para

organizar la solución, incluyendo la vista lógica, de desarrollo, de procesos, física y de casos de

uso.

Se  detalla  la  organización  del  código  dentro  de  Godot  Engine,  destacando  el  uso  de  nodos  y

escenas  para  la  construcción  modular  del  juego.  También  se  explica  la  implementación  de

sistemas  fundamentales  como  la  gestión  de  niveles,  los  ataques  del  personaje,  la  inteligencia

artificial de los enemigos y la interfaz de usuario.

Por otro lado, se explica el funcionamiento de la aplicación del sensor y el enfoque en la obtención

de puntos para el perfil de usuario.

Además,  se  profundiza  en  la  integración  con  bGames,  explicando  el  flujo  de  datos  entre  el

videojuego  y  este  servicio.  Se  discuten  los  desafíos  técnicos  enfrentados  y  las  soluciones

adoptadas para garantizar una experiencia fluida y escalable.

80

CAPÍTULO 5.  EVALUACIÓN

Aquí se presentan las pruebas realizadas para validar el correcto funcionamiento de

la solución. Se incluyen pruebas de rendimiento y compatibilidad, junto con una evaluación de los

resultados obtenidos y posibles cambios a aplicar en el proyecto.

5.1. PRUEBAS DE SOFTWARE

5.1.1. Ambientes de prueba

Las pruebas descritas en este apartado se realizaron en los siguientes entornos:

Computador 1 (escritorio):

•  Procesador: AMD Ryzen 7 5700

•  Tarjeta gráfica: Dedicada, AMD Radeon RX 5500XT Challenger D, VRAM: 4GB

•  Memoria RAM: 2x16GB (Dual Channel)

Computador 2 (portátil):

•  Procesador: AMD Ryzen 5 7520U

•  Tarjeta gráfica: Integrada, AMD Radeon Graphics, VRAM: 500MB

•  Memoria RAM: 1x16GB (Single Channel)

5.1.2. Pruebas de compatibilidad

Las  pruebas  de  compatibilidad  se  llevaron  a  cabo  ejecutando  el  videojuego  en

ambos dispositivos. Si bien estos computadores no abarcan una amplia gama de configuraciones

de  hardware,  como  el  uso  de  procesadores  de  otra  marca,  la  arquitectura  del  videojuego  no

presenta razones para suponer que habría incompatibilidades con otros sistemas. Esto se debe

a  que  el  motor  Godot  permite  exportar  juegos  a  múltiples  plataformas  de  escritorio  (Windows,

Linux,  macOS),  y  sus  requisitos  mínimos  son  muy  accesibles,  lo  que  garantiza  una  alta

compatibilidad con la mayoría de PCs modernos (Godot Docs, 2024).

Como  tal,  las  pruebas  de  compatibilidad  se  realizaron  en  conjunto  con  las  pruebas  de

rendimiento, que se detallan en el siguiente apartado.

81

5.1.3. Pruebas de rendimiento

Para evaluar el rendimiento, se desarrolló un script que genera un log al iniciar un

nivel  de  prueba.  En  este  nivel,  se  generan  oleadas  progresivas  de  enemigos  de  manera

incremental para probar distintos niveles de estrés en un solo intento y se desactivan los ataques

del jugador, permitiendo así un incremento continuo en la cantidad de enemigos y objetos en la

escena sin ser eliminados por ataques automáticos.

La variable controlada en esta prueba es la cantidad de enemigos, lo que a su vez incrementa

indirectamente  otras  variables  dependientes  como  el  uso  de  memoria,  la  cantidad  de  objetos

totales, las llamadas de renderizado y la tasa de fotogramas. Las variables registradas en el log

son las siguientes:

•  Enemigos: Cantidad de enemigos en escena, variable controlada que determina el nivel

de carga.

•  Memoria: Uso de memoria RAM, importante para evaluar la eficiencia en el consumo de

recursos del sistema.

•  Objetos: Número total de objetos en escena. Un enemigo, por ejemplo, está compuesto

por múltiples objetos como sprites, colliders y temporizadores que serían los nodos de

Godot. Por lo que este valor refleja la complejidad estructural de la escena.

•  Draw  Calls:  Cantidad  de  llamadas  de  renderizado  realizadas  por  el  motor,  relevantes

para estimar la carga gráfica de la escena.

•  FPS  (fotogramas  por  segundo):  indica  el  rendimiento  perceptible  por  el  jugador.  Un

valor constante de al menos 30 FPS se considera un estándar mínimo aceptable para

garantizar una experiencia fluida, especialmente en videojuegos de acción en tiempo real.

Caídas por debajo de este umbral pueden generar una sensación de lentitud, afectar la

jugabilidad y percibirse como errores de rendimiento.

Estas variables permiten observar cómo responde el motor frente a un incremento progresivo en

la  carga,  permitiendo  identificar  posibles  cuellos  de  botella  en  memoria,  procesamiento  o

renderizado.

82

Prueba 1

En el Computador 1, se realizó un primer test registrando valores cada 3 segundos.

Los resultados se presentan en el siguiente gráfico (valores normalizados para su visualización

en un solo gráfico) de unidad vs tiempo:

Figura 5.1: Gráfico de rendimiento prueba 1, unidad vs tiempo. Fuente: Elaboración propia.

Se  observa  que,  con  el  tiempo,  todos  los  valores  aumentan  o  se  mantienen

constantes, como era esperado. Sin embargo, los FPS comienzan a disminuir significativamente

a partir de los 96 segundos.

Prueba 2

Para  un  análisis  más  detallado,  se  repitió  la  prueba  dos  veces  más  en  el  mismo

equipo, obteniendo gráficos separados por tipo de métrica y comparándolos con la cantidad de

enemigos en escena, pues es este el factor clave para le medición, por lo que ahora todos los

valores serán medidos con los enemigos en el eje X:

83

Figura 5.2: Gráfico de objetos prueba 2, objetos vs enemigos. Fuente: Elaboración propia.

Figura 5.3: Gráfico de Draw Calls prueba 2, cantidad vs enemigos. Fuente: Elaboración propia.

84

Figura 5.4: Gráfico de uso de memoria prueba 2, valor vs enemigos. Fuente: Elaboración propia.

Figura 5.5: Gráfico de FPS prueba 2, valor vs enemigos. Fuente: Elaboración propia.

De  estos  gráficos,  los  FPS  evidencian  el  principal  factor  limitante,  ya  que  se

esperaba que la cantidad de objetos y draw calls aumentara a medida que lo hacían los enemigos.

El  uso  de  memoria,  por  otro  lado,  no  mostró  un  incremento  significativo  y,  por  lo  tanto,  no  se

analizará en profundidad.

85

Como se observa en el gráfico de la figura 5.5, los FPS comienzan a caer cuando

hay aproximadamente 350 enemigos en escena. Si bien este número es alto, su análisis permite

tomar decisiones, como establecer un límite de enemigos simultáneos. Para verificar esto, y en

paralelo con las pruebas de compatibilidad, se repitió el test en el Computador 2. Dado que este

equipo es considerablemente menos potente, se aumentó la frecuencia de registro en el log a 1

segundo para una mayor precisión, obteniendo los siguientes resultados:

Prueba 3

Figura 5.6: Gráfico de rendimiento prueba 3 unidad vs tiempo. Fuente: Elaboración propia.

86

Figura 5.7: Gráfico de FPS prueba 3 valor vs enemigos. Fuente: Elaboración propia.

Nuevamente, se evidencia la caída en los FPS, aunque en este caso el umbral es

menor.  En  este  equipo,  la  caída  comienza  cuando  hay  aproximadamente  150  enemigos  en

escena  y  llegando  rápidamente  bajo  el  umbral  de  los  30  FPS.  A  partir  de  estas  pruebas,  se

pueden extraer las siguientes conclusiones y tomar las siguientes decisiones:

•  El videojuego es compatible con los equipos testeados, aunque es necesario ampliar las

pruebas en otros dispositivos.

•  Tomando  como  referencia  el  equipo  de  menor  rendimiento,  se  establecerá  un  límite

máximo de 100 enemigos simultáneos, dejando un margen de 50 para otros elementos

como ataques del jugador y efectos visuales del nivel.

•  Dado que el límite fue determinado en función del Computador 2, se tomará este equipo

como referencia para definir los requisitos mínimos del videojuego.

•  Los  requisitos  mínimos  del  videojuego  corresponderán  a  las  especificaciones  del

Computador 2, mientras que los requisitos recomendados serán los del Computador 1,

ya que es el equipo principal de desarrollo. Estos requisitos podrán ajustarse conforme

se realicen pruebas en una mayor variedad de dispositivos.

87

5.2. PRUEBAS DE ACEPTACIÓN

En este capítulo se presentan las pruebas de aceptación realizadas para Nightmare

Survivor,  con  el  objetivo  de  asegurar  que  el  juego  cumple  con  los  requisitos  definidos.  Cada

prueba tiene un identificador único y evalúa aspectos clave como el movimiento del personaje, la

generación de enemigos, la progresión del jugador, la interfaz de usuario, el sistema de guardado

y el sonido.

Las pruebas siguen un formato estructurado que incluye una descripción del escenario, los pasos

a seguir, el resultado esperado y el resultado obtenido. Esto permite detectar errores y realizar

mejoras  antes  de  la  versión  final.  Los  identificadores  de  las  pruebas  (PA-XX  con  XX  para

numeración) ayudan a organizarlas y relacionarlas con los requisitos funcionales y no funcionales

del juego.

La evaluación es realizada por el cliente, en este caso profesor, el cual colocará en el apartado

de resultado obtenido una calificación en una escala de letras de la A a la E, o “N/A” cuando la

prueba no aplique. A continuación, se detallan los significados de cada calificación:

•  A  (Excelente):  Cumple  completamente  con  el  requisito  y  supera  las  expectativas.  No

requiere mejoras.

•  B  (Bueno):  Cumple  con  el  requisito  de  forma  satisfactoria.  Puede  haber  pequeños

detalles menores, pero no afectan la funcionalidad.

•  C (Aceptable): Cumple de forma mínima con el requisito. Se considera aceptado, pero

se recomienda revisión o mejora futura.

•  D  (Deficiente):  No  cumple  adecuadamente  con  el  requisito.  Requiere  ajustes

importantes.

•  E (Inaceptable): No cumple con el requisito. Necesita corrección inmediata.

•  N/A (No aplica): El requisito no es aplicable en el contexto de esta prueba específica.

Se considera que una prueba es aprobada cuando obtiene una calificación de A, B o C, mientras

que una calificación de D o E indica que la prueba no ha sido superada y requiere corrección.

88

Tabla 5.1: Prueba de aceptación 01. Fuente: Elaboración propia.

PA-01
Movimiento de personaje
Verificar que el personaje pueda moverse en cuatro direcciones.

ID
Nombre
Descripción
Requisito cubierto  RF-NS-01
Pasos

1. Iniciar el juego y comenzar una partida.
2. Intentar mover al personaje en todas las direcciones (arriba, abajo,
izquierda, derecha)
El personaje se mueve en todas las direcciones sin problemas.

Resultado
esperado
Resultado
obtenido
Observaciones

A

Tabla 5.2: Prueba de aceptación 02. Fuente: Elaboración propia.

PA-02
Generación de enemigos en oleadas
Verificar que el juego genere enemigos en oleadas progresivas.

ID
Nombre
Descripción
Requisito cubierto  RF-NS-02
Pasos

1. Iniciar el juego y comenzar una partida.
2. Observar si los enemigos aparecen en intervalos de tiempo predefinidos.

Resultado esperado  Los enemigos aparecen en oleadas y en intervalos de tiempo progresivos.
Resultado obtenido  A
Observaciones

Tabla 5.3: Prueba de aceptación 03. Fuente: Elaboración propia.

ID

Nombre
Descripción

PA-03

Generación de enemigos infinita con aumento de dificultad
Verificar que los enemigos continúen apareciendo indefinidamente y
aumente la dificultad.

Requisito cubierto  RF-NS-02
Pasos

Resultado
esperado
Resultado
obtenido
Observaciones

1. Iniciar el juego y comenzar una partida en modo infinito.
2. Jugar por 3-5 minutos.
3. Observar si la cantidad de enemigos o su fuerza aumenta con el tiempo.
Los enemigos aparecen de forma continua y su dificultad aumenta
progresivamente.

A

89

Tabla 5.4: Prueba de aceptación 04. Fuente: Elaboración propia.

ID

Nombre
Descripción

PA-04

Recolección de recursos
Verificar que los enemigos derrotados dejen caer recursos que el jugador
pueda recoger.

Requisito cubierto  RF-NS-04
Pasos

1. Iniciar una partida y derrotar enemigos.
2. Observar si los enemigos derrotados dejan caer recursos.
3. Intentar recoger los recursos.
Los enemigos dejan recursos al ser derrotados, y el jugador puede
recogerlos.

A

Tabla 5.5: Prueba de aceptación 05. Fuente: Elaboración propia.

PA-05

Aumento de nivel
Verificar que el jugador gane experiencia y suba de nivel al alcanzar un
umbral específico.

Requisito cubierto  RF-NS-05
Pasos

1. Derrotar enemigos para ganar experiencia.
2. Verificar si al alcanzar un umbral el nivel del personaje aumenta.
El personaje sube de nivel al alcanzar la cantidad de experiencia requerida.

A

Tabla 5.6: Prueba de aceptación 06. Fuente: Elaboración propia.

PA-06

Elección de habilidades
Verificar que el jugador pueda elegir una habilidad al subir de nivel.

Descripción
Requisito cubierto  RF-NS-06
Pasos

1. Subir de nivel en el juego.
2. Observar la pantalla de selección de mejoras.
3. Seleccionar una habilidad.
4. Esperar a atacar con la habilidad seleccionada.
Resultado esperado  El jugador puede elegir una habilidad al subir de nivel y esta se activa.
Resultado obtenido  A
Observaciones

Resultado
esperado
Resultado
obtenido
Observaciones

ID

Nombre

Descripción

Resultado
esperado
Resultado
obtenido
Observaciones

ID

Nombre

90

Tabla 5.7: Prueba de aceptación 07. Fuente: Elaboración propia.

PA-07
Elección de estadísticas
Verificar que el jugador pueda elegir mejorar estadísticas al subir de nivel.

ID

Nombre
Descripción
Requisito cubierto  RF-NS-08
Pasos

1. Subir de nivel en el juego.
2. Observar la pantalla de selección de mejoras.
3. Seleccionar una estadística.
4. Esperar para ver el cambio en la estadística seleccionada.

Resultado esperado  El jugador puede mejorar una estadística al subir de nivel.
Resultado obtenido  A
Observaciones

Tabla 5.8: Prueba de aceptación 08. Fuente: Elaboración propia.

ID

PA-08

Evolución de habilidad
Verificar que una habilidad evolucione al cumplir los requisitos.

Nombre
Descripción
Requisito cubierto  RF-NS-10
Pasos

1. Subir una habilidad hasta su nivel máximo.
2. Obtener el atributo necesario para la evolución.
3. Observar si la habilidad evoluciona.

Resultado esperado  La habilidad evoluciona correctamente al cumplir los requisitos.
Resultado obtenido  A
Observaciones

Tabla 5.9: Prueba de aceptación 09. Fuente: Elaboración propia.

ID

PA-09

Elementos del HUD
Verificar que los elementos del HUD muestren la información correcta.

Nombre
Descripción
Requisito cubierto  RF-NS-11
Pasos

1. Iniciar una partida.
2. Observar los indicadores de vida, experiencia, monedas y tiempo.

Resultado esperado  Los elementos del HUD muestran la información correcta y actualizada.
Resultado obtenido  A
Observaciones

91

Tabla 5.10: Prueba de aceptación 10. Fuente: Elaboración propia.

ID

PA-10

Selector de apariencia
Verificar que el jugador pueda cambiar la apariencia del personaje.

Nombre
Descripción
Requisito cubierto  RF-NS-17
Pasos

1. Abrir el menú de personalización.
2. Seleccionar una apariencia distinta.
3. Ingresar a un nivel para comprobar el cambio.
Resultado esperado  El personaje cambia de apariencia correctamente según la selección.
Resultado obtenido  A
Observaciones

Tabla 5.11: Prueba de aceptación 11. Fuente: Elaboración propia.

ID

PA-11

Sonido
Verificar que el juego tenga música de fondo y efectos de sonido.

Nombre
Descripción
Requisito cubierto  RNF-NS-01
Pasos

1. Iniciar el juego.
2. Observar si la música de fondo y efectos de sonido funcionan
correctamente.
La música de fondo y efectos de sonido se reproducen correctamente.

Resultado
esperado
Resultado obtenido  NA
Observaciones

No lo puedo evaluar en remoto

Tabla 5.12: Prueba de aceptación 12. Fuente: Elaboración propia.

PA-12

Ventana de bGames
Verificar que la ventana de bGames se abra y funcione correctamente.

ID

Nombre

Descripción
Requisito cubierto  RF-NS-22
Pasos

1. Acceder al menú de bGames.
2. Iniciar sesión.
3. Verificar que los datos del perfil se carguen correctamente.
4. Intentar realizar una compra o canje.

Resultado esperado  La ventana de bGames se abre y permite realizar las acciones esperadas.
Resultado obtenido  A
Observaciones

92

Tabla 5.13: Prueba de aceptación 13. Fuente: Elaboración propia.

ID

PA-13

Tutorial
Verificar que el tutorial aparezca cuando corresponde.

Nombre
Descripción
Requisito cubierto  RF-NS-19
Pasos

1. Iniciar una partida nueva.
2. Verificar si se muestra la intro y los primeros tutoriales según la progresión
de juego inicial.
El tutorial aparece en el momento adecuado.

Resultado
esperado
Resultado
obtenido
Observaciones

A

Tabla 5.14: Prueba de aceptación 14. Fuente: Elaboración propia.

ID

PA-14

Permanencia de datos
Verificar que los datos del jugador se guarden.

Nombre
Descripción
Requisito cubierto  RF-NS-16
Pasos

1. Iniciar una partida nueva.
2. Avanzar en el nivel más tiempo que la última vez registrada.
3. Utilizar el menú de pausa para salir del nivel.
4. Cerrar y abrir el juego.
5. Confirmar que el tiempo máximo se mantuvo.

Resultado esperado  Los datos del jugador se mantienen después de cerrar y reiniciar el juego.
Resultado obtenido  A
Observaciones

En general, las 13 de las 14 pruebas realizadas fueron calificadas con “A”, por lo que

obtuvieron los resultados esperados. El caso PA-11, referente al sonido, es el  único  calificado

con  N/A,  pues  el  medio  utilizado  para  su  prueba  no  permitía  reproducción  de  sonido,  pero

posteriormente se entregó una muestra en video para la confirmación de esta. Por lo mismo, no

fue necesario realizar ningún cambio en el proyecto a la hora de la entrega.

Se omiten todo tipo de pruebas para la aplicación ya que no puede ser testeada en un dispositivo

real, pues los servicios de bGames solo están disponibles de forma local a la hora de realizar el

proyecto.

93

5.3. RESUMEN

En  este  capítulo  se  presentan  las  pruebas  y  evaluaciones  realizadas  sobre  el

videojuego,  asegurando  su  estabilidad,  rendimiento  y  jugabilidad.  Se  realizaron  pruebas  de

compatibilidad, rendimiento y aceptación, evaluando la capacidad del juego para ejecutarse en

diferentes dispositivos y garantizar una experiencia fluida.

Las pruebas de rendimiento analizaron el uso de memoria, la tasa de cuadros por segundo (FPS)

y la carga de procesamiento del motor gráfico. Se identificaron cuellos de botella y se aplicaron

optimizaciones para mejorar la eficiencia del juego, especialmente en escenarios con una gran

cantidad de enemigos simultáneos.

94

CAPÍTULO 6.  CONCLUSIONES

El  capítulo  final  ofrece  una  evaluación  global  del  proyecto,  analizando  los  logros

alcanzados y las dificultades encontradas. Se revisa el cumplimiento de los objetivos y se discuten

posibles  mejoras.  Finalmente,  se  proponen  líneas  de  trabajo  futuro  para  la  evolución  y

optimización de la solución desarrollada.

6.1. OBJETIVOS

A continuación, se realiza una evaluación sobre el cumplimiento de los objetivos,

tanto el objetivo general como los objetivos específicos.

6.1.1. Objetivos específicos

Elaborar un documento de diseño de juego (GDD).

Aunque el GDD no fue detallado en profundidad en el informe, se creó en la fase

inicial  del  proyecto  y  se  actualizó  conforme  se  agregaban  y  modificaban  elementos  del

videojuego. Al tratarse de un proyecto independiente, el documento cumplió su función como una

guía  referencial  sin  necesidad  de  una  alta  complejidad.  Dicho  documento  se  encuentra  en  el

anexo del informe, por lo que este objetivo se considera completado satisfactoriamente.

Implementar el juego a partir del GDD.

A  lo  largo  del  desarrollo,  el  videojuego  se  implementó  siguiendo  las  directrices

establecidas en el GDD. Además, cualquier cambio sustancial en la propuesta inicial fue revisado

y  reflejado  en  el  documento  cuando  fue  necesario.  Por  lo  tanto,  este  objetivo  también  fue

cumplido exitosamente.

Aplicar el framework de bGames para la modificación de mecánicas.

Se logró integrar bGames en el videojuego, permitiendo la modificación de una mecánica

específica. En este caso, la conexión con el  framework se implementó a través del sistema de

compra de rerolls, que permite cambiar las tarjetas de mejora al subir de nivel en una partida.

Dado  que  la  funcionalidad  fue  implementada  correctamente,  este  objetivo  se  considera

alcanzado.

95

Implementar al menos un sensor para captura de datos que alimenten al perfil de usuario
en bGames.

Este  objetivo  también  fue  cumplido,  ya  que  se  desarrolló  la  aplicación  Screen  Time

Analyzer, que detecta el uso de la pantalla del dispositivo y otorga puntos al perfil de bGames en

función del tiempo de no uso del teléfono.

6.1.2. Objetivo general

Desarrollar un juego del género survivors utilizando el motor Godot e integrándolo con el

framework bGames para ampliar su catálogo.

Dado que todos los objetivos específicos fueron completados con éxito, es posible

evaluar el cumplimiento del objetivo general. Analizando cada uno de sus componentes:

•  Se desarrolló un videojuego de acuerdo con los lineamientos establecidos.

•  El juego pertenece al género survivors, respetando sus características fundamentales.

•

 El desarrollo se realizó en el motor Godot, cumpliendo con la herramienta establecida.

•  Se integró el framework bGames, permitiendo su vinculación con la plataforma.

•  El  videojuego  contribuye  a  la  expansión  del  catálogo  de  bGames,  alineándose  con  la

finalidad del proyecto.

Y  dado  el  estado  de  los  puntos  anteriormente  presentados,  se  puede  concluir  que  el  objetivo

general fue alcanzado en su totalidad.

6.2. IMPLICACIONES

El desarrollo de este videojuego e  integración con  bGames ha generado  diversas

implicaciones tanto técnicas como de experiencia de usuario. Desde un punto de vista técnico,

se  demostró  que  es  posible  vincular  un  motor  de  código  abierto  como  Godot  Engine  con  un

framework de gamificación como bGames, lo que abre la puerta a futuras implementaciones en

otros juegos independientes.

En  términos  de  jugabilidad,  la  mecánica  de  integración  con  bGames  permitió  explorar  nuevas

formas de incentivar la participación del jugador mediante recompensas basadas en su actividad

fuera del juego.

Desde  una  perspectiva  académica,  este  proyecto  contribuye  al  estudio  de  Blended  Games,

proporcionando otro caso práctico de integración de mecánicas externas en la jugabilidad. Esto

96

podría inspirar futuras investigaciones sobre la efectividad de los videojuegos como herramientas

para la modificación de hábitos.

6.3. ALCANCES Y LIMITACIONES

El  presente  trabajo  logró  el  desarrollo  de  un  videojuego  del  género  survivors  en

Godot  Engine,  integrando  mecánicas  de  progresión  y  combate  características  del  género.

Además, se consiguió la compatibilidad con bGames, permitiendo la interacción con el perfil para

modificar aspectos de la jugabilidad.

Es importante mencionar que no se realizó una validación empírica del impacto del juego en la

reducción  del  sedentarismo  tecnológico,  ya  que  el  enfoque  estuvo  centrado  en  la  viabilidad

técnica  y  la  integración  con  bGames.  Si  bien  se  espera  que  el  videojuego  contribuya

indirectamente a la reducción del sedentarismo tecnológico al incentivar la actividad del jugador,

este efecto no fue medido ni validado dentro del alcance del proyecto.

Las limitaciones del videojuego se ven reflejadas en algunos factores no testeados, por ejemplo,

la  compatibilidad  con  una  variedad  más  amplia  de  dispositivos.  Además,  de  factores  de

disponibilidad de contenido, esto debido a que el juego no está completado, pues solo se tiene

disponible el nivel 1 y el nivel infinito. Sumado a lo anterior, no todas las habilidades y atributos

están  implementados  y  son  accesibles  para  los  jugadores.  Así  como  las  opciones  de

personalización de apariencia que de momento son escasas.

Para tratar también al sensor, este queda como una buena alternativa para conectar la actividad

del  teléfono,  es  decir,  la  vida  diaria,  con  el  perfil  de  usuario  en  bGames.  Aunque  una  de  las

limitaciones importantes fueron las pruebas, pues como bGames solo estaba arriba localmente,

la aplicación solo podría ser probada en el simulador. Por lo tanto, no se pudieron hacer pruebas

descargando la aplicación y probándola en entornos reales.

6.4. TRABAJO FUTURO

Como se mencionó en el punto anterior, el juego no se encuentra completado, por

lo tanto, como trabajo futuro personal quedaría completar el resto de los niveles planificados, es

decir,  nivel  2,  3  y  4.  Además  de  implementar  todas  las  habilidades  y  atributos  que  quedaron

pendientes.  Parte  del  trabajo  de  esto  se  ve  solventado  por  la  implementación  del  sistema  de

versiones, que da bastante facilidad a actualizaciones futuras del videojuego.

97

Otro apartado importante es la actualización de la divisa de bGames, esto tanto para el videojuego

como el sensor. Pues al momento de terminar ambos, fueron probados con  bGames levantado

localmente, por lo que no está equilibrada la obtención y el gasto de puntos en un perfil normal.

Con  esto,  habría  que  actualizar  también  los  datos  de  los  endpoints  para  hacer  las  llamadas

correspondientes cuando el servicio de bGames se encuentre levantado correctamente.

Con  respecto  a  bGames,  queda  como  trabajo  futuro  comprobar  o  medir  de  alguna  forma  su

impacto en la reducción del sedentarismo tecnológico.

6.4.1. Distribución y publicación

El  videojuego

fue  publicado  bajo  el  nombre  Nightmare  Survivor  Demo,

denominación que se adoptó al momento de su liberación para dejar explícito que se trata de una

versión preliminar del producto. Esta versión se encuentra disponible de manera gratuita a través

de la plataforma itch.io (https://pixtale-games.itch.io/nightmare-survivor-demo) y cuenta con todos

los derechos reservados por su autor. Asimismo, se ha publicado un video demostrativo a modo

de tráiler en YouTube (https://youtu.be/Ylb5Fl56zvc), con el objetivo de facilitar su difusión y la

comprensión de su jugabilidad. La publicación se realizó bajo el sello  PixTale Games, nombre

que representa  un estudio  independiente de  desarrollo de videojuegos.  Esta identidad ha sido

establecida como marca formal para su uso en futuros proyectos personales dentro del mismo

ámbito creativo.

6.5. REFLEXIONES FINALES

El  desarrollo  de  este  proyecto  permitió  explorar  la  creación  de  un  videojuego  del

género survivors en Godot Engine, con el desafío adicional de integrar funcionalidades externas

a través del framework bGames. A lo largo del proceso, se identificaron tanto fortalezas como

áreas  de  mejora  en  el  diseño,  implementación  y  optimización  de  un  videojuego.  Los  desafíos

encontrados  a  lo  largo  del  desarrollo  llevaron  a  un  proceso  de  aprendizaje  continuo  y  a  la

definición  de  un  enfoque  preferido  para  la  creación  de  mecánicas,  favoreciendo  sistemas

modulares y escalables que facilitan futuras modificaciones que dan más control al desarrollador.

Godot  Engine  cumplió  un  papel  importante  en  el  desarrollo,  pues  da  muchas  facilidades  al

desarrollador y demuestra ser una herramienta potente y relativamente sencilla de aprender. Con

esto se pudo llevar el desarrollo sin problemas por parte del motor. Quedando así, incluso como

una preferencia personal.

98

Finalmente,  el  desarrollo  de  este  proyecto  no  solo  permitió  profundizar  en  la  creación  de

videojuegos y la integración de tecnologías externas, sino que también resaltó la importancia de

la iteración, la adaptabilidad y la planificación a largo plazo en el diseño de sistemas de juego.

99

REFERENCIAS BIBLIOGRÁFICAS

Apperley, T. (2006). Genre and Game Studies: Toward a Critical Approach to Video Game

Genres. Simulation and Gaming. Recuperado de:

https://doi.org/10.1177/1046878105282278

Canle, E. (2022). ¿Cómo funciona un motor gráfico?. Tokio School. Recuperado de

https://www.tokioschool.com/noticias/como-funciona-motor-grafico/

Cabezas, S. (2022). Metodología Kanban y diseño de videojuegos. LinkedIn. Recuperado de

https://es.linkedin.com/pulse/metodología-kanban-y-diseño-de-videojuegos-sergio-g-

cabezas

Calistro, D. (2019). b-Games: framework enfocado en el desarrollo de servicios de datos para

videojuegos mapeando fuentes de información al perfil de un usuario. Universidad de

Santiago de Chile.

Castro-Sánchez, M., Linares Manrique, M., Sanromán-Mata, S., & Pérez-Cortés, A. J. (2017).

Análisis de los comportamientos sedentarios, práctica de actividad física y uso de

videojuegos en adolescentes. Sportis, 3(2), 241-255.

Deterding, S., Dixon, D., Khaled, R., & Nacke, L. (2011). From game design elements to

gamefulness: Defining “gamification”. Proceedings of the 15th International

Academic MindTrek Conference.

Esposito, N. (2005). A Short and Simple Definition of What a Videogame Is. In Proceedings of

DiGRA 2005 Conference: Changing Views – Worlds in Play. Recuperado de:

https://www.digra.org/digital-library/publications/a-short-and-simple-definition-of-what-

a-videogame-is/

Fernández, I. (2023). Desarrollo de videojuego shooter multijugador en Unreal Engine

incorporando el framework Blended Games. Universidad de Santiago de Chile.

flanne. (2023). 20 Minutes Till Dawn. Steam. Recuperado de:

https://store.steampowered.com/app/1966900/20_Minutes_Till_Dawn/

Flores, A. (2020). 10 apps que te ayudarán a llevar una vida saludable desde casa. Conecta.

Recuperado de https://conecta.tec.mx/es/noticias/sinaloa/salud/10-apps-que-te-

ayudaran-llevar-una-vida-saludable-desde-casa

Game Smithing Limited. (2023). Soulstone Survivors. Steam. Recuperado de:

https://store.steampowered.com/app/2066020/Soulstone_Survivors/

100

GlitchGuru. (2022, October 30). Game Engines: A Comparative Analysis. Medium. Recuperado

de: https://medium.com/@GlitchGuru/game-engines-a-comparative-analysis-

ef9af01f125e

Godot Docs. (2024). System requirements: Hardware requirements. Godot Engine

documentation. Recuperado de:

https://docs.godotengine.org/en/stable/about/system_requirements.html#hardware-

requirements

Jaulent, E. (2024). metodología RAD. uCloud. Recuperado de

https://ucloudglobal.com/blog/metodologia-rad/

Hilliard, K. (2024). What Is The Difference Between Roguelike And Rogue-lite?. Game Informer.

Recuperado de https://www.gameinformer.com/faq/2024/04/13/what-is-the-difference-

between-roguelike-and-rogue-lite

Kruchten, P. (1995). The 4+1 View Model of Architecture. IEEE Software, 12(6), 42–50.

https://doi.org/10.1109/52.469759

Kukurelo Cruz, D. El estilo visual utilizado en videojuegos indie modernos y su efecto en el

jugador peruano. Caso de estudio: Summon Hat y Tunche.

López, V. (2022). Smartwatch: un recurso que ayuda a romper con el sedentarismo y a caminar

más. La Vanguardia. Recuperado el 18 de junio de 2024 de

https://www.lavanguardia.com/magazine/lifestyle/20220730/8441324/smartwatch-

recurso-ayuda-romper-sedentarismo-caminar-mas-pmv.html

Mahu, L. (2020). Ambiente para el almacenamiento y disponibilización ubicua de perfiles de

usuario del framework BlendedGames. Universidad de Santiago de Chile.

MedlinePlus. (s.f). Health Risks of an Inactive Lifestyle. Recuperado el 18 de junio de 2024 de

https://medlineplus.gov/healthrisksofaninactivelifestyle.html

Muñoz, C. (2024). Aplicación del framework bGames al videojuego Terraria a través de un mod

y sensores especializados. Universidad de Santiago de Chile.

Oh, Y., & Yang, S. (2010). Defining exergames & exergaming. Proceedings of Meaningful Play

2010.

Onetto, B. (2023). Blazing Duel: Videojuego de Lucha con la implementación del framework de

Blended Games. Undergraduate Thesis. Universidad de Santiago de Chile.

101

Ortiz de Murua, I. (2022). 'Exergames': videojuegos contra el sedentarismo. Deia. Recuperado

de https://www.deia.eus/ciencia-y-tecnologia/2022/04/10/exergames-videojuegos-

sedentarismo-1712837.html

poncle. (2022). Vampire Survivors. Steam. Recuperado de:

https://store.steampowered.com/app/1794680/Vampire_Survivors/

Riot Cadmus. (2024, septiembre 23). Looking forward for Arena and Swarm. Riot Games.

Recuperado de: https://www.leagueoflegends.com/es-mx/news/dev/dev-looking-

forward-for-arena-and-swarm/

Simken Ruminot, G. A. (2023). Desarrollo de mods basados en bGames para el videojuego

Minecraft. Universidad de Santiago de Chile.

Soto, M & Failde, I. (2004). La calidad de vida relacionada con la salud como medida de

resultados en pacientes con cardiopatía isquémica. Revista de la Sociedad Española

del Dolor vol.11 no.8. Recuperado de

https://scielo.isciii.es/scielo.php?script=sci_arttext&pid=S1134-80462004000800004

Staiano, A. E., & Calvert, S. L. (2011). Exergames for Physical Education Courses: Physical,

Social, and Cognitive Benefits. Child Development Perspectives, 5(2), 93–98.

Ternero Silva, G. A. (2019). Village Defender: videojuego de estrategia multiplataforma

aplicando el framework Blended Games. Universidad de Santiago de Chile.

102

A. Anexo

A. GAME DESIGN DOCUMENT

A.1. VISIÓN GENERAL DEL JUEGO

A.1.1. TÍTULO DEL JUEGO

Nightmare Survivor.

A.1.2. GÉNERO/S

•  Survivors

•  Roguelite

•  Bullet-hell

A.1.3. PÚBLICO OBJETIVO

Jóvenes y Adultos.

A.1.4. PLATAFORMA(S)

Inicialmente, solo PC.

A.2. HISTORIA Y NARRATIVA

A.2.1. SINOPSIS DEL JUEGO

Nightmare Survivor es un juego de acción y supervivencia ambientado en el inquietante mundo

de  las  pesadillas.  Como  una  esfera  de  energía  onírica  atrapada  en  un  ciclo  interminable  de

sueños,  deberás  enfrentar  oleadas  de  entidades  terroríficas  mientras  exploras  los  paisajes

distorsionados de la mente humana. Las habilidades y armas que adquieras están inspiradas en

elementos  que  fomentan  el  descanso  y  la  tranquilidad,  evolucionando  hasta  convertirse  en

herramientas poderosas contra los horrores de las pesadillas.

A.2.2. CONTEXTO/HISTORIA DE FONDO

En Nightmare Survivor, el protagonista es una esfera de energía atrapada en un ciclo de sueños

perturbadores. Cada nivel representa una noche de sueño distorsionada por pesadillas, donde

las entidades hostiles son manifestaciones de miedos y ansiedades del subconsciente.

Guiado por Morph, un personaje enigmático, el objetivo es recolectar Fragmentos de Ensueño,

piezas  de  energía  que  restauran  el  equilibrio  en  este  mundo  onírico.  A  medida  que  la  esfera

avanza, se enfrenta a enemigos que encarnan pesadillas y miedos profundos o recurrentes.

El propósito no es desentrañar una historia compleja, sino sobrevivir a las oleadas de enemigos

y mejorar al personaje utilizando habilidades y atributos vinculados al descanso y la calma. Con

103

cada victoria, el jugador se acerca a la posibilidad de escapar del ciclo de pesadillas y alcanzar

un sueño reparador.

A.2.3. PROGRESIÓN NARRATIVA

La  narrativa  de  Nightmare  Survivor  no  sigue  una  estructura  lineal  tradicional,  sino  que  está

integrada  en  la  atmósfera  y  los  elementos  del  juego.  A  medida  que  el  jugador  avanza  por  los

niveles (representando diferentes etapas del sueño), la historia y el mundo se revelan de forma

ambiental y a través de interacciones con NPC.

A.2.4. EVENTOS CLAVE

Los eventos clave son:

•  Primeras charlas con Morph e introducción del mundo

•  Derrota del primer jefe

•  Derrota del segundo jefe

•  Derrota del tercer jefe

•  ¿Derrota de jefe final?

A.3. JUGABILIDAD

A.3.1. NIVELES Y TARJETAS

El juego consistirá en algunas etapas independientes. Al iniciar cada etapa el jugador siempre

inicia en nivel 0. Al subir de nivel se mostrarán aleatoriamente 3 tarjetas con posibles mejoras con

las  que  el  jugador  puede  mejorar  sus  atributos,  seleccionar  una  nueva  habilidad  o  mejorar

habilidades/atributos que ya tenga. Solo se pueden tener a la vez un total de 5 habilidades nuevas

y 5 atributos  para  mejorar, luego  de  llegar  al  límite, las tarjetas se comenzarán a repetir en  la

selección  dejando  solo  la  opción  de  mejorar  habilidades  o  atributos  ya  seleccionados

anteriormente.

En el menú inicial, es decir, en el entorno fuera de los niveles se puede mejorar los atributos de

forma permanente base para poder llegar más lejos y tener menos dificultades para avanzar

A.3.2. ATRIBUTOS

El juego tendrá 12 atributos básicos que se pueden subir durante la etapa, estos son:

•  Velocidad de movimiento

•  Vida máxima

•  Defensa

•  Evasión

104

•  Cantidad de proyectiles

•  Daño

•  Velocidad de ataque

•  Experiencia

•  Regeneración de vida

•  Rango de recoger

•  Probabilidad de crítico

•  Daño crítico

A.3.3. HABILIDADES BÁSICAS

El juego tendrá 12 habilidades básicas, cada una está directamente relacionada con uno de los

atributos en el orden respectivo:

•  Aliento de nube

•  Ruido verde

•  Pulso de lavanda

•  Capa de algodón

•  Llama del amanecer

•  Disparo lunar

•  Estrella de la mañana

•  EnviOveja

•  Almohada mina

•  Estrella fugaz

•  Filo del silencio

•  Oso Teddy

Su inspiración son cosas que están relacionadas con el sueño, la noche y la relajación de forma

positiva.

A.3.4. EVOLUCIONES

Al haber elegido en la etapa alguna habilidad y su atributo seleccionado y al tener la habilidad en

nivel 5 se desbloqueará la opción de evolucionar la habilidad en una versión más poderosa, y en

orden respectivo son las siguientes:

•  Aire fresco

•  Ruido marrón

•  Brisa floral

•  Manta de animal print

105

•  Fenix del amanecer

•  Gravedad lunar

•  Estrella brillante

•  Detonación de plumas

•  Destello radiante

•  Velo de calma

•  Teddy de la infancia

A.3.5. OBJETIVOS DE JUGADOR

El jugador debe sobrevivir durante un tiempo limitado usando habilidades y mejoras para soportar

las oleadas de enemigos.

A.3.6. SISTEMA DE COMBATE

El jugador tiene la selección de ataques los cuales son automáticos cada cierto tiempo apuntando

al  enemigo  más  cercano,  a  todos  en  un  rango  o  a  un  enemigo  aleatorio.  Por  el  lado  de  los

enemigos, estos se acercarán siempre al jugador.

A.3.7. ECONOMÍA DEL JUEGO

El juego tendrá 3 tiendas en el menú inicial, en 2 ellas se podrá comprar mejoras permanentes

para los niveles y en la otra, cambios estéticos.

La moneda de cambio será obtenible jugando y completando niveles.

A.3.8. DIFICULTAD Y CURVA DE APRENDIZAJE

Se espera que los primeros intentos no se puedan ganar, pero usando las mejoras permanentes

sea posible avanzar. La curva de aprendizaje es baja.

A.3.9. INTEGRACIÓN CON BGAMES

Para la integración de bGames en el videojuego, se creará una ventana especial que realice las

conexiones pertinentes. La idea es poder usar los puntos de bGames para poder comprar alguna

ventaja dentro del juego, esa ventaja es la siguiente: Cambios en las tarjetas. Al subir de nivel

aparecen 3 tarjetas aleatorias, estas tarjetas se pueden cambiar por otras 3, lo que se conoce

como reroll. Estos cambios se podrán comprar en el apartado de bGames y se irán gastando con

su uso.

106

Esta integración evita que el juego se rompa, pues es difícil abusar de esto. Los usuarios que

tengan muchos rerolls solo estarán comprando un poco de suerte, pero un jugador que no tiene

estos puntos puede llegar al mismo resultado en una partida.

A.3.10. CONTROLES

Se usarán las teclas W, A, S, D para moverse por el mapa y se usará el mouse para momentos

de selección y menú.

A.4. DISEÑO DE NIVELES

A.4.1. GENERAL DE NIVELES

Cada nivel tendrá temática lo suficientemente genérica, pero cada uno tendrá detalles que los

relacionen con el jefe de este. Además, los niveles serán acotados, es decir, tendrán límites fijos,

pero serán lo suficientemente grandes para permitirle cierta libertad de movimiento al jugador.

A.4.2. PROGRESIÓN DE NIVELES

Dentro de cada nivel, la progresión de dificultad derivará de los factores cantidad de enemigos y

dificultad de enemigos. Además, cada nivel será más difícil que el anterior ajustando los mismos

factores antes mencionados.

A.4.3. ELEMENTOS INTERACTIVOS

Habrá pocos elementos interactivos dentro del nivel. Estos estarán enfocados en ser elementos

destruibles que dejen caer elementos como monedas o alguna mejora temporal.

A.4.4. LISTA DE NIVELES

107

Figura A.0.1: Lista de niveles. Fuente: Elaboración propia.

A.5. PERSONAJES

A.5.1. DESCRIPCIÓN DE PERSONAJES JUGABLES

El personaje jugable es una esfera, no tiene ninguna característica destacable. Sin embargo, en

una tienda del juego se podrán desbloquear accesorios para agregarle y cambios de  color, por

ejemplo, dotando al personaje de un cierto nivel de personalización.

A.5.2. DESCRIPCIÓN DE PERSONAJES NO JUGABLES

Morph:  Un  misterioso  guía  también  atrapado  en  el  mundo  de  las  pesadillas.  Parece  estar

interesado en los fragmentos de ensueño, por lo que se los intercambiará al jugador por mejoras

permanentes o accesorios. Durante la aventura le dará al jugador una serie de consejos.

A.5.3. DESCRIPCIÓN DE ENEMIGOS Y JEFES

A.5.3.1. ENEMIGOS

Se presenta la lista de enemigos disponibles:

108

Figura A.0.2: Ficha de Ghoul. Fuente: Elaboración propia.

Figura A.0.3: Ficha de Swift Ghoul. Fuente: Elaboración propia.

109

Figura A.0.4: Ficha de Bulwark Ghoul. Fuente: Elaboración propia.

Figura A.0.5: Ficha de Fading Ghoul. Fuente: Elaboración propia.

A.5.3.2. JEFES

Se presenta la lista de jefes totales (de momento, solo el primer jefe está implementado):

110

Figura A.0.6: Ficha jefe Shadow King. Fuente: Elaboración propia.

Figura A.0.7: Ficha jefe Nightweaver. Fuente: Elaboración propia.

111

Figura A.0.8: Ficha jefe Crimson Grin. Fuente: Elaboración propia.

Figura A.0.9: Ficha jefe Nightmare Core. Fuente: Elaboración propia.

A.6. ARTE Y ESTILO VISUAL

A.6.1. ESTILO VISUAL

112

El estilo visual es uno pixel art, pero con líneas gruesas, de 2 a 3 pixeles de ancho, y dentro del

juego no se usará pixel perfecto, quedando suavizado. Por lo que es un estilo en medio del pixel

art y el dibujo tradicional.

A.6.2. DISEÑO DE ENTORNOS Y ESCENARIOS

Para  la  construcción  de  escenarios  se  hará  uso  del  sistema  de  tiles  de  godot.  Además,  cada

escenario debe contar con una versión de nivel normal y un escenario para la pelea contra el jefe

del nivel.

Cada nivel debe tener un motivo que acompañe tanto a la ambientación como al jefe. Por ejemplo,

el nivel 1 se trata de un pueblo fantasma, pero el tercer nivel, al tener de jefe final a un payaso,

transcurrirá en un circo.

A.6.3. DISEÑO DE PERSONAJES

Los  personajes  son  sencillos,  ya  que  se  trata  de  esferas,  esto  en  el  personaje  principal  es

básicamente  para  evitar  animaciones  extra  y  permitir  de  forma  sencilla  la  personalización.

Personajes como Morph siguen la  misma estética ya que se  trata de un aliado  a pesar de no

contar con personalización.

El diseño de enemigos es más libre dependiendo de lo que se quiera buscar con cada uno.

A.6.4. REFERENCIAS ESTÉTICAS

Si bien el diseño comenzó de forma improvisada, un juego con estética similar (Diseño pixel art

con bordes gruesos) puede ser The Binding of Isaac.

113

Figura A.0.10: The Binding of Isaac. Fuente :
[https://bindingofisaac.fandom.com/es/wiki/The_Binding_of_Isaac]

A.7. MÚSICA Y SONIDO

A.7.1. ESTILO DE BANDA SONORA

El  estilo usa  mucho piano, pero dándole una ambientación creepy e  inquietante, esto también

ajustado a la ambientación de cada nivel.

A.7.2. EFECTOS DE SONIDO

Los efectos de sonido son genéricos y no se busca darle mayor profundidad.

A.8. INTERFAZ DE USUARIO

A.8.1. DISEÑO DE MENÚS

Los menús tienen estética simple, con bordes gruesos normalmente grises, y usando colores de

una selección de 3 para las bases:

•  Gris muy oscuro para la mayoría de los fondos.

114

•  Violeta/Lila opaco para cuando se necesite contraste con el fondo gris.

•  Rojo para botones importantes.

A.8.2. HUD

El HUD usa los mismos colores que el resto del menú, generalmente se presenta un hud para el

dinero. En los niveles hay hud de barras para la vida y la experiencia, y un hud para las habilidades

y atributos actuales.

A.9. TECNOLOGÍA Y HERRAMIENTAS

A.9.1. MOTOR DE JUEGO

Inicialmente se usó Godot 4.2, pero Godot 4.3 traía una nueva función que simplifica la transición

entre la música, por lo que se optó por cambiarla.

A.9.2. HERRAMIENTAS DE DESARROLLO

•  Godot 4.3: Motor de desarrollo.

•  Suno: Herramienta IA para crear música.

•  Aseprite: Creación de sprites.

•  Clip Studio Paint: Diseño preliminar de recursos gráficos.

115

