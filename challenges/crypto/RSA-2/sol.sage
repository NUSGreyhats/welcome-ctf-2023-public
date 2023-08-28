from Crypto.Util.number import long_to_bytes, bytes_to_long
from secrets import randbits

c = 9141779787876217885893245581785342661162555266453461051068530650252221166636753917526448649474894200888812989665074004419870594104933907348185670534113403516493549767090644738165146480042743664488756962047250548471078556661966371339922083765348133426510512817067449094644604679392211977694731638185838369075217265152007459144719806421555177795957823399955812727792866556337701407623447387484461041207947538135564318594967603051753205921079459570510178653628808968822989036057150576524149233553862123103000796135069360807269363142292225808665947586846587298653198919813527886111550213773428411495566056845310181757285
N = 17024517151500852563752251872398859684519095315960257225238488395844074099586346111404994313809980870030798741245661189951082279664829634601545086068603019999926596939658339551613228261966995296199397320176066555174004496112604162254830317558950055642812361751105889404097361472602893222598442726530429531348676805026629819357319584695573672999928653170697562280634643632467517958125939309701800367050214592014062222324570516208801131221049723744107608447552939396733847669228959695621965674012654639697910044425914978458052259467240128271033410376458900032286136249265934367426337198473758730241235345521508982382280
l = 34
e = 0x10001

# from https://www.alpertron.com.ar/ECM.HTM
partial_factors = [5, 269, 353, 4243, 24247, 1924543, 16744603995961, 98234797292003, 346338676705159]

val = []
NN = 1

for p in partial_factors:
    d = pow(e, -1, p - 1)
    val.append(int(pow(c, d, p)))
    NN *= p

prefix = b'greyhats{'

assert N % NN == 0

k = crt(val, partial_factors) - (bytes_to_long(prefix) * 256^(l - len(prefix)))

print(long_to_bytes(int(k % NN)))
