requireName=[]
requireNum=[]

#[采矿效率,冶炼效率,制造效率,其它]
speedList=[1.5,1,1,1]
#产品配方序号dictionary
fNumDic = {'ironOre' : 0 , 'copperOre' : 0 , 'stoneOre' : 0 , 'coalOre' : 0 , 'siliconOre' : 0 , 'titaniumOre' : 0 , 'water' : 0 , 'crudeOil' : 0 , 'H' : 0 , 'heavyH' : 0 , 'antimatter' : 0 , 'kimberley' : 0 , 'iron' : 0 , 'copper' : 0 , 'stone' : 0 , 'graphite' : 0 , 'silicon' : 0 , 'titanium' : 0 , 'vitriol' : 0 , 'refineOil' : 0 , 'HfuelRod' : 0 , 'HHfuelRod' : 0 , 'antifuelRod' : 0 , 'partingSi' : 0 , 'magnet' : 0 , 'MagneticCoil' : 0 , 'glass' : 0 , 'diamond' : 0 , 'latticeSilicon' : 0 , 'titaniumAlloy' : 0 , 'cIce' : 0 , 'plastics' : 0 , 'organicCrystal' : 0 , 'graphene' : 0 , 'propeller' : 0 , 'raster' : 0
, 'steel' : 0 , 'cicuitBoard' : 0 , 'prism' : 0 , 'motor' : 0 , 'electronic' : 0 , 'CasimirCrystal' : 0 , 'singularity' : 0 , 'Ticrystal' : 0 , 'cnt' : 0 , 'propellerPlus' : 0 , 'stabShoot' : 0 , 'gear' : 0
, 'plasma' : 0 , 'photonCombiner' : 0 , 'greenMotor' : 0 , 'cpu' : 0 , 'limiter' : 0 , 'Tiglass' : 0 , 'ParticleW' : 0 , 'craft' : 0 , 'singlePole' : 0 , 'foundation' : 0 , 'criticalPhoton' : 0 , 'ParticleContainer' : 0 , 'blueMotor' : 0 , 'gravityMirror' : 0 , 'spaceWarp' : 0 , 'planesFilter' : 0 , 'quantumCpu' : 0 , 'spacceCraft' : 0 , 'wood' : 0 , 'blueCube' : 0 , 'redCube' : 0 , 'yellowCube' : 0 , 'purpleCube' : 0 , 'greenCube' : 0 , 'whiteCube' : 0 , 'solarSail' : 0 , 'frame' : 0 , 'dysonComponent' : 0 , 'rocket' : 0 , 'TeslaTower' : 0 , 'plantFuelTeslaTower' : 0 , 'WirelessPowerTower' : 0 , 'SatalliteSubstation' : 0 , 'WindTurbine' : 0 , 'ThermalPowerPlant' : 0 , 'SolarPanel' : 0 , 'MiniFusionPowerPlant' : 0 , 'Accumulator' : 0 , 'AccumulatorFull' : 0 , 'EnergyExchanger' : 0 , 'RayReceiver' : 0 , 'ArtificialStar' : 0 , 'Conveyor1' : 0 , 'Conveyor2' : 0 , 'Conveyor3' : 0 , 'Splitter' : 0 , 'Storage1' : 0 , 'Storage2' : 0 , 'StorageTank' : 0 , 'PlanetaryLogistics' : 0 , 'InterStellarLogistics' : 0 , 'OrbitalCollector' : 0 , 'EMRail' : 0 , 'Sorter1' : 0 , 'Sorter2' : 0 , 'Sorter3' : 0 , 'MiningMachine' : 0 , 'WaterPump' : 0 , 'OilExtrator' : 0 , 'OliRefinery' : 0 , 'MiniatureParticleCollider' : 0 , 'Lab' : 0 , 'launchingSilo' : 0 , 'Assembing1' : 0 , 'Assembing2' : 0 , 'Assembing3' : 0 , 'Smelter1' : 0 , 'Smelter2' : 0 , 'ChemicalPlant' : 0 , 'Fractionator' : 0
, 'mk1' : 0 , 'mk2' : 0 , 'mk3' : 0 , 'coater' : 0 }
#修改默认值
fNumDic['organicCrystal']=1
fNumDic['diamond']=1
fNumDic['cnt']=1
fNumDic['CasimirCrystal']=1
fNumDic['spaceWarp']=1
fNumDic['ParticleContainer']=1
#可用配方
canUseFormula={}
canUseFormula['organicCrystal']=['有机晶体矿','塑料合成']#0表示有机晶体矿，1表示合成
canUseFormula['diamond']=['石墨','金伯利矿石']#0表示石墨，1表示金伯利
canUseFormula['latticeSilicon']=['硅公式','分型硅公式']#0表示硅公式，1表示分型硅公式
canUseFormula['graphene']=['可燃冰公式','石墨硫酸公式']#0表示可燃冰公式，1表示石墨硫酸公式
canUseFormula['cnt']=['石墨烯钛公式','刺笋公式']#0表示石墨烯钛公式，1表示刺笋公式
canUseFormula['heavyH']=['采集器','对撞机']#0表示采集器公式，1表示对撞机公式
canUseFormula['photonCombiner']=['棱镜公式','光栅石公式']#0表示棱镜公式，1表示光栅石公式
canUseFormula['ParticleContainer']=['绿马达公式','单极磁石公式']#0表示绿马达公式，1表示单极磁石公式
canUseFormula['CasimirCrystal']=['钛晶石公式','光栅石公式']#0表示钛晶石公式，1表示光栅石公式
canUseFormula['spaceWarp']=['引力透镜公式','绿糖公式']#0表示引力透镜公式，1表示绿糖公式
canUseFormula['vitriol']=['硫酸海洋采集','精炼油合成']#0表示硫酸海洋采集公式，1表示精炼油合成
canUseFormula['cIce']=['矿脉','轨道采集器']#0表示矿脉公式，1表示轨道采集器

def start():
    from material import name_obj_dic
    stuffs={}
    for i in range(len(requireName)):
        # #取得对应的生产效率
        ps=speedList[name_obj_dic[requireName[i]].formula[fNumDic[requireName[i]]].productionTool]
        if requireName[i] in stuffs:
            stuffs[requireName[i]][1]+=requireNum[i]
            stuffs[requireName[i]][2]+=requireNum[i]/(name_obj_dic[requireName[i]].formula[fNumDic[requireName[i]]].productionSpeed)/ps
        else:
            stuffs[requireName[i]]=[name_obj_dic[requireName[i]],requireNum[i],requireNum[i]/(name_obj_dic[requireName[i]].formula[fNumDic[requireName[i]]].productionSpeed)/ps]

    #stuffs中每个元素是一个列表，第0位是对象，第1位是数量，第2位是所需的生产设备数
    #item中的每个元素是一个列表，第0位是对象，第1位是比例
    #递归搜索
    def search_tree(Target,num):
        for item in Target.formula[fNumDic[Target.name]].material:#fNumDic[Target.name]用名称去字典里去序号
            # print(item[0].name)
            # print(fNumDic[item[0].name])
            # print(item[0].formula[fNumDic[item[0].name]])
            ps=speedList[item[0].formula[fNumDic[item[0].name]].productionTool]#取得对应的生产效率
            if item[0].name in stuffs:
                stuffs[item[0].name][1]+=item[1]*num
                stuffs[item[0].name][2]+=item[1]*num/item[0].formula[fNumDic[item[0].name]].productionSpeed/ps
            else:
                stuffs[item[0].name]=[item[0],item[1]*num,item[1]*num/item[0].formula[fNumDic[item[0].name]].productionSpeed/ps]

            # if item[1]<0:#判断终止
            if item[0].formula[fNumDic[item[0].name]].ifFoundation==1:#是原材料
                pass
            else:
                search_tree(item[0],item[1]*num)

    for i in range(len(requireName)):
        search_tree(name_obj_dic[requireName[i]],requireNum[i])

    return stuffs


