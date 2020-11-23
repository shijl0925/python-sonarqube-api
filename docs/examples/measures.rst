============
api/measures
============

Get components or children with specified measures.
---------------------------------------------------

Examples
--------

Return component with specified measures::

    component = sonar.measures.get_component_with_specified_measures(component="my_project",
                                                                     branch="develop",
                                                                     fields="metrics,periods",
                                                                     metricKeys="code_smells,bugs,vulnerabilities")


Navigate through components based on the chosen strategy with specified measures. The baseComponentId or the component parameter must be provided::

    component_tree = list(sonar.measures.get_component_tree_with_specified_measures(component_key="my_project",
                                                                               branch="develop",
                                                                               metricKeys="code_smells,bugs,vulnerabilities"))

Search measures history of a component::

    measures_history = list(sonar.measures.search_measures_history(component="my_project", branch="develop"))

