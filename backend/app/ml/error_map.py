ERROR_MAP: dict[str, str] = {
    # Dental fricatives
    "θ_f":  "Use the tip of your tongue between your teeth for /θ/, as in 'think' — not the /f/ sound",
    "θ_t":  "Place your tongue between your teeth for /θ/, not behind them as in /t/ — try 'think'",
    "ð_v":  "Touch the tip of your tongue lightly to your upper teeth for /ð/, as in 'this' — not the /v/ sound",
    "ð_d":  "Your tongue rests between your teeth for /ð/, not behind them as in /d/ — try 'the'",
    # Approximants / labiodentals
    "w_v":  "Round your lips and use no teeth contact for /w/, as in 'wine' — /v/ requires upper teeth on lower lip",
    "v_b":  "Bring your upper teeth to your lower lip and let air through for /v/, as in 'vine' — /b/ is a lip stop",
    # Vowels
    "ɪ_iː": "Relax your tongue and jaw slightly for /ɪ/; it is shorter and laxer than /iː/ — as in 'bit' not 'beat'",
    "iː_ɪ": "Tense your tongue and extend /iː/ longer, as in 'beat' — not the short lax /ɪ/ of 'bit'",
    "æ_ɛ":  "Drop your jaw further for /æ/; it is more open than /ɛ/ — as in 'cat' not 'get'",
    "ɛ_æ":  "Raise your jaw slightly for /ɛ/; it is less open than /æ/ — as in 'bed' not 'bad'",
    "ʌ_ɑː": "The /ʌ/ vowel is short and central — as in 'cut', not the long back /ɑː/ of 'car'",
    "ʊ_uː": "Relax your lips for /ʊ/; it is shorter and laxer than /uː/ — as in 'book' not 'boot'",
    # Liquids
    "l_r":  "Place your tongue tip on the alveolar ridge for /l/, as in 'light' — do not curl it back",
    "r_l":  "Curl your tongue back without touching the palate for /r/, as in 'right' — do not let it touch",
    # Nasals
    "n_ŋ":  "The /n/ tongue tip touches the alveolar ridge — /ŋ/ is only at syllable ends as in 'sing'",
    "ŋ_n":  "Raise the back of your tongue to the soft palate for /ŋ/, as in 'sing' — not the front /n/",
    # Sibilants
    "s_ʃ":  "Keep your tongue further forward and spread your lips for /s/, as in 'sun' — not the rounded /ʃ/",
    "ʃ_s":  "Round your lips and pull your tongue back for /ʃ/, as in 'she' — not the spread /s/",
    "dʒ_ʒ": "Add a /d/ stop before the fricative for /dʒ/, as in 'jump' — not the smooth /ʒ/",
    "z_s":  "Voice /z/ by vibrating your vocal cords while keeping the same tongue position, as in 'zoo'",
}

# Errors typical of Spanish-speaking learners of English. Keys: "{target}_{produced}".
# Hints are written in Spanish.
ERROR_MAP_ES: dict[str, str] = {
    # Dental fricatives — inexistentes en español
    "θ_s":  "Para /θ/ (como en 'think'), coloca la punta de la lengua entre los dientes y deja salir el aire — no uses el sonido /s/",
    "θ_t":  "Para /θ/, la lengua debe asomarse entre los dientes, no apoyarse detrás de ellos como en /t/ — practica con 'think'",
    "ð_d":  "El sonido /ð/ (como en 'the') se produce con la lengua entre los dientes dejando vibrar las cuerdas vocales — no es la /d/ española",
    # Fricativa labiodental sonora
    "v_b":  "Para /v/, apoya los dientes superiores en el labio inferior y deja salir el aire con vibración — no cierres los labios como en /b/",
    # Vocal central breve vs. /a/ española
    "æ_a":  "El sonido /æ/ (como en 'cat') requiere la mandíbula más abierta y la lengua avanzada — es más abierto que la /a/ española",
    "ʌ_a":  "El sonido /ʌ/ (como en 'cut') es breve y central; la lengua está relajada y la mandíbula, semiabierta — diferente de la /a/ española",
    # Vocales laxas vs. vocales tensas españolas
    "ɪ_iː": "El sonido /ɪ/ (como en 'bit') es más breve y relajado que la /i/ española — no lo alargues ni tenses la lengua",
    "ʊ_uː": "El sonido /ʊ/ (como en 'book') es más breve y relajado que la /u/ española — relaja los labios y no lo alargaras",
    # Nasal velar
    "ŋ_n":  "Para /ŋ/ (como en 'sing'), eleva la parte posterior de la lengua hacia el velo del paladar — no toques la zona alveolar como en /n/",
    # Fricativa glotal
    "h_x":  "El sonido /h/ inglés (como en 'hello') es suave y solo de aire; evita la /x/ fuerte del español (como en 'jota')",
    # Fricativa alveopalatal sonora
    "ʒ_ʃ":  "Para /ʒ/ (como en 'measure'), vibra las cuerdas vocales mientras produces el sonido — es la versión sonora de /ʃ/",
    # Semivocal vs. bilabial
    "w_b":  "Para /w/ (como en 'wine'), redondea los labios sin cerrarlos ni rozarlos — no uses el cierre bilabial de /b/",
    # Fricativa alveolar sorda: español no tiene /z/
    "z_s":  "El sonido /z/ (como en 'zoo') es igual que /s/ pero con vibración de las cuerdas vocales — mantén la misma posición de lengua y añade voz",
    # Africada vs. fricativa
    "dʒ_ʒ": "Para /dʒ/ (como en 'jump'), añade un cierre /d/ justo antes del sonido fricativo — no empieces directamente con la fricción",
}
