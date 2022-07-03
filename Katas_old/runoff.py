def runoff(voters):
    vote_dict = {}
    for v in voters:
        vote_dict.setdefault(v[0], 0)
        vote_dict[v[0]] += 1
    if len(vote_dict) > 1 and min(vote_dict.values()) == max(vote_dict.values()):
        return None
    cand_for_win = [cand for cand, count in vote_dict.items() if count == max(vote_dict.values())]
    if len(cand_for_win) == 1 and vote_dict[cand_for_win[0]] / len(voters) > 0.5:
        return cand_for_win[0]

    cand_for_delete = [cand for cand, count in vote_dict.items() if count == min(vote_dict.values())]

    for v in voters:
        for cand in cand_for_delete:
            if cand in v:
                v.remove(cand)
        while v[0] not in vote_dict:
            v.remove(v[0])
        if not v:
            voters.remove(v)
    return runoff(voters)


voters = [['Frank Underwood', 'Abelt Dessler', 'Drake Luft', 'Lex Luthor', 'Daisuke Aramaki'],
          ['Abelt Dessler', 'Daisuke Aramaki', 'Drake Luft', 'Lex Luthor', 'Frank Underwood'],
          ['Lex Luthor', 'Frank Underwood', 'Daisuke Aramaki', 'Drake Luft', 'Abelt Dessler'],
          ['Drake Luft', 'Lex Luthor', 'Abelt Dessler', 'Frank Underwood', 'Daisuke Aramaki'],
          ['Drake Luft', 'Abelt Dessler', 'Daisuke Aramaki', 'Frank Underwood', 'Lex Luthor'],
          ['Abelt Dessler', 'Frank Underwood', 'Daisuke Aramaki', 'Drake Luft', 'Lex Luthor']]
print(runoff(voters))
