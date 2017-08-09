import matplotlib.gridspec as gridspec
import matplotlib.pyplot as plt


def use_subplot_spec(nrows, ncols, subplot_spec, fig=None, gs_out=False,
                     **kwargs):

    if fig is None:
        fig = plt.gcf()
    if subplot_spec is not None:
        gs = gridspec.GridSpecFromSubplotSpec(nrows, ncols,
                                              subplot_spec=subplot_spec,
                                              **kwargs)
    else:
        gs = gridspec.GridSpec(nrows, ncols, **kwargs)

    if gs_out:
        return gs

    return [fig.add_subplot(x) for x in gs]