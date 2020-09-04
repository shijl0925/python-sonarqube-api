============
api/settings
============

Manage settings.
----------------

Examples
--------

Update a setting value.::

    sonar.settings.update_setting_value(setting_key='sonar.issues.defaultAssigneeLogin', setting_value="kevin")

Remove a setting value.::

    sonar.settings.remove_setting_value(setting_keys="sonar.issues.defaultAssigneeLogin")

List settings values.::

    setting_values = sonar.settings.get_settings_values(component_key="my_project",
                                                        setting_keys="sonar.dbcleaner.daysBeforeDeletingClosedIssues")

List settings definitions.::

    settings_definitions = sonar.settings.get_settings_definitions(component_key="my_project")

