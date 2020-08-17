import Tkinter as tk
import requests

class Example(tk.Frame):
    def __init__(self, parent):
        tk.Frame.__init__(self, parent)
        self.ticker = tk.Text(height=1, wrap="none")
        self.ticker.pack(side="top", fill="x")

        # Collect the data from the APIs: Data is coming from ThingSpeak, originally sourced from Yahoo Finance
        api_request = requests.get("https://api.thingspeak.com/apps/thinghttp/send_request?api_key=80Z9HLIBHGPTA6AI")
        EW = round(float(api_request.content),2)
        api_request = requests.get("https://api.thingspeak.com/apps/thinghttp/send_request?api_key=NNFPQR3F8BMWUR8T")
        EWClose = round(float(api_request.content), 2)
        api_request = requests.get("https://api.thingspeak.com/apps/thinghttp/send_request?api_key=CSNFIT36WLIY9ASN")
        A = round(float(api_request.content),2)
        api_request = requests.get("https://api.thingspeak.com/apps/thinghttp/send_request?api_key=772X95SUNGQ0UDDN")
        AClose = round(float(api_request.content), 2)
        api_request = requests.get("https://api.thingspeak.com/apps/thinghttp/send_request?api_key=B4FJXCVARH1F3FFU")
        REGN = round(float(api_request.content),2)
        api_request = requests.get("https://api.thingspeak.com/apps/thinghttp/send_request?api_key=6E7MAONJSPLFFAHF")
        REGNClose = round(float(api_request.content), 2)
        api_request = requests.get("https://api.thingspeak.com/apps/thinghttp/send_request?api_key=QK7UFLZ6W8UO5V7M")
        UHS = round(float(api_request.content),2)
        api_request = requests.get("https://api.thingspeak.com/apps/thinghttp/send_request?api_key=YMOT63HNOI7UDLAL")
        UHSClose = round(float(api_request.content), 2)
        api_request = requests.get("https://api.thingspeak.com/apps/thinghttp/send_request?api_key=25I56AD4GYNKPGW2")
        MRK = round(float(api_request.content),2)
        api_request = requests.get("https://api.thingspeak.com/apps/thinghttp/send_request?api_key=QJQW3ZBUQIWJQ8TJ")
        MRKClose = round(float(api_request.content), 2)
        api_request = requests.get("https://api.thingspeak.com/apps/thinghttp/send_request?api_key=59BGL4BGB25F0V9N")
        VAR = round(float(api_request.content),2)
        api_request = requests.get("https://api.thingspeak.com/apps/thinghttp/send_request?api_key=R5BAES89IKD1KEFJ")
        VARClose = round(float(api_request.content), 2)
        api_request = requests.get("https://api.thingspeak.com/apps/thinghttp/send_request?api_key=TF7VW0GLJWKHXRXC")
        XRAY = round(float(api_request.content),2)
        api_request = requests.get("https://api.thingspeak.com/apps/thinghttp/send_request?api_key=5B0AIHQF79SXI9VB")
        XRAYClose = round(float(api_request.content), 2)
        api_request = requests.get("https://api.thingspeak.com/apps/thinghttp/send_request?api_key=MKFE7JADSMH02HB0")
        BMY = round(float(api_request.content),2)
        api_request = requests.get("https://api.thingspeak.com/apps/thinghttp/send_request?api_key=5XOVB7AA1SV358C2")
        BMYClose = round(float(api_request.content), 2)
        api_request = requests.get("https://api.thingspeak.com/apps/thinghttp/send_request?api_key=XAW7TTZSCZDBU0NA")
        ABBV = round(float(api_request.content),2)
        api_request = requests.get("https://api.thingspeak.com/apps/thinghttp/send_request?api_key=NCUCBT1RB1H0P87H")
        ABBVClose = round(float(api_request.content), 2)
        api_request = requests.get("https://api.thingspeak.com/apps/thinghttp/send_request?api_key=C2VQ0VNY3BY16TVQ")
        JNJ = round(float(api_request.content),2)
        api_request = requests.get("https://api.thingspeak.com/apps/thinghttp/send_request?api_key=W1XQ3RKOWYBPR6D1")
        JNJClose = round(float(api_request.content), 2)
        api_request = requests.get("https://api.thingspeak.com/apps/thinghttp/send_request?api_key=TX0DFO38DORILDHJ")
        ABT = round(float(api_request.content),2)
        api_request = requests.get("https://api.thingspeak.com/apps/thinghttp/send_request?api_key=NMA1YPL1I578UE3R")
        ABTClose = round(float(api_request.content), 2)
        api_request = requests.get("https://api.thingspeak.com/apps/thinghttp/send_request?api_key=S2SSKLDU8SZ2FUY8")
        LLY = round(float(api_request.content),2)
        api_request = requests.get("https://api.thingspeak.com/apps/thinghttp/send_request?api_key=NA10B9NBUGXYGEQL")
        LLYClose = round(float(api_request.content), 2)
        api_request = requests.get("https://api.thingspeak.com/apps/thinghttp/send_request?api_key=OUGSYHU645B0A56L")
        ANTM = round(float(api_request.content),2)
        api_request = requests.get("https://api.thingspeak.com/apps/thinghttp/send_request?api_key=2ZKNYFB0OH8DE1RM")
        ANTMClose = round(float(api_request.content), 2)
        api_request = requests.get("https://api.thingspeak.com/apps/thinghttp/send_request?api_key=9VOP1OQ2DRCUT07D")
        ISRG = round(float(api_request.content),2)
        api_request = requests.get("https://api.thingspeak.com/apps/thinghttp/send_request?api_key=JXZJIIA0S4KA8BOX")
        ISRGClose = round(float(api_request.content), 2)
        api_request = requests.get("https://api.thingspeak.com/apps/thinghttp/send_request?api_key=CS5RELWDLD3PM2PX")
        BIIB = round(float(api_request.content),2)
        api_request = requests.get("https://api.thingspeak.com/apps/thinghttp/send_request?api_key=3CE77IJYJZFCMNEY")
        BIIBClose = round(float(api_request.content), 2)

        # Determine the percentage change
        EWstr = "("+str(round(EW / EWClose - 1, 4)*100)+"%"+")"
        Astr = "("+str(round(A / AClose - 1, 4)*100)+"%"+")"
        REGNstr = "("+str(round(REGN / REGNClose - 1, 4)*100)+"%"+")"
        UHSstr = "("+str(round(UHS / UHSClose - 1, 4)*100)+"%"+")"
        MRKstr = "("+str(round(MRK / MRKClose - 1, 4)*100)+"%"+")"
        VARstr = "("+str(round(VAR / VARClose - 1, 4)*100)+"%"+")"
        XRAYstr = "("+str(round(XRAY / XRAYClose - 1, 4)*100)+"%"+")"
        BMYstr = "("+str(round(BMY / BMYClose - 1, 4)*100)+"%"+")"
        ABBVstr = "("+str(round(ABBV / ABBVClose - 1, 4)*100)+"%"+")"
        JNJstr = "("+str(round(JNJ / JNJClose - 1, 4)*100)+"%"+")"
        ABTstr = "("+str(round(ABT / ABTClose - 1, 4)*100)+"%"+")"
        LLYstr = "("+str(round(LLY / LLYClose - 1, 4)*100)+"%"+")"
        ANTMstr = "("+str(round(ANTM / ANTMClose - 1, 4)*100)+"%"+")"
        ISRGstr = "("+str(round(ISRG / ISRGClose - 1, 4)*100)+"%"+")"
        BIIBstr = "("+str(round(BIIB / BIIBClose - 1, 4)*100)+"%"+")"

        # Assemble the completed data
        EW = "EW"+" "+str(EW)+" "+EWstr
        A = "A"+" "+str(A)+" "+Astr
        REGN = "REGN"+" "+str(REGN)+" "+REGNstr
        UHS = "UHS"+" "+str(UHS)+" "+UHSstr
        MRK = "MRK"+" "+str(MRK)+" "+MRKstr
        VAR = "VAR"+" "+str(VAR)+" "+VARstr
        XRAY = "XRAY"+" "+str(XRAY)+" "+XRAYstr
        BMY = "BMY"+" "+str(BMY)+" "+BMYstr
        ABBV = "ABBV"+" "+str(ABBV)+" "+ABBVstr
        JNJ = "JNJ"+" "+str(JNJ)+" "+JNJstr
        ABT = "ABT"+" "+str(ABT)+" "+ABTstr
        LLY = "LLY"+" "+str(LLY)+" "+LLYstr
        ANTM = "ANTM"+" "+str(ANTM)+" "+ANTMstr
        ISRG = "ISRG"+" "+str(ISRG)+" "+ISRGstr
        BIIB = "BIIB"+" "+str(BIIB)+" "+BIIBstr

        # Ticker colors, depending on setting
        self.ticker.tag_configure("up", foreground="#00b04f")
        self.ticker.tag_configure("down", foreground="#ff0000")
        self.ticker.tag_configure("same", foreground="#808080")
        self.ticker.tag_configure("default", foreground="orange")

        self.data = [EW,A,REGN,UHS,MRK,VAR,XRAY,BMY,ABBV,JNJ,ABT,LLY,ANTM,ISRG,BIIB,"   "]
        self.after_idle(self.tick)

    def tick(self):
        symbol = self.data.pop(0)
        self.data.append(symbol)

        # Tag format is hardcoded to default, under which the tickers display Orange
        # Soon the tickers will display Green or Red, according to their value with respect to previous close
        tag = "default"

        self.ticker.configure(bg="black",font="Calibri 10 bold")
        self.ticker.insert("end", " %s" % (symbol), tag)
        self.ticker.see("end")
        self.after(1250, self.tick)

if __name__ == "__main__":
    root = tk.Tk()
    Example(root).pack(fill="both", expand=True)
    root.title("Live Feed")
    root.configure(bg="black")
    root.mainloop()