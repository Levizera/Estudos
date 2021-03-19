from tqdm import tqdm
from tqdm.auto import tqdm

# First Method --> Simple
"""
for i, x in enumerate(list(range(100001))):
    print(i, end="\r")
"""


#Second Method --> Better 
 
loop = tqdm(total= 5000, position= 0, leave= False)

for k in range(5000):
    loop.set_description("Carregando... ".format(k))
    loop.update(1)
loop.close()



#Third Method 
"""
for i in tqdm(range(10001)):
    print(" ", end="\r")
"""  