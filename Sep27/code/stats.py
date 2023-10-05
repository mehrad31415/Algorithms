import numpy as np
import matplotlib.pyplot as plt
from scipy import stats

size = np.array([i for i in range(5, 2501, 5)])
#experiment 1
selection1 = [2412, 4770, 1808, 2562, 3545, 4487, 5637, 6700, 7970, 9058, 10670, 12937, 12150, 5195, 2491, 2800, 3258, 3283, 3475, 3849, 4145, 4854, 5008, 5120, 5579, 6133, 6387, 6708, 7241, 7458, 7825, 8841, 9141, 9616, 10358, 10637, 11304, 12649, 12229, 13154, 13512, 15195, 15212, 16204, 17629, 18141, 18291, 19874, 19833, 21524, 20529, 22812, 21733, 23891, 23491, 26508, 25049, 26279, 28958, 27208, 30766, 29400, 32437, 30841, 32350, 35271, 33595, 35475, 36566, 39758, 37558, 40283, 40958, 44187, 42550, 45304, 46212, 42429, 45479, 47641, 46691, 47341, 50374, 48374, 52716, 50162, 53283, 52070, 55883, 55371, 56808, 58995, 58904, 62545, 63470, 61358, 65954, 64429, 67233, 68620, 67804, 72566, 73191, 76804, 73500, 77124, 76179, 76791, 82254, 81650, 79970, 87062, 83012, 88008, 87091, 88545, 88329, 98537, 98308, 96320, 94787, 95683, 95333, 98625, 100404, 100875, 103458, 103458, 106283, 110395, 109137, 115570, 112487, 112912, 124350, 120179, 118737, 120145, 127191, 125220, 127062, 130616, 129066, 135695, 138916, 133537, 136991, 136637, 140425, 143562, 146725, 148158, 149683, 149646, 151095, 153716, 157025, 161341, 159646, 163641, 160650, 164533, 168712, 168437, 169920, 172304, 180912, 180170, 174016, 177208, 182937, 182449, 185070, 187595, 194971, 196437, 193787, 192167, 199925, 196974, 202412, 201170, 214283, 206762, 203954, 210595, 213325, 228683, 226412, 216375, 218016, 224558, 230862, 231112, 229962, 228320, 240083, 240899, 251474, 251166, 250970, 257537, 256912, 250637, 250379, 256246, 255366, 256741, 265020, 261175, 260812, 264745, 270124, 271154, 287254, 277579, 284104, 288804, 292033, 289583, 303641, 294204, 298529, 292121, 299987, 310695, 304712, 308120, 313887, 318391, 323516, 332816, 320137, 322466, 320975, 338549, 329091, 334033, 333983, 343345, 350262, 342937, 347341, 354962, 359308, 364262, 367425, 361925, 366262, 378262, 369029, 370500, 370404, 382208, 379579, 378958, 382191, 404466, 389054, 390791, 410308, 405191, 409795, 418370, 420733, 426666, 404020, 415687, 415800, 427820, 423174, 426491, 426745, 441329, 446666, 448362, 472183, 458045, 458416, 460370, 469904, 452450, 461716, 478454, 472245, 468699, 474512, 501191, 476387, 482654, 496429, 484654, 492616, 509374, 502966, 510616, 511779, 532504, 528291, 524516, 514616, 523891, 521196, 536446, 535454, 544766, 557141, 542041, 542425, 559341, 548666, 553179, 563025, 565825, 582058, 577133, 570754, 574158, 591137, 583245, 589025, 588033, 587808, 609016, 594437, 602737, 616729, 609325, 613204, 626729, 633508, 652537, 627266, 633154, 651429, 653858, 650317, 640912, 650683, 660304, 669212, 680162, 677558, 684304, 693408, 699133, 694933, 695241, 699950, 705658, 692204, 709904, 708400, 731675, 709466, 712804, 729566, 736566, 763287, 734604, 757179, 733179, 745691, 751383, 768354, 761929, 751199, 781862, 776074, 787675, 775791, 796279, 784370, 794275, 801521, 811525, 806437, 827541, 819004, 834825, 815458, 832925, 826170, 855145, 825787, 838295, 834866, 864908, 863833, 865075, 849612, 870404, 856037, 872679, 871866, 886616, 902458, 902670, 879837, 890333, 896537, 921066, 924495, 916150, 913458, 911783, 931458, 924075, 944704, 956020, 949108, 957716, 952516, 985600, 966025, 980862, 964354, 981533, 1003987, 983283, 995174, 980779, 994525, 1017820, 1015495, 1043716, 1006841, 1027237, 1033624, 1022341, 1042770, 1030220, 1060091, 1060179, 1058041, 1069321, 1062687, 1052479, 1079154, 1067566, 1066079, 1096375, 1083154, 1105070, 1101795, 1098870, 1121687, 1117708, 1103408, 1137012, 1147458, 1127045, 1136849, 1137237, 1137174, 1149525, 1171354, 1176304, 1160966, 1180020, 1196575, 1186737, 1233804, 1198808, 1195137, 1199004, 1200029, 1242121, 1219579, 1219012, 1250337, 1245816, 1236645, 1248216, 1247066, 1248175, 1248379, 1275412, 1274275, 1274537, 1278066, 1298678, 1298158, 1287429, 1289541, 1304516, 1326208, 1348879, 1325496, 1332370, 1333933, 1341545, 1344516, 1367404, 1362191, 1367079, 1358129, 1366729, 1351200, 1368887]
merge1     = [3833, 6183, 8558, 10637, 1741, 1595, 1753, 2233, 2408, 2362, 3016, 3008, 3245, 3941, 3725, 4104, 4620, 4741, 5112, 5299, 5683, 6050, 6154, 6325, 6604, 6925, 7304, 11458, 7946, 8437, 8754, 9787, 9483, 9670, 9929, 10445, 10808, 8425, 6891, 7295, 7362, 7533, 7545, 8237, 8891, 9625, 8745, 10441, 9320, 9499, 9554, 9887, 12804, 10708, 10512, 11749, 10495, 11154, 12375, 11933, 12608, 11712, 13670, 12683, 12558, 14033, 12729, 16566, 13833, 13454, 12187, 14216, 12879, 13916, 12845, 14333, 16575, 13287, 16766, 16266, 14704, 14408, 15791, 14291, 16279, 15424, 16475, 15054, 18037, 16245, 15633, 17603, 16016, 18729, 16966, 18129, 19416, 18220, 17479, 20141, 17179, 21225, 18975, 24308, 18708, 21658, 19058, 19679, 95537, 21833, 19737, 19916, 16912, 19854, 20050, 19862, 17954, 20729, 20670, 18670, 18662, 19220, 22241, 22912, 19429, 20050, 19800, 20304, 20316, 20949, 20858, 24000, 21324, 21662, 33295, 25241, 21575, 22425, 25000, 25187, 23695, 26154, 24791, 24987, 25558, 23904, 24454, 24374, 25016, 25200, 25437, 25954, 25666, 30429, 36974, 30775, 32883, 34754, 31908, 36954, 34375, 33504, 33745, 34029, 34221, 34891, 38570, 40974, 35495, 36062, 38179, 36612, 39008, 35658, 38908, 37521, 36512, 37020, 39166, 38095, 38258, 37695, 48316, 39654, 41496, 39262, 40183, 46995, 50125, 41850, 44566, 39479, 42979, 41070, 41900, 44154, 43203, 46087, 43433, 45646, 49454, 45879, 45104, 58912, 44358, 48546, 44591, 44791, 48829, 48245, 47191, 46520, 46129, 49458, 61145, 50046, 49591, 48054, 50845, 50491, 57570, 53583, 51191, 51049, 51279, 59091, 50762, 53971, 54212, 54754, 53529, 68237, 58200, 53566, 53208, 61587, 57920, 58100, 54679, 57041, 66758, 55279, 54537, 58187, 57750, 64950, 58320, 60745, 58766, 72516, 61425, 62691, 60970, 69470, 63404, 62383, 60545, 71925, 63724, 61108, 63991, 68966, 71495, 66120, 65270, 76462, 63666, 67933, 64941, 74696, 68137, 65316, 67795, 74878, 69200, 71950, 78796, 70587, 69887, 72200, 79795, 71420, 71071, 76812, 72570, 70712, 70700, 78387, 71029, 74399, 79075, 128241, 63441, 68187, 63091, 63545, 65574, 73162, 64704, 75458, 64145, 66366, 64904, 75441, 67300, 67274, 76150, 73279, 67716, 73450, 73487, 73366, 77108, 71320, 76370, 76949, 69312, 73845, 83316, 70158, 76900, 71045, 71483, 84612, 71241, 73045, 84975, 75337, 73024, 81820, 78137, 82754, 76533, 76087, 84954, 84745, 80012, 81612, 75962, 81958, 85808, 83295, 80175, 84237, 86633, 81858, 86370, 79925, 86512, 86500, 84012, 86404, 85125, 87925, 84820, 80770, 85996, 88387, 87791, 85749, 92529, 84450, 93004, 87670, 86433, 94029, 86108, 90533, 90354, 93100, 86145, 95845, 89195, 95704, 93141, 92237, 93674, 92799, 96708, 100345, 90599, 98862, 90562, 99358, 95087, 101279, 90133, 106096, 99833, 100487, 91970, 95970, 94183, 93408, 168091, 99141, 95512, 103100, 92029, 94845, 96200, 99562, 99212, 100499, 95137, 96566, 101174, 98604, 103900, 100783, 102445, 99191, 99258, 110033, 101587, 104129, 100841, 102320, 111083, 102650, 105529, 102949, 106062, 111087, 105241, 113754, 102066, 109341, 104962, 105566, 111158, 105012, 110583, 113325, 109179, 119199, 114550, 105695, 113220, 112608, 107095, 111937, 109841, 111562, 112521, 109033, 109337, 112287, 111741, 116979, 119058, 111741, 113820, 113458, 113937, 116991, 120429, 117325, 114949, 122187, 119216, 118612, 121637, 121137, 119479, 118612, 125191, 124291, 120508, 123145, 126041, 133120, 122241, 128762, 136075, 182604, 121941, 128504, 131175, 135329, 122449, 122950, 130041, 122749, 122654, 129137, 130320, 136800, 127137, 129545, 132362, 134037, 130562, 129633, 131987, 133766, 127079, 133745, 127274, 129524]

#experiment 2
selection2 = [933, 2583, 2858, 1716, 2429, 3454, 4299, 5254, 6574, 8058, 9641, 8658, 10362, 11720, 5220, 2204, 2554, 2608, 2837, 3112, 3262, 3887, 4341, 4491, 4858, 5000, 5366, 5700, 6658, 6829, 7345, 7400, 7716, 8858, 8791, 9445, 10337, 10466, 11379, 12274, 12270, 12750, 13762, 14808, 15816, 15216, 16991, 17354, 18670, 18145, 19408, 19416, 21812, 22120, 24196, 25375, 24266, 26141, 25258, 29104, 28304, 27274, 29904, 28896, 31687, 30962, 34299, 33300, 36229, 34691, 36954, 38346, 40495, 38475, 41091, 40229, 44508, 41720, 46412, 46658, 45583, 52283, 48775, 48024, 52449, 46904, 51708, 51941, 52033, 59841, 53079, 55216, 54716, 59425, 57387, 60175, 59820, 62829, 61966, 62933, 65362, 67387, 67775, 66637, 70703, 71779, 71883, 72987, 74333, 79112, 84524, 78854, 83387, 83562, 84020, 85083, 85221, 86416, 91125, 89387, 90162, 91795, 93387, 94912, 96500, 99341, 108937, 107187, 104566, 104445, 105146, 106379, 113512, 116254, 112691, 113029, 115104, 116158, 124291, 122241, 121254, 126591, 125191, 125212, 127479, 127137, 132895, 133541, 135962, 137199, 146554, 152583, 143387, 146095, 152933, 148570, 148125, 152675, 153825, 152470, 156046, 160433, 164562, 162304, 165358, 168749, 166821, 169091, 171904, 170195, 184287, 180908, 178862, 180104, 180650, 182912, 186754, 185571, 192524, 201337, 195504, 197433, 202754, 201737, 204554, 210958, 217341, 208291, 207858, 212670, 215991, 220754, 219187, 226445, 225966, 227379, 231541, 233904, 244803, 242804, 251187, 245962, 254375, 250041, 246016, 250137, 260804, 269608, 266737, 265908, 274149, 285424, 275558, 277624, 280783, 283429, 289600, 295575, 300837, 292412, 293570, 304987, 307504, 304195, 302654, 310279, 314758, 324812, 324966, 314841, 321566, 320591, 342525, 334358, 330320, 331837, 337520, 357841, 350962, 350687, 352812, 365737, 352691, 351483, 356870, 367262, 395470, 369729, 378066, 369187, 382037, 376121, 390858, 387750, 397958, 395170, 403346, 397199, 415525, 397937, 414979, 403795, 418183, 408179, 422174, 427616, 425758, 436978, 440954, 433833, 455162, 440862, 434108, 463062, 446441, 452904, 464874, 468125, 457787, 457508, 495824, 473875, 471262, 505604, 484445, 506562, 501366, 485762, 496208, 484129, 529375, 515837, 521304, 523229, 521300, 534512, 535308, 520370, 519637, 534229, 541108, 537108, 542212, 541529, 548796, 563912, 549683, 551046, 559604, 567249, 588733, 574104, 579391, 587616, 581383, 589716, 610937, 603087, 586570, 617879, 600641, 630783, 617650, 604137, 622575, 619254, 617358, 642887, 625145, 646045, 629166, 637404, 659537, 641354, 663925, 681737, 659020, 703820, 669754, 678724, 678025, 694416, 669770, 683016, 701749, 701904, 730945, 699179, 721875, 701491, 719650, 714379, 723183, 737525, 732283, 739704, 739179, 747929, 760245, 765545, 780054, 759245, 766012, 777949, 777033, 768433, 792337, 771158, 806966, 789091, 816037, 780716, 802291, 804350, 821770, 823975, 833133, 829008, 836600, 821620, 848662, 857529, 844283, 866320, 856166, 905850, 921008, 860454, 871079, 922116, 913645, 906879, 942654, 910429, 904299, 902520, 888850, 928012, 943766, 911883, 978579, 922979, 934591, 918516, 946791, 953041, 926920, 974150, 945729, 989516, 970666, 985496, 971904, 983312, 1047008, 976587, 982562, 1027920, 1026637, 1007308, 1079520, 1029066, 1013970, 1026291, 1044529, 1043391, 1054120, 1050354, 1069924, 1041983, 1083291, 1048471, 1097962, 1097641, 1063387, 1089441, 1093628, 1156258, 1102029, 1105874, 1112883, 1124362, 1148274, 1125770, 1104879, 1123475, 1167091, 1133750, 1160012, 1185754, 1150504, 1168100, 1168370, 1180991, 1184462, 1226008, 1232645, 1184433, 1245995, 1224816, 1247004, 1224441, 1218641, 1230287, 1230299, 1245945, 1253304, 1264408, 1238937, 1278962, 1313462, 1281279, 1271704, 1272454, 1288775, 1304541, 1304170, 1303975, 1315471, 1296108, 1336291, 1361700, 1393083, 1343658, 1348979, 1337641, 1338595, 1340254, 1375512, 1363920, 1360441, 1384149, 1383995, 1380058, 1404737, 1429404, 1391016, 1403633, 1460866, 1433733]
merge2     = [1779, 3704, 6249, 9620, 9187, 1675, 1599, 1662, 2175, 2270, 2595, 3008, 3237, 3358, 3741, 3837, 4179, 4408, 4570, 5112, 5237, 5246, 6212, 6304, 6595, 6779, 7074, 7399, 7787, 8141, 8262, 8516, 9329, 9429, 11658, 10108, 10437, 10766, 10958, 11774, 11645, 12924, 7449, 7354, 7987, 7520, 8608, 8033, 9100, 8574, 9312, 9045, 9974, 10183, 10833, 11058, 12262, 12454, 11337, 18712, 12345, 10683, 12720, 11758, 13183, 12075, 13820, 12754, 15008, 13220, 15437, 13487, 16158, 14291, 16312, 14604, 19458, 12916, 12504, 13787, 13383, 13745, 14087, 14945, 13850, 14620, 16483, 15791, 16425, 18600, 15920, 16050, 14983, 20670, 15237, 16700, 16683, 17537, 17000, 15983, 16195, 16224, 17150, 17716, 18858, 18991, 18716, 18296, 18479, 105337, 23029, 18062, 18716, 17487, 17400, 16508, 17787, 18625, 21250, 18662, 17766, 17662, 18162, 18150, 18596, 18737, 24591, 21208, 22058, 19308, 20883, 23079, 24416, 24316, 20791, 20779, 20929, 21054, 22183, 21887, 23737, 24162, 21796, 22300, 28137, 26245, 22745, 23058, 22987, 23441, 29866, 30708, 23975, 24000, 29879, 29162, 33299, 30737, 29874, 30037, 30666, 32300, 37100, 33937, 31112, 33816, 31583, 31625, 32599, 32662, 45037, 36491, 33383, 36337, 34487, 36133, 35699, 35145, 35908, 50062, 37983, 36283, 36299, 36687, 39346, 37704, 41945, 37662, 37733, 40037, 37591, 39133, 39512, 39675, 40100, 43512, 40879, 39629, 41500, 41354, 48920, 42366, 43199, 42170, 41708, 41858, 51937, 43391, 42833, 42862, 47854, 50424, 56554, 44929, 45800, 45491, 44129, 56404, 46570, 46362, 47254, 47033, 48104, 48421, 50325, 48808, 46704, 49104, 52012, 50308, 49837, 49408, 67783, 50095, 51354, 54258, 52195, 62816, 51725, 51808, 56012, 60670, 52149, 56745, 53325, 53754, 59341, 59108, 55129, 54125, 61712, 57733, 56820, 55833, 65979, 55158, 58908, 59791, 66283, 58779, 60829, 58733, 71287, 61637, 59183, 59958, 65133, 59579, 61504, 64545, 64387, 61991, 65341, 76779, 64620, 63216, 68658, 68929, 64787, 94162, 76091, 71099, 67545, 74041, 69716, 87133, 74945, 69900, 67745, 69166, 81641, 68770, 142608, 69850, 68858, 63729, 75308, 69595, 67275, 75816, 66058, 67295, 76433, 69829, 65604, 70075, 63483, 73258, 72829, 71808, 77158, 77316, 72866, 75429, 66374, 71033, 83254, 75841, 73137, 79341, 74629, 82420, 67991, 69620, 83095, 70779, 70841, 79520, 71091, 82000, 79404, 77999, 82424, 80637, 83916, 74191, 79124, 82758, 82616, 90108, 83745, 88912, 79704, 83645, 88778, 84058, 93887, 86066, 93683, 82758, 86845, 88087, 88408, 92120, 81287, 82366, 81404, 90758, 80125, 84170, 87729, 91350, 83745, 84716, 91500, 88258, 89916, 85312, 97062, 90329, 91724, 83649, 92179, 87445, 108366, 92441, 103737, 96070, 106137, 95208, 107695, 97258, 101891, 103450, 103550, 97225, 103775, 95683, 94945, 106679, 95262, 101062, 102658, 110304, 95399, 163716, 91266, 97433, 104204, 93316, 101466, 94724, 102808, 94749, 100225, 99033, 93825, 102537, 96820, 99887, 98895, 99366, 102991, 99625, 107091, 100041, 102312, 106487, 101791, 108129, 105479, 102629, 110554, 103191, 104679, 110712, 102712, 110258, 112408, 105016, 113679, 105358, 106233, 112104, 103487, 113012, 113954, 108041, 110791, 115625, 107191, 111058, 117004, 109891, 110120, 116333, 113275, 109349, 118029, 116329, 112641, 116541, 118045, 111512, 116666, 119312, 119891, 113975, 119454, 119566, 116304, 114370, 120162, 120879, 117000, 118916, 122445, 132050, 120174, 119870, 122345, 122283, 122966, 119412, 124616, 127637, 202179, 121033, 121745, 123987, 127083, 125691, 122758, 123612, 125499, 128408, 129504, 128429, 125141, 128599, 127329, 127916, 129262, 125120, 128441, 129679, 133983, 132287, 130387, 129445]

# mean and median
median = np.median(selection1)
mean = np.mean(selection1)
print(f"median for selection1 {median}")
print(f"mean for selection1 {mean}")

median = np.median(merge1)
mean = np.mean(merge1)
print(f"median for merge1 {median}")
print(f"mean for merge1 {mean}")

median = np.median(selection2)
mean = np.mean(selection2)
print(f"median for selection2 {median}")
print(f"mean for selection2 {mean}")

median = np.median(merge2)
mean = np.mean(merge2)
print(f"median for merge2 {median}")
print(f"mean for merge2 {mean}")