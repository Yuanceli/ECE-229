def get_ML_seq(seq,plist):
    '''
    Find the maximum likelihood solution for this sequence amoung the given dictionaries
    '''
    assert isinstance(seq, str)
    assert len(seq) > 0
    assert isinstance(plist, list)
    for item in plist:
        assert isinstance(item, dict)
        assert 0.999 <= sum(item.values()) <= 1.001
    
    ML_value = 0
    ML_dict = dict()
    
    for pnum, p in enumerate(plist):
        likelihood = [0 for ch in seq]
        for i, _ in enumerate(seq):
            if seq[0:(i+1)] in p.keys():
                likelihood[i] = p[seq[0:(i+1)]]
            for j in range(1, i+1):
                if likelihood[j-1] == 0:
                    continue
                if seq[j:(i+1)] not in p.keys():
                    continue
                likelihood[i] += likelihood[j-1] * p[seq[j:(i+1)]]
        if likelihood[len(seq)-1] > ML_value:
            ML_dict = p
            ML_value = likelihood[len(seq)-1]
        print(p, likelihood[len(seq)-1])
             
    assert ML_value > 0
    return ML_dict
    