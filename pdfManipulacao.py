from pathlib import Path
from glob import glob
# PASTAS 
dowloadPdf = Path("C:/Users/marco/Desktop/AutomaMP/ManipulaDowload-WebScrapin/DowloadPdf")
contaPaga = Path("C:/Users/marco/Desktop/AutomaMP/ManipulaDowload-WebScrapin/ContaPaga")
contaAtrasada = Path("C:/Users/marco/Desktop/AutomaMP/ManipulaDowload-WebScrapin/ContaAtrasada")

def manipulaPdf ():

    for pdf_conta in dowloadPdf.glob("*.pdf"):
        with open(pdf_conta) as arquivo_pdf:
            print(arquivo_pdf)
            pdf_conta in dowloadPdf.glob("*.pdf")
            file_name = pdf_conta.stem
            file_ext = pdf_conta.suffix
            conta_formatada = file_name + '-PAGA' + file_ext
            new_path = contaPaga / conta_formatada
            with open(pdf_conta, 'rb') as old_file:
                with open(new_path, 'wb') as new_file:
                    new_file.write(old_file.read())
        pdf_conta.unlink()

def manipulaZip ():
    for zip_file in dowloadPdf.glob("*.zip"):
        with open(zip_file) as arquivo_zip:
            print(arquivo_zip)
            zip_file in dowloadPdf.glob("*.zip")
            file_name = zip_file.stem
            file_ext = zip_file.suffix
            zip_formatado = file_name + '-PAGA' + file_ext
            new_path = contaAtrasada / zip_formatado
            with open(zip_file, 'rb') as old_file:
                with open(new_path, 'wb') as new_file:
                    new_file.write(old_file.read())   
        zip_file.unlink() 
