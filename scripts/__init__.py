from src.data_loader import load_data
import matplotlib.pyplot as plt

if __name__ == "__main__":
    file_paths = ["data/file1.xlsx", "data/file2.xlsx"]
    data = load_data(file_paths)

    # Plot example
    data['GHI'].hist()
    plt.title("GHI Distribution")
    plt.show()

