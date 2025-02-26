import unittest
import json
from cloudevents.http import CloudEvent
from main import process_file

class TestCloudFunction(unittest.TestCase):
    """Pruebas unitarias para la Cloud Function"""

    def create_test_cloudevent(self, data):
        """Crea un evento CloudEvent simulado"""
        attributes = {
            "specversion": "1.0",
            "type": "google.cloud.storage.object.v1.finalized",
            "source": "//storage.googleapis.com/projects/_/buckets/my-secure-bucket-ivan1417",
            "id": "test-event-1234"
        }
        return CloudEvent(attributes, data)

    def test_process_file_success(self):
        """Prueba que la función procesa correctamente un archivo válido"""
        event_data = {
            "name": "archivo_prueba.txt",
            "size": "1024",
            "contentType": "text/plain"
        }

        cloud_event = self.create_test_cloudevent(event_data)
        result = process_file(cloud_event)
        self.assertIn("Archivo recibido: archivo_prueba.txt", result)

    def test_process_file_missing_fields(self):
        """Prueba que la función maneja datos incompletos"""
        event_data = {
            "name": "archivo_sin_tamaño.txt"
        }

        cloud_event = self.create_test_cloudevent(event_data)
        result = process_file(cloud_event)
        self.assertIn("Archivo recibido: archivo_sin_tamaño.txt", result)

    def test_process_file_error_handling(self):
        """Prueba que la función maneja excepciones correctamente"""
        result = process_file(None) #Enviar un evento invalido
        self.assertEqual(result, "Error: Evento inválido")

if __name__ == "__main__":
    unittest.main()
