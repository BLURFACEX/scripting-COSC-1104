import os
import time
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler
from googleapiclient.discovery import build
from googleapiclient.http import MediaFileUpload
from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials

# Authenticate with Google Drive API
def authenticate_google_drive():
    creds = None
    if os.path.exists('token.json'):
        creds = Credentials.from_authorized_user_file('token.json')
    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())
        else:
            raise Exception("Token file missing or invalid. Run initial authentication.")
    return build('drive', 'v3', credentials=creds)

# Upload file to Google Drive
def upload_file_to_drive(service, file_path, folder_id=None):
    file_name = os.path.basename(file_path)
    media = MediaFileUpload(file_path)
    file_metadata = {"name": file_name}
    if folder_id:
        file_metadata["parents"] = [folder_id]
    service.files().create(body=file_metadata, media_body=media).execute()
    print(f"Uploaded: {file_name}")

# Folder event handler
class FolderMonitorHandler(FileSystemEventHandler):
    def __init__(self, service, drive_folder_id):
        self.service = service
        self.drive_folder_id = drive_folder_id

    def on_created(self, event):
        if not event.is_directory:
            upload_file_to_drive(self.service, event.src_path, self.drive_folder_id)

    def on_modified(self, event):
        if not event.is_directory:
            upload_file_to_drive(self.service, event.src_path, self.drive_folder_id)

# Start monitoring a folder
def start_monitoring(folder_path, drive_folder_id=None):
    service = authenticate_google_drive()
    event_handler = FolderMonitorHandler(service, drive_folder_id)
    observer = Observer()
    observer.schedule(event_handler, folder_path, recursive=True)
    observer.start()
    print(f"Monitoring folder: {folder_path}")
    try:
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        observer.stop()
    observer.join()
