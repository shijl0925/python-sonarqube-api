===========
api/metrics
===========

Get information on automatic metrics, and manage custom metrics.
----------------------------------------------------------------

Examples
--------

Search for metrics.::

    metrics = list(sonar.metrics.search_metrics())


List all available metric types.::

    metric_types = sonar.metrics.get_metrics_types()

