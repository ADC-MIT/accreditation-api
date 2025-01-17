INSERT INTO institutes (
    id, institute_code, name, type, year_of_establishment, ownership_status, 
    affiliating_university_name, affiliating_university_address, vision, mission, 
    other_academic_institute_ids, programs_offered, programs_considered, 
    head_of_institute_id, nba_coordinator_id
) VALUES (
    $id, $institute_code, $name, $type, $year_of_establishment, $ownership_status, 
    $affiliating_university_name, $affiliating_university_address, $vision, $mission, 
    $other_academic_institute_ids, $programs_offered, $programs_considered, 
    $head_of_institute_id, $nba_coordinator_id
);