# CIS Controls v8 - IG1 (Grupo de Implementación 1): Guía de Conocimiento Ampliada para PYMEs

Este documento detalla las salvaguardas de ciberhigiene básica que componen el Grupo de Implementación 1 (IG1) de CIS Controls v8. Sirve como referencia técnica para estructurar cápsulas y cartas pedagógicas equilibradas a lo largo de todo el programa CyberSwipe.

---

## 1. Cobertura de Controles e Salvaguardas IG1

### Control 1: Inventario y Control de Activos Físicos y Dispositivos
* **Salvaguardas:** Mantener un inventario actualizado de todos los dispositivos corporativos (laptops, celulares, tablets). Prohibir la conexión de dispositivos personales o no autorizados a la red interna.
* **Escenarios pedagógicos:** Teletrabajo, conexión de pendrives desconocidos, uso de redes Wi-Fi públicas o dispositivos personales (BYOD).

### Control 2: Inventario y Control de Activos de Software
* **Salvaguardas:** Utilizar solo software autorizado y licenciado. Eliminar o bloquear aplicaciones no autorizadas, plugins de navegador dudosos o suites piratas.
* **Escenarios pedagógicos:** Instalación de herramientas "gratuitas" de conversión de PDF, plugins no verificados, software de control remoto no aprobado.

### Control 4: Configuración Segura de Activos y Software
* **Salvaguardas:** Plantillas de configuración segura (CIS 4.1), desactivación de ejecuciones automáticas (Autorun/Autoplay en USB - CIS 4.8) y activación de firewall personal en endpoints (CIS 4.4).
* **Escenarios pedagógicos:** Desactivar avisos de seguridad, conectar discos externos, puertos de red expuestos.

### Control 5: Gestión de Cuentas y Control de Accesos
* **Salvaguardas:**
  * **Políticas de Contraseñas Fuertes (CIS 5.2):** Longitud mínima (14+ caracteres o passphrases), uso de gestores autorizados, prohibición absoluta de reutilizar claves.
  * **MFA Obligatorio (CIS 5.3):** Aplicación de MFA en correo, VPN, finanzas y la nube. Uso de apps autenticadoras en lugar de SMS cuando sea posible.
  * **Principio de Mínimo Privilegio (CIS 5.4):** Limitar accesos a lo estrictamente necesario para la función laboral. Prohibir el uso diario de cuentas de administrador.
  * **Bloqueo Automático y Manual de Sesiones (CIS 5.5):** Bloqueo tras inactividad y hábito de bloqueo manual (`Win + L` / `Cmd + Ctrl + Q`) al levantarse del escritorio.
* **Escenarios pedagógicos:** Post-its con claves, préstamo informal de credenciales a colegas, sesiones abiertas en escritorios compartidos o recepción.

### Control 7: Gestión de Vulnerabilidades y Parches
* **Salvaguardas (CIS 7.1):** Habilitar actualizaciones automáticas del sistema operativo y aplicaciones de terceros para corregir fallas de seguridad conocidas.
* **Escenarios pedagógicos:** Notificaciones de actualización pospuestas durante semanas por "no interrumpir el trabajo".

### Control 10: Defensas contra Malware y Filtros
* **Salvaguardas (CIS 10.1):** Antivirus corporativo con firmas actualizadas diariamente. Filtros de correo para bloquear adjuntos ejecutables o sospechosos.
* **Escenarios pedagógicos:** Alertas de antivirus ignoradas, descarga de adjuntos con macros (`.xlsm`).

### Control 11: Copias de Seguridad (Backups) y Recuperación
* **Salvaguardas:**
  * **Respaldos Automatizados (CIS 11.1):** Copias periódicas de datos de negocio (facturación, contabilidad, clientes).
  * **Respaldos Aislados / Offline (CIS 11.2):** Mantener al menos una copia desconectada de la red local para protegerla contra el ransomware.
  * **Pruebas de Restauración (CIS 11.4):** Simulacros periódicos para asegurar que los datos respaldados sean legibles y recuperables.
* **Escenarios pedagógicos:** Infecciones de ransomware, falla de discos locales, validación de respaldos antes de emergencias.

### Control 17: Gestión de Incidentes y Reporte
* **Salvaguardas (CIS 17.1):** Establecer un flujo claro para que los empleados reporten inmediatamente eventos sospechosos (correos dudosos, pérdidas de equipos, comportamientos extraños del sistema).
* **Escenarios pedagógicos:** Miedo a reportar un error propio vs reporte oportuno que evita la propagación de una brecha.
