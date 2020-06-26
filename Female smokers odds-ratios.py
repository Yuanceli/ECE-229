def get_odds_ratio_overall():
    '''
    :return:
    '''
    return 139 * (732-230) / (230 * (582-139))

def get_odds_ratio_by_age():
    '''
    :return:
    '''
    result = {
        "18-24": 2 * (61-1) / (1 * (55-2)),
        "25-34": 3 * (157-5) / (5 * (124-3)),
        "35-44": 14 * (121-7) / (7 * (109-14)),
        '45-54': 27 * (78-12) / (12 * (130-27)),
        '55-64': 51 * (121-40) / (40 * (115-51)),
        '65-74': 29 * (129-101) / (101 * (36-29))
    }

    return result
