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
        print("Error : Some modules are missing to launch the Matrix!")
        print("-> To install with pip, type : pip install -r requirements.txt")
        print("-> To install with poetry, type : poetry install")
        sys.exit(1)

    print(f"""LOADING STATUS: Loading programs...\n
Checking dependencies:
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

    print("Analysis complete!")
    print(f"Results saved to: {png_name}")
