====================
api/new_code_periods
====================

Manage New Code project settings.
-----------------------------------------------------------------------------------------------------------

Examples
--------

Set New Code default for all branches of the _project_ to be based on reference branch _branch_::

    sonar.new_code_periods.set("REFERENCE_BRANCH", project=project, value=branch)

For a specific branch _branch_ set New Code to be evaluated relatively to the previous version::

    sonar.new_code_periods.set("PREVIOUS_VERSION", project=project, branch=branch)

