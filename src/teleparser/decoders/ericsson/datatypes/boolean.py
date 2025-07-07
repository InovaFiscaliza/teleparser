from .primitives import Bool


class RerountingIndicator(Bool):
    """Rerouting Indicator

    This parameter indicates if the call has been rerouted
    (for example a new B-number analysis has been performed)
    by the exchange where the charging data is output. This
    field is output only for ISOCODE or PACKED postprocessing
    purposes.
    """
