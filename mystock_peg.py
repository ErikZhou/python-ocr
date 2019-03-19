
# coding: utf-8

# In[ ]:


import urllib.request
import certifi
#import ocr
import ocr_ut
import cvcrop
import blob

#certifi.where()
#'/Library/Frameworks/Python.framework/Versions/3.6/lib/python3.6/site-packages/certifi/cacert.pem'

pemfile = '/Library/Frameworks/Python.framework/Versions/3.6/lib/python3.6/site-packages/certifi/cacert.pem'

# Function definition is here
def printme( str ):
   "This prints a passed string into this function"
   print (str)
   return;

def down_file( name ):
   # Download the file from `url` and save it locally under `file_name`:
   #url='https://www.nasdaq.com//charts/BABA_peg.jpeg'
   url='https://www.nasdaq.com//charts/' + name + '_peg.jpeg'
   file_name= name + '_peg.jpeg'
   with urllib.request.urlopen(url,cafile=pemfile) as response, open(file_name, 'wb') as out_file:
       data = response.read() # a `bytes` object
       out_file.write(data)
       print(file_name)
       #ocr.ocrdigits(file_name)
   return file_name;

path = 'stock.txt'
days_file = open(path,'r')
#print (days_file.read())
stock_list = []
#print (days_file.readline())
while True:
    li = days_file.readline()
    if len(li) > 2:      
        #li.replace("\n","")
        li = li[:-1]
        stock_list.append(li)   
    #print(line)
    if not li: 
        break


        # close the file after reading the lines.
days_file.close()
#print(stock_list)
print('my stock count is :')
print(len(stock_list))

#printme('test')
#pow2 = []
file = open("mystock.txt","w")
 
for x in range(len(stock_list)):
    #print(stock_list[x])
    file_name = down_file(stock_list[x])
    #ocr.ocrdigits(file_name)
    cvcrop.imcrop(file_name)
    blob.imsplit(file_name)
    text = ocr_ut.im2string(file_name)
    peg = 0.0
    try:
        peg = float(text.replace(" ", "")) * 0.01
    except:
        print ("error message!")
    s2 = "{:.2f}".format( peg ) # new
    file.write(file_name + '\t\t' + s2 +'\n') 

file.close() 
