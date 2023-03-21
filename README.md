# Whasapmasivo

El codigo del programa se encuentra en el archivo "interfaz.py".

Lo que hace este software es mediante enviar mensajes masivos a distintos numeros de de Wathsapp.
se diseño para una empresa de depilacion definitiva con el fin de enviar recordatorios para los turnos.

el programa tiene un boton que al accionarlo automaticamente enviara los mensajes, previo a eso.
el usuario en la planilla de calculos "libro1.csv" el usuario tendra que poner:
el nombre y apellido del ciente,el numero de telefono, el mensaje y en este caso el horario en su perpetivas columnas.
hay una columna llamada "Mensaje Completo" que su funcion es concatenar el texto que aprece en "Mensaje" y "Horario".
el programa en este caso tomara como referencia la columna "Mensaje completo" para enviar el mensaje.
De esta manera se podra hacer un mensaje personalizado para cada cliente o un mensaje mas general.

Una vez que se hallan hecho los cambios en las planilas de calculo, abrimo el software y le damos al boton de enviar mensaje.
automaticamente entrara a la pagina de Whattsap web y enviara mensaje el mensaje a cada cliente.
el tiempo que tarda el mensaje puede variar dependiendo de la computadora, en este caso tarda entre 20 y 30 segundos.
