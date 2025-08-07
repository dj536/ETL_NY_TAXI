import requests
from pathlib import Path

output_dir = Path("data")
output_dir.mkdir(exist_ok=True)

urls = {
    "yellow_tripdata_2025-01.parquet": "https://d37ci6vzurychx.cloudfront.net/trip-data/yellow_tripdata_2025-01.parquet",
    "yellow_tripdata_2025-02.parquet": "https://d37ci6vzurychx.cloudfront.net/trip-data/yellow_tripdata_2025-02.parquet",
    "yellow_tripdata_2025-03.parquet": "https://d37ci6vzurychx.cloudfront.net/trip-data/yellow_tripdata_2025-03.parquet"
}

for filename, url in urls.items():
    print(f"Téléchargement de {filename}...")
    response = requests.get(url)
    file_path = output_dir / filename
    with open(file_path, "wb") as f:
        f.write(response.content)  
    print(f" {filename} téléchargé dans {file_path}")

print("Tous les fichiers ont été téléchargés avec succès.")
input("Appuyez sur Entrée pour fermer...")
