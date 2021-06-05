text = "X-DSPAM-Confidence:    0.8475";

ipos=text.find(':')
#print (ipos)
piece=text[ipos+1:]
#print (piece)
p2=piece.strip()
p3=float(piece)
print (p3)
