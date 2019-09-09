from pykalman import KalmanFilter
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import data_process

df = pd.read_csv('cgm_data.csv', encoding='utf-8')
data = data_process.load_cgm_data(df=df, col_name="electricCurrent1")
train_x, test_x, train_y, test_y = data_process.parse_data(data, [5635, 5800], 1, 1);

app_filter_out_0_18 = [0.21035896540540538, 0.37077446107438017, 0.4441940664252752, 0.5204837666972472, 0.5649639402910835, 0.6181412654325202, 0.6472234989330242, 0.6641898416393339, 0.6769227417837276, 0.6858119411434191, 0.7054792184201693, 0.7151946433396086, 0.7178465191389601, 0.7243753914908315, 0.7302564141489174, 0.7399686609290128, 0.7436825059201042, 0.7370750166831442, 0.7242257383637674, 0.7131325648910657, 0.6787175703761883, 0.7024196195371697, 0.6961610649883533, 0.6920536067334262, 0.6824412384898221, 0.6617673095186701, 0.6615003884053061, 0.658664953568357, 0.6578681754831234, 0.6600055098213996, 0.6789659154369119, 0.669063391903309, 0.6519233950031307, 0.6428027041853472, 0.6330924805749295, 0.6384248326866093, 0.648841092682101, 0.6434400568870394, 0.6372351315321401, 0.6422077376350819, 0.6263173950387847, 0.6329142774411888, 0.6388399307101198, 0.6294276317611488, 0.6237824385839054, 0.6280582904243792, 0.625543999068132, 0.6265541379807031, 0.6187042712024657, 0.5949306552218394, 0.6006101924365317, 0.5192094783423489, 0.5594275762245747, 0.5778417499546098, 0.597375592894368, 0.5995545370459435, 0.6020486709752306, 0.6063458110795643, 0.6128903623242159, 0.5969675792412806, 0.6535559664051146, 0.6438741526844762, 0.6396482304288773, 0.6363427267957554, 0.6214041172948669, 0.6195807461796685, 0.6322174043772549, 0.6186966886896886, 0.6092910583115454, 0.6105669054844234, 0.6215132056989457, 0.630825412121112, 0.6497061908160812, 0.6541167879853307, 0.664992205064554, 0.6652130234551749, 0.6642938451953352, 0.67167135714327, 0.6733208773227676, 0.677063705056918, 0.6800521527189849, 0.6852057637617446, 0.691248308918173, 0.6882973374796504, 0.6895529338416906, 0.690909027349956, 0.6912669729264925, 0.6909698424121266, 0.6822620177675585, 0.6877201874850407, 0.6907703087321592, 0.6927720881510663, 0.6903614864911689, 0.6882473721820107, 0.6905842455745612, 0.6862653638797522, 0.6871552593922452, 0.682950833576954, 0.6769991821142389, 0.6730931428320869, 0.6673373244054845, 0.6630277575171486, 0.6564750540729527, 0.6521745473618884, 0.6456277866299676, 0.6344145197282683, 0.6355681243049925, 0.6230239535108919, 0.5738233456021393, 0.6165524257577248, 0.6009671254035834, 0.5790334466034763, 0.5880487294292163, 0.5870487509519929, 0.6119309178281338, 0.5926135410398355, 0.5873843582936509, 0.5839524716403233, 0.6056424371371464, 0.5911466982453749, 0.5938703923111025, 0.5876771716831645, 0.5836125917581961, 0.5846693876956995, 0.5965360293823185, 0.5697407283566438, 0.5883345765633891, 0.5920248108242092, 0.585401825451331, 0.5443436700767474, 0.5833717370269251, 0.5962164361138969, 0.5929412281198091, 0.5918558256596791, 0.5927396335454042, 0.5938517241240229, 0.5940495317902449, 0.5947114038334318, 0.5956778390213573, 0.6021646657239076, 0.6096142455480367, 0.6123751637889786, 0.6131230370024949, 0.624254885822679, 0.6342209152904501, 0.6450179788741699, 0.6505078859281274, 0.6588993444675363, 0.6660027691382145, 0.6743890709997679, 0.6825532116407843, 0.6884433484318628, 0.6928410677953974, 0.6925349614708282, 0.6955263731022834, 0.694829365855595, 0.6975642311541892, 0.6913783421508736, 0.6862544736623231, 0.6834237560877116, 0.6783736625176127, 0.684636230837461, 0.6765091478347206, 0.6307395045503383, 0.6427331463040216, 0.6383673417561468, 0.6386943936156539, 0.6319923723257566, 0.631850277018163, 0.6211160006646699, 0.617795504539764, 0.6108278196136271, 0.6051908589085013, 0.5967028932255671, 0.5916643319409062, 0.5942101127334385, 0.5863039763812129, 0.5811152183776057, 0.5771778104272467, 0.5740616607361209]
app_filter_out_0_10 = [0.18531623142857145, 0.32547636525773194, 0.39717749967838445, 0.47074314356641456, 0.5194321282419504, 0.5736972566113256, 0.6086162991788544, 0.6324004025238396, 0.6510041904797259, 0.6649961863575494, 0.6860807826625357, 0.698958581588931, 0.7054294553304129, 0.7139159117425996, 0.7213642232604623, 0.731400491807749, 0.7366343750522607, 0.7333449015864134, 0.7242529228321368, 0.7155262087239658, 0.6878289487749791, 0.7039975487789016, 0.6986519624529399, 0.694750519655325, 0.6864664954673438, 0.6691290919786426, 0.6669304575229776, 0.6632348049536312, 0.661373954117901, 0.6621068165680983, 0.6764422408426636, 0.6693405254034868, 0.655793413724634, 0.6475789321757508, 0.6386562527454421, 0.6413444575993856, 0.6487430075959827, 0.6445242272283405, 0.6393541864145934, 0.6426902383811355, 0.6300698886793278, 0.6342413575958165, 0.6385404729135691, 0.6312231938716699, 0.6263009223313536, 0.6289814089341523, 0.6267557596893386, 0.6272223762839725, 0.6208717584826092, 0.6015998521374724, 0.6042623112686311, 0.5392937348795839, 0.5654797536499585, 0.5783184808753498, 0.59354352298384, 0.5962914566102213, 0.5991334171264551, 0.603298594524286, 0.6092659144738898, 0.5977295838371646, 0.6420028719536054, 0.6375139909296751, 0.6359106027548109, 0.6343221807410127, 0.623126118264724, 0.6212277175248869, 0.6307153423029607, 0.6204936896359291, 0.6126152808180753, 0.6127200525791552, 0.6207422892642286, 0.6282700626318234, 0.6438009237991923, 0.6488630504365012, 0.6588305880274393, 0.6606687530384104, 0.6611739308259543, 0.667815607606073, 0.670153804863432, 0.6739513164776482, 0.6771411031524821, 0.6819783411274933, 0.6875997620857677, 0.6862659408699077, 0.6878016490244053, 0.6893406751957587, 0.6900457247722728, 0.6901421044131609, 0.6835212687694087, 0.6874712608975055, 0.6899359417024998, 0.6917347736777442, 0.6901202489214187, 0.688523701644382, 0.6902858599295657, 0.6869717780538253, 0.6874804043812494, 0.6840878355201859, 0.6791025982262121, 0.6754641537548595, 0.6702994683756259, 0.6661118557195398, 0.6601281642376255, 0.6557610041794739, 0.6496462684399255, 0.6397468888632207, 0.6392130631972325, 0.6283684921999606, 0.5882523662408338, 0.6179398441852192, 0.6053147921973238, 0.5869001094198373, 0.5918610016029814, 0.5900450975637126, 0.6087932963539985, 0.5944572553388608, 0.5898489643547355, 0.5864856318060837, 0.6028498548695402, 0.5922104643618384, 0.594063937414059, 0.5891437045961442, 0.5855527032378437, 0.5858592243026718, 0.5948651046926753, 0.5742550886383911, 0.5876504930031848, 0.5907358706439025, 0.5858783402102008, 0.5534774061278653, 0.5816863975004978, 0.5922377893850261, 0.5907382929002958, 0.5904802902328633, 0.5915465832304007, 0.5927430096653932, 0.5931980149525099, 0.5939482968492927, 0.59491408454542, 0.6002191408499701, 0.606600195224446, 0.6095845743652679, 0.6109263067137863, 0.6202695332157385, 0.6291796192082163, 0.6390281776337129, 0.6449614921808974, 0.653055671572784, 0.6602177527636325, 0.6683723443301883, 0.6764149124987147, 0.6827029300315277, 0.6877103996819086, 0.6888558783155515, 0.6922010907656785, 0.6925515804218595, 0.6953165751051554, 0.6910616106874256, 0.6871197558111699, 0.6846610166304464, 0.6803573291278386, 0.6847438827912395, 0.6783268156100257, 0.6418602749223786, 0.6482830754360887, 0.6433521530712311, 0.6422625419984255, 0.6360307157427514, 0.6348280435735497, 0.62558631198121, 0.6217686799847733, 0.6152186183602014, 0.6096016983428194, 0.6017384402346689, 0.5964176865628384, 0.5971345524027346, 0.5901301792296794, 0.5850180809795922, 0.580868848713049, 0.5774223609049577]
app_filter_out_0_01 = [0.15348710770992363, 0.2594066479817525, 0.3157247501507505, 0.3698607938133843, 0.4093591731548363, 0.4500685632211055, 0.48132324034513185, 0.5067063764752942, 0.5287675325764246, 0.5478835213888439, 0.5687691850951732, 0.5860527577646409, 0.6001420683514113, 0.6140152176258568, 0.626801004284974, 0.6398860839475587, 0.6508160317153328, 0.6580281758150189, 0.6620869078924655, 0.6649836784046326, 0.6599593502591936, 0.6684135264458493, 0.6699324087033587, 0.6713025871371339, 0.6706112246380963, 0.6659876404510399, 0.6655100119112224, 0.6643392423432796, 0.66357649698038, 0.6636251576011236, 0.6685390150277275, 0.6667871137652519, 0.6622533434722293, 0.6587422631364571, 0.6545344856764247, 0.6539701663114039, 0.6553751729524647, 0.6532576791832264, 0.650605322559471, 0.650709756477598, 0.6455016111342056, 0.6455024892402628, 0.6459451269952522, 0.6426637383767143, 0.639841900368194, 0.6394976070181034, 0.6377134216073576, 0.6368353120533794, 0.6336845743741363, 0.6256795212501512, 0.6243263714680456, 0.599540834932211, 0.6030303074272683, 0.6039789892375944, 0.606898989412428, 0.6065961244097939, 0.6066165789472293, 0.607371355141498, 0.6090851057117874, 0.6050402118425243, 0.6199339723296537, 0.6204526934474384, 0.6215110815531945, 0.6223215367203594, 0.6195208356687614, 0.619195339831717, 0.622729370557379, 0.6198898773486046, 0.6171732390987235, 0.6167765545891346, 0.6192153981689122, 0.6220112555950019, 0.6280752111602066, 0.6313535491590365, 0.6365288185098689, 0.6392975111047, 0.6415083278706262, 0.6457176237501566, 0.6486429976959821, 0.6520263568391998, 0.6552351255934503, 0.6590221740762022, 0.6631852410255075, 0.6650380176711275, 0.6675980617613807, 0.670061834261178, 0.6721439881386289, 0.6738808257945964, 0.6730964108524129, 0.6754789096059697, 0.6774875218627268, 0.679305065028326, 0.6799189484832152, 0.6803271848431355, 0.6817273528498434, 0.6813745561201516, 0.6820860842496996, 0.6814046583671468, 0.6799045394501609, 0.6785471192291531, 0.6764353108346433, 0.6743771356216907, 0.6714839790715639, 0.6688660338134326, 0.6654663543490442, 0.6604757913693403, 0.6583159903482585, 0.6526803352378331, 0.6362423515457948, 0.6421305897781091, 0.6353840297365175, 0.6260396870332765, 0.6240633215200513, 0.6203606789121, 0.6240783550215228, 0.6175764900265054, 0.6137546455698707, 0.6102963537690377, 0.6137933805009481, 0.6090061340936543, 0.6080610752144113, 0.6049971314215481, 0.6022246450429308, 0.6007466572592844, 0.6025015591792894, 0.5945181326420248, 0.5973072788128955, 0.597475072629435, 0.5951236176018568, 0.5828354422407037, 0.5899754520833999, 0.5929022155320102, 0.5923110231282094, 0.5920705717603714, 0.5922947496427816, 0.592644855049584, 0.5928144042789175, 0.5931150775790045, 0.5935344017828458, 0.5955336116583753, 0.5982261604670246, 0.6000735720197357, 0.6014507438367152, 0.60564195704635, 0.6101707416637707, 0.6154467435190443, 0.6197791097768643, 0.6250246299816324, 0.6302129268188601, 0.6359384533687765, 0.6418555998897032, 0.6473571307374909, 0.6524825813206176, 0.6562369602004143, 0.6605177176987512, 0.6636550072855036, 0.6673773760616472, 0.6685368712326915, 0.6692915656113835, 0.6701217221741536, 0.6699893965421291, 0.6725201982738849, 0.6714234566014486, 0.6592398749922324, 0.6598481793683764, 0.6570118187025226, 0.65532878024023, 0.6518915619705526, 0.6499593263417961, 0.6452658506734192, 0.6420496066050276, 0.6378140375535069, 0.6336868718215927, 0.6286270334099642, 0.6241957632091503, 0.6218057920455358, 0.6169926268040177, 0.6126373135305397, 0.608549046664403, 0.6047024243881953]


kf = KalmanFilter(transition_covariance=0.18, observation_covariance=1)
measurements = train_y  # 3 observations
# kf = kf.em(measurements, n_iter=0)
(filtered_state_means, filtered_state_covariances) = kf.filter(measurements)
(smoothed_state_means, smoothed_state_covariances) = kf.smooth(measurements)

plt.plot(range(len(train_y)), train_y, label="source")
plt.plot(range(len(filtered_state_means)), filtered_state_means, label="py_filter")
# plt.plot(range(len(app_filter_out_0_18)), app_filter_out_0_18, label="app_filter")
plt.legend()
plt.show()

print(test_y,)
