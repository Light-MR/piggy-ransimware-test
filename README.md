



## Monitoreo de ataque con WAZUH
El pdf muestra una sección sobre el ataque de ransomware en Windows monitoreado con wazuh,  detalla lo siguiente:

- Estado previo al ataque:
El documento muestra un dashboard inicial antes de que ocurra el ataque. No se especifican eventos de seguridad relevantes en esta etapa.
-  Estado posterior al ataque:
Después del ataque, se observa en el reporte de eventos de seguridad que el agente en el sistema Windows (identificado como "windows-is-victim") está desconectado.

- Detalles del agente afectado:
ID: 003
Nombre: windows-is-victim
IP: 10.0.2.15
Versión de Wazuh: 4.6.0
Sistema Operativo: Microsoft Windows 10 Home
Última conexión: 22 de noviembre de 2023, 03:50:11
El estado del agente desconectado es un posible indicio de actividad maliciosa o pérdida de control tras el ataque.
Reporte de alertas:

Se enumeran las reglas y eventos detectados en el sistema.
Entre los eventos críticos identificados está la presencia de vulnerabilidades como CVE-2023-21526 y otras asociadas con Windows 10.
Algunos eventos están relacionados con configuraciones que no cumplen estándares de seguridad, como "Allow Basic Authentication" habilitado o contraseñas no protegidas adecuadamente.