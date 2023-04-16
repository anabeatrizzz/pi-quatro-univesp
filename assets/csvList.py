inherentNewColumnsNames = {
            "Entity": "Entity",
            "Code": "Code",
            "Year": "Ano",
            "Deaths - HIV/AIDS - Sex: Both - Age: Under 5 (Number)": "Idade: Menor do que 5 anos",
            "Deaths - HIV/AIDS - Sex: Both - Age: 70+ years (Number)": "Idade: Mais do que 70 anos",
            "Deaths - HIV/AIDS - Sex: Both - Age: 5-14 years (Number)": "Idade: 5 a 14 anos",
            "Deaths - HIV/AIDS - Sex: Both - Age: 15-49 years (Number)": "Idade: 15 a 49 anos",
            "Deaths - HIV/AIDS - Sex: Both - Age: 50-69 years (Number)": "Idade: 50 a 69 anos"
        }

csvList = [
    {
        "csvSource": "https://raw.githubusercontent.com/anabeatrizzz/pi-quatro-univesp/master/tb-related-deaths-hiv.csv",
        "title": "Mortes estimadas relacionadas à tuberculose entre pessoas vivendo com HIV por ano",
        "yColumn": "Mortes estimadas",
        "newColumnsNames": {
            "Entity": "Entity",
            "Code": "Code",
            "Year": "Ano",
            "Estimated TB-related deaths among people living with HIV - estimate": "Mortes estimadas"
        }
    },
    {
        "csvSource": "https://raw.githubusercontent.com/anabeatrizzz/pi-quatro-univesp/master/deaths-from-hiv-by-age.csv",
        "title": "Mortes relacionadas com HIV/AIDS em pessoas com menos de 5 anos",
        "yColumn": "Idade: Menor do que 5 anos",
        "newColumnsNames": inherentNewColumnsNames
    },
    {
        "csvSource": "https://raw.githubusercontent.com/anabeatrizzz/pi-quatro-univesp/master/deaths-from-hiv-by-age.csv",
        "title": "Mortes relacionadas com HIV/AIDS em pessoas com mais do que 70 anos por ano",
        "yColumn": "Idade: Mais do que 70 anos",
        "newColumnsNames": inherentNewColumnsNames
    },
    {
        "csvSource": "https://raw.githubusercontent.com/anabeatrizzz/pi-quatro-univesp/master/deaths-from-hiv-by-age.csv",
        "title": "Mortes relacionadas com HIV/AIDS em pessoas entre 5 a 14 anos por ano",
        "yColumn": "Idade: 5 a 14 anos",
        "newColumnsNames": inherentNewColumnsNames
    },
    {
        "csvSource": "https://raw.githubusercontent.com/anabeatrizzz/pi-quatro-univesp/master/deaths-from-hiv-by-age.csv",
        "title": "Mortes relacionadas com HIV/AIDS em pessoas entre 15 a 49 anos por ano",
        "yColumn": "Idade: 15 a 49 anos",
        "newColumnsNames": inherentNewColumnsNames
    },
    {
        "csvSource": "https://raw.githubusercontent.com/anabeatrizzz/pi-quatro-univesp/master/deaths-from-hiv-by-age.csv",
        "title": "Mortes relacionadas com HIV/AIDS em pessoas entre 50 a 69 anos por ano",
        "yColumn": "Idade: 50 a 69 anos",
        "newColumnsNames": inherentNewColumnsNames
    },

]