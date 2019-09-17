from watchdog.observers import Observer
import time 
from watchdog.events import FileSystemEventHandler 
import os 
import shutil
# import json
 
class MyHandler(FileSystemEventHandler):
    i = 1
    def on_modified(self, event):
        print("")
        # print("Directory event")
        print('the directory is modified')
        time.sleep(5)

        for filename in os.listdir(folder_to_track):
            name, ext = os.path.splitext(filename)

            ext = ext[1:]

            new_dir = folder_to_track+'\\'+ext

            if ext == '': 
                continue 
            # elif ext == "part":
            #     continue

            if os.path.exists(new_dir):
    
                print("\nDirectory exists")
                print("moving " + filename + " to " + new_dir + '\\' + filename + " now.")
                shutil.move(os.path.join(folder_to_track + '\\',filename), os.path.join(new_dir + '\\', filename))
                print("Moving successful")

            elif not os.path.exists(new_dir): 
                os.makedirs(new_dir) 
                print("\nmoving " + filename + " to " + folder_to_track+'\\'+ext+'\\'+filename + " now.")
                shutil.move(os.path.join(folder_to_track + '\\',filename), os.path.join(new_dir + '\\', filename))
                print("Moving successful")

        

                     

if __name__ == "__main__":
    print("File Sorter 101")
    folder_to_track = r'D:\Users\Roy Matthew\Downloads'
    event_handler = MyHandler()
    observer = Observer()
    observer.schedule(event_handler,folder_to_track, recursive=False)
    observer.start()

    try:
        while True:
            time.sleep(10)
    except KeyboardInterrupt:
        observer.stop()
    observer.join()


