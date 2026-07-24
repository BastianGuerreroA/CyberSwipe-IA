# CAPÍTULO 3. DISEÑO DEL VIDEOJUEGO (GDD)

En este capítulo se detalla el documento de diseño del videojuego (GDD), el cual explica de manera exhaustiva la visión general, mecánicas, interfaces y aspectos técnicos para el desarrollo de la solución propuesta. Este documento sirve como plano de diseño y referencia estructural para el videojuego serio **CyberSwipe-v2**, facilitando su construcción lógica sobre el motor de desarrollo Godot Engine y detallando su integración con el framework de gamificación bGames (LifeSync-Games).

---

## 3.1 OBJETIVOS DEL JUEGO

El videojuego serio **CyberSwipe-v2** tiene como objetivo primordial mejorar la concienciación y alfabetización en ciberseguridad en colaboradores y empleados de pequeñas y medianas empresas (PYMEs) en Chile. Dado que el factor humano representa uno de los eslabones más vulnerables y explotados en los incidentes de seguridad de la información (mediante técnicas de ingeniería social como phishing o manipulación física), la solución busca capacitar a usuarios no técnicos de una manera lúdica e interactiva, facilitando la retención de buenas prácticas y la toma de decisiones informadas.

Para lograr este fin, el juego adopta la forma de una aplicación móvil en formato vertical orientada a la toma de decisiones rápidas de la categoría **Puzzle** con interacción de arrastre horizontal (*Swipe*). A través de una baraja de cartas de dilemas realistas de oficina, el jugador debe decidir la mejor línea de acción en situaciones cotidianas de riesgo digital. Las elecciones correctas aumentan el desempeño y la puntuación de la ronda, mientras que las incorrectas conllevan explicaciones pedagógicas inmediatas para consolidar el conocimiento y penalizaciones en los recursos críticos de la empresa.

Adicionalmente, el videojuego se conecta de forma opcional con el framework **bGames (LifeSync-Games)** desarrollado en el laboratorio InTeractiOn de la Universidad de Santiago de Chile. Esta integración permite personalizar la experiencia de juego recopilando datos del entorno real del usuario mediante sensores virtuales (actividades de estudio, resiliencia emocional, trabajo colaborativo o hábitos saludables de movimiento físico), transformando dichos datos reales en puntos multidimensionales. Los jugadores pueden canjear estos puntos en el videojuego por ventajas previas a las partidas o por reanimaciones en caso de derrota, promoviendo hábitos saludables y de capacitación continua en su vida diaria.

---

## 3.2 MECÁNICAS DEL JUEGO

En este apartado se definen detalladamente las mecánicas y funcionalidades del videojuego, sirviendo como guía conceptual y técnica para su implementación en el motor de desarrollo y su interoperabilidad con el backend de red.

### 3.2.1 Reglas generales

El videojuego se basa en una mecánica de dilemas y toma de decisiones a través del deslizamiento lateral de cartas. Al comenzar una partida, el jugador selecciona una **Cápsula de Aprendizaje** (nivel o módulo temático). Cada cápsula cuenta con una baraja de cartas (dilemas) que se extraen de forma aleatoria para conformar la partida. 

En cada turno, la pantalla muestra una carta con un dilema de ciberseguridad contextualizado en el entorno laboral de una PYME. El jugador debe arrastrar la carta de forma horizontal:
* **Hacia la izquierda**: Selecciona la opción detallada en la etiqueta izquierda.
* **Hacia la derecha**: Selecciona la opción detallada en la etiqueta derecha.

Cada decisión impacta de forma positiva o negativa en los recursos del juego. Si el jugador desliza hacia la opción correcta (indicada en la base de datos de contenidos), suma un punto a su puntuación de la ronda actual. Si el jugador comete un error y desliza hacia la opción incorrecta, el juego suspende el temporizador, congela el gameplay y despliega una ventana de retroalimentación pedagógica explicativa que instruye al usuario sobre los riesgos de esa decisión en el mundo real antes de permitirle continuar con la siguiente carta.

La partida cuenta con dos posibles desenlaces:
* **Victoria**: El jugador sobrevive con sus recursos por encima de cero a lo largo de toda la baraja de cartas de la cápsula. Al finalizar las cartas, la partida concluye, registrando la puntuación total, comparándolo con el récord personal local y desbloqueando secuencialmente la siguiente cápsula en el progreso.
* **Derrota (Game Over)**: Ocurre en el instante en que cualquiera de las métricas de recursos cae a cero o menos. El juego se congela, se presenta un mensaje formativo asociado a la causa del incidente de seguridad y se ofrecen las opciones de reiniciar la partida, volver al selector o —si está conectado a bGames— canjear una reanimación para restaurar el recurso fallido y continuar la partida.

### 3.2.2 Sistema de contenidos

El videojuego implementa un sistema dinámico de contenidos desacoplados del código fuente de Godot. La baraja de cartas, títulos, textos BBCode de estudio previo, explicaciones de error e impactos en los recursos se definen externamente en un archivo estructurado en formato JSON (`capsulas.json`).

Al iniciar, el motor analiza el archivo y puebla dinámicamente el selector de niveles y las barajas correspondientes a cada cápsula. Este diseño permite una alta escalabilidad pedagógica, haciendo posible que docentes, administradores o encargados de seguridad informática actualicen los dilemas de ciberseguridad o añadan nuevos módulos temáticos y normativos sin necesidad de modificar el código fuente del videojuego o compilar nuevos instaladores.

### 3.2.3 Sistema de progresión

El videojuego mantiene la progresión y estadísticas del jugador a través de dos mecanismos complementarios:

1. **Perfil de Usuario Local**: Se almacena localmente en la memoria del dispositivo en la ruta `user://progreso_usuario.tres` mediante un recurso serializado (`Resource`) de tipo `ProgresoUsuario`. Este archivo almacena de forma persistente:
   - El nombre o identificador del usuario.
   - El puntaje total acumulado de sus mejores marcas de juego (`puntos_totales`).
   - El nivel general máximo de cápsula desbloqueado (`progreso_general`).
   - Un diccionario que asocia el identificador de cada cápsula con su respectivo récord de puntuación máxima (`puntajes_maximos`).
2. **Progresión de Cápsulas (Niveles)**: El videojuego se compone de un conjunto secuencial de cápsulas educativas. Al iniciar, el jugador solo tiene disponible la Cápsula 1. Las cápsulas posteriores se presentan bloqueadas y atenuadas. Para desbloquear la cápsula $N+1$, el jugador debe completar con éxito (victoria) la cápsula $N$ correspondiente a su nivel máximo actual (`progreso_general`), incrementando de forma persistentemente dicho valor en su perfil.
3. **Respaldo e Integración de Red**: Cuando el jugador inicia sesión con su cuenta académica, el videojuego sincroniza su nombre de usuario local con la información oficial del servidor obtenida de la API `/whoami` y habilita la consulta del historial centralizado del estudiante en la base de datos de bGames.

### 3.2.4 Interacción del jugador

Durante la sesión, el jugador cuenta con las siguientes interacciones lúdicas y operacionales:

* **Estudiar Cápsula**: Antes de iniciar la simulación, el jugador puede presionar el botón "Estudiar" en el selector de niveles. Esto despliega una interfaz de lectura con textos formateados en BBCode que explican conceptos teóricos y buenas prácticas para preparar al usuario antes de la evaluación práctica.
* **Canjear Ventajas pre-partida**: Si el usuario está autenticado en la plataforma de bGames, al seleccionar "Practicar", se despliega la interfaz de la tienda virtual (`StoreLSG`). Aquí, el jugador interactúa con botones que le permiten gastar puntos de su perfil real en ventajas de supervivencia para la ronda (Consultoría Preventiva, Análisis de Impacto, Subsidio de Seguridad o Ciberseguro Activo), simulando el gasto y recalculando balances virtuales antes de confirmar el juego.
* **Arrastrar y Previsualizar**: Durante el juego, el usuario mantiene presionada la carta y la arrastra hacia los lados. El movimiento continuo actualiza indicadores visuales en el HUD (flechas arriba/abajo o valores exactos) que anticipan el impacto de la decisión sobre los recursos corporativos, permitiendo corregir la trayectoria si el impacto es perjudicial.
* **Resolver Dilema (Swipe)**: Al soltar la carta sobrepasando el umbral físico en la pantalla, la carta se desplaza fuera del área de juego de forma automática, validando la selección y aplicando los cambios sobre el estado de la PYME.
* **Pausar Partida**: El jugador puede presionar el botón de pausa en la esquina superior derecha en cualquier momento de la ronda. Esto congela los elementos lúdicos (cartas, animaciones y tiempos) pero mantiene activos los nodos de comunicaciones HTTP y registros del logger de fondo.
* **Canjear Reanimación (Salvavidas)**: Ante una derrota por agotamiento de recursos, el usuario puede interactuar con el botón "Reanudar con Salvavidas" en el menú de Game Over, consumiendo puntos afectivos reales para restablecer el juego.

### 3.2.5 Economía del juego

La economía del videojuego es mixta y está compuesta por dos subsistemas monetarios bien diferenciados:

#### A. Recursos Internos de Partida (Métricas de la PYME)
Son cuatro indicadores numéricos que representan la salud y seguridad de la organización simulada. Tienen un rango estricto de **[0, 100]** y comienzan la partida con un valor base de **50 puntos** (o **60 puntos** si se adquiere la ventaja de Consultoría Preventiva):
1. **Presupuesto ($P$)**: Dinero de la empresa. Las buenas medidas preventivas consumen presupuesto; los ataques e incidentes graves por negligencia provocan pérdidas financieras drásticas en este recurso.
2. **Confidencialidad ($C$)**: Representa la protección de los datos contra intrusos o fugas de información.
3. **Integridad ($I$)**: Mide la precisión, consistencia y estado inalterado de los datos financieros y de clientes de la PYME.
4. **Disponibilidad ($D$)**: Mide la operatividad de los servidores y el acceso continuo de los empleados a sus sistemas de trabajo.

#### B. Saldos Externos de bGames (LifeSync-Games)
Son puntos reales acumulados por el usuario a través de actividades externas registradas por sensores lógicos o físicos en la plataforma de la USACH. Se dividen en cuatro dimensiones específicas que actúan como divisas en el videojuego:
* **Puntos de Dimensión Mental ($M$)**: Canjeados en la tienda pre-partida por la ventaja de *Consultoría Preventiva* (Costo: 25 puntos).
* **Puntos de Dimensión Afectiva ($A$)**: Canjeados por la ventaja de *Análisis de Impacto* (Costo: 40 puntos) o por la reanimación *Salvavidas* en la pantalla de Game Over (Costo: 50 puntos).
* **Puntos de Dimensión Social ($S$)**: Canjeados en la tienda por la ventaja de *Subsidio de Seguridad* (Costo: 30 puntos).
* **Puntos de Dimensión Física ($F$)**: Canjeados en la tienda por la ventaja de *Ciberseguro Activo* (Costo: 35 puntos).

### 3.2.6 Sistema de puntaje

El sistema de puntaje mide de forma cuantitativa el rendimiento del jugador durante la simulación:
* Cada respuesta correcta tomada por el usuario durante la ronda incrementa en **1 punto** el marcador de puntuación de la ronda actual (`puntaje_ronda_actual`). Las respuestas incorrectas no suman puntos, pero no restan del marcador acumulado de score.
* El puntaje máximo posible de alcanzar en una cápsula es igual a la cantidad total de cartas que conforman su baraja.
* Al concluir con éxito la cápsula (victoria), el juego compara el marcador `puntaje_ronda_actual` con el récord previo del jugador almacenado en el diccionario local de estadísticas de la cápsula activa. Si el puntaje actual es estrictamente mayor, se sobreescribe y se guarda como el nuevo récord.
* El puntaje total general acumulado del perfil del jugador en el selector (`puntos_totales`) se calcula de forma automática sumando los récords de puntuación de todas las cápsulas del juego:

$$puntos\_totales = \sum_{k=1}^{n} record(k)$$

Donde $record(k)$ es la puntuación máxima obtenida en la cápsula $k$, y $n$ es el número total de cápsulas disponibles.

---

## 3.3 DISEÑO DE MUNDO

El mundo de **CyberSwipe-v2** se desarrolla dentro de una simulación de oficina corporativa de una pequeña o mediana empresa (PYME) en Chile, ambientada en la época actual. Este entorno virtual representa el escenario social y laboral del trabajador, buscando que el colaborador asocie los dilemas de seguridad con su espacio físico de trabajo diario.

El juego se compone de **5 Cápsulas de Aprendizaje** que dividen el contenido de ciberseguridad en módulos de entrenamiento temáticos. Cada cápsula simula un módulo de entrenamiento o una fase operativa en el día a día de la empresa:
* **Cápsula 1 (Física y Accesos)**: Representa el control de acceso en la oficina y los dispositivos personales del personal.
* **Cápsula 2 (Ingeniería Social Digital)**: Simula la recepción de correos y mensajes en los canales de comunicación de la empresa.
* **Cápsula 3 (Resiliencia e Información)**: Modela el almacenamiento, control de copias y resguardo ante catástrofes lógicas.
* **Cápsula 4 (Comunicaciones)**: Representa la conectividad y redes informáticas de la oficina.
* **Cápsula 5 (Ingeniería Social Presencial)**: Simula situaciones físicas con extraños o elementos desconocidos que ingresan al edificio de la PYME.

El diseño visual del mundo es abstracto y ciberpunk, con un fondo oscuro animado mediante un shader que simula un entorno digital flotante, reforzando la inmersión del usuario en el espacio lúdico y tecnológico de la seguridad informática.

---

## 3.4 INTERFAZ DE USUARIO (UI)

La interfaz de usuario del videojuego está estructurada de forma clara para guiar la interacción del jugador a través de dos grandes entornos visuales: las interfaces de menús y la interfaz de gameplay de la partida.

### 3.4.1 Interfaces de Menús

* **Menú Principal**: Es el primer vistazo del usuario al iniciar el videojuego. Permite navegar hacia el selector de niveles mediante el botón "Jugar", salir de la aplicación mediante "Salir" o interactuar con el botón en la esquina superior izquierda que despliega el panel de autenticación de bGames.
* **Panel de Login LSG**: Interfaz emergente que permite al usuario iniciar sesión con sus credenciales universitarias (correo institucional y contraseña) para cargar su sesión de red. Si ya existe una sesión iniciada, muestra un mensaje de bienvenida y el botón de "Cerrar Sesión".
* **Selector de Cápsulas**: Es el centro de navegación de la progresión del juego. Muestra en la parte superior el nombre del usuario, su balance de puntos totales y una barra de progreso que indica cuántas cápsulas han sido completadas con éxito. En la parte central, despliega una lista de acordeón para las 5 cápsulas. Al presionar el botón flecha (chevron) de una cápsula disponible, esta rota con una animación suavizada de *tween* y despliega la mini descripción conceptual del módulo junto a dos botones: "Estudiar" y "Practicar".
* **Escena de Estudio**: Pantalla con formato de pergamino que muestra el contenido de lectura de la cápsula seleccionada en un texto formateado enriquecido con etiquetas BBCode, incluyendo secciones de conceptos clave y recomendaciones pedagógicas. Cuenta con un botón superior para regresar al selector.
* **Tienda de Ventajas (StoreLSG)**: Interfaz que se despliega de forma previa a la partida si hay sesión iniciada en bGames. Muestra una cabecera con los saldos reales y virtuales del usuario para las 4 dimensiones (Mental, Afectiva, Social, Física). Despliega en filas las 4 ventajas disponibles con sus descripciones y botones para "Adquirir" o "Desmarcar", recalculando en tiempo real los saldos virtuales de forma visual. Cuenta con un botón de "Cancelar" para regresar al selector y un botón "Confirmar y Jugar" que realiza los cobros reales e inicia la escena principal de juego.

### 3.4.2 Interfaz de Partida (Gameplay)

* **HUD Superior**: Despliega permanentemente las cuatro barras e iconos que representan el nivel actual de los recursos corporativos (Presupuesto, Confidencialidad, Integridad y Disponibilidad), cambiando su porcentaje visual de forma interactiva. En el centro superior muestra el marcador de score de la ronda actual, a la derecha el botón de pausa y a la izquierda el acceso al perfil del estudiante.
* **Área Central de Juego**: Zona destinada para el spawn dinámico de las cartas de dilema. Cada carta muestra una ilustración temática central representativa y, al ser arrastrada hacia los lados, dibuja una superposición de color translúcido con el texto de la decisión respectiva (izquierdo o derecho) y su valor predictivo en caso de contar con la ventaja adecuada.
* **Footer de Información**: Campo de texto animado que muestra la descripción textual del dilema en curso y los detalles de las opciones disponibles al jugador.
* **Menú de retroalimentación de error**: Emergente que pausa y bloquea el juego cuando el jugador toma una decisión incorrecta. Muestra un título de advertencia y el texto explicativo de por qué esa acción fue perjudicial para las finanzas y seguridad de la PYME, obligando al usuario a leer y presionar el botón "Continuar" para reactivar el juego.
* **Menú de Pausa**: Interfaz de confirmación que detiene el juego lúdico, permitiendo reanudar o salir al selector.
* **Pantalla de Game Over**: Emergente visualizado al caer a cero cualquier recurso. Muestra la puntuación alcanzada, el récord de la cápsula, la causa del fallo identificada (ej: "Presupuesto agotado") y un consejo de ciberseguridad centralizado según la métrica fallida. Si el usuario está conectado a la red, despliega el botón "Reanudar con Salvavidas (50 ptos Afectivo)", además de los botones estándar para reintentar o salir.
* **Pantalla de Victoria**: Se despliega al terminar con éxito la baraja de cartas. Muestra la copa de logro de nivel completado, puntuación obtenida, récord y un resumen pedagógico específico de la cápsula.

---

## 3.5 CONTROL Y ACCESIBILIDAD

El videojuego está diseñado principalmente para dispositivos móviles con sistema operativo Android, por lo que el esquema de interacción se basa en controles táctiles directos:
* El usuario interactúa deslizando un solo dedo de forma horizontal para arrastrar y soltar las cartas en el área de juego, lo que facilita el juego casual con una sola mano.
* Godot Engine emula de forma nativa los gestos táctiles de arrastre a partir del botón izquierdo del mouse en computadores (`pointing/emulate_touch_from_mouse=true`), garantizando la total compatibilidad e interoperabilidad de la interfaz de juego si es compilada para Windows o Web sin necesidad de alterar los scripts de control.
* Toda la navegación por menús se realiza mediante toques directos a botones, con un tamaño mínimo de colisión y área de clic adaptada para evitar toques erróneos en pantallas móviles.

---

## 3.6 ESTILO ARTÍSTICO Y SONIDO

### 3.6.1 Estilo Visual
El estilo artístico adopta una estética moderna de ciencia ficción ciberpunk, combinando paletas de colores oscuros para los fondos y menús con elementos neón de alto contraste y esquinas redondeadas en la UI (*glassmorphism*). Cada una de las métricas de recursos en el HUD cuenta con una identidad cromática única y de rápido reconocimiento:
* **Presupuesto**: Color Naranja.
* **Confidencialidad**: Color Azul.
* **Integridad**: Color Verde.
* **Disponibilidad**: Color Magenta.

### 3.6.2 Audio y Sonidos
El videojuego cuenta con un apartado de audio interactivo para mejorar la inmersión y la retroalimentación lúdica:
* **Música de Fondo**: Un loop musical de estilo electrónico o de sintetizadores ciberpunk suave que se reproduce de forma constante en la escena principal de juego para acompañar la partida sin distraer del contenido teórico de estudio.
* **Efectos de Sonido (SFX)**:
  - *Sonido de Escritura (Typing Sound)*: Se reproduce secuencialmente al mostrar el texto de los dilemas en el footer de la escena de juego. Cuenta con una validación por código para evitar reproducirse ante espacios en blanco, creando una sensación táctil y orgánica al leer.
  - *Sonido de Swipe*: Un efecto rápido de viento que se reproduce al lanzar la carta fuera de la pantalla.
  - *Sonido de Compra*: Un efecto acústico metálico reproducido al canjear ventajas en la tienda StoreLSG o al adquirir el Salvavidas.

---

## 3.7 MODOS DE JUEGO

El videojuego cuenta con dos modos principales de ejecución que dependen de la conectividad de red y la cuenta del estudiante:

* **Modo Offline (Invitado)**: 
  - Modalidad por defecto si el usuario no cuenta con conexión a internet o no inicia sesión en bGames.
  - El progreso general y las marcas de récord se persisten localmente en el dispositivo.
  - No hay acceso a la tienda pre-partida de ventajas (`StoreLSG`) ni a la reanimación de *Salvavidas* en el Game Over. El jugador debe enfrentar la dificultad base del juego con 50 puntos de inicio en cada métrica y un único intento por dilema.
* **Modo Online (LSG Integrado)**:
  - Modalidad académica y de gamificación completa para estudiantes autenticados.
  - Permite cargar en tiempo real los saldos de puntos multidimensionales del backend.
  - Habilita la compra de ventajas en la tienda pre-partida y el Salvavidas para reanimarse consumiendo puntos de la dimensión afectiva obtenidos en su vida real.
  - Registra y envía el reporte de telemetría de la sesión de juego de manera automática al servidor de la USACH para evaluación y seguimiento académico.

---

## 3.8 ADMINISTRACIÓN DE PARTIDAS Y GUARDADO

### 3.8.1 Estructura del Guardado Local
El guardado local del progreso del juego se realiza mediante la serialización del recurso nativo de Godot `ProgresoUsuario.new()`, que hereda de la clase `Resource`. Este archivo se escribe físicamente en el almacenamiento persistente del dispositivo en la ruta de usuario protegida `user://progreso_usuario.tres`. La estructura se compone de las variables:
* `nombre_usuario` (String).
* `puntos_totales` (int).
* `progreso_general` (int).
* `puntajes_maximos` (Dictionary).

La carga de este archivo se efectúa al iniciar la aplicación mediante el método `cargar_progreso_jugador()` en el Singleton `CapsulaManager`. Si el archivo no existe (por ejemplo, en la primera ejecución de la aplicación), el sistema inicializa una estructura limpia y guarda el progreso base.

### 3.8.2 Gestión de Sesión y HTTP (Autoloads de Godot)
La administración de peticiones de red y la conexión de la sesión académica se delegan de forma modular a Singletons configurados como Autoloads en Godot. Esta arquitectura desacopla la comunicación y evita duplicar llamadas HTTP en las escenas:
* **`LsgAuth`**: Singleton encargado directo del flujo de login de usuario y validación de perfiles (`whoami`), almacenando el token JWT de acceso.
* **`LsgCore`**: Singleton encargado de la llamada al backend para iniciar sesión global de juego (`/sessions`), finalizarla y registrar transacciones de canje de ventajas en el servidor.
* **`LsgLogger`**: Singleton encargado de almacenar temporalmente en memoria (mediante arreglos y diccionarios) los eventos y marcas de tiempo de la partida y enviar el log final consolidado.

### 3.8.3 Cierre de Sesión y Resguardo de Red
Para prevenir la pérdida de datos de telemetría y garantizar que el progreso de red del estudiante se registre de forma segura incluso ante cierres repentinos de la aplicación, el Autoload `LsgCore` deshabilita el cierre automático de la ventana en Godot (`get_tree().set_auto_accept_quit(false)`). 

Cuando el sistema operativo gatilla el evento de cierre (`NOTIFICATION_WM_CLOSE_REQUEST` o cierre voluntario por botón de salir), el Singleton intercepta la señal, detiene el proceso de salida y ejecuta una subrutina asíncrona bloqueante que envía el reporte estructurado de telemetría acumulado en `LsgLogger` al servidor central de la USACH y cierra la sesión de juego de forma ordenada antes de finalizar la ejecución del proceso en el dispositivo.

---

## 3.9 RESUMEN

En el presente capítulo se ha dado a conocer el diseño general, mecánicas, interfaz, estilo visual y administración de red para el videojuego serio **CyberSwipe-v2**. La solución combina la simplicidad lúdica del control de swipe en dispositivos móviles con el rigor pedagógico necesario para la formación de colaboradores en PYMEs chilenas. 

A través del framework bGames, el videojuego se alinea con la investigación del laboratorio InTeractiOn, creando una alternativa gamificada, formativa e interactiva que estimula el aprendizaje de la ciberseguridad y promueve buenos hábitos en el entorno real del estudiante.
