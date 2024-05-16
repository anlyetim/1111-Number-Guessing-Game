import pygame
import random
pygame.init()
pygame.mixer.init()

# ATAMALAR -------------------------------------------------------------------------------------------------------------

Muzik = pygame.mixer.music.load("datdat2.wav")
pygame.mixer.music.play(-1, 3.0)
pygame.mixer.music.set_volume(1)
Volume = True
BeyazRenk = (255, 255, 255)
SiyahRenk = (0, 0, 0)

fontlist = pygame.font.get_fonts()
yazi_40 = pygame.font.SysFont('cheeseburger', 40)
yazi_90 = pygame.font.SysFont('cheeseburger', 90)
yazi_70 = pygame.font.SysFont('cheeseburger', 70)
yazi_55 = pygame.font.SysFont('cheeseburger', 55)

text = yazi_40.render("0", True, (0, 0, 0))
rotateText = pygame.transform.rotate(text, -45)
TurKontrolText = yazi_90.render("1.Tur", True, SiyahRenk)
SiraGostergeText = yazi_70.render("Senin Sıran", True, SiyahRenk)
yakinlikText = yazi_90.render("0 0 0 0", True, SiyahRenk)
CevaplaTextButton = yazi_90.render("CEVAPLA", True, SiyahRenk)
Tahminim1Text = yazi_55.render("", True, SiyahRenk)
RakipTahmin1Text = yazi_55.render("", True, SiyahRenk)
username = ""
TahminEdiliyor = ""
rakipTahmini = ""

Tur = 1
saat = pygame.time.Clock()
kalanZaman = 0
baslangicZamani = None
TurGecildi = None
RakipTahminAsamasinda = False

oyuncu_sayilar = []
Tahminlerim = []
RakibinTahminleri = []
yakinlik_derecesi = [0, 0, 0, 0]
rakip_yakinlik_derecesi = [0, 0, 0, 0]

Base = True
MainMenuOpen = True
MainWindow = pygame.display.set_mode((1920, 1080))
OynaWindowOpen = False
oynaWindow = pygame.display.set_mode((1920, 1080))
SecenekWindowOpen = False
secenekWindow = pygame.display.set_mode((1920, 1080))
usernameWindowOpen = False
usernameWindow = pygame.display.set_mode((1920, 1080))
KazanmaWindowOpen = False
kazanmaWindow = pygame.display.set_mode((1920, 1080))
KayipWindowOpen = False
kayipWindow = pygame.display.set_mode((1920, 1080))
BerabereWindowOpen = False
berabereWindow = pygame.display.set_mode((1920, 1080))
OgreticiWindowOpen = False
ogreticiWindow = pygame.display.set_mode((1920, 1080))
EmegiGecenlerWindowOpen = False
emegiGecenlerWindow = pygame.display.set_mode((1920, 1080))

# GÖRSELLER -----------------------------------------------------------------------------------------------------------

OynaButton = pygame.image.load("oynabutton.png")
SolPencere = pygame.image.load("solpencere.png")
SecenekButton = pygame.image.load("secenekbutton.png")
Versiyon = pygame.image.load("versiyon.png")
Exit = pygame.image.load("exitbutton.png")

DefterKalem = pygame.image.load("defterkalem.png")
HMBase = pygame.image.load("hesapmakineBase.png")
HMNokta = pygame.image.load("hesapmakineNokta.png")

Ogretici1 = pygame.image.load("Talimat1.png")
Ogretici2 = pygame.image.load("Talimat2.png")
Ogretici3 = pygame.image.load("Talimat3.png")
Ogretici4 = pygame.image.load("Talimat4.png")
Ogretici5 = pygame.image.load("Talimat5.png")

HM0 = pygame.image.load("hm0.png")
HM1 = pygame.image.load("hm1.png")
HM2 = pygame.image.load("hm2.png")
HM3 = pygame.image.load("hm3.png")
HM4 = pygame.image.load("hm4.png")
HM5 = pygame.image.load("hm5.png")
HM6 = pygame.image.load("hm6.png")
HM7 = pygame.image.load("hm7.png")
HM8 = pygame.image.load("hm8.png")
HM9 = pygame.image.load("hm9.png")
HMTopla = pygame.image.load("hmTopla.png")
HMFark = pygame.image.load("hmFark.png")
HMCarp = pygame.image.load("hmCarp.png")
HMBol = pygame.image.load("hmBolme.png")
HMEsittir = pygame.image.load("hmEsittir.png")

seceneklercikis = pygame.image.load("seçeneklerdençıkış.png")
seceneklermenu = pygame.image.load("seçeneklermenüsü.png ")
sesButton = pygame.image.load("sesayarbutton.png")
sesTik = pygame.image.load("sesayartik.png")
sesX = pygame.image.load("sesayarx.png")
emegiGecenler = pygame.image.load("emegigecenlerbutton.png")
ogreticiButton = pygame.image.load("öğreticibutton.png")

usernameScreen = pygame.image.load("username.png")
usernameOkButton = pygame.image.load("username ok.png")

TekrarOynaButton = pygame.image.load("TekrarOynaButton.png")
AnaMenuButton = pygame.image.load("AnaMenüButton.png")
KazanmaScreen = pygame.image.load("KAZANMA EKRANI.png")
KayipScreen = pygame.image.load("KAYIP EKRANI.png")
BerabereScreen = pygame.image.load("BERABERE EKRANI.png")

GameScreen = pygame.image.load("oyun ekranı.png")
sagMenu_inGame = pygame.image.load("sağ parşomen.png")
sagMenuOpen_inGame = pygame.image.load("Sağ Parşomen Açık.png")
solMenu_inGame = pygame.image.load("sol parşomen.png")
solMenuOpen_inGame = pygame.image.load("Sol parşomen açık.png")
YakinlikDuzeyi = pygame.image.load("yakınlık.png")

# KOORDİNATLAR --------------------------------------------------------------------------------------------------------

coordinatText = text.get_rect()
coordinatOynaButton = OynaButton.get_rect()
coordinatSolPencere = SolPencere.get_rect()
coordinatExit = Exit.get_rect()
coordinatVersiyon = Versiyon.get_rect()
coordinatDefterKalem = DefterKalem.get_rect()
coordinatSecenekButton = SecenekButton.get_rect()
coordinatCevaplaTextButton = CevaplaTextButton.get_rect()
coordinatCevaplaTextButton.topleft = (810, 532)

coordinatOgretici1 = Ogretici1.get_rect()
coordinatOgretici2 = Ogretici2.get_rect()
coordinatOgretici3 = Ogretici3.get_rect()
coordinatOgretici4 = Ogretici4.get_rect()
coordinatOgretici5 = Ogretici5.get_rect()

solMenu_inGame_x, solMenu_inGame_y, solMenu_inGame_w, solMenu_inGame_h = 1, 85, 288, 163,
sagMenu_inGame_x, sagMenu_inGame_y, sagMenu_inGame_w, sagMenu_inGame_h = 1621, 95, 298, 167
CevaplaButton_x, CevaplaButton_y, CevaplaButton_w, CevaplaButton_h = 810, 532, 297, 75

oynabutton_x, oynabutton_y, oynabutton_w, oynabutton_h = 35, 365, 345, 95
secenekbtn_x, secenekbtn_y, secenekbtn_w, secenekbtn_h = 35, 490, 380, 68
sesbtn_x, sesbtn_y, sesbtn_w, sesbtn_h =  347, 267, 96, 96
emegGecBtn_x, emegGecBtn_y, emegGecBtn_w, emegGecBtn_h = 151, 545, 590, 144
Ogreticibtn_x, Ogreticibtn_y, Ogreticibtn_w, Ogreticibtn_h = 944, 544, 588, 148

btn0_x, btn0_y, btn0_w, btn0_h = 654, 303, 45, 40
btn1_x, btn1_y, btn1_w, btn1_h = 698, 262, 39, 38

tekrarOyna_x, tekrarOyna_y, tekrarOyna_w, tekrarOyna_h = 596, 560, 210, 210
anaMenuyeDon_x, anaMenuyeDon_y, anaMenuyeDon_w, anaMenuyeDon_h = 1106, 561, 210, 210

coordinatHMNokta = HMNokta.get_rect()
coordinatHMBase = HMBase.get_rect()
coordinatHM0 = HM0.get_rect()
coordinatHM1 = HM1.get_rect()
coordinatHM2 = HM2.get_rect()
coordinatHM3 = HM3.get_rect()
coordinatHM4 = HM4.get_rect()
coordinatHM5 = HM5.get_rect()
coordinatHM6 = HM6.get_rect()
coordinatHM7 = HM7.get_rect()
coordinatHM8 = HM8.get_rect()
coordinatHM9 = HM9.get_rect()
coordinatHMTopla = HMTopla.get_rect()
coordinatHMCarp = HMCarp.get_rect()
coordinatHMFark = HMFark.get_rect()
coordinatHMBol = HMBol.get_rect()
coordinatHMEsittir = HMEsittir.get_rect()
coordinatRotateText = rotateText.get_rect()
coordinatRotateText.topleft = (990, 190)
coordinatTurKontrolText = TurKontrolText.get_rect()
coordinatTurKontrolText.topleft = (870, 910)
coordinatSiraGostergeText = SiraGostergeText.get_rect()
coordinatSiraGostergeText.topleft = (806, 1010)
coordinatYakinlikText = yakinlikText.get_rect()
coordinatYakinlikText.topleft = (830, 710)
coordinatTahminim1 = Tahminim1Text.get_rect()
coordinatTahminim1.topleft = (55, 150)
coordinatRakipTahmin1 = RakipTahmin1Text.get_rect()
coordinatRakipTahmin1.topleft = (1710, 150)

coordinatsecenekcikis = seceneklercikis.get_rect()
coordinatseceneklermenu = seceneklermenu.get_rect()
coordinatsesButton = sesButton.get_rect()
coordinatsesTik = sesTik.get_rect()
coordinatsesX = sesX.get_rect()
coordinatEmegiGecenler = emegiGecenler.get_rect()
coordinatOgreticiButton = ogreticiButton.get_rect()

coordinatUsernameScreen = usernameScreen.get_rect()
coordinatUsernameOkButton = usernameOkButton.get_rect()

coordinatTekrarOynaButton = TekrarOynaButton.get_rect()
coordinatAnaMenuButton = AnaMenuButton.get_rect()
coordinatKazanmaScreen = KazanmaScreen.get_rect()
coordinatKayipScreen = KayipScreen.get_rect()
coordinatBerabereScreen = BerabereScreen.get_rect()

coordinatGameScreen = GameScreen.get_rect()
coordinatSolMenu_inGame = solMenu_inGame.get_rect()
coordinatSolMenuOpen_inGame = solMenuOpen_inGame.get_rect()
coordinatSagMenu_inGame = sagMenu_inGame.get_rect()
coordinatSagMenuOpen_inGame = sagMenuOpen_inGame.get_rect()
coordinatYakinlikDuzeyi = YakinlikDuzeyi.get_rect()

# FONKSİYONLAR --------------------------------------------------------------------------------------------------------
def yaziGirdiSayi(yazi, font, renk, x, y):

    ekranaYazma = font.render(TahminEdiliyor, True, (SiyahRenk))
    yukseklik = ekranaYazma.get_width()
    oynaWindow.blit(ekranaYazma, (x - (yukseklik / 2), y))
def yaziGirdiUsername(yazi, font, renk, x, y):
    ekranaYazma = font.render(username, True, SiyahRenk)
    yukseklik = ekranaYazma.get_width()
    usernameWindow.blit(ekranaYazma, (x - (yukseklik / 2), y))

def anaMenuEkrani():
    MainWindow.fill(BeyazRenk)
    MainWindow.blit(HM0, coordinatHM0)
    MainWindow.blit(HM1, coordinatHM1)
    MainWindow.blit(HM2, coordinatHM2)
    MainWindow.blit(HM3, coordinatHM3)
    MainWindow.blit(HM4, coordinatHM4)
    MainWindow.blit(HM5, coordinatHM5)
    MainWindow.blit(HM6, coordinatHM6)
    MainWindow.blit(HM7, coordinatHM7)
    MainWindow.blit(HM8, coordinatHM8)
    MainWindow.blit(HM9, coordinatHM9)
    MainWindow.blit(HMTopla, coordinatHMTopla)
    MainWindow.blit(HMBol, coordinatHMBol)
    MainWindow.blit(HMCarp, coordinatHMCarp)
    MainWindow.blit(HMFark, coordinatHMFark)
    MainWindow.blit(HMBase, coordinatHMBase)
    MainWindow.blit(HMNokta, coordinatHMNokta)
    MainWindow.blit(HMEsittir, coordinatHMEsittir)
    MainWindow.blit(SolPencere, coordinatSolPencere)
    MainWindow.blit(OynaButton, coordinatOynaButton)
    MainWindow.blit(SecenekButton, coordinatSecenekButton)
    MainWindow.blit(Versiyon, coordinatVersiyon)
    MainWindow.blit(DefterKalem, coordinatDefterKalem)
    MainWindow.blit(Exit, coordinatExit)
    MainWindow.blit(rotateText, coordinatRotateText)
    pygame.display.set_caption("Başlangıç")
    pygame.display.flip()

def usernameEkrani():
    usernameWindow.fill(BeyazRenk)
    usernameWindow.blit(usernameScreen, coordinatUsernameScreen)
    usernameWindow.blit(usernameOkButton, coordinatUsernameOkButton)
    yaziGirdiUsername(username, yazi_90, SiyahRenk, 940, 330)
    pygame.display.flip()

def oyuniciEkrani():
    oynaWindow.fill(BeyazRenk)
    pygame.display.set_caption("Oyun İçi")
    oynaWindow.blit(GameScreen, coordinatGameScreen)
    oynaWindow.blit(YakinlikDuzeyi, coordinatYakinlikDuzeyi)
    oynaWindow.blit(sagMenu_inGame, coordinatSagMenu_inGame)
    oynaWindow.blit(TurKontrolText, coordinatTurKontrolText)
    oynaWindow.blit(solMenu_inGame, coordinatSolMenu_inGame)
    oynaWindow.blit(SiraGostergeText, coordinatSiraGostergeText)
    oynaWindow.blit(yakinlikText, coordinatYakinlikText)
    oynaWindow.blit(CevaplaTextButton, coordinatCevaplaTextButton)
    BilgisayarAdi = yazi_70.render("Bilgisayar", True, SiyahRenk)
    BilgisayarGizliSayi = yazi_70.render("* * * *", True, SiyahRenk)
    oynaWindow.blit(BilgisayarAdi, (1360, 10))
    oynaWindow.blit(BilgisayarGizliSayi, (1700, 25))
    global ZamanText, kalanZaman, gecenZaman

    oyuncu_sayilar_str = ' '.join(map(str, oyuncu_sayilar))
    OyuncuSayisiText = yazi_55.render(oyuncu_sayilar_str, True, SiyahRenk)
    coordinatOyuncuSayisiText = (65, 27)
    oynaWindow.blit(OyuncuSayisiText, coordinatOyuncuSayisiText)
    OyuncuAdi = yazi_90.render(username, True, SiyahRenk)

def KazanmaEkrani():
    kazanmaWindow.fill(BeyazRenk)
    kazanmaWindow.blit(KazanmaScreen, coordinatKazanmaScreen)
    kazanmaWindow.blit(TekrarOynaButton, coordinatTekrarOynaButton)
    kazanmaWindow.blit(AnaMenuButton, coordinatAnaMenuButton)
    pygame.display.flip()

def KayipEkrani():
    kayipWindow.fill(BeyazRenk)
    kayipWindow.blit(KayipScreen, coordinatKayipScreen)
    kayipWindow.blit(TekrarOynaButton, coordinatTekrarOynaButton)
    kayipWindow.blit(AnaMenuButton, coordinatAnaMenuButton)
    pygame.display.flip()

def BerabereEkrani():
    berabereWindow.fill(BeyazRenk)
    berabereWindow.blit(BerabereScreen, coordinatBerabereScreen)
    berabereWindow.blit(TekrarOynaButton, coordinatTekrarOynaButton)
    berabereWindow.blit(AnaMenuButton, coordinatAnaMenuButton)
    pygame.display.flip()

def SecenekEkrani():
    secenekWindow.fill(BeyazRenk)
    emegiGecenlerWindow.fill(BeyazRenk)
    secenekWindow.blit(seceneklermenu, coordinatseceneklermenu)
    secenekWindow.blit(seceneklercikis, coordinatsecenekcikis)
    secenekWindow.blit(emegiGecenler, coordinatEmegiGecenler)
    secenekWindow.blit(ogreticiButton, coordinatOgreticiButton)
    secenekWindow.blit(sesTik, coordinatsesTik)
    secenekWindow.blit(sesButton, coordinatsesButton)
    pygame.display.set_caption("Seçenekler")
    pygame.display.flip()

def YakinlikDuzeyiKontrolleri():

    if TahminEdilen1 == str(rakip_s1):
        yakinlik_derecesi[0] = 1
    elif TahminEdilen1 == str(rakip_s2) or TahminEdilen1 == str(rakip_s3) or TahminEdilen1 == str(rakip_s4):
        yakinlik_derecesi[0] = "!"

    if TahminEdilen2 == str(rakip_s2):
        yakinlik_derecesi[1] = 1
    elif TahminEdilen2 == str(rakip_s1) or TahminEdilen2 == str(rakip_s3) or TahminEdilen2 == str(rakip_s4):
        yakinlik_derecesi[1] = "!"

    if TahminEdilen3 == str(rakip_s3):
        yakinlik_derecesi[2] = 1
    elif TahminEdilen3 == str(rakip_s1) or TahminEdilen3 == str(rakip_s2) or TahminEdilen3 == str(rakip_s4):
        yakinlik_derecesi[2] = "!"

    if TahminEdilen4 == str(rakip_s4):
        yakinlik_derecesi[3] = 1
    elif TahminEdilen4 == str(rakip_s1) or TahminEdilen4 == str(rakip_s2) or TahminEdilen4 == str(rakip_s3):
        yakinlik_derecesi[3] = "!"

def RakipTahminAsamasi():
    rakip_TahminEdiyor = random.sample(range(1, 10), 4)
    print("RakipTahmini: ", rakip_TahminEdiyor)
    rakipTahmini = ''.join(map(str, rakip_TahminEdiyor))
    RakibinTahminleri.append(rakipTahmini)

    return rakip_TahminEdiyor

def RakipYakinlikDuzeyiKontrolleri():

    if int(rakipTahmini_1) == int(oyuncu_s1) and int(rakipTahmini_2) == int(oyuncu_s2) and int(rakipTahmini_3) == int(oyuncu_s3) and int(rakipTahmini_4) == int(oyuncu_s4):
        print("BİLGİSAYAR KAZANDI!")
        CevaplaTextButton = yazi_90.render("KAYBETTİN", True, SiyahRenk)
        KayipWindowOpen= True
        OynaWindowOpen = False

def Donus():
    global username, baslangicZamani, TahminEdilen1, TahminEdilen2, TahminEdilen3, TahminEdilen4, oyuncu_s1, \
    oyuncu_s2, oyuncu_s3, oyuncu_s4, rakip_s1, rakip_s2, rakip_s3, rakip_s4, Tur, yakinlik_derecesi, CevaplaTextButton, \
    rakip_sayilar, oyuncu_sayilar

    baslangicZamani = None
    Tahminlerim.clear()
    TahminEdilen1 = ""
    TahminEdilen2 = ""
    TahminEdilen3 = ""
    TahminEdilen4 = ""
    rakip_sayilar = random.sample(range(1, 10), 4)
    oyuncu_sayilar = random.sample(range(1, 10), 4)
    yakinlik_derecesi[0] = 0
    yakinlik_derecesi[1] = 0
    yakinlik_derecesi[2] = 0
    yakinlik_derecesi[3] = 0
    rakip_sayilar = random.sample(range(1, 10), 4)
    oyuncu_sayilar = random.sample(range(1, 10), 4)
    CevaplaTextButton = yazi_90.render("CEVAPLA", True, SiyahRenk)
    Tur = 1
    oyuncu_s1, oyuncu_s2, oyuncu_s3, oyuncu_s4 = oyuncu_sayilar
    rakip_s1, rakip_s2, rakip_s3, rakip_s4 = rakip_sayilar
    pygame.mixer_music.play(-1, 3.0)

def OgreticiDongusu():
    global OgreticiWindowOpen, SecenekWindowOpen
    ogreticiWindow.fill(BeyazRenk)
    ogreticiWindow.blit(Ogretici1, coordinatOgretici1)
    pygame.display.flip()
    pygame.time.delay(5000)
    ogreticiWindow.fill(BeyazRenk)
    ogreticiWindow.blit(Ogretici2, coordinatOgretici2)
    pygame.display.flip()
    pygame.time.delay(5000)
    ogreticiWindow.fill(BeyazRenk)
    ogreticiWindow.blit(Ogretici3, coordinatOgretici3)
    pygame.display.flip()
    pygame.time.delay(5000)
    ogreticiWindow.blit(Ogretici4, coordinatOgretici4)
    pygame.display.flip()
    pygame.time.delay(5000)
    ogreticiWindow.blit(Ogretici5, coordinatOgretici5)
    pygame.display.flip()
    pygame.time.delay(5000)
    OgreticiWindowOpen = False
    SecenekWindowOpen = True

def EmegiGecenlerEkrani():
    secenekWindow.fill(BeyazRenk)
    EmegiGecenlerText = yazi_70.render("""
    Anıl Yetim      

    Bilal Korkmaz    

    Emirhan Yalçın    

    Salih Sercan Turgut  

    Yusuf Gundogdu
    """, True, SiyahRenk)
    coordinatEmegiGecenlerText = (256, 88)
    emegiGecenlerWindow.blit(EmegiGecenlerText, coordinatEmegiGecenlerText)
    emegiGecenlerWindow.blit(seceneklercikis, coordinatsecenekcikis)
    pygame.display.flip()

# OYUN DÖNGÜSÜ ---------------------------------------------------------------------------------------------------------

while Base:
    for event in pygame.event.get():
        mouse_x, mouse_y = pygame.mouse.get_pos()
        MouseMotionControl = (event.type == pygame.MOUSEMOTION)
        MouseButtonDownControl = (event.type == pygame.MOUSEBUTTONDOWN)
        TextInputControl = (event.type == pygame.TEXTINPUT)

        if event.type == pygame.QUIT:
            Base = False
# MOUSE TUŞUNA BASILDIĞINDA YAPILACAK İŞLEMLER -------------------------------------------------------------------------
        elif MouseButtonDownControl:
            if event.button == 1:
                mouse_x, mouse_y = pygame.mouse.get_pos()
                if oynabutton_x < mouse_x < oynabutton_x + oynabutton_w and oynabutton_y < mouse_y < oynabutton_y + oynabutton_h:
                    usernameWindowOpen = True
                    print("OyunEkranı Açıldı")  #Sadece ufak kontroller :)

                elif secenekbtn_x < mouse_x < secenekbtn_x + secenekbtn_w and secenekbtn_y < mouse_y < secenekbtn_y + secenekbtn_h:
                    SecenekWindowOpen = True
                    print("SecenekEkranı Açıldı")  #Sadece ufak kontroller :)

                elif btn0_x < mouse_x < btn0_x + btn0_w and btn0_y < mouse_y < btn0_y + btn0_h:
                    rotateText = yazi_40.render("0", True, SiyahRenk)
                    rotateText = pygame.transform.rotate(rotateText, -45)
                    print("0'a basıldı.")  #Sadece ufak kontroller :)

                elif btn1_x < mouse_x < btn1_x + btn0_w and btn1_y < mouse_y < btn1_y + btn1_h:
                    rotateText = yazi_40.render("1", True, SiyahRenk)
                    rotateText = pygame.transform.rotate(rotateText, -45)
                    print("1'a basıldı.")  #Sadece ufak kontroller :)

# ANA MENÜ EKRANI -----------------------------------------------------------------------------------------------------

    if not OynaWindowOpen and not SecenekWindowOpen and MainMenuOpen and not usernameWindowOpen and not KazanmaWindowOpen \
            and not KayipWindowOpen and not BerabereWindowOpen and not OgreticiWindowOpen and not EmegiGecenlerWindowOpen:
        anaMenuEkrani()

# OYUN İÇİ EKRANI(USERNAME) --------------------------------------------------------------------------------------------

    elif usernameWindowOpen:
        usernameEkrani()
        if TextInputControl:
            if len(username) < 10:
                username += event.text
                print(username)  # Sadece Ufak Kontroller :)

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_BACKSPACE:
                username = username[:-1]

        if MouseButtonDownControl:
            usernameOk_x, usernameOk_y, usernameOk_w, usernameOk_h = 795, 569, 316, 148
            if usernameOk_x < mouse_x < usernameOk_x + usernameOk_w and usernameOk_y < mouse_y < usernameOk_y + usernameOk_h:
                if len(username) < 1:
                    print("a")
                    UyariYazisi = yazi_55.render("Lütfen en az 1 Harf Girin.", True, SiyahRenk)
                    usernameWindow.blit(UyariYazisi, (710, 820))
                    pygame.display.flip()
                    pygame.time.delay(1000)
                else:
                    print("ok'a tıklandı.") # Sadece ufak kontroller :)
                    usernameWindowOpen = False
                    OynaWindowOpen = True

# OYUN İÇİ EKRANI(OYNANIŞ) ---------------------------------------------------------------------------------------------

    elif not KazanmaWindowOpen and not KayipWindowOpen and not BerabereWindowOpen and OynaWindowOpen:
        oyuniciEkrani()
        yaziGirdiSayi(TahminEdiliyor, yazi_90, SiyahRenk, 940, 317)
        OyuncuAdi = yazi_70.render(username, True, SiyahRenk)
        oynaWindow.blit(OyuncuAdi, (315, 10))

        if baslangicZamani is None:
            baslangicZamani = pygame.time.get_ticks()
            gecenZaman = pygame.time.get_ticks() - baslangicZamani
            kalanZaman_saniye = kalanZaman // 1000
            coordinatZamanText = (930, 30)
            baslangicZamani = pygame.time.get_ticks()
            print("Zamanlayıcı sıfırlandı.")      # Sadece Kontrol Amaçlı :)

            rakip_sayilar = random.sample(range(1, 10), 4)
            oyuncu_sayilar = random.sample(range(1, 10), 4)
            oyuncu_s1, oyuncu_s2, oyuncu_s3, oyuncu_s4 = oyuncu_sayilar
            rakip_s1, rakip_s2, rakip_s3, rakip_s4 = rakip_sayilar

            print("Bilgisayar Sayıları", rakip_s1, rakip_s2, rakip_s3, rakip_s4)
            print("Oyuncu Sayıları", oyuncu_s1, oyuncu_s2, oyuncu_s3, oyuncu_s4)

        gecenZaman = pygame.time.get_ticks() - baslangicZamani
        kalanZaman = max(0, 16 * 1000 - gecenZaman)

        if Tur % 2 == 1:
            kalanZaman = max(0, 16 * 1000 - gecenZaman)
            SiraGostergeText = yazi_70.render("Senin Sıran", True, SiyahRenk)
            coordinatSiraGostergeText.topleft = (806, 1010)
            RakipTahminAsamasinda = False

        elif Tur == 16:
            print("TUR 16'ya geldi")
            CevaplaTextButton = yazi_90.render("BERABERE", True, SiyahRenk)
            BerabereWindowOpen = True
            OynaWindowOpen = False

        else:
            kalanZaman = max(0, 3 * 1000 - gecenZaman)
            RakipTahminAsamasinda = True
            SiraGostergeText = yazi_55.render("Rakibin Sırası", True, SiyahRenk)
            coordinatSiraGostergeText.topleft = (826, 1020)
            TurKontrolText = yazi_90.render("{}.Tur".format(Tur), True, SiyahRenk)
            TurGecildi = False

        if RakipTahminAsamasinda:
            RakipTahminAsamasi()
            rakip_TahminEdiyor = RakipTahminAsamasi()
            rakipTahmini_1, rakipTahmini_2, rakipTahmini_3, rakipTahmini_4 = rakip_TahminEdiyor
            RakipYakinlikDuzeyiKontrolleri()

        kalanZaman_saniye = kalanZaman // 1000
        ZamanText = yazi_90.render(str(kalanZaman_saniye), True, SiyahRenk)
        coordinatZamanText = (930,30)

        if kalanZaman <= 0:
            baslangicZamani = pygame.time.get_ticks()
            Tur += 1
            TurKontrolText = yazi_90.render("{}.Tur" .format(Tur), True, SiyahRenk)
            kalanZaman_saniye = kalanZaman // 1000
            ZamanText = (yazi_90.render(str(kalanZaman_saniye), True, SiyahRenk))
            coordinatZamanText = (930, 30)
            print("Zamanlayıcı sıfırlandı!") # Sadece Ufak Kontroller :)
            coordinatZamanText = (930, 30)

        if MouseMotionControl:
            if solMenu_inGame_x < mouse_x < solMenu_inGame_x + solMenu_inGame_w and solMenu_inGame_y < mouse_y < solMenu_inGame_y + solMenu_inGame_h:

                for tahmin in Tahminlerim:
                    Tahminim1Text = yazi_55.render(tahmin, True, SiyahRenk)
                oynaWindow.blit(solMenuOpen_inGame, coordinatSolMenuOpen_inGame)
                oynaWindow.blit(Tahminim1Text, coordinatTahminim1)

            elif sagMenu_inGame_x < mouse_x < sagMenu_inGame_x + sagMenu_inGame_w and sagMenu_inGame_y < mouse_y < sagMenu_inGame_y + sagMenu_inGame_h:
                for rakiptahmin in RakibinTahminleri:
                    RakipTahmin1Text = yazi_55.render(rakiptahmin, True, SiyahRenk)
                oynaWindow.blit(sagMenuOpen_inGame, coordinatSagMenuOpen_inGame)
                oynaWindow.blit(RakipTahmin1Text, coordinatRakipTahmin1)

        if TextInputControl:
            if event.text.isdigit():
                if len(TahminEdiliyor) < 4:
                    TahminEdiliyor += event.text
                    print(TahminEdiliyor)  # Sadece Ufak Kontroller :)

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_BACKSPACE:
                TahminEdiliyor = TahminEdiliyor[:-1]

            if event.key == pygame.K_RETURN and Tur % 2 == 1 and len(TahminEdiliyor) == 4:
                baslangicZamani = pygame.time.get_ticks()
                TurGecildi = True
                Tur += 1
                TurKontrolText = yazi_90.render("{}.Tur".format(Tur), True, SiyahRenk)
                print("Zamanlayıcı sıfırlandı!")  # Sadece Ufak Kontroller :)
                print("Cevaplandı.")  # Sadece Ufak Kontroller :)
                Tahminlerim.append(TahminEdiliyor)
                TahminEdiliyor = ""

        if len(TahminEdiliyor) == 4:
            TahminEdilen1, TahminEdilen2, TahminEdilen3, TahminEdilen4 = TahminEdiliyor

        if MouseButtonDownControl:
            if CevaplaButton_x < mouse_x < CevaplaButton_x + CevaplaButton_w and CevaplaButton_y < mouse_y < CevaplaButton_y + CevaplaButton_h and Tur % 2 == 1 and len(TahminEdiliyor) == 4:
                baslangicZamani = pygame.time.get_ticks()
                Tur += 1
                TurGecildi = True
                TurKontrolText = yazi_90.render("{}.Tur".format(Tur), True, SiyahRenk)
                print("Zamanlayıcı sıfırlandı!")  # Sadece Ufak Kontroller :)
                print("Cevaplandı.")  # Sadece Ufak Kontroller :)
                Tahminlerim.append(TahminEdiliyor)
                TahminEdiliyor = ""

        if TurGecildi:
            YakinlikDuzeyiKontrolleri()
            yakinlikText = yazi_90.render(" ".join(map(str, yakinlik_derecesi)), True, (0, 0, 0))
            if yakinlik_derecesi[0] == 1 and yakinlik_derecesi[1] == 1 and yakinlik_derecesi[2] == 1 and yakinlik_derecesi[3] == 1:
                coordinatCevaplaTextButton.topleft = (780, 532)
                CevaplaTextButton = yazi_90.render("KAZANDIN!", True, SiyahRenk)
                KazanmaWindowOpen = True
                OynaWindowOpen = False

        oynaWindow.blit(SiraGostergeText, coordinatSiraGostergeText)
        oynaWindow.blit(ZamanText, coordinatZamanText)
        saat.tick(60)
        pygame.display.flip()

# KAZANMA & KAYBETME & BERABERE EKRANLARI ------------------------------------------------------------------------------

    elif KazanmaWindowOpen:
        KazanmaEkrani()
        pygame.mixer.music.stop()
        if MouseButtonDownControl:
            if tekrarOyna_x < mouse_x < tekrarOyna_x + tekrarOyna_w and tekrarOyna_y < mouse_y < tekrarOyna_y + tekrarOyna_h:
                KazanmaWindowOpen = False
                OynaWindowOpen = True
                rakip_sayilar = random.sample(range(1, 10), 4)
                oyuncu_sayilar = random.sample(range(1, 10), 4)
                CevaplaTextButton = yazi_90.render("CEVAPLA", True, SiyahRenk)
                Donus()
                Tur = 1

            if anaMenuyeDon_x < mouse_x < anaMenuyeDon_x + anaMenuyeDon_w and anaMenuyeDon_y < mouse_y < anaMenuyeDon_y + anaMenuyeDon_h:
                KazanmaWindowOpen = False
                OynaWindowOpen = False
                Donus()
                username = ""

    elif KayipWindowOpen:
        KayipEkrani()
        pygame.mixer.music.stop()
        if MouseButtonDownControl:
            if tekrarOyna_x < mouse_x < tekrarOyna_x + tekrarOyna_w and tekrarOyna_y < mouse_y < tekrarOyna_y + tekrarOyna_h:
                KayipWindowOpen = False
                Donus()
                OynaWindowOpen = True

            if anaMenuyeDon_x < mouse_x < anaMenuyeDon_x + anaMenuyeDon_w and anaMenuyeDon_y < mouse_y < anaMenuyeDon_y + anaMenuyeDon_h:
                KayipWindowOpen = False
                OynaWindowOpen = False
                Donus()
                username = ""

    elif BerabereWindowOpen:
        BerabereEkrani()
        pygame.mixer.music.stop()
        if MouseButtonDownControl:
            if tekrarOyna_x < mouse_x < tekrarOyna_x + tekrarOyna_w and tekrarOyna_y < mouse_y < tekrarOyna_y + tekrarOyna_h:
                BerabereWindowOpen = False
                Donus()
                OynaWindowOpen = True

            if anaMenuyeDon_x < mouse_x < anaMenuyeDon_x + anaMenuyeDon_w and anaMenuyeDon_y < mouse_y < anaMenuyeDon_y + anaMenuyeDon_h:
                BerabereWindowOpen = False
                OynaWindowOpen = False
                Donus()
                username = ""
# SEÇENEKLER EKRANI ----------------------------------------------------------------------------------------------------

    elif SecenekWindowOpen and not EmegiGecenlerWindowOpen and not OgreticiWindowOpen:
        SecenekEkrani()
        secenekgeributton_x, secenekgeributton_y, secenekgeributton_W, secenekgeributton_h = 1570, 873, 135, 132
        if MouseButtonDownControl:
            if secenekgeributton_x < mouse_x < secenekgeributton_x + secenekgeributton_W and secenekgeributton_y < mouse_y < secenekgeributton_y + secenekgeributton_h:
                MainMenuOpen = True
                SecenekWindowOpen = False
                print("Ana menüye dönüldü")  # Deneme 1,2,3

            if sesbtn_x < mouse_x < sesbtn_x + sesbtn_w and sesbtn_y < mouse_y < sesbtn_y + sesbtn_h:
                if Volume:
                    pygame.mixer.music.set_volume(0)
                    pygame.mixer.music.pause()
                    secenekWindow.blit(sesX, coordinatsesX)
                    secenekWindow.blit(sesButton, coordinatsesButton)
                    pygame.display.flip()
                    Volume = False
                else:
                    pygame.mixer.music.set_volume(1)
                    pygame.mixer.music.unpause()
                    secenekWindow.blit(sesTik, coordinatsesTik)
                    secenekWindow.blit(sesButton, coordinatsesButton)
                    pygame.display.flip()
                    Volume = True

            if Ogreticibtn_x < mouse_x < Ogreticibtn_x + Ogreticibtn_w and Ogreticibtn_y < mouse_y < Ogreticibtn_y + Ogreticibtn_h:
                secenekWindow.fill(BeyazRenk)
                OgreticiWindowOpen = True
                SecenekWindowOpen = False

            if emegGecBtn_x < mouse_x < emegGecBtn_x + emegGecBtn_w and emegGecBtn_y < mouse_y < emegGecBtn_y + emegGecBtn_h:
                secenekWindowOpen = False
                EmegiGecenlerWindowOpen = True
                print("Emeği Geçenler")

# ÖGRETİCİ EKRANI ------------------------------------------------------------------------------------------------------

    elif OgreticiWindowOpen:
        OgreticiDongusu()

# EMEĞİ GEÇENLER EKRANI ------------------------------------------------------------------------------------------------

    elif EmegiGecenlerWindowOpen:
        coordinatsecenekcikis.topleft = (-200, -200)
        secenekgeributton_x, secenekgeributton_y, secenekgeributton_W, secenekgeributton_h = 1365, 682, 111, 131
        EmegiGecenlerEkrani()
        if MouseButtonDownControl:
            if secenekgeributton_x < mouse_x < secenekgeributton_x + secenekgeributton_W and secenekgeributton_y < mouse_y < secenekgeributton_y + secenekgeributton_h:
                EmegiGecenlerWindowOpen = False
                print("Seçenekler'e Dönüldü")  # Deneme 1,2,3
                secenekWindowOpen = True
                coordinatsecenekcikis.topleft = (0, 0)

pygame.quit()
