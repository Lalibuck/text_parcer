from google_drive_downloader import GoogleDriveDownloader as gdd

class ParsedText:
    def __init__(self, file, orig_name, transl_name):  # initializing the file
        self.file = file
        self.orig_name = orig_name   # English words
        self.transl_name = transl_name  # Russian words

    def parsing(self):
        with (open(self.file, 'r', encoding='utf-8') as parsing_file,
              open(self.orig_name, 'w', encoding='utf-8') as orig_file,
              open(self.transl_name, 'w', encoding='utf-8') as transl_file):
            parsing_file.seek(0)
            for line in parsing_file:
                if not line.startswith('#') and line != '\n':
                    orig, transl = line.split('\t')  # separation english and russian words
                    orig = set(orig.strip().split(' ; '))  # removing the repeating words
                    transl = set(transl.strip().split(' ; '))
                    for c in sorted(orig):
                        for w in sorted(transl):
                            orig_file.write(c + '\n')
                            transl_file.write(w + '\n')


file_id = '1Z08DG36-oDMokooOug2O0ejDKUxwS9T3'
file_name = './PythonTest.txt'

gdd.download_file_from_google_drive(file_id, file_name)  # downloading the file from Google Drive

python_test = ParsedText(file_name, 'English.txt', 'Russian.txt')
python_test.parsing()