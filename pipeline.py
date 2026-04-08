import pandas as pd

def transform(input_file: str, output_file: str) -> None:
    df = pd.read_csv(input_file)

    # Remove rows with missing values
    df = df.dropna()

    # Convert numeric columns safely
    df["quantity"] = df["quantity"].astype(float)
    df["price"] = df["price"].astype(float)

    # Add derived column
    df["total"] = df["quantity"] * df["price"]
    df["discount"] = df["total"] * 0.10

    df.to_csv(output_file, index=False)

if __name__ == "__main__":
    transform("input.csv", "output.csv")
    print("Pipeline finished. Wrote output.csv")