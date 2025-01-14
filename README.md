# Piggy Ransomware

Este proyecto contiene un script de ransomware escrito en Python y empaquetado en un ejecutable .exe utilizando PyInstaller. Este script es solo para fines educativos y de prueba en entornos controlados. No debe ser utilizado de manera maliciosa.

##  Descripción

1. Escalado de Permisos:

- Intenta ejecutar el script con privilegios de administrador.
- Si no tiene permisos de administrador, solicita al usuario que lo ejecute con privilegios elevados y termina la ejecución si no se otorgan.
Cifrado de Archivos:

1. Genera una clave AES-256 aleatoria.

- Cifra archivos específicos en el directorio de documentos del usuario utilizando AES-256.
- Cifra la clave AES-256 con una clave RSA-2048 y guarda la clave cifrada en un archivo encrypted_key.bin.
- Mueve el archivo encrypted_key.bin al directorio system32.


1. Manipulación de Archivos del Sistema:

- Crea un nuevo directorio en system32 llamado dragoncode_dir.
- Copia el ejecutable del script al directorio system32.

1. Manipulación de Imágenes:

- Lee una representación hexadecimal de una imagen desde un archivo de texto image_data.txt.
- Convierte los datos hexadecimales en una imagen.
- Guarda la imagen en el escritorio del usuario como IMPORTANTE.jpg.
- Establece la imagen como fondo de escritorio.

1. Limpieza de Claves:
- Borra la clave AES-256 de la memoria después de cifrar los archivos.



### Empaquetado del Script
El script se empaqueta en un ejecutable .exe utilizando PyInstaller. El archivo de especificaciones piggy.spec define cómo se empaqueta el
script.


El archivo piggy.spec incluye las siguientes configuraciones:

- Análisis del Script: Analiza el script executer.py y sus dependencias.
- Creación del Archivo PYZ: Crea un archivo PYZ que contiene todos los módulos Python necesarios.
- Creación del Ejecutable: Define la creación del ejecutable con el nombre piggy, incluyendo un icono personalizado piggy_icon.ico.









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