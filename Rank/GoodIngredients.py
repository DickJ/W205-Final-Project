import pymongo
from pymongo import MongoClient
#conn=pymongo.MongoClient('mongodb://recipe:recipe@ds053370.mongolab.com:53370/recipemaker')
conn =pymongo.MongoClient()
db = conn.recipemaker
coll = db.ingredients
#brute force
coll.insert({'ingredient':'abalone'})
coll.insert({'ingredient':'absinthe'})
coll.insert({'ingredient':'achar'})
coll.insert({'ingredient':'ackee'})
coll.insert({'ingredient':'acorn'})
coll.insert({'ingredient':'adobo'})
coll.insert({'ingredient':'advieh'})
coll.insert({'ingredient':'agar'})
coll.insert({'ingredient':'aioli'})
coll.insert({'ingredient':'Ajowan'})
coll.insert({'ingredient':'ale'})
coll.insert({'ingredient':'alfalfa'})
coll.insert({'ingredient':'alfredo sauce'})
coll.insert({'ingredient':'Alitame'})
coll.insert({'ingredient':'alize liqueur'})
coll.insert({'ingredient':'alligator'})
coll.insert({'ingredient':'allspice'})
coll.insert({'ingredient':'almond'})
coll.insert({'ingredient':'alum'})
coll.insert({'ingredient':'amaranth'})
coll.insert({'ingredient':'amarena cherries'})
coll.insert({'ingredient':'amaretti'})
coll.insert({'ingredient':'amaretto'})
coll.insert({'ingredient':'amchoor powder'})
coll.insert({'ingredient':'amla'})
coll.insert({'ingredient':'ammonium bicarbonate'})
coll.insert({'ingredient':'anchov'})
coll.insert({'ingredient':'andouille'})
coll.insert({'ingredient':'angelica'})
coll.insert({'ingredient':'anise'})
coll.insert({'ingredient':'annatto seeds'})
coll.insert({'ingredient':'apple'})
coll.insert({'ingredient':'apricots'})
coll.insert({'ingredient':'aquavit'})
coll.insert({'ingredient':'arak'})
coll.insert({'ingredient':'arrowroot'})
coll.insert({'ingredient':'artichokes'})
coll.insert({'ingredient':'arugula'})
coll.insert({'ingredient':'asadero'})
coll.insert({'ingredient':'asafetida'})
coll.insert({'ingredient':'asiago cheese'})
coll.insert({'ingredient':'asparagus'})
coll.insert({'ingredient':'aspic'})
coll.insert({'ingredient':'avocados'})
coll.insert({'ingredient':'azuki beans'})
coll.insert({'ingredient':'baba'})
coll.insert({'ingredient':'babaco'})
coll.insert({'ingredient':'babka'})
coll.insert({'ingredient':'bacon'})
coll.insert({'ingredient':'bacon grease'})
coll.insert({'ingredient':'bagels'})
coll.insert({'ingredient':'bagna cauda'})
coll.insert({'ingredient':'bagoong'})
coll.insert({'ingredient':'baguette'})
coll.insert({'ingredient':'baharat'})
coll.insert({'ingredient':'baking powder'})
coll.insert({'ingredient':'baking soda'})
coll.insert({'ingredient':'baklava'})
coll.insert({'ingredient':'Balmain Bug'})
coll.insert({'ingredient':'bamboo shoots'})
coll.insert({'ingredient':'bananas'})
coll.insert({'ingredient':'bangers'})
coll.insert({'ingredient':'bannocks'})
coll.insert({'ingredient':'barbecue'})
coll.insert({'ingredient':'barberries'})
coll.insert({'ingredient':'bard'})
coll.insert({'ingredient':'barley'})
coll.insert({'ingredient':'baron'})
coll.insert({'ingredient':'basil'})
coll.insert({'ingredient':'bass'})
coll.insert({'ingredient':'bay leaves'})
coll.insert({'ingredient':'bean'})
coll.insert({'ingredient':'beat'})
coll.insert({'ingredient':'bechamel'})
coll.insert({'ingredient':'beef'})
coll.insert({'ingredient':'beer'})
coll.insert({'ingredient':'beets'})
coll.insert({'ingredient':'bel paese'})
coll.insert({'ingredient':'bento'})
coll.insert({'ingredient':'berbere'})
coll.insert({'ingredient':'berries'})
coll.insert({'ingredient':'beurre'})
coll.insert({'ingredient':'biltong'})
coll.insert({'ingredient':'biscuit mix'})
coll.insert({'ingredient':'bisque'})
coll.insert({'ingredient':'blackberries'})
coll.insert({'ingredient':'blanch'})
coll.insert({'ingredient':'blueberries'})
coll.insert({'ingredient':'boerewors'})
coll.insert({'ingredient':'boil'})
coll.insert({'ingredient':'bok choy'})
coll.insert({'ingredient':'borage'})
coll.insert({'ingredient':'borscht'})
coll.insert({'ingredient':'bottarga'})
coll.insert({'ingredient':'bouillon'})
coll.insert({'ingredient':'bouquet garni'})
coll.insert({'ingredient':'bourbon'})
coll.insert({'ingredient':'braai'})
coll.insert({'ingredient':'braise'})
coll.insert({'ingredient':'brandy'})
coll.insert({'ingredient':'breadcrumbs'})
coll.insert({'ingredient':'breadfruit'})
coll.insert({'ingredient':'bresaola'})
coll.insert({'ingredient':'broccoli'})
coll.insert({'ingredient':'broil'})
coll.insert({'ingredient':'broth'})
coll.insert({'ingredient':'brunoise'})
coll.insert({'ingredient':'bruschetta'})
coll.insert({'ingredient':'Brussels sprouts'})
coll.insert({'ingredient':'buckwheat'})
coll.insert({'ingredient':'buerre manie'})
coll.insert({'ingredient':'bulgur wheat'})
coll.insert({'ingredient':'butter'})
coll.insert({'ingredient':'buttermilk'})
coll.insert({'ingredient':'cabbage'})
coll.insert({'ingredient':'cacao'})
coll.insert({'ingredient':'cachaca'})
coll.insert({'ingredient':'cactus'})
coll.insert({'ingredient':'Caerphilly'})
coll.insert({'ingredient':'calabaza'})
coll.insert({'ingredient':'callaloo'})
coll.insert({'ingredient':'Calvados'})
coll.insert({'ingredient':'cannellini beans'})
coll.insert({'ingredient':'canola oil'})
coll.insert({'ingredient':'cantaloupes'})
coll.insert({'ingredient':'capers'})
coll.insert({'ingredient':'capsicums'})
coll.insert({'ingredient':'carambola'})
coll.insert({'ingredient':'caramelize'})
coll.insert({'ingredient':'caraway seeds'})
coll.insert({'ingredient':'carboy'})
coll.insert({'ingredient':'cardamom'})
coll.insert({'ingredient':'carob'})
coll.insert({'ingredient':'carrageen'})
coll.insert({'ingredient':'carrots'})
coll.insert({'ingredient':'cashew nut'})
coll.insert({'ingredient':'cassava'})
coll.insert({'ingredient':'Casserole'})
coll.insert({'ingredient':'catfish'})
coll.insert({'ingredient':'caul'})
coll.insert({'ingredient':'cauliflower'})
coll.insert({'ingredient':'caviar'})
coll.insert({'ingredient':'celeriac'})
coll.insert({'ingredient':'celery'})
coll.insert({'ingredient':'chai'})
coll.insert({'ingredient':'chambord'})
coll.insert({'ingredient':'chard'})
coll.insert({'ingredient':'chayote'})
coll.insert({'ingredient':'cheese'})
coll.insert({'ingredient':'cheesecloth'})
coll.insert({'ingredient':'chendol'})
coll.insert({'ingredient':'cherimoya'})
coll.insert({'ingredient':'cherries'})
coll.insert({'ingredient':'chervil'})
coll.insert({'ingredient':'chestnuts'})
coll.insert({'ingredient':'chickens'})
coll.insert({'ingredient':'chickpeas'})
coll.insert({'ingredient':'chicory'})
coll.insert({'ingredient':'chiffonade'})
coll.insert({'ingredient':'chile peppers'})
coll.insert({'ingredient':'chili powder'})
coll.insert({'ingredient':'chili sauce'})
coll.insert({'ingredient':'chipotle peppers'})
coll.insert({'ingredient':'chives'})
coll.insert({'ingredient':'chocolate'})
coll.insert({'ingredient':'chowder'})
coll.insert({'ingredient':'chutney'})
coll.insert({'ingredient':'cider'})
coll.insert({'ingredient':'cilantro'})
coll.insert({'ingredient':'cinnamon'})
coll.insert({'ingredient':'citron'})
coll.insert({'ingredient':'Citrus oils'})
coll.insert({'ingredient':'clafouti'})
coll.insert({'ingredient':'clams'})
coll.insert({'ingredient':'clarify'})
coll.insert({'ingredient':'cloves'})
coll.insert({'ingredient':'cocoa powder'})
coll.insert({'ingredient':'coconut'})
coll.insert({'ingredient':'cod'})
coll.insert({'ingredient':'coffee'})
coll.insert({'ingredient':'colby'})
coll.insert({'ingredient':'confit'})
coll.insert({'ingredient':'cookies'})
coll.insert({'ingredient':'cooking wine'})
coll.insert({'ingredient':'Cool Whip'})
coll.insert({'ingredient':'Copha'})
coll.insert({'ingredient':'coriander'})
coll.insert({'ingredient':'corn'})
coll.insert({'ingredient':'cornichons'})
coll.insert({'ingredient':'cornmeal'})
coll.insert({'ingredient':'cornstarch'})
coll.insert({'ingredient':'coulis'})
coll.insert({'ingredient':'couscous'})
coll.insert({'ingredient':'crabs'})
coll.insert({'ingredient':'craisins'})
coll.insert({'ingredient':'cranberries'})
coll.insert({'ingredient':'crayfish'})
coll.insert({'ingredient':'crostini'})
coll.insert({'ingredient':'croutons'})
coll.insert({'ingredient':'crozzled'})
coll.insert({'ingredient':'cucumbers'})
coll.insert({'ingredient':'cucuzza'})
coll.insert({'ingredient':'cumin'})
coll.insert({'ingredient':'curacao'})
coll.insert({'ingredient':'currants'})
coll.insert({'ingredient':'curry'})
coll.insert({'ingredient':'custard'})
coll.insert({'ingredient':'dash'})
coll.insert({'ingredient':'date'})
coll.insert({'ingredient':'deglaze'})
coll.insert({'ingredient':'demi-glace'})
coll.insert({'ingredient':'dhania-jeera powder'})
coll.insert({'ingredient':'dill'})
coll.insert({'ingredient':'dragees'})
coll.insert({'ingredient':'dried leeks'})
coll.insert({'ingredient':'dripping'})
coll.insert({'ingredient':'duck'})
coll.insert({'ingredient':'dumpling'})
coll.insert({'ingredient':'durian'})
coll.insert({'ingredient':'eclairs'})
coll.insert({'ingredient':'edam'})
coll.insert({'ingredient':'edamame'})
coll.insert({'ingredient':'eel'})
coll.insert({'ingredient':'eggplants'})
coll.insert({'ingredient':'egg'})
coll.insert({'ingredient':'Elderberries'})
coll.insert({'ingredient':'endive'})
coll.insert({'ingredient':'English muffins'})
coll.insert({'ingredient':'English mustard'})
coll.insert({'ingredient':'epazote'})
coll.insert({'ingredient':'erythritol'})
coll.insert({'ingredient':'escalopes'})
coll.insert({'ingredient':'falafel'})
coll.insert({'ingredient':'Falernum'})
coll.insert({'ingredient':'farina'})
coll.insert({'ingredient':'fava beans'})
coll.insert({'ingredient':'feijoa'})
coll.insert({'ingredient':'fennel'})
coll.insert({'ingredient':'fennel seeds'})
coll.insert({'ingredient':'fenugreek'})
coll.insert({'ingredient':'feta cheese'})
coll.insert({'ingredient':'figs'})
coll.insert({'ingredient':'finnan haddie'})
coll.insert({'ingredient':'fish'})
coll.insert({'ingredient':'five-spice powder'})
coll.insert({'ingredient':'flageolet'})
coll.insert({'ingredient':'flax seed'})
coll.insert({'ingredient':'flounder'})
coll.insert({'ingredient':'flour'})
coll.insert({'ingredient':'focaccia'})
coll.insert({'ingredient':'foie gras'})
coll.insert({'ingredient':'fond'})
coll.insert({'ingredient':'forcemeat'})
coll.insert({'ingredient':'frangipane'})
coll.insert({'ingredient':'french fries'})
coll.insert({'ingredient':'frisee'})
coll.insert({'ingredient':'fructose'})
coll.insert({'ingredient':'galangal'})
coll.insert({'ingredient':'ganache'})
coll.insert({'ingredient':'garlic'})
coll.insert({'ingredient':'geese'})
coll.insert({'ingredient':'gelatin'})
coll.insert({'ingredient':'ghee'})
coll.insert({'ingredient':'ginger'})
coll.insert({'ingredient':'ginkgo nut'})
coll.insert({'ingredient':'glace de viande'})
coll.insert({'ingredient':'Gloucester'})
coll.insert({'ingredient':'gluten'})
coll.insert({'ingredient':'Goji berry'})
coll.insert({'ingredient':'golden syrup'})
coll.insert({'ingredient':'gooseberries'})
coll.insert({'ingredient':'gorgonzola'})
coll.insert({'ingredient':'gouda'})
coll.insert({'ingredient':'graham crackers'})
coll.insert({'ingredient':'grains of paradise'})
coll.insert({'ingredient':'gram flour'})
coll.insert({'ingredient':'Grand Marnier'})
coll.insert({'ingredient':'granola'})
coll.insert({'ingredient':'grapefruits'})
coll.insert({'ingredient':'grapes'})
coll.insert({'ingredient':'grating cheese'})
coll.insert({'ingredient':'greens'})
coll.insert({'ingredient':'grits'})
coll.insert({'ingredient':'grouper'})
coll.insert({'ingredient':'Gruyere'})
coll.insert({'ingredient':'guanbana'})
coll.insert({'ingredient':'guavas'})
coll.insert({'ingredient':'gumbo'})
coll.insert({'ingredient':'habanero chilies'})
coll.insert({'ingredient':'haddock'})
coll.insert({'ingredient':'half-and-half'})
coll.insert({'ingredient':'halibut'})
coll.insert({'ingredient':'ham'})
coll.insert({'ingredient':'hamburger'})
coll.insert({'ingredient':'hard cheese'})
coll.insert({'ingredient':'Harissa'})
coll.insert({'ingredient':'hash browns'})
coll.insert({'ingredient':'Havarti'})
coll.insert({'ingredient':'Hawaij'})
coll.insert({'ingredient':'hazelnuts'})
coll.insert({'ingredient':'herbs'})
coll.insert({'ingredient':'herbsaint'})
coll.insert({'ingredient':'herring'})
coll.insert({'ingredient':'hoisin sauce'})
coll.insert({'ingredient':'hoja santa'})
coll.insert({'ingredient':'hoki'})
coll.insert({'ingredient':'hominy'})
coll.insert({'ingredient':'honey'})
coll.insert({'ingredient':'honeydew melons'})
coll.insert({'ingredient':'horseradish'})
coll.insert({'ingredient':'hot sauce'})
coll.insert({'ingredient':'huckleberries'})
coll.insert({'ingredient':'hundred-year eggs'})
coll.insert({'ingredient':'Hungarian wax chile'})
coll.insert({'ingredient':'hyssop'})
coll.insert({'ingredient':'ice cream'})
coll.insert({'ingredient':'ice wine'})
coll.insert({'ingredient':'icing sugar'})
coll.insert({'ingredient':'Indian pudding'})
coll.insert({'ingredient':'infusion'})
coll.insert({'ingredient':'insalata'})
coll.insert({'ingredient':'invert sugar'})
coll.insert({'ingredient':'Irish coffee'})
coll.insert({'ingredient':'Irish cream liqueur'})
coll.insert({'ingredient':'Irish mist'})
coll.insert({'ingredient':'isinglass'})
coll.insert({'ingredient':'jaggery'})
coll.insert({'ingredient':'jambalaya'})
coll.insert({'ingredient':'jamon serrano'})
coll.insert({'ingredient':'jamun'})
coll.insert({'ingredient':'jelly'})
coll.insert({'ingredient':'jicama'})
coll.insert({'ingredient':'joint'})
coll.insert({'ingredient':'jowl'})
coll.insert({'ingredient':'Kabsa Spice Mix'})
coll.insert({'ingredient':'kaffir lime'})
coll.insert({'ingredient':'Kahlua'})
coll.insert({'ingredient':'kalamata olives'})
coll.insert({'ingredient':'kale'})
coll.insert({'ingredient':'kamaboko'})
coll.insert({'ingredient':'kasha'})
coll.insert({'ingredient':'kashk'})
coll.insert({'ingredient':'ketchup'})
coll.insert({'ingredient':'ketjap manis'})
coll.insert({'ingredient':'kewra'})
coll.insert({'ingredient':'Khus Essence'})
coll.insert({'ingredient':'kidney beans'})
coll.insert({'ingredient':'kielbasa'})
coll.insert({'ingredient':'kirsch'})
coll.insert({'ingredient':'kiwi fruit'})
coll.insert({'ingredient':'kohlrabi'})
coll.insert({'ingredient':'konfyt'})
coll.insert({'ingredient':'kosher'})
coll.insert({'ingredient':'kudzu'})
coll.insert({'ingredient':'kugel'})
coll.insert({'ingredient':'kumquats'})
coll.insert({'ingredient':'ladyfingers'})
coll.insert({'ingredient':'lamb'})
coll.insert({'ingredient':'Lamprey'})
coll.insert({'ingredient':'Lancashire cheese'})
coll.insert({'ingredient':'lardons'})
coll.insert({'ingredient':'lavender'})
coll.insert({'ingredient':'lecithin'})
coll.insert({'ingredient':'leeks'})
coll.insert({'ingredient':'Lefse'})
coll.insert({'ingredient':'lemon'})
coll.insert({'ingredient':'lentil'})
coll.insert({'ingredient':'lettuce'})
coll.insert({'ingredient':'lima bean'})
coll.insert({'ingredient':'lime'})
coll.insert({'ingredient':'lingcod'})
coll.insert({'ingredient':'litchi'})
coll.insert({'ingredient':'liver'})
coll.insert({'ingredient':'lobster'})
coll.insert({'ingredient':'longan'})
coll.insert({'ingredient':'loquat'})
coll.insert({'ingredient':'lotus'})
coll.insert({'ingredient':'lovage'})
coll.insert({'ingredient':'lumpia wrapper'})
coll.insert({'ingredient':'macaroni'})
coll.insert({'ingredient':'mace'})
coll.insert({'ingredient':'mackerel'})
coll.insert({'ingredient':'Madeira'})
coll.insert({'ingredient':'mahi mahi'})
coll.insert({'ingredient':'mahleb'})
coll.insert({'ingredient':'Mandarin oranges'})
coll.insert({'ingredient':'mange-tout'})
coll.insert({'ingredient':'mangoe'})
coll.insert({'ingredient':'mangosteen'})
coll.insert({'ingredient':'maple syrup'})
coll.insert({'ingredient':'maraschino cherries'})
coll.insert({'ingredient':'margarine'})
coll.insert({'ingredient':'marjoram'})
coll.insert({'ingredient':'marmalade'})
coll.insert({'ingredient':'Marsala'})
coll.insert({'ingredient':'marshmallows'})
coll.insert({'ingredient':'marula'})
coll.insert({'ingredient':'marzipan'})
coll.insert({'ingredient':'masa harina'})
coll.insert({'ingredient':'masala'})
coll.insert({'ingredient':'masarepa'})
coll.insert({'ingredient':'mascarpone'})
coll.insert({'ingredient':'matignon'})
coll.insert({'ingredient':'matzo meal'})
coll.insert({'ingredient':'mayonnaise'})
coll.insert({'ingredient':'melons'})
coll.insert({'ingredient':'meringue powder'})
coll.insert({'ingredient':'mesclun'})
coll.insert({'ingredient':'mettwursts'})
coll.insert({'ingredient':'milk'})
coll.insert({'ingredient':'mimolette cheese'})
coll.insert({'ingredient':'mince'})
coll.insert({'ingredient':'Mini Babybel Light'})
coll.insert({'ingredient':'mint'})
coll.insert({'ingredient':'Miracle Whip dressing'})
coll.insert({'ingredient':'mirepoix'})
coll.insert({'ingredient':'miso'})
coll.insert({'ingredient':'mixed spice'})
coll.insert({'ingredient':'mizuna'})
coll.insert({'ingredient':'Moambé Sauce'})
coll.insert({'ingredient':'molasses'})
coll.insert({'ingredient':'monkfish'})
coll.insert({'ingredient':'monosodium glutamate'})
coll.insert({'ingredient':'moo shu wrappers'})
coll.insert({'ingredient':'morels'})
coll.insert({'ingredient':'Moreton Bay Bug'})
coll.insert({'ingredient':'moringa'})
coll.insert({'ingredient':'mortadella'})
coll.insert({'ingredient':'mostaccioli'})
coll.insert({'ingredient':'mozzarella'})
coll.insert({'ingredient':'muddle'})
coll.insert({'ingredient':'mugwort'})
coll.insert({'ingredient':'mung beans'})
coll.insert({'ingredient':'Muscadine grape'})
coll.insert({'ingredient':'muscovado sugar'})
coll.insert({'ingredient':'Muscovy duck'})
coll.insert({'ingredient':'mushrooms'})
coll.insert({'ingredient':'muskmelons'})
coll.insert({'ingredient':'mussels'})
coll.insert({'ingredient':'mustard'})
coll.insert({'ingredient':'nasturtium'})
coll.insert({'ingredient':'nectarine'})
coll.insert({'ingredient':'nigella seed'})
coll.insert({'ingredient':'nopales'})
coll.insert({'ingredient':'nori'})
coll.insert({'ingredient':'OAMC'})
coll.insert({'ingredient':'oatmeal'})
coll.insert({'ingredient':'octopus'})
coll.insert({'ingredient':'offal'})
coll.insert({'ingredient':'okra'})
coll.insert({'ingredient':'olive'})
coll.insert({'ingredient':'onion'})
coll.insert({'ingredient':'orange'})
coll.insert({'ingredient':'oregano'})
coll.insert({'ingredient':'orgeat syrup'})
coll.insert({'ingredient':'oyster sauce'})
coll.insert({'ingredient':'palm'})
coll.insert({'ingredient':'pancetta'})
coll.insert({'ingredient':'panir'})
coll.insert({'ingredient':'panko'})
coll.insert({'ingredient':'panna cotta'})
coll.insert({'ingredient':'papayas'})
coll.insert({'ingredient':'paprika'})
coll.insert({'ingredient':'parboil'})
coll.insert({'ingredient':'parsley'})
coll.insert({'ingredient':'parsnips'})
coll.insert({'ingredient':'passion fruit'})
coll.insert({'ingredient':'pasta'})
coll.insert({'ingredient':'pastis'})
coll.insert({'ingredient':'paysanne'})
coll.insert({'ingredient':'peach'})
coll.insert({'ingredient':'peanut'})
coll.insert({'ingredient':'pear'})
coll.insert({'ingredient':'pea'})
coll.insert({'ingredient':'pecan'})
coll.insert({'ingredient':'Pelargonium citronellum'})
coll.insert({'ingredient':'pepper'})
coll.insert({'ingredient':'perch'})
coll.insert({'ingredient':'Periwinkle'})
coll.insert({'ingredient':'persimmon'})
coll.insert({'ingredient':'pesto'})
coll.insert({'ingredient':'pheasant'})
coll.insert({'ingredient':'phyllo dough'})
coll.insert({'ingredient':'pickle'})
coll.insert({'ingredient':'pico de gallo'})
coll.insert({'ingredient':'pierogie'})
coll.insert({'ingredient':'pike'})
coll.insert({'ingredient':'piloncillo'})
coll.insert({'ingredient':'pimiento'})
coll.insert({'ingredient':'pinch'})
coll.insert({'ingredient':'pineapple'})
coll.insert({'ingredient':'pistachio'})
coll.insert({'ingredient':'plantain'})
coll.insert({'ingredient':'plumcot'})
coll.insert({'ingredient':'plum'})
coll.insert({'ingredient':'polenta'})
coll.insert({'ingredient':'pomegranate'})
coll.insert({'ingredient':'pomelo'})
coll.insert({'ingredient':'pompano'})
coll.insert({'ingredient':'ponzu'})
coll.insert({'ingredient':'poppy seed'})
coll.insert({'ingredient':'porcini'})
coll.insert({'ingredient':'pork'})
coll.insert({'ingredient':'portabella'})
coll.insert({'ingredient':'potato'})
coll.insert({'ingredient':'poussin'})
coll.insert({'ingredient':'prawn'})
coll.insert({'ingredient':'preserve'})
coll.insert({'ingredient':'Prosciuttini'})
coll.insert({'ingredient':'prosciutto'})
coll.insert({'ingredient':'provel rope cheese'})
coll.insert({'ingredient':'provolone'})
coll.insert({'ingredient':'prune'})
coll.insert({'ingredient':'pulse'})
coll.insert({'ingredient':'pumpkin'})
coll.insert({'ingredient':'purslane'})
coll.insert({'ingredient':'quail'})
coll.insert({'ingredient':'quark'})
coll.insert({'ingredient':'quenelle'})
coll.insert({'ingredient':'quesadilla'})
coll.insert({'ingredient':'queso'})
coll.insert({'ingredient':'quetsch'})
coll.insert({'ingredient':'quince'})
coll.insert({'ingredient':'quinoa'})
coll.insert({'ingredient':'quorn'})
coll.insert({'ingredient':'rabbit'})
coll.insert({'ingredient':'radiatore'})
coll.insert({'ingredient':'radicchio'})
coll.insert({'ingredient':'radishes'})
coll.insert({'ingredient':'raisins'})
coll.insert({'ingredient':'rambutan'})
coll.insert({'ingredient':'ramps'})
coll.insert({'ingredient':'ras el hanout'})
coll.insert({'ingredient':'raspberrie'})
coll.insert({'ingredient':'Recado rojo'})
coll.insert({'ingredient':'recaito'})
coll.insert({'ingredient':'remoulade'})
coll.insert({'ingredient':'rhubarb'})
coll.insert({'ingredient':'rice'})
coll.insert({'ingredient':'romaine lettuce'})
coll.insert({'ingredient':'Rookworst'})
coll.insert({'ingredient':'rosemary'})
coll.insert({'ingredient':'roux'})
coll.insert({'ingredient':'rum'})
coll.insert({'ingredient':'rusks'})
coll.insert({'ingredient':'saffron'})
coll.insert({'ingredient':'sage'})
coll.insert({'ingredient':'sago'})
coll.insert({'ingredient':'salmon'})
coll.insert({'ingredient':'salsa'})
coll.insert({'ingredient':'salsify'})
coll.insert({'ingredient':'salt'})
coll.insert({'ingredient':'sambal'})
coll.insert({'ingredient':'Sand Dab'})
coll.insert({'ingredient':'sardine'})
coll.insert({'ingredient':'satay'})
coll.insert({'ingredient':'sauerkraut'})
coll.insert({'ingredient':'Saunf'})
coll.insert({'ingredient':'sausage'})
coll.insert({'ingredient':'saute'})
coll.insert({'ingredient':'savory'})
coll.insert({'ingredient':'sazon'})
coll.insert({'ingredient':'scald'})
coll.insert({'ingredient':'scallop'})
coll.insert({'ingredient':'scaloppine'})
coll.insert({'ingredient':'scrapple'})
coll.insert({'ingredient':'sear'})
coll.insert({'ingredient':'seed'})
coll.insert({'ingredient':'seitan'})
coll.insert({'ingredient':'semolina'})
coll.insert({'ingredient':'sesame seed'})
coll.insert({'ingredient':'seville orange'})
coll.insert({'ingredient':'shallots'})
coll.insert({'ingredient':'sherry'})
coll.insert({'ingredient':'shitakes'})
coll.insert({'ingredient':'shortening'})
coll.insert({'ingredient':'shrimp'})
coll.insert({'ingredient':'shrimp paste'})
coll.insert({'ingredient':'Shropshire Blue'})
coll.insert({'ingredient':'simmer'})
coll.insert({'ingredient':'Slipper Lobster'})
coll.insert({'ingredient':'smelt'})
coll.insert({'ingredient':'snapper'})
coll.insert({'ingredient':'snoek'})
coll.insert({'ingredient':'soba'})
coll.insert({'ingredient':'soda crackers'})
coll.insert({'ingredient':'sodium citrate'})
coll.insert({'ingredient':'sole'})
coll.insert({'ingredient':'somen'})
coll.insert({'ingredient':'sorghum'})
coll.insert({'ingredient':'sorrel'})
coll.insert({'ingredient':'souffle'})
coll.insert({'ingredient':'sour cream'})
coll.insert({'ingredient':'soy sauce'})
coll.insert({'ingredient':'soybeans'})
coll.insert({'ingredient':'soymilk'})
coll.insert({'ingredient':'spaetzle'})
coll.insert({'ingredient':'spatchcock'})
coll.insert({'ingredient':'spearmint'})
coll.insert({'ingredient':'spinach'})
coll.insert({'ingredient':'squash'})
coll.insert({'ingredient':'squid'})
coll.insert({'ingredient':'star anise'})
coll.insert({'ingredient':'steak'})
coll.insert({'ingredient':'steam'})
coll.insert({'ingredient':'stevia'})
coll.insert({'ingredient':'Stilton'})
coll.insert({'ingredient':'strawberr'})
coll.insert({'ingredient':'stuffings'})
coll.insert({'ingredient':'sturgeon'})
coll.insert({'ingredient':'sucanat'})
coll.insert({'ingredient':'succotash'})
coll.insert({'ingredient':'suet'})
coll.insert({'ingredient':'sugar'})
coll.insert({'ingredient':'sultana'})
coll.insert({'ingredient':'sumac'})
coll.insert({'ingredient':'sushi'})
coll.insert({'ingredient':'sweetbreads'})
coll.insert({'ingredient':'swiss cheese'})
coll.insert({'ingredient':'swordfish'})
coll.insert({'ingredient':'Szechuan peppercorn'})
coll.insert({'ingredient':'Tabasco sauce'})
coll.insert({'ingredient':'tagine'})
coll.insert({'ingredient':'tahini'})
coll.insert({'ingredient':'tamarillo'})
coll.insert({'ingredient':'tamarind'})
coll.insert({'ingredient':'tandoori paste'})
coll.insert({'ingredient':'tapioca'})
coll.insert({'ingredient':'tarragon'})
coll.insert({'ingredient':'tartar sauce'})
coll.insert({'ingredient':'tasso'})
coll.insert({'ingredient':'tatsoi'})
coll.insert({'ingredient':'tea'})
coll.insert({'ingredient':'teff'})
coll.insert({'ingredient':'tempeh'})
coll.insert({'ingredient':'terrapins'})
coll.insert({'ingredient':'thyme'})
coll.insert({'ingredient':'tofu'})
coll.insert({'ingredient':'togarashi'})
coll.insert({'ingredient':'tomato'})
coll.insert({'ingredient':'tortilla'})
coll.insert({'ingredient':'tripe'})
coll.insert({'ingredient':'trout'})
coll.insert({'ingredient':'truffle'})
coll.insert({'ingredient':'tuna'})
coll.insert({'ingredient':'turkey'})
coll.insert({'ingredient':'turmeric'})
coll.insert({'ingredient':'turnip'})
coll.insert({'ingredient':'udo'})
coll.insert({'ingredient':'umeboshi'})
coll.insert({'ingredient':'urad dal'})
coll.insert({'ingredient':'vanilla'})
coll.insert({'ingredient':'veal'})
coll.insert({'ingredient':'vegemite'})
coll.insert({'ingredient':'veloute'})
coll.insert({'ingredient':'Velveeta'})
coll.insert({'ingredient':'venison'})
coll.insert({'ingredient':'vermouth'})
coll.insert({'ingredient':'vincotto'})
coll.insert({'ingredient':'vinegar'})
coll.insert({'ingredient':'vital wheat gluten'})
coll.insert({'ingredient':'wakame seaweed salad'})
coll.insert({'ingredient':'walnut'})
coll.insert({'ingredient':'wasabi'})
coll.insert({'ingredient':'washed-rind cheese'})
coll.insert({'ingredient':'water'})
coll.insert({'ingredient':'water bath'})
coll.insert({'ingredient':'water chestnut'})
coll.insert({'ingredient':'waterblommetji'})
coll.insert({'ingredient':'watercress'})
coll.insert({'ingredient':'watermelon'})
coll.insert({'ingredient':'wattleseed'})
coll.insert({'ingredient':'Weetabix'})
coll.insert({'ingredient':'weisswurst'})
coll.insert({'ingredient':'Welsh rarebit'})
coll.insert({'ingredient':'whelk'})
coll.insert({'ingredient':'wine'})
coll.insert({'ingredient':'won ton skin'})
coll.insert({'ingredient':'woodruff'})
coll.insert({'ingredient':'Worcestershire sauce'})
coll.insert({'ingredient':'yeast'})
coll.insert({'ingredient':'yogurt'})
coll.insert({'ingredient':'yuzu kosho'})
coll.insert({'ingredient':'zabaglione'})
coll.insert({'ingredient':'zest'})
