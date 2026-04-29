import pandas as pd
from colorama import Fore
from file import load_data


def export_to_csv(filename="reporte.csv"):
    data = load_data()

    if not data:
        print(Fore.YELLOW + "No hay datos para exportar")
        return

    df = pd.DataFrame(data)
    df.to_csv(filename, index=False)

    print(Fore.GREEN + f"✔ Reporte exportado correctamente a {filename}")


# Uso de **kwargs (REQUISITO)
def generate_report(**filters):
    data = load_data()

    if not data:
        print(Fore.YELLOW + "No hay datos disponibles")
        return

    df = pd.DataFrame(data)

    # Aplicar filtros dinámicos
    for key, value in filters.items():
        if key in df.columns:
            df = df[df[key].astype(str).str.contains(str(value), case=False)]

    if df.empty:
        print(Fore.RED + "No hay resultados con esos filtros")
        return

    print(Fore.CYAN + "\n--- REPORTE FILTRADO ---")
    print(df)

    return df