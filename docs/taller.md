# Taller - Métodos HTTP y Códigos de Estado

Identificar los principales métodos HTTP y los códigos de respuesta utilizados en servidores y APIs REST.

## Métodos HTTP

Complete la tabla consultando la función de cada método.

### 📋 Métodos HTTP - Completos

| Método  | Función                                                                                                | Ejemplo                                                 |
| ------- | ------------------------------------------------------------------------------------------------------ | ------------------------------------------------------- |
| GET     | Obtiene o consulta información del servidor. Es de solo lectura y no modifica datos.                   | `GET /api/productos`<br>`GET /api/usuarios/2`           |
| POST    | Crea o registra nuevos datos o recursos en el servidor. Envía información en el cuerpo de la petición. | `POST /api/productos`<br>`Body: {"nombre": "Lápiz", "cantidad": 30}` |
| PUT     | Actualiza o modifica un recurso existente. Se envía el recurso completo con todos los datos.           | `PUT /api/productos/5`<br>`Body: {"nombre": "Lápiz", "cantidad": 40}` |
| PATCH   | Actualiza parcialmente un recurso. Solo se envían los campos que se quieren modificar.                 | `PATCH /api/productos/5`<br>`Body: {"cantidad": 45}`    |
| DELETE  | Elimina un recurso o dato específico del servidor.                                                     | `DELETE /api/productos/5`                              |
| OPTIONS | Consulta al servidor qué métodos y operaciones están permitidos en una ruta.                           | `OPTIONS /api/productos`                                |
| HEAD    | Igual que GET, pero solo devuelve los encabezados, sin el contenido de la respuesta.                   | `HEAD /api/productos`                                   |
| TRACE   | Realiza una prueba de ruta hasta el recurso, para ver el camino que sigue la petición.                 | `TRACE /api/productos`                                  |
| CONNECT | Establece una conexión de red (generalmente para usar túneles con SSL).                                | `CONNECT ejemplo.com:443`                               |

### 📋 Códigos de Estado HTTP - Completos

| Código | Nombre                       | Significado                                                                 |
| ------ | ---------------------------- | ---------------------------------------------------------------------------- |
| 100    | Continue                     | La petición fue recibida y puede continuar enviando el resto de los datos.   |
| 101    | Switching Protocols          | El servidor acepta cambiar el protocolo según lo solicitado por el cliente. |
| 200    | OK                           | La solicitud se procesó correctamente y devuelve el resultado esperado.      |
| 201    | Created                      | Se creó un nuevo recurso de forma exitosa en el servidor.                   |
| 202    | Accepted                     | La solicitud fue aceptada, pero aún no se ha procesado (está pendiente).    |
| 203    | Non-Authoritative Information| La información devuelta proviene de una copia o caché, no del servidor original. |
| 204    | No Content                   | Éxito en la solicitud, pero no hay contenido para devolver en la respuesta.  |
| 205    | Reset Content                | Éxito, y se debe reiniciar el formulario o vista del cliente.                |
| 206    | Partial Content              | Se envió solo una parte del contenido solicitado (para descargas divididas). |
| 300    | Multiple Choices             | Hay varias opciones para el recurso solicitado, el usuario debe elegir una.  |
| 301    | Moved Permanently            | El recurso se movió de forma permanente a una nueva URL.                     |
| 302    | Found                        | El recurso está temporalmente en otra ubicación.                             |
| 303    | See Other                    | Redirecciona a otra URL con un método GET.                                   |
| 304    | Not Modified                 | El recurso no ha cambiado desde la última solicitud, se puede usar la versión guardada. |
| 305    | Use Proxy                    | Se debe acceder al recurso a través de un proxy específico.                   |
| 307    | Temporary Redirect           | Redirección temporal, manteniendo el método HTTP original.                   |
| 308    | Permanent Redirect           | Redirección permanente, manteniendo el método HTTP original.                 |
| 400    | Bad Request                  | La solicitud tiene errores de sintaxis o datos inválidos, no se puede procesar. |
| 401    | Unauthorized                 | Falta autenticación: el usuario no está identificado o le faltan credenciales. |
| 402    | Payment Required             | Código reservado para uso futuro (pagos requeridos).                         |
| 403    | Forbidden                    | El usuario está identificado, pero no tiene permisos para realizar esa acción. |
| 404    | Not Found                    | El recurso o la ruta solicitada no existe en el servidor.                    |
| 405    | Method Not Allowed           | El método usado (GET, POST, etc.) no está permitido para esa ruta.            |
| 406    | Not Acceptable               | El formato de datos solicitado no es soportado por el servidor.              |
| 407    | Proxy Authentication Required| Se requiere autenticación para acceder a través del proxy.                   |
| 408    | Request Timeout              | El servidor tardó demasiado en recibir la solicitud y se canceló.            |
| 409    | Conflict                     | Hay un conflicto en los datos enviados (ej: nombre duplicado).                |
| 410    | Gone                         | El recurso existía antes, pero ya no está disponible y no volverá.           |
| 411    | Length Required              | Falta el encabezado `Content-Length` necesario para procesar la petición.    |
| 412    | Precondition Failed          | Una condición previa enviada en la petición no se cumple.                    |
| 413    | Payload Too Large            | Los datos enviados son demasiado grandes para ser procesados.                |
| 414    | URI Too Long                 | La dirección URL solicitada es demasiado larga.                              |
| 415    | Unsupported Media Type       | El formato de los datos enviados no es soportado por el servidor.            |
| 416    | Range Not Satisfiable        | El rango de datos solicitado no es válido o no existe.                       |
| 417    | Expectation Failed           | La expectativa indicada en la solicitud no puede ser cumplida.                |
| 429    | Too Many Requests            | Se han enviado demasiadas peticiones en poco tiempo (límite excedido).       |
| 500    | Internal Server Error        | Ocurrió un error inesperado dentro del servidor al procesar la solicitud.     |
| 501    | Not Implemented              | La función o método solicitado aún no está implementado en el servidor.       |
| 502    | Bad Gateway                  | El servidor actuó de intermediario y recibió una respuesta inválida.        |
| 503    | Service Unavailable          | El servidor está temporalmente fuera de servicio o sobrecargado.             |
| 504    | Gateway Timeout              | El servidor intermediario no recibió respuesta a tiempo del servidor final.  |
| 505    | HTTP Version Not Supported   | La versión del protocolo HTTP usada no es soportada.                         |
