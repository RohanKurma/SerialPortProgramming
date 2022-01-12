import serial.tools.list_ports

ports = serial.tools.list_ports.comports()
serailInst = serial.Serial()

portList = []

for onePort in ports:
    portList.append(str(onePort))
    print(str(onePort))

val = input("select port: COM ")

for x in range(0, len(portList)):
    if portList[x].startswith("COM" +str(val)):
        portVar = "COM" +str(val)
        print(portList[x])

serailInst.baudrate = 9600
serailInst.port = portVar
serailInst.open()

while True:
    if serailInst.in_waiting:
        packet = serailInst.readLine()
        print(packet.decode('utf'))
