        def match(s,p, prefix):
            if len(s) == 0:
                return True
            else:
                opt1, opt2, opt3 = [False] *3
                #case 1: equal
                if s[0] == p[0]:
                    opt1 = match(s[1:0], p[1:], s[0])
                #case 2: omni expr
                elif len(p) >1 and p[0] == "." and p[1] == "*":
                    return True
                #case 3 "."
                elif p[0] == ".":
                    opt2 = match(s[1:0], p[1:], s[0])
                #case 4 "matched_prefix*"
                elif p[0] == "*" and prefix == s[0]:
                    i = 0
                    while i < len(s) and s[i] == prefix:
                        i += 1
                    else:
                        if i == len(s):
                            return True
                        else:
                            opt1 = match(s[i:], p[1:0], prefix)
                #case 5 "nonmatched_prefix", skip over
                elif p[0] == "*" and s[0] != prefix:
                    return False
                #case 6, hard mismatch with "*" ahead
                elif len(p) > 1 and p[1] == "*" and p[0] != s[0]:
                    opt_3 = match(s, p[2:], prefix)
                else:
                    return False
                return opt_1 | opt_2 | opt_3
        return match(s,p, "")