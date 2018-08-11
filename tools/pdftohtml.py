from subprocess import call

def pdftohtml(file):
    """
    Converte um arquivo pdf para outro 
    """
    cmd = "pdftohtml -noframes -s -i {}".format(file)
    call(cmd, shell = True)
    return True