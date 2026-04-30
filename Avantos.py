def computePolkadotScore(art):
    rows = art.split("\n")
    
    # locate the mouth - it's the widest () span on the face
    mx_start, mx_end = 0, 0
    for row in rows:
        i = 0
        while i < len(row):
            if row[i] == "(":
                j = row.find(")", i + 1)
                if j != -1 and (j - i) > (mx_end - mx_start):
                    mx_start, mx_end = i, j
            i += 1
        if mx_end > mx_start + 5:
            break

    # eyes are the row with exactly two back-to-back () pairs
    # each () = one pupil = 2 chars, so both = 4
    eye_chars = 0
    for row in rows:
        count, k = 0, 0
        while k < len(row) - 1:
            if row[k] == "(" and row[k+1] == ")":
                count += 1
                k += 2
            else:
                k += 1
        if count == 2:
            eye_chars = count * 2
            break

    # tally up the polkadots
    in_range, out_range = 0, 0
    for row in rows:
        for col, ch in enumerate(row):
            if ch == "O":
                if mx_start <= col <= mx_end:
                    in_range += 1
                else:
                    out_range += 1

    return out_range + in_range * eye_chars


art = """        ,   ,-',
        ,', ,'  ','  ,'   ÅÑGË£ÏÇÄ †(–)Ë ßRÄ†
      '-',  '      ,'
          ' -,    ',
              ' -, ',                                         , - - -,
             ('''''' ®'''''''')                        ,,,,,    ,-' -,''''''''',
              ` ~„''`„~ '                          ',  ,', -' , -,'' ''''''''',
                  \"„  \" - „                   „ - \",®,-'     `~~' '''''''
                 „\"         \" „         „ - \"      ,',,,',
               „-\" \" \" \" \" \" \" ~~~~~~\" - „       ,'
            „\" –,'' ~ ,       • ; •          \"      \"„
            \"\"\"\";      ' - , ,  ; , , , - '' ' ' -,_ ', ',
           , -' ' ',           ,'    ,'             ',~', ',
         ,'         ' - , ,()' /\\    ',          (),'¯ ,'   `¸`;
         ',                            ` ` ` ` ` `      ,-,,,-'
           '-,                                  ,¬  ,-'
              ' -, ~            ~~~~~~' ' ` ,-'
                  `~-,,,,,,,      ,,,,,,,,,,-~'
      ('('('(,,,              ;    ;                •Å(V)åö•
       '-, '-,'''      ,-';`,`'ˆˆˆˆˆ ,' ;' ' -,           •97•
         ;¯ ;      ;  ;  ', ; ; ,'  ;  ‚¸  ' -,        •••
         ;   ;     ;       '''''''''''    ``'-,',  ,'
         ;   ;, -¬;    O   O   O  O   '-',,,,,,,,,,,,
         ;        ;  O   O     O O    O  ,'     O     ,'
          ' - - ' `;    O        O  O    O   O    ,'
               ,-'   O    O    O  O      O    O   ,'
            ,-' O O  O   O        O        O ,'
         ,-'   O      O   O   O     O  O     ,'
      ,-'  O    O    O  O   O   O O O   O,-'-,
       ``¬ -,,,,,,,-¬~,~~~~~~~~~--',)  (' -,
                    ',   (',                     ' -,    '-,
                     ',)  (',                        `-,)  ' -,
                      ',    ',                           `-,  ,',-----,
                       ',)   ;                              `\\,- ---'
                   ¸,,,,'‡  (;
                  (¸,,,,,';_'\\ ßy §(V)òó†(–)775 ™"""

print(computePolkadotScore(art))