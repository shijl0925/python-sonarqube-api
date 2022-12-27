================
api/qualitygates
================

Manage quality gates, including conditions and project association.
-------------------------------------------------------------------

Examples
--------

Copy a Quality Gate.::

    sonar.qualitygates.copy_quality_gate(id=2, name="Sonar Way (for test)")

Delete a Quality Gate.::

    sonar.qualitygates.delete_quality_gate(5)

Create a Quality Gate.::

    sonar.qualitygates.create_quality_gate(name="Sonar Way (for test)")

Rename a Quality Gate.::

    sonar.qualitygates.rename_quality_gate(id=6, name="Sonar Way (for Test)")

Add a new condition to a quality gate.::

    sonar.qualitygates.create_condition_to_quality_gate(gateId=6, metric="new_coverage", error="80", op="LT")

Delete a condition from a quality gate.::

    sonar.qualitygates.delete_condition_from_quality_gate(id=33)

Update a condition attached to a quality gate.::

    sonar.qualitygates.update_condition_to_quality_gate(id=35, metric="new_coverage", error="60", op="LT")

Search for projects associated (or not) to a quality gate.::

    projects = sonar.qualitygates.get_qualitygate_projects(gateId=2)

Set a quality gate as the default quality gate.::

    sonar.qualitygates.set_default_qualitygate(2)

Get the quality gate status of a project::

    qualitygates_status = sonar.qualitygates.get_project_qualitygates_status(projectKey="my_project", branch="master")

Get a list of quality gates::

    quality_gates = sonar.qualitygates.get_quality_gates()

Associate a project to a quality gate.::

    sonar.qualitygates.select_quality_gate_for_project(projectKey="my_project", gateName="MyJavaGate827")

Remove the association of a project from a quality gate.::

    sonar.qualitygates.remove_project_from_quality_gate(projectKey="my_project")

Display the details of a quality gate.::

    qualitygate1 = sonar.qualitygates.show_quality_gate(name='Sonar Way (for Test)')

or::

    qualitygate2 = sonar.qualitygates.show_quality_gate(name="Sonar Way (for Test)")

Get the quality gate of a project.::

    quality_gate = sonar.qualitygates.get_quality_gate_of_project(project="my_project")

