|     |     | UNIVERSIDAD  | DE SANTIAGO   |     | DE CHILE    |     |     |
| --- | --- | ------------ | ------------- | --- | ----------- | --- | --- |
|     |     | FACULTAD     | DE INGENIERÍA |     |             |     |     |
|     |     | DEPARTAMENTO | DE INGENIERÍA |     | INFORMÁTICA |     |     |
Desarrollo de un videojuego serio con foco en la ciberseguridad de
| PYMEs | Chilenas | aplicando | el marco | de  | trabajo | LifeSync-Games. |     |
| ----- | -------- | --------- | -------- | --- | ------- | --------------- | --- |
Propuesta de trabajo de título
|     |     |     | Estudiante:    |             |     | Bastian         | Guerrero Introduce el texto aquí |
| --- | --- | --- | -------------- | ----------- | --- | --------------- | -------------------------------- |
|     |     |     | Carrera:       |             |     | Ingeniería      | Civil en Informática             |
|     |     |     | Profesor       | Guía:       |     | Roberto         | González I.                      |
|     |     |     | Profesor       | Co-Guía:    |     | Juan Iturbe     | y Joaquin Macias.                |
|     |     |     | Profesor       | Asignatura: |     | Mario Inostroza | P.                               |
|     |     |     | 19 de enero de | 2026        |     |                 |                                  |

Resumen
La ciberseguridad se ha vuelto crítica ante el aumento de amenazas como el ransomware y la promul-
gación de la Ley 21.719 en Chile; sin embargo, el factor humano continúa siendo uno de los principales
vectoresderiesgo,especialmenteencontextosdondelacapacitacióntradicionalpresentalimitacionespara
generar cambios conductuales sostenidos. Frente a esta problemática, este trabajo aborda el desarrollo
de un videojuego serio para dispositivos móviles, implementado mediante el motor Godot Engine, que
emplea mecánicas de interacción tipo swipe para apoyar la formación en detección de phishing e integra el
framework LifeSync-Games (LSG) con el fin de vincular la experiencia de juego con hábitos del entorno
cotidiano. El propósito del proyecto es diseñar e implementar una herramienta formativa interactiva que
apoye los procesos de capacitación y concienciación en ciberseguridad en empleados de PYMEs chilenas,
sin pretender medir impactos organizacionales de largo plazo ni la reducción directa de incidentes reales.
El desarrollo se abordará mediante una metodología iterativa inspirada en RAD (Rapid Application
Development), orientada a la construcción incremental de un prototipo funcional, el cual será evaluado
desde una perspectiva técnica, de usabilidad y de jugabilidad mediante instrumentos estandarizados.
1
1ParalaelaboracióndeestedocumentoseutilizóInteligenciaArtificial(ChatGPTensuversiónGPT-4o,desarrolladapor
OpenAI)entareasespecíficasdesíntesis,redacciónyrevisiónortográfica,conelpropósitodemejorarlaclaridadycoherencia
textual.Elusodeestaherramientaselimitóexclusivamentealapoyodelaredacciónylacorrecciónortográficasininfluirenlos
objetivosdelproyecto,contenidotécnico,resultadosniconclusionesobtenidas.

| Tabla          | de contenidos |     |     |     |
| -------------- | ------------- | --- | --- | --- |
| 1. Descripción | del Problema  |     |     | 1   |
1.1. Motivación y Contexto . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 1
1.2. Enunciado del Problema . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 2
| 2. Análisis | de la solución |     |     | 2   |
| ----------- | -------------- | --- | --- | --- |
2.1. Enfoques de Solución . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 2
| 3. Justificación | del Enfoque | Seleccionado |     | 3   |
| ---------------- | ----------- | ------------ | --- | --- |
3.1. Marco Conceptual . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 4
3.1.1. Juegos Serios y Gamificación . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 4
3.1.2. Godot Engine . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 4
3.1.3. Framework LifeSync-Games (LSG) . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 4
3.1.4. Game Design Document . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 4
3.2. Estado del Arte . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 5
3.2.1. Videojuegos en la ciberseguridad . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 5
3.3. Resumen. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 6
| 4. Descripción | de la solución | propuesta |     | 6   |
| -------------- | -------------- | --------- | --- | --- |
4.1. Propósitos de la Solución . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 6
4.2. Características de la solución . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 6
4.3. Alcances y limitaciones de la solución . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 7
4.3.1. Alcances . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 7
4.3.2. Limitaciones . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 7
| 5. Evaluación | de la Solución |     |     | 8   |
| ------------- | -------------- | --- | --- | --- |
5.1. Pruebas Técnicas y de Rendimiento . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 8
5.2. Evaluación de la Experiencia de Usuario (UX) y Jugabilidad . . . . . . . . . . . . . . . . . . 8
5.3. Evaluación del Componente LifeSync-Games . . . . . . . . . . . . . . . . . . . . . . . . . . . 8
5.4. Pruebas de Aceptación . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 8
| 6. Objetivos | del Proyecto |     |     | 9   |
| ------------ | ------------ | --- | --- | --- |
6.1. Objetivo general . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 9
6.2. Objetivos Específicos . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 9
| 7. Metodología, | Herramientas | y Ambiente | de Desarrollo | 9   |
| --------------- | ------------ | ---------- | ------------- | --- |
7.1. Metodología a Usar . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 9
3

7.2. Herramientas de Desarrollo . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 10
7.3. Ambiente de Desarrollo . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 10
| 8. Plan   | de Trabajo | 10  |
| --------- | ---------- | --- |
| 9. Anexos |            | 11  |
9.1. Anexo A: Comparación de enfoques de formación en ciberseguridad. . . . . . . . . . . . . . . 11
9.2. Anexo B: Carta Gantt del Proyecto . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 11
9.3. Anexo C: Trazabilidad entre fases del plan de trabajo y objetivos específicos . . . . . . . . . . 12
| Referencias |     | 13  |
| ----------- | --- | --- |

1. Descripción del Problema
1.1. Motivación y Contexto
La ciberseguridad se ha consolidado como un factor crítico para la continuidad operativa de las
organizaciones modernas, especialmente ante el crecimiento sostenido de amenazas digitales que hoy superan
las capacidades defensivas tradicionales. A pesar del aumento sostenido en la inversión en tecnologías de
protección, la evidencia muestra que las conductas inseguras de los usuarios siguen siendo explotadas con
alta efectividad por ataques como el phishing y la ingeniería social, lo que sitúa al factor humano como el
eslabón más débil dentro de la cadena de defensa. En este contexto, la capacitación en ciberseguridad se ha
posicionado como una necesidad estratégica; sin embargo, los métodos tradicionales presentan limitaciones
relevantes para generar cambios conductuales sostenidos sobre los hábitos de seguridad de los empleados.
Uno de los principales factores que agrava esta problemática es la persistencia del error humano
comoorigendelosincidentesdeseguridad.Estudiosrecientesindicanquemásdel90 %delosataquesexitosos
tienen su origen en técnicas que explotan la falta de concienciación de los empleados (Álvarez et al., 2024).
Este escenario se ve intensificado por el uso creciente de herramientas basadas en inteligencia artificial por
parte de los atacantes, las cuales permiten generar mensajes fraudulentos más convincentes y personalizados,
dificultando su detección incluso por usuarios con experiencia básica.
Anivelorganizacional,lasPYMEsenfrentanunavulnerabilidadparticulardebidoasuslimitados
recursos técnicos, bajos niveles de madurez en ciberseguridad y una menor formalización de procesos de
capacitación. Esta situación se refleja en el impacto económico de los incidentes: el Reporte de Ciberseguridad
2025 señala que el ransomware concentró el 38 % de los ataques registrados en 2024, con un costo promedio
de 4.88 millones de dólares por incidente, ubicando a Chile entre los países más afectados de la región (Entel
Digital, 2025). En el contexto nacional, la Ley 21.719 refuerza la responsabilidad organizacional en materia de
ciberseguridad. En particular, su Artículo 50 establece la formación permanente del personal como una
función clave, mientras que el Artículo 14 quinquies 2 exige la adopción de medidas técnicas y organizativas
para resguardar la seguridad de la información, incluyendo la capacitación. El incumplimiento de estas
disposiciones puede constituir una infracción grave, sancionada conforme al Artículo 35, conllevando multas
de hasta 10.000 unidades tributarias mensuales. Este marco normativo refuerza la necesidad de estrategias
formativas más efectivas en las organizaciones (Biblioteca del Congreso Nacional de Chile, 2024).
Pese a este escenario, la literatura evidencia que las capacitaciones tradicionales basadas en
charlas expositivas o módulos informativos, presentan una efectividad limitada para modificar conductas de
seguridad. Estudios longitudinales muestran que los empleados capacitados mediante estos métodos presentan
tasas de error similares a aquellos sin capacitación al enfrentar simulaciones de phishing (Patringenaru,
2025). Asimismo, Resultados consistentes fueron reportados por Ho et al. (2025), quienes evidenciaron que la
2Términojurídicoquedesignaunaquintainserciónosubdivisióndeunartículo.
1

capacitación basada únicamente en la transmisión de información no genera cambios conductuales sostenidos.
Asimismo, ciertos enfoques punitivos, como las simulaciones de phishing con retroalimentación negativa,
pueden incluso producir efectos contraproducentes, generando desconfianza o resistencia en los empleados
(Byrd, 2025).
En síntesis, la combinación de un escenario de amenazas crecientes, la vulnerabilidad persistente
del factor humano y la baja efectividad de los métodos tradicionales de capacitación ha impulsado, a nivel
internacional, la exploración de enfoques formativos más dinámicos e interactivos. Investigaciones como las de
Hendrixetal.(2016)analizanelusodevideojuegosserioscomoalternativaparalaformaciónenciberseguridad,
destacando su potencial para promover un aprendizaje activo mediante la simulación de situaciones de riesgo.
Sin embargo, estos estudios también evidencian limitaciones relevantes, tales como su orientación a usuarios
conaltabasetécnica,lafaltadecontextualizaciónorganizacionalylaescasaalineaciónconmarcosregulatorios
locales. Este escenario refuerza la necesidad de desarrollar soluciones lúdicas e interactivas que, además de ser
participativas, se encuentren adaptadas a la realidad operativa y normativa de las PYMEs en el contexto
nacional.
1.2. Enunciado del Problema
Apesardelacrecienteinversiónentecnologíasdeproteccióndigital,lasPYMEschilenasenfrentan
dificultades para cumplir de manera efectiva con las exigencias de formación permanente establecidas por
el marco normativo. Los métodos tradicionales de capacitación en ciberseguridad presentan una capacidad
limitada para preparar a los empleados frente a amenazas como el phishing y la ingeniería social, debido a
su carácter principalmente pasivo y a la escasa contextualización de los contenidos respecto de la realidad
operativa de este tipo de organizaciones. En particular, estas capacitaciones suelen estar dirigidas a usuarios
sin formación técnica especializada, con tiempos acotados para procesos formativos, y utilizan enfoques
poco adaptados al contexto de las PYMEs chilenas. Esta situación evidencia una brecha en la forma en que
los contenidos formativos son entregados, dificultando la preparación efectiva de los empleados frente a las
amenazas digitales actuales.
¿De qué manera se pueden entregar los contenidos de formación en ciberseguridad
dispuestos por el marco normativo y las buenas prácticas actuales, orientados a la capacitación
de empleados de PYMEs chilenas?
2. Análisis de la solución
2.1. Enfoques de Solución
Para abordar la problemática de la formación en ciberseguridad, la literatura identifica diversas
estrategias orientadas a modificar el comportamiento del usuario. A continuación, se presenta un análisis
2

comparativo de los enfoques más representativos, evaluando su efectividad pedagógica y técnica:
|              |             |            | Consiste | en la evolución | de métodos | expositivos | mediante |
| ------------ | ----------- | ---------- | -------- | --------------- | ---------- | ----------- | -------- |
| Capacitación | tradicional | reforzada: |          |                 |            |             |          |
un incremento en la frecuencia de las sesiones y la actualización de contenidos. Pese a mejorar la
disponibilidad de información, su efectividad para generar cambios conductuales es limitada debido a su
| carácter | predominantemente | pasivo | (Ho et al., 2025). |     |     |     |     |
| -------- | ----------------- | ------ | ------------------ | --- | --- | --- | --- |
E-learning interactivo: Plataformas digitales basadas en módulos multimedia y evaluaciones au-
toguiadas. Investigaciones recientes destacan que, para ser efectivos, estos sistemas deben centrarse
en el usuario y en el cumplimiento de políticas, fomentando la conciencia situacional a través de la
interactividad técnica (Oroni et al., 2025). No obstante, su éxito depende de la motivación intrínseca del
| empleado | para completar | los módulos | sin supervisión | directa. |     |     |     |
| -------- | -------------- | ----------- | --------------- | -------- | --- | --- | --- |
serios:Entornoslúdicosdiseñadosparaelaprendizajeexperiencialmediantelasimulación
Videojuegos
de riesgos. Este enfoque permite la experimentación en entornos seguros y la toma de decisiones bajo
presión,loquefavoreceunamayorretencióndeconocimientosyuncompromisosuperiorencomparación
| con | métodos no | interactivos (Hendrix | et al., 2016). |     |     |     |     |
| --- | ---------- | --------------------- | -------------- | --- | --- | --- | --- |
LacomparaciónentrelosenfoquesdesoluciónidentificadossepresentaenlaTabla
| Análisis | Comparativo. |     |     |     |     |     |     |
| -------- | ------------ | --- | --- | --- | --- | --- | --- |
Anexo 1, incluida en el Anexo C. Dicha tabla resume los principales atributos de efectividad reportados en la
literatura académica, tales como motivación del usuario, nivel de interactividad, retención de información y
potencial de cambio conductual. Los criterios considerados se basan en tendencias observadas en estudios
previos sobre aprendizaje experiencial y simulación interactiva en ciberseguridad (Hendrix et al., 2016; Jaffray
| et al., 2021;    | Sharif & Ameen, | 2023).      |              |     |     |     |     |
| ---------------- | --------------- | ----------- | ------------ | --- | --- | --- | --- |
| 3. Justificación |                 | del Enfoque | Seleccionado |     |     |     |     |
A partir del análisis comparativo de los enfoques de solución y de la evidencia reportada en
la literatura, el uso de un videojuego serio se justifica como un enfoque coherente para apoyar procesos de
capacitación en ciberseguridad desde una perspectiva formativa e interactiva. Estudios previos destacan que
los entornos lúdicos y basados en simulación favorecen el aprendizaje activo, la participación del usuario y la
toma de decisiones contextualizadas, aspectos relevantes para la concienciación en seguridad digital (Hendrix
| et al., 2016; | Jaffray et | al., 2021). |     |     |     |     |     |
| ------------- | ---------- | ----------- | --- | --- | --- | --- | --- |
Asimismo, este enfoque se alinea con experiencias desarrolladas en el Lab, tales
InTeraction
como DigitalMaster, orientado a la formación en comercio electrónico (Vargas Morales, 2024), y WealthQuest,
enfocadoeneducaciónfinancieramediantemecánicasdejuego(SotoAguilar,2024).Estasiniciativasevidencian
el potencial de los videojuegos serios como herramientas habilitantes para la entrega de contenidos complejos
demaneraestructuradayparticipativa.Enconsecuencia,laseleccióndeesteenfoquerespondeasucoherencia
con el problema abordado, la literatura revisada y los alcances académicos del proyecto.
3

3.1. Marco Conceptual
3.1.1. Juegos Serios y Gamificación
Los juegos serios (serious games) son videojuegos que utilizan su arquitectura lúdica completa,
incluyendomecánicas,dinámicasyestética,paraalcanzarunobjetivoprimordialdistintoalapuraentretención,
tales como la educación o el entrenamiento profesional. Según Michael y Chen (2006), estos juegos aprovechan
el aspecto lúdico para captar la atención del usuario y facilitar el aprendizaje de conceptos complejos en un
entorno seguro, permitiendo el error y la práctica reiterada sin las consecuencias del mundo real.
Por otro lado, la gamificación difiere del juego serio en que no implica necesariamente la creación
de un juego, sino el uso de elementos de diseño de juegos en contextos no lúdicos. Deterding et al. (2011)
la describen formalmente como la incorporación de mecánicas, tales como sistemas de puntos, insignias o
tablas de clasificación, en entornos productivos o educativos con el objetivo de aumentar la motivación, el
compromiso y la participación del usuario en tareas que tradicionalmente no poseen un carácter recreativo.
3.1.2. Godot Engine
GodotEngineesunmotordedesarrollodevideojuegosdecódigoabierto(opensource),distribuido
bajo licencia MIT, que permite la creación de aplicaciones 2D y 3D sin costos de licenciamiento. Su soporte
multiplataforma y su buen rendimiento en dispositivos móviles lo convierten en una alternativa adecuada
para proyectos formativos dirigidos a organizaciones con recursos limitados, garantizando viabilidad técnica y
económica (Godot Engine Community, 2025).
3.1.3. Framework LifeSync-Games (LSG)
LifeSync-Games (LSG), anteriormente denominado Blended Games o bGames, es un marco de
trabajo desarrollado por el laboratorio InTeractiOn de la Universidad de Santiago de Chile, orientado a
integrar experiencias del mundo real dentro de videojuegos. Su propósito es promover un equilibrio entre la
vida cotidiana del usuario y el entretenimiento digital, incorporando datos provenientes de actividades reales
como parte de la dinámica de juego. Para ello, el framework permite transformar información capturada a
través de sensores físicos y lógicos del dispositivo en recompensas temporales que influyen en el progreso del
jugador.
3.1.4. Game Design Document
ElGameDesignDocument(GDD)actúacomoelplanoarquitectónicodelproyecto,consolidando
en un documento vivo todas las decisiones de diseño fundamentales, tales como las mecánicas de juego, la
narrativa, el diseño de niveles y la interfaz de usuario. Su propósito principal es servir como una herramienta
de comunicación unificada para el equipo de desarrollo, asegurando que la visión del producto se mantenga
coherente y evolucione de manera estructurada a lo largo del ciclo de vida del software (Rogers, 2014).
4

3.2. Estado del Arte
3.2.1. Videojuegos en la ciberseguridad
Diversas investigaciones han validado el uso de experiencias interactivas para la enseñanza de
ciberseguridad.Anivelinternacional,estudiosrecientesdemuestranquelosjuegosseriosresultanherramientas
efectivasyatractivastantoparaespecialistascomoparaaudienciasgenerales.Porejemplo,Jaffrayetal.(2021)
desarrollaron SherLOCKED, un juego serio para estudiantes de pregrado, mostrando que la combinación
de narrativa, decisiones rápidas y retroalimentación inmediata mejora la comprensión de conceptos como
la triada CIA y la identificación de amenazas. De manera similar, Williams et al. (2024) evidenciaron que
los entornos tipo Capture The Flag pueden involucrar a usuarios sin experiencia técnica, aumentando su
interés y participación en actividades formativas relacionadas con la seguridad digital. En la misma línea,
Sharif y Ameen (2023) concluyeron con su juego Security Power Lab que la interactividad práctica supera las
limitaciones de compromiso de los métodos tradicionales, indicando que el juego sirve como una herramienta
de formación crucial para aumentar los conocimientos y las habilidades en ciberseguridad.
También se han llevado a cabo estudios de videojuegos referentes a la ciberseguridad en la
Universidad de Santiago de Chile. Se tiene, por ejemplo, el trabajo de Parra Luman (2023), quien desarrolló
un juego serio 2D estilo RPG como complemento al aprendizaje para estudiantes del curso de Ciberseguridad.
Sus resultados, basados en pruebas de usabilidad y evaluación de contenidos aplicadas a ex-alumnos del curso,
confirmaron la calidad educativa del juego y su eficacia para reforzar los conocimientos adquiridos en clases
tradicionales, evidenciando una recepción positiva por parte de los participantes. Por otro lado, Toro Flores
(2024) creó un videojuego RPG 2D enfocado en simular el rol específico de Gestor de Riesgos (Cybersecurity
Risk Manager según ENISA) dentro de una empresa mediana de desarrollo de software, aplicando el proceso
de gestión de riesgos de ISO 27005. Las evaluaciones realizadas a 16 usuarios mostraron una alta usabilidad
(promedio SUS de 87.2) y un alto porcentaje de logro en los objetivos de aprendizaje (promedio 81.92%),
concluyendo que el videojuego contribuyó efectivamente a adquirir conocimiento sobre las competencias de
dicho rol profesional.
Respectoalassolucionescomercialesexistentes,seidentificaronherramientascomoCybersecurity
Lab de PBS, Hacknet, el Phishing Quiz de Google o el Cyber Awareness Challenge del Departamento de
Defensa de EE. UU. Si bien estas propuestas son funcionales en sus respectivos nichos, presentan brechas
significativas para el objetivo de este proyecto, dado que la mayoría se encuentra únicamente en inglés, poseen
unenfoqueexcesivamentetécnico,ocarecendemétricasdeaprendizajeprofundas.Además,ningunaconsidera
la realidad cultural ni el marco legal de las PYMEs chilenas. Por ello, la solución propuesta busca cubrir
este vacío mediante un diseño contextualizado y apoyado en el framework LifeSync-Games para asegurar
resultados medibles.
5

3.3. Resumen
En síntesis, la literatura revisada evidencia que el factor humano continúa siendo el principal
origen de incidentes de ciberseguridad, especialmente en PYMEs que carecen de cultura digital robusta. Asi
mismo, Los métodos tradicionales de capacitación presentan baja efectividad, mientras que los juegos serios
han demostrado mejorar la motivación, la retención del aprendizaje, la toma de decisiones mediante escenarios
simulados y retroalimentación inmediata. Adicionalmente, frameworks como LSG permiten estructurar
experiencias formativas más completas, integrando métricas y elementos de bienestar. Este panorama justifica
el uso de un videojuego serio como alternativa prometedora para fortalecer la concienciación en ciberseguridad.
4. Descripción de la solución propuesta
4.1. Propósitos de la Solución
Lasoluciónpropuestatienecomopropósitoapoyarlosprocesosdecapacitaciónenciberseguridad
medianteunaexperienciainteractivaquepermitaalosusuariosreconocerriesgosdigitalescomunesypracticar
la toma de decisiones seguras en un entorno simulado, alineado con las necesidades formativas y operativas de
las PYMEs chilenas, complementando los métodos tradicionales de formación sin reemplazarlos.
4.2. Características de la solución
La solución propuesta consiste en el desarrollo de un videojuego serio para dispositivos
móviles,conectadoconlarealidadapartirdelaaplicacióndelframeworkLifeSync-Games,orientadoaapoyar
la concienciación en ciberseguridad en colaboradores de PYMEs chilenas. El videojuego se implementará
utilizando el motor Godot, seleccionado debido a su carácter de código abierto, su ligereza, su excelente
rendimiento en dispositivos móviles y la ausencia de costos por licencias o distribución. Estas características
lo convierten en una alternativa ventajosa frente a motores como Unity, cuyo nuevo modelo de tarifas y
dependencias adicionales lo hacen menos adecuado para proyectos formativos dirigidos a organizaciones con
recursos limitados. El diseño del videojuego considera este perfil de usuario, priorizando una interacción
simple, contenidos en español y escenarios cercanos al contexto laboral de las PYMEs, con el fin de facilitar su
adopción por empleados sin formación técnica especializada y con tiempos acotados para procesos formativos.
El videojuego incorporará una mecánica principal de tipo Swipe, propia de juegos de categoría
Puzzle, mediante la cual el usuario deberá tomar decisiones rápidas frente a situaciones cotidianas asociadas a
riesgos de ciberseguridad. Esta dinámica favorece sesiones breves de interacción y permite entrenar la toma
de decisiones rápidas ante intentos de phishing, mensajes engañosos o solicitudes sospechosas, replicando
escenarios cotidianos del entorno laboral de las PYMEs, favoreciendo su adopción por usuarios no técnicos.
Una característica central del diseño es la utilización de contenido dinámico. Los escenarios,
tarjetas y desafíos no formarán parte fija del código del videojuego; en su lugar, serán cargados desde un
6

repositorio externo o fuente actualizable. Esto permitirá que las organizaciones actualicen los contenidos sin
necesidad de modificar el juego ni generar nuevas compilaciones. Como característica adicional, la solución
considera la incorporación de modelos de Lenguaje de Gran Tamaño (LLM) para la generación dinámica de
escenarios, preguntas o interacciones, tales como simulaciones de ingeniería social. Este enfoque permitiría
diversificar las experiencias de juego y adaptar los desafíos presentados al usuario.
El videojuego integrará elementos de gamificación, tales como sistemas de puntos, insignias,
niveles y métricas de desempeño, con el propósito de aumentar la motivación del usuario y reforzar el proceso
de aprendizaje. Asimismo, se incluirán mecanismos de seguimiento que permitirán a las empresas evaluar el
progresodesuscolaboradoresymedirelimpactodelacapacitaciónentérminosdemejoradelaconcienciación
en ciberseguridad.
Finalmente, el diseño se alineará con la aplicacion del framework LifeSync-Games (LSG),
permitiendo reforzar conductas asociadas a los objetivos formativos del videojuego, vinculando acciones del
mundo real con ajustes en la experiencia lúdica. Esta integración posibilita que determinadas prácticas o
comportamientos del usuario puedan verse reflejados en la dinámica del juego.
4.3. Alcances y limitaciones de la solución
4.3.1. Alcances
La solución está dirigida a PYMEs chilenas, proporcionando una herramienta accesible para
la formación en prácticas básicas de ciberseguridad. El videojuego permitirá simular escenarios comunes de
riesgo,talescomoataquesdephishing,ingeniería socialymanejoinadecuadodeinformación,promoviendo
la toma de decisiones seguras en un entorno controlado.
El videojuego será desarrollado para dispositivos móviles, considerando su alta penetración en
el contexto nacional. Asimismo, la solución incorpora elementos de gamificación y mecánicas simples basadas
en gestos swipe, diseñadas para sesiones breves y para usuarios sin experiencia técnica.
4.3.2. Limitaciones
La solución no reemplaza las políticas ni las medidas técnicas de ciberseguridad organizacional,
como firewalls o configuraciones de red, limitándose a la formación y concienciación del usuario final.
La evaluación del videojuego se realizará en un contexto acotado, centrado en su funcionamiento
técnico,jugabilidadyaceptaciónporpartedeungruporeducidodeparticipantesdeconfianza.Enconsecuencia,
no se medirá su impacto a largo plazo en el comportamiento organizacional ni en la reducción
de incidentes reales, ya que ello excede los alcances del proyecto y requeriría aprobación de un comité
de ética (CEI). Asimismo, la solución corresponde a una implementación para plataformas móviles y no
contempla soporte ni mantenimiento posterior al desarrollo de este proyecto.
7

5. Evaluación de la Solución
Para validar la efectividad, usabilidad y calidad técnica de la solución propuesta, se ha definido
una estrategia de evaluación mixta que abarca pruebas técnicas de software y evaluaciones centradas en la
experienciadelusuario(UX).Estopermitiráverificarelcorrectofuncionamientodelvideojuego,suestabilidad
en distintos dispositivos, la experiencia del usuario y el impacto del uso del framework LifeSync-Games en el
comportamiento del sistema.
5.1. Pruebas Técnicas y de Rendimiento
Se realizarán pruebas orientadas a garantizar la estabilidad y correcto funcionamiento del
videojuego desarrollado en Godot Engine. Estas incluyen evaluaciones de rendimiento en dispositivos móviles
de gama media y baja, considerando métricas como tasa de fotogramas por segundo (FPS), tiempos de
carga, consumo de memoria RAM y uso de batería. Asimismo, se efectuarán pruebas unitarias e integradas
para validar la lógica de juego y la correcta comunicación entre el cliente y los sensores del framework
LifeSync-Games.
5.2. Evaluación de la Experiencia de Usuario (UX) y Jugabilidad
Dado el carácter formativo del videojuego serio, se evaluará la experiencia de usuario mediante
instrumentos estandarizados aplicados a un grupo de participantes de confianza. La usabilidad percibida
se medirá utilizando la escala System Usability Scale (SUS), la cual permite obtener un puntaje global de
facilidad de uso a partir de un cuestionario de 10 ítems (Brooke, 1996). Por su parte, la jugabilidad será
evaluada mediante el modelo Heuristic Evaluation for Playability (HEP), considerando aspectos como claridad
de objetivos, retroalimentación del sistema y curva de aprendizaje (Heather Desurvire, 2004).La evaluación
propuesta se centra en la eficacia formativa de la solución como herramienta de capacitación en ciberseguridad
y no en la medición directa de incidentes reales de seguridad, lo cual excede el alcance del presente proyecto.
5.3. Evaluación del Componente LifeSync-Games
ParaevaluarelimpactodelframeworkLifeSync-Games,seconsiderarándosescenariosdeprueba:
uno en el que el videojuego utiliza datos del entorno físico del usuario para modificar dinámicamente variables
internasdeljuego,yotroenelqueoperasindichaintegración.Estacomparaciónpermitiráanalizarlosefectos
de LSG en el juego.
5.4. Pruebas de Aceptación
Finalmente, se realizará una verificación de cumplimiento de requisitos funcionales, donde se
comprobará que las funcionalidades críticas operen según lo diseñado en el Documento de Diseño de Juego
8

(GDD).Esta validación será ejecutada por tres usuarios expertos: el profesor guía y los dos profesores co-guías
del proyecto, quienes certificarán la correcta operación del MVP desarrollado.
| 6. Objetivos |          | del     | Proyecto |     |     |     |     |
| ------------ | -------- | ------- | -------- | --- | --- | --- | --- |
| 6.1.         | Objetivo | general |          |     |     |     |     |
Desarrollar un videojuego serio para la formación en ciberseguridad, utilizando el framework
LifeSync-Games (LSG), el motor Godot y Modelos de Lenguaje de Gran Tamaño (LLM), orientado a apoyar
los procesos de capacitación y concienciación en ciberseguridad de empleados de PYMEs chilenas, mediante la
| simulación | de escenarios |             | comunes | de riesgo digital. |     |     |     |
| ---------- | ------------- | ----------- | ------- | ------------------ | --- | --- | --- |
| 6.2.       | Objetivos     | Específicos |         |                    |     |     |     |
1. Elaborar el (GDD) de un videojuego serio orientado a la formación y concien-
|     |     | Game Design | Document |     |     |     |     |
| --- | --- | ----------- | -------- | --- | --- | --- | --- |
ciación en ciberseguridad, incorporando mecánicas de juego condicionadas por el perfil de usuario de
LSG.
2. Diseñar la estructura instruccional y el contenido formativo base en ciberseguridad, definiendo objetivos
de aprendizaje, principios pedagógicos y contenidos iniciales que orienten el diseño de la experiencia
educativa.
3. Implementar un videojuego serio a partir del GDD, integrando el framework LifeSync-Games y el uso
de modelos de lenguaje de gran tamaño (LLM) para la generación automática de escenarios comunes de
| riesgo | digital. |     |     |     |     |     |     |
| ------ | -------- | --- | --- | --- | --- | --- | --- |
4. Desarrollar e integrar al menos dos sensores que permitan registrar actividades del usuario en el entorno
| real | y/o | dentro del | videojuego, | para su | uso en la dinámica | del | sistema. |
| ---- | --- | ---------- | ----------- | ------- | ------------------ | --- | -------- |
5. Evaluar el videojuego mediante pruebas técnicas y de experiencia de usuario, considerando métricas de
| rendimiento,    |             | usabilidad | y jugabilidad. |     |            |     |               |
| --------------- | ----------- | ---------- | -------------- | --- | ---------- | --- | ------------- |
| 7. Metodología, |             |            | Herramientas   |     | y Ambiente |     | de Desarrollo |
| 7.1.            | Metodología |            | a Usar         |     |            |     |               |
El proyecto se abordará mediante una metodología iterativa e incremental estructurada en
| tres etapas | principales. |     | La primera, | de análisis | e inspirada | en el enfoque |     |
| ----------- | ------------ | --- | ----------- | ----------- | ----------- | ------------- | --- |
Rapid Application Development
(RAD), utiliza prototipos funcionales y no funcionales para el levantamiento y refinamiento de requerimientos,
incorporando una evaluación temprana desde la perspectiva del usuario. La segunda etapa consiste en un
9

proceso iterativo e incremental centrado en el diseño e implementación técnica del videojuego. Finalmente,
la tercera etapa contempla la evaluación exhaustiva del sistema y su despliegue funcional en un entorno
controlado.
| 7.2. Herramientas |              | de  | Desarrollo |               |     |                 |            |          |       |         |
| ----------------- | ------------ | --- | ---------- | ------------- | --- | --------------- | ---------- | -------- | ----- | ------- |
|                   |              |     |            | El videojuego |     | se desarrollará | utilizando | el motor |       | Engine, |
|                   | Herramientas | de  | software:  |               |     |                 |            |          | Godot |         |
debido a su carácter de código abierto, su eficiencia en dispositivos móviles y la ausencia de costos de
licenciamiento. Para el control de versiones se emplearán Git y GitHub, mientras que el diseño visual se
apoyará en herramientas de edición 2D. La documentación técnica y académica se elaborará en LATEX,
| complementada | con          | herramientas | de diagramación. |     |            |               |               |            |     |           |
| ------------- | ------------ | ------------ | ---------------- | --- | ---------- | ------------- | ------------- | ---------- | --- | --------- |
|               |              |              |                  | El  | desarrollo | y las pruebas | se realizarán | utilizando |     | un equipo |
|               | Herramientas |              | de hardware:     |     |            |               |               |            |     |           |
computacionalpersonalconsistemaoperativoWindows,juntocondispositivosmóvilesutilizadosparapruebas
| de ejecución, | compatibilidad | y               | rendimiento. |               |     |             |             |                  |     |     |
| ------------- | -------------- | --------------- | ------------ | ------------- | --- | ----------- | ----------- | ---------------- | --- | --- |
| 7.3. Ambiente |                | de Desarrollo   |              |               |     |             |             |                  |     |     |
|               | El proyecto    | se desarrollará |              | bajo el alero | del |             |             |                  |     |     |
|               |                |                 |              |               |     | laboratorio | InTeractiOn | del Departamento |     | de  |
Ingeniería Informática (DIINF) de la Universidad de Santiago de Chile. Este entorno proporciona
una red de apoyo conformada por estudiantes, profesionales y tutores académicos, así como el acceso a
los servicios cloud del framework LifeSync-Games (LSG) desplegados en el DIINF, los cuales son
fundamentales para la implementación y validación de la solución. Asimismo, este entorno facilita instancias
de pares, permitiendo obtener retroalimentación temprana y referencias para
| evaluación    | preliminar   | por    |                |     |           |             |     |     |     |     |
| ------------- | ------------ | ------ | -------------- | --- | --------- | ----------- | --- | --- | --- | --- |
| el desarrollo | del proyecto | dentro | de un contexto |     | académico | controlado. |     |     |     |     |
| 8. Plan       | de Trabajo   |        |                |     |           |             |     |     |     |     |
El proyecto se desarrolla en cuatro fases distribuidas en 17 semanas, las cuales se agrupan dentro
de las tres etapas definidas en la metodología propuesta. La Fase 1 (Análisis y diseño conceptual) se enmarca
en la etapa de análisis, e incluye el levantamiento y refinamiento de requisitos, el diseño instruccional y la
elaboración del Game Design Document (GDD). La Fase 2 (Prototipado rápido) también forma parte de
esta etapa y se orienta a la validación temprana de mecánicas y decisiones de diseño. La Fase 3 (Desarrollo
iterativo e incremental) corresponde a la segunda etapa metodológica y contempla la implementación del
videojuego, la integración del framework LifeSync-Games, el uso de modelos de lenguaje y el desarrollo de
sensores. Finalmente, la Fase 4 (Evaluación y cierre) se alinea con la tercera etapa metodológica e incluye
pruebas técnicas, evaluaciones de usabilidad y jugabilidad, pruebas de aceptación y documentación final. La
planificación temporal detallada y la trazabilidad entre actividades y objetivos específicos se presentan en los
| Anexos 9.2 | y 9.3. |     |     |     |     |     |     |     |     |     |
| ---------- | ------ | --- | --- | --- | --- | --- | --- | --- | --- | --- |
10

9. Anexos
9.1. Anexo A: Comparación de enfoques de formación en ciberseguridad
|                | Tabla         | 1: Cuadro comparativo | de   | atributos por enfoque | de solución. |     |
| -------------- | ------------- | --------------------- | ---- | --------------------- | ------------ | --- |
| Criterio       |               | Capacitación          | Tra- | E-learning            | Videojuegos  | Se- |
|                |               | dicional              |      |                       | rios         |     |
| Costo          | de Desarrollo | Bajo                  |      | Medio                 | Medio/Alto   |     |
| Escalabilidad  |               | Baja                  |      | Alta                  | Alta         |     |
| Motivación     | del Usuario   | Baja/Media            |      | Media                 | Alta         |     |
| Cambio         | Conductual    | Bajo/Medio            |      | Medio                 | Medio/Alto   |     |
| Interactividad |               | Baja                  |      | Media                 |              |     |
Alta
| Retención | de Informa- | Baja/Media |     | Media | Alta |     |
| --------- | ----------- | ---------- | --- | ----- | ---- | --- |
ción
Fuente:Elaboraciónpropia.
| 9.2. Anexo | B: Carta | Gantt del | Proyecto |     |     |     |
| ---------- | -------- | --------- | -------- | --- | --- | --- |
Esteanexopresentalaplanificacióntemporaldelproyecto,distribuidaencuatrofasesprincipales
y organizada en un horizonte de 17 semanas. La carta Gantt detalla las actividades consideradas en cada fase,
su duración estimada y su secuencia temporal, permitiendo visualizar el avance esperado del desarrollo del
| videojuego serio. |     |     |     |     |     |     |
| ----------------- | --- | --- | --- | --- | --- | --- |
11

|     | Figura 1: Carta | Gantt del proyecto | de desarrollo | del videojuego | serio. |
| --- | --------------- | ------------------ | ------------- | -------------- | ------ |
9.3. Anexo C: Trazabilidad entre fases del plan de trabajo y objetivos específicos
La Tabla 2 presenta la relación entre las fases definidas en el plan de trabajo y los objetivos
específicos del proyecto. Esta trazabilidad complementa la planificación presentada en la carta Gantt, permi-
tiendo evidenciar la coherencia entre la metodología adoptada, las actividades desarrolladas y los resultados
esperados.
|          | Tabla 2: Trazabilidad | entre fases   | del plan de trabajo | y objetivos | específicos |
| -------- | --------------------- | ------------- | ------------------- | ----------- | ----------- |
| Fase del | Plan de Trabajo       |               | Objetivos           | Específicos | Asociados   |
| Fase 1:  | Análisis y diseño     | conceptual    | OE1, OE2            |             |             |
| Fase 2:  | Prototipado rápido    |               | OE3                 |             |             |
| Fase 3:  | Desarrollo iterativo  | e incremental | OE3, OE4            |             |             |
| Fase 4:  | Evaluación y cierre   |               | OE5                 |             |             |
12

Referencias
Álvarez, A. L., Cruz, J. A., Cruz, S. B., Gallardo, J. d. C., López, I. M., & García, R. E. (2024). El phishing
comoamenazaenlaciberseguridadcorporativadegrandesempresas.InvestigacionesLatinoamericanas
en Ingeniería y Arquitectura, (1), 26-33. https://doi.org/10.51378/ilia.vi1.8496
Biblioteca del Congreso Nacional de Chile. (2024). Ley N° 21.719: Regula la protección y el tratamiento de los
datos personales y crea la Agencia de Protección de Datos Personales [Publicada en el Diario Oficial
el 13-12-2024. Consultado el 27 de octubre de 2025]. https://www.bcn.cl/leychile/navegar?idNorma=
1209272
Brooke, J. (1996). SUS: A ’quick and dirty’ usability scale. En P. W. Jordan, B. Thomas, B. A. Weerdmeester
|     | & I. L. McClelland |     | (Eds.), |           |            |     | (pp.     | 189-194). | Taylor & Francis. |     |
| --- | ------------------ | --- | ------- | --------- | ---------- | --- | -------- | --------- | ----------------- | --- |
|     |                    |     |         | Usability | Evaluation | in  | Industry |           |                   |     |
Byrd, P. (2025, marzo). Why Your Phishing Simulations Feel Like a Trap—and How to Make Them Feel Like
a Game. Consultado el 18 de noviembre de 2025, desde https://www.hooksecurity.co/blog/phishing-
simulations-game
Deterding, S., Dixon, D., Khaled, R., & Nacke, L. (2011). From game design elements to gamefulness: defining
"gamification".
Proceedings of the 15th International Academic MindTrek Conference: Envisioning
|     | Future Media | Environments, |     | 9-15. https://doi.org/10.1145/2181037.2181040 |     |     |     |     |     |     |
| --- | ------------ | ------------- | --- | --------------------------------------------- | --- | --- | --- | --- | --- | --- |
Entel Digital. (2025). Reporte de Ciberseguridad 2025 [Consultado el 25 de septiembre de 2025]. https:
//enteldigital.cl/reporte-ciberseguridad
Godot Engine Community. (2025). Godot Engine 4.3 Documentation: Introduction to Godot [Accedido:
06-12-2025]. Godot Foundation. https://docs.godotengine.org/en/stable/about/introduction.html
Heather Desurvire, J. A. T., Martin Caplan. (2004). Using heuristics to evaluate the playability of games.
|     |                  |           |     |          |         |              | Systems, | 1509-1512. | https://doi.org/10. |     |
| --- | ---------------- | --------- | --- | -------- | ------- | ------------ | -------- | ---------- | ------------------- | --- |
|     | CHI ’04 Extended | Abstracts |     | on Human | Factors | in Computing |          |            |                     |     |
1145/985921.986102
Hendrix, M., Al-Sherbaz, A., & Bloom, V. (2016). Game Based Cyber Security Training: Are Serious
Games Suitable for Cyber Security Training? Games, 3(1), 53-61.
|     |     |     |     |     |     | International | Journal | of Serious |     |     |
| --- | --- | --- | --- | --- | --- | ------------- | ------- | ---------- | --- | --- |
https://doi.org/10.17083/ijsg.v3i1.107
Ho, G., Mirian, A., Luo, E., Tong, K., Lee, E., Liu, L., Longhurst, C. A., Dameff, C., Savage, S., & Voelker,
G. M. (2025). Understanding the Efficacy of Phishing Training in Practice. 2025 IEEE Symposium on
Security and Privacy (S&P). https://people.cs.uchicago.edu/~grantho/papers/oakland2025_phishing-
training.pdf
Jaffray, A., Finn, C., & Nurse, J. R. C. (2021). SherLOCKED: A Detective-Themed Serious Game for Cyber
|          | Security Education. |             | En                                          |         |                |       |               |               | (pp. 35-45). | Springer |
| -------- | ------------------- | ----------- | ------------------------------------------- | ------- | -------------- | ----- | ------------- | ------------- | ------------ | -------- |
|          |                     |             | Human                                       | Aspects | of Information |       | Security      | and Assurance |              |          |
|          | International       | Publishing. | https://doi.org/10.1007/978-3-030-81111-2_4 |         |                |       |               |               |              |          |
| Michael, | D. R., &            | Chen, S.    | L. (2006).                                  |         |                |       |               |               | Inform.      | Cengage  |
|          |                     |             |                                             | Serious | Games:         | Games | That Educate, | Train,        | and          |          |
Learning.
13

Oroni, C. Z., Xianping, F., Ndunguru, D. D., & Ani, A. (2025). Enhancing Cyber Safety in E-Learning
Environment through Cybersecurity Awareness and Information Security Compliance: PLS-SEM and
FsQCAAnalysis.ResearchGate/InternationalJournalofInformationSecurity.https://doi.org/https:
//doi.org/10.1016/j.cose.2024.104276
Parra Luman, B. I. (2023). Uso de juego serio como complemento al aprendizaje en estudiantes de Ingeniería
del área Computación e Informática en el curso de ciberseguridad [Tesis de Grado]. Universidad
de Santiago de Chile. https://usach.primo.exlibrisgroup.com/discovery/fulldisplay?docid=
alma992124240206116&context=L&vid=56USACH_INST:REPOSITORIO
Patringenaru, I. (2025, septiembre). Cybersecurity Training Programs Don’t Prevent Employees from Falling
for Phishing Scams. Consultado el 18 de noviembre de 2025, desde https://today.ucsd.edu/story/
cybersecurity-training-programs-dont-prevent-employees-from-falling-for-phishing-scams
Rogers, S. (2014). Level Up! The Guide to Great Video Game Design (2nd). John Wiley & Sons.
Sharif, K. H., & Ameen, S. Y. (2023). A Intelligent Security Power Lab (SPL): The Ultimate Serious
Game Training in Cybersecurity. International Journal of Intelligent Systems and Applications in
Engineering, 11(11s), 245-259. https://ijisae.org/index.php/IJISAE/article/view/3468
Soto Aguilar, J. I. (2024). WealthQuest: un juego serio para apoyar la educación financiera aplicando el
framework Blended Games [Tesis de Ingeniero de Ejecución]. Universidad de Santiago de Chile
[Accedido: 12-12-2025]. https://usach.primo.exlibrisgroup.com/discovery/fulldisplay?docid=
alma992203734506116&context=L&vid=56USACH_INST:REPOSITORIO
Toro Flores, L. J. (2024). Simulando el rol de gestor de riesgos en ciberseguridad para estudiantes de la
Universidad de Santiago de Chile: Un enfoque educativo mediante un videojuego RPG [TesisdeGrado].
Universidad de Santiago de Chile. https://usach.primo.exlibrisgroup.com/discovery/fulldisplay?
docid=alma992164036006116&context=L&vid=56USACH_INST:REPOSITORIO
VargasMorales,V.A.(2024).LaborettoNostra:JuegoSerioparaimpulsarunavisiónemprendedoraatravésde
comercios en línea [Tesis de Ingeniero de Ejecución]. Universidad de Santiago de Chile [Accedido: 12-
12-2025]. https://usach.primo.exlibrisgroup.com/discovery/fulldisplay?docid=alma992205840506116&
context=L&vid=56USACH_INST:REPOSITORIO
Williams, L., Anthi, E., Cherdantseva, Y., & Javed, A. (2024). Leveraging Gamification and Game-based
Learning in Cybersecurity Education: Engaging and Inspiring Non-Cyber Students. Journal of The
Colloquium for Information Systems Security Education, 11(1). https://cisse.info/journal/index.php/
cisse/article/view/186
14