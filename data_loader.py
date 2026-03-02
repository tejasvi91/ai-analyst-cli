import pandas as pd


def load_csv(file_path: str) -> pd.DataFrame:
    """
    Load a CSV file into a pandas DataFrame.
    """
    try:
        df = pd.read_csv(file_path)
        return df
    except Exception as e:
        raise Exception(f"Error loading CSV file: {e}")


def get_basic_summary(df: pd.DataFrame) -> dict:
    """
    Generate a structured summary of the dataset.
    """
    summary = {
        "columns": list(df.columns),
        "shape": df.shape,
        "missing_values": df.isnull().sum().to_dict(),
        "numeric_summary": df.describe(include="all").to_dict()
    }

    return summary