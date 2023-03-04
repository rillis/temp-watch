import clr, time, os

folder = __file__.rsplit('\\', 1)[0]

clr.AddReference(folder+r'\OpenHardwareMonitorLib.dll')

from OpenHardwareMonitor.Hardware import Computer

config = {"CPU": False, "GPU": False, "RAM": False, "Mainboard": False, "HDD": False}
id = {1: "CPU", 2: "GPU", 3: "RAM", 4: "Mainboard", 5: "HDD"}
i = ""
while i.lower() != "ok":
    os.system("cls")
    print("Setup Inicial: ")
    for c, i in zip(config, id):
        print(f"{i}) {c}: {'Habilitado' if config[c] else 'Desabilitado'}")
    print("a) Todos")
    print("ok) Continuar")
    i = input("Escolha uma opção: ")
    if i.isnumeric() and int(i) in id:
        config[id[int(i)]] = not config[id[int(i)]]
    if i.lower() == "a":
        for c in config:
            config[c] = True
    if i.lower() == "ok" and not any(config.values()):
        i = ""

os.system("cls")
print("Iniciando...")

c = Computer()
c.CPUEnabled = config["CPU"] # get the Info about CPU
c.GPUEnabled = config["GPU"] # get the Info about GPU
c.RAMEnabled = config["RAM"] # get the Info about RAM
c.MainboardEnabled = config["Mainboard"] # get the Info about Mainboard
c.HDDEnabled = config["HDD"] # get the Info about HDD
c.Open()

while True:
    stout = []
    for hid, hardware in enumerate(c.Hardware):

        hardware.Update()
        stout.append(f"{hardware.Name} ({hardware.HardwareType})")

        allsensors = {}

        for sid, sensor in enumerate(hardware.Sensors):
            if not sensor.SensorType in allsensors:
                allsensors[sensor.SensorType] = []
            allsensors[sensor.SensorType].append(sensor.Name+": "+str(round(sensor.Value,1)))
        for type in allsensors:
            sinfo = allsensors[type]
            stout.append(f"{type}: "+' | '.join(sinfo))
        stout.append(" ")
    os.system('cls')
    print('\n'.join(stout))
    time.sleep(1)
