============
api/plugins
============

Manage the plugins on the server, including installing, uninstalling, and upgrading.
------------------------------------------------------------------------------------

Examples
--------

Get the list of all the plugins available for installation on the SonarQube instance, sorted by plugin name.::

    plugins = sonar.plugins.get_available_plugins()

Cancels any operation pending on any plugin (install, update or uninstall).::

    sonar.plugins.cancel_operation_pending_plugins()

Installs the latest version of a plugin specified by its key.::

    sonar.plugins.install_plugin(key="typescript")

Get the list of all the plugins installed on the SonarQube instance, sorted by plugin name.::

    plugins = sonar.plugins.get_installed_plugins()

Get the list of plugins which will either be installed or removed at the next startup of the SonarQube instance, sorted by plugin name.::

    plugins = sonar.plugins.get_pending_plugins()

Uninstalls the plugin specified by its key.::

    sonar.plugins.install_plugin(key="typescript")

Updates a plugin specified by its key to the latest version compatible with the SonarQube instance. Plugin information is retrieved from Update Center.::

    sonar.plugins.install_plugin(key="typescript")


Lists plugins installed on the SonarQube instance for which at least one newer version is available, sorted by plugin name.::

    plugins = sonar.plugins.get_available_update_plugins()

