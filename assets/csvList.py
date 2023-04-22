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
inherentCsvSource = "https://raw.githubusercontent.com/anabeatrizzz/pi-quatro-univesp/master/data-bases-bkp/selected-datasets/deaths-from-hiv-by-age.csv"

csvList = [
    {
        "csvSource": "https://raw.githubusercontent.com/anabeatrizzz/pi-quatro-univesp/master/data-bases-bkp/selected-datasets/tb-related-deaths-hiv.csv",
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
        "csvSource": inherentCsvSource,
        "title": "Mortes relacionadas com HIV/AIDS em pessoas com menos de 5 anos",
        "yColumn": "Idade: Menor do que 5 anos",
        "newColumnsNames": inherentNewColumnsNames
    },
    {
        "csvSource": inherentCsvSource,
        "title": "Mortes relacionadas com HIV/AIDS em pessoas com mais do que 70 anos por ano",
        "yColumn": "Idade: Mais do que 70 anos",
        "newColumnsNames": inherentNewColumnsNames
    },
    {
        "csvSource": inherentCsvSource,
        "title": "Mortes relacionadas com HIV/AIDS em pessoas entre 5 a 14 anos por ano",
        "yColumn": "Idade: 5 a 14 anos",
        "newColumnsNames": inherentNewColumnsNames
    },
    {
        "csvSource": inherentCsvSource,
        "title": "Mortes relacionadas com HIV/AIDS em pessoas entre 15 a 49 anos por ano",
        "yColumn": "Idade: 15 a 49 anos",
        "newColumnsNames": inherentNewColumnsNames
    },
    {
        "csvSource": inherentCsvSource,
        "title": "Mortes relacionadas com HIV/AIDS em pessoas entre 50 a 69 anos por ano",
        "yColumn": "Idade: 50 a 69 anos",
        "newColumnsNames": inherentNewColumnsNames
    },
    {
        "csvSource": "https://raw.githubusercontent.com/anabeatrizzz/pi-quatro-univesp/master/data-bases-bkp/selected-datasets/tb-patients-tested-positive-for-hiv.csv",
        "title": "Pacientes que testaram positivo para HIV por ano",
        "yColumn": "Total de pacientes que testaram positivo para HIV",
        "newColumnsNames": {
            "Entity": "Entity",
            "Code": "Code",
            "Year": "Ano",
            "TB patients tested positive for HIV - Total": "Total de pacientes que testaram positivo para HIV"
        }
    },
    {
        "csvSource": "https://raw.githubusercontent.com/anabeatrizzz/pi-quatro-univesp/master/data-bases-bkp/selected-datasets/tb-patients-living-with-hiv-receiving-art.csv",
        "title": "Pacientes vivendo com HIV e que fazem terapia anti-retroviral por ano",
        "yColumn": "Total de pacientes vivendo com HIV que fazem terapia anti-retroviral",
        "newColumnsNames": {
            "Entity": "Entity",
            "Code": "Code",
            "Year": "Ano",
            "TB patients living with HIV receiving ART - Total": "Total de pacientes vivendo com HIV que fazem terapia anti-retroviral"
        }
    },
    {
        "csvSource": "https://raw.githubusercontent.com/anabeatrizzz/pi-quatro-univesp/master/data-bases-bkp/selected-datasets/life-expectancy.csv",
        "title": "Expectativa de vida de pessoas vivendo com HIV durante os anos",
        "yColumn": "Expectativa de Vida",
        "newColumnsNames": {
            "Entity": "Entity",
            "Code": "Code",
            "Year": "Ano",
            "Life expectancy": "Expectativa de Vida"
        }
    }
]
