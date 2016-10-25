print "importing smbus and time"
import smbus
import time

print "adding bus and address"
bus = smbus.SMBus(1)
address = 0x48
print "bus: " + str(bus)
print "addr: " + str(address)
start = time.time()

lowT = 999999.99
highT = -999999.99
def getTmp():
     print ""
     print 'time since start: %.2f' % (time.time() - start)
     data = bus.read_word_data(address,0x00)
    # print bin(data)
   
    # print "random calcs" 
     a = data - ((data >> 8) << 8)
     b = data >> 8
     c = (a << 8) + b
     d = c >> 4
    # print bin(a)
    # print bin(b)
    # print bin(c)
    # print bin(d)
   
     tmpSum = d
    # print bin(tmpSum)
    # print hex(tmpSum)
  
     tmp = tmpSum*0.0625
     return tmp

def getFahr(cels):
     fahr = (1.8 * cels) + 32
     return fahr

while(True):
     cels = getTmp()
     fahr = getFahr(cels)
     if(fahr > highT):
          highT = fahr
     if(fahr < lowT):
          lowT = fahr
     print "cels: " + str(cels)
     print 'fahr: {0:.2f}  Low: {1:.2f}  High: {2:.2f}'.format(fahr, lowT, highT)

     time.sleep(1)
