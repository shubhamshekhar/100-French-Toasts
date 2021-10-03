Step 1: Get most frequent used word from any one of the below link:
            https://github.com/hermitdave/FrequencyWords
            https://en.wiktionary.org/wiki/Wiktionary:Frequency_lists

Step 2: Format data using below code:
            import pandas
            data = pandas.read_csv("words.csv", sep=' ')
            data.drop('frequency', inplace=True, axis=1)
            data.to_csv("formatted_words.csv", encoding='utf-8', index=False)

Step 3: In spreadsheet in adjacent column, get translated word using below Spreadsheet function:
            =GOOGLETRANSLATE(columnName, lang1, lang2)

