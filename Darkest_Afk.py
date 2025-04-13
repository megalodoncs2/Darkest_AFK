from pygame import* 
import time as tm
from random import randint
bg = image.load('fon7.png')
bg2 = image.load('fon8.jpg')
bg3 = image.load('KARTA.png')
window = display.set_mode((400,700))
w1,h2 = window.get_size()
bg=  transform.scale(image.load('fon7.png'),(w1,h2))
bg2=  transform.scale(image.load('fon8.jpg'),(w1,h2))
window.blit( bg,(0,0)) 
glav_kart = image.load('glavna_kartinka/glav-kart.png')
window.blit(glav_kart,(400,500))
FPS = 60
font.init()
my_font = font.Font(None,40)
peremena = 'главний фон'

WHITE = (255, 255, 255)
RED = (200, 0, 0)
GREEN = (0, 200, 0)
BLACK = (0, 0, 0)
class GameSprite(sprite.Sprite):
    def __init__(self, images, speed , x,y , w,h):
        self.image = transform.scale(image.load(images),(w,h))
        self.rect = self.image.get_rect()
        self.speed = speed
        self.rect.x = x
        self.rect.y = y
        self.width = w
        self.height = h
    def risovka(self):
        window.blit(self.image, (self.rect.x, self.rect.y))

class Player(GameSprite):
    pass
    


        

#(self, images, speed , x,y , w,h):

#----------------Skills--------------------------------------

class Button:
    def __init__(self, w, h, images, x, y, ):
           self.width = w
           self.height = h
           self.image = image.load(images)
           self.image = transform.scale(self.image, (self.width, self.height))
           self.rect = self.image.get_rect()
           self.rect.x = x
           self.rect.y = y
           
           self.is_kasanie = False
           
    def draw_btn(self, bg):
       bg.blit(self.image, (self.rect.x, self.rect.y))
       
       
       
    def check_kasanie(self, mouse_pos, event):
        self.is_kasanie = self.rect.collidepoint(mouse_pos)
        if self.is_kasanie and event.type == MOUSEBUTTONDOWN:
            return True
        
#--------------------------------------

#def __init__(self, w, h, images, x, y, ):
#-----------------------------------------------------------------------------------------------------
geroy_red_Sir_Joseph = Button(80,70,'geroy_avatar/red/Damger_Class/Sir_Joseph3.png',15,10)
geroy_red_Chas = Button(80,70,'geroy_avatar/red/Damger_Class/Chas3.png',100,10)
geroy_red_Drowzet = Button(80,70,'geroy_avatar/red/Damger_Class/Drowzet3.png',185,10)
geroy_red_Ridael =  Button(80,70,'geroy_avatar/red/Damger_Class/Ridael3.png',270,10)
geroy_red_Tiara =  Button(80,70,'geroy_avatar/red/Damger_Class/Tiara3.png',15,85)
#-------------------------------------------------------------------------------------------------
geroy_red_Brina = Button(80,70,'geroy_avatar/red/Support_Class/Brina3.png',100,85)
geroy_red_Drogo = Button(80,70,'geroy_avatar/red/Support_Class/Drogo3.png',185,85)
geroy_red_Harumi = Button(80,70,'geroy_avatar/red/Support_Class/Harumi3.png',270,85)
geroy_red_Ja_Van = Button(80,70,'geroy_avatar/red/Support_Class/JaVan3.png',15,165)
geroy_red_Marylee = Button(80,70,'geroy_avatar/red/Support_Class/Marylee3.png',100,165)

geroy_red_Airon = Button(80,70,'geroy_avatar/red/Tank_Class/Airon3.png',185,165)
geroy_red_Condrat = Button(80,70,'geroy_avatar/red/Tank_Class/Condrat3.png',270,165)
geroy_red_Gabriella = Button(80,70,'geroy_avatar/red/Tank_Class/Gabriella3.png',15,250)
geroy_red_Ghorm= Button(80,70,'geroy_avatar/red/Tank_Class/Ghorm3.png',15,250)
geroy_red_Ingrid = Button(80,70,'geroy_avatar/red/Tank_Class/Ingrid3.png',100,250)


#-------------------------------------





#def __init__(self, w, h, images, x, y, ):
house = Button(80,70,'glavna_kartinka/button_house.png',0,630)
karta = Button(80,70,'glavna_kartinka/button_karta.png',80,630)
LVL =   Button(85,70,'glavna_kartinka/button_LVL.png',159,630)
geroy = Button(80,70,'glavna_kartinka/button_geroy.png',241,630)
back =  Button(82,70,'glavna_kartinka/button_back.png',321,630)
pyti =  Button(0,0,'glavna_kartinka/button_pyti.png',0,250)






class Character:
    def __init__(self,  img, health, damage,x,y,w1,h2):
        self.x = x
        self.y = y
        self.img = transform.scale(image.load(img),(w1,h2))
        self.health = health
        self.max_health = health
        self.damage = damage
        self.damage_texts = []  # Список для хранения урона

    def draw(self, surface):
        surface.blit(self.img, (self.x, self.y))
        self.draw_health_bar(surface)
        self.draw_damage_texts(surface)

    def draw_health_bar(self, surface):
        draw.rect(surface, RED, (self.x, self.y - 10, 50, 5))
        draw.rect(surface, GREEN, (self.x, self.y - 10, 50 * (self.health / self.max_health), 5))

    def draw_damage_texts(self, surface):
        for dmg in self.damage_texts:

           
            text = my_font.render(str(dmg[0]), True, (255, 255, 0))
            surface.blit(text, (self.x + 20, dmg[1]))  # Урон уходит вверх
        self.damage_texts = [(dmg[0], dmg[1] - 1) for dmg in self.damage_texts if dmg[1] > self.y - 40]  # Удаление текста

    def take_damage(self, amount):
        self.health -= amount
        self.damage_texts.append([amount, self.y])  # Добавляем урон в список
    



peremena_geroy = 0
# def __init__(self, img, health, damage,x,y,w1,h2):
#-------------------Damger-------------------------------
Damager_Class_Agra =        Character("geroy/Damger_Class/Agra.png", 100,50,100 ,100,50,100)
Damager_Class_Avalon =      Character("geroy/Damger_Class/Avalon.png",  100,50,150 ,250,50,100)
Damager_Class_Chas =        Character("geroy/Damger_Class/Chas.png",  100,50,150 ,150,50,100)
Damager_Class_Drowzet =     Character("geroy/Damger_Class/Drowzet.png",  100,50,150 ,150,50,100)
Damager_Class_Lilith =      Character("geroy/Damger_Class/Lilith.png",  100,50,150 ,150,50,100)
Damager_Class_Morrigan =    Character("geroy/Damger_Class/Morrigan.png",  100,50,150 ,150,50,100)
Damager_Class_Ridael =      Character("geroy/Damger_Class/Ridael.png", 100,50,150 ,150,50,100)
Damager_Class_Sir_Joseph =  Character("geroy/Damger_Class/Sir_Joseph.png", 100,50,150 ,150,50,100)
Damager_Class_Tiara =       Character("geroy/Damger_Class/Tiara.png", 100,50,150 ,150,50,100)
Damager_Class_Violet =      Character("geroy/Damger_Class/Violet.png", 100,50,50 ,50,50,100)
Damager_Class_Ziuk =        Character("geroy/Damger_Class/Ziuk.png", 100,50,50 ,50,50,100)
Damager_Class_ZikZak =      Character("geroy/Damger_Class/ZikZak.png", 100,50,50 ,50,50,100)
 #---------------------Support-----------------------------
Support_Class_Brina =       Character("geroy/Support_Class/Brina.png", 100,50,50 ,50,50,100)
Support_Class_Drogo=        Character("geroy/Support_Class/Drogo.png", 100,50,50 ,50,50,100)
Support_Class_Harumi =      Character("geroy/Support_Class/Harumi.png", 100,50,50 ,50,50,100)
Support_Class_Ja_Van =      Character("geroy/Support_Class/Ja_Van.png", 100,50,50 ,50,50,100)
Support_Class_Marylee =     Character("geroy/Support_Class/Marylee.png", 100,50,50 ,50,50,100)
Support_Class_NurZak =      Character("geroy/Support_Class/NurZak.png", 100,50,50 ,50,50,100)
Support_Class_Rigz_A=       Character("geroy/Support_Class/Rigz_Ash.png", 100,50,50 ,50,50,100)
Support_Class_Rose =        Character("geroy/Support_Class/Rose.png", 100,50,50 ,50,50,100)
Support_Class_Selina=       Character("geroy/Support_Class/Selina.png", 100,50,50 ,50,50,100)
Support_Class_Tilio =       Character("geroy/Support_Class/Tilion.png", 100,50,50 ,50,50,100)
# #-------------------Tank----------------------------------
Tank_Class_Airon =          Character("geroy/Tank_Class/Airon.png", 100,50,50 ,50,50,100)
Tank_Class_Condrat=         Character("geroy/Tank_Class/Condrat.png", 100,50,50 ,50,50,100)
Tank_Class_Gabriella =      Character("geroy/Tank_Class/Gabriella.png", 100,50,50 ,50,50,100)
Tank_Class_Ghorm =          Character("geroy/Tank_Class/Ghorm.png", 100,50,50 ,50,50,100)
Tank_Class_Ingrid =         Character("geroy/Tank_Class/Ingrid.png", 100,50,50 ,50,50,100)
Tank_Class_Kuldjar =        Character("geroy/Tank_Class/Kuldjar.png", 100,50,50 ,50,50,100)
Tank_Class_Larion =         Character("geroy/Tank_Class/Larion.png", 100,50,50 ,50,50,100)
Tank_Class_Rabba =          Character("geroy/Tank_Class/Rabba.png", 100,50,50 ,50,50,100)
Tank_Class_Tao =            Character("geroy/Tank_Class/Tao.png", 100,50,50 ,50,50,100)
Tank_Class_Tomas =          Character("geroy/Tank_Class/Tomas.png", 100,50,50 ,50,50,100)
Tank_Class_Zoryg =          Character("geroy/Tank_Class/Zoryg.png", 100,50,50 ,50,50,100)
#----------------------BOSS------------------------
boss =   Character("BOSS1.png", 1000,randint(20,50),200 ,200,50,100)
        
clock = time.Clock()
game = True
team=[]
while game:
    for e in event.get():
        if e.type == KEYDOWN:
            if e.key == K_SPACE and peremena == "битва":

                boss.take_damage(team[0].damage + team[1].damage+ team[2].damage)
                boss.draw_damage_texts(window)
                team[randint(0,2)].take_damage(randint(20,50))

                
            if e.key == K_ESCAPE:
                game = False
                


        if e.type == MOUSEBUTTONDOWN and e.button == 3:
            # print(2)
            mous2 = mouse.get_pos()
            
            #--------------Damger class------------------------
            if geroy_red_Sir_Joseph.check_kasanie(mous2, e):
                geroy_red_Sir_Joseph.image = image.load('geroy_avatar/red/Damger_Class/Sir_Joseph3.png')
                geroy_red_Sir_Joseph.image = transform.scale(geroy_red_Sir_Joseph.image, (80,70))
                peremena_geroy -= 1
                try:
                    team.remove(Damager_Class_Sir_Joseph)
                except:
                    pass

            elif geroy_red_Chas.check_kasanie(mous2, e):
                geroy_red_Chas.image = image.load('geroy_avatar/red/Damger_Class/Chas3.png')
                geroy_red_Chas.image = transform.scale(geroy_red_Chas.image, (80,70))
                peremena_geroy -= 1 
                try:

                    team.remove(Damager_Class_Chas)
                except:
                    pass
            elif geroy_red_Drowzet.check_kasanie(mous2, e):
                geroy_red_Drowzet.image = image.load('geroy_avatar/red/Damger_Class/Drowzet3.png')
                geroy_red_Drowzet.image = transform.scale(geroy_red_Drowzet.image, (80,70))
                peremena_geroy -= 1 
                try:

                    team.remove(Damager_Class_Drowzet)
                except:
                    pass
            elif geroy_red_Ridael.check_kasanie(mous2, e):
                geroy_red_Ridael.image = image.load('geroy_avatar/red/Damger_Class/Ridael3.png')
                geroy_red_Ridael.image = transform.scale(geroy_red_Ridael.image, (80,70))
                peremena_geroy -= 1 
                try:
                    team.remove(Damager_Class_Ridael )
                except:
                    pass
            elif geroy_red_Tiara.check_kasanie(mous2, e):
                geroy_red_Tiara.image = image.load('geroy_avatar/red/Damger_Class/Tiara3.png')
                geroy_red_Tiara.image = transform.scale(geroy_red_Tiara.image, (80,70))
                peremena_geroy -= 1 
                try:
                    team.remove(Damager_Class_Tiara)
                except:
                    pass
            #--------------Support class------------------------
            elif geroy_red_Brina.check_kasanie(mous2, e):
                geroy_red_Brina.image = image.load('geroy_avatar/red/Support_Class/Brina3.png')
                geroy_red_Brina.image = transform.scale(geroy_red_Brina.image, (80,70))
                peremena_geroy -= 1 
                try:
                    team.remove(Support_Class_Brina)
                except:
                    pass
            elif geroy_red_Drogo.check_kasanie(mous2, e):
                geroy_red_Drogo.image = image.load('geroy_avatar/red/Support_Class/Drogo3.png')
                geroy_red_Drogo.image = transform.scale(geroy_red_Drogo.image, (80,70))
                peremena_geroy -= 1 
                try:
                    team.remove(Support_Class_Drogo)
                except:
                    pass
            elif geroy_red_Harumi.check_kasanie(mous2, e):
                geroy_red_Harumi.image = image.load('geroy_avatar/red/Support_Class/Harumi3.png')
                geroy_red_Harumi.image = transform.scale(geroy_red_Harumi.image, (80,70))
                peremena_geroy -= 1 
                try:
                    team.remove(Support_Class_Harumi)
                except:
                    pass
            elif geroy_red_Ja_Van.check_kasanie(mous2, e):
                geroy_red_Ja_Van.image = image.load('geroy_avatar/red/Support_Class/JaVan3.png')
                geroy_red_Ja_Van.image = transform.scale(geroy_red_Ja_Van.image, (80,70))
                peremena_geroy -= 1 
                try:
                    team.remove(Support_Class_Ja_Van)
                except:
                    pass
            elif geroy_red_Marylee.check_kasanie(mous2, e):
                geroy_red_Marylee.image = image.load('geroy_avatar/red/Support_Class/Marylee3.png')
                geroy_red_Marylee.image = transform.scale(geroy_red_Marylee.image, (80,70))
                peremena_geroy -= 1   
                try:
                    team.remove(Support_Class_Marylee)  
                except:
                    pass
            #--------Tank class---------------------------
            elif geroy_red_Airon.check_kasanie(mous2, e):
                geroy_red_Airon.image = image.load('geroy_avatar/red/Tank_Class/Airon3.png')
                geroy_red_Airon.image = transform.scale(geroy_red_Airon.image, (80,70))
                peremena_geroy -= 1  
                try:
                    team.remove(Tank_Class_Airon)   
                except:
                    pass
            elif geroy_red_Condrat.check_kasanie(mous2, e):
                geroy_red_Condrat.image = image.load('geroy_avatar/red/Tank_Class/Condrat3.png')
                geroy_red_Condrat.image = transform.scale(geroy_red_Condrat.image, (80,70))
                peremena_geroy -= 1   
                try:

                    team.remove(Tank_Class_Condrat)  
                except:
                    pass
            elif geroy_red_Gabriella.check_kasanie(mous2, e):
                geroy_red_Gabriella.image = image.load('geroy_avatar/red/Tank_Class/Gabriella3.png')
                geroy_red_Gabriella.image = transform.scale(geroy_red_Gabriella.image, (80,70))
                peremena_geroy -= 1     
                try:

                    team.remove(Tank_Class_Gabriella)
                except:
                    pass
            elif geroy_red_Ghorm.check_kasanie(mous2, e):
                geroy_red_Ghorm.image = image.load('geroy_avatar/red/Tank_Class/Ghorm3.png')
                geroy_red_Ghorm.image = transform.scale(geroy_red_Ghorm.image, (80,70))
                peremena_geroy -= 1  
                try:
                    team.remove(Tank_Class_Ghorm)
                except:
                    pass
            

            elif geroy_red_Ingrid.check_kasanie(mous2, e):
                geroy_red_Ingrid.image = image.load('geroy_avatar/red/Tank_Class/Ingrid3.png')
                geroy_red_Ingrid.image = transform.scale(geroy_red_Ingrid.image, (80,70))
                peremena_geroy -= 1 
                try:
                    team.remove(Tank_Class_Ingrid)
                except:
                    pass
                    
                



        if e.type == MOUSEBUTTONDOWN and e.button == 1 :
            # print(1)
            mous1 = mouse.get_pos()
            if peremena_geroy < 3:
                #--------------Damger class-------------------
                if geroy_red_Sir_Joseph.check_kasanie(mous1, e):
                
                    geroy_red_Sir_Joseph.image = image.load('geroy_avatar/green/Damger_Class/Sir_Joseph2.png')
                    geroy_red_Sir_Joseph.image = transform.scale(geroy_red_Sir_Joseph.image, (80,70))
                    peremena_geroy += 1 
                    print(peremena_geroy)
                    team.append(Damager_Class_Sir_Joseph)   
                    print(len(team))
                    print("hello")
                elif geroy_red_Chas.check_kasanie(mous1, e):
                    geroy_red_Chas.image = image.load('geroy_avatar/green/Damger_Class/Chas2.png')
                    geroy_red_Chas.image = transform.scale(geroy_red_Chas.image, (80,70))
                    peremena_geroy += 1 
                    team.append(Damager_Class_Chas)
                    print(len(team))
                elif geroy_red_Drowzet.check_kasanie(mous1, e):
                    geroy_red_Drowzet.image = image.load('geroy_avatar/green/Damger_Class/Drowzet2.png')
                    geroy_red_Drowzet.image = transform.scale(geroy_red_Drowzet.image, (80,70))
                    peremena_geroy += 1 
                    team.append(Damager_Class_Drowzet)
                    print(len(team))
                elif geroy_red_Ridael.check_kasanie(mous1, e):
                    geroy_red_Ridael.image = image.load('geroy_avatar/green/Damger_Class/Ridael2.png')
                    geroy_red_Ridael.image = transform.scale(geroy_red_Ridael.image, (80,70))
                    peremena_geroy += 1 
                    team.append(Damager_Class_Ridael)
                    print(len(team))
                elif geroy_red_Tiara.check_kasanie(mous1, e):
                    geroy_red_Tiara.image = image.load('geroy_avatar/green/Damger_Class/Tiara2.png')
                    geroy_red_Tiara.image = transform.scale(geroy_red_Tiara.image, (80,70))
                    peremena_geroy += 1 
                    team.append(Damager_Class_Tiara)
                    print(len(team))
                #---------------------------------Support class-----------------------

            
                elif geroy_red_Brina.check_kasanie(mous1, e):
                    geroy_red_Brina.image = image.load('geroy_avatar/green/Support_Class/Brina2.png')
                    geroy_red_Brina.image = transform.scale(geroy_red_Brina.image, (80,70))
                
                    peremena_geroy += 1 
                    team.append(Support_Class_Brina)

                elif geroy_red_Drogo.check_kasanie(mous1, e):
                    geroy_red_Drogo.image = image.load('geroy_avatar/green/Support_Class/Drogo2.png')
                    geroy_red_Drogo.image = transform.scale(geroy_red_Drogo.image, (80,70))
                    peremena_geroy += 1 
                    team.append(Support_Class_Drogo)
            
                elif geroy_red_Harumi.check_kasanie(mous1, e):
                    geroy_red_Harumi.image = image.load('geroy_avatar/green/Support_Class/Harumi2.png')
                    geroy_red_Harumi.image = transform.scale(geroy_red_Harumi.image, (80,70))
                    peremena_geroy += 1 
                    team.append(Support_Class_Harumi)
                
                elif geroy_red_Ja_Van.check_kasanie(mous1, e):
                    geroy_red_Ja_Van.image = image.load('geroy_avatar/green/Support_Class/JaVan2.png')
                    geroy_red_Ja_Van.image = transform.scale(geroy_red_Ja_Van.image, (80,70))
                    peremena_geroy += 1 
                    team.append(Support_Class_Ja_Van)
                
                elif geroy_red_Marylee.check_kasanie(mous1, e):
                    geroy_red_Marylee.image = image.load('geroy_avatar/green/Support_Class/Marylee2.png')
                    geroy_red_Marylee.image = transform.scale(geroy_red_Marylee.image, (80,70))
                    peremena_geroy += 1
                    team.append(Support_Class_Marylee)
                #--------Tank class---------------------------
                elif geroy_red_Airon.check_kasanie(mous1, e):
                    geroy_red_Airon.image = image.load('geroy_avatar/green/Tank_Class/Airon2.png')
                    geroy_red_Airon.image = transform.scale(geroy_red_Airon.image, (80,70))
                    peremena_geroy += 1     
                    team.append(Tank_Class_Airon)
                
                elif geroy_red_Condrat.check_kasanie(mous1, e):
                    geroy_red_Condrat.image = image.load('geroy_avatar/green/Tank_Class/Condrat2.png')
                    geroy_red_Condrat.image = transform.scale(geroy_red_Condrat.image, (80,70))
                    peremena_geroy += 1     
                    team.append(Tank_Class_Condrat)

                elif geroy_red_Gabriella.check_kasanie(mous1, e):
                    geroy_red_Gabriella.image = image.load('geroy_avatar/green/Tank_Class/Gabriella2.png')
                    geroy_red_Gabriella.image = transform.scale(geroy_red_Gabriella.image, (80,70))
                    peremena_geroy += 1     
                    team.append(Tank_Class_Gabriella)
                
                elif geroy_red_Ghorm.check_kasanie(mous1, e):
                    geroy_red_Ghorm.image = image.load('geroy_avatar/green/Tank_Class/Ghorm2.png')
                    geroy_red_Ghorm.image = transform.scale(geroy_red_Ghorm.image, (80,70))
                    peremena_geroy += 1  
                    team.append(Tank_Class_Ghorm)
                elif geroy_red_Ingrid.check_kasanie(mous1, e):
                    geroy_red_Ingrid.image = image.load('geroy_avatar/green/Tank_Class/Ingrid2.png')
                    geroy_red_Ingrid.image = transform.scale(geroy_red_Ingrid.image, (80,70))
                    peremena_geroy += 1
                    team.append(Tank_Class_Ingrid)
            



            
            
            if LVL.check_kasanie(mous1, e) and peremena_geroy == 3 :
               peremena = 'битва'

            if geroy.check_kasanie(mous1, e):
                peremena = 'герой'
                
            

            if karta.check_kasanie(mous1, e):
                peremena = "карта"


   

    if peremena == 'карта':
        window.blit(bg3,(0,0))
        pyti.draw_btn(window)
        back.draw_btn(window)
        geroy.draw_btn(window)
        house.draw_btn(window)
        LVL.draw_btn(window)
        karta.draw_btn(window)



    if peremena == "главний фон":
        window.blit(bg,(0,0))
        pyti.draw_btn(window)
        back.draw_btn(window)
        geroy.draw_btn(window)
        house.draw_btn(window)
        LVL.draw_btn(window)
        karta.draw_btn(window)
    
        

    if peremena == 'герой':
        window.fill((153,121,80))
        
        geroy_red_Sir_Joseph.draw_btn(window)
        geroy_red_Chas.draw_btn(window)
        geroy_red_Drowzet.draw_btn(window)
        geroy_red_Ridael.draw_btn(window)
        geroy_red_Tiara.draw_btn(window)

        geroy_red_Brina.draw_btn(window)
        geroy_red_Drogo.draw_btn(window)
        geroy_red_Harumi.draw_btn(window)
        geroy_red_Ja_Van.draw_btn(window)
        geroy_red_Marylee.draw_btn(window)
        geroy_red_Airon.draw_btn(window)
        geroy_red_Condrat.draw_btn(window)
        geroy_red_Gabriella.draw_btn(window)
        geroy_red_Ghorm.draw_btn(window)
        geroy_red_Ingrid.draw_btn(window)
        pyti.draw_btn(window)
        back.draw_btn(window)
        geroy.draw_btn(window)
        house.draw_btn(window)
        LVL.draw_btn(window)
        karta.draw_btn(window)
    if peremena =='битва':

        
        
        window.blit(bg2,(0,0))
        if boss.health > 0 :

            boss.draw(window)
            

        for i in team :
            if i.health > 0:

                i.draw(window)



        pyti.draw_btn(window)
        back.draw_btn(window)
        geroy.draw_btn(window)
        house.draw_btn(window)
        LVL.draw_btn(window)
        karta.draw_btn(window)

    display.update()
    clock.tick(FPS)