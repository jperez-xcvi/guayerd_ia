# programa: leer_markdown.py
# Descripción: Lee el archivo README.md y permite al usuario elegir un capítulo (##) para visualizar su contenido.

def leer_markdown(ruta_archivo):
    """Lee el archivo markdown y devuelve su contenido línea por línea."""
    with open(ruta_archivo, 'r', encoding='utf-8') as archivo:
        return archivo.readlines()

def obtener_capitulos(lineas):
    """Devuelve un diccionario con los títulos de nivel 2 (##) y su contenido."""
    capitulos = {}
    titulo_actual = None
    contenido_actual = []

    for linea in lineas:
        if linea.startswith("## "):
            # Si ya había un capítulo previo, lo guardamos antes de iniciar el nuevo
            if titulo_actual:
                capitulos[titulo_actual] = "".join(contenido_actual).strip()
                contenido_actual = []
            titulo_actual = linea.strip().replace("## ", "")
        elif titulo_actual:
            contenido_actual.append(linea)

    # Guarda el último capítulo
    if titulo_actual:
        capitulos[titulo_actual] = "".join(contenido_actual).strip()

    return capitulos

def mostrar_menu(capitulos):
    """Muestra el menú de capítulos disponibles."""
    print("\nCapítulos disponibles:\n")
    for i, capitulo in enumerate(capitulos.keys(), 1):
        print(f"{i}. {capitulo}")
    print(f"{len(capitulos) + 1}. Salir")

def main():
    print("👋 Bienvenido al lector de capítulos del archivo Documentacion.md 📘")

    ruta = "docs/Documentacion.md"

    try:
        lineas = leer_markdown(ruta)
        capitulos = obtener_capitulos(lineas)

        if not capitulos:
            print("⚠️ No se encontraron capítulos (##) en el archivo.")
            return

        while True:
            mostrar_menu(capitulos)
            opcion = input("\nSeleccione un capítulo por número: ")

            try:
                opcion = int(opcion)
            except ValueError:
                print("❌ Por favor ingrese un número válido.\n")
                continue

            if opcion == len(capitulos) + 1:
                print("\n👋 Gracias por usar el lector de Markdown. ¡Hasta pronto!")
                break
            elif 1 <= opcion <= len(capitulos):
                titulo = list(capitulos.keys())[opcion - 1]
                print(f"\n--- {titulo} ---\n")
                print(capitulos[titulo])
                print("\n" + "-" * 50 + "\n")
            else:
                print("⚠️ Opción fuera de rango.\n")

    except FileNotFoundError:
        print("❌ No se encontró el archivo README.md en el directorio actual.")

if __name__ == "__main__":
    main()
