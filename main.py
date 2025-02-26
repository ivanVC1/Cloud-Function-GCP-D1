import logging
import functions_framework

@functions_framework.cloud_event
def process_file(cloud_event):
    """Función Cloud Function activada por la subida de archivos a Cloud Storage."""
    try:
        if cloud_event is None or not hasattr(cloud_event, 'data'):
            logging.warning("Evento recibido es None o no tiene datos válidos.")
            return "Error: Evento inválido"

        data = cloud_event.data
        file_name = data.get("name", "desconocido")
        file_size = data.get("size", "desconocido")
        content_type = data.get("contentType", "desconocido")

        log_message = f"Archivo recibido: {file_name}, Tamaño: {file_size} bytes, Tipo: {content_type}"
        logging.info(log_message)

        return log_message

    except Exception as e:
        logging.warning(f"Error procesando el archivo: {str(e)}")
        return f"Error: {str(e)}"

