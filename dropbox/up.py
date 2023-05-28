import dropbox
import os
from dropbox.files import WriteMode

class TransferData:
    def __init__(self, accessToken):
        self.accessToken = accessToken

    def uploadFile(self, fileFrom, fileTo):
        dbx = dropbox.Dropbox(self.accessToken)

        for root, dirs, files in os.walk(fileFrom):

            for filename in files:

                local_path = os.path.join(root, filename)
                
                relative_path = os.path.relpath(local_path, fileFrom)
                dropbox_path = os.path.join(fileTo, relative_path)
                with open(local_path, 'rb') as f:
                    dbx.files_upload(f.read(), dropbox_path, mode=WriteMode('overwrite'))

def main():
    accessToken = 'mytA54CC06AAAAAAAAAAPqR-ZsukeIl6iOFNjVmCwAk'
    transferData1 = TransferData(accessToken)
    
    fileFrom = input("Please enter the file path of which you want to transfer: ")
    fileTo = input("Please enter the path of the destination in dropbox: ")

    transferData1.uploadFile(fileFrom, fileTo)
    print("Your files have been uploaded succesfully!")

main()
