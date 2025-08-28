# checking if a input is blanced or not
def isValid(s: str) -> bool:
        l = []
        flag = False
        for ele in s:
            if ele in '{[(':
                l.append(ele)
            else:
                if ele ==']':
                    if ele == l[-1]:
                        flag = True
                    else:
                        flag =False
                        break
                elif ele ==')':
                    if ele == l[-1]:
                        flag = True
                    else:
                        flag =False
                        break
                if ele =='}':
                    if ele == l.pop():
                        flag = True
                    else:
                        flag =False
                        break
            
        return flag
isValid('{}')