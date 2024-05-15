"""
This is a boilerplate pipeline 'data_processing'
generated using Kedro 0.19.3
"""

import polars as pl
import plotly.graph_objects as go

from .utils import get_explanation, get_funniness


def summarize_submissions(
    submissions_raw: pl.DataFrame,
) -> pl.DataFrame:
    """Add summaries to submissions data."""

    return submissions_raw

def plot_funniness(submissions_summaries: pl.DataFrame) -> go.Figure:
    """Plot funniness of jokes."""

    return None