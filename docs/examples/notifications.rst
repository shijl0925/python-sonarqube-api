=================
api/notifications
=================

Manage notifications of the authenticated user.
-----------------------------------------------

Examples
--------

List notifications of the authenticated user.::

    user_notifications = sonar.notifications.get_user_notifications(login="kevin")

Add a notification for the authenticated user.::

    sonar.notifications.add_notification_for_user(login="kevin", type="CeReportTaskFailure")

or::

    sonar.notifications.add_notification_for_user(login="kevin", type="ChangesOnMyIssue", project="my_project")

Remove a notification for the authenticated user.::

    sonar.notifications.remove_notification_for_user(login="kevin", type="CeReportTaskFailure")

or::

    sonar.notifications.remove_notification_for_user(login="kevin", type="ChangesOnMyIssue", project="my_project")

