from ya_disk import YaUploader

if __name__ == '__main__':

    TOKEN = ""
    uploader = YaUploader(token=TOKEN)
    result = uploader.upload_file_to_disk("netology/test.txt", "test.txt")