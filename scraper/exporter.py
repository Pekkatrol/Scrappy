import pandas as pd

def export_to_csv(data, filename) -> None:
    """
    This function take a dictionnary and a filename, transform the dictionnary into a csv file with the filename.
    """
    df = pd.DataFrame(data)
    df.to_csv(filename, index=False)