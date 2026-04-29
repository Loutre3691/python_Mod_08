import sys
import importlib


if __name__ == "__main__":
    try:
        pd = importlib.import_module("pandas")
        np = importlib.import_module("numpy")
        rq = importlib.import_module("requests")
        mpb = importlib.import_module("matplotlib")
    except ImportError:
        print("Should show missing dependencies and installation instructions for pip and Poetry")
        sys.exit(1)

    print(f"""LOADING STATUS: Loading programs...
[OK] {pd.__name__} ({pd.__version__}) - Data manipulation ready
[OK] {np.__name__} ({np.__version__}) -  Numerical computation ready
[OK] {rq.__name__} ({rq.__version__}) - Network access ready
[OK] {mpb.__name__} ({mpb.__version__}) - Visualization ready
""")

# 1. Génère des fausses données "façon Matrix" en utilisant numpy
#    calcul (interdiction d'écrire les données à la main, doit s'agir de 
#    la source de votre DATASET).
# 2. Met ces données dans un tableau pandas.
# 3. Crée un graphique visuel avec matplotlib et le sauvegarde sous
#    le nom matrix_analysis.png.