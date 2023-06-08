"""Pre-calculated constant values for Gaussian quadrature methods."""

legendre_roots = {
    2: [-0.5773502691896257645091488, 0.5773502691896257645091488],
    3: [-0.7745966692414833770358531, 0, 0.7745966692414833770358531],
    4: [
        -0.8611363115940525752239465, -0.3399810435848562648026658,
        0.3399810435848562648026658, 0.8611363115940525752239465
    ],
    5: [
        -0.9061798459386639927976269, -0.5384693101056830910363144, 0,
        0.5384693101056830910363144, 0.9061798459386639927976269
    ],
    6: [
        -0.9324695142031520278123016, -0.6612093864662645136613996,
        -0.2386191860831969086305017, 0.2386191860831969086305017,
        0.6612093864662645136613996, 0.9324695142031520278123016
    ],
    7: [
        -0.9491079123427585245261897, -0.7415311855993944398638648,
        -0.4058451513773971669066064, 0, 0.4058451513773971669066064,
        0.7415311855993944398638648, 0.9491079123427585245261897
    ],
    8: [
        -0.9602898564975362316835609, -0.7966664774136267395915539,
        -0.5255324099163289858177390, -0.1834346424956498049394761,
        0.1834346424956498049394761, 0.5255324099163289858177390,
        0.7966664774136267395915539, 0.9602898564975362316835609
    ],
    9: [
        -0.9681602395076260898355762, -0.8360311073266357942994298,
        -0.6133714327005903973087020, -0.3242534234038089290385380, 0,
        0.3242534234038089290385380, 0.6133714327005903973087020,
        0.8360311073266357942994298, 0.9681602395076260898355762
    ],
    10: [
        -0.9739065285171717200779640, -0.8650633666889845107320967,
        -0.6794095682990244062343274, -0.4333953941292471907992659,
        -0.1488743389816312108848260, 0.1488743389816312108848260,
        0.4333953941292471907992659, 0.6794095682990244062343274,
        0.8650633666889845107320967, 0.9739065285171717200779640
    ],
    11: [
        -0.9782286581460569928039380, -0.8870625997680952990751578,
        -0.7301520055740493240934163, -0.5190961292068118159257257,
        -0.2695431559523449723315320, 0, 0.2695431559523449723315320,
        0.5190961292068118159257257, 0.7301520055740493240934163,
        0.8870625997680952990751578, 0.9782286581460569928039380
    ],
    12: [
        -0.9815606342467192506905491, -0.9041172563704748566784659,
        -0.7699026741943046870368938, -0.5873179542866174472967024,
        -0.3678314989981801937526915, -0.1252334085114689154724414,
        0.1252334085114689154724414, 0.3678314989981801937526915,
        0.5873179542866174472967024, 0.7699026741943046870368938,
        0.9041172563704748566784659, 0.9815606342467192506905491
    ],
    13: [
        -0.9841830547185881494728294, -0.9175983992229779652065478,
        -0.8015780907333099127942065, -0.6423493394403402206439846,
        -0.4484927510364468528779129, -0.2304583159551347940655281, 0,
        0.2304583159551347940655281, 0.4484927510364468528779129,
        0.6423493394403402206439846, 0.8015780907333099127942065,
        0.9175983992229779652065478, 0.9841830547185881494728294
    ],
    14: [
        -0.9862838086968123388415973, -0.9284348836635735173363911,
        -0.8272013150697649931897947, -0.6872929048116854701480198,
        -0.5152486363581540919652907, -0.3191123689278897604356718,
        -0.1080549487073436620662447, 0.1080549487073436620662447,
        0.3191123689278897604356718, 0.5152486363581540919652907,
        0.6872929048116854701480198, 0.8272013150697649931897947,
        0.9284348836635735173363911, 0.9862838086968123388415973
    ],
    15: [
        -0.9879925180204854284895657, -0.9372733924007059043077589,
        -0.8482065834104272162006483, -0.7244177313601700474161861,
        -0.5709721726085388475372267, -0.3941513470775633698972074,
        -0.2011940939974345223006283, 0, 0.2011940939974345223006283,
        0.3941513470775633698972074, 0.5709721726085388475372267,
        0.7244177313601700474161861, 0.8482065834104272162006483,
        0.9372733924007059043077589, 0.9879925180204854284895657
    ],
    20: [
        -0.9931285991850949247861224, -0.9639719272779137912676661,
        -0.9122344282513259058677524, -0.8391169718222188233945291,
        -0.7463319064601507926143051, -0.6360536807265150254528367,
        -0.5108670019508270980043641, -0.3737060887154195606725482,
        -0.2277858511416450780804962, -0.0765265211334973337546404,
        0.0765265211334973337546404, 0.2277858511416450780804962,
        0.3737060887154195606725482, 0.5108670019508270980043641,
        0.6360536807265150254528367, 0.7463319064601507926143051,
        0.8391169718222188233945291, 0.9122344282513259058677524,
        0.9639719272779137912676661, 0.9931285991850949247861224
    ],
    32: [
        -0.9972638618494815635449811, -0.9856115115452683354001750,
        -0.9647622555875064307738119, -0.9349060759377396891709191,
        -0.8963211557660521239653072, -0.8493676137325699701336930,
        -0.7944837959679424069630973, -0.7321821187402896803874267,
        -0.6630442669302152009751152, -0.5877157572407623290407455,
        -0.5068999089322293900237475, -0.4213512761306353453641194,
        -0.3318686022821276497799168, -0.2392873622521370745446032,
        -0.1444719615827964934851864, -0.0483076656877383162348126,
        0.0483076656877383162348126, 0.1444719615827964934851864,
        0.2392873622521370745446032, 0.3318686022821276497799168,
        0.4213512761306353453641194, 0.5068999089322293900237475,
        0.5877157572407623290407455, 0.6630442669302152009751152,
        0.7321821187402896803874267, 0.7944837959679424069630973,
        0.8493676137325699701336930, 0.8963211557660521239653072,
        0.9349060759377396891709191, 0.9647622555875064307738119,
        0.9856115115452683354001750, 0.9972638618494815635449811
    ],
}

legendre_weights = {
    2: [1.0, 1.0],
    3: [
        0.5555555555555555555555556, 0.8888888888888888888888889,
        0.5555555555555555555555556
    ],
    4: [
        0.3478548451374538573730639, 0.6521451548625461426269361,
        0.6521451548625461426269361, 0.3478548451374538573730639
    ],
    5: [
        0.2369268850561890875142640, 0.4786286704993664680412915,
        0.5688888888888888888888889, 0.4786286704993664680412915,
        0.2369268850561890875142640
    ],
    6: [
        0.1713244923791703450402961, 0.3607615730481386075698335,
        0.4679139345726910473898703, 0.4679139345726910473898703,
        0.3607615730481386075698335, 0.1713244923791703450402961
    ],
    7: [
        0.1294849661688696932706114, 0.2797053914892766679014678,
        0.3818300505051189449503698, 0.4179591836734693877551020,
        0.3818300505051189449503698, 0.2797053914892766679014678,
        0.1294849661688696932706114
    ],
    8: [
        0.1012285362903762591525314, 0.2223810344533744705443560,
        0.3137066458778872873379622, 0.3626837833783619829651504,
        0.3626837833783619829651504, 0.3137066458778872873379622,
        0.2223810344533744705443560, 0.1012285362903762591525314
    ],
    9: [
        0.0812743883615744119718922, 0.1806481606948574040584720,
        0.2606106964029354623187429, 0.3123470770400028400686304,
        0.3302393550012597631645251, 0.3123470770400028400686304,
        0.2606106964029354623187429, 0.1806481606948574040584720,
        0.0812743883615744119718922
    ],
    10: [
        0.0666713443086881375935688, 0.1494513491505805931457763,
        0.2190863625159820439955349, 0.2692667193099963550912269,
        0.2955242247147528701738930, 0.2955242247147528701738930,
        0.2692667193099963550912269, 0.2190863625159820439955349,
        0.1494513491505805931457763, 0.0666713443086881375935688
    ],
    11: [
        0.0556685671161736664827537, 0.1255803694649046246346943,
        0.1862902109277342514260976, 0.2331937645919904799185237,
        0.2628045445102466621806889, 0.2729250867779006307144835,
        0.2628045445102466621806889, 0.2331937645919904799185237,
        0.1862902109277342514260976, 0.1255803694649046246346943,
        0.0556685671161736664827537
    ],
    12: [
        0.0471753363865118271946160, 0.1069393259953184309602547,
        0.1600783285433462263346525, 0.2031674267230659217490645,
        0.2334925365383548087608499, 0.2491470458134027850005624,
        0.2491470458134027850005624, 0.2334925365383548087608499,
        0.2031674267230659217490645, 0.1600783285433462263346525,
        0.1069393259953184309602547, 0.0471753363865118271946160
    ],
    13: [
        0.0404840047653158795200216, 0.0921214998377284479144218,
        0.1388735102197872384636018, 0.1781459807619457382800467,
        0.2078160475368885023125232, 0.2262831802628972384120902,
        0.2325515532308739101945895, 0.2262831802628972384120902,
        0.2078160475368885023125232, 0.1781459807619457382800467,
        0.1388735102197872384636018, 0.0921214998377284479144218,
        0.0404840047653158795200216
    ],
    14: [
        0.0351194603317518630318329, 0.0801580871597602098056333,
        0.1215185706879031846894148, 0.1572031671581935345696019,
        0.1855383974779378137417166, 0.2051984637212956039659241,
        0.2152638534631577901958764, 0.2152638534631577901958764,
        0.2051984637212956039659241, 0.1855383974779378137417166,
        0.1572031671581935345696019, 0.1215185706879031846894148,
        0.0801580871597602098056333, 0.0351194603317518630318329
    ],
    15: [
        0.0307532419961172683546284, 0.0703660474881081247092674,
        0.1071592204671719350118695, 0.1395706779261543144478048,
        0.1662692058169939335532009, 0.1861610000155622110268006,
        0.1984314853271115764561183, 0.2025782419255612728806202,
        0.1984314853271115764561183, 0.1861610000155622110268006,
        0.1662692058169939335532009, 0.1395706779261543144478048,
        0.1071592204671719350118695, 0.0703660474881081247092674,
        0.0307532419961172683546284
    ],
    20: [
        0.0176140071391521183118620, 0.0406014298003869413310400,
        0.0626720483341090635695065, 0.0832767415767047487247581,
        0.1019301198172404350367501, 0.1181945319615184173123774,
        0.1316886384491766268984945, 0.1420961093183820513292983,
        0.1491729864726037467878287, 0.1527533871307258506980843,
        0.1527533871307258506980843, 0.1491729864726037467878287,
        0.1420961093183820513292983, 0.1316886384491766268984945,
        0.1181945319615184173123774, 0.1019301198172404350367501,
        0.0832767415767047487247581, 0.0626720483341090635695065,
        0.0406014298003869413310400, 0.0176140071391521183118620
    ],
    32: [
        0.0070186100094700966004071, 0.0162743947309056706051706,
        0.0253920653092620594557526, 0.0342738629130214331026877,
        0.0428358980222266806568786, 0.0509980592623761761961632,
        0.0586840934785355471452836, 0.0658222227763618468376501,
        0.0723457941088485062253994, 0.0781938957870703064717409,
        0.0833119242269467552221991, 0.0876520930044038111427715,
        0.0911738786957638847128686, 0.0938443990808045656391802,
        0.0956387200792748594190820, 0.0965400885147278005667648,
        0.0965400885147278005667648, 0.0956387200792748594190820,
        0.0938443990808045656391802, 0.0911738786957638847128686,
        0.0876520930044038111427715, 0.0833119242269467552221991,
        0.0781938957870703064717409, 0.0723457941088485062253994,
        0.0658222227763618468376501, 0.0586840934785355471452836,
        0.0509980592623761761961632, 0.0428358980222266806568786,
        0.0342738629130214331026877, 0.0253920653092620594557526,
        0.0162743947309056706051706, 0.0070186100094700966004071
    ],
}

stieltjes_roots = {
    15: [
        -0.9914553711208126392069, -0.8648644233597690727897,
        -0.5860872354676911302941, -0.2077849550078984676007,
        0.2077849550078984676007, 0.5860872354676911302941,
        0.8648644233597690727897, 0.9914553711208126392069
    ],
    21: [
        -0.9956571630258080807355, -0.9301574913557082260012,
        -0.7808177265864168970637, -0.562757134668604683339,
        -0.294392862701460198131, 0, 0.2943928627014601981311,
        0.562757134668604683339, 0.7808177265864168970637,
        0.9301574913557082260012, 0.9956571630258080807355
    ],
    31: [
        -0.9980022986933970602852, -0.9677390756791391342574,
        -0.8972645323440819008825, -0.7904185014424659329677,
        -0.6509967412974169705337, -0.4850818636402396806937,
        -0.2991800071531688121668, -0.1011420669187174990271,
        0.1011420669187174990271, 0.2991800071531688121668,
        0.4850818636402396806937, 0.6509967412974169705337,
        0.7904185014424659329677, 0.8972645323440819008825,
        0.9677390756791391342574, 0.9980022986933970602852
    ],
}

# For each n kronrod_weights[n] consists of the weights for all Legendre roots
# concatenated with weights for Stieltjes roots.
kronrod_weights = {
    15: [
        0.0630920926299785532907, 0.1406532597155259187452,
        0.1903505780647854099133, 0.209482141084727828013,
        0.1903505780647854099133, 0.1406532597155259187452,
        0.0630920926299785532907, 0.0229353220105292249637,
        0.1047900103222501838399, 0.1690047266392679028266,
        0.2044329400752988924142, 0.2044329400752988924142,
        0.1690047266392679028266, 0.10479001032225018384,
        0.02293532201052922496373
    ],
    21: [
        0.0325581623079647274788, 0.075039674810919952767,
        0.1093871588022976418992, 0.134709217311473325928,
        0.1477391049013384913748, 0.1477391049013384913748,
        0.134709217311473325928, 0.109387158802297641899,
        0.075039674810919952767, 0.032558162307964727479,
        0.0116946388673718742781, 0.0547558965743519960314,
        0.093125454583697605535, 0.123491976262065851078,
        0.142775938577060080797, 0.149445554002916905665,
        0.1427759385770600807971, 0.123491976262065851078,
        0.093125454583697605535, 0.05475589657435199603138,
        0.0116946388673718742781
    ],
    31: [
        0.0150079473293161225384, 0.035346360791375846222,
        0.0534815246909280872653, 0.06985412131872825871,
        0.0830805028231330210383, 0.0931265981708253212255,
        0.0991735987217919593324, 0.101330007014791549017,
        0.0991735987217919593324, 0.093126598170825321225,
        0.083080502823133021038, 0.0698541213187282587095,
        0.0534815246909280872653, 0.035346360791375846222,
        0.015007947329316122538, 0.0053774798729233489878,
        0.025460847326715320187, 0.044589751324764876608,
        0.0620095678006706402851, 0.0768496807577203788944,
        0.0885644430562117706473, 0.0966427269836236785052,
        0.100769845523875595045, 0.100769845523875595045,
        0.096642726983623678505, 0.088564443056211770647,
        0.0768496807577203788944, 0.062009567800670640285,
        0.044589751324764876608, 0.0254608473267153201869,
        0.0053774798729233489878
    ]
}