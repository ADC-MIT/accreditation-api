INSERT INTO faculty_sponsored_research_projects_consultancy_work_institute_seed_money (
    faculty_id,
    name_of_principal_investigator,
    name_of_co_principal_investigator,
    department_id,
    project_title,
    name_of_funding_agency,
    duration_of_project,
    amount_inr,
    outcomes
) VALUES (
    $faculty_id,
    $name_of_principal_investigator,
    $name_of_co_principal_investigator,
    $department_id,
    $project_title,
    $name_of_funding_agency,
    $duration_of_project,
    $amount_inr,
    $outcomes
);