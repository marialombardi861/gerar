import geojson
import os

def filter_basilicata_communes_in_folder(input_folder, output_folder):
    # Crea la cartella di output se non esiste
    os.makedirs(output_folder, exist_ok=True)
    
    # Itera su tutti i file nella cartella di input
    for filename in os.listdir(input_folder):
        if filename.endswith('.geojson'):  # Considera solo i file GeoJSON
            input_path = os.path.join(input_folder, filename)
            output_path = os.path.join(output_folder, f"filtered_{filename}")
            
            # Carica il file GeoJSON di input
            with open(input_path, 'r', encoding='utf-8') as f:
                data = geojson.load(f)
            
            # Filtra le feature che appartengono alla regione Basilicata
            filtered_features = [
                feature for feature in data["features"]
                if feature["properties"].get("reg_name") == "Basilicata"
            ]
            
            # Crea un nuovo oggetto GeoJSON con le feature filtrate
            filtered_data = geojson.FeatureCollection(filtered_features)
            
            # Salva il risultato in un nuovo file GeoJSON
            with open(output_path, 'w', encoding='utf-8') as f:
                geojson.dump(filtered_data, f, indent=2)
            
            print(f"File filtrato salvato in: {output_path}")

# Esempio di utilizzo
input_folder = 'MeteoAnalytics\src\static\js'
output_folder = 'cartella_output_geojson'
filter_basilicata_communes_in_folder(input_folder, output_folder)
