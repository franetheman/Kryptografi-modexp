import random

# Function code
def modexp(b, e, m):
    if m == 1:
        return 0
    r = 1
    b %= m
    while e > 0:
        if e % 2 == 1:
            r = (r*b)%m
        e = e >> 1
        b = (b**2)%m
    return r

# Misc driver code
b32 = [
    [1966758622, 1071479546, 2631363222],
    [3156512288, 2445713601, 3598641416],
    [1435657545, 1930586633, 2813600845],
    [1641335488, 613975753, 2353514192],
    [535593225, 3848488653, 4043806331]
]

b64 = [
    [3867276190411408488, 1083167955091736790, 10327582571183739404],
    [7839779258864645767, 15456653946681654022, 17593428686470479729],
    [1495503322731413139, 924864416071670865, 4633398355502731012],
    [1837561488741147373, 11527791677604185021, 13528789831194303742],
    [4679923193848441079, 9567965054972851935, 12130448656844095469]
]

b128 = [
    [49341875532468960133133017127899390245, 1918701176578538762936461778687183522, 268927044207557850460772013822623838702],
    [102530324611595787995733649436362103057, 64097670525349035248146371488753855781, 105484008633908273005246309449218087150],
    [288781050452434311173347247729363242256, 287983497188597560668495364360850496908, 303746655824185332975091466309652037260],
    [21008110148258590949374811523960869731, 218920998003577105535361834276213182577, 334239149012019692576780113992209197401],
    [241483913870887409224430040752462162242, 87065838522482499184847924955134070718, 297038919773135933801001776604646159431]
]

print("32 bit nums")
n = b32[0]
print(modexp(n[0], n[1], n[2]), modexp(n[0], n[1], n[2]) == pow(n[0], n[1], n[2]))
n = b32[1]
print(modexp(n[0], n[1], n[2]), modexp(n[0], n[1], n[2]) == pow(n[0], n[1], n[2]))
n = b32[2]
print(modexp(n[0], n[1], n[2]), modexp(n[0], n[1], n[2]) == pow(n[0], n[1], n[2]))
n = b32[3]
print(modexp(n[0], n[1], n[2]), modexp(n[0], n[1], n[2]) == pow(n[0], n[1], n[2]))
n = b32[4]
print(modexp(n[0], n[1], n[2]), modexp(n[0], n[1], n[2]) == pow(n[0], n[1], n[2]))

print("64 bit nums")
n = b64[0]
print(modexp(n[0], n[1], n[2]), modexp(n[0], n[1], n[2]) == pow(n[0], n[1], n[2]))
n = b64[1]
print(modexp(n[0], n[1], n[2]), modexp(n[0], n[1], n[2]) == pow(n[0], n[1], n[2]))
n = b64[2]
print(modexp(n[0], n[1], n[2]), modexp(n[0], n[1], n[2]) == pow(n[0], n[1], n[2]))
n = b64[3]
print(modexp(n[0], n[1], n[2]), modexp(n[0], n[1], n[2]) == pow(n[0], n[1], n[2]))
n = b64[4]
print(modexp(n[0], n[1], n[2]), modexp(n[0], n[1], n[2]) == pow(n[0], n[1], n[2]))

print("128 bit nums")
n = b128[0]
print(modexp(n[0], n[1], n[2]), modexp(n[0], n[1], n[2]) == pow(n[0], n[1], n[2]))
n = b128[1]
print(modexp(n[0], n[1], n[2]), modexp(n[0], n[1], n[2]) == pow(n[0], n[1], n[2]))
n = b128[2]
print(modexp(n[0], n[1], n[2]), modexp(n[0], n[1], n[2]) == pow(n[0], n[1], n[2]))
n = b128[3]
print(modexp(n[0], n[1], n[2]), modexp(n[0], n[1], n[2]) == pow(n[0], n[1], n[2]))
n = b128[4]
print(modexp(n[0], n[1], n[2]), modexp(n[0], n[1], n[2]) == pow(n[0], n[1], n[2]))

fails = 0
vectors = []
for i in range(10**6):
    args = []
    for j in range(3):
        args.append(random.randint(1, (2**128)-1))
    if not modexp(args[0], args[1], args[2]) == pow(args[0], args[1], args[2]):
        fails += 1
    args.append(modexp(args[0], args[1], args[2]))
    vectors.append(args)

print(fails)
#f = open("modexp_runs1.txt", "w")
#f.write("Failures: {}\n".format(fails))
#f.write("Base, Exponent, Module, Result")
#for i in range(len(vectors)//2):
#    f.write("{}, {}, {}, {}\n".format(vectors[i][0],vectors[i][1],vectors[i][2],vectors[i][3]))
#f.close()
#f = open("modexp_runs2.txt", "w")
#for i in range(len(vectors)//2, len(vectors)):
#    f.write("{}, {}, {}, {}\n".format(vectors[i][0],vectors[i][1],vectors[i][2],vectors[i][3]))
