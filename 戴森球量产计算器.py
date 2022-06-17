import os
import tkinter as tk
from tkinter import ttk
from tkinter import font
from tkinter.constants import (HORIZONTAL, RIDGE, TOP, VERTICAL, RIGHT, LEFT, X, Y, BOTH, BOTTOM, YES, END)
import ret

# 原材料图片路径
path = './image-ycl/'

# 决定展示顺序
material_level_0 = ['criticalPhoton', 'wood', 'plantFuel', 'crudeOil', 'water', 'H']
material_level_1 = ['antimatter', 'heavyH', 'ParticleW', 'cnt', 'graphene', 'latticeSilicon', 'steel', 'gear', 'prism',
                    'glass', 'magnet', 'vitriol', 'refineOil', 'graphite', 'titanium', 'silicon', 'stone', 'copper',
                    'iron']
material_level_2 = ['HHfuelRod', 'HfuelRod', 'Ticrystal', 'ParticleContainer', 'titaniumAlloy', 'plastics', 'blueMotor',
                    'greenMotor', 'motor', 'photonCombiner', 'plasma', 'Tiglass', 'diamond', 'electronic',
                    'MagneticCoil', 'cicuitBoard']
material_level_3 = ['foundation', 'whiteCube', 'greenCube', 'purpleCube', 'yellowCube', 'redCube', 'blueCube',
                    'spaceWarp', 'gravityMirror', 'rocket', 'spacceCraft', 'craft', 'antifuelRod', 'limiter',
                    'dysonComponent', 'frame', 'solarSail', 'quantumCpu', 'cpu', 'propellerPlus', 'propeller',
                    'singularity', 'planesFilter', 'CasimirCrystal','mk1','mk2','mk3']
# 可能显示矿脉
kuangmai = ['organicCrystal', 'ironOre', 'copperOre', 'stoneOre', 'coalOre', 'siliconOre', 'titaniumOre', 'cIce',
            'kimberley', 'partingSi', 'raster', 'stabShoot', 'singlePole']
# 建筑物
material_level_4 = ['Fractionator', 'ChemicalPlant', 'coater', 'Smelter2', 'Smelter1', 'Assembing3', 'Assembing2', 'Assembing1',
                    'launchingSilo', 'Lab', 'MiniatureParticleCollider', 'OliRefinery', 'OilExtrator', 'WaterPump',
                    'MiningMachine', 'Sorter3', 'Sorter2', 'Sorter1', 'EMRail', 'OrbitalCollector',
                    'InterStellarLogistics', 'PlanetaryLogistics', 'StorageTank', 'Storage2', 'Storage1', 'Splitter','piler',
                    'Conveyor3', 'Conveyor2', 'Conveyor1', 'ArtificialStar', 'RayReceiver', 'EnergyExchanger','geothermal',
                    'AccumulatorFull', 'Accumulator', 'MiniFusionPowerPlant', 'SolarPanel', 'ThermalPowerPlant',
                    'WindTurbine', 'SatalliteSubstation', 'WirelessPowerTower', 'TeslaTower']
material_all = material_level_4 + material_level_3 + material_level_2 + material_level_1 + material_level_0 + kuangmai

window = tk.Tk()
window.title('戴森球量产计算器 By雾霾天')
window.geometry('900x600')
frameInput1 = tk.Frame(window, height=40, width=125)
frameInput1.pack(pady=5)
frameInput1.config(bg='#f0f0f0')

frameInput2 = tk.Frame(window, height=40, width=125)
frameInput2.pack(pady=5)
frameInput2.config(bg='#f0f0f0')

frameInput3 = tk.Frame(window, height=40, width=125)
frameInput3.pack(pady=5)
frameInput3.config(bg='#f0f0f0')

frameInput4 = tk.Frame(window, height=40, width=125)
frameInput4.pack(pady=5)
frameInput4.config(bg='#f0f0f0')

frameOutput = tk.Frame(window, height=900 * 0.75 * 0.2, width=600 * 0.75)
frameOutput.pack(pady=5)
frameOutput.config(bg='#f0f0f0')

###参数输入
##生产参数
# 采矿效率
labelK = tk.Label(frameInput1, text='采矿效率：', bg='#f0f0f0', font=('宋体', 14))
labelK.pack(side=LEFT, pady=10)
addrK = tk.StringVar(value=str(ret.speedList[0]))
paramK = tk.Entry(frameInput1, textvariable=addrK, show=None, font=('宋体', 14), width=15)  # 显示成明文形式
paramK.pack(side=LEFT, padx=10, pady=10)

# 制作台参数
labelZ = tk.Label(frameInput1, text='制作台效率：', bg='#f0f0f0', font=('宋体', 14))
labelZ.pack(side=LEFT, pady=10)
xVariable1 = tk.StringVar()  # #创建变量，便于取值
com1 = ttk.Combobox(frameInput1, textvariable=xVariable1)  # #创建下拉菜单
com1.pack(side=LEFT, padx=10, pady=10)
com1["value"] = (0.75, 1, 1.5)  # #给下拉菜单设定值
com1.current(1)  # #设定下拉菜单的默认值


def xFunc1(event):
    ret.speedList[2] = float(com1.get())


com1.bind("<<ComboboxSelected>>", xFunc1)  # #给下拉菜单绑定事件

# 熔炉参数
labelR = tk.Label(frameInput1, text='熔炉效率：', bg='#f0f0f0', font=('宋体', 14))
labelR.pack(side=LEFT, pady=10)
xVariable2 = tk.StringVar()
com2 = ttk.Combobox(frameInput1, textvariable=xVariable2)
com2.pack(side=LEFT, pady=10)
com2["value"] = (1, 2)
com2.current(0)


def xFunc2(event):
    ret.speedList[1] = float(com2.get())


com2.bind("<<ComboboxSelected>>", xFunc2)

##需求参数
# 需求物品
# 需求选择窗口
# tk.Canvas列表
canva_files = []
image_files = {}

strExc = 'ironOre	copperOre	stoneOre	coalOre	siliconOre	titaniumOre	water	crudeOil	H	heavyH	antimatter	kimberley	iron	copper	stone	graphite	silicon	titanium	vitriol	refineOil	HfuelRod	HHfuelRod	antifuelRod	partingSi	magnet	MagneticCoil	glass	diamond	latticeSilicon	titaniumAlloy	cIce	plastics	organicCrystal	graphene	propeller	raster	steel	cicuitBoard	prism	motor	electronic	mk1	CasimirCrystal	singularity	Ticrystal	cnt	propellerPlus	stabShoot	gear	plasma	photonCombiner	greenMotor	cpu	mk2	kong	limiter	Tiglass	ParticleW	craft	singlePole	foundation	criticalPhoton	ParticleContainer	blueMotor	gravityMirror	mk3	kong	spaceWarp	planesFilter	quantumCpu	spacceCraft	kong	blueCube	redCube	yellowCube	purpleCube	greenCube	whiteCube	kong	solarSail	frame	dysonComponent	rocket	kong	'
str1 = 'kong	kong	kong	kong	kong	kong	kong	kong	kong	kong	kong	kong	'
str2 = 'TeslaTower	WirelessPowerTower	SatalliteSubstation	WindTurbine	ThermalPowerPlant	SolarPanel	MiniFusionPowerPlant	Accumulator	geothermal	EnergyExchanger	RayReceiver	ArtificialStar	Conveyor1	Conveyor2	Conveyor3	Splitter	piler	Storage1	Storage2	StorageTank	PlanetaryLogistics	InterStellarLogistics	OrbitalCollector	EMRail	Sorter1	Sorter2	Sorter3	MiningMachine	WaterPump	OilExtrator	OliRefinery	MiniatureParticleCollider	Lab	launchingSilo	kong	kong	Assembing1	Assembing2	Assembing3	Smelter1	Smelter2	coater	ChemicalPlant	Fractionator	kong	kong	kong	kong'
strExc = strExc + str1 + str2
ls_shunxu = strExc.split('\t')
for name in ls_shunxu:
    image_files[name] = tk.PhotoImage(file=path + name + '.png')


def chooseRequire():
    # 定义长在窗口上的窗口
    window_small = tk.Toplevel(window)
    window_small.geometry('600x606')
    window_small.title('需求选择')

    def callback(event):
        index = canva_files.index(event.widget)
        goods = ls_shunxu[index]
        if goods == 'kong':
            pass
        else:
            event.widget['bg'] = 'yellow'
            # 需求物品
            ret.requireName.append(str(goods))
            # 需求数量
            ret.requireNum.append(float(param2.get()))

            showbox.set_content()
            start_caculate()

            window_small.destroy()

    jishu = 0
    canva_files = []
    for item in ls_shunxu:
        canva = tk.Canvas(window_small, height=46, width=46)
        canva.bind("<Button-1>", callback)  # 绑定回调函数
        canva_files.append(canva)
        image = canva.create_image(0, 0, image=image_files[item], tag='photo', anchor='nw')
        canva.grid(row=int(jishu / 12), column=jishu % 12, padx=0, pady=0, ipadx=0, ipady=0)  # 摆放
        jishu += 1


btn_label1 = tk.Button(frameInput2, text='需求', command=chooseRequire, font=('宋体', 14))
btn_label1.grid(row=1, column=0, padx=50, pady=10, ipadx=20, sticky=tk.E)
# 需求数量
label2 = tk.Label(frameInput2, text='数量  ', bg='#f0f0f0', font=('宋体', 14))
label2.grid(row=1, column=3, pady=10, sticky=tk.E)
addr2 = tk.StringVar(value='60')
param2 = tk.Entry(frameInput2, textvariable=addr2, show=None, font=('宋体', 14))  # 显示成明文形式
param2.grid(row=1, column=4)


# 显示已经输入的需求
class showbox:
    def __init__(self, master):
        self.master = master
        self.str = tk.StringVar()
        self.initWidgets()

    def initWidgets(self):
        self.label4 = tk.Label(self.master, text='需求： ', bg='#c3c3c3', font=('宋体', 14), height=1, width=80,
                               anchor="nw", relief=RIDGE, borderwidth=3, )
        self.label4.pack()

    def set_content(self):
        zipped = zip(ret.requireName, ret.requireNum)
        strrsc = ''
        for item in zipped:
            strrsc += str(item) + ' '
        self.label4['text'] = '需求： ' + strrsc


showbox = showbox(frameInput3)

# scrollbar展示
scrollbar_v = tk.Scrollbar(frameOutput)
scrollbar_v.pack(side=RIGHT, fill=Y)
text = tk.Text(frameOutput, width=250, height=40, font=('宋体', 14), spacing1=20, bd=2)
text.config(yscrollcommand=scrollbar_v.set)  # text绑定垂直滚动条
scrollbar_v.config(command=text.yview)  # 垂直滚动条绑定text
text.pack(expand=YES, fill=BOTH)

photo = {}  # 字典{物品名称：物品图片对象}
chooseButtonall = ['']  # button列表
namelis = []  # 物品名称列表，与button列表一一对应


# 选择公式
def chooseFormula(event):
    labelLis = []

    # 获得可选的公式
    indexf = chooseButtonall.index(event.widget)
    goodsf = namelis[indexf]  # 点击按钮对应的物品名称
    # 显示可选的公式
    try:
        canUsedF = ret.canUseFormula[goodsf]
    except KeyError:
        return  # 只有一种公式

    # 选择可选的公式
    def setformual(event):
        formulaIndex = labelLis.index(event.widget)  # 选中的公式代码
        ret.fNumDic[goodsf] = formulaIndex  # 设置公式
        # 刷新列表
        # 删除上次的展示
        text.delete('1.0', 'end')
        # 再显示
        start_caculate()
        window_cf.destroy()

    # 定义长在窗口上的窗口
    window_cf = tk.Toplevel(window)
    window_cf.geometry('300x120')
    window_cf.title('choose your formula')

    scrollbar_cf = tk.Scrollbar(window_cf)
    scrollbar_cf.pack(side=RIGHT, fill=Y)
    text_cf = tk.Text(window_cf, width=250, height=40, font=('宋体', 14), spacing1=20, bd=2)

    text_cf.config(yscrollcommand=scrollbar_cf.set)  # text绑定垂直滚动条
    scrollbar_cf.config(command=text_cf.yview)  # 垂直滚动条绑定text

    for i in range(len(canUsedF)):
        label_cf = tk.Label(window_cf, text=str(canUsedF[i]), bg='#f0f0f0', font=('宋体', 14))
        label_cf.bind("<Button-1>", setformual)
        labelLis.append(label_cf)
        i += 1
        text_cf.window_create(f'{i}.1', window=label_cf)
        text_cf.insert(END, '\n')

    text_cf.pack()

    # #选择按钮
    # b1 = tk.Button(text, text=f"选择公式")
    # b1.bind("<Button-1>",chooseFormula)#鼠标左键绑定事件
    # chooseButton.append(b1)
    # namelis.append(str(s))
    # text.window_create(f'{si}.4', window=b1)

    # btn_comfirm_sign_up = tk.Button(window_cf, text='choose', command=confirm)
    # btn_comfirm_sign_up.place(x=120, y=120)


def start_caculate():
    # 初始化button列表
    chooseButton = []
    global namelis
    namelis = []
    # 删除上次的展示
    text.delete('1.0', 'end')

    ret.speedList[0] = float(paramK.get())

    stuffs = ret.start()

    # 显示
    si = 1  # caculate
    for s in material_all:
        if s in stuffs:
            #如果产量为0，跳过显示
            if stuffs[s][1] == 0:
                continue

            text.insert(f'{si}.1', '\t')
            photo[s] = tk.PhotoImage(file=os.path.join(path, s) + '.png')
            text.image_create(f'{si}.2', image=photo[s])  # 位置，行号从1开始，列号从0开始
            text.insert(f'{si}.3', ' ')
            # 选择按钮
            b1 = tk.Button(text, text=f"选择公式")
            b1.bind("<Button-1>", chooseFormula)  # 鼠标左键绑定事件
            chooseButton.append(b1)
            namelis.append(str(s))
            text.window_create(f'{si}.4', window=b1)
            # 判断是否是矿脉
            chandi = '机器数：'
            if s in kuangmai:
                if s == 'cIce' or s == 'organicCrystal':
                    if ret.fNumDic[s] == 0:
                        chandi = '矿脉数：'
                    else:
                        chandi = '机器数：'
                else:
                    chandi = '矿脉数：'

            if stuffs[s][0].formula[ret.fNumDic[s]].ifFoundation == 1:
                text.insert(f'{si}.5', f'\t产物：{str(s)} 产量：{round(stuffs[s][1], 1)} {chandi}{round(stuffs[s][2], 1)}')
            else:
                # 求最大承载
                radioLis = [abs(num[1]) for num in stuffs[s][0].formula[ret.fNumDic[s]].material]
                radioLis.append(1)
                mNum = 1800 / (stuffs[s][0].formula[ret.fNumDic[s]].productionSpeed * max(radioLis) * ret.speedList[
                    stuffs[s][0].formula[ret.fNumDic[s]].productionTool])
                text.insert(f'{si}.5',
                            f'\t产物：{str(s)} 产量：{round(stuffs[s][1], 1)} {chandi}{round(stuffs[s][2], 1)}(max:{round(mNum, 1)})')
            try:
                ret.canUseFormula[s]
            except KeyError:
                pass
            else:
                text.insert(END, f'\t\t{ret.canUseFormula[s][ret.fNumDic[s]]}')

            text.insert(END, '\n')
            si += 1

    global chooseButtonall
    chooseButtonall = chooseButton


def clearShow():
    # 清空配方
    ret.requireName = []
    ret.requireNum = []
    # 删除上次的展示
    text.delete('1.0', 'end')
    # 显示框
    showbox.set_content()


# 开始计算
btn_start = tk.Button(frameInput4, text='start', command=start_caculate, font=('宋体', 14))
btn_start.pack(padx=80, pady=10, side=LEFT, ipadx=20)
# 删除
btn_clear = tk.Button(frameInput4, text='clear', command=clearShow, font=('宋体', 14))
btn_clear.pack(pady=10, side=LEFT, ipadx=20)

window.mainloop()
