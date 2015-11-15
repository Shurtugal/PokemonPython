from pyglet import *
W=window.Window(910,512)
W.set_location(0,0)
T1=text.Label('Pokémon', font_name='Arial', font_size=50, x=W.width//2, y=W.height//4*3, anchor_x='center', anchor_y='center', color=(0,0,0,255))
player=media.Player()
for a in range(10):
	player.queue(media.load('Track1.mp3'))
player.play()
fond=sprite.Sprite(image.load('white.png'))
menu=True
etat,ll,pl,ytiret,xtiret=0,0,0,0,0
@W.event
def on_draw():
	W.clear()
	fond.draw()
	T1.draw()
@W.event
def on_key_press(symbol, modifiers):
	global menu,etat,ll,pl,xtiret,ytiret
	if menu==True and symbol==window.key.I:
		W.clear()
		fond.draw()
		text.Label(' Continuer\n Nouvelle partie', font_name='Arial', font_size=25, x=W.width//2, y=W.height//2, anchor_x='left', anchor_y='center', color=(0,0,0,255)).draw()
		etat=1
		ll=2
		pl=0
		ytiret=270
		xtiret=455
	if etat==1:
		if pl<ll-1 and symbol==window.key.Z:
			T=text.Label('-', font_name='Arial', font_size=25, x=xtiret, y=ytiret+pl*30, anchor_x='left', anchor_y='center', color=(255,255,255,255))
			T.draw()
			pl+=1
			T=text.Label('-', font_name='Arial', font_size=25, x=xtiret, y=ytiret+pl*30, anchor_x='left', anchor_y='center', color=(0,0,0,255))
			T.draw()
		elif pl>0 and symbol==window.key.S:
			text.Label('-', font_name='Arial', font_size=25, x=xtiret, y=ytiret+pl*30, anchor_x='left', anchor_y='center', color=(255,255,255,255)).draw()
			pl-=1
			text.Label('-', font_name='Arial', font_size=25, x=xtiret, y=ytiret+pl*30, anchor_x='left', anchor_y='center', color=(0,0,0,255)).draw()
		if symbol==window.key.P:
			etat=-1
	if menu==True and etat==-1:
		W.clear()
	print(menu,etat,ll,pl,xtiret,ytiret)
app.run()
