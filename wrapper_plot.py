import pandas as pd
import matplotlib as ml


def getting_series_plot(
        x: pd.Series,
        y: pd.Series,
        axes: ml.axes._subplots,
        xlabel: str,
        ylabel: str,
        xticks_grid: int=0,
        color: str = None,
        title: str = None,
        plot_label:
        str = None,
        marker: str = None
):
    axes.plot(x,y, color=color, marker=marker, label=plot_label)
    if xticks_grid >0:
        axes.set_xticks(list(range(x.min(), x.max()+1, xticks_grid)))
    axes.set_xlabel(xlabel)
    axes.set_ylabel(ylabel)
    if title:
        axes.set_title(title)
    if plot_label:
        lines, labels = axes.get_legend_handles_labels()
        axes.legend(lines, labels, loc='best')
    return axes
