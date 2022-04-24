inf = float("inf")

#通过材料名称获取对应对象
name_obj_dic={} 

# python 使用类创建结构体formula
class Myclass(object):
    class Struct(object):
        def __init__(self, productionTool,productionSpeed,ifFoundation, material):
            #生产工具
            self.productionTool = productionTool
            #生产基础速度
            self.productionSpeed = productionSpeed
            #是否原材料
            self.ifFoundation = ifFoundation
            #是一个列表，里面的元素是列表（对象，比例）
            self.material = material

    def make_struct(self, productionTool,productionSpeed,ifFoundation, material):
        return self.Struct(productionTool,productionSpeed,ifFoundation, material)

class unit:
    def __init__(self,name):
        self.name=name
        self.formula=[]
    #设置公式  
    def setFormula(self,speed,ifF,tool,m):
        #生产工具
        productionTool=tool#0采矿效率，1冶炼效率，2制造效率，3其它
        #生产基础速度
        productionSpeed=speed
        #是否是原材料
        ifFoundation=ifF
        ls=[]
        for item in m:
            ls.append(item)
        myFormula = Myclass()
        temp = myFormula.make_struct(productionTool,productionSpeed,ifFoundation,ls)
        self.formula.append(temp)


# #--------矿物---------------------------
H=unit('H')
H.setFormula(inf,1,0,[])#采集器
name_obj_dic['H']=H

water=unit('water')
water.setFormula(50,1,0,[])
name_obj_dic['water']=water

ironOre=unit('ironOre')
ironOre.setFormula(30,1,0,[])
name_obj_dic['ironOre']=ironOre

copperOre=unit('copperOre')
copperOre.setFormula(30,1,0,[])
name_obj_dic['copperOre']=copperOre

stoneOre=unit('stoneOre')
stoneOre.setFormula(30,1,0,[])
name_obj_dic['stoneOre']=stoneOre

coalOre=unit('coalOre')
coalOre.setFormula(30,1,0,[])
name_obj_dic['coalOre']=coalOre

siliconOre=unit('siliconOre')
siliconOre.setFormula(30,1,0,[])
name_obj_dic['siliconOre']=siliconOre

titaniumOre=unit('titaniumOre')
titaniumOre.setFormula(30,1,0,[])
name_obj_dic['titaniumOre']=titaniumOre

crudeOil=unit('crudeOil')
crudeOil.setFormula(inf,1,0,[])
name_obj_dic['crudeOil']=crudeOil

plantFuel=unit('plantFuel')
plantFuel.setFormula(inf,1,3,[])
name_obj_dic['plantFuel']=plantFuel

wood=unit('wood')
wood.setFormula(inf,1,3,[])
name_obj_dic['wood']=wood

cIce=unit('cIce')
cIce.setFormula(30,1,0,[])#矿脉
cIce.setFormula(inf,1,0,[])#气体采集
name_obj_dic['cIce']=cIce

kimberley=unit('kimberley')
kimberley.setFormula(30,1,0,[])
name_obj_dic['kimberley']=kimberley

partingSi=unit('partingSi')
partingSi.setFormula(30,1,0,[])
name_obj_dic['partingSi']=partingSi
#有机晶体公式1
organicCrystal=unit('organicCrystal')
organicCrystal.setFormula(30,1,0,[])#有机晶体矿
name_obj_dic['organicCrystal']=organicCrystal
#硫酸公式1
vitriol=unit('vitriol')
vitriol.setFormula(50,1,0,[])
name_obj_dic['vitriol']=vitriol

organicCrystal=unit('organicCrystal')
organicCrystal.setFormula(30,1,0,[])#有机晶体矿
name_obj_dic['organicCrystal']=organicCrystal
#光栅石
raster=unit('raster')
raster.setFormula(30,1,0,[])
name_obj_dic['raster']=raster

stabShoot=unit('stabShoot')
stabShoot.setFormula(30,1,0,[])
name_obj_dic['stabShoot']=stabShoot

singlePole=unit('singlePole')
singlePole.setFormula(30,1,0,[])
name_obj_dic['singlePole']=singlePole
#临界光子
criticalPhoton=unit('criticalPhoton')
criticalPhoton.setFormula(inf,1,3,[])
name_obj_dic['criticalPhoton']=criticalPhoton

# #--------一级产物---------------------------

iron=unit('iron')
iron.setFormula(60,0,1,[[ironOre,1]])
name_obj_dic['iron']=iron

copper=unit('copper')
copper.setFormula(60,0,1,[[copperOre,1]])
name_obj_dic['copper']=copper

stone=unit('stone')
stone.setFormula(60,0,1,[[stoneOre,1]])
name_obj_dic['stone']=stone

silicon=unit('silicon')
silicon.setFormula(30,0,1,[[siliconOre,2]])
name_obj_dic['silicon']=silicon

titanium=unit('titanium')
titanium.setFormula(30,0,1,[[titaniumOre,2]])
name_obj_dic['titanium']=titanium

graphite=unit('graphite')
graphite.setFormula(30,0,1,[[coalOre,2]])
name_obj_dic['graphite']=graphite

refineOil=unit('refineOil')
refineOil.setFormula(30,0,3,[[crudeOil,1],[H,-0.5]])
name_obj_dic['refineOil']=refineOil
#考虑从精炼油里取氢,H公式2
H.setFormula(15,0,3,[[crudeOil,2],[refineOil,-2]])

#硫酸公式2
vitriol.setFormula(40,0,3,[[refineOil,1.5],[stoneOre,2],[water,1]])

magnet=unit('magnet')
magnet.setFormula(40,0,1,[[ironOre,1]])
name_obj_dic['magnet']=magnet

glass=unit('glass')
glass.setFormula(30,0,1,[[stoneOre,2]])
name_obj_dic['glass']=glass

prism=unit('prism')
prism.setFormula(60,0,2,[[glass,1.5]])
name_obj_dic['prism']=prism

gear=unit('gear')
gear.setFormula(60,0,2,[[iron,1]])
name_obj_dic['gear']=gear

steel=unit('steel')
steel.setFormula(20,0,1,[[iron,3]])
name_obj_dic['steel']=steel
#晶格硅
latticeSilicon=unit('latticeSilicon')
latticeSilicon.setFormula(30,0,1,[[silicon,1]])#硅公式
latticeSilicon.setFormula(80,0,2,[[partingSi,0.5]])#分型硅公式
name_obj_dic['latticeSilicon']=latticeSilicon
#石墨烯
graphene=unit('graphene')
graphene.setFormula(60,0,3,[[cIce,1],[H,-0.5]])#可燃冰公式
graphene.setFormula(40,0,3,[[graphite,1.5],[vitriol,0.5]])#石墨硫酸公式
name_obj_dic['graphene']=graphene
#碳纳米管
cnt=unit('cnt')
cnt.setFormula(30,0,3,[[graphene,1.5],[titanium,0.5]])#石墨烯钛公式
cnt.setFormula(30,0,3,[[stabShoot,1]])#刺笋公式
name_obj_dic['cnt']=cnt
#粒子带宽
ParticleW=unit('ParticleW')
# ParticleW.setFormula(7.5,0,2,[[cnt,2],[latticeSilicon,2],[plastics,1]])
name_obj_dic['ParticleW']=ParticleW

heavyH=unit('heavyH')
heavyH.setFormula(inf,1,0,[])#采集器
heavyH.setFormula(60,0,3,[[H,2]])#对撞机
name_obj_dic['heavyH']=heavyH

antimatter=unit('antimatter')
antimatter.setFormula(60,0,3,[[criticalPhoton,1],[H,-1]])
name_obj_dic['antimatter']=antimatter







#钛
titanium=unit('titanium')
titanium.setFormula(30,0,1,[[titaniumOre,2]])
name_obj_dic['titanium']=titanium

#石墨
graphite=unit('graphite')
graphite.setFormula(30,0,1,[[coalOre,2]])
name_obj_dic['graphite']=graphite
#精炼油
refineOil=unit('refineOil')
refineOil.setFormula(30,0,3,[[crudeOil,1],[H,-0.5]])
name_obj_dic['refineOil']=refineOil

# # #--------二级产物----------------------------
cicuitBoard=unit('cicuitBoard')
cicuitBoard.setFormula(120,0,2,[[iron,1],[copper,0.5]])
name_obj_dic['cicuitBoard']=cicuitBoard

MagneticCoil=unit('MagneticCoil')
MagneticCoil.setFormula(120,0,2,[[magnet,1],[copper,0.5]])
name_obj_dic['MagneticCoil']=MagneticCoil

electronic=unit('electronic')
electronic.setFormula(30,0,2,[[silicon,2],[copper,1]])
name_obj_dic['electronic']=electronic

#MK1
mk1=unit('mk1')
mk1.setFormula(120,0,2,[[coalOre,1]])
name_obj_dic['mk1']=mk1

#金刚石
diamond=unit('diamond')
diamond.setFormula(30,0,1,[[graphite,1]])#金刚石公式1石墨
diamond.setFormula(80,0,1,[[kimberley,0.5]])#金刚石公式2金伯利
name_obj_dic['diamond']=diamond

#MK2
mk2=unit('mk2')
mk2.setFormula(60,0,2,[[mk1,2],[diamond,1]])
name_obj_dic['mk2']=mk2

#MK3
mk3=unit('mk3')
mk3.setFormula(30,0,2,[[mk2,2],[cnt,1]])
name_obj_dic['mk3']=mk3

Tiglass=unit('Tiglass')
Tiglass.setFormula(24,0,2,[[glass,1],[titanium,1],[water,1]])
name_obj_dic['Tiglass']=Tiglass
#电浆
plasma=unit('plasma')
plasma.setFormula(30,0,2,[[MagneticCoil,4],[prism,2]])
name_obj_dic['plasma']=plasma
#光子合并器
photonCombiner=unit('photonCombiner')
photonCombiner.setFormula(20,0,2,[[prism,2],[cicuitBoard,1]])#光子合并器公式1棱镜
photonCombiner.setFormula(20,0,2,[[raster,1],[cicuitBoard,1]])#光子合并器公式1光栅石
name_obj_dic['photonCombiner']=photonCombiner

motor=unit('motor')
motor.setFormula(30,0,2,[[iron,2],[gear,1],[MagneticCoil,1]])
name_obj_dic['motor']=motor

greenMotor=unit('greenMotor')
greenMotor.setFormula(30,0,2,[[motor,2],[MagneticCoil,2]])
name_obj_dic['greenMotor']=greenMotor

blueMotor=unit('blueMotor')
blueMotor.setFormula(20,0,2,[[greenMotor,2],[magnet,3],[graphite,1]])
name_obj_dic['blueMotor']=blueMotor

plastics=unit('plastics')
plastics.setFormula(20,0,3,[[refineOil,2],[graphite,1]])
name_obj_dic['plastics']=plastics
#粒子带宽
ParticleW.setFormula(7.5,0,2,[[cnt,2],[latticeSilicon,2],[plastics,1]])

titaniumAlloy=unit('titaniumAlloy')
titaniumAlloy.setFormula(20,0,1,[[titanium,1],[steel,1],[vitriol,2]])
name_obj_dic['titaniumAlloy']=titaniumAlloy
#粒子容器
ParticleContainer=unit('ParticleContainer')
ParticleContainer.setFormula(15,0,2,[[greenMotor,2],[copper,2],[graphene,2]])#绿马达公式
ParticleContainer.setFormula(15,0,2,[[singlePole,10],[copper,2]])#单极磁石公式
name_obj_dic['ParticleContainer']=ParticleContainer
#钛晶石
Ticrystal=unit('Ticrystal')
Ticrystal.setFormula(15,0,2,[[organicCrystal,1],[titanium,3]])
name_obj_dic['Ticrystal']=Ticrystal
#氢燃料棒
HfuelRod=unit('HfuelRod')
HfuelRod.setFormula(20,0,2,[[titanium,0.5],[H,5]])
name_obj_dic['HfuelRod']=HfuelRod
#氘燃料棒
HHfuelRod=unit('HHfuelRod')
HHfuelRod.setFormula(10,0,2,[[titaniumAlloy,0.5],[heavyH,10],[blueMotor,0.5]])
name_obj_dic['HHfuelRod']=HHfuelRod
#反物质燃料棒
antifuelRod=unit('antifuelRod')
name_obj_dic['antifuelRod']=antifuelRod

#有机晶体公式2塑料合成
organicCrystal.setFormula(10,0,3,[[plastics,2],[refineOil,1],[water,1]])

# #--------高级产物----------------------------
#卡西米尔晶体
CasimirCrystal=unit('CasimirCrystal')
CasimirCrystal.setFormula(15,0,2,[[Ticrystal,1],[graphene,2],[H,12]])#钛晶石公式
CasimirCrystal.setFormula(15,0,2,[[raster,4],[graphene,2],[H,12]])#光栅石公式
name_obj_dic['CasimirCrystal']=CasimirCrystal
#位面过滤器
planesFilter=unit('planesFilter')
planesFilter.setFormula(5,0,2,[[CasimirCrystal,1],[Tiglass,2]])
name_obj_dic['planesFilter']=planesFilter
#奇异物质
singularity=unit('singularity')
singularity.setFormula(7.5,0,3,[[ParticleContainer,2],[iron,2],[heavyH,10]])
name_obj_dic['singularity']=singularity
#推进器
propeller=unit('propeller')
propeller.setFormula(15,0,2,[[steel,2],[copper,3]])
name_obj_dic['propeller']=propeller
#加力推进器
propellerPlus=unit('propellerPlus')
propellerPlus.setFormula(10,0,2,[[titaniumAlloy,5],[greenMotor,5]])
name_obj_dic['propellerPlus']=propellerPlus

cpu=unit('cpu')
cpu.setFormula(20,0,2,[[cicuitBoard,2],[electronic,2]])
name_obj_dic['cpu']=cpu

quantumCpu=unit('quantumCpu')
quantumCpu.setFormula(10,0,2,[[cpu,2],[planesFilter,2]])
name_obj_dic['quantumCpu']=quantumCpu

solarSail=unit('solarSail')
solarSail.setFormula(30,0,2,[[graphene,0.5],[photonCombiner,0.5]])
name_obj_dic['solarSail']=solarSail

frame=unit('frame')
frame.setFormula(10,0,2,[[cnt,4],[titaniumAlloy,1],[silicon,1]])
name_obj_dic['frame']=frame

dysonComponent=unit('dysonComponent')
dysonComponent.setFormula(7.5,0,2,[[frame,3],[solarSail,3],[cpu,3]])
name_obj_dic['dysonComponent']=dysonComponent

limiter=unit('limiter')
limiter.setFormula(3,0,2,[[ParticleContainer,1],[cpu,1]])
name_obj_dic['limiter']=limiter
#反物质燃料棒
antifuelRod.setFormula(5,0,2,[[antimatter,6],[H,6],[limiter,0.5],[titaniumAlloy,0.5]])

craft=unit('craft')
craft.setFormula(15,0,2,[[iron,5],[cpu,2],[propeller,2]])
name_obj_dic['craft']=craft

spacceCraft=unit('spacceCraft')
spacceCraft.setFormula(10,0,2,[[titaniumAlloy,10],[cpu,10],[propellerPlus,2]])
name_obj_dic['spacceCraft']=spacceCraft

rocket=unit('rocket')
rocket.setFormula(10,0,2,[[dysonComponent,2],[HHfuelRod,4],[quantumCpu,2]])
name_obj_dic['rocket']=rocket
#引力透镜
gravityMirror=unit('gravityMirror')
gravityMirror.setFormula(10,0,2,[[diamond,4],[singularity,1]])
name_obj_dic['gravityMirror']=gravityMirror
#空间翘曲器
spaceWarp=unit('spaceWarp')
spaceWarp.setFormula(6,0,2,[[gravityMirror,1]])#引力透镜公式
name_obj_dic['spaceWarp']=spaceWarp

blueCube=unit('blueCube')
blueCube.setFormula(20,0,3,[[cicuitBoard,1],[MagneticCoil,1]])
name_obj_dic['blueCube']=blueCube

redCube=unit('redCube')
redCube.setFormula(10,0,3,[[graphite,2],[H,2]])
name_obj_dic['redCube']=redCube

yellowCube=unit('yellowCube')
yellowCube.setFormula(7.5,0,3,[[diamond,1],[Ticrystal,1]])
name_obj_dic['yellowCube']=yellowCube

purpleCube=unit('purpleCube')
purpleCube.setFormula(6,0,3,[[cpu,2],[ParticleW,1]])
name_obj_dic['purpleCube']=purpleCube

greenCube=unit('greenCube')
greenCube.setFormula(5,0,3,[[gravityMirror,0.5],[quantumCpu,0.5]])
name_obj_dic['greenCube']=greenCube
#空间翘曲器公式2
spaceWarp.setFormula(48,0,2,[[greenCube,0.125]])#绿糖公式

whiteCube=unit('whiteCube')
whiteCube.setFormula(4,0,2,[[blueCube,1],[redCube,1],[yellowCube,1],[purpleCube,1],[greenCube,1],[antimatter,1]])
name_obj_dic['whiteCube']=whiteCube

foundation=unit('foundation')
foundation.setFormula(60,0,2,[[stone,3],[steel,1]])
name_obj_dic['foundation']=foundation

#-------------建筑物公式------------------
#-------------建筑物公式------------------
#-------------建筑物公式------------------
#-------------建筑物公式------------------
TeslaTower=unit('TeslaTower')
TeslaTower.setFormula(60,0,2,[[iron,2],[MagneticCoil,1]])
name_obj_dic['TeslaTower']=TeslaTower

ThermalPowerPlant=unit('ThermalPowerPlant')
ThermalPowerPlant.setFormula(12,0,2,[[iron,10],[stone,10],[gear,4],[MagneticCoil,4]])
name_obj_dic['ThermalPowerPlant']=ThermalPowerPlant

WirelessPowerTower=unit('WirelessPowerTower')
WirelessPowerTower.setFormula(20,0,2,[[TeslaTower,1],[plasma,3]])
name_obj_dic['WirelessPowerTower']=WirelessPowerTower

SatalliteSubstation=unit('SatalliteSubstation')
SatalliteSubstation.setFormula(12,0,2,[[WirelessPowerTower,1],[blueMotor,10],[frame,2]])
name_obj_dic['SatalliteSubstation']=SatalliteSubstation

WindTurbine=unit('WindTurbine')
WindTurbine.setFormula(15,0,2,[[iron,6],[gear,1],[MagneticCoil,3]])
name_obj_dic['WindTurbine']=WindTurbine

ThermalPower=unit('ThermalPower')
ThermalPower.setFormula(12,0,2,[[iron,10],[stone,4],[gear,4],[MagneticCoil,4]])
name_obj_dic['ThermalPower']=ThermalPower

SolarPanel=unit('SolarPanel')
SolarPanel.setFormula(10,0,2,[[copper,10],[silicon,10]])
name_obj_dic['SolarPanel']=SolarPanel

Accumulator=unit('Accumulator')
Accumulator.setFormula(12,0,2,[[iron,6],[blueMotor,1],[latticeSilicon,6]])
name_obj_dic['Accumulator']=Accumulator

AccumulatorFull=unit('AccumulatorFull')
AccumulatorFull.setFormula(inf,1,3,[])
name_obj_dic['AccumulatorFull']=AccumulatorFull

RayReceiver=unit('RayReceiver')
RayReceiver.setFormula(7.5,0,2,[[steel,20],[silicon,20],[photonCombiner,10],[cpu,5],[blueMotor,20]])
name_obj_dic['RayReceiver']=RayReceiver

MiniFusionPowerPlant=unit('MiniFusionPowerPlant')
MiniFusionPowerPlant.setFormula(6,0,2,[[titaniumAlloy,12],[blueMotor,10],[cnt,8],[cpu,4]])
name_obj_dic['MiniFusionPowerPlant']=MiniFusionPowerPlant

EnergyExchanger=unit('EnergyExchanger')
EnergyExchanger.setFormula(4,0,2,[[titaniumAlloy,4],[steel,40],[cpu,40],[ParticleContainer,8]])
name_obj_dic['EnergyExchanger']=EnergyExchanger

ArtificialStar=unit('ArtificialStar')
ArtificialStar.setFormula(2,0,2,[[titaniumAlloy,20],[frame,20],[limiter,10],[quantumCpu,10]])
name_obj_dic['ArtificialStar']=ArtificialStar

Conveyor1=unit('Conveyor1')
Conveyor1.setFormula(180,0,2,[[iron,2/3],[gear,1/3]])
name_obj_dic['Conveyor1']=Conveyor1

Conveyor2=unit('Conveyor2')
Conveyor2.setFormula(180,0,2,[[Conveyor1,1],[greenMotor,1/3]])
name_obj_dic['Conveyor2']=Conveyor2

Conveyor3=unit('Conveyor3')
Conveyor3.setFormula(180,0,2,[[Conveyor2,1],[blueMotor,1/3],[graphene,1/3]])
name_obj_dic['Conveyor3']=Conveyor3

Splitter=unit('Splitter')
Splitter.setFormula(30,0,2,[[iron,3],[gear,2],[cicuitBoard,1]])
name_obj_dic['Splitter']=Splitter

Storage1=unit('Storage1')
Storage1.setFormula(30,0,2,[[iron,4],[stone,4]])
name_obj_dic['Storage1']=Storage1

Storage2=unit('Storage2')
Storage2.setFormula(15,0,2,[[steel,8],[stone,8]])
name_obj_dic['Storage2']=Storage2

StorageTank=unit('StorageTank')
StorageTank.setFormula(30,0,2,[[iron,8],[stone,4],[glass,4]])
name_obj_dic['StorageTank']=StorageTank

EMRail=unit('EMRail')
EMRail.setFormula(10,0,2,[[steel,20],[gear,20],[cpu,5],[blueMotor,10]])
name_obj_dic['EMRail']=EMRail

PlanetaryLogistics=unit('PlanetaryLogistics')
PlanetaryLogistics.setFormula(3,0,2,[[steel,40],[titanium,40],[cpu,40],[ParticleContainer,20]])
name_obj_dic['PlanetaryLogistics']=PlanetaryLogistics

MiniatureParticleCollider=unit('MiniatureParticleCollider')
MiniatureParticleCollider.setFormula(4,0,2,[[titaniumAlloy,20],[frame,20],[blueMotor,50],[graphene,10],[cpu,5]])
name_obj_dic['MiniatureParticleCollider']=MiniatureParticleCollider

Sorter1=unit('Sorter1')
Sorter1.setFormula(60,0,2,[[iron,1],[cicuitBoard,1]])
name_obj_dic['Sorter1']=Sorter1

Sorter2=unit('Sorter2')
Sorter2.setFormula(60,0,2,[[Sorter1,1],[motor,0.5]])
name_obj_dic['Sorter2']=Sorter2

Sorter3=unit('Sorter3')
Sorter3.setFormula(60,0,2,[[Sorter2,1],[greenMotor,0.5]])
name_obj_dic['Sorter3']=Sorter3

MiningMachine=unit('MiningMachine')
MiningMachine.setFormula(20,0,2,[[iron,4],[cicuitBoard,2],[MagneticCoil,2],[gear,2]])
name_obj_dic['MiningMachine']=MiningMachine

WaterPump=unit('WaterPump')
WaterPump.setFormula(15,0,2,[[iron,8],[stone,4],[motor,4],[cicuitBoard,2]])
name_obj_dic['WaterPump']=WaterPump

OilExtrator=unit('OilExtrator')
OilExtrator.setFormula(7.5,0,2,[[steel,12],[stone,12],[cicuitBoard,6],[plasma,4]])
name_obj_dic['OilExtrator']=OilExtrator

OliRefinery=unit('OliRefinery')
OliRefinery.setFormula(10,0,2,[[steel,10],[stone,10],[cicuitBoard,6],[plasma,6]])
name_obj_dic['OliRefinery']=OliRefinery

launchingSilo=unit('launchingSilo')
launchingSilo.setFormula(2,0,2,[[titaniumAlloy,80],[frame,30],[gravityMirror,20],[quantumCpu,10]])
name_obj_dic['launchingSilo']=launchingSilo

InterStellarLogistics=unit('InterStellarLogistics')
InterStellarLogistics.setFormula(2,0,2,[[PlanetaryLogistics,1],[titaniumAlloy,40],[ParticleContainer,20]])
name_obj_dic['InterStellarLogistics']=InterStellarLogistics

Assembing1=unit('Assembing1')
Assembing1.setFormula(30,0,2,[[iron,4],[gear,8],[cicuitBoard,4]])
name_obj_dic['Assembing1']=Assembing1

Assembing2=unit('Assembing2')
Assembing2.setFormula(20,0,2,[[Assembing1,1],[graphene,8],[cpu,4]])
name_obj_dic['Assembing2']=Assembing2

Assembing3=unit('Assembing3')
Assembing3.setFormula(15,0,2,[[Assembing2,1],[ParticleW,8],[quantumCpu,2]])
name_obj_dic['Assembing3']=Assembing3

Smelter1=unit('Smelter1')
Smelter1.setFormula(20,0,2,[[iron,4],[stone,2],[cicuitBoard,4],[MagneticCoil,2]])
name_obj_dic['Smelter1']=Smelter1

Smelter2=unit('Smelter2')
Smelter2.setFormula(12,0,2,[[Smelter1,1],[frame,5],[planesFilter,10],[singlePole,15]])
name_obj_dic['Smelter2']=Smelter2

Fractionator=unit('Fractionator')
Fractionator.setFormula(20,0,2,[[steel,8],[stone,4],[glass,4],[cpu,1]])
name_obj_dic['Fractionator']=Fractionator
#喷涂器
coater=unit('coater')
coater.setFormula(20,0,2,[[steel,4],[plasma,2],[cicuitBoard,2],[electronic,2]])
name_obj_dic['coater']=coater

ChemicalPlant=unit('ChemicalPlant')
ChemicalPlant.setFormula(12,0,2,[[steel,8],[stone,8],[glass,8],[cicuitBoard,2]])
name_obj_dic['ChemicalPlant']=ChemicalPlant

Lab=unit('Lab')
Lab.setFormula(20,0,2,[[iron,8],[glass,4],[cicuitBoard,4],[MagneticCoil,4]])
name_obj_dic['Lab']=Lab

OrbitalCollector=unit('OrbitalCollector')
OrbitalCollector.setFormula(2,0,2,[[InterStellarLogistics,1],[blueMotor,50],[propellerPlus,20],[AccumulatorFull,20]])
name_obj_dic['OrbitalCollector']=OrbitalCollector