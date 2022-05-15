# Deadeye Class Skills
# skillname = ( 1.fullname, 2.description, 3.baseDmg, 4.idleTime, 5.moveTime, 6.skillLevel)

# fix zero indexing for display skill list, display skill rotation list -> need to fix logic too (indexing of delete and add)


sTracker = ["Spiral Tracker", "Throw a spinning handgun at target location.", 250, 0.65, 0, 1]
aGrenade = ["AT02 Grenade", "Throw a grenade at target location.", 150, 0.55, 0, 1]
eExecution = ["Enforce Execution","Dash forward delivering an upper kick, then rapid fire your gun keeping pushed foes airborne.", 250, 0, 2.4, 1]
pBullet = ["Plasma Bullet", "Fire a plasma bullet that travels at a low speed, continuously doing damage for 5 seconds", 110, 2.4, 0, 1]
sShot = ["Somersault Shot", "Somersault to move 10 meters forward while firing your handgun.", 156, 0, 1, 1]
mStream = ["Meteor Stream", "Fire a volley of bullets into air, then control where they land. Launches foes into the air.", 500, 0, 1.9, 1]
equilibrium = ["Equilibrium","Fire your handgun across a broad area", 500, 2, 0, 1]
dFire = ["Death Fire", "Fire a volley of bullets to attack nearby foes, then throw a grenade as you flip backwards.", 725, 2.75, 1, 1]
dShot = ["Dextrous Shot", "Move 6 meters as you glide and fire your handgun 4 times at nearby foes.", 90, 0, 1.85, 1]
qShot = ["Quick Shot", "Quickly fire your handgun two times.", 160, 1.2, 0, 1]
cTracker = ["Cruel Tracker", "Fire your handguns six times in a cone, followed by a final shot.", 660, 1.7, 0, 1]
sApocalypse = ["Sign of Apocalypse", "Fire your shotgun 2 times in rapid succession.", 700, 1.9, 0, 1]
hJudgement = ["Hour of Judgement", "Fire 3 bullets in a cone-shaped area.", 780, 1.5, 0, 1]
srFire = ["Shotgun Rapid Fire", "Fire shotgun 3 times, pushing foes back with the last shot.", 1160, 3, 0, 1]
lRequest = ["Last Request", "Fire a powerful explosive bullet that inflicts damage and launches foe into the air.", 840, 1.7, 0, 1]
sDominator = ["Shotgun Dominator", "Fire two shotguns at foes followed be a finishing shot.", 780, 3, 0, 1]
sFlame = ["Spiral Flame", "Fire a powerful flame bullet, launching foes in the air and setting the ground ablaze.", 860, 2.7, 0, 1]
catastrophe = ["Catastrophe", "Throw a claymore at target location then detonate it, launching foes into the air.", 720, 3, 0, 1]
tExplosion = ["Triple Explosion", "Fire an explosive bullet at target location, can cast up to three times.", 930, 4.5, 0]
aShot = ["Aimed Shot", "Fire 4 high caliber bullet while aiming around target location.", 700, 4.5, 0, 1]
pShot = ["Perfect Shot", "Fire high-speed large-caliber bullet, knocking back foes.", 1120, 1.75, 0, 1]
 

skillList = [sTracker,aGrenade,eExecution,pBullet,sShot,mStream,equilibrium,dFire,dShot,qShot,cTracker,sApocalypse,hJudgement,srFire,lRequest,sDominator,sFlame,catastrophe,tExplosion,aShot,pShot]

#rotation = []
#rotation.append(skillList[0])


#for item in skillList:
#    print(str(skillList.index(item))+ '. ' + item[0])

#for item in rotation:
#    print(str(skillList.index(item))+ '. ' + item[0])


