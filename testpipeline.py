import pandas as pd
from pipeline import transform

def test_transform_creates_total_column(tmp_path):
    input_file = tmp_path / "input.csv"
    output_file = tmp_path / "output.csv"

    input_file.write_text(
        "item,quantity,price\n"
        "apple,2,10\n"
        "banana,,5\n"
        "orange,3,7\n"
    )

    transform(str(input_file), str(output_file))

    df = pd.read_csv(output_file)

    assert "total" in df.columns
    assert len(df) == 2
    assert df["total"].tolist() == [20.0, 21.0]