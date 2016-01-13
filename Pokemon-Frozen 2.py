# -*- coding: UTF-8 -*-
import pygame, sys, random
from pokemonFx import *
pygame.init()
end=0
types=['','Combat','Dragon','Eau','Electrik','Feu','Glace','Insecte','Normal','Plante','Poison','Psy','Roche','Sol','Spectre','Vol','Acier']
save=eval(open('save.sav','r').readline())
size=width,height=910,512
black=0,0,0
white=255,255,255
blue=0,25,136
green=86,163,89
fighttext=[('Un ','sid',' sauvage apparait !'),('','mid',' ! Go !'),['Attaque','Sac','Pokemon','Fuite']]
typemodtext=['in','tres peu ','pas tres ','super ','extremement ']
framecount=0
fighttextcount=-1

screen=pygame.display.set_mode(size)
pygame.display.set_caption("Pokemon Frozen")

sid=109
mid=save[3]
Wmaxpv=pokemon(sid)[3][3]*5/50+5+10
Wpv=Wmaxpv
Smaxpv=pokemon(mid)[3][3]*save[0]/50+save[0]+10
Spv=save[2]
wildim=pygame.image.load("Sprites Pokemons/N°"+str(sid)+"-"+pokemon(sid)[0]+".png").convert_alpha()
selfim=pygame.transform.flip(pygame.image.load("Sprites Pokemons/N°"+str(mid)+"-"+pokemon(mid)[0]+".png").convert_alpha(),True,False)

while not end:
	for event in pygame.event.get():
		if event.type==pygame.QUIT:
			end=1
	framecount+=1
	if fighttextcount==-1 and framecount>60:
		fighttextcount=0
		framecount=0
		textW1=pygame.font.SysFont('Arial', 20, False, False).render(pokemon(sid)[0], True, black)
		textW2=pygame.font.SysFont('Arial', 20, False, False).render('n. 5', True, black)
		textW3=pygame.font.SysFont('Arial', 20, False, False).render('PV', True, black)
		textS1=pygame.font.SysFont('Arial', 20, False, False).render(pokemon(mid)[0], True, black)
		textS2=pygame.font.SysFont('Arial', 20, False, False).render('n. '+str(save[0]), True, black)
		textS3=pygame.font.SysFont('Arial', 20, False, False).render('PV', True, black)
		textS4=pygame.font.SysFont('Arial', 20, False, False).render(str(int(Spv))+'/'+str(int(Smaxpv)), True, black)
		textS5=pygame.font.SysFont('Arial', 12, False, False).render('exp', True, black)
	if fighttextcount in [0,1]:
		text1=pygame.font.SysFont('Arial', 35, False, False).render(fighttext[fighttextcount][0]+pokemon(eval(fighttext[fighttextcount][1]))[0]+fighttext[fighttextcount][2], True, black)
	if framecount>20 and fighttextcount==0 and pygame.key.get_pressed()[111]==1:
		fighttextcount+=1
		framecount=0
	if framecount>70 and fighttextcount==1:
		fighttextcount+=1
		submenu=0
		framecount=0
		J=0,0
		LA=0,0
	if fighttextcount==2:
		if submenu==0:
			text1=pygame.font.SysFont('Arial', 35, False, False).render('Que doit faire ', True, black)
			text1b=pygame.font.SysFont('Arial', 35, False, False).render(pokemon(mid)[0]+' ?', True, black)
			text2=pygame.font.SysFont('Arial', 35, False, False).render(fighttext[2][0], True, black)
			text3=pygame.font.SysFont('Arial', 35, False, False).render(fighttext[2][1], True, black)
			text4=pygame.font.SysFont('Arial', 35, False, False).render(fighttext[2][2], True, black)
			text5=pygame.font.SysFont('Arial', 35, False, False).render(fighttext[2][3], True, black)
			if framecount>20 and pygame.key.get_pressed()[111]==1:
				submenu=J[0]+J[1]*2+1
				framecount=0
				J=0,0
				if submenu==1:
					J=LA
			if pygame.key.get_pressed()[100]==1 and J[0]==0:
				J=1,J[1]
			if pygame.key.get_pressed()[113]==1 and J[0]==1:
				J=0,J[1]
			if pygame.key.get_pressed()[115]==1 and J[1]==0:
				J=J[0],1
			if pygame.key.get_pressed()[122]==1 and J[1]==1:
				J=J[0],0
		if submenu==1:
			text2=pygame.font.SysFont('Arial', 35, False, False).render(attaque(save[5])[4], True, black)
			text3=pygame.font.SysFont('Arial', 35, False, False).render(attaque(save[6])[4], True, black)
			text4=pygame.font.SysFont('Arial', 35, False, False).render(attaque(save[7])[4], True, black)
			text5=pygame.font.SysFont('Arial', 35, False, False).render(attaque(save[8])[4], True, black)
			text6=pygame.font.SysFont('Arial', 35, False, False).render('PP '+str(save[J[0]+2*J[1]+9])+'/'+str(attaque(save[J[0]+2*J[1]+5])[5]), True, black)
			text7=pygame.font.SysFont('Arial', 35, False, False).render(types[attaque(save[J[0]+2*J[1]+5])[0]], True, black)
			if framecount>20 and pygame.key.get_pressed()[111]==1:
				if save[J[0]+2*J[1]+9]>0:
					fighttextcount+=1
					framecount=0
					alea=random.uniform(0.85,1)
					if random.randint(1,16)==1:
						critical=1
					else:
						critical=0
					typemod=table(attaque(save[J[0]+2*J[1]+5])[0],pokemon(sid)[1])*table(attaque(save[J[0]+2*J[1]+5])[0],pokemon(sid)[2])
					stab=1+(attaque(save[J[0]+2*J[1]+5])[0]==pokemon(mid)[1] or attaque(save[J[0]+2*J[1]+5])[0]==pokemon(mid)[2])*0.5
					save[J[0]+2*J[1]+9]-=1
					LA=J
				else:
					framecount=0
					submenu=1.5
			if pygame.key.get_pressed()[100]==1 and J[0]==0 and save[6+2*J[1]]!=0:
				J=1,J[1]
			if pygame.key.get_pressed()[113]==1 and J[0]==1 and save[5+2*J[1]]!=0:
				J=0,J[1]
			if pygame.key.get_pressed()[115]==1 and J[1]==0 and save[7+J[0]]!=0:
				J=J[0],1
			if pygame.key.get_pressed()[122]==1 and J[1]==1 and save[5+J[0]]!=0:
				J=J[0],0
		if submenu==1.5:
			text1=pygame.font.SysFont('Arial', 35, False, False).render('Cette attaque n\'a plus de PP !', True, black)
			if framecount>60:
				submenu=1
		if submenu>=2:
			text1=pygame.font.SysFont('Arial', 35, False, False).render('Fonctionalite non disponible.', True, black)
			if framecount>60:
				submenu=0
	if fighttextcount==3:
		text1=pygame.font.SysFont('Arial', 35, False, False).render(pokemon(mid)[0]+' utilise '+attaque(save[J[0]+J[1]*2+5])[4]+' !', True, black)
		if framecount in range(60,111) and attaque(save[J[0]+J[1]*2+5])[1]>0:
			Wpv+=-((save[0]*0.4+2)*(pokemon(mid)[3][0]*save[0]/50+5)*attaque(save[J[0]+J[1]*2+5])[1]/(pokemon(sid)[3][2]*5/50+5)/50+2)*(critical+1)*typemod*stab*alea/50
			if Wpv<=0:
				Wpv=0
				fighttextcount=4
				framecount=0
				if critical or typemod!=1:
					fighttextcount=3.1
					framecount=0
		if framecount==140:
			text1=pygame.font.SysFont('Arial', 35, False, False).render('Que doit faire ', True, black)
			text2=pygame.font.SysFont('Arial', 35, False, False).render(fighttext[2][0], True, black)
			text3=pygame.font.SysFont('Arial', 35, False, False).render(fighttext[2][1], True, black)
			text4=pygame.font.SysFont('Arial', 35, False, False).render(fighttext[2][2], True, black)
			text5=pygame.font.SysFont('Arial', 35, False, False).render(fighttext[2][3], True, black)
			fighttextcount=2
			submenu=0
			J=0,0
			if critical or typemod!=1:
				fighttextcount=3.1
				framecount=0
	if fighttextcount==3.1:
		if critical:
			text1=pygame.font.SysFont('Arial', 35, False, False).render('Coup critique !', True, black)
		else:
			text1=pygame.font.SysFont('Arial', 35, False, False).render('C\'est '+typemodtext[[0,0.25,0.5,2,4].index(typemod)]+'efficace !', True, black)
		if framecount>80:
			if critical and typemod!=1:
				fighttextcount=3.2
				framecount=0
			else:
				if Wpv<=0:
					fighttextcount=4
				else:
					fighttextcount=2
	if fighttextcount==3.2:
		text1=pygame.font.SysFont('Arial', 35, False, False).render('C\'est '+typemodtext[[0,0.25,0.5,2,4].index(typemod)]+'efficace !', True, black)
		if framecount>80:
			if Wpv<=0:
				fighttextcount=4
			else:
				fighttextcount=2
	if fighttextcount==4:
		text1=pygame.font.SysFont('Arial', 35, False, False).render(pokemon(sid)[0]+' sauvage est K.O.!', True, black)
		if framecount>20 and pygame.key.get_pressed()[111]==1:
			end=1


	screen.fill(white)
	if not (fighttextcount==3 and framecount in range(11,21)+range(31,41)):
		screen.blit(wildim, [(fighttextcount==-1)*framecount*15-256+(fighttextcount>=0)*913,60])
	if fighttextcount>=0:
		pygame.draw.rect(screen,blue,[115,385,682,126],4)
		pygame.draw.rect(screen,green,[669,0,239,55],4)
		if Wpv>0:
			pygame.draw.line(screen,green,(778,41),(778+120*Wpv/Wmaxpv,41),4)
		screen.blit(textW1, [684, 6])
		screen.blit(textW2, [844, 6])
		screen.blit(textW3, [746, 31])
	if fighttextcount>1:
		pygame.draw.rect(screen,green,[0,0,241,91],4)
		if Spv>0:
			pygame.draw.line(screen,green,(112,41),(112+120*Spv/Smaxpv,41),4)
		screen.blit(selfim, [0,120])
		screen.blit(textS1, [18, 6])
		screen.blit(textS2, [178, 6])
		screen.blit(textS3, [80, 31])
		screen.blit(textS4, [162, 51])
		screen.blit(textS5, [65, 72])
	if fighttextcount in [0,1,3,3.1,3.2,4]:
		screen.blit(text1, [140, 400])
	if fighttextcount==2:
		if submenu==0:
			pygame.draw.rect(screen,black,[511+J[0]*171,412+J[1]*50,15,15])
			pygame.draw.line(screen,blue,(490,385),(490,511),4)
			screen.blit(text1, [140, 400])
			screen.blit(text1b, [140, 450])
			screen.blit(text2, [530, 400])
			screen.blit(text3, [700, 400])
			screen.blit(text4, [530, 450])
			screen.blit(text5, [700, 450])
		if submenu==1:
			pygame.draw.rect(screen,black,[121+J[0]*260,412+J[1]*50,15,15])
			pygame.draw.line(screen,blue,(640,385),(640,511),4)
			screen.blit(text2, [140, 400])
			screen.blit(text3, [400, 400])
			screen.blit(text4, [140, 450])
			screen.blit(text5, [400, 450])
			screen.blit(text6, [650, 400])
			screen.blit(text7, [650, 450])
		if submenu>1:
			screen.blit(text1, [140, 400])
	pygame.display.flip()
	pygame.time.Clock().tick(60)
open('save.sav','w').write(repr(save))
sys.exit()
