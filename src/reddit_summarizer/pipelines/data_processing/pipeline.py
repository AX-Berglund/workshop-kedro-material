"""
This is a boilerplate pipeline 'data_processing'
generated using Kedro 0.19.3
"""

from kedro.pipeline import Pipeline, pipeline, node

from .nodes import summarize_submissions, plot_funniness


def create_pipeline(**kwargs) -> Pipeline:
    return pipeline(
        [
            node(
                func=summarize_submissions,
                inputs=["submissions-raw"],
                outputs="submissions-summaries",
                name="summarize",
            ),
            node(
                func=plot_funniness,
                inputs=["submissions-summaries"],
                outputs="funniness-plot",
                name="plot_funniness"
            ),
        ]
    )
