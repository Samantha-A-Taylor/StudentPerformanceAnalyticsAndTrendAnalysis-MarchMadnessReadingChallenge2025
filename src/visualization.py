"""
visualization.py

Visualization utilities for student performance analytics.
"""

from pathlib import Path
import matplotlib.pyplot as plt
import pandas as pd


FIGURES_PATH = Path("outputs/figures")
FIGURES_PATH.mkdir(parents=True, exist_ok=True)


def plot_reading_trend(df: pd.DataFrame, student_id: int) -> None:
    """
    Plot reading minutes over time for a single student.
    """
    student_df = df[df["student_id"] == student_id]

    plt.figure()
    plt.plot(student_df["date"], student_df["reading_minutes"])
    plt.title(f"Reading Trend – Student {student_id}")
    plt.xlabel("Date")
    plt.ylabel("Reading Minutes")

    output_file = FIGURES_PATH / f"student_{student_id}_trend.png"
    plt.savefig(output_file)
    plt.close()
