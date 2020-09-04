===================
api/qualityprofiles
===================

Manage quality profiles.
________________________

Examples
--------

Activate a rule for a given quality profile.::

    sonar.qualityprofiles.activate_rule_for_quality_profile(profile_key="AXQkbph7jOKlq86mQnys",
                                                            rule_key="squid:S2204",
                                                            severity="BLOCKER")

Search quality profiles::

    qualityprofiles = sonar.qualityprofiles.search_quality_profiles(language="java")

Select the default profile for a given language.::

    sonar.qualityprofiles.set_default_quality_profile(language="java", profile_name="FindBugs&P3C")

Associate a project with a quality profile.::

    sonar.qualityprofiles.associate_project_with_quality_profile(project="my_project",
                                                                 language="java",
                                                                 profile_name="FindBugs&P3C")

Remove a project's association with a quality profile.::

    sonar.qualityprofiles.remove_project_associate_with_quality_profile(project="my_project",
                                                                        language="java",
                                                                        profile_name="FindBugs&P3C")

Backup a quality profile in XML form.::

    quality_profile = sonar.qualityprofiles.backup_quality_profile(language="java",
                                                                   profile_name="FindBugs&Security&P3C")
    with open("quality_profile.xml", "w") as f:
        f.write(quality_profile)

Change a quality profile's parent.::

    sonar.qualityprofiles.change_parent_of_quality_profile(parent_profile_name="Sonar way",
                                                           language="java",
                                                           profile_name="FindBugs&P3C")


Get the history of changes on a quality profile: rule activation/deactivation, change in parameters/severity. Events are ordered by date in descending order (most recent first).::

    change_history = sonar.qualityprofiles.get_history_of_changes_on_quality_profile(language="java",
                                                                                     profile_name="FindBugs")

Copy a quality profile.::

    sonar.qualityprofiles.copy_quality_profile(profile_key="AW7vWZ7X6yOn6l1iXsR_", new_profile_name="FindBugs&P3C-test")

Create a quality profile.::

    sonar.qualityprofiles.create_quality_profile(language="java", profile_name="FindBugs&P3C-test")

Deactivate a rule on a quality profile.::

    sonar.qualityprofiles.deactivate_rule_on_quality_profile(profile_key="AXQkbph7jOKlq86mQnys",
                                                             rule_key="squid:S2204")

Delete a quality profile and all its descendants.::

    sonar.qualityprofiles.delete_quality_profile(language="java", profile_name="FindBugs-test")

Export a quality profile.::

    quality_profile = sonar.qualityprofiles.export_quality_profile(exporter_key="pmd", language="java", profile_name="FindBugs&P3C")
    with open("quality_profile.xml", "w") as f:
        f.write(quality_profile)

Lists available profile export formats.::

    supported_exporters = sonar.qualityprofiles.get_supported_exporters()

List supported importers.::

    supported_importers = sonar.qualityprofiles.get_supported_importers()

Show a quality profile's ancestors and children.::

    quality_profile = sonar.qualityprofiles.show_quality_profile(language="java", profile_name="FindBugs")

List projects with their association status regarding a quality profile::

    projects = sonar.qualityprofiles.get_projects_associate_with_quality_profile(profile_key="AW7vWZ7X6yOn6l1iXsR_")

Rename a quality profile.::

    sonar.qualityprofiles.rename_quality_profile(profile_key="AXQkj1lxjOKlq86mQny7", profile_name="FindBugs&P3C-test")

Restore a quality profile using an XML file. The restored profile name is taken from the backup file, so if a profile with the same name and language already exists, it will be overwritten.::

    with open("backup.xml", "r") as f:
        sonar.qualityprofiles.restore_quality_profile(backup=f.read())

