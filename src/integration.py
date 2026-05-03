import pandas as pd
from typing import Any, Dict
from colorama import Fore
from src.file import load_data


def export_to_csv(filename: str = "reporte.csv") -> None:
    """Exporta los datos a un archivo CSV."""
    data = load_data()

    if not data:
        print(Fore.YELLOW + "No hay datos para exportar")
        return

    df = pd.DataFrame(data)
    df.to_csv(filename, index=False)

    print(Fore.GREEN + f" Reporte exportado a {filename}")


def generate_report(**filters: Dict[str, Any]):
    """Genera un reporte filtrado usando pandas."""
    data = load_data()

    if not data:
        print(Fore.YELLOW + "No hay datos disponibles")
        return

    df = pd.DataFrame(data)

    for key, value in filters.items():
        if key in df.columns:
            df = df[df[key].astype(str).str.contains(str(value), case=False)]

    if df.empty:
        print(Fore.RED + "No hay resultados")
        return

    print(df)
    return df