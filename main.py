import logging
import functions_framework

# 📌 Esta función se activa cuando se sube un archivo a Cloud Storage
@functions_framework.cloud_event
def process_file(cloud_event):
    """Función que se activa cuando un archivo es subido a Cloud Storage.
       Extrae metadatos del archivo y los registra en Cloud Logging."""
    try:
        if cloud_event is None or not hasattr(cloud_event, 'data'): # 📌 Se usó esta validación porque daba error el código al venir un None además del cloud_event
            logging.warning("Evento recibido es None o no tiene datos válidos.") # 📌 Se uso logging.warning en lugar de error para que no detuviera la ejecuión del código
            return "Error: Evento inválido"

        # 📌 Extraer los metadatos del archivo
        data = cloud_event.data
        file_name = data.get("name", "desconocido")
        file_size = data.get("size", "desconocido")
        content_type = data.get("contentType", "desconocido")

        # 📌 Construye el mensaje de log
        log_message = f"Archivo recibido: {file_name}, Tamaño: {file_size} bytes, Tipo: {content_type}"
        logging.info(log_message)

        return log_message # 📌 Devuelve el mensaje como respuesta

    except Exception as e:
        logging.warning(f"Error procesando el archivo: {str(e)}") # 📌 Se uso logging.warning en lugar de error para que no detuviera la ejecuión del código
        return f"Error: {str(e)}"

