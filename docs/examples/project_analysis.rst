====================
api/project_analyses
====================

Manage project analyses.
________________________

Examples
--------

Create a project analysis event.Only event of category 'VERSION' and 'OTHER' can be created.::

    sonar.project_analyses.create_project_analysis_event(analysis="AXHAfesPdxfTzNWG9gDW", name='1.3.12')

Delete a project analysis event.Only event of category 'VERSION' and 'OTHER' can be deleted.::

    sonar.project_analyses.delete_project_analysis_event(event="AXQPuYYdjOKlq86mQnOV")

Delete a project analysis.::

    sonar.project_analyses.delete_project_analysis(analysis="AXLA7wQ9dxfTzNWGB_Su")

Search a project analyses and attached events.::

    project_analyses_and_events = sonar.project_analyses.search_project_analyses_and_events(project="my_project")


Set an analysis as the baseline of the New Code Period on a project or a long-lived branch. This manually set baseline overrides the `sonar.leak.period` setting.::

    sonar.project_analyses.set_analysis_as_baseline_on_project(project="my_project", analysis="AXHAfesPdxfTzNWG9gDW")


Unset any manually-set New Code Period baseline on a project or a long-lived branch. Unsetting a manual baseline restores the use of the `sonar.leak.period` setting.::


    sonar.project_analyses.unset_baseline_on_project(project="my_project")

Update a project analysis event. Only events of category 'VERSION' and 'OTHER' can be updated.::

    sonar.project_analyses.update_project_analysis_event(event="AXQPuvIBjOKlq86mQnOW", name="1.3.13")

