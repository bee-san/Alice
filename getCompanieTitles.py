from bs4 import BeautifulSoup
import requests

# Open URL, read HTML, and find title
titles = """19 Entertainment – talent company founded by Simon Fuller and "named after Paul Hardcastle's single 19, the first No. 1 Fuller had a hand in", according to TV Guide After selling 19 Entertainment to CKX, Inc, Fuller founded XIX Entertainment, which is 19 in Roman numerals.
20th Century Fox – film studio; formed in 1935 through the merger of William Fox's Fox Film, and Twentieth Century Pictures.
21st Century Fox – media company formed by spinning off News Corporation's TV and movie properties in 2013. It owns 20th Century Fox, the Fox Broadcasting Company, Fox News, Star TV and others.
23andMe – using the 23 pairs of chromosomes that make up each person's genome, the company helps individuals make sense of their own genome.
27b/6 – apartment where George Orwell wrote the novel Nineteen Eighty-Four was number 27B on level 6.
37signals – web development company; named for the 37 radiotelescope signals identified by astronomer Paul Horowitz as potential messages from extraterrestrial intelligence. In 2014, the company renamed itself Basecamp, after its main product.
3Com – network technology producer; the three coms are computer, communication, and compatibility.
3dfx Interactive – 3d and fx, standing for "three-dimensional effects".
3M – from the company's original name, Minnesota Mining and Manufacturing Company.
7-Eleven – convenience stores; renamed from "Tote'm" in 1946 to reflect their newly extended hours, 7:00 am until 11:00 pm.
A
A&M Records – named after founders Herb Alpert and Jerry Moss
A&P – from Atlantic & Pacific in Great Atlantic and Pacific Tea Company, a U.S.-based supermarket chain
A&W Root Beer – named after founders Roy Allen and Frank Wright
A. Le Coq – named after the founder Albert von Le Coq.
Abba Seafood – from Aktiebolaget Bröderna Ameln, meaning "Ameln brothers limited company".
ABC – American Broadcasting Company
Abloy – derived from Aktiebolag Låsfabriken Lukkotehdas Osakeyhtiö, which means "lock factory limited company" in both Swedish and Finnish
ABN AMRO – in the 1960s, the Nederlandsche Handel-Maatschappij (Dutch Trading Society; 1824) and De Twentsche Bank merged to form the Algemene Bank Nederland (ABN; General Bank of the Netherlands); in 1966, the Amsterdamsche Bank and the Rotterdamsche Bank merged to form the Amro Bank; in 1991, ABN and Amro Bank merged to form ABN AMRO.
Accenture – from "Accent on the future". The name Accenture was proposed by a company employee in Norway as part of an internal name finding process (BrandStorming). Before 1 January 2001, the company was called Andersen Consulting.
Acer – born as Multitech International in 1976, the company changed its name to Acer in 1987; the Latin word for “sharp, acute, able and facile”
Adecco – named from the merger of Swiss staffing company Adia with French staffing company Ecco
Adidas – from the name of the founder Adolf (Adi) Dassler. Adolf and his brother Rudolf Dassler split the original company, Gebrüder Dassler Schuhfabrik (Dassler Brothers Shoe Factory), with Rudolf founding Puma.
Adobe Systems – from the Adobe Creek that ran behind the house of co-founder John Warnock
Aflac – initialism for the company's previous name of American Family Life Assurance Company of Columbus (which remains the legal name of Aflac's underwriting subsidiary).
Ahlstrom – named after founder Antti Ahlström
Ahold – holding company of Albert Heijn and other supermarkets. For its 100th anniversary in 1987, Ahold was granted the title of Koninklijke ("Royal" in Dutch) by the Monarchy of the Netherlands, changing its name to Koninklijke Ahold (Royal Ahold).
Akai – named for its founder, Masukichi Akai
Akamai – from the Hawaiian word akamai meaning smart or clever; the company defines it as "intelligent, clever and cool"
AKG Acoustics – from the company’s original name, Akustische und Kino-Geräte (Acoustic and Cinema Equipment)
AKZO – named from the 1969 merger of Algemene Kunstzijde Unie (AKU) and Koninklijke Zout Organon (KZO)
Alcatel-Lucent – Alcatel was named from Alsacienne de Constructions Atomiques, de Télécommunications et d'Électronique. It took over Lucent Technologies (below) in 2006.
Alcoa – Aluminum Company of America
Aldi – portmanteau of Albrecht (name of the founders) and discount
Alfa Romeo – company was originally known as ALFA, an acronym for Anonima Lombarda Fabbrica Automobili. When Nicola Romeo bought ALFA in 1915, his surname was appended.
Alltel – from original company name Allied Telephone Company
Alps Electric/Alpine Electronics – Katsutaro Kataoka founded Kataoka Electronics in a suburb of Tokyo in 1947. A subsidiary was established in the province of Tohoku, also known as the Tohoku Alps, as Tohoku Alps Co. Ltd. When Kataoka was seeking investment during the 1960s, he found that foreigners had difficulty pronouncing "Kataoka," and renamed his firm Alps Electric. Alpine Electronics was originally named Alps-Motorola as a joint venture in the Japanese car audio market and the Alpine name was adopted after Motorola divested its stake in 1978.
Alstom – set up as Alsthom in 1928 by Société Alsacienne de Constructions Mécaniques and Compagnie Française Thomson-Houston, it changed the spelling to Alstom in 1997.
AltaVista – Spanish for "high view"
Alza – from the name of the founder Alex Zaffaroni
Amazon.com – founder Jeff Bezos renamed the company "Amazon" (from the earlier name of Cadabra.com) after the world's most voluminous river, the Amazon. He saw the potential for a larger volume of sales in an online (as opposed to a bricks and mortar) bookstore. (Alternative: Amazon was chosen to cash in on the popularity of Yahoo, which listed entries alphabetically.)
AmBev – American Beverage Company, the largest Brazilian beverage company and fourth in the world. In 2004 it merged with Interbrew to create InBev, which in turn purchased Anheuser-Busch in 2008 to form Anheuser-Busch InBev.
AMC Theatres – American Multi-Cinema: the company pioneered multi-screen cinemas
AMD – Advanced Micro Devices
Amdahl Corporation – American mainframe computer company named after its founder, Dr. Gene Amdahl, formerly of IBM. It was taken over by Fujitsu in 1997.
Amiga Corporation – original developers of the 16-bit Amiga computer chose the name, which means a 'female friend' in Spanish and Portuguese, because it sounded friendly, and because it came before rivals (Apple Inc. and Atari) alphabetically.
AMKOR – American Korea
Amoco – American Oil Company, now part of BP
Amstrad – Amstrad Consumer Electronics plc was founded by Lord Alan Michael Sugar in the UK. The name is a contraction of Alan Michael Sugar Trading.
Anheuser-Busch InBev – formed by the 2008 purchase of Anheuser-Busch by InBev. Anheuser-Busch was named for the company's original founder, Eberhard Anheuser, and his later partner Adolphus Busch.
AOL – from America Online. The company was founded in 1983 as Quantum Computer Services.
Apache – according to the project's 1997 FAQ: "The Apache group was formed around a number of people who provided patch files that had been written for NCSA httpd 1.3. The result after combining them was A PAtCHy server."
Apple – for the favorite fruit of co-founder Steve Jobs and/or for the time he worked at an apple orchard, and to distance itself from the cold, unapproachable, complicated imagery created by other computer companies at the time – which had names such as IBM, DEC, and Cincom
Apricot Computers – early UK-based microcomputer company founded by ACT (Applied Computer Techniques), a business software and services supplier. The company wanted a "fruity" name (Apple and Acorn were popular brands) that included the letters A, C and T. Apricot fit the bill.
Arby's – enunciation of the initials of its founders, the Raffel Brothers. The partners wanted to use the name Big Tex, but were unsuccessful in negotiating with the Akron businessman who was already using the name. So, Forrest said, "We came up with Arby's, which stands for R.B., the initials of Raffel Brothers, although I guess customers might think the initials stand for roast beef."
Arcelor – created in 2001 by a merger of Arbed (Luxembourg), Aceralia (Spain) and Usinor (France) with the ambition of becoming a major player in the steel industry.
Arcor – Arroyito, Córdoba, the city where it was founded.
Areva – named from the region of Ávila in northern Spain, location of the Arevalo abbey. Arevalo was shorted to AREVA.
Aricent – communications software company name created in 2006 by combining two words "arise" and "ascent".
Arm & Hammer – based on the arm and hammer of Vulcan, the Roman god of fire and metalworking. It was previously the logo of the Vulcan Spice Mills in Brooklyn. When James Church, the son of Church & Dwight founder Austin Church, came to Church and Dwight from Vulcan Spice Mills, he brought the logo with him.
ARM Limited – named after the microprocessor developed by small UK company Acorn as a successor to the 6502 used in its BBC Microcomputer. ARM originally stood for Acorn Risc Machine. When the company was spun off with backing from Apple and VTI, this was changed to Advanced Risc Machines.
ARP – company that made analog synthesizers in the 1970s, named after founder Alan Robert Pearlman
Artis – zoo in Amsterdam; named from the Latin phrase Natura Artis Magistra, or "Nature is Art's Teacher"
Asda – Asda Stores Limited was founded as Associated Dairies & Farm Stores Ltd in 1949. However, the formation of the Asda name occurred in 1965 with the merger of the Asquith chain of three supermarkets and Associated Dairies; it is an abbreviation of Asquith and Dairies, a large UK supermarket chain that is now a subsidiary of Walmart.
ASICS – acronym for Anima Sana In Corpore Sano, which, translated from Latin, means "Healthy soul in a healthy body". Originally the citation is mens sana in corpore sano, but MSICS does not sound as good.
Ask.com – search engine formerly named after Jeeves, the gentleman's gentleman (valet, not butler) in P. G. Wodehouse's series of books. Ask Jeeves was shortened to Ask in 2006.
Aston Martin – from the "Aston Hill" races (near Aston Clinton) where the company was founded, and the surname of Lionel Martin, the company's founder.
Asus – named after Pegasus, the winged horse of Greek mythology. The first three letters of the word were dropped to get a high position in alphabetical listings. An Asus company named Pegatron, using the spare letters, was spun off in 2008.
AT&T – American Telephone and Telegraph Corporation officially changed its name to AT&T in the 1990s.
Atari – named from the board game Go. "Atari" is a Japanese word to describe a position where an opponent's stones are in danger of being captured. It is similar, though not identical, to "check" in chess. The original games company was American but wanted a Japanese-sounding name.
ATI Technologies – founded in Canada as Array Technology Inc. and taken over by AMD in 2006.
ATS – Auto Technik Spezialerzeugnisse, a German company producing light alloy wheels and motor parts, which ran its own Formula 1 racing team in the late 1970s and early 1980s.
Audi – Latin translation of the German name "Horch". The founder August Horch left the company after five years, but still wanted to manufacture cars. Since the original "Horch" company was still there, he called his new company Audi, the Latin form of his last name. In English it is "hark".
B
B&H Photo Video – named after Blimie Schreiber and her husband, company founder Herman Schreiber
B&Q – from the initials of its founders, Richard Block and David Quayle
Babolat – racquet sports (tennis, badminton, squash) equipment company named after its founder, Pierre Babolat
Bahco – from the name B.A. Hjort & Company. Founder Berndt August Hjort signed a deal to distribute the tools of inventor Johan Petter Johansson.
Bakkavör – from the street in a Reykjavík suburb where the founders grew up
Bally – originally Lion Manufacturing, the company changed its name to Bally after the success of its first popular pinball machine, Ballyhoo.
Banesto – from Banco Español de Crédito (Spanish Credit Bank)
Bang & Olufsen – from the names of its founders, Peter Bang and Svend Olufsen, who met at a school of engineering in Denmark.
BAPE – A Bathing Ape is a cult clothing company founded by Tomoaki "Nigo" Nagao in 1993. The name is derived from a Japanese saying, "A Bathing Ape in Lukewarm Water", which Nigo says is "a reference to the young generation being spoiled, pampered and too complacent."
BASF – from Badische Anilin und Soda Fabriken. Anilin and soda were the first products. "Badisch" refers to the location in the state of Baden, Germany (Black Forest region).
Bauhaus – European chain of DIY stores founded by Heinz-Georg Baus and named from the German words bauen (to build) and Haus (house). The reference to the classic Bauhaus art school is only an allusion.
Bauknecht – founded as an electrotechnical workshop in 1919 by Gottlob Bauknecht, and now a Whirlpool brand
Bayer – named after Friedrich Bayer, who founded the company in 1863
BBC – British Broadcasting Corporation, originally British Broadcasting Company
BBVA – Banco Bilbao Vizcaya Argentaria, a Spanish banking group formed in 1999 from the merger of Banco Bilbao Vizcaya and Argentaria
BEA Systems – from the first initial of each of the company's three founders: Bill Coleman, Ed Scott and Alfred Chuang
Beko – Turkish consumer electronics company named after its founders, Bejerano and Koç
Ben & Jerry's – named after Ben Cohen and Jerry Greenfield, who founded an ice cream parlor in 1978 after completing a correspondence course on ice cream making from Pennsylvania State University. The company, Ben & Jerry's Homemade Holdings, Inc. was later taken over by Unilever.
BenQ – Bringing Enjoyment and Quality to life
Berkshire Hathaway – originally a textile company formed by the merger of Berkshire Fine Spinning Associates and the Hathaway Manufacturing Company. In 1964, the declining company was taken over by one of its investors, Warren Buffett, who converted it into a conglomerate holding company.
BHP – Broken Hill Proprietary, named after the town of Broken Hill, where BHP was founded
BIC Corporation – pen company was named after one of its founders, Marcel Bich. He dropped the final h to avoid a potentially inappropriate English pronunciation of the name.
Black & Decker – named after founders S. Duncan Black and Alonzo G. Decker.
BlackBerry – first device produced by the company originally known as Research In Motion (below) was a two-way pager; the BlackBerry name was chosen because of the resemblance between the keyboard buttons and the drupelets that form the blackberry fruit. The company rebranded itself as BlackBerry in 2013.
Blaupunkt – Blaupunkt ("Blue dot") was founded in 1923 under the name "Ideal". Its core business was the manufacturing of headphones. If the headphones came through quality tests, the company would give the headphones a blue dot. The headphones quickly became known as the blue dots or blaue Punkte. The quality symbol would become a trademark and the trademark would become the company name in 1938.
Blizzard Entertainment - videogame company founded in 1991 as Silicon & Synapse, it briefly changed its name to Chaos Studios (1993–94), before discovering there was already a company using the Chaos name. It picked Blizzard from the dictionary.
BMW – Bayerische Motoren Werke (Bavarian Motor Works).
Bo-Dyn Bobsled Project – Geoff Bodine and Chassis Dynamics, the bobsled maker that the NASCAR driver teamed with. The company name is pronounced the same as that of Bodine himself: .
Boeing – named after founder William E. Boeing. It was originally called Pacific Aero Products Co.
Bosch – named after founder Robert Bosch. Robert Bosch GmbH (full company name) is a German diversified technology-based corporation.
Bose Corporation – named after founder Amar Bose
BP – formerly British Petroleum, now BP (The slogan "Beyond Petroleum" has incorrectly been taken to refer to the company's new name following its rebranding effort in 2000.)
BRAC – Bangladesh Rural & Advancement Committee, world's largest NGO (non-governmental organization)
Bridgestone – named after founder Shojiro Ishibashi. The surname Ishibashi (石橋) means "stone bridge", or "bridge of stone".
Brine, Corp. – sporting goods company named after founder, W.H. Brine. It was taken over by New Balance in 2006.
Brooks Sports – anglicized version of Bruchs, the maiden name of the wife of founder Morris Goldenberg.
Brunswick Corporation – founded in 1845 as "J.M. Brunswick Manufacturing Company" in Cincinnati, Ohio by John Moses Brunswick, an immigrant from Bremgarten, Switzerland
BSA – Birmingham Small Arms Company, which started out making guns but later became best known for its motorcycles.
BT – formerly British Telecom (from BT Group, formerly British Telecommunications plc.)
Buick – named for its founder, David Dunbar Buick. The company was the original focal point for General Motors, established in 1908 as a holding company for Buick plus other companies acquired by William C. Durant. Buick survives to this day as a GM brand.
Bull – Compagnie des machines Bull was founded in Paris to exploit the patents for punched card machines taken out by Norwegian engineer Fredrik Rosing Bull.
Burroughs Corporation – founded in 1886 as the American Arithmometer Company and later renamed after the adding machine invented by William Seward Burroughs. The company took over Sperry Corporation and became Unisys.
Bultaco – Spanish company of motorcycles, which disappeared in the 1980s. Its name is based on the name of its founder, Paco Bultó.
ByWater Solutions – library software company named after a village in J. R. R. Tolkien's The Lord of the Rings
C
C&A – named after the brothers Clemens and August Brenninkmeijer, who founded a textile company called C&A in the Netherlands in 1841
CA – Computer Associates was founded in 1976 as Computer Associates International, Inc. by Charles Wang and Russell Artzt.
Cadillac – the car company, founded in 1902, was named after the 18th-century French explorer Antoine Laumet de La Mothe, sieur de Cadillac. Cadillac is a small town in the South of France. The company was taken over by General Motors in 1909 and survives as a GM brand.
CAE – originally Canadian Aviation Electronics
Campagnolo – from the name of its founder, Tullio Campagnolo
Canon – originally (1933) "Precision Optical Instruments Laboratory", the new name (1935) derived from the name of the company's first camera, the Kwanon, in turn named after the Japanese name of the Buddhist bodhisattva of mercy.
Capcom – Capsule Computers, the former name of the company and how they described the arcade machines they manufactured at the time
Caprabo – Catalan supermarkets, founded by Pere Carbó, Jaume Prats and Josep Bonet
Carrefour – chain of supermarkets and hypermarkets which started with a store near a crossroads (carrefour in French) in Annecy
Casio – from the name of its founder, Kashio Tadao, who had set up the company Kashio Seisakujo as a subcontractor factory
Caterpillar – originally Holt Tractor Co, merged with Best Tractor Co. in 1925. A company photographer exclaimed aloud of a Holt tractor that the tracks' movement resembled a caterpillar moving along the ground. The name stuck.
Cathay Pacific Airways Limited – airline was founded on 24 September 1946 by American Roy C. Farrell and Australian Sydney H. de Kantzow, with each man putting up HK$1 to register the airline. They named it Cathay Pacific because Cathay was the ancient name given to China; and Pacific because Farrell speculated that they would one day fly across the Pacific.
CBS – Columbia Broadcasting System
Celera – inspired by ‘celerity’ or swiftness (in decoding the human genome), with "era of the cell" a secondary meaning
Cemex – portmanteau of the company's former name of Cementos Mexicanos (Spanish for "Mexican Cement")
Cerner – from the Latin "cerner" meaning "to discern"
CGI Group – from the first letters of Information Management Consultant in French (Conseillers en Gestion et Informatique)
Chello – Dutch internet service provider, its name was originally pronounced 'say hello' (in Dutch the letter C at the beginning of a word is pronounced 'say'). This did not catch on and now it is pronounced "cello" (as in the stringed instrument).
Chevrolet – named after company co-founder Louis Chevrolet, a Swiss-born auto racer. The company was merged into General Motors in 1917 and survives only as a brand name.
Chrysler – named after the company founder, Walter P. Chrysler. Merged with Fiat in 2014 to create Fiat Chrysler Automobiles (FCA), with the Chrysler corporate entity becoming the Fiat Chrysler subsidiary FCA US. The "Chrysler" name survives as a brand of FCA US.
Ciba Geigy – CIBA, named from Chemical Industry Basel (after Basel in Switzerland), merged with a company named after its founder Johann Rudolf Geigy-Merian. It became Novartis (below) after a merger with Sandoz.
CiCi's Pizza – from the first letters of the last names of the founders of the franchise (Joe Croce and Mike Cole)
Cigna – CIGNA was formed in 1982 through the combination of Insurance Company of North America (INA) and Connecticut General (CG). The name is a combination of the letters of the predecessor companies, CG and INA.
Cincom – originally called United Computer Systems, which was similar to several other software and services companies of the day. Two of the three founders visited Philco (Philadelphia Company), and this inspired them to create a new company name derived from Cincinnati (where it was based) and Computer (its business).
Cisco – short for San Francisco.
Citroën – named after André Citroën (1878–1935), a French entrepreneur of Dutch descent. He was the fifth and last child of the Dutch Jewish diamond merchant Levie Citroen and Mazra Kleinmann (of Warsaw, Poland). The Citroen family moved to Paris from Amsterdam in 1873 where the name changed to Citroën.
CKX, Inc. – named from "Content is King", with the X from founder Robert F.X. Sillerman. Other Sillerman companies include SFX Entertainment and FXM Asset Management.
Clarion – named after the "bugle-like wind instrument used in ancient Greece", says the company, which wanted a name English speakers would find easy to remember. It was founded in Japan in 1940 as Hakusan Wireless Electric Company, making radios, and became Teikoku Dempa after merging with Takizawa Wireless Electric Industries in 1943.
CNN – Cable News Network
Coca-Cola – derived from the coca leaves and kola nuts used as flavoring. Coca-Cola creator John S. Pemberton changed the 'K' of kola to 'C' to make the name look better.
Coleco – began as the Connecticut Leather Company
Colgate-Palmolive – formed from a merger of soap manufacturers Colgate & Company and Palmolive-Peet. Peet was dropped in 1953. Colgate was named after William Colgate, an English immigrant, who set up a starch, soap and candle business in New York City in 1806. Palmolive was named for the two oils (Palm and Olive) used in its manufacture.
COLT – from City Of London Telecom
Comcast – from communications and broadcast
Commodore International – supposedly named after the Opel Commodore, after the company's founder Jack Tramiel had unsuccessfully tried to name his company first "General" and then "Admiral". However, the Opel Commodore only debuted in 1967, years after the company's founding.
Compaq – from computer and "pack" to denote a small integral object; or: Compatibility And Quality; or: from the company's first product, the very compact Compaq Portable
COMSAT – contraction of communications satellites. This American digital telecommunications and satellite company was founded during the era of U.S. President John F. Kennedy era to develop the technology.
ConocoPhillips – formed from the merger of Conoco (from Continental Oil Company) and the Phillips Petroleum Company, named after the brothers who founded it: Lee Eldas "L.E." and Frank Phillips.
Copersucar – Brazilian production cooperative in sugar and alcohol; its name is a contraction of Cooperativa de Açucar e Álcool
Corel – from Cowpland Research Laboratory, after the name of the company's founder, Michael Cowpland
Cosworth – automotive engineering company named after company founders Mike Costin and Keith Duckworth.
CPFL – Companhia Paulista de Força e Luz (São Paulo Company of Light and Power), one of the largest in Brazil, based in Campinas
Crabtree & Evelyn – toiletry company named after gardener John Evelyn, and the tree that bears Crabapples
Cray – supercomputer company named after its founder, Seymour Cray
CRC Press – originally Chemical Rubber Company
Cromemco – early microcomputer company in Silicon Valley (circa 1975–198?) founded by two PhD students who once lived at Stanford University's Crothers Memorial Hall (a dormitory)
Cutco – Cooking Utensils Company
CVS – originally Consumer Value Stores. CEO Tom Ryan has said he now considers "CVS" to stand for "Customer, Value, and Service".
D
Daewoo – company founder Kim Woo Chong called it Daewoo which means "Great House" or "Great Universe" in Korean
DAF Trucks – from 1932 the company's name was Van Doorne's Aanhangwagen Fabriek (Van Doorne's Trailer Factory). In 1949 the company started making trucks, trailers and buses and changed the name into Van Doorne's Automobiel Fabriek (Van Doorne's Automobile Factory).
Daihatsu – first kanji from "Osaka" (大坂, the kanji is here pronounced dai) and "engine" (発動機, the first kanji is hatsu). Engine manufacturers were listed on the Tokyo and Osaka Stock Exchanges, and their names shortened to the first kanji. (The company listed on the Tokyo exchange is Tohatsu.)
Danone (Dannon in the U.S.) – Isaac Carasso in Barcelona made his first yogurts with the nickname of his first son Daniel (DAN-ONE)
Dassault Aviation – origins of the company go back to 1929 with SAAMB (Société des Avions Marcel Bloch), named after its founder Marcel Bloch (1892-1986). Bloch changed his name to Marcel Dassault in 1949. Dassault was derived from char d'assaut (French for "assault wagon" or battle tank), the codename that his brother had used in the French resistance.
Datsun – first called DAT, from the initials of its financiers Den, Aoyama and Takeuchi. Soon changed to DATSON to imply a smaller version of their original car, then (as SON can mean "loss" in Japanese) again to DATSUN when they were acquired by Nissan.
DEC – Digital Equipment Corporation, a pioneering American minicomputer manufacturer founded by Ken Olsen and taken over by Compaq, before Compaq was merged into Hewlett-Packard (HP). It was generally called DEC ("deck"), but later tried to rebrand itself as Digital.
DEKA – named after its founder Dean Kamen, developer of the Segway, iBOT, HomeChoice Dialysis and other products.
Delhaize – named after its founders, Jules Delhaize and his brothers, who originated from Charleroi (Belgium). They opened the first European self-service "supermarket" in Ixelles/Elsene, a Brussels borough.
Dell – named after its founder, Michael Dell. The company changed its name from Dell Computer in 2003.
Denning & Fourcade, Inc. – interior designer company named after its founders Robert Denning and Vincent Fourcade in 1960.
DHL – named after its founders, Adrian Dalsey, Larry Hillblom, and Robert Lynn. DHL was taken over by the German post office and both now operate under the group name Deutsche Post DHL.
Diageo – name created by branding consultancy Wolff Olins in 1997. It is based on the Latin word diēs, meaning "day", and the Greek root geo-, meaning "world". This refers to the company slogan, "Celebrating Life, Every Day, Everywhere".
Dick's Sporting Goods – named after its founder, Dick Stack, who opened a bait and tackle shop in 1948 with a $300 gift from his grandmother
Digg, Inc. – Kevin Rose's friend David Prager (The Screen Savers, This Week in Tech) originally wanted to call the site "Diggnation", but Kevin wanted a simpler name. He chose the name "Digg", because users are able to "dig" stories, out of those submitted, up to the front page. The site was called "Digg" instead of "Dig" because the domain name "dig.com" was previously registered, by Walt Disney Internet Group. "Diggnation" would eventually be used as the title of Kevin Rose and Alex Albrecht's weekly podcast discussing popular stories from Digg.
Digi-Key – electronic component distributor whose name is derived from founder Dr. Ronald Stordahl's amateur radio telegraphic keyer, the "IC Keyer Kit", which utilized digital integrated circuits
Dillard's – named for William T. Dillard who founded the Arkansas-based department store in 1938
Dixons – commonly used abbreviation for DSG International plc (Dixons Stores Group), a UK-based retailer. The company was founded in 1937 by Charles Kalms and Michael Mindel. When opening their first photographic shop in Southend, they only had room for six letters on the fascia, and chose the name Dixons from the phone book.
DKNY – Donna Karan New York
Double Fine Productions – named after a sign upon the Golden Gate Bridge that warned patrons that it was "Double Fine Zone" referring to the fact that speeders would be charged twice.
Dow – named after its founder, Herbert Henry Dow
DSM – established in 1902 to exploit the Dutch coal mines, the name meaning Dutch State Mines. The last mine closed in 1973, and the company switched to chemicals.
Duane Reade – named after Duane and Reade Streets in lower Manhattan, where the chain's first warehouse was located. The chain was purchased by Walgreens in 2010, but still operates separately.
DuPont – short name for E. I. du Pont de Nemours and Company. This American chemical company was founded in 1802 as a gunpowder mill by Eleuthère Irénée du Pont, who left France to escape the French Revolution.
Dynegy – Natural Gas Clearinghouse changed its name in 1998 to reflect its self-described traits as a dynamic energy company. "Dynergy" had already been taken by a German health foods company.
E
E. J. Korvette – named for the founder Eugene Ferkauf and his associate Joe Swillenberg; an intentional misspelling of "Corvette". A common urban legend misstates the origin as "Eight Jewish Korean War Veterans".
EA - Electronic Arts. The company was founded in May 1982 as Amazin' Software and rebranded as Electronic Arts in October the same year.
eBay – Pierre Omidyar, who had created the Auction Web trading website, had formed a web consulting concern called Echo Bay Technology Group. "Echo Bay" did not refer to the town in Nevada, "It just sounded cool", Omidyar reportedly said. Echo Bay Mines Limited, a gold mining company, had already taken EchoBay.com, so Omidyar registered what (at the time) he thought was the second best name: eBay.com.
EDS – Electronic Data Systems, founded in 1962 by former IBM salesman Ross Perot. According to the company history: "He chose Electronic Data Systems from potential names he scribbled on a pledge envelope during a service at Highland Park Presbyterian Church in Dallas."
El Al - Hebrew: אל על‎, "To the Skies" or "Skywards", Arabic: إل-عال
Eidos – named from a Greek word meaning "species".
Eletropaulo – one of the largest Brazilian companies in electricity generation and distribution, its name derives from Companhia de Electricidade de São Paulo.
Elron - from Estonian "elektrirong ("electrical train").
Embraer – Brazilian aircraft manufacturer, its name is an abbreviation of Empresa Brasileira de Aeronáutica (Brazilian Aeronautics Company).
EMBRAPA – Brazilian state agricultural research and development company, its name is an abbreviation of Empresa Brasileira de Pesquisa Agropecuária (Brazilian Agriculture Research Company).
EMBRATEL – abbreviation of Empresa Brasileira de Telecomunicações (Brazilian Telecommunications Company). Brazil's largest telecommunications company, it was a state monopoly until 1992 when it was privatized and sold to MCI, then later resold to Telmex.
EMC Corporation – named from the initials of the founders, Richard Egan and Roger Marino. There has long been a rumor that another partner provided the third letter (C). Other reports indicate the C stands for Company. EMC adopted the EMC² notation to refer to Einstein's famous equation, E = mc².
EMI – formerly Electric and Musical Industries Ltd.
Emporis – Empor comes from the German and means "aloft, rising"; one of the world's largest providers of data concerning buildings
Epson – Epson Seiko Corporation, the Japanese printer and peripheral manufacturer, was named from "Son of Electronic Printer" after a highly successful model, the EP-101.
Equifax – from equitable and factual
Ericsson – Telefonaktiebolaget LM Ericsson is named after its founder Lars Magnus Ericsson, who opened a telegraph equipment repair shop in Stockholm, Sweden, in 1876
Ernst & Young – named for the company's founders, A.C. Ernst and Arthur Young
ESPN – Entertainment and Sports Programming Network
ESRI – Environmental Systems Research Institute, the first geographic information system (GIS) software company founded by Jack and Laura Dangermond in Redlands, California, in 1969
Esso – enunciation of the initials S.O. in Standard Oil of New Jersey
Etsy – founder Rob Kalin said that he named the site Etsy because he "wanted a nonsense word because I wanted to build the brand from scratch. I was watching Fellini's 8 ½ and writing down what I was hearing. In Italian, you say 'etsi' a lot. It means 'oh, yes' (actually it's "eh, si"). And in Latin and French, it means 'what if.'"
Evernote – combination of the words forever and note to indicate the core service that the app provides
Exxon – name contrived by Esso (Standard Oil of New Jersey) in the early 1970s to create a neutral but distinctive label for the company. Within days, Exxon was being called the "double cross company" but this eventually subsided. (Esso is a trademark of ExxonMobil.) Esso could not use its name in parts of the U.S. because of restrictions dating to the 1911 Standard Oil antitrust decision.
F
F5 Networks – originally F5 Labs – taken from the Fujita scale of ratings for tornado intensity, where F5 is the most intense to be used in normal practice even though the scale can physically describe up to F12 which corresponds to wind velocities of Mach 1.0.
Facebook – name stems from the colloquial name of books given to newly enrolled students at the start of the academic year by university administrations in the US with the intention of helping students to get to know each other better.
Fair Isaac Corporation – named after founders Bill Fair and Earl Isaac
FAS – abbreviation for Foras Áiseanna Saothair (Labour Facilities Foundation). Fás means grow in Irish.
Fazer – Finnish food company named after its founder, Karl Fazer
FCUK – French Connection United Kingdom
FedEx – abbreviation of Federal Express Corporation, the company's original name
Fegime – abbreviation for "Fédération Européenne des Grossistes Indépendants" (European Federation of Independent Electrical Wholesalers)
Ferodo – anagram of the name of its founder, Herbert Froode
Ferrari – from the name of its founder, Enzo Ferrari
Fiat – acronym of Fabbrica Italiana Automobili Torino (Italian Automobile Factory of Turin)
Finnair – from "Finland" and "air". Originally called "Aero Osakeyhtiö", which led to its international flight code, "AY".
Firestone – named after its founder, Harvey Firestone
Fisher-Price – toy company named after two of its three founders: Herman Fisher, Irving Price, and Helen Schelle. It became a Mattel subsidiary in 1993.
Fiskars – from the town of Fiskars, where the company was founded.
Five Guys – American restaurant chain founded by "five guys" – Jerry Murrell and his four sons. The "five guys" would later become the Murrell sons, after Jerry and his wife Janie had a fifth son two years after opening their first restaurant.
Fluke – named after its founder, John Fluke, Sr.
Fonterra – glosses its own name as "spring from the land". That would match a faux-Latin combination of fons (stem font-) conveying the idea of a fountain or spring, and terra, meaning earth, land, or ground.
Ford Motor Company – named after its founder, Henry Ford, who introduced automobile mass production in 1914.
Forrester Research – from the family name of the mother of the founder George Forrester Colony.
FranklinCovey – named after Benjamin Franklin and Stephen Covey. The company was formed from the 1997 merger of FranklinQuest and the Covey Leadership Center.
Fuji – named after Mount Fuji, the highest mountain in Japan
Fujitsu – originally the data division of Fuji Electric, which was a joint venture between Furukawa Electric and Siemens. The tsu comes from tsūshinki, meaning data equipment.
G
Gallup – polling company named after its founder, George Gallup. After his death in 1984, the company was sold to Selection Research, Incorporated (SRI).
Garmin – named after its founders, Gary Burrell and Dr. Min Kao
Gartner – named after its founder, Gideon Gartner, who left the firm in 1992 to start Giga (named from Gideon Gartner)
Gatti's Pizza – Gatti was the maiden name of Pat Eure, wife of company founder Jim Eure.
GCap Media – named after the merger of the GWR Group and Capital Radio Group in May 2005. GWR was launched in 1985 after the merger of Radio West and Wiltshire Radio.
GEICO – from Government Employees Insurance Company
Genentech – from Genetic Engineering Technology
Gerdau – largest producer of long steel in the Americas, named from the surname of the founder, Johannes Heinrich Kaspar Gerdau
Gilead Sciences – pharmaceutical company named after Gilead, a biblical place name
Glaxo – dried-milk company set up in Bunnythorpe, New Zealand, by Joseph Edward Nathan. The company wanted to use the name "Lacto" but it was similar to some already in use. The company says: "By adding and changing letters, the name Glaxo evolved and was registered in October 1906." GlaxoSmithKline was a 2000 merger of Glaxo Wellcome and SmithKline Beecham.
Glock Ges.m.b.H. – named after its founder, Gaston Glock
Goodyear – named after the founder of vulcanization, Charles Goodyear, the Goodyear Tire and Rubber company was founded by Frank Seiberling in 1898
Google – originally an accidental misspelling of the word "googol", settled upon because google.com was unregistered. Googol was proposed to reflect the company's mission to organize the immense amount of information available online.
Grey Global Group – advertising and marketing agency supposed to have derived its name from the colour of the walls of its first office
Groupon – chief executive Andrew Mason used the derivation as his five-word acceptance speech at the 2011 Webby Awards ceremony: "It's short for group coupon."
Grundig – named after its founder, radio dealer-turned-manufacturer Max Grundig, in 1945
Gucci – named after its founder, Guccio Gucci, who became familiar with high class luggage while working as a lift boy at the Savoy Hotel in London. He returned to Florence and started making travel bags and accessories, founding the House of Gucci in 1921.
Gulfstream Aerospace – named after the Gulf Stream current that starts in the Gulf of Mexico and crosses the Atlantic. The company traces its origins to the Grumman Aircraft Engineering Corporation, which was sold and renamed in 1985.
H
H&M – named from Hennes & Mauritz. In 1947, Swedish businessman Erling Persson established Hennes, a ladies' clothing store, in Västerås, Sweden. "Hennes" is Swedish for "hers". In 1968, Persson bought the Stockholm premises and inventory of a hunting equipment store called Mauritz Widforss. The inventory included a collection of men's clothing, which prompted Persson to expand into menswear.
H&R Block – after the founders, brothers Henry W. and Richard Bloch (with "Bloch" changed to "Block" to avoid mispronunciation)
Häagen-Dazs – name was invented in 1961 by ice-cream makers Reuben and Rose Mattus of the Bronx "to convey an aura of the old-world traditions and craftsmanship" The name has no meaning.
Haier – Chinese 海 "sea" and 尔 (a transliteration character; also means "you" in Literary Chinese). Portion of transliteration of German Liebherr 利勃海尔.
Happy Madison Productions – film and TV production company founded by Adam Sandler, its name is taken from the films Happy Gilmore and Billy Madison, two of his box office successes.
Haribo – from the name of the founder and the German home town of the company: Hans Riegel, Bonn
Harman Kardon – named after its founders Dr. Sidney Harman and Bernard Kardon
Harpo Productions – production company founded by Oprah Winfrey; "Oprah" spelled backwards.
Harvey Norman – named after its founders Gerry Harvey and Ian Norman
Hasbro – founded by Henry and Helal Hassenfeld, the Hassenfeld Brothers
HBOS – UK-based banking company formed by the merger of the Halifax and the Bank of Scotland
HDFC – Housing Development Finance Corporation, Indian mortgage company.
Hesburger – from Hese, the nickname of the company's founder Heikki Salmela, and hamburger
Hess Corporation – named after its founder Leon Hess
Hispano-Suiza – former Spanish luxury automotive and engineering firm; its name – literally meaning "Spanish-Swiss" – refers to Spanish origin of the company and Swiss origin of its head engineer Marc Birkigt
Hitachi – old place name, literally "sunrise"
HMV – from "His Master's Voice", which appeared in 1899 as the title of a painting of Nipper, a Jack Russell terrier, listening to a gramophone
Hoechst – from the name of a district in Frankfurt
Honda – from the name of its founder, Soichiro Honda
Honeywell – from the name of Mark Honeywell, founder of Honeywell Heating Specialty Co. It later merged with Minneapolis Heat Regulator Company and was finally called Honeywell Inc. in 1963.
Hospira – name, selected by the company's employees, is derived from the words hospital, spirit, inspire and the Latin word spero, which means hope. It expresses the hope and optimism that are critical in the healthcare industry.
Hotmail – founder Jack Smith got the idea of accessing e-mail via the web from a computer anywhere in the world. When Sabeer Bhatia came up with the business plan for the mail service he tried all kinds of names ending in 'mail' and finally settled for Hotmail as it included the letters "HTML" – the markup language used to write web pages. It was initially referred to as HoTMaiL with selective upper casing. (At one time, if you clicked on Hotmail's 'mail' tab, you would have seen "HoTMaiL" in the URL.) Hotmail addresses now use Microsoft's Outlook.com service.
HP – co-founders Bill Hewlett and Dave Packard tossed a coin to decide whether their company would be called Hewlett-Packard or Packard-Hewlett. In November 2015, Hewlett-Packard split into two listed companies: HP Inc and Hewlett Packard Enterprise Co.
HSBC – Hongkong and Shanghai Banking Corporation.
HTC – contraction of its original corporate name, High Tech Computer Corporation.
Huawei – Chinese 华 (hua) and 为 (wei) as a whole may be translated as "splendid act" or "China is able"; Hua can mean "splendid" (literally "flowery beauty") or "China", while wei can mean "action" or "achievement".
Hudson's Bay Company – in 1670, a Royal Charter granted the lands of the Hudson Bay watershed to "the Governor and Company of Adventurers of England trading into Hudson Bay." The company ceded the territory to Canada in 1870.
Hyundai – connotes the sense of "the present age" or "modernity" in Korean
I
IBM – named by Tom (Thomas John) Watson Sr, an ex-employee of National Cash Register (NCR Corporation). To one-up them in all respects, he called his company International Business Machines.
ICL – abbreviation for International Computers Limited, once the UK's largest computer company but now a service arm of Fujitsu, of Japan.
IG Farben – Interessen-Gemeinschaft Farbenindustrie AG was so named because the constituent German companies produced dyestuffs among many other chemical compounds. The consortium is most known today for its central participation in the World War II Holocaust, as it made the Zyklon B gas used in the gas chambers.
IGN Entertainment – IGN Entertainment is an online entertainment media outlet. Its name comes from its origin as a spin-off of Imagine Media and used to stand for Imagine Games Network.
Iiyama – manufacturer of monitors and TVs, named after the Japanese city, Iiyama
IKEA – composite of the first letters in the Swedish founder Ingvar Kamprad's name in addition to the first letters of the names of the property and the village in which he grew up: Ingvar Kamprad Elmtaryd Agunnaryd.
IMI – Imperial Metal Industries, split off from Imperial Chemical Industries
InBev – name was created after the merger of the Belgian company Interbrew with Brazilian Ambev
Inditex – Spanish group named from Industria de Diseño Textil (Textile Design Industry).
Infineon Technologies – derived from Infinity and Aeon. The name was given to Siemens's Semiconductor branch (called Siemens HL or Siemens SC/SSC) when it was spun off.
Ingenico – electronic payment device manufacturer based in Paris and named from the French Ingenieux Compagnie (Ingenious Company)
Inktomi – internet search engine, acquired by Yahoo! in 2002; named after Iktomi, a spider-trickster spirit from Lakota Indian legends
Intel – Robert Noyce and Gordon Moore initially incorporated their company as N M Electronics. Someone suggested Moore Noyce Electronics but it sounded too close to "more noise". Later, Integrated Electronics was proposed but it had already been taken, so they used the initial syllables (INTegrated ELectronics). To avoid potential conflicts with other companies with similar names, Intel purchased the name rights for $15,000 from a company called Intelco. (Source: Intel 15 Years Corporate Anniversary Brochure)
ITC – established in 1910 as the Imperial Tobacco Company.
J
J. C. Penney – from James Cash Penney, founder of the department store chain.
J2TV – television and film production company formed by Malcolm in the Middle actor Justin Berfield and producer Jason Felts
JAL – from Japan Airlines
Jat Airways – founded in 1927 as "Aeroput" (Airway in Serbian). From 1947, it was known as JAT (Jugoslovenski Aero Transport). After the break-up of the former Yugoslavia (and after Federal Republic of Yugoslavia changed its name to Serbia and Montenegro), the company kept the name, Jat, but not as an abbreviation.
Jawa Motors – from Janeček (the owner) and Wanderer (the motorcycle product)
JBL – from James B Lansing, an electronics designer
Johnson & Johnson – originally a partnership between brothers James Wood Johnson and Edward Mead Johnson in 1885, the addition of brother Robert Wood Johnson I led to formal incorporation as Johnson & Johnson in 1887.
Jordache – from the first names of the Nakash brothers who founded the company: Joe, Ralph, David (Ralph's first son), Avi, plus che, after the second syllable of "Nakash"
JVC – Japan Victor Company (Victor Company of Japan, Ltd) was founded in 1927 as a US subsidiary, The Victor Talking Machine Company of Japan, Limited. JVC developed the VHS video cassette format.
K
Kalev – after Kalev, the character from Estonian mythology and father of the protagonist in the national epic Kalevipoeg ("Son of Kalev").
Kamaz – after Kama River; long form Kamskiy avtomobilny zavod (Kama Automobile Plant)
Kawasaki – from the name of its founder, Shozo Kawasaki
KFC – short for Kentucky Fried Chicken
Kenvelo – clothing retailer founded in the Czech Republic by Israel-born owner Dany Himi. Various names were proposed to managers, but some said "yes" and some "no". David Dahan came up with yesandno or Ken (yes), ve (and) lo (no) in Hebrew (כן ולא).
Kenwood Electronics – Bill Kasuga was a partner in a firm that imported Japanese-made audio products from Trio Corporation to the United States. Kasuga wanted to create a trustworthy and Western-sounding name for products sold by his importing company as he was confident of the quality of Trio's products in a period when Japanese-made goods were considered inferior. He came up with Kenwood by combining "Ken" – a name common to Japan and North America that had proven acceptable to American consumers in the name of Kenmore Appliances – and "wood", referring to the durable substance as well as suggesting a relation to Hollywood. Trio Corporation renamed itself Kenwood in 1986.
Kenwood Limited – named after Kenneth (Ken) Wood, who founded this kitchenware company in the UK in 1947 with wartime colleague Roger Laurence as Woodlau Industries It is not related to Kenwood Electronics, which started as Kasuga Radio Co in Japan in 1946 and became Trio Corporation in 1960.
Kenworth Truck Company – named after the two principal stockholders Harry Kent and Edgar Worthington
Keurig – from the Dutch word keurig. Company co-founder John Sylvan said that once his coffee pod system worked, "he looked up the word excellence in Dutch — because 'everyone likes the Dutch'."
Kia Motors – "Kia" (起亞) roughly translates as "Rising from Asia" in Hanja
Kinko's – from the college nickname of founder, Paul Orfalea. He was called Kinko because he had curly red hair. The company was bought by FedEx for $2.4 billion in 2004.
Kmart – named for Sebastian S. Kresge, who opened the first Kmart in 1962 as a division of his S. S. Kresge Company. The company became Kmart Corporation in 1977. After purchasing Sears, Roebuck & Company in 2005, the merged company became Sears Holdings Corporation, with Kmart continuing as a discount store chain within the new structure.
Kodak – both the Kodak camera and the name were the invention of founder George Eastman. The letter "K" was a favorite with Eastman; he felt it a strong and incisive letter. He tried out various combinations of words starting and ending with "K". He saw three advantages in the name. It had the merits of a trademark word, would not be mis-pronounced and the name did not resemble anything in the art. There is a misconception that the name was chosen because of its similarity to the sound produced by the shutter of the camera.
Komatsu – Japanese construction vehicle manufacturer named from the city of Komatsu, Ishikawa, where it was founded in 1917
Kone – Means "machine" or "device" in Finnish.
Konica – earlier known as Konishiroku Kogaku. Konishiroku in turn is the short for Konishiya Rokubeiten, which was the first name of the company established by Rokusaburo Sugiura in the 1850s.
Korg – named from the surnames of the founders, Tsutomu Katoh and Tadashi Osanai, combined with the letters "rg" from the word "organ"
KPMG – from the last names of the founders of the firms which combined to form the cooperative: Piet Klijnveld, William Barclay Peat, James Marwick, and Reinhard Goerdeler
Kroger – American supermarket chain named after its founder, Barney Kroger
KUKA – founded in 1898 in Augsburg, Germany as Keller Und Knappich Augsburg, it shortened its name to KUKA. Today, it is a manufacturer of industrial robots and automation systems.
Kyocera – from Kyoto Ceramics, after Kyoto in Japan
L
LaCie – from the French phrase la cie, meaning "the company"
Lada – from the name of a Slavic goddess, and used as a trading name by Russian automobile manufacturer AvtoVAZ (АВТОВАЗ in Russian). VAZ is derived from Volzhsky Automobilny Zavod.
Lancôme – began in 1935, when its founder, Armand Petitjean, was exploring the ruins of a castle, Le Chateau de Lancôme (Loir-et-Cher) while vacationing in the French countryside. Petitjean's inspiration for the company's symbol, a rose, was the many wild roses growing around the castle.
LCL – from Le Crédit Lyonnais
Lego – combination of the Danish "leg godt", which means to "play well". Lego also means "I put together" in Latin, but Lego Group claims this is only a coincidence and the etymology of the word is entirely Danish. Years before the little plastic brick was invented, Lego manufactured wooden toys.
Lenovo Group – portmanteau of "Le-" (from former name Legend) and "novo", pseudo-Latin for "new". This Chinese company took over IBM's PC division.
Lesney Products – named from the founders Leslie Smith and Rodney Smith, who were school friends but not related. This British company made the Matchbox series of die-cast toys, similar to Dinky toys.
Level 3 Communications – "Level 3" is a reference to the network layer of the OSI model.
Lexmark – in the 1980s, IBM wanted to spin off its printer and typewriter businesses. The main production facility for this business segment was in Lexington, Kentucky, and the code name for the spinoff was Lexington Marketing.
LG – from the combination of two popular Korean brands, Lucky and Goldstar. (In Mexico, publicists explained the name change as an abbreviation to Linea Goldstar, Spanish for Goldstar Line)
Lidl – Named after painter and retired schoolteacher Ludwig Lidl, from whom Dieter Schwarz, the son of company founder Josef Schwarz bought the rights to the name for 1,000 German marks. Schwarz originally wanted to use the name of his father's former business partner A. Lidl, but legal reasons prevented it. Schwarz did not want to name the company after himself as Schwarzmarkt means "black market" in German.
Lionbridge – word "localisation", which is the service this company offers, is often shortened to L10N. That is the first letter of the word and the last letter of the word, with 10 letters missing in between, hence L 10 N, which looks like lion. Bridge is the second part of the word as translation 'bridges' gap between people and markets that do not have a common language.
Lionhead Studios – games studio named after Mark Webley's pet hamster, which died a week before the company was founded Webley worked for Bullfrog, and co-founded Lionhead with Peter Molyneux, Tim Rance and Steve Jackson in July 1997. Microsoft bought the company in April 2006.
Loblaws – Canadian supermarket chain named for founder Theodore Loblaw
Lockheed Martin – aerospace manufacturer, a combination of Lockheed Corporation and Martin Marietta, which was a combination of Glenn L. Martin Company and American-Marietta Corporation, named for Marietta, Ohio
LoJack – "LoJack" (the stolen-vehicle recovery system) is a pun on the word "hijack" (to steal a vehicle).
Longines – in 1862 the new company "Ancienne Maison Auguste Agassiz, Ernest Francillon, Successeur" was born. At that time watchmaking in the area used the skills of people working outside the "comptoir d'établissage", often at home. In 1866 Ernest Francillon bought two plots of land on the right bank of the river Suze at the place called "Les Longines" and brought all of the watchmaking skills under one roof. This was the first "Longines factory".
Lonsdale – boxing equipment manufacturer named after the Lonsdale Belt, a boxing trophy donated by the English Lord Lonsdale.
L'Oréal – in 1907, Eugène Schueller, a young French chemist, developed an innovative hair-color formula. He called his improved hair dye Auréole.
LOT – LOT Polish Airlines. "Lot" in Polish means "flight".
Lotus Software – Mitch Kapor named his company after the Lotus Position or 'Padmasana'. Kapor used to be a teacher of Transcendental Meditation technique as taught by Maharishi Mahesh Yogi.
LTX – semiconductor test equipment company formed by people who left Teradyne, and said to stand for "Leave Teradyne by Xmas" or possibly "Left Teradyne at Xmas" (Christmas). LTX merged with Credence Systems Corporation and is now part of Xcerra Corporation.
Lucent Technologies – spin-off from AT&T, it was named Lucent (meaning "luminous" or "glowing with light") because "light as a metaphor for visionary thinking reflected the company's operating and guiding business philosophy", according to the Landor Associates staff who chose the name. It was taken over by Alcatel to form Alcatel-Lucent in 2006.
Ludicorp – named from the Latin lūdere (to play) because the intention was to develop an online game, though co-founders Stewart Butterfield and Caterina Fake developed a successful photo-sharing website. They wanted to call it Flicker, but Fake dropped the "e" when the owner of Flicker.com wouldn't sell them the domain name. Ludicorp sold Flickr to Yahoo in 2005. The Oath division of Verizon sold Flickr to SmugMug in 2018.
Lufthansa – founded as Deutsche Luft Hansa in 1926, where "Deutsche Luft" means "German Air" and Hansa refers to the Hanseatic League of medieval guilds. It was renamed Lufthansa in 1933.
Lukoil – from the first letters of the three companies that merged to form the Russian oil giant: Langepasneftegaz, Uraineftegaz, and Kogalymneftegaz, plus the English word "oil"
LVMH – from the initials of the 1987 merger of Louis Vuitton and Moët Hennessy. The former was named after Louis Vuitton while the latter was created in the 1971 merger of two earlier companies, Moët & Chandon (champagne) and Hennessy (cognac).
Lycos – web search engine company founded in 1994 and named from Lycosidae, the family of wolf spiders
M
Maggi – food company named after its founder, Julius Maggi. It was taken over by Nestlé in 1947 and survives as a brand name.
Mailchimp – the email marketing company was originally going to be called Chimpmail but the domain was taken, so co-founder Ben Chestnut switched it around. He told Inc magazine that his parents had had "a pet monkey in Thailand. And they always warned me never to have a pet monkey. So I had this mischievous monkey in my brain."
Malév – Hungary's national airline carrier. Its name comes from Magyar Légiközlekedési Vállalat – meaning Hungarian Air-traffic Company.
MAN – abbreviation for Maschinenfabrik Augsburg-Nürnberg (Augsburg-Nuremberg Machine Company). The MAN company is a German engineering works and truck manufacturer.
Mandriva – new company formed from the merger of Mandrake Linux and Connectiva Linux
Manugistics – Manufacturing + Logistics, a supplier of supply chain optimization software
Manulife Financial – founded in 1887 as Manufacturing Life Insurance Company
Mars – named after Frank C. Mars and his wife, Ethel, who started making candy in 1911. Their son, Forrest E. Mars, joined with Bruce Murrie, the son of a Hershey executive, to form M&M Ltd (from Mars & Murrie). Forrest took over the family business after his father's death and merged the two companies in 1964. After retiring from Mars, Inc. in 1993, Forrest founded Ethel M. Chocolates, named after his mother.
Masco Corporation – from the names of the founder Alex Manoogian, Screw and Company. Masco Screw Products Co. was founded in 1929.
Mast-Jägermeister AG – named for founder Wilhelm Mast and its main product, Jägermeister (German for "hunt master") liqueur
Mattel – portmanteau of the founders names Harold "Matt" Matson and Elliot Handler
Maybach-Motorenbau GmbH – German for "Maybach Engine Construction Company" – was named after Wilhelm Maybach and his son Karl Maybach, who founded it in 1909. The Maybach name continued as a brand of Daimler AG until the end of 2012.
Mazda Motor Corporation – company was founded as Toyo Kogyo, started manufacturing Mazda brand cars in 1931, and changed its name to Mazda in 1984. The cars were supposedly named after Ahura Mazda, the chief deity of the Zoroastrians, though many think this explanation was created after the fact, to cover up what is simply a poor anglicized version of the founders name, Jujiro Matsuda.
MBNA – originally a subsidiary of Maryland National Corporation, MBNA once stood for Maryland Bank, NA (NA itself standing for National Association, a federal designation representing the bank's charter).
McDonald's – from the name of the brothers Dick McDonald and Mac McDonald, who founded the first McDonald's restaurant in 1940.
MCI Communications – Microwave Communications, Inc. The company later merged with Worldcom to create MCI Worldcom. The MCI was dropped in 2000 and the acquiring company changed its name to MCI when it emerged from bankruptcy in 2003.
McSweeney's – Dave Eggers' publishing ventures started with Timothy McSweeney's Quarterly Concern. This was named after mysterious letters that he collected as a child, "written by a man named Timothy McSweeney, who thought he was related to my mother". (McSweeney was his mother's maiden name.)
Mercedes-Benz – formed from the first name of Mercédès Jellinek, the daughter of Emil Jellinek, who distributed cars of the early Daimler company around 1900, and the last name of Karl Benz, one of the owners of the Daimler-Benz company that the Daimler company merged into in 1926.
Merillat Industries – named after Orville D. Merillat, who founded the company in 1946.
Metro-Goldwyn-Mayer (MGM) – film studio formed from the merger of three other companies: Metro Picture Corporation, Goldwyn Pictures Corporation, and Louis B. Mayer Pictures. Goldwyn Picture Corporation in turn was named after the last names of Samuel Goldfish, and Edgar and Archibald Selwyn.
MFI – from Mullard Furniture Industries. The original company was named after the founder's wife, whose maiden name was Mullard.
MG Cars – from Morris Garages after co-founder William Morris. Under Chinese ownership, the company says: "We want Chinese consumers to know this brand as 'Modern Gentleman'."
Microlins – from Microcomputers and Lins, a Brazilian city where the company was founded by José Carlos Semenzato
Micron Technology – computer memory producer named after the microscopic parts of its products. It is now better known by its consumer brand name: Crucial.
Microsoft – coined by Bill Gates to represent the company that was devoted to microcomputer software. Originally christened Micro-Soft, the '-' disappeared on 3/2/1987 with the introduction of a new corporate identity and logo. The "slash between the 'o' and 's' [in the Microsoft logo] emphasizes the "soft" part of the name and conveys motion and speed."
Midway Games – derived from the name of an airport on the southwestern part of Chicago.
Miele – German based manufacturer of high-end domestic appliances, founded in 1899 by Carl Miele and Reinhard Zinkann.
Mincom Limited – company initially created software to specifically assist mining companies and the name Mining 'computing.
Minolta – founded in Osaka, Japan in 1928 as Nichi-Doku Shashinki Shōten (日独写真機商店; literally: Japan-Germany camera shop). It was not until 1934 that the name Minolta first appeared on a camera, the Minolta Vest. The name was given by founder Kazuo Tajima due to its similarity to the Japanese term "minoru ta" {稔る田} meaning "growing rice fields", which came from an ancient Japanese proverb that was a favorite of Tajima's mother meaning "the ripest ears of rice bow their heads lowest", and a desire from Tajima to run an innovative, yet humble business.
MIPRO – stands for MIcrophone PROfessionals. MIPRO is a manufacturer of wireless microphones.
MIPS – originally stood for Microprocessor without Interlocking Pipeline Stages. When interlocks where added to a later implementation, the name was redefined to not be an acronym but just a name. (The name also connotes computer speed, by association with the acronym for millions of instructions per second.)
MITIE – acronym for Management Incentive Through Investment Equity
Mitel – from Mike and Terry's Lawnmowers, after the founders Michael Cowpland (see also: Corel) and Terry Matthews, and the company's original business plan
MITRE – Massachusetts Institute of Technology Research Establishment (however, the MITRE Corporation asserts that its name is not an acronym)
Mitsubishi – name Mitsubishi (三菱) has two parts: mitsu means three and hishi (changing to bishi in the middle of the word) means diamond (the shape). Hence, the three diamond logo. (Note that "diamond" in this context refers only to the rhombus shape, not to the precious gem.)
Mondelez International - American multinational snacks company spun off from Kraft Foods Inc. Kraft Foods said: "'Monde' derives from the Latin word for 'world,' and 'delez' is a fanciful expression of 'delicious'. In addition, 'International' captures the global nature of the business."
Moneris Solutions – Latin for "you (singular) are being protected"
Morningstar, Inc. – name is taken from the last sentence in Walden, a book by Henry David Thoreau; "the sun is but a morning star"
Motorola – founded in 1928 as the Galvin Manufacturing Company by two brothers, Paul V. and Joseph E. Galvin. It was renamed after its Motorola car radios became widely known. The "ola" ending was already in use, most famously for the "Victrola" phonograph made by the Victor Talking Machine Company.
Mozilla Foundation – from the name of the web browser that preceded Netscape Navigator. When Marc Andreesen, co-founder of Netscape, created a browser to replace the Mosaic browser, it was internally named Mozilla (Mosaic-Killer, Godzilla) by Jamie Zawinski.
Mozy – from the words "More Zetabytes for Your Mom". It was initially named "Breakaway Data Services for Your Mom," or "Bdsym".
MRF – from Madras Rubber Factory, founded by K M Mammen Mappillai in 1946. He started with a toy-balloon manufacturing unit at Tiruvottiyur, Chennai (then called Madras). In 1952 he began manufacturing tread-rubber and, in 1961, tyres.
MTM Enterprises – from the initials of the co-founder, actress Mary Tyler Moore
Musco Lighting – from the company's original location of Muscatine County, Iowa, where it still operates a large manufacturing facility
Mustek – Taiwanese electronics manufacturer with name derived from Most Unique Scanner Technology
MVC – from Music and Video Club, the name of a UK-based entertainment chain
N
Nabisco – The National Biscuit Company changed its name to Nabisco in 1971.
NAD Electronics – audio equipment manufacturer named for New Acoustic Dimension
Napster – original music-sharing service was named after co-founder Shawn Fanning's hairstyle-based nickname
NCR Corporation – from National Cash Register
NEC – from Nippon Electric Company
Nero – Nero Burning ROM named after Nero burning Rome ("Rom" is the German spelling of "Rome").
Nestlé – named after its founder, Henri Nestlé, who was born in Germany under the name "Nestle", which is German (actually, Swabian diminutive) for "bird's nest". The company logo is a bird's nest with a mother bird and two chicks.
Netscape – originally the product name of the company's web browser ("Mosaic Communications Netscape Web Navigator"). The company adopted the product name after the University of Illinois threatened to sue for trademark infringement over the use of the Mosaic name. Netscape is the combination of network and landscape.
Nike – named for the Greek goddess of victory
Nikon – original name was Nippon Kogaku, meaning "Japanese Optical"
Nintendo – Nintendo is the transliteration of the company's Japanese name, nintendou (任天堂). The first (nin) can be translated as to "entrusted"; ten-dou means "heaven".
Nissan – earlier known by the name Nippon Sangyo, which means "Japan Industries"
Nokia – started as a wood-pulp mill, the company expanded into producing rubber products in the Finnish town of Nokia. The company later adopted the town's name.
Nortel Networks – named from Nortel (Northern Telecom) and Bay Networks. The company was originally spun off from the Bell Telephone Company of Canada Ltd in 1895 as Northern Electric and Manufacturing, and traded as Northern Electric from 1914 to 1976.
Novartis – after the Latin expression "novae artes" which means something like "new skills"
Novell – Novell, Inc. was earlier Novell Data Systems co-founded by George Canova. The name was suggested by George's wife who mistakenly thought that "Novell" meant new in French. (Nouvelle is the feminine form of the French adjective 'Nouveau'. Nouvelle as a noun in French is 'news'.)
Nvidia (stylized as NVIDIA) – comes from "invidia" in Roman mythology; the Latin word for "envy".
O
OCZ – play on the word Overclockers
Olympus – Japanese company founded as Takachiho Seisakusho in 1919, where Takachiho referred to Takama-ga-hara, the home of the gods in Japanese mythology. It was renamed Olympus Optical Co., Ltd in 1949, after Mount Olympus, the home of the gods in Greek mythology, and then Olympus Corporation in 2003. The company had been using Olympus as a brand name for optical products such as microscopes since 1921.
Onkyo – translates as "sound harmony". The Japanese audio company was founded as Osaka Denki Onkyo K.K in 1946.
Ooyala – word Ooyala (ఉయ్యల) means 'cradle' in Telugu, as in a "cradle of innovation".
Oracle – Larry Ellison, Ed Oates and Bob Miner worked on a consulting project, code-named Oracle, for the CIA. The project was designed to use the new SQL database language from IBM. When the project was terminated, they decided to finish what they started and market it. Later they changed the name of their company, Relational Software Inc., to the name of the product.
Ornge – new name (2006) for Ontario Air Ambulance, chosen to reflect the orange color of its aircraft. It was intended to provide a unique branding but the ornge.com misspelling was already used by an advertising portal.
Osram – from osmium and wolfram
Össur – from the name of the founder, Icelandic entrepreneur Össur Kristinsson
P
Paccar – from Pacific Car and Rail
PCCW – originally Pacific Century Development, the company's English name was changed from Pacific Century CyberWorks Limited to PCCW Limited on 9 August 2002. It owns Hong Kong Telecom.
Pamida – U.S. retailer co-founded by Jim Witherspoon and named after his three sons: Patrick, Michael and David. Following a merger in 2012, Pamida's 175 stores were rebranded as Shopko Hometown stores or closed.
Panasonic – the giant Japanese electronics manufacturer was originally called Matsushita, after its founder, Kōnosuke Matsushita. In 2008, it was renamed Panasonic Corporation after the brand names it used for TV sales in the United States. National, its original global brand name, was not available in the United States and was abandoned.
Pemex – abbreviation of the full name of the state-owned Mexican oil/gasoline company, Petróleos Mexicanos (Spanish for Mexican Petroleum)
Pennzoil – formed by a merger of South Penn Oil (Penn), a former Standard Oil subsidiary, and Zapata Oil (zoil)
Penske Corporation – transportation company founded in 1969 by US racing driver Roger Penske.
Pepsi – named from the digestive enzyme pepsin
Pernod Ricard – French drinks company formed in 1975 with the merger of eponymous rivals founded by Henri-Louis Pernod and Paul Ricard
Petrobras – abbreviation of the Brazilian oil company's full name, Petróleo Brasileiro (Portuguese for Brazilian Petroleum)
Peugeot – in 1810, Jean-Pierre and Jean-Frédéric Peugeot diversified their family-run grain mill into a steel foundry. In 1896, after a family squabble, Armand Peugeot founded the Société des Automobiles Peugeot to focus on cars.
Pez – from the first, middle and last letters of the German language word "Pfefferminz", meaning "peppermint"
Philco – from the Philadelphia Storage Battery Company. The pioneering U.S. radio and television manufacturer was taken over by Ford and later by Philips.
Philips – Royal Philips Electronics was founded in 1891 by brothers Gerard (the engineer) and Anton (the entrepreneur) Philips
Piaggio – Italian manufacturer of Vespa scooters and cars was named after its founder, Rinaldo Piaggio.
Pioneer Corporation – In 1938, Nozomu Matsumoto, the son of a Christian missionary, founded Fukuin Shokai Denki Seisakusho ("Gospel Electric Works") to manufacture the A-8 loudspeaker, which he called "Pioneer". The company name was changed to the religiously neutral Pioneer Electronic Corporation in 1961, when it went public. In 1999, the company simplified its name by removing "Electronic".
Pixar – from pixel and the co-founder's name, Alvy Ray Smith. According to the biography "The Second Coming of Steve Jobs" by Alan Deutschman, the 'el' in pixel was changed to 'ar' because 'ar' is frequently used in Spanish verbs, implying the name means "To Pix". Alternatively, "pixarr" is a common abbreviation for "pixel array," an often used term in computer graphics programming.
PMC-Sierra – PMC from Pacific Microelectronics Centre, a research arm of BC Tel, and Sierra from the company that acquired it, Sierra Semiconductor, presumably so named because of the allure of the Sierra Nevada mountains to members of a California-based company.
Porsche – car company named after founder Ferdinand Porsche, an Austrian automotive engineer. The family name may have originated in the Czech name "Boreš" (boresh).
POW! Entertainment – American media production company co-founded by former Marvel Comics editor and publisher Stan Lee in 2001. POW! is commonly used in comic book fights, but it is used as an acroynm (or backronym) in the name POW! (Purveyors of Wonder) Entertainment, Inc.
Prada – an Italian high fashion house named after the founder Mario Prada, who founded Prada in Milan 1914
PricewaterhouseCoopers – global professional services firm named as a result of the merger of Price Waterhouse and Coopers & Lybrand in 1998. It started trading as PwC in 2010 without changing its legal name.
Procter & Gamble – named after the founders, William Procter, a candlemaker, and James Gamble, a soapmaker, who pooled their resources after marrying two sisters. The company was founded in Cincinnati in 1837.
ProfSat – Brazilian satellite-based education company, meaning Professional Sateliite
Proton – the Malaysian car manufacturer's name is derived from Perusahaan Otomobil Nasional, which means National Automobile Enterprise in the Malay language.
PRS Guitars – named after its founder, Paul Reed Smith.
Psion – UK computer company named by its founder, South Africa-born Dr David Potter, from Potter Scientific Instruments Or Nothing
Q
Q8 – acronym for these gas stations sounds like Kuwait, that is, the letter Q followed by the number 8. It is the abbreviation for Kuwait Petroleum International Limited.
Qantas – from its original name, Queensland and Northern Territory Aerial Services
Qimonda – invented name, where the company says: "In Chinese, 'Qi', pronounced as 'ch-ee', stands for breathing and flowing energy, while 'monda' denotes 'world' in Latin-based languages. 'Qi', when pronounced as a hard 'k', suggests 'key to the world', a positive connotation." It filed for insolvency on January 23, 2009.
Quad – acronym for Quality Unit Amplified Domestic. Quad Electroacoustics was founded in 1936 by Peter Walker, and was formerly called the Acoustical Manufacturing Company.
Quark – named after the subatomic particle. The word quark originates from Finnegans Wake by James Joyce.
Qualcomm – Quality Communication
Quora – faux plural of quorum, evocative of questions and answers
QVC – Quality, Value and Convenience
R
Rabobank – Raiffeisen-Boerenleenbank (Dutch for "Farmers Loan Bank"), a combination of the two cooperatives that merged to form the company
Raising Cane's Chicken Fingers – from "Raising Cane", a Labrador Retriever owned by chain founder Todd Graves when he opened his first restaurant in 1996
RAND – Research ANd Development.
Raytheon – "light of the gods"; maker of missiles such as Patriot, Maverick, Sidewinder and Tomahawk, among other military technology
RCA – Radio Corporation of America
Reckitt & Colman – named from the merger of Reckitt & Sons with J&J Colman in 1938. Colman's, best known for its mustard, was founded by Jeremiah Colman in 1814. Isaac Reckitt founded Reckitt & Sons in 1840.
Reckitt Benckiser – consumer goods giant named from the merger of Britain's Reckitt & Colman and the Dutch company Benckiser NV in December 1999. The latter was named after its founder, Johann Benckiser.
Red Hat – while at college, company founder Marc Ewing was given the Cornell lacrosse team cap (with red and white stripes) by his grandfather. People would turn to him to solve their problems and he was referred to as "that guy in the red hat". By the time he wrote the manual of the beta version of Red Hat Linux he had lost the cap, so the manual included an appeal to readers to return his Red Hat if found.
Reebok – alternate spelling of rhebok (Pelea capreolus), an African antelope
Renault – French car manufacturer founded in 1899 as Société Renault Frères (French for Renault Brothers) by Louis Renault and his brothers Marcel and Fernand.
REO Motor Car Company – car manufacturer founded in 1904 by Ransom E. Olds, and named from its founder's initials. Later, the rock band REO Speedwagon took its name from one of its trucks, the REO Speed Wagon.
Repsol – name derived from Refinería de Petróleo de eScombreras Oil (Escombreras is an oil refinery in Cartagena, Spain) and chosen for its euphony when the, then, state-owned oil company was incorporated in 1986. Previously Repsol was a lubricating-oil trademark.
Research in Motion – from the phrase "poetry in motion", which company founder Mike Lazaridis had seen used to describe a football player. The company changed its name to BlackBerry in 2013, after its most famous product.
Rickenbacker – named after co-founder Adolph Rickenbacher, with the spelling anglicised. The company started as the Electro String Instrument Corporation in 1931.
Rio Tinto - the Anglo-Australian multinational mining company’s name comes from the Rio Tinto (Red River) in southwestern Spain, which has flowed red since mining began there about 5000 years ago, due to acid mine drainage.
Robeez – baby-shoe company named after the founder's son Robbie (Robert) Robeez was taken over by Stride Rite in 2006.
Roche – healthcare company named after its founder, Fritz Hoffmann-La Roche. The compound surname was the result of Fritz Hoffmann marrying Adèle La Roche in 1895: it was a common practice in Switzerland at that time.
Roku – from the Japanese word 六 (roku) meaning "six", because it was the sixth company started by Anthony Wood.
Rolls-Royce – name used by Rolls-Royce plc and Rolls-Royce Motor Cars, among others. In 1884 Frederick Henry Royce started an electrical and mechanical business, making his first car, a Royce, in 1904. He was introduced to Charles Stewart Rolls on 4 May that year. The pair entered into a partnership in which Royce would manufacture cars to be sold exclusively by Rolls, and the cars would be called Rolls-Royce.
ROLM – named after the founders, Gene Richeson, Ken Oshman, Walter Loewenstern, and Robert Maxfield
RSA Security – formed from the first letters of the family names of its founders Ronald Rivest, Adi Shamir and Len Adleman
S
Saab – founded in 1937 in Sweden as Svenska Aeroplan aktiebolaget (Swedish Aeroplane Company); the last word is typically abbreviated as AB, hence Saab and Saab Automobile AB
Sabre – Semi-Automatic Business Research Environment
SAIC – Science Applications International Corporation
SAIC Motor – Shanghai Automotive Industry Corporation
Saku Brewery – after the Saku small borough, Estonia, where the company was founded
Samsonite – named from the Biblical character Samson, renowned for his strength
Sams Publishing – named after Howard W. Sams, who founded the company in 1946. It is now an imprint of Pearson PLC.
Samsung – meaning "three stars" in Korean
Santander – Banco Santander was founded in Spain in 1857 and named after the port of Santander in the north of Spain.
Sanyo – meaning "three oceans" in Japanese. The company was taken over by Panasonic in 2009 and the Sanyo brand name is no longer used.
SAP – SystemAnalyse und Programmentwicklung (German for "System analysis and program development"), a company formed by five ex-IBM employees who used to work in the 'Systems/Applications/Projects' group of IBM. Later, SAP was redefined to stand for Systeme, Anwendungen und Produkte in der Datenverarbeitung (Systems, Applications and Products in Data Processing).
SAS – Scandinavian Airlines System, the flag airline carrier of Sweden, Norway and Denmark
SAS Institute – originally an abbreviation for Statistical Analysis System
Sasol – Suid-Afrikaanse Steenkool en Olie. (Afrikaans for South African Coal and Oil)
Saudi Aramco – Aramco name was derived in 1944 when California Arabian Standard Oil Company (Casoc) changed its name to Arabian American Oil Company. The Saudi government purchased the company in 1980, and changed its name to Saudi Arabian Oil Company or Saudi Aramco in 1988.
Selver - from Estonian "selvehall" ("self-service market"), an earlier Estonian word for a "supermarket", and the noun suffix -r.
SCB – from Standard Chartered Bank. The name Standard Chartered comes from the two original banks from which it was founded – the Chartered Bank of Sri Lanka, Australia and China, and the Standard Bank of British South Africa.
Schick – manufacturer of shaving razors and blades, named after the inventor Jacob Schick
SCO – from Santa Cruz Operation. The company's office was in Santa Cruz, California. It eventually formed Tarantella, Inc. and sold off its operating system division to Caldera Systems, which is based in Utah. Caldera Systems changed its name to Caldera International and then to The SCO Group (at which point SCO no longer stood for anything).
SEAT – an acronym from Sociedad Española de Automóviles de Turismo (Spanish Corporation of Touring Cars)
Sealed Air – from the "sealed air" found in its most notable product, Bubble Wrap
Sears, Roebuck – named after its founders Richard Warren Sears and Alvah Curtis Roebuck in 1886, and taken over by Kmart in 2005. Sears Holdings now owns both Sears and Kmart.
Sega – Service Games of Japan was founded by Marty Bromley (an American) to import pinball games to Japan for use on American military bases.
Seiko – Seiko, now referred to in katakana as セイコー("seiko"), was originally named in kanji as 精工(also "seiko"). The two characters were taken from the phrase 「精巧で精密な時計の生産に成功する工場」, the company's vision which roughly translates to "a factory（工場:kojyo）that successfully（成功:seiko）produces（生産:seisan）exquisit（精巧:seiko）and precise（精密:seimitsu）watches". – According to Seiko's official company history, titled A Journey in Time: The Remarkable Story of Seiko (2003), Seiko is a Japanese word for "exquisite" or "minute" (both spelled 精巧), as well as a word for "success" (spelled 成功).
Sennheiser – named after one of its founders, Fritz Sennheiser.
SGI – Silicon Graphics Inc.
Sharp – Japanese consumer electronics company named from its first product, an ever-sharp pencil
Shell – Royal Dutch/Shell was established in 1907, when the Royal Dutch Petrol Society Plc. and the Shell Transport and Trading Company Ltd. merged their operations. The Shell Transport and Trading Company Ltd had been established at the end of the 19th century by commercial firm Samuel & Co (founded in 1830). Samuel & Co was already importing Japanese shells when it set up an oil company, so the oil company was named after the shells.
Siemens – founded in 1847 by Werner von Siemens and Johann Georg Halske. The company was originally called Telegraphen-Bau-Anstalt von Siemens & Halske.
Six Apart – company co-founders Ben and Mena Trott were born six days apart in September 1977. In 2011, the company was taken over by Infocom, a Japanese IT company.
Skanska – Swedish construction company named from Aktiebolaget Skånska Cementgjuteriet (Scania Cement Casting Ltd)
SKF – from Svenska Kullagerfabriken AB (Swedish ball bearing factory) founded in 1907; see also Volvo
Skoda Auto – car company was founded in 1895 and originally named Laurin & Klement after its founders, Vaclav Laurin and Vaclav Klement. It was taken over by Škoda Works, an industrial conglomerate, in 1924, and adopted the Škoda name from Emil Škoda. Škoda Auto was split off after World War II and is now part of Volkswagen.
Skype – original concept for the name was Sky-Peer-to-Peer, which morphed into Skyper, then Skype. The company was taken over by Microsoft in May 2011.
Smart – Swatch + Mercedes + Art
Smeg, Smalterie Metallurgiche Emiliane Guastalla (metal enamelling of Guastalla, Emilia)
Smilebit – former Sega development studio named from what they hope to make you do (smile), and the smallest unit of computer information (bit). The company developed Jet Set Radio.
SNK – Shin Nihon Kikaku, Japanese for "Plans for a New Japan"
Sony – from the Latin word 'sonus' meaning sound, and 'sonny' a slang word used by Americans to refer to a bright youngster, "since we were sonny boys working in sound and vision", said Akio Morita. The company was founded as Tokyo Tsushin Kogyo KK (Tokyo Telecommunications Engineering Corporation) in 1946, and changed its name to Sony in 1958. Sony was chosen as it could be pronounced easily in many languages.
Sorcim – "Micros" backwards. Sorcim was the original publisher of the SuperCalc spreadsheet in 1980. It was taken over by Computer Associates.
SPAR – originally DE SPAR, from Door Eendrachtig Samenwerken Profiteren Allen Regelmatig (Dutch, meaning "All will benefit from united co-operation"). "De spar" in Dutch translates as "the fir tree", hence the fir tree logo. As the company expanded across Europe, the name was shortened by dropping the article, "DE".
Sperry – company founded by Elmer Ambrose Sperry (1860–1930), originally as Sperry Gyroscope Company. Sperry took over Univac, and eventually was itself taken over by Burroughs. The merged companies became Unisys, from United Information Systems.
Spiratone – from the last name of founders Fred Spira and Hans Spira. The company was founded as Spiratone Fine Grain Laboratories. The "tone" suffix was common in the photographic industry (an example cited by Fred Spira is Royaltone) at the time of the company's founding in the 1940s.
Sprint – from its parent company, Southern Pacific Railroad INTernal Communications. At the time, pipelines and railroad tracks were the cheapest place to lay communications lines, as the right-of-way was already leased or owned.
SRAM Corporation – bicycle component manufacturer named from its founders Scott King, Stanley Ray Day, and Sam Patterson
SRI International – from Stanford Research Institute, established by the trustees of Stanford University, California
Stanley Works – name created to reflect the merger of Stanley's Bolt Manufactory of New Britain, Connecticut (founded by Frederick Trent Stanley) and the Stanley Rule and Level Company (founded by his cousin Henry Stanley)
Starbucks – named after Starbuck, a character in Herman Melville's novel Moby-Dick, also a variation of Starbo; at the time, a local mining camp north of Seattle.
Stellent – coined from a combination of the words stellar and excellent.
Sturm, Ruger – from its founders, Alexander McCormick Sturm and William B. Ruger.
STX – pronounced as the word "sticks" because, when first founded, STX manufactured only lacrosse sticks
Subaru – from the Japanese name for the constellation known to Westerners as Pleiades or the Seven Sisters. Subaru's parent company, Fuji Heavy Industries, was formed from a merger of six companies, and the constellation is featured on the company's logo.
Sumazi – social data intelligence company named after its Bangladeshi-American founder Sumaya Kazi.
Sun Microsystems – its founders designed their first workstation in their dorm at Stanford University, and chose the name Stanford University Network for their product, hoping to sell it to the college. They did not. The company was taken over by Oracle Corporation in 2010.
SuSE – from Software und System-Entwicklung (software and system development). The company was bought by Novell for its Linux distribution.
Suzuki – automotive giant named after its founder, Michio Suzuki. The company started as Suzuki Loom Works in Japan in 1909, and entered the motorcycle market in the early 1950s. It changed its name to Suzuki Motor Co., Ltd in 1954.
T
Taco Bell – named after founder Glen Bell
TAG Group (Holdings) S.A. – Luxembourg-based holding company named from Techniques d'Avant Garde
TAG Heuer – watch-maker named after Edouard Heuer, who founded Uhrenmanufaktur Heuer AG in Switzerland in 1860 It was taken over by TAG Group (Holdings) S.A. in 1985 and branded TAG Heuer in 1999. It is now owned by the LVMH (Louis Vuitton Moët Hennessy) conglomerate.
Talgo – from "Tren Articulado Ligero Goicoechea-Oriol" (Spanish for "Goicoechea-Oriol Light Articulated Train"), Goicoechea and Oriol being the founders of the company.
Tallink - from the Estonian capital Tallinn and the word "link" as the company links Tallinn with other cities by the sea.
Tama Drums – Tama was the name of the owner's wife, and means "jewel" in Japanese.
TAM Airlines – named from Transportes Aéreos Marília (Marilia's Air Transport). Marília is a city in São Paulo state, Brazil
TAP Portugal – from "Transportes Aéreos Portugueses" (Portuguese Air Transport).
Targray – a portmanteau of founder Thomas Andrew Richardson's initials and his mother's maiden name. (Gray)
Taser International – named after a fictional weapon, Thomas A. Swift's Electric Rifle, after the novel Tom Swift and His Electric Rifle by Victor Appleton. The company was incorporated in Arizona in 1993 by brothers Rick and Tom Smith as Air Taser, Inc.
Taxan – made-up name chosen partly because Takusan is a Japanese word for many or much and was considered propitious, but mainly because the head of the company, in the U.S. at the time, Tak Shimizu was known by everyone as Tak-san.
TCBY – originally, the company's name was "This Can't Be Yogurt", but a lawsuit from a competitor named "I Can't Believe It's Yogurt!" forced TCBY to create a new backronym for its initials: "The Country's Best Yogurt".
TCL – from Today China Lion. Derived from literal translation of "今日中国雄狮" from Chinese to English.
TDK Corporation – from Tokyo Denki Kagaku (Tokyo Electronics and Chemicals)
Textron – this U.S. defense conglomerate was founded as the Special Yarns Corporation in 1923 and later traded as Atlantic Rayon Corporation, when its main business was parachutes. After World War II, it moved into lingerie and other consumer goods, and needed a new name. The company history says: "Atlantic Rayon's advertising agency suggested Señorita Creations, but it was rejected in favor of Textron. The 'Tex' was derived from textiles and the 'tron' came from synthetics such as Lustron." Textron bought Bell Aerospace and the Cessna Aircraft Company, among many others.
TEPCO – Tokyo Electric Power Company
Tesco – founder Jack Cohen, who sold groceries in the markets of the London East End from 1919, acquired a large shipment of tea from T. E. Stockwell. He made new labels by using the first three letters of the supplier's name and the first two letters of his surname.
Tesla – Named after Serbian electrical engineer and physicist, Nikola Tesla. The Tesla Roadster uses an AC motor descended directly from Nikola Tesla's original 1882 design.
Teva Naot – outdoors shoe company is named after the modern Hebrew word for 'nature' (pronounced "tehvah")
Texaco – from The Texas Company U.S.A.
THX – from Tomlinson Holman Crossover, the name of the technology's inventor and the audio technology of a "crossover" amplifier. It may be a backronym, as the technology was created by George Lucas's then-company, Lucasfilm, and he directed THX 1138.
THY – Turkish Airlines. THY is the abbreviation of Türk Hava Yolları, which means Turkish Air Ways in Turkish.
TIBCO Software – The Information Bus Company. The company was founded by Vivek Ranadive as Teknekron Software Systems in 1985.
Tim Hortons – Canadian fast food doughnut, sandwich and coffee shop named after founder and hockey player Tim Horton. In Canada Tim Hortons is nicknamed "Tim's" and "Timmy's"; in America, the chain is nicknamed "Timmy Ho's". The name was changed from Tim Horton's, dropping the apostrophe, to preclude legal action in Quebec where businesses are obliged to use French language names.
TNT N.V. and TNT Express – Thomas Nationwide Transport, an Australian company which was acquired by the Dutch postal company in 1996. The postal company renamed itself TNT N.V. in 2005. In 2011, TNT N.V. demerged; the express delivery company took the name TNT Express while the postal company renamed itself PostNL.
Toshiba – named from the merger of consumer goods company Tokyo Denki (Tokyo Electric Co) and electrical firm Shibaura Seisaku-sho (Shibaura Engineering Works).
Toyota – from the name of the founder, Sakichi Toyoda. Initially called Toyeda, it was changed after a contest for a better-sounding name. The new name was written in katakana with eight strokes, a number that is considered lucky in Japan.
Trader Joe's – named after the grocery store's founder, Joe Coulombe
Tronc – In 2016, US-based media corporation Tribune Publishing changed its name to Tronc – short for Tribune online content. In 2018, the company changed it back.
Triang – operating name for Lines Bros Ltd, which was founded by William, Walter and Arthur Edwin Lines. Three Lines make a triangle
TSMC – Taiwan Semiconductor Manufacturing Company, an independent chip foundry founded in Taiwan in 1987.
Tucows – acronym for The Ultimate Collection Of Winsock Software.
Tungsram – derived from Tungsten + Wolfram, two variations of the name of the main raw material of the lamp production.
TVR – derived from the first name of the company founder TreVoR Wilkinson
TWA – derived from Trans World Airlines. Before the airline opened up its first international route from New York to Paris in the 1950s, it was a domestic operation that focused on serving Los Angeles and San Francisco from New York, operating under the name Transcontinental and Western Air. Keeping the initials and rebranding as a global airline was a stroke of marketing continuity genius.
Twinings – named after founder Thomas Twining, who set up a tea-shop on the Strand in London in 1706.
Twitter – having rejected the name Twitch for their social networking service, co-founder Jack Dorsey says: "we looked in the dictionary for words around it and we came across the word 'twitter' and it was just perfect. The definition was 'a short burst of inconsequential information', and 'chirps from birds'. And that's exactly what the product was."
U
UBS – named from the initials of the Union Bank of Switzerland, which merged with the Swiss Bank Corporation (SBC) in 1998. The initials no longer stand for anything, says the company, possibly because "United Bank of Switzerland" might be confused with the United Bank's subsidiary, United Bank Switzerland.
Umbro – Umbro was founded in 1924 by the Humphrey (Umphrey) Brothers, Harold C. and Wallace.
Unilever – name created to reflect the merger of Margarine Unie and Lever Brothers, agreed in 1929. Lever Brothers was named after its founders, William Hesketh Lever and his brother, James.
UNIMED – Brazilian cooperative of physicians, meaning União de Medicos (Physicians' Union)
Unisys – from United Information Systems, the new name for the company that resulted from the merging of two old mainframe computer companies, Burroughs and Sperry [Sperry Univac/Sperry Rand]. It united two incompatible ranges. The newborn Unisys was briefly the world's second-largest computer company, after IBM.
Unocal Corporation – the Union Oil Company of California, founded in 1890
UPS – United Parcel Service of America, Inc.
UUNET – one of the industry's oldest and largest Internet Service Providers, named from UNIX-to-UNIX Network
V
Vaisala – Finnish company named after its founder, Professor Vilho Väisälä
Valero Energy Corporation – from Misión San Antonio de Valero, the Spanish-language name of the mission in the company's home city better known as The Alamo
Valtra – from Valmet Tractors, where Valmet is the name of a Finnish state-owned company (originally "Valtion Metallitehtaat" – English: "State Metalworks")
Valve Corporation – game development company who uses a valve as symbolism, as in a lever which makes the flow of ideas readily accessible
Varig – Brazilian airline, its name is an abbreviation of Viação Aérea Rio-Grandense, because it was founded in the state of Rio Grande do Sul.
Verizon – portmanteau of veritas (Latin for truth) and horizon.
Verkkokauppa.com – directly from the company's official URL. "Verkkokauppa" translates to "Internet store" in Finnish.
Victorinox – derived from the name of the founder's mother, Victoria, and a French abbreviation for stainless steel, inox. Known for their Swiss army knife.
Viking Line – from the prefix "Viking" appearing in the names of all the ships of Rederi Ab Sally, Viking Line's predecessor company.
Virb – play on "verb", representing an action word in order to describe the product's users as "people who create"
Virgin – founder Richard Branson started a magazine called Student while still at school. In his autobiography, Losing My Virginity, Branson says that when they were starting a business to sell records by mail order, "one of the girls suggested: 'What about Virgin? We're complete virgins at business.'"
VMware – Virtual Machine [soft]ware
Vodafone – from Voice, Data, Telefone. Vodafone made the UK's first mobile call at a few minutes past midnight on 1 January 1985.
Volkswagen – from the German for "people's car". Ferdinand Porsche wanted to produce a car that was affordable for the masses – the Kraft-durch-Freude-Wagen (or "Strength-Through-Joy car", from a Nazi social organization) later became known, in English, as the Beetle.
Volvo – from the Latin word "volvo", which means "I roll". It was originally a name for a ball bearing being developed by SKF (Svenska Kullagerfabriken AB or, in English, Swedish ball bearing factory).
W
Wachovia – from the Latin version of the German wachau, the name given to a region in North Carolina by Moravian settlers because it reminded them of the Austrian valley of Wachau, through which the Danube River flows. Wachovia Bank was founded in Winston-Salem, North Carolina, which is located in the region.
Waitrose – upmarket UK supermarket chain originally named after the founders, Wallace Waite, Arthur Rose and David Taylor. The "Taylor" was later dropped.
Walgreens – named after founder Charles R. Walgreen, Sr.
Wal-Mart – named after founder Sam Walton
The Walt Disney Company – named for its co-founder Walt Disney
Wang Laboratories – from the name of the founder, An Wang, the inventor of core memory.
Wells Fargo – from the founders of the original Wells Fargo company, Henry Wells and William G. Fargo.(When Norwest Corporation purchased Wells Fargo in 1998, it chose to retain the Wells Fargo name.)
Wendy's – Wendy was the nickname of founder Dave Thomas' daughter Melinda.
Weta Digital – special effects company co-founded by The Lord of the Rings director Peter Jackson. Weta are a group of about 70 species of insect found in New Zealand, where Weta Digital is based.
W H Smith – founded by Henry Walton Smith and his wife Anna in London, England, in 1792. They named their small newsagent's shop after their son William Henry Smith, who was born the same year.
Williams-Sonoma – founded by Chuck Williams in Sonoma, California.
Wolfram Research – named after computer scientist Stephen Wolfram, who founded the company in 1987 before launching Mathematica software in 1988
Wonderware – from Wonderful Software - Wonderware was the project code name for the company prior to its launch. Upon making the company a legal entity, the code name was retained as the company name.
Worlds of Wonder – founder Don Kingsborough wanted an eyecatching stock symbol, and Worlds of Wonder provided WOW. The company went bankrupt in 1988.
WPP – global advertising and marketing company founded by Martin Sorrell in 1985. He bought an existing listed company, Wire & Plastic Products PLC, to use as a shell.
WWE – from the company's legal name of World Wrestling Entertainment, adopted in 2002; it began using the initialism as its trading name in 2011. The previous name of World Wrestling Federation (WWF), used since 1979, was changed after a court case brought by the World Wildlife Fund (WWF), which is now called the World Wide Fund for Nature.
X
Xerox – named from xerography, a word derived from the Greek xeros (dry) and graphos (writing). The company was founded as The Haloid Company in 1906, launched its first XeroX copier in 1949, and changed its name to Haloid Xerox in 1958.
Xiaomi – Xiaomi is the Chinese word for "millet".
XIX Entertainment – XIX is 19 in Roman numerals, so the company is named indirectly after Paul Hardcastle's single 19, and directly derived from 19 Entertainment – see above.
Xobni – "inbox", spelled backwards
Xstrata – name for a Swiss global mining and extraction company, formerly known as Sudelektra. The name is derived from the terms "extraction" and "strata" (sedimentary levels). The name was created in 1999 by John Lloyd of the design consultancy, Lloyd Northover.
XTO Energy – founded in 1986 as Cross Timbers Oil Company, it went public under the stock ticker XTO, and changed its name to XTO Energy Inc in 2001. It is now owned by ExxonMobil.
Y
Yahoo! – word Yahoo was invented by Jonathan Swift and used in his book Gulliver's Travels. It represents a person who is repulsive in appearance and barely human. Yahoo! founders David Filo and Jerry Yang jokingly considered themselves yahoos. It's also an interjection sometimes associated with United States Southerners' and Westerners' expression of joy, as alluded to in Yahoo.com commercials that end with someone singing the word "yahoo". It is also sometime jokingly referred to by its backronym, Yet Another Hierarchical Officious Oracle.
YKK – zipper manufacturer named from Yoshida Kogyo Kabushikikaisha (Yoshida Company Limited) after the founder, Tadao Yoshida. The letters YKK were stamped onto the zippers' pull tabs.
Yakult – official claims state that the name is derived from jahurto, an older form of jogurto, the Esperanto word for "yogurt". However, it has also been claimed that the name is derived from the fact that the product was developed from ancient Mongolian practices of culturing yak's milk in a sack made from a yak's stomach – the combination of Yak and Culture in English giving the product name as "Yakult".
Yamaha – after Torakusu Yamaha, who founded the company as Nippon Gakki Seizō Kabushiki Gaisha (Japan Musical Instrument Manufacturing Corporation) in 1897 after repairing a reed organ. The name was changed to Yamaha Corporation on 1 October 1987.
Yoplait – from the merger of Yola and Coplait in 1965
Z
Zamzar – based on the main character Gregor Samsa (Gregor Samsa) from Franz Kafka's story The Metamorphosis. Kafka describes a young man who is transformed whilst sleeping into a monstrous verminous bug. A version of the man's name was used as the basis for the company name because of its powerful association with change and transformation.
Zend Technologies – contraction derived from the names of Zeev Suraski and Andi Gutmans, the two founders
Zero Corporation – Founded by Herman Zierold as Zierold Metal Corporation, it is the parent company of Zero Halliburton. In 1952, when then owner Jack Gilbert noticed that many of the company's customers mispronounced and misspelled "Zierold" as "Zero," he changed the name of the company to Zero Manufacturing.
ZF Group – car parts manufacturer named from Zahnradfabrik, the German for Gear Factory.
Zimmer – named after Justin O. Zimmer, who co-founded the medical equipment company in Warsaw, Indiana, in 1927.
Zuse – pioneering German computer company named after its founder, Konrad Zuse (1910–1995). He built his first computer in his parents' living room at the end of the 1930s. Zuse was taken over by Siemens AG. The name is now supposedly echoed by SuSE (Software und System-Entwicklung: "Software and system development").
Zynga – named after founder Mark Pincus's American bulldog, Zinga
"""
f = open("wikipedia.txt", "w")
new_titles = []
loops = titles.split("\n")
for counter, text in enumerate(loops):
    head, sep, tail = text.partition(" – ")
    new_titles.append(head + "\n")
    f.write(head + "\n")

f.close()
