============
api/settings
============

Manage settings.
----------------

Examples
--------

Update a setting value.::

    sonar.settings.update_setting_value(key='sonar.issues.defaultAssigneeLogin', value="kevin")

Remove a setting value.::

    sonar.settings.remove_setting_value(keys="sonar.issues.defaultAssigneeLogin")

List settings values.::

    setting_values = sonar.settings.get_settings_values(component="my_project",
                                                        keys="sonar.dbcleaner.daysBeforeDeletingClosedIssues")

List settings definitions.::

    settings_definitions = sonar.settings.get_settings_definitions(component="my_project")

