from datetime import datetime
agora = datetime.now()
print("%d:%d"%(agora.hour,agora.minute))
if agora.hour>22:
    print("Boa noite e até amanhã!")
else:
    print("Ainda está cedo!")
