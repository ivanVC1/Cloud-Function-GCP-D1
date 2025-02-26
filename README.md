# 🚀 Cloud-Function-GCP-D1
Repositorio con el código del día 1

## 📌 Descripción
Esta **Cloud Function** se activa cuando se sube un archivo a **Cloud Storage** y registra los metadatos en **Cloud Logging**.

## 📁 Estructura del Proyecto
cloud-function-gcp-d1/ 
│── main.py # Código de la Cloud Function 
│── test_main.py # Pruebas unitarias con unittest 
│── requirements.txt # Dependencias 
│── README.md # Documentación


## 🛠️ Instalación y Configuración
1. **Clonar el repositorio**
   ---sh
   git clone https://github.com/ivanVC1/cloud-function-gcp-d1.git
   cd cloud-function-gcp-d1
   
2. **Instalar dependencias**
pip install -r requirements.txt

3. **Ejecutar pruebas**
python -m unittest test_main.py

## Para desplegar la función en GCP se usó

   gcloud functions deploy process_file --runtime python311 --trigger-event google.storage.object.finalize --trigger-resource my-secure-bucket-ivan1417 --entry-point process_file --region us-central1 --memory 256MB --timeout 60s

   en --memory se usaron 256mb porque el programa me daba error al usar menos.


## Diagrama de flujo

---

## **🔹 Explicación del Diagrama**
1️⃣ **Un usuario sube un archivo** a **Cloud Storage**.  
2️⃣ **Se genera un evento** en **Google Cloud Storage**, activando la **Cloud Function**.  
3️⃣ **La Cloud Function extrae los metadatos** del archivo:  
   - 📌 **Nombre**  
   - 📌 **Tamaño**  
   - 📌 **Tipo de contenido**  
4️⃣ **Los metadatos se registran en Cloud Logging**.  
5️⃣ **La función responde con un mensaje de éxito**.  

---


## 📌 Explicación:

  1. Un usuario sube un archivo a Cloud Storage
  2. Se activa la Cloud Function
  3. La función extrae los metadatos del archivo
  4. Se guarda un registro en Cloud Logging
  5. La función responde con un mensaje exitoso
