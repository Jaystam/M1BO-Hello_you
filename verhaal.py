from time import sleep

def wakkerofslapen():
    ochtend = input("opstaan of slapen: ")
    while ochtend == "slapen":
        print("je gaat weer verder slapen")
        sleep(2)
        print("na 15 minuten wordt je weer wakker")
        ochtend = input("opstaan of slapen: ")
    if ochtend == "opstaan":
        print("je staat op")
        sleep(2)
        print("ga je eerst douchen en dan eten of niet douchen")
def douchenofeten():
    naochtend = input("douchen of eten: ")
    if naochtend == "douchen":
        print("je gaat douchen")
        sleep(2)
        print("je bent klaar met douchen")
        sleep(2)
        print("je gaat nu eten")
        sleep(2)
        print("wat ga je eten")
    elif naochtend == "eten":
        print("je gaat eten")
        sleep(2)
        print("wat ga je eten? ")
def wateten():
    eten = input("niks, brood of ontbijtgranen: ")
    if eten == "niks":
        print("weet je het zeker")
        jaofnee = input("ja of nee: ")
        if jaofnee == "ja":
            print("je hebt honger")

        if jaofnee == "nee": 
            print("wat ga je dan eten")
            wateten()
    if eten == "brood":
        print("je maakt brood")
    if eten == "ontbijtgranen":
        print("je maakt ontbijtgranen")
def metwatopvakantie():
    print("ga je met de trein of vliegtuig naar Nederland")
    sleep(2)
    opvakantie = input("trein of vliegtuig: ")
    if opvakantie == "trein":
        print("je gaat naar het centraal station")
    if opvakantie == "vliegtuig":
        print("je gaat naar het vliegveld")
def hotelofhuisje():
    print("ga je naar een hotel of naar een huisje?")
    hotelhuis = input("hotel of huisje: ")
    if hotelhuis == "hotel":
        print("je zoekt een hotel op waar je kan slapen")
        sleep(2)
        print("je hebt je hotel gevonden")
        sleep(2)
        print("je gaat nu uiteten of in het hotel eten")
        sleep(2)
        hotelwaareten()
    if hotelhuis == "huisje":
        print("je zoekt een huisje waar je kan slapen")
        sleep(2)
        print("je hebt je huisje gevonden")
        sleep(2)
        print("je gaat nu uiteten of etenhalen")
        sleep(2)
        huisjewaareten()
def hotelwaareten():
    eten = input("uiteten of hotel: ")
    if eten == "uiteten":
        print("je zoekt een restaurant")
        sleep(2)
        print("je hebt een restaurant gevonden")
        sleep(2)
        print("wat ga je eten")
        sleep(2)
        hotelwateten()
    if eten == "hotel":
        print("je gaat naar het restaurant van het hotel")
        sleep(2)
        print("wat ga je eten?")
        sleep(2)
        hotelwateten()
def huisjewaareten():
    eten = input("uiteten of etenhalen: ")
    if eten == "uiteten":
        print("je zoekt een restaurant")
        sleep(2)
        print("je hebt een restaurant gevonden")
        sleep(2)
        print("wat ga je eten")
        sleep(2)
        huisjewateten()
    if eten == "etenhalen":
        print("je gaat naar de supermarkt om eten te halen")
        sleep(2)
        print("wat ga je halen")
        sleep(2)
        etenhalen()
def hotelwateten():
    eten = input("burger of schnitzel: ")
    if eten == "burger":
        print("je eet de burger")
        sleep(2)
        print("je vondt hem lekker")
        sleep(2)
        hotelofstad()
    if eten == "schnitzel":
        print("je eet de schnitzel")
        sleep(2)
        print("je vondt hem lekker")
        sleep(2)
        hotelofstad()
def huisjewateten():
    eten = input("burger of schnitzel: ")
    if eten == "burger":
        print("je eet de burger")
        sleep(2)
        print("je vondt hem lekker")
        sleep(2)
        huisjeofstad()
    if eten == "schnitzel":
        print("je eet de schnitzel")
        sleep(2)
        print("je vondt hem lekker")
        sleep(2)
        huisjeofstad()
def etenhalen(): 
    eten = input("burger of schnitzel: ")
    if eten == "burger":
        print("je eet de burger")
        sleep(2)
        print("je vondt hem lekker")
        sleep(2)
        huisjeofstad()
    if eten == "schnitzel":
        print("je maakt de schnitzel")
        sleep(2)
        print("je eet de schnitzel")
        sleep(2)
        print("je vondt hem lekker")
        sleep(2)
        huisjeofstad()
def hotelofstad():
        print("ga je naar de stad of naar terug naar je hotel")
        sleep(2)
        buitenofbinnen = input("stad of hotel: ")
        if buitenofbinnen == "stad":
            print("je loopt naar de stad")
            sleep(2)
            print("je loopt een rondje door de stad")
            sleep(2)
            print("je wordt moe")
            sleep(2)
            print("je gaat weer naar je hotel")
            sleep(2)
            print("je gaat nog even op je telefoon voor dat je in slaap valt")
        if buitenofbinnen == "hotel":
            print("je loopt weer terug naar je hotel")
            sleep(2)
            print("je bent moe")
            sleep(2)
            print("je gaat in je bed liggen")
            sleep(2)
            print("je gaat nog even op je telefoon voor dat je in slaap valt")
def huisjeofstad():
    print("ga je naar de stad of terug naar je huisje")
    sleep(2)
    buitenofbinnen = input("stad of huisje: ")
    if buitenofbinnen == "stad":
        print("je loopt naar de stad")
        sleep(2)
        print("je loopt een rondje door de stad")
        sleep(2)
        print("je wordt moe")
        sleep(2)
        print("je gaat weer naar je huisje")
        sleep(2)
        print("je gaat nog even op je telefoon voor dat je in slaap valt")
    if buitenofbinnen == "huisje":
        print("je loopt weer terug naar je huisje")
        sleep(2)
        print("je bent moe")
        sleep(2)
        print("je gaat in je bed liggen")
        sleep(2)
        print("je gaat nog ecven op je telefoon voor dat je in slaap valt")
def naarhuisofblijven():
    wegofblijven = input("blijven of huis: ")
    if wegofblijven == "blijven":
        print("je gaat ontbijten ")
        sleep(2)
        print("je gaat weer door de stad lopen")
        sleep(2)
        print("je krijg wel honger")
        sleep(2)
        print("je zoekt een restaurant")
        sleep(2)
        print("je besteld wat te eten")
        sleep(2)
        print("je vondt het lekker")
        sleep(2)
        print("je gaat weer naar huis")
        sleep(2)
        print("hoe ga je naar huis")
        sleep(2)
        metwatterug()
    if wegofblijven == "huis":
        print("je gaat ontbijten")
        sleep(2)
        print("met wat ga je weer terug")
        sleep(2)
        metwatterug()
def metwatterug():
    weg = input("vliegtuig of trein: ")
    if weg == "vliegtuig":
        print("je gaat naar het vliegveld")
        sleep(2)
        print("je bent weer thuis")
    if weg == "trein":
        print("je gaat naar het centraal station")
        sleep(2)
        print("je bent weer thuis")
def feestenofthuis():
    feest = input("feestje of thuis: ")
    if feest == "feestje":
        print("je gaat naar het feestje")
        sleep(2)
        print("ga je drinken of niet")
        sleep(2)
        drinkenofniet()
    if feest == "thuis":
        print("je blijft thuis")
        sleep(2)
        print("ga je een film kijken of slapen")
        sleep(2)
        filmofslapen()
def filmofslapen():
    filmofslapen = input("film of slapen: ")
    if filmofslapen == "film":
        print("je gaat een film kijken")
        sleep(2)
        iemandbinnen()
    if filmofslapen == "slapen":
        print("je gaat slapen")
        sleep(2)
        print("je wordt niet meer wakker")
def drinkenofniet():
    drinkenofniet = input("drinken of niet drinken: ")
    if drinkenofniet == "drinken":
        print("je bent heel dronken")
        sleep(2)
        print("je gaat weer naar huis fietsen")
        sleep(2)
        print("je valt in een sloot en verdrinkt")
    if drinkenofniet == "niet drinken":
        print("je gaat weer naar huis fietsen")
        sleep(2)
        print("je bent weer thuis en gaat naar bed")
        sleep(2)
        print("je wordt niet meer wakker")
def iemandbinnen():
    print("er komt iemand je huis binnen")
    sleep(2)
    print("je hebt het niet door omdat je een film aan het kijken bent")
    sleep(2)
    print("hij komt je kamer binnen")
    sleep(2)
    print("hij steekt je neer")
    sleep(2)
    print("je overleeft het niet")

print("je wordt wakker")
sleep(2)
print("maak een keuzen opstaan of verder slapen")
sleep(2)
wakkerofslapen()
sleep(2)
douchenofeten()
sleep(2)
wateten()
sleep(2)
print("je pakt je spullen in")
sleep(2)
print("je gaat op vakantie")
sleep(2)
metwatopvakantie()
sleep(2)
print("je komt aan in Nederland")
sleep(2)
hotelofhuisje()
sleep(2)
print("je wordt weer wakker")
sleep(2)
print("wil je nog een dagje blijven of ga je weer naar huis")
sleep(2)
naarhuisofblijven()
sleep(2)
feestenofthuis()
