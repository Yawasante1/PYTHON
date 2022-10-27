def sales(q):
    if 50<=q<=100:
        return q*100
    elif q>100:
        return q*100+50
    else:
        return ("Sacked, you lazy Sales Person")
sales(11)