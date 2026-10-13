"""Format constants, static lists, and threshold definitions for EDH analysis."""

# Fast Mana: Net-Positive & Immediate Ramp Staples
FAST_MANA_CARDS = {
    "Sol Ring", "Mana Crypt", "Lotus Petal", "Chrome Mox", "Mox Diamond",
    "Mox Opal", "Mana Vault", "Grim Monolith", "Ancient Tomb",
    "Gemstone Caverns", "Dark Ritual", "Pyretic Ritual", "Seething Song",
    "Cabal Ritual", "Elvish Spirit Guide", "Simian Spirit Guide", "Jeweled Lotus"
}

# Commander Format Panel (CFP) 53 Tracked "Game Changers" Staples
GAME_CHANGERS = {
    # Fast Mana & Explosive Acceleration
    "Mana Crypt", "Sol Ring", "Jeweled Lotus", "Mana Vault", "Grim Monolith",
    "Ancient Tomb", "Dockside Extortionist", "Chrome Mox", "Mox Diamond",
    # Free Spells & Extreme Interaction
    "Force of Will", "Fierce Guardianship", "Deflecting Swat", "Deadly Rollick",
    "Pact of Negation", "Flusterstorm", "Mindbreak Trap", "Cyclonic Rift",
    # Elite Card Advantage & Rhystic Engines
    "Rhystic Study", "Mystic Remora", "The One Ring", "Esper Sentinel",
    "Smothering Tithe", "Sylvan Library", "Necropotence", "Bolas's Citadel",
    "Ad Nauseam", "Trouble in Pairs",
    # Unconditional & Hyper-Efficient Tutors
    "Demonic Tutor", "Vampiric Tutor", "Imperial Seal", "Mystical Tutor",
    "Worldly Tutor", "Enlightened Tutor", "Gamble", "Intuition",
    # Format-Warpiing Stax & Lock Pieces
    "Drannith Magistrate", "Opposition Agent", "Dauthi Voidwalker", "Orcish Bowmasters",
    "Grand Arbiter Augustin IV", "Winter Orb", "Static Orb", "Trinisphere",
    # Compact Win-Conditions & Extinction Engines
    "Thassa's Oracle", "Underworld Breach", "Food Chain", "Aetherflux Reservoir",
    "Peer into the Abyss", "Toxic Deluge", "Farewell", "Torment of Hailfire"
}

# Hard Stax & Lock Pieces (Oppression / Turn-Denial)
HARD_STAX_PIECES = {
    "Drannith Magistrate", "Rule of Law", "Eidolon of Rhetoric", "Archon of Emeria",
    "Deafening Silence", "Spirit of the Labyrinth", "Aven Mindcensor", "Winter Orb",
    "Static Orb", "Stasis", "Trinisphere", "Armageddon", "Ravages of War",
    "Hokori, Dust Drinker", "Back to Basics", "Blood Moon", "Magus of the Moon",
    "Contamination", "Opposition Agent", "Grand Arbiter Augustin IV", "Humility",
    "The Tabernacle at Pendrell Vale"
}

# Local Fallback Combo Database (Card Pair -> Description)
STAPLE_COMBOS = [
    ({"Sanguine Bond", "Exquisite Blood"}, "Sanguine Bond + Exquisite Blood -> Infinite life drain & life gain"),
    ({"Kiki-Jiki, Mirror Breaker", "Combat Celebrant"}, "Kiki-Jiki + Combat Celebrant -> Infinite combat steps & tokens"),
    ({"Dualcaster Mage", "Ghostly Flicker"}, "Dualcaster Mage + Ghostly Flicker -> Infinite mana & magecraft triggers"),
    ({"Dualcaster Mage", "Twinflame"}, "Dualcaster Mage + Twinflame -> Infinite hasty Dualcaster tokens"),
    ({"Heliod, Sun-Crowned", "Walking Ballista"}, "Heliod + Walking Ballista -> Infinite ping damage"),
    ({"Thassa's Oracle", "Demonic Consultation"}, "Thassa's Oracle + Demonic Consultation -> Instant library exile win"),
    ({"Thassa's Oracle", "Tainted Pact"}, "Thassa's Oracle + Tainted Pact -> Instant library exile win"),
    ({"Isochron Scepter", "Dramatic Reversal"}, "Isochron Scepter + Dramatic Reversal -> Infinite mana & noncreature cast triggers"),
    ({"Gravecrawler", "Phyrexian Altar"}, "Gravecrawler + Phyrexian Altar -> Infinite sacrifice & death loop with any Zombie"),
    ({"Pitiless Plunderer", "Gravecrawler", "Carrion Feeder"}, "Pitiless Plunderer + Gravecrawler + Carrion Feeder -> Infinite mana & death triggers"),
    ({"Pitiless Plunderer", "Gravecrawler", "Viscera Seer"}, "Pitiless Plunderer + Gravecrawler + Viscera Seer -> Infinite scry, mana & death triggers"),
    ({"Forsaken Miner", "Phyrexian Altar"}, "Forsaken Miner + Phyrexian Altar -> Infinite death loop whenever opponent loses life")
]

# Archetype Dynamic Weight Matrix
ARCHETYPE_WEIGHTS = {
    "Cheat / Aggro Tempo": {
        "w_vel": 0.25, "w_eng": 0.25, "w_int": 0.10, "w_res": 0.05,
        "w_resi": 0.10, "w_clos": 0.15, "w_mana": 0.10
    },
    "Spellslinger / Storm": {
        "w_vel": 0.25, "w_eng": 0.20, "w_int": 0.20, "w_res": 0.05,
        "w_resi": 0.05, "w_clos": 0.15, "w_mana": 0.10
    },
    "Aristocrats / Sacrifice": {
        "w_vel": 0.10, "w_eng": 0.30, "w_int": 0.10, "w_res": 0.10,
        "w_resi": 0.15, "w_clos": 0.15, "w_mana": 0.10
    },
    "Big Mana / Landfall": {
        "w_vel": 0.10, "w_eng": 0.15, "w_int": 0.10, "w_res": 0.35,
        "w_resi": 0.05, "w_clos": 0.15, "w_mana": 0.10
    },
    "Control / Stax": {
        "w_vel": 0.10, "w_eng": 0.20, "w_int": 0.30, "w_res": 0.10,
        "w_resi": 0.15, "w_clos": 0.05, "w_mana": 0.10
    },
    "Voltron / Equipment": {
        "w_vel": 0.15, "w_eng": 0.25, "w_int": 0.10, "w_res": 0.10,
        "w_resi": 0.15, "w_clos": 0.15, "w_mana": 0.10
    },
    "Midrange / Engine Value": {
        "w_vel": 0.15, "w_eng": 0.20, "w_int": 0.15, "w_res": 0.15,
        "w_resi": 0.10, "w_clos": 0.15, "w_mana": 0.10
    }
}

# Official Commander Format Panel (CFP) 5-Bracket System Definitions
BRACKET_DEFINITIONS = {
    1: {
        "label": "Bracket 1: Exhibition (Ultra-Casual / Theme)",
        "description": "Purely expressive, artistic, or narrative builds with zero Game Changers, no extra turns, and no infinite combos.",
        "power_min": 1.0,
        "power_max": 3.4
    },
    2: {
        "label": "Bracket 2: Core (Precon / Standard Casual)",
        "description": "Standard preconstructed decks and battlecruiser casual builds. Straightforward combat, no Game Changers, no 2-card infinites.",
        "power_min": 3.5,
        "power_max": 5.4
    },
    3: {
        "label": "Bracket 3: Upgraded (Tuned Casual)",
        "description": "Focused synergies and upgraded precons. Up to 3 Game Changers permitted; compact 2-card infinites and chained extra turns restricted.",
        "power_min": 5.5,
        "power_max": 6.9
    },
    4: {
        "label": "Bracket 4: Optimized (High-Power Casual)",
        "description": "Optimized high-power casual. Uncapped Game Changers, fast mana, efficient combos, and high-velocity engines, distinct from tournament cEDH.",
        "power_min": 7.0,
        "power_max": 8.4
    },
    5: {
        "label": "Bracket 5: cEDH (Competitive Commander)",
        "description": "Format ceiling and tournament competitive play. Unrestricted speed (turn 1-3 win/lock threat), maximum density of free interaction and fast mana.",
        "power_min": 8.5,
        "power_max": 10.0
    }
}
