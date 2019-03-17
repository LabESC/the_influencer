

def user_influence_level_calculation_complete(user, uses_closeness, uses_long_time, uses_status, uses_project_status,
                                              uses_content_value, uses_source, uses_participation_code,
                                              uses_participation_comment):
    closeness = 0.0
    long_time = 0.0
    status = 0.0
    project_status = 0.0
    content_value = 0.0
    source_of_learning = 0.0
    participation_code = 0.0
    participation_comment = 0.0

    if uses_closeness:
        closeness = project_closeness_to_github_project_owner(user.user_cl_influence_metric)

    if uses_long_time:
        long_time = project_long_time_interaction_with_the_project(user.user_lt_influence_metric)

    if uses_status:
        status = status_github(user.user_st_influence_metric)

    if uses_project_status:
        project_status = project_status_in_the_project(user.user_stp_influence_metric)

    if uses_content_value:
        content_value = project_content_value(user.user_cv_influence_metric)

    if uses_source:
        source_of_learning = project_source_of_learning(user.user_sl_influence_metric)

    if uses_participation_code:
        participation_code = project_participation_with_code(user.user_pcode_influence_metric)

    if uses_participation_comment:
        participation_comment = project_participation_with_comments(user.user_pcomm_influence_metric)

    influence_level = closeness + long_time + status + project_status + content_value + source_of_learning + \
                      participation_code + participation_comment

    return round(influence_level, 5)

def project_closeness_to_github_project_owner(cl_metric):
    cl_coeficient = 1.0505

    return float(cl_metric) * cl_coeficient

def project_long_time_interaction_with_the_project(lt_metric):
    lt_coeficient = 2.3283

    return float(lt_metric) * lt_coeficient

def status_github(st_metric):
    st_coeficient = 0.9671

    return float(st_metric) * st_coeficient

def project_status_in_the_project(stp_metric):
    stp_coeficient = 2.2567

    return float(stp_metric) * stp_coeficient

def project_content_value(cv_metric):
    cv_coeficient = 2.2443

    return float(cv_metric) * cv_coeficient

def project_source_of_learning(sl_metric):
    sl_coeficient = 1.5007

    return float(sl_metric) * sl_coeficient

def project_participation_with_code(pcode_metric):
    pcode_coeficient = 2.3392

    return float(pcode_metric) * pcode_coeficient

def project_participation_with_comments(pcomm_metric):
    pcomm_coeficient = 1.8437

    return float(pcomm_metric) * pcomm_coeficient

def ecosystem_influence_level_calculation(ecosystem, user, old_influence):
    influence_level = round((user.ecosystem_influence_level + old_influence) - (status_github(user.user_st_influence_metric) / ecosystem.total_ecosystem_influence_later_standarization),5)

    return round(influence_level, 5)

