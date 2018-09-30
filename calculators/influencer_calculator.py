

def influence_level_calculation(cl_influence_level, lt_influence_level, st_influence_level, stp_influence_level,
                                cv_influence_level, sl_influence_level, pcode_influence_level, pcomm_influence_level):
    influence_level = closeness_to_github_project_owner(cl_influence_level) + \
                            long_time_interaction_with_the_project(lt_influence_level) + \
                            status_github(st_influence_level) + status_in_the_project(stp_influence_level) + \
                            content_value(cv_influence_level) + source_of_learning(sl_influence_level) + \
                            participation_with_code(pcode_influence_level) + \
                            participation_with_comments(pcomm_influence_level)
    return influence_level

def closeness_to_github_project_owner(cl_metric):
    cl_coeficient = 1.0505
    return cl_metric * cl_coeficient

def long_time_interaction_with_the_project(lt_metric):
    lt_coeficient = 2.3283
    return lt_metric * lt_coeficient

def status_github(st_metric):
    st_coeficient = 0.9671
    return st_metric * st_coeficient

def status_in_the_project(stp_metric):
    stp_coeficient = 2.2567
    return stp_metric * stp_coeficient

def content_value(cv_metric):
    cv_coeficient = 2.2443
    return cv_metric * cv_coeficient

def source_of_learning(sl_metric):
    sl_coeficient = 1.5007
    return sl_metric * sl_coeficient

def participation_with_code(pcode_metric):
    pcode_coeficient = 2.3392
    return pcode_metric * pcode_coeficient

def participation_with_comments(pcomm_metric):
    pcomm_coeficient = 1.8437
    return pcomm_metric * pcomm_coeficient

