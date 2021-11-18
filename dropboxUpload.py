import dropbox

class TransferData:
    def __init__(self, access_token):
        self.access_token = access_token

    def upload_file(self, file_from, file_to):
        """upload a file to Dropbox using API v2
        """
        dbx = dropbox.Dropbox(self.access_token)

        with open(file_from, 'rb') as f:
            dbx.files_upload(f.read(), file_to)

def main():
    access_token = 'sl.A8ieLOxsuClYLLMzFv6YslyA5WetFa3EL9PCZRNsVYqmqDpFlIfJ098HU-ENiMwEOpXhbAOvIJGMjm7jWEUSTakknbXtGSVPLIOIj9zolpZOYmC4Jo2vfEKwO4kMeM6wvm-Wnkk'
    transferData = TransferData(access_token)

    file_from = input("Enter the file to transfer:- ")
    file_to = input("The full path to upload the file to, including the file name:-")

    # API v2
    transferData.upload_file(file_from, file_to)

    print("File has been moved successfully!!!!")

if __name__ == '__main__':
    main()