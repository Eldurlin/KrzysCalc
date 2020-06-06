from tkinter import Tk, StringVar, Text, Pack, ttk, Frame, Entry, Label, Button, END, IntVar, Grid, Radiobutton, OptionMenu

calcWindow = Tk()
calcWindow.title("Calc")
calcWindow.geometry("350x500")

calcWork = ttk.Notebook(calcWindow)
calcWork.pack()

businessCard = Frame(calcWork)
poster = Frame(calcWork)
flyer = Frame(calcWork)
rollUp = Frame(calcWork)
foldedFlyer = Frame(calcWork)

calcWork.add(businessCard, text = "Wizytówki")
calcWork.add(poster, text = "Plakaty")
calcWork.add(flyer, text = "Ulotki")
calcWork.add(rollUp, text = "Roll-upy")
calcWork.add(foldedFlyer, text = "Ulotki składane")

#ulotki składane - ogarnąć
#dodać marżę wszędzie
#odstępy
#stały koszt = koszt a pod tym marża
#niestandardowa wielkość
#zmiana kosztów papieru etc
# ff6600

#podstawowe stałe
sra3Ryza130g = 48.47
sra3Ryza150g = 55.81
sra3Ryza170g = 63.12
sra3Ryza200g = 37.48
sra3Ryza250g = 47.87
sra3Ryza300g = 57.58
sra3Ryza350g = 34.5
sra3RyzaOzdobny = 185.0
iloscRyza125 = 125.0
iloscRyza250 = 250.0
iloscRyza500 = 500.0
iloscRyzaOzdobny = 100
cenaPapieruSra3130g = sra3Ryza130g / iloscRyza500
cenaPapieruSra3150g = sra3Ryza150g / iloscRyza500
cenaPapieruSra3170g = sra3Ryza170g / iloscRyza500
cenaPapieruSra3200g = sra3Ryza200g / iloscRyza250
cenaPapieruSra3250g = sra3Ryza250g / iloscRyza250
cenaPapieruSra3300g = sra3Ryza300g / iloscRyza250
cenaPapieruSra3350g = sra3Ryza350g / iloscRyza125
cenaPapieruSra3Ozdobny = sra3RyzaOzdobny / iloscRyzaOzdobny
ciecieA3PracownikLokal = 4 * (0.5 + 0.5)
ciecieA4PracownikLokal = 5 * (0.5 + 0.5)
ciecieA5PracownikLokal = 6 * (0.5 + 0.5)
ciecieA6PracownikLokal = 7 * (0.5 + 0.5)
ciecieDlPracownikLokal = 7 * (0.5 + 0.5)
przelotSerwisowy = 0.1
leasingMaszyny = 985.0
kosztWliczonyDoPrzelotu = leasingMaszyny / 10000.0
drukKosztPracownika1MinutaLokalZa1Pracownika = 0.5 + 0.5
drukKosztPracownikaLokal36Sra3NaMin = drukKosztPracownika1MinutaLokalZa1Pracownika / 30.0
przygotowanieDoDrukuRozgrzanieMaszyny10Min = 30.0 / 60.0 * 10.0
cenaFoliiZaPrzelotSra310 = 390.0 / 3000.0 / 2.0
ryczaltZakupFoliarkiDoliczonydoPrzelotu10Sra3 = 0.2
foliaKosztPracownikaLokal = 0.5 + 0.5
foliaKosztPracownikaLokal2PrzelotyNaMin = foliaKosztPracownikaLokal / 2.0
ciecieKosztPracownika8MinutLokal = 8.0 * (0.5 + 0.5)
ryczaltZaGilotyneNozMin = 5.0
stalyProcent = 7.0 / 100.0
pakowanie = 5.0
iloscNaArkuszu = 20.0

#businessCard
def cardsCost():
    ciecieWizytowek = float((ciecieKosztPracownika8MinutLokal + ryczaltZaGilotyneNozMin) * float(entryCardsPatterns.get()))
    cost1 = float(entryCardsPatterns.get()) * float(entryCardsQuantity.get()) / float(iloscNaArkuszu)
    cenaPrzelotuPracownik = 0
    if varCardsOverprint.get() == "4+0":
        cenaPrzelotuPracownik = float(2 * (przelotSerwisowy + kosztWliczonyDoPrzelotu + drukKosztPracownikaLokal36Sra3NaMin))
    else:
        cenaPrzelotuPracownik = float(4 * (przelotSerwisowy + kosztWliczonyDoPrzelotu + drukKosztPracownikaLokal36Sra3NaMin))
    foliowanie = float(cenaFoliiZaPrzelotSra310) + float(ryczaltZakupFoliarkiDoliczonydoPrzelotu10Sra3) + float(foliaKosztPracownikaLokal2PrzelotyNaMin)
    if (varCardsOverprint.get() == "4+0" or varCardsOverprint.get() == "4+4") and varCardsFoil.get() == "Brak":
        foliowanie = 0
    elif varCardsOverprint.get() == "4+0" and varCardsFoil.get() == "1+0":
        foliowanie = float(foliowanie)
    elif (varCardsOverprint.get() == "4+0" and varCardsFoil.get() == "1+1") or (varCardsOverprint.get() == "4+4" and varCardsFoil.get() == "1+0"):
        foliowanie = float(foliowanie * 2)
    else:
        foliowanie = float(foliowanie * 4)
    cost2 = float(cenaPapieruSra3350g) + float(cenaPrzelotuPracownik) + float(foliowanie)
    finalCost = round(((cost1 * cost2) + ciecieWizytowek + pakowanie + przygotowanieDoDrukuRozgrzanieMaszyny10Min), 2)
    finalCostProfit = round((finalCost + (finalCost * stalyProcent)), 3)
    textCardsCost.delete("1.0", END)
    textCardsCost.insert(END, finalCost)
    textCardsCostProfit.delete("1.0", END)
    textCardsCostProfit.insert(END, finalCostProfit)

labelCardsPatterns = Label(businessCard, text = "Ilość wzorów:")
labelCardsPatterns.pack()

entryCardsPatterns = StringVar()
entryCardsPatterns = Entry(businessCard, textvariable = entryCardsPatterns)
entryCardsPatterns.pack()

labelCardsQuantity = Label(businessCard, text = "Ilość:")
labelCardsQuantity.pack()

entryCardsQuantity = StringVar()
entryCardsQuantity = Entry(businessCard, textvariable = entryCardsQuantity)
entryCardsQuantity.pack()

labelCardsPaperWeight = Label(businessCard, text = "Gramatura:")
labelCardsPaperWeight.pack()

optionsCardsPaperWeight = ["350", "Ozdobny"]
varCardsPaperWeight = StringVar()
varCardsPaperWeight.set(optionsCardsPaperWeight[0])
optCardsPaperWeightMenu = OptionMenu(businessCard, varCardsPaperWeight, *optionsCardsPaperWeight)
optCardsPaperWeightMenu.pack()

labelCardsOverprint = Label(businessCard, text = "Zadruk:")
labelCardsOverprint.pack()

optCardsOverprint = ["4+0", "4+4"]
varCardsOverprint = StringVar()
varCardsOverprint.set(optCardsOverprint[0])
optCardsOverprintMenu = OptionMenu(businessCard, varCardsOverprint, *optCardsOverprint)
optCardsOverprintMenu.pack()

labelCardsFoil = Label(businessCard, text = "Foliowanie:")
labelCardsFoil.pack()

optCardsFoil = ["Brak", "1+0", "1+1"]
varCardsFoil = StringVar()
varCardsFoil.set(optCardsFoil[0])
optCardsFoil = OptionMenu(businessCard, varCardsFoil, *optCardsFoil)
optCardsFoil.pack()

buttonCardsCost = Button(businessCard, text = "Oblicz koszt", command = cardsCost)
buttonCardsCost.pack()

textCardsCost = Text(businessCard, height = 1, width = 20)
textCardsCost.pack()

labelCardsProfit = Label(businessCard, text = "Stały koszt 7%")
labelCardsProfit.pack()

textCardsCostProfit = Text(businessCard, height = 1, width = 20)
textCardsCostProfit.pack()

#posters
def posterCost():
    cost = 0
    if varPosterSize.get() == "A4":
        cost = float(entryPostersPatterns.get()) * float(entryPosterQuantity.get()) / 2
    else:
        cost = float(entryPostersPatterns.get()) * float(entryPosterQuantity.get()) / 1
    cenaPrzelotuPracownik = 0
    if varPosterOverprint.get() == "4+0":
        cenaPrzelotuPracownik = (2 * (przelotSerwisowy + kosztWliczonyDoPrzelotu)) + drukKosztPracownikaLokal36Sra3NaMin
    else:
        cenaPrzelotuPracownik = (4 * (przelotSerwisowy + kosztWliczonyDoPrzelotu)) + drukKosztPracownikaLokal36Sra3NaMin
    foliowanie = float(cenaFoliiZaPrzelotSra310) + float(ryczaltZakupFoliarkiDoliczonydoPrzelotu10Sra3) + float(foliaKosztPracownikaLokal2PrzelotyNaMin)
    if (varPosterPaperWeight.get() == "200" or varPosterPaperWeight.get() == "250" or varPosterPaperWeight.get() == "300" or varPosterPaperWeight.get() == "350") and varPosterFoil.get() == "1+0" and varPosterOverprint.get() == "4+0":
        foliowanie = foliowanie
    elif (varPosterPaperWeight.get() == "200" or varPosterPaperWeight.get() == "250" or varPosterPaperWeight.get() == "300" or varPosterPaperWeight.get() == "350") and varPosterFoil.get() == "1+1" and varPosterOverprint.get() == "4+4":
        foliowanie = foliowanie * 2 + drukKosztPracownikaLokal36Sra3NaMin
    elif varPosterPaperWeight.get() == "Ozdobny" and varPosterOverprint.get() == "4+4":
        foliowanie = drukKosztPracownikaLokal36Sra3NaMin
    else:
        foliowanie = 0
    ciecie = 0
    if varPosterSize.get() == "A4":
        ciecie = (ciecieA4PracownikLokal + ryczaltZaGilotyneNozMin) * float(entryPostersPatterns.get())
    else:
        ciecie = (ciecieA3PracownikLokal + ryczaltZaGilotyneNozMin) * float(entryPostersPatterns.get())
    finalCost = 0
    if varPosterPaperWeight.get() == "130":
        finalCost = (cost * (cenaPapieruSra3130g + cenaPrzelotuPracownik + foliowanie) + ciecie + pakowanie + przygotowanieDoDrukuRozgrzanieMaszyny10Min)
    elif varPosterPaperWeight.get() == "150":
        finalCost = (cost * (cenaPapieruSra3150g + cenaPrzelotuPracownik + foliowanie) + ciecie + pakowanie + przygotowanieDoDrukuRozgrzanieMaszyny10Min)
    elif varPosterPaperWeight.get() == "170":
        finalCost = (cost * (cenaPapieruSra3170g + cenaPrzelotuPracownik + foliowanie) + ciecie + pakowanie + przygotowanieDoDrukuRozgrzanieMaszyny10Min)
    elif varPosterPaperWeight.get() == "200":
        finalCost = (cost * (cenaPapieruSra3200g + cenaPrzelotuPracownik + foliowanie) + ciecie + pakowanie + przygotowanieDoDrukuRozgrzanieMaszyny10Min)
    elif varPosterPaperWeight.get() == "250":
        finalCost = (cost * (cenaPapieruSra3250g + cenaPrzelotuPracownik + foliowanie) + ciecie + pakowanie + przygotowanieDoDrukuRozgrzanieMaszyny10Min)
    elif varPosterPaperWeight.get() == "300":
        finalCost = (cost * (cenaPapieruSra3300g + cenaPrzelotuPracownik + foliowanie) + ciecie + pakowanie + przygotowanieDoDrukuRozgrzanieMaszyny10Min)
    elif varPosterPaperWeight.get() == "350":
        finalCost = (cost * (cenaPapieruSra3350g + cenaPrzelotuPracownik + foliowanie) + ciecie + pakowanie + przygotowanieDoDrukuRozgrzanieMaszyny10Min)
    else:
        finalCost = (cost * (cenaPapieruSra3Ozdobny + cenaPrzelotuPracownik + foliowanie) + ciecie + pakowanie + przygotowanieDoDrukuRozgrzanieMaszyny10Min)
    finalCost = round(finalCost, 2)
    textPosterCost.delete("1.0", END)
    textPosterCost.insert(END, finalCost)

labelPosterPatterns = Label(poster, text = "Ilość wzorów:")
labelPosterPatterns.pack()

entryPostersPatterns = StringVar()
entryPostersPatterns = Entry(poster, textvariable = entryPostersPatterns)
entryPostersPatterns.pack()

labelPosterQuantity = Label(poster, text = "Ilość:")
labelPosterQuantity.pack()

entryPosterQuantity = StringVar()
entryPosterQuantity = Entry(poster, textvariable = entryPosterQuantity)
entryPosterQuantity.pack()

labelPosterSize = Label(poster, text = "Wielkość:")
labelPosterSize.pack()

optPosterSize = ["A4", "A3"]
varPosterSize = StringVar()
varPosterSize.set(optPosterSize[0])
optPosterSize = OptionMenu(poster, varPosterSize, *optPosterSize)
optPosterSize.pack()

labelPosterPaperWeight = Label(poster, text = "Gramatura:")
labelPosterPaperWeight.pack()

optPosterPaperWeight = ["130", "150", "170", "200", "250", "300", "350", "Ozdobny"]
varPosterPaperWeight = StringVar()
varPosterPaperWeight.set(optPosterPaperWeight[0])
optPosterPaperWeight = OptionMenu(poster, varPosterPaperWeight, *optPosterPaperWeight)
optPosterPaperWeight.pack()

labelPostersOverprint = Label(poster, text = "Zadruk:")
labelPostersOverprint.pack()

optPosterOverprint = ["4+0", "4+4"]
varPosterOverprint = StringVar()
varPosterOverprint.set(optPosterOverprint[0])
optPosterOverprint = OptionMenu(poster, varPosterOverprint, *optPosterOverprint)
optPosterOverprint.pack()

labelPosterFoil = Label(poster, text = "Foliowanie:")
labelPosterFoil.pack()

optPosterFoil = ["Brak", "1+0", "1+1"]
varPosterFoil = StringVar()
varPosterFoil.set(optPosterFoil[0])
optPosterFoil = OptionMenu(poster, varPosterFoil, *optPosterFoil)
optPosterFoil.pack()

buttonPosterCost = Button(poster, text = "Oblicz koszt", command = posterCost)
buttonPosterCost.pack()

textPosterCost = Text(poster, height = 1, width = 20)
textPosterCost.pack()

labelPostersProfit = Label(poster, text = "Stały koszt 7%")
labelPostersProfit.pack()

textPostersCostProfit = Text(poster, height = 1, width = 20)
textPostersCostProfit.pack()

#flyers
def flyerCost():
    cost = 0
    if varFlyerSize.get() == "A4":
        cost = float(entryFlyerPatterns.get()) * float(entryFlyerQuantity.get()) / 2
    elif varFlyerSize.get() == "A5" or varFlyerSize.get() == "14/14 14,5/14,5 15/15":
        cost = float(entryFlyerPatterns.get()) * float(entryFlyerQuantity.get()) / 4
    elif varFlyerSize.get() == "A6":
        cost = float(entryFlyerPatterns.get()) * float(entryFlyerQuantity.get()) / 8
    else:
        cost = float(entryFlyerPatterns.get()) * float(entryFlyerQuantity.get()) / 6
    cenaPrzelotuPracownik = 0
    if varFlyerOverprint.get() == "4+0":
        cenaPrzelotuPracownik = (2 * (przelotSerwisowy + kosztWliczonyDoPrzelotu)) + drukKosztPracownikaLokal36Sra3NaMin
    else:
        cenaPrzelotuPracownik = (4 * (przelotSerwisowy + kosztWliczonyDoPrzelotu)) + drukKosztPracownikaLokal36Sra3NaMin
    foliowanie = float(cenaFoliiZaPrzelotSra310) + float(ryczaltZakupFoliarkiDoliczonydoPrzelotu10Sra3) + float(foliaKosztPracownikaLokal2PrzelotyNaMin)
    if (varFlyerPaperWeight.get() == "200" or varFlyerPaperWeight.get() == "250" or varFlyerPaperWeight.get() == "300" or varFlyerPaperWeight.get() == "350") and varFlyerFoil.get() == "1+0" and varFlyerOverprint.get() == "4+0":
        foliowanie = foliowanie
    elif (varFlyerPaperWeight.get() == "200" or varFlyerPaperWeight.get() == "250" or varFlyerPaperWeight.get() == "300" or varFlyerPaperWeight.get() == "350") and varFlyerFoil.get() == "1+1" and varFlyerOverprint.get() == "4+4":
        foliowanie = foliowanie * 2 + drukKosztPracownikaLokal36Sra3NaMin
    elif varFlyerPaperWeight.get() == "Ozdobny" and varFlyerOverprint.get() == "4+4":
        foliowanie = drukKosztPracownikaLokal36Sra3NaMin
    else:
        foliowanie = 0
    ciecie = 0
    if varFlyerSize.get() == "A4":
        ciecie = (ciecieA4PracownikLokal + ryczaltZaGilotyneNozMin) * float(entryFlyerPatterns.get())
    elif varFlyerSize.get() == "A5" or varFlyerSize.get() == "14/14 14,5/14,5 15/15":
        ciecie = (ciecieA5PracownikLokal + ryczaltZaGilotyneNozMin) * float(entryFlyerPatterns.get())
    elif varFlyerSize.get() == "A6":
        ciecie = (ciecieA6PracownikLokal + ryczaltZaGilotyneNozMin) * float(entryFlyerPatterns.get())
    else:
        ciecie = (ciecieDlPracownikLokal + ryczaltZaGilotyneNozMin) * float(entryFlyerPatterns.get())
    finalCost = 0
    if varFlyerPaperWeight.get() == "130":
        finalCost = (cost * (cenaPapieruSra3130g + cenaPrzelotuPracownik + foliowanie) + ciecie + pakowanie + przygotowanieDoDrukuRozgrzanieMaszyny10Min)
    elif varFlyerPaperWeight.get() == "150":
        finalCost = (cost * (cenaPapieruSra3150g + cenaPrzelotuPracownik + foliowanie) + ciecie + pakowanie + przygotowanieDoDrukuRozgrzanieMaszyny10Min)
    elif varFlyerPaperWeight.get() == "170":
        finalCost = (cost * (cenaPapieruSra3170g + cenaPrzelotuPracownik + foliowanie) + ciecie + pakowanie + przygotowanieDoDrukuRozgrzanieMaszyny10Min)
    elif varFlyerPaperWeight.get() == "200":
        finalCost = (cost * (cenaPapieruSra3200g + cenaPrzelotuPracownik + foliowanie) + ciecie + pakowanie + przygotowanieDoDrukuRozgrzanieMaszyny10Min)
    elif varFlyerPaperWeight.get() == "250":
        finalCost = (cost * (cenaPapieruSra3250g + cenaPrzelotuPracownik + foliowanie) + ciecie + pakowanie + przygotowanieDoDrukuRozgrzanieMaszyny10Min)
    elif varFlyerPaperWeight.get() == "300":
        finalCost = (cost * (cenaPapieruSra3300g + cenaPrzelotuPracownik + foliowanie) + ciecie + pakowanie + przygotowanieDoDrukuRozgrzanieMaszyny10Min)
    elif varFlyerPaperWeight.get() == "350":
        finalCost = (cost * (cenaPapieruSra3350g + cenaPrzelotuPracownik + foliowanie) + ciecie + pakowanie + przygotowanieDoDrukuRozgrzanieMaszyny10Min)
    else:
        finalCost = (cost * (cenaPapieruSra3Ozdobny + cenaPrzelotuPracownik + foliowanie) + ciecie + pakowanie + przygotowanieDoDrukuRozgrzanieMaszyny10Min)
    finalCost = round(finalCost, 2)
    finalCostProfit = round((finalCost + (finalCost * stalyProcent)), 3)
    textFlyerCost.delete("1.0", END)
    textFlyerCost.insert(END, finalCost)
    textFlyerCostProfit.delete("1.0", END)
    textFlyerCostProfit.insert(END, finalCostProfit)

labelFlyerPatterns = Label(flyer, text = "Ilość wzorów:")
labelFlyerPatterns.pack()

entryFlyerPatterns = StringVar()
entryFlyerPatterns = Entry(flyer, textvariable = entryFlyerPatterns)
entryFlyerPatterns.pack()

labelFlyerQuantity = Label(flyer, text = "Ilość:")
labelFlyerQuantity.pack()

entryFlyerQuantity = StringVar()
entryFlyerQuantity = Entry(flyer, textvariable = entryFlyerQuantity)
entryFlyerQuantity.pack()

labelFlyerSize = Label(flyer, text = "Wielkość:")
labelFlyerSize.pack()

optFlyerSize = ["A4", "A5", "A6", "DL", "14/14 14,5/14,5 15/15"]
varFlyerSize = StringVar()
varFlyerSize.set(optFlyerSize[0])
optFlyerSize = OptionMenu(flyer, varFlyerSize, *optFlyerSize)
optFlyerSize.pack()

labelFlyerPaperWeight = Label(flyer, text = "Gramatura:")
labelFlyerPaperWeight.pack()

optFlyerPaperWeight = ["130", "150", "170", "200", "250", "300", "350", "Ozdobny"]
varFlyerPaperWeight = StringVar()
varFlyerPaperWeight.set(optFlyerPaperWeight[0])
optFlyerPaperWeight = OptionMenu(flyer, varFlyerPaperWeight, *optFlyerPaperWeight)
optFlyerPaperWeight.pack()

labelFlyersOverprint = Label(flyer, text = "Zadruk:")
labelFlyersOverprint.pack()

optFlyerOverprint = ["4+0", "4+4"]
varFlyerOverprint = StringVar()
varFlyerOverprint.set(optFlyerOverprint[0])
optFlyerOverprint = OptionMenu(flyer, varFlyerOverprint, *optFlyerOverprint)
optFlyerOverprint.pack()

labelFlyerFoil = Label(flyer, text = "Foliowanie:")
labelFlyerFoil.pack()

optFlyerFoil = ["Brak", "1+0", "1+1"]
varFlyerFoil = StringVar()
varFlyerFoil.set(optFlyerFoil[0])
optFlyerFoil = OptionMenu(flyer, varFlyerFoil, *optFlyerFoil)
optFlyerFoil.pack()

buttonFlyerCost = Button(flyer, text = "Oblicz koszt", command = flyerCost)
buttonFlyerCost.pack()

textFlyerCost = Text(flyer, height = 1, width = 20)
textFlyerCost.pack()

labelFlyersProfit = Label(flyer, text = "Stały koszt 7%")
labelFlyersProfit.pack()

textFlyerCostProfit = Text(flyer, height = 1, width = 20)
textFlyerCostProfit.pack()

#roll-ups
blockoutSico420gm = 5.85
blockoutSico530gm = 7.60
cenaMaterial420gm = 2.5 * blockoutSico420gm
cenaMaterial420gm120 = 2.5 * blockoutSico420gm * 1.2
cenaMaterial530gm150 = 2.5 * blockoutSico530gm * 1.5
kosztAtramentM2 = 2.21
cenaWydruk85M2 = 0.85 * kosztAtramentM2 * 2.1
cenaWydruk100M2 = 1.0 * kosztAtramentM2 * 2.1
cenaWydruk120M2 = 1.2 * kosztAtramentM2 * 2.1
cenaWydruk150M2 = 1.5 * kosztAtramentM2 * 2.1
ryczaltMaszyna = 1.5
ryczaltSerwis85M2 = ryczaltMaszyna * 0.85 * 2.1
ryczaltSerwis100M2 = ryczaltMaszyna * 1.0 * 2.1
ryczaltSerwis120M2 = ryczaltMaszyna * 1.2 * 2.1
ryczaltSerwis150M2 = ryczaltMaszyna * 1.5 * 2.1
kosztKaseta85 = 35.4
kosztKaseta100 = 38.9
kosztKaseta120 = 68.0
kosztKaseta150 = 84.0
plikMediaZaladowanieTestGlowicy = 10.0
czasObsMasDrukStawkaPrac = 4.0
kosztPracownik85 = czasObsMasDrukStawkaPrac * 0.85 * 2.1
kosztPracownik100 = czasObsMasDrukStawkaPrac * 1.0 * 2.1
kosztPracownik120 = czasObsMasDrukStawkaPrac * 1.2 * 2.1
kosztPracownik150 = czasObsMasDrukStawkaPrac * 1.5 * 2.1
kosztPracCiecie = 4.0
kosztPracCiecie150 = 8.0
kosztPracMontazKaseta = 8.0

def rollUpCost():
    finalCost = 0
    if varRollUpWidthThickness.get() == "85":
        finalCost = (plikMediaZaladowanieTestGlowicy + pakowanie + (cenaMaterial420gm + cenaWydruk85M2 + ryczaltSerwis85M2 + kosztKaseta85 + kosztPracownik85 + kosztPracCiecie + kosztPracMontazKaseta) * float(entryRollUpQuantity.get())) * float(entryRollUpPattern.get())
    elif varRollUpWidthThickness.get() == "100":
        finalCost = (plikMediaZaladowanieTestGlowicy + pakowanie + (cenaMaterial420gm + cenaWydruk100M2 + ryczaltSerwis100M2 + kosztKaseta100 + kosztPracownik100 + kosztPracCiecie + kosztPracMontazKaseta) * float(entryRollUpQuantity.get())) * float(entryRollUpPattern.get())
    elif varRollUpWidthThickness.get() == "120":
        finalCost = (plikMediaZaladowanieTestGlowicy + pakowanie + (cenaMaterial420gm120 + cenaWydruk120M2 + ryczaltSerwis120M2 + kosztKaseta120 + kosztPracownik120 + kosztPracCiecie + kosztPracMontazKaseta) * float(entryRollUpQuantity.get())) * float(entryRollUpPattern.get())
    elif varRollUpWidthThickness.get() == "150":
        finalCost = (plikMediaZaladowanieTestGlowicy + pakowanie + (cenaMaterial530gm150 + cenaWydruk150M2 + ryczaltSerwis150M2 + kosztKaseta150 + kosztPracownik150 + kosztPracCiecie150 + kosztPracMontazKaseta) * float(entryRollUpQuantity.get())) * float(entryRollUpPattern.get())
    else:
        finalCost = 666.66    
    finalCost = round(finalCost, 2)
    finalCostProfit = round((finalCost + (finalCost * stalyProcent)), 3)
    textRollUpCost.delete("1.0", END)
    textRollUpCost.insert(END, finalCost)
    textRollUpCostProfit.delete("1.0", END)
    textRollUpCostProfit.insert(END, finalCostProfit)

labelRollUpMedium = Label(rollUp, text = "Gramatura/medium:")
labelRollUpMedium.pack()

optRollUpPattern = ["Baner", "Blockout"]
varRollUpPattern = StringVar()
varRollUpPattern.set(optRollUpPattern[0])
optRollUpPattern = OptionMenu(rollUp, varRollUpPattern, *optRollUpPattern)
optRollUpPattern.pack()

labelRollUpWidthThickness = Label(rollUp, text = "Szerokość/grubość:")

optRollUpWidthThickness = ["85", "100", "120", "150", "200"]
varRollUpWidthThickness = StringVar()
varRollUpWidthThickness.set(optRollUpWidthThickness[0])
optRollUpWidthThickness = OptionMenu(rollUp, varRollUpWidthThickness, *optRollUpWidthThickness)
optRollUpWidthThickness.pack()

labelRollUpPattern = Label(rollUp, text = "Ilość wzorów:")
labelRollUpPattern.pack()

entryRollUpPattern = StringVar()
entryRollUpPattern = Entry(rollUp, textvariable = entryRollUpPattern)
entryRollUpPattern.pack()

labelRollUpQuantity = Label(rollUp, text = "Ilość:")
labelRollUpQuantity.pack()

entryRollUpQuantity = StringVar()
entryRollUpQuantity = Entry(rollUp, textvariable = entryRollUpQuantity)
entryRollUpQuantity.pack()

buttonRollUpCost = Button(rollUp, text = "Oblicz koszt", command = rollUpCost)
buttonRollUpCost.pack()

textRollUpCost = Text(rollUp, height = 1, width = 20)
textRollUpCost.pack()

labelRollUpProfit = Label(rollUp, text = "Stały koszt 7%")
labelRollUpProfit.pack()

textRollUpCostProfit = Text(rollUp, height = 1, width = 20)
textRollUpCostProfit.pack()

#folded flyers do zrobienia składanie i zmiany danych
def foldedFlyerCost():
    cost = 0
    if varFoldedFlyerSize.get() == "A4":
        cost = float(entryFoldedFlyerPatterns.get()) * float(entryFoldedFlyerQuantity.get()) / 2
    elif varFoldedFlyerSize.get() == "A5" or varFoldedFlyerSize.get() == "14/14 14,5/14,5 15/15":
        cost = float(entryFoldedFlyerPatterns.get()) * float(entryFoldedFlyerQuantity.get()) / 4
    elif varFoldedFlyerSize.get() == "A6":
        cost = float(entryFoldedFlyerPatterns.get()) * float(entryFoldedFlyerQuantity.get()) / 8
    else:
        cost = float(entryFoldedFlyerPatterns.get()) * float(entryFoldedFlyerQuantity.get()) / 6
    cenaPrzelotuPracownik = 0
    if varFoldedFlyerOverprint.get() == "4+0":
        cenaPrzelotuPracownik = (2 * (przelotSerwisowy + kosztWliczonyDoPrzelotu)) + drukKosztPracownikaLokal36Sra3NaMin
    else:
        cenaPrzelotuPracownik = (4 * (przelotSerwisowy + kosztWliczonyDoPrzelotu)) + drukKosztPracownikaLokal36Sra3NaMin
    foliowanie = float(cenaFoliiZaPrzelotSra310) + float(ryczaltZakupFoliarkiDoliczonydoPrzelotu10Sra3) + float(foliaKosztPracownikaLokal2PrzelotyNaMin)
    if (varFoldedFlyerPaperWeight.get() == "200" or varFoldedFlyerPaperWeight.get() == "250" or varFoldedFlyerPaperWeight.get() == "300" or varFoldedFlyerPaperWeight.get() == "350") and varFoldedFlyerFoil.get() == "1+0" and varFoldedFlyerOverprint.get() == "4+0":
        foliowanie = foliowanie
    elif (varFoldedFlyerPaperWeight.get() == "200" or varFoldedFlyerPaperWeight.get() == "250" or varFoldedFlyerPaperWeight.get() == "300" or varFoldedFlyerPaperWeight.get() == "350") and varFoldedFlyerFoil.get() == "1+1" and varFoldedFlyerOverprint.get() == "4+4":
        foliowanie = foliowanie * 2 + drukKosztPracownikaLokal36Sra3NaMin
    elif varFoldedFlyerPaperWeight.get() == "Ozdobny" and varFoldedFlyerOverprint.get() == "4+4":
        foliowanie = drukKosztPracownikaLokal36Sra3NaMin
    else:
        foliowanie = 0
    ciecie = 0
    if varFoldedFlyerSize.get() == "A4":
        ciecie = (ciecieA4PracownikLokal + ryczaltZaGilotyneNozMin) * float(entryFoldedFlyerPatterns.get())
    elif varFoldedFlyerSize.get() == "A5" or varFoldedFlyerSize.get() == "14/14 14,5/14,5 15/15":
        ciecie = (ciecieA5PracownikLokal + ryczaltZaGilotyneNozMin) * float(entryFoldedFlyerPatterns.get())
    elif varFoldedFlyerSize.get() == "A6":
        ciecie = (ciecieA6PracownikLokal + ryczaltZaGilotyneNozMin) * float(entryFoldedFlyerPatterns.get())
    else:
        ciecie = (ciecieDlPracownikLokal + ryczaltZaGilotyneNozMin) * float(entryFoldedFlyerPatterns.get())
    finalCost = 0
    if varFoldedFlyerPaperWeight.get() == "130":
        finalCost = (cost * (cenaPapieruSra3130g + cenaPrzelotuPracownik + foliowanie) + ciecie + pakowanie + przygotowanieDoDrukuRozgrzanieMaszyny10Min)
    elif varFoldedFlyerPaperWeight.get() == "150":
        finalCost = (cost * (cenaPapieruSra3150g + cenaPrzelotuPracownik + foliowanie) + ciecie + pakowanie + przygotowanieDoDrukuRozgrzanieMaszyny10Min)
    elif varFoldedFlyerPaperWeight.get() == "170":
        finalCost = (cost * (cenaPapieruSra3170g + cenaPrzelotuPracownik + foliowanie) + ciecie + pakowanie + przygotowanieDoDrukuRozgrzanieMaszyny10Min)
    elif varFoldedFlyerPaperWeight.get() == "200":
        finalCost = (cost * (cenaPapieruSra3200g + cenaPrzelotuPracownik + foliowanie) + ciecie + pakowanie + przygotowanieDoDrukuRozgrzanieMaszyny10Min)
    elif varFoldedFlyerPaperWeight.get() == "250":
        finalCost = (cost * (cenaPapieruSra3250g + cenaPrzelotuPracownik + foliowanie) + ciecie + pakowanie + przygotowanieDoDrukuRozgrzanieMaszyny10Min)
    elif varFoldedFlyerPaperWeight.get() == "300":
        finalCost = (cost * (cenaPapieruSra3300g + cenaPrzelotuPracownik + foliowanie) + ciecie + pakowanie + przygotowanieDoDrukuRozgrzanieMaszyny10Min)
    elif varFoldedFlyerPaperWeight.get() == "350":
        finalCost = (cost * (cenaPapieruSra3350g + cenaPrzelotuPracownik + foliowanie) + ciecie + pakowanie + przygotowanieDoDrukuRozgrzanieMaszyny10Min)
    else:
        finalCost = (cost * (cenaPapieruSra3Ozdobny + cenaPrzelotuPracownik + foliowanie) + ciecie + pakowanie + przygotowanieDoDrukuRozgrzanieMaszyny10Min)
    finalCost = round(finalCost, 2)
    finalCostProfit = round((finalCost + (finalCost * stalyProcent)), 3)
    textFoldedFlyerCost.delete("1.0", END)
    textFoldedFlyerCost.insert(END, finalCost)
    textFoldedFlyerCostProfit.delete("1.0", END)
    textFoldedFlyerCostProfit.insert(END, finalCostProfit)

labelFoldedFlyerPatterns = Label(foldedFlyer, text = "Ilość wzorów:")
labelFoldedFlyerPatterns.pack()

entryFoldedFlyerPatterns = StringVar()
entryFoldedFlyerPatterns = Entry(foldedFlyer, textvariable = entryFoldedFlyerPatterns)
entryFoldedFlyerPatterns.pack()

labelFoldedFlyerQuantity = Label(foldedFlyer, text = "Ilość:")
labelFoldedFlyerQuantity.pack()

entryFoldedFlyerQuantity = StringVar()
entryFoldedFlyerQuantity = Entry(foldedFlyer, textvariable = entryFoldedFlyerQuantity)
entryFoldedFlyerQuantity.pack()

labelFoldedFlyerSize = Label(foldedFlyer, text = "Wielkość:")
labelFoldedFlyerSize.pack()

optFoldedFlyerSize = ["A4", "A5", "A6", "DL", "14/14 14,5/14,5 15/15"]
varFoldedFlyerSize = StringVar()
varFoldedFlyerSize.set(optFoldedFlyerSize[0])
optFoldedFlyerSize = OptionMenu(foldedFlyer, varFoldedFlyerSize, *optFoldedFlyerSize)
optFoldedFlyerSize.pack()

labelFoldedFlyerPaperWeight = Label(foldedFlyer, text = "Gramatura:")
labelFoldedFlyerPaperWeight.pack()

optFoldedFlyerPaperWeight = ["130", "150", "170", "200", "250", "300", "350", "Ozdobny"]
varFoldedFlyerPaperWeight = StringVar()
varFoldedFlyerPaperWeight.set(optFoldedFlyerPaperWeight[0])
optFoldedFlyerPaperWeight = OptionMenu(foldedFlyer, varFoldedFlyerPaperWeight, *optFoldedFlyerPaperWeight)
optFoldedFlyerPaperWeight.pack()

labelFoldedFlyersOverprint = Label(foldedFlyer, text = "Zadruk:")
labelFoldedFlyersOverprint.pack()

optFoldedFlyerOverprint = ["4+0", "4+4"]
varFoldedFlyerOverprint = StringVar()
varFoldedFlyerOverprint.set(optFoldedFlyerOverprint[0])
optFoldedFlyerOverprint = OptionMenu(foldedFlyer, varFoldedFlyerOverprint, *optFoldedFlyerOverprint)
optFoldedFlyerOverprint.pack()

labelFoldedFlyerFoil = Label(foldedFlyer, text = "Foliowanie:")
labelFoldedFlyerFoil.pack()

optFoldedFlyerFoil = ["Brak", "1+0", "1+1"]
varFoldedFlyerFoil = StringVar()
varFoldedFlyerFoil.set(optFoldedFlyerFoil[0])
optFoldedFlyerFoil = OptionMenu(foldedFlyer, varFoldedFlyerFoil, *optFoldedFlyerFoil)
optFoldedFlyerFoil.pack()

buttonFoldedFlyerCost = Button(foldedFlyer, text = "Oblicz koszt", command = foldedFlyerCost)
buttonFoldedFlyerCost.pack()

textFoldedFlyerCost = Text(foldedFlyer, height = 1, width = 20)
textFoldedFlyerCost.pack()

labelFoldedFlyersProfit = Label(foldedFlyer, text = "Stały koszt 7%")
labelFoldedFlyersProfit.pack()

textFoldedFlyerCostProfit = Text(foldedFlyer, height = 1, width = 20)
textFoldedFlyerCostProfit.pack()

calcWindow.mainloop()