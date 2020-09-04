==================
api/project_badges
==================

Generate badges based on quality gates or measures.
---------------------------------------------------

Examples
--------
Generate badge for project's measure as an SVG.::

    project_measures_badge = sonar.project_badges.generate_badge_for_project_measures("my_project",
                                                                                      metric='code_smells')
    with open("project_measures_badge.html", 'w') as f:
        f.write(project_measures_badge)

Generate badge for project's quality gate as an SVG.::

    quality_gate_badge = sonar.project_badges.generate_badge_for_project_quality_gate("my_project")
    with open("quality_gate_badge.html", 'w') as f:
        f.write(quality_gate_badge)

