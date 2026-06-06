import os

def load_data(final_data):
    output_path = "data/processed_sales_data.csv"

    final_data.to_csv(
        output_path,
        index=False
    )

    print(f"\nTransformed data loaded successfully to: {output_path}")

    return output_path