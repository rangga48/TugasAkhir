

def handle_uploaded_file(f, filename):
    with open('static/upload/'+filename, 'wb+') as destination:
        for chunk in f.chunks():
            destination.write(chunk)