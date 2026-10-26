---
title: Investigación (Concurrencia, Tipos de SSOO, Instalación Dual Boot)
author: Rosendo Camal
date: 2026-10-18
categories:
  - operating-systems
  - dual-boot
---
# Investigación

**Rosendo Camal**

| Fecha        | Asignatura          | Cuatrimestre | Profesor               |
| ------------ | ------------------- | ------------ | ---------------------- |
| 2026-10-2026 | Sistemas Operativos | 4to          | Oscar David Catzim Pat |

## Concurrencia

El concepto de **concurrencia** se entiende principalmente bajo la siguiente definición:
> Propiedad de un sistema que permite ejecutar varias tareas durante periodos de tiempo que se solapan. Las tareas pueden alternarse en un mismo procesador o ejecutarse simultáneamente en varios procesadores.[^1]

Sin embargo, desde el punto de vista formal, la *concurrencia* no se refiere a dos o más tareas ocurran a la vez sino a dos o más eventos cuyo orden es **no determinista**, esto es, eventos acerca de los cuales *no se puede predecir el orden relativo en que ocurrirán*.[^2] Esto no implica que la primera concepción esté mal, puesto que dos o más tareas simultáneas son considerados concurrentes.

Un ejemplo de concurrencia es la de un servidor web que recibe dos solicitudes. Mientras procesa los datos de la primera solicitud, puede alternar la ejecución con la segunda. Ambas tareas avanzan durante intervalos de tiempo superpuestos, aunque no necesariamente se ejecuten al mismo instante.[^1]

## Tipos de sistemas operativos

### SSOO de tiempo real

Los **sistemas operativos de tiempo real** son aquellos sistemas en los que los procesos *requieren de garantías de tiempo*. Los procesos para poder ejecutarse deben garantizar el haber tenido determinado tiempo de proceso antes de un *tiempo límite*[^2]. En términos amenos, los procesos deben realizarse en un espacio de tiempo restringido y limitado del mundo real.

Un ejemplo de estos sistemas es [**QNX**](https://qnx.software/en) utilizado en automóviles y equipos industriales, diseñado para ofrecer alta fiabilidad, estabilidad y respuestas rápidas ante eventos críticos.[^1]

### SSOO distribuidos

Los **sistemas operativos distribuidos** es un tipo de **sistema distribuido**. Se define un *sistema distribuido* como una colección de computadoras independientes que aparecen ante los usuarios del sistema como una única computadora.[^3]

Un ejemplo es [**Plan 9**](https://p9f.org/), un sistema operativo distribuido desarrollado por Bell Labs que permite acceder a recursos locales y remotos mediante una interfaz uniforme basada en archivos.[^1] Sin embargo, es habitual utilizar actualmente **Linux con Kubernetes**; donde *Linux* proporciona el sistema operativo y *Kubernetes* coordina contenedores en múltiples servidores, facilitando el despliegue, la escalabilidad y la administración de aplicaciones distribuidas.[^1]

### SSOO embebidos

Los **sistemas operativos embebidos** es un sistema operativo que se integra en lo que se conoce como **sistema embebido**. Un *sistema embebido* es un sistema digital diseñado para controlar, procesar, almacenar o comunicar información dentro de un dispositivo o aplicación específica. Su objetivo principal es ser confiable, autosuficiente y contener en sí mismo todas las capacidades de cómputo necesarias para su función, lo que permite operar con autonomía e independencia de otros sistemas.[^4]

Existen varias *distros* de Linux con enfoque en sistemas operativos embebidos y dispositivos IoT. Igualmente, está **Embedded Linux ([Yocto](https://www.yoctoproject.org/))**, un proyecto que permite crear distribuciones Linux personalizadas y optimizadas para dispositivos embebidos, adaptadas a los requisitos de hardware y software.[^1]

## Concepto esclavo y maestro en sistemas operativos

En ingeniería, la relación **maestro-esclavo** se refiere a la interacción entre dos sistemas en la que uno controla al otro. En algunos casos, un maestro controla un único sistema esclavo, pero en otros, varios sistemas esclavos son controlados por el mismo maestro. A veces, el maestro es un sistema diferente al esclavo, pero en ocasiones existen varios sistemas similares y uno de ellos se designa como maestro para centralizar el control externo (es decir, del usuario) del conjunto. También se utiliza para distinguir entre sistemas que solo emiten comandos (maestro) y aquellos que solo los reciben (esclavo).[^5]

> Debido a su asociación con la *esclavitud*, la terminología es objeto de controversia y en algunos casos se ha sustituido por términos alternativos.

## ¿Cómo instalar dos sistemas operativos en un mismo equipo (Linux y Windows)?.

Se utiliza **Dual Boot** (en español: *arranque dual*) y es una configuración informática que permite instalar dos sistemas operativos en un mismo equipo y elegir cuál ejecutar al encenderlo.[^1] Esta configuración permite instalar cada sistema operativo en una *partición independiente* del disco o medio de almacenamiento. Además configura un *gestor de arranque* (ej. **GRUB** o **Windows Boot Manager**). Y al encenderlo, se puede elegir el sistema operativo y el equipo inicia el sistema seleccionado.

| Ventajas | Desventajas  |
|----------|--------------|
| Permite utilizar las funciones de ambos sistemas operativos. | Requiere espacio adicional en el disco. |
| Ofrece acceso directo al hardware del equipo. | Una configuración incorrecta de las particiones puede provocar pérdida de datos. |
| No requiere ejecutar un sistema operativo con el rendimiento de una máquina virtual. | Las actualizaciones o modificaciones del gestor de arranque puede afectar el inicio de uno de los SSOO. |

Para instalar **Windows** y **Linux** mediante el *arranque dual* primero se debe verificar la compatibilidad del hardware, comprobar que exista suficiente espacio de almacenamiento y preparar memorias **Boot USB** con los instaladores de ambos sistemas operativos. Antes de modificar las particiones, es indispensable realizar una copia de seguridad de los datos importantes para prevenir posibles pérdidas de información. Se recomienda instalar Windows primero, utilizando el modo de arranque UEFI cuando sea compatible con el equipo. Posteriormente, se debe acceder al administrador de discos de Windows y reducir la partición principal para liberar espacio sin asignar, reservando preferentemente entre 30 y 50 GB como mínimo para una instalación básica de Linux. A continuación, se debe descargar una distribución de Linux, y crear una memoria USB de instalación mediante herramientas como **Rufus** o **balenaEtcher**.[^1]

Después, se inicia el equipo desde dicha memoria USB y se ejecuta el instalador de Linux, seleccionando la opción de instalarlo junto a Windows, si está disponible, o realizando un particionado manual para asignar el espacio libre al nuevo sistema operativo, sin eliminar ni modificar indebidamente las particiones existentes de Windows. Una vez finalizada la instalación, se debe configurar el gestor de arranque GRUB para permitir la selección entre Linux y Windows durante el inicio del equipo. En sistemas modernos, se recomienda utilizar el esquema de **particionado GPT** y el **firmware UEFI**, procurando que ambos sistemas operativos utilicen el mismo modo de arranque. Asimismo, si el disco está protegido mediante **BitLocker**, puede ser necesario suspender temporalmente su protección antes de realizar determinadas modificaciones y conservar la clave de recuperación.[^1]

Es fundamental preservar las particiones EFI, de recuperación y del sistema Windows para evitar errores de arranque o pérdida de datos. Finalmente, se debe reiniciar el equipo, comprobar que ambos sistemas operativos aparezcan en el menú de inicio y verificar que funcionen correctamente. En conclusión, el arranque dual constituye una solución eficiente para utilizar Linux y Windows en un mismo ordenador sin necesidad de desinstalar uno para ejecutar el otro; sin embargo, instalar primero Windows y después Linux suele simplificar la configuración del gestor de arranque y reducir los problemas de compatibilidad.[^1]

> Es posible instalar primero Linux y posteriormente Windows con el *arranque dual*; sin embargo, este orden no es el más recomendable, ya que, al instalar Windows después de Linux, el gestor de arranque de Windows puede modificar la configuración de inicio y dificultar el acceso directo a Linux. Para conservar ambos sistemas operativos, primero se debe realizar una copia de seguridad de los datos importantes y, si es necesario, reducir la partición de Linux mediante una herramienta compatible para liberar espacio en el disco. 
> 
> A continuación, se debe instalar Windows en el espacio disponible, evitando formatear, eliminar o modificar las particiones que contienen Linux y sus archivos de arranque. Una vez finalizada la instalación de Windows, se debe iniciar el equipo desde una memoria USB Live de Linux para reparar o restaurar el gestor de arranque GRUB y actualizar su configuración, de modo que detecte Windows y permita seleccionar cualquiera de los dos sistemas operativos al encender el ordenador. Finalmente, se debe reiniciar el equipo  verificar que ambos sistemas puedan iniciarse correctamente. 
> 
> En conclusión, instalar primero Linux y después Windows es técnicamente viable, pero puede requerir la reparación manual del gestor de arranque; por ello, se recomienda instalar primero Windows y posteriormente Linux para simplificar la configuración del arranque dual y reducir posibles inconvenientes técnicos.[^1]

## Referencias

[^1]: OpenAI. (2026). *ChatGPT*. URL: `https://chatgpt.com//`
[^2]: Gunnar Wolf, et al. (2015). *Fundamentos de Sistemas Operativos*. Universidad Nacional Autonóma de México.
[^3]: López F., Francisco de Asís. (2015). *Sistemas distribuidos*. Universidad Autónoma Metropolitana. URL: `http://dccd.cua.uam.mx/libros/archivos/03IXStream_sistemas_distribuidos.pdf`.
[^4]: Benitez B., Víctor H. (2024). *Introducción a los sistemas embebidos*. ResearchGate. DOI: `10.13140/RG.2.2.19561.51044`.
[^5]: Wikipedia, the free encyclopedia. (s.f.). *Master-slave (technology)*. URL: `https://en.wikipedia.org/wiki/Master%E2%80%93slave_(technology)`.