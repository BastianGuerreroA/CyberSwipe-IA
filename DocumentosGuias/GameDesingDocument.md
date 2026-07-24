GAME DESIGN DOCUMENT

(Inserte imagen de referencia de su juego aquí)

TITULO DEL JUEGO

VERSIÓN DEL DOCUMENTO 1.1

Escrito por (nombre de tu equipo):

Numero de contacto:

Dia de publicación:

Numero de versión:

Copyright Company Date

Página 1 de 15

Fecha de hoy

TITULO

GDD

CONTENIDO

OBJETIVOS DEL JUEGO

DESCRIPCIÓN GENERAL DE LA HISTORIA

CONTROLES DEL JUEGO

REQUERIMIENTOS TECNOLÓGICOS

PARTE FRONTAL DEL JUEGO

CUTSCENE DESCRIPTION (SI SE APLICA)

ATTRACT MODE DESCRIPTION (SI SE APLICA)

TÍTULO/PANTALLA DE INICIO

OTRAS PANTALLAS

DIAGRAMA DE FLUJO

PANTALLA DE CARGA

CÁMARA DEL JUEGO

SISTEMA HUD

PERSONAJE DEL JUGADOR

MEDIDAS DEL JUGADOR

HABILIDADES DEL JUGADOR

HERRAMIENTAS DE INVENTARIO DEL JUGADOR

POTENCIADORES/MODIFICADORES DE ESTADO

VIDA

SCORE

RECOMPENSA Y ECONOMÍA

VEHÍCULOS

4

4

4

4

4

4

5

5

5

6

6

6

6

7

7

7

7

8

8

9

9

9

Página 2 de 15

TITULO

GDD

PERSONAJES PRINCIPALES DE LA HISTORIA

ESQUEMA DE PROGRESIÓN DEL JUEGO

CLASIFICACIÓN DE LA JUGABILIDAD

PANTALLA DE RESUMEN DEL MUNDO/SELECCIÓN DE NIVEL/NAVEGACIÓN

MECÁNICAS UNIVERSALES

NIVELES DEL JUEGO

REGLAS GENERALES EN LOS ENEMIGOS

NIVEL - ENEMIGOS ESPECIFICOS

JEFES

NON-PLAYER CHARACTERS

SETS DE OBJETOS COLECCIONABLES

MINIJUEGOS

ESCENAS SECUNDARIAS

MUSICA Y EFECTOS DE SONIDO

PUNTOS Y PREOCUPACIONES

APENDICE

10

10

10

10

10

11

12

12

12

13

13

13

14

14

14

14

Página 3 de 15

TITULO

GDD

OBJETIVOS DEL JUEGO

Aquí puede ir:

El “gran concepto” del juego

El “reverso de la caja” listando cualquier new/novedosa mecánica con sus características.

Funciones de internet, incluye las configuraciones del wifi.

DESCRIPCIÓN GENERAL DE LA HISTORIA

Recuerda que debes ser breve y enmarcarla en el contexto de la jugabilidad. Esto incluye:

Configuración - ¿Cómo inicia el juego el jugador?

Ubicaciones y como se relaciona con la narrativa - ¿Cómo el jugador consigue ir de una ubicación a la
otra?

Final- ¿Cuál es el final de la historia? ¿Qué se espera que el jugador haya hecho o hizo al final del
juego?

CONTROLES DEL JUEGO

Descripción general - Enumere los movimientos específicos que hará el jugador, pero no los detalle
todavía.

Diagrama de control de esquema - Hay aplicaciones para poder lograr estos diagramas.

Muestre una imagen del control - Controladores si el juego está en múltiples plataformas, con el
correspondiente mapeo de botones.

REQUERIMIENTOS TECNOLÓGICOS

Sea breve, ya que mucha de estas características debe incluirse en el documento de diseño
técnico (TDD) del videojuego.

¿Qué herramientas utilizara el juego?

•

¿Cómo será la cámara, físicas, jefes y como va a terminar? ¿La implementación del
programador? ¿El diseñador? ¿Habrá código difícil?

¿Qué herramienta de diseño se utilizará?

•  Herramienta de creación de niveles
•  Sistema de código

Herramientas propuestas para trampas – incluye controles para trampas

•  Trucos de nivel
•  Trucos de invulnerabilidad
•  Truco de cámara
•  Otros trucos (vida completa, armadura completa, dinero completo, etc.)

PARTE FRONTAL DEL JUEGO

Indica que pantalla de créditos ira cuando el juego se muestre por primera vez, incluso:

•  Editor
•  Logo del estudio
•  Licencias
•  Fabricantes de software de terceros
•  Pantalla legal

CUTSCENE DESCRIPTION (SI SE APLICA)

Una escena o escena de evento (a veces cinemática o película dentro del juego) es una secuencia
en un videojuego que no es interactiva y que interrumpe el juego.

Página 4 de 15

TITULO

GDD

No es necesario colocar todo el guion aquí, solo da una breve idea al lector de lo que se trata.

ATTRACT MODE DESCRIPTION (SI SE APLICA)

El modo de atracción, también conocido como modo de visualización o modo de exhibición, es una
demostración pregrabada de un videojuego que se muestra cuando no se está jugando.
Originalmente integrado en los juegos de arcade, el objetivo principal del modo de atracción es
atraer a los transeúntes para que jueguen.

TÍTULO/PANTALLA DE INICIO

¿Cuál es la primera impresión del juego actual? Se incluye:

Imagen del título/pantalla de inicio

Detalle de lo que se presentará al jugador

•  Título del juego y como apareceré en la pantalla.
•  Cualquier animación/gráficos implementados.

Una lista de las opciones disponibles para el jugador

Como el jugador interactuará con las opciones (Cursor, pad, etc.)

Guardar/cargar juego – Describir como el juego se guardará y cargará

Nombrar/designar un archivo guardado - Mediante teclado u otro sistema de nombrado.

Lista de detalles del archivo guardado que se muestra al jugador

•  Nombre
•  Fecha
•  Ubicación del nivel o nombre/número del capitulo
•  Tiempo de juego transcurrido
•  Una imagen del aspecto del archivo de la partida guardada (si es necesario)

Detallar cualquier cruce o características de guardado

Opciones del jugador - Incluye imagen, sonido y música, detalles de interfaz del reproductor. Detalla
los enlaces de conexión a las opciones

•  Ajustes de video
•  Ajustes de audio
•  Ajustes de música
•  Ajuste de subtítulos
•  Herramienta de contraste
•  Ajuste de control alternativo (joystick inverso, activación/desactivación de

retroalimentación, etc.)

OTRAS PANTALLAS

Podrían ser contenidos desbloqueables a la que se accede desde la pantalla del título. Asegúrate
de incluir la imagen, sonido y la música, los detalles de la interfaz del jugador. Entre las posibles
pantallas se incluyen:

Créditos

•  Foto del equipo
•

Imágenes del estudio

Material extra - Incluya imágenes de las pantallas, ¿Cómo interactuará el jugador con la interfaz, como
lo activará? (desbloqueable, comprable, easter eggs, etc.)

•  Trajes o armas alternativos
•  Trucos
•  Trucos funcionales (invulnerabilidad, salud completa, etc.)

Página 5 de 15

TITULO

GDD

•  Trucos requeridos por el licenciador (con fines de marketing)
•  Otros trucos (modo cabeza grande, cambio de color, etc.)
•  Galerías de arte/sonido/animación
•  Reproductor de video para escenas, películas, etc.
•  Trailers de otros juegos o productos.

Características especiales

•  Comentarios
•  Entrevistas con el equipo
•  Material eliminado
•  Documentales
•  Gag reels

DIAGRAMA DE FLUJO

Muestra cómo se conectan entre si todas las pantallas, desde el título/pantalla de inicio hasta el
game over.

PANTALLA DE CARGA

¿Qué ve el jugador cuando el juego está cargando? Incluya:

Una imagen de pausa del juego (indique si se utiliza varias imágenes)

Datos presentados al jugador del juego (pistas, trivias, preguntas, minijuegos)

CÁMARA DEL JUEGO

Tipos de cámara específicos

Imagen de la cámara desde el punto de vista de cualquiera de estos estaría bien:

•  Primera persona
•  Tercera persona
•  Tres cuartos
•
•  Forced scroll
•  Spline
•  Cámara bloqueada

2.5 D

Descripción del sistema lógico de la cámara

•  Juego – Situaciones específicas donde se requieren un tipo exacto de cámara
•  Guía de resolución de problemas de la cámara – Ejemplos de lo que hará la cámara cuando

se encuentre con problemas.

Lógica para la cámara de los trucos/capturas de pantalla.

•  Como el desarrollador/publicador puede acceder y manejar esta cámara.

SISTEMA HUD

Información presentada en la pantalla del jugador. Incluya imágenes de todo a continuación:

•  Salud/estado
•  Vidas
•  Dinero/puntuación/rango
•  Potencia/combustible
•  Munición
•  Habilidades/destreza
•  Temporizador
•  Mapa o sistema de navegación
•  Opciones: enlace a pantallas externas

Página 6 de 15

TITULO

GDD

•  Plings/información sensible
•  Sistema de puntería/retícula/cursor
•  Velocímetro

Si el juego no tiene HUD, describe cómo se va a transmitir la información anterior al jugador.

PERSONAJE DEL JUGADOR

Nombre del jugador.

Imagen/dibujo conceptual de tu personaje.

Breve descripción que explique la motivación del jugador y su relación con otros personajes
principales/otros jugadores.

MEDIDAS DEL JUGADOR

Relaciones de tamaño del personaje del jugador con otros elementos/personajes del mundo.

Movimiento (caminar, correr, escabullirse, agacharse, rodas, arrastrarse)

•  Mostrar métricas

Navegación (saltar, nadar, volar)

•  Muestra las métricas y condiciones para estos movimientos.

Elevación/colgaduras

•  Mostrar métricas.

Movimientos sensibles (empujar/tirar, accionar botones, balancearse, etc.)

•  Muestra ejemplos y métricas.
•  Muestre ejemplos y métricas como también las condiciones para esto.

Reacciones/daños/muertes

•  Mostrar ejemplos o métricas.

Estado de reposo

HABILIDADES DEL JUGADOR

Descripción de las habilidades básicas

Lista de mejora de habilidades

•  Descripción de las habilidades
•  Modificadores de habilidades
•  Métricas (si procede)

HERRAMIENTAS DE INVENTARIO DEL JUGADOR

Equipamiento, hechizos, potenciadores, y lo demás

Lista de herramientas

Imagen de las herramientas
•
¿Qué hace cada herramienta?
•
•  Controles para usar la herramienta

Pantalla de inventario

•
•
•

Imagen del inventario
¿Cómo el jugador accede a este inventario?
¿Cómo el jugador selecciona una herramienta de este inventario?

Página 7 de 15

TITULO

GDD

Combate – cuerpo a cuerpo.

Movimientos de combate - Incluye métricas y controles.

Reacciones de combate - Incluye métricas y controles.

•  Bloqueo
•  Esquivar
•  Parar
•  Agarrar

Tipos de efecto - Daño, knockback, stun, veneno, etc.

Progresión de combate – Como el jugador mejora sus movimientos.

Descripción de movimientos combo

•  Controles de movimiento de combo.
•  Progresión del combo.

Indicador de combate

•  Valores modificados en base al indicador de combate mediante descripciones.

Descripción de movimientos combo

•  Control de los movimientos combo.
•  Progresión de los combos.

Armas

Progresión de armas

•  Árbol tecnológico
•
•  Daño y efecto

Inspiración/concepto sobre las armas

▪  Sistema de mira
▪  Sistema de bloqueo

•  Munición necesaria
•  Alcance
•  Atributos especiales (rompible, degradable)
•  Controles

▪  Como el jugador usa estas armas
▪  Como el jugador cambia estas armas

POTENCIADORES/MODIFICADORES DE ESTADO

Lista

•  Descripción incluida la imagen
•  Efecto
•  Duración
•  Efectos en controles (si es válido)

VIDA

Vida (en general)

•  Visualización en HUD
•  Como reponer la salud
•  Potenciadores e ítems de salud
•  Alertas al jugador cuando la vida esta baja

Página 8 de 15

TITULO

GDD

Estados alternativos – (stuneado, envenenado, convertido en bebe, etc.)

•  Controles
•  Mostrar ejemplos y métricas

Vidas (si es aplicable)

•
•
•

¿Cómo se ganan las vidas?
¿Cómo se pierden las vidas?
¿Qué ocurre cuando se acaban todas las vidas?

Muerte

•  Condiciones de muerte instantánea: combate, fuego, ahogamiento, etc.
•  Condiciones de game over

▪  Penalización por morir
▪  Pantalla de fin de partida (muestra la imagen de la pantalla de game over)

Checkpoints

•  Sistema de continuar juego

SCORE

Puntos

Bonificaciones

•

¿Que da una bonificación?

Tabla de clasificación

Imagen

•
•  Elementos que contribuyen a la puntuación

Logros

•  Lista de logros
•

Icono

RECOMPENSA Y ECONOMÍA

Sistema monetario

•

Interfaz de compra

▪  Descripción
▪  Navegación del jugador

¿Qué se puede comprar?

•
•  Costo

VEHÍCULOS

Como el jugador entra y sale del vehículo

¿Cómo interactúa el vehículo con el mundo, los enemigos, objetos, etc.?

Descripción

•

Imagen del vehículo

Controles

Métricas (tamaño, velocidad, etc.)

Página 9 de 15

TITULO

GDD

Atributos (armadura, armas, etc.)

•  Estadísticas
•  Efectos especiales

PERSONAJES PRINCIPALES DE LA HISTORIA

Cualquiera que se mencione en el esquema de la historia anterior, preferiblemente los que tienen
impacto en la historia o el juego.

Esto incluye aliados/ayudantes, amantes, rivales/villanos

•
•

¿Cuál es su relación con el personaje del jugador?
¿Dónde aparecen?

ESQUEMA DE PROGRESIÓN DEL JUEGO

Resumen de todos los niveles del juego – inserta la tabla de tiempos del juego. Recuerda esto:

•

•

Incluye los tiempos de la historia para mostrar cómo se entrelazan la jugabilidad y la
historia.
Indicar si el ritmo de la historia es una escena de corte o en el juego.

Indica progresión/recompensas para el jugador

•  Muestra donde las nuevas habilidades, poderes, armas, y coleccionables son ganadas en

relación a la historia.

CLASIFICACIÓN DE LA JUGABILIDAD

Descripción de los tipos de juego (sigilo, arena de combate, conducción, vuelo, etc.)

PANTALLA DE RESUMEN DEL MUNDO/SELECCIÓN DE NIVEL/NAVEGACIÓN

Imagen general del mundo (si procede).

Lista de niveles del juego disponibles en el mundo.

Descripción de cómo será presentada la información al jugador.

Detalles de cómo el jugador navegara en esta pantalla (cursor, personaje, etc.)

Animaciones (personaje y/o elementos) necesarios.

Sonido y música requerido para esta pantalla de selección de nivel.

MECÁNICAS UNIVERSALES

Lista de mecánicas que se encontraran por el juego. Siempre incluye referencias de cada
mecánica.

Mecánicas de la plataforma

•  Descripción
•  Métricas relacionadas con el jugador

Portales

•  Puertas

▪  Accionadas por manivela/interruptor
▪  Accionadas por llave
▪  Rompible
▪  Pestillo (movimiento sensible)

•  Teleportación

▪  Descripción e imágenes

Página 10 de 15

TITULO

GDD

▪  Efectos
▪  Ayuda de navegación

Checkpoints

Objetos rompibles (cajas, muebles, hierba, etc.)

•  Como se rompe el objeto
•  Que ítems te quitan un porcentaje de rendimiento
•  Otros efectos (explosiones, temporizador, interruptor, etc.)

Objetos no rompibles

•  Descripción e imagen de referencia
•  Que ítems te quitan un porcentaje de rendimiento
•  Otros efectos (explosiones, temporizador, interruptor, etc.)

Objetos Puzzle (bloques empujables, llaves, etc.)

•  Descripción e imagen de referencia.
•  Como el jugador interactúa con ellos.

Interruptores

•  Descripción e imagen de referencia.
•  Como el jugador interactúa con ellos.

NIVELES DEL JUEGO

Enumera cada uno de los niveles mencionados en el resumen del mundo.

Nombre/título de los niveles

•  Breve descripción del nivel
•  Objetivo del jugador (entrenamiento, ir de A - B, encontrar una llave, etc.)
•  Recompensa del nivel (subir de nivel, espada mágica, progresión, etc.)
•  Principales modos de juegos en este nivel (sigilo, plataforma, vehículo, etc.)

▪  Sub-juegos encontrados en este nivel, con una descripción de la jugabilidad y un

esquema de control

•  Enemigos encontrados en este nivel
•  Guías de estilo visual para el nivel

Incluye ilustraciones de inspiración y arte conceptual.

▪
▪  Hora del día.
▪  Guía de color

•  Música

▪  Proporcionar ejemplos/archivos de sonido.

HUB

•  Descripción del HUB.
•  Lista de locaciones encontrados en el HUB.
•  Requerimientos para viajar/desbloquear.
•  Cambios de estado.
•  Salvar/cargar opciones (si es aplicable)

Entrenamiento

•  Objetivos del nivel de entrenamiento

▪  Lista de actividades del nivel de entrenamiento

Página 11 de 15

TITULO

GDD

Mecánicas específicas de niveles

Información sobre el tiempo

•  Peligros (spikes, chorro de llamas, campos de laser, etc.)
•  Descripción e imagen de referencia
•
•  Daño/efectos
•
•
•  Efectos o elementos necesarios

¿Cómo afecta al jugador? (movimiento, vida, etc.)
¿Cómo el jugador puede esquivarlos/pasarlos?

Mecánica contextual especifica de nivel

Información sobre el tiempo

•  Descripción e imagen de referencia
•
•  Daño/efectos
•
•
•  Efectos o elementos necesarios

¿Cómo afecta al jugador) (movimiento, vida, etc.)
¿Cómo el jugador puede esquivarlos/pasarlos?

REGLAS GENERALES EN LOS ENEMIGOS

Tipos de comportamiento (patrullero, cazador, volador, etc.)

Reglas de AI y métricas de detección.

Parámetros de spawn

Parámetros de derrota

Reglas de recompensa

NIVEL - ENEMIGOS ESPECIFICOS

Referencia del enemigo

Descripción del enemigo – incluye tipo de enemigo.

Niveles en los que se encuentra.

Patrones de movimiento – mostrar métricas.

Ataques

•  Valores de daño
•  Efectos de daño (knockback, stun, etc.)

Reacciones/daño/muerte

Estado de reposo

Efectos especiales

Recompensa por derrota

JEFES

Descripción e imágenes de referencia del jefe

•  Se incluye escala

Indicar los puntos débiles/ataques.

Como interactúa con el jugador (dañara al jugador si colisiona, solo dañara al jugador en un estado en
específico, etc.)

Patrones de movimiento

•  Muestra métrica en relación al jugador.

Página 12 de 15

TITULO

GDD

Patrones de ataque

•  Advertencias
•  Ataques específicos

▪  Daños causados
▪  Efectos especiales

•  Reacciones/daño/muerte
•  Estado de reposo

Descripción de la experiencia del jugador

•  Descripción de la intro/escena de corte.
•
•  Progresión de acción

Incluye número de rondas

Descripción e imagen del entorno

•  Peligros y mecanismos utilizados
•  Potenciadores y coleccionables
•  Otros enemigos usados en la pelea del jefe.

¿Cómo se derrota al jefe?

Recompensas

NON-PLAYER CHARACTERS

Tipo de estado (información, entrega de misiones, escolta/defensa, etc.)

Lista de personajes

•  Nombre, sexo, edad
•  Material de fondo
•  Tipo de NPC
•  Niveles donde los encontraremos

Interacción con los NPC

•  Dialogo
•  Colisión

Recompensas de NPC

SETS DE OBJETOS COLECCIONABLES

Lista de ítems

Imágenes de referencia
•
•  Niveles donde se encontrarán
•  Que objetos o conjuntos de objetos desbloquea (si procede

MINIJUEGOS

Tipos de minijuegos

Como se accede a estos minijuegos

Controles

Elementos necesarios/reutilizados

Niveles encontrados

Página 13 de 15

TITULO

GDD

ESCENAS SECUNDARIAS

Lista de escenas secundarias

Breve resumen de cada escena

Niveles donde se encontrará cada escena

MUSICA Y EFECTOS DE SONIDO

Lista de música

•  Niveles donde la música será necesitada – no olvidar el título, pausa, opciones y créditos

finales

•  Tono/sentimiento de la música

PUNTOS Y PREOCUPACIONES

APENDICE

Lista de animaciones de los personajes

Lista de animaciones de los enemigos

Lista de los efectos de sonido

Lista de la música

•  Localización de niveles

Guiones de escenas

•  Guiones de storyboards

VO scripts

•  Jugador
•  Enemigos
•  Jefes
•  NPC

Texto del juego

•  Pantalla de advertencia
•  Texto de tutoriales
•  Diálogos y subtítulos de los personajes

Página 14 de 15

TITULO

GDD

Página 15 de 15

