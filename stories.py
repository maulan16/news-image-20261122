"""The day's stories for the 22 November 2026 broadsheet.

Every line is a plain, sourced summary of news reported on Sunday 22 November 2026
(Reuters, AP, BBC, Guardian, Al Jazeera, France 24, DW and others, as gathered on
the day). Numbers are copied as reported; anything still unsettled is labelled so.
"""

DATE_LINE = "SUNDAY 22 NOVEMBER 2026"

HEROES = [
    {
        "kicker": "UKRAINE",
        "head": "Russian drone collapses Kyiv-region apartment block",
        "deck": "Part of a five-storey building in Dymer fell on Sunday morning; at least 14 "
                "people missing, 9 rescued, fire contained, Zelensky says.",
        "art": "building",
    },
    {
        "kicker": "CLIMATE  COP31",
        "head": "COP31 final draft leaves out 'fossil fuels'",
        "deck": "Talks in Antalya ran into a second day of overtime. The text admits warming will "
                "pass 1.5\u00b0C, drops the $120bn adaptation figure; approval still pending.",
        "art": "thermo",
    },
]

# region -> (accent colour, list of one-or-two line headlines)
REGIONS = [
    ("EUROPE", (24, 64, 120), [
        "Drone-hit Russian ship Sparta II burns in Finnish waters",
        "Kryvyi Rih missile strike kills 2, including a child; 58 hurt",
        "NATO calls emergency council for Monday after missiles fell in Poland",
        "Denmark expels Russian attach\u00e9 over alleged murder plot",
        "Estonia to close its border with Russia next month",
        "Princess of Wales says she is in remission from cancer",
        "Belgium: Monday strike expected to cancel all flights",
        "Cost-of-living protests in France and Portugal",
        "Costa proposes smaller 2028-34 EU budget with 3% digital tax",
    ]),
    ("MIDDLE EAST", (150, 60, 20), [
        "Iran starts rationing electricity as US blockade passes 130 days",
        "Iran strikes Bahrain's Sitra industrial area; two tankers hit near Hormuz",
        "Houthis fire missiles at Riyadh; three intercepted",
        "Gaza City: Israeli drone hits food van, 3 killed",
        "West Bank settlers set 12 vehicles on fire",
        "Fire at Basra's Hartha power station kills at least 4",
        "Lebanon's Aoun says Israel and Iran threaten sovereignty",
        "Swimmer Lewis Pugh crosses 15 km of the Strait of Hormuz",
    ]),
    ("ASIA-PACIFIC", (160, 30, 40), [
        "South Korea's education minister resigns over AI exam-cheating scandal",
        "Indonesia: candy factory fire in Banten, at least 3 dead, dozens missing",
        "EU and Indonesia sign trade deal removing most tariffs",
        "Nepal PM Balendra Shah begins visit to India",
        "Hong Kong votes for its 1,500-member Election Committee",
        "Fake liquor kills at least 11 in India's Manipur",
        "Bangladesh: about 80 garment factories shut amid wage sit-ins",
        "Mongolia prepares snap presidential election",
        "Cyclone Xavier weakens; everyone on Cook Islands' Nassau safe",
    ]),
    ("AMERICAS", (30, 110, 70), [
        "Mexico captures cartel boss 'El Chapo Isidro' in Sinaloa",
        "FBI investigates hack of NCIC national crime database",
        "Bolsonaro in intensive care with bowel obstruction",
        "Argentina approves $50bn YPF LNG export project",
        "Jury convicts man of starting the 2025 Palisades fire",
        "ICE arrests on Seattle airport jet bridge spark outcry",
        "Trump orders contractors to report congressional requests",
        "Haiti and El Salvador agree to build three prisons",
    ]),
    ("AFRICA", (180, 120, 0), [
        "Nigeria: boat carrying funeral mourners capsizes in Bayelsa, 24 dead",
        "South Africa's first woman deputy president, Phumzile Mlambo-Ngcuka, dies at 71",
        "Five EU countries agree deportation centres with Rwanda",
        "Zimbabwe author cleared of using AI for prize-winning story",
        "Tanzania fight back to draw 2-2 with Costa Rica at U17 World Cup",
    ]),
    ("SCIENCE  TECH  WORLD", (90, 50, 130), [
        "ESA-JAXA probe BepiColombo enters orbit around Mercury",
        "UN talks in Geneva on AI weapons end without binding rules",
        "One-time CRISPR infusion cuts 'bad' cholesterol by 52% in trial",
        "Mathematician says Claude AI helped him prove Riemann hypothesis",
        "Whale genome sequenced from breath collected by drone",
        "Pilotless air taxi carries a passenger in Japan",
        "Shuri Castle main hall in Okinawa restored, 7 years after fire",
    ]),
    ("SPORT", (40, 40, 40), [
        "Verstappen wins the Las Vegas Grand Prix",
        "Alcaraz beats Shelton, meets Zverev in ATP Finals final",
        "Gukesh v Sindarov world chess title match opens in Geneva",
        "Kansas City Current win first NWSL title, 2-1 v Spirit",
        "Wembanyama scores 50; Harden's 51 passes Kobe",
        "England beat All Blacks; France reach Nations final",
        "Cricket: India declare on 720/9 against New Zealand",
    ]),
]

SOURCES_NOTE = ("All items reported on 22 Nov 2026 by Reuters, AP, BBC, Guardian, Al Jazeera, "
                "France 24, DW, Euronews, SCMP and others. Tolls are as first reported; "
                "COP31 text was not yet adopted at press time.")

# Market close figures as reported on 22 Nov 2026 (last trading session).
MARKETS = [
    ("S&P 500", "6,910", "-3.7%"),
    ("NIKKEI", "", "-5.06%"),
    ("FTSE 100", "10,346", "-1.02%"),
    ("SENSEX", "", "+2.3%"),
    ("BRENT", "$89.95", "+0.6%"),
    ("GOLD", "$3,515", "-4.62%"),
    ("US 10Y", "4.91%", ""),
]
MARKETS_NOTE = "AI SELLOFF HITS WORLD STOCKS"
