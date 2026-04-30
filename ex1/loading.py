import sys
import importlib

png_name = "matrix_analysis.png"

if __name__ == "__main__":
    try:
        pd = importlib.import_module("pandas")
        np = importlib.import_module("numpy")
        rq = importlib.import_module("requests")
        mbp = importlib.import_module("matplotlib")
    except ImportError:
        print("Erreur : Des modules sont manquants pour lancer la Matrice !")
        print("-> Pour installer avec pip, tapez : pip install -r requirements.txt")
        print("-> Pour installer avec Poetry, tapez : poetry install")
        sys.exit(1)

    print(f"""LOADING STATUS: Loading programs...
[OK] {pd.__name__} ({pd.__version__}) - Data manipulation ready
[OK] {np.__name__} ({np.__version__}) -  Numerical computation ready
[OK] {rq.__name__} ({rq.__version__}) - Network access ready
[OK] {mbp.__name__} ({mbp.__version__}) - Visualization ready
""")
    
    print("Analyzing Matrix data...")
    print("Processing 1000 data points...")
    
    random_number = np.random.randint(0, 2, 1000)
    df = pd.DataFrame(random_number, columns=["Matrix_Data"])

    print("Generating visualization...\n")
    plt = importlib.import_module("matplotlib.pyplot")
    plt.plot(df.cumsum())
    plt.savefig(png_name)
    plt.show()
    plt.close()

    print("Analyzis complete!")
    print(f"Results saved to: {png_name}")
    
    
    

# 1. Génère des fausses données "façon Matrix" en utilisant numpy
#    calcul (interdiction d'écrire les données à la main, doit s'agir de 
#    la source de votre DATASET).
# 2. Met ces données dans un tableau pandas.
# 3. Crée un graphique visuel avec matplotlib et le sauvegarde sous
#    le nom matrix_analysis.png.