#
# model_info={
#     'resnet34' :  {
#         'class' : "resnet",
#         'resnet_blocks' :  [3,4,6,3]
#     },
#     'resnet110' : {
#             'class' : "resnet",
#             'resnet_blocks' :  [3,8,40,3]
#         },
#     'resnet34w' : {
#             'class' : "resnet_w",
#             'resnet_blocks' :  [3,4,6,3]
#         },
#     'resnet110w':{
#         'class' : "resnet_w",
#         'resnet_blocks' :  [3,8,40,3]
#     },
#     'plain34':{
#             'class' : "plain",
#             'plainnet_blocks' :  [6,8,12,6]
#         },
#     'plain110':{
#             'class' : "plain",
#             'plainnet_blocks' :  [6,16,80,6]
#         }
#
# }


user_def_conv_idx = {
    'resnet34_1' : [  [
                        [[3, 6, 12, 15, 21, 24]],
                        [[30, 33, 39, 42, 48, 51, 57, 60]],
                        [[66, 69, 75, 78, 84, 87],
                            [93, 96, 102, 105, 111, 114]],
                        [[120, 123, 129, 132, 138, 141]]
                        ] ,
                        [
                            [[[[9], [3, 6]], [[18], [12, 15]], [[27], [21, 24]]]],
                            [[[[36], [30, 33]], [[45], [39, 42]], [[54], [48, 51]], [[63], [57, 60]]]],
                            [   [[[72], [66, 69]], [[81], [75, 78]], [[90], [84, 87]]],
                                [[[99], [93, 96]], [[108], [102, 105]], [[117], [111, 114]]]
                            ],
                            [[[[126], [120, 123]], [[135], [129, 132]], [[144], [138, 141]]]]
                        ]
                    ],
    'resnet110_1' : [   [
                            [[3, 6, 12, 15, 21, 24]],
                            [[30, 33, 39, 42, 48, 51, 57,  60], [66, 69, 75, 78, 84, 87, 93, 96]],
                            [[102, 105, 111, 114, 120, 123, 129, 132], [138, 141, 147, 150, 156, 159, 165, 168], [174, 177, 183, 186,
                              192, 195, 201, 204], [210, 213, 219, 222, 228, 231, 237, 240], [246, 249, 255, 258, 264, 267, 273, 276], [
                              282, 285, 291, 294, 300, 303], [309, 312, 318, 321, 327, 330, 336, 339], [345, 348, 354, 357, 363, 366,
                              372, 375], [381, 384, 390, 393, 399, 402, 408, 411], [417, 420, 426, 429, 435, 438, 444, 447, 453, 456]],
                            [[462, 465, 471, 474, 480, 483]]
                        ],
                        [
                            [[[[9], [3, 6]], [[18], [12, 15]], [[27], [21, 24]]]],
                            [   [[[36], [30, 33]], [[45], [39, 42]], [[54], [48, 51]], [[63], [57, 60]]],
                                [[[72], [66, 69]], [[81], [75, 78]], [[90], [84, 87]], [[99], [93, 96]]]
                            ],
                            [   [[[108], [102, 105]], [[117], [111, 114]], [[126], [120, 123]], [[135], [129, 132]] ],
                                [[[144], [138, 141]], [[153], [147, 150]], [[162], [156, 159]], [[171], [165, 168]]],
                                [[[180], [174, 177]], [[189], [183, 186]], [[198], [192, 195]], [[207], [201, 204]]],
                                [[[216], [210, 213]], [[225], [219, 222]], [[234], [228, 231]], [[243], [237, 240]]],
                                [[[252], [246, 249]], [[261], [255, 258]], [[270], [264, 267]], [[279], [273, 276]]],
                                [[[288], [282, 285]], [[297], [291, 294]], [[306], [300, 303]], [[315], [309, 312]]],
                                [[[324], [318, 321]], [[333], [327, 330]], [[342], [336, 339]], [[351], [345, 348]]],
                                [[[360], [354, 357]], [[369], [363, 366]], [[378], [372, 375]], [[387], [381, 384]]],
                                [[[396], [390, 393]], [[405], [399, 402]], [[414], [408, 411]], [[423], [417, 420]]],
                                [[[432], [426, 429]], [[441], [435, 438]], [[450], [444, 447]], [[459], [453, 456]]]
                            ],
                             [[[[468], [462, 465]], [[477], [471, 474]], [[486], [480, 483]]]]
                        ]
                    ]
}


