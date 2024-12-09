import sys, os
from pathlib import Path

plugindir = Path.absolute(Path(__file__).parent)
paths = (".", "lib", "plugin")
sys.path = [str(plugindir / p) for p in paths] + sys.path
import webbrowser
import http.client
import json
from flowlauncher import FlowLauncher

class Foobar2000(FlowLauncher):
    def __init__(self):
        self.base_url = "localhost:8880"
        super().__init__()

    def query(self, query):
        if query == "play":
            self.send_command("/api/player/play")
            return [{"Title": "Playing", "SubTitle": "Foobar2000 is now playing", "IcoPath": "Images/app.png"}]
        elif query == "pause":
            self.send_command("/api/player/pause")
            return [{"Title": "Paused", "SubTitle": "Foobar2000 is paused", "IcoPath": "Images/app.png"}]
        elif query == "stop":
            self.send_command("/api/player/stop")
            return [{"Title": "Stopped", "SubTitle": "Foobar2000 is stopped", "IcoPath": "Images/app.png"}]
        elif query == "next":
            self.send_command("/api/player/next")
            return [{"Title": "Next", "SubTitle": "Playing next item", "IcoPath": "Images/app.png"}]
        elif query == "previous":
            self.send_command("/api/player/previous")
            return [{"Title": "Previous", "SubTitle": "Playing previous item", "IcoPath": "Images/app.png"}]
        else:
            return [{"Title": "Unknown command", "SubTitle": "Use play, pause, stop, next, or previous", "IcoPath": "Images/app.png"}]

    def send_command(self, endpoint):
        conn = http.client.HTTPConnection(self.base_url)
        payload = ""
        headers = {'Content-type': 'application/json'}
        try:
            conn.request("POST", endpoint, payload, headers)
            response = conn.getresponse()
            if response.status != 204:
                print(f"Error sending command to foobar2000: {response.status} {response.reason}")
        except Exception as e:
            print(f"Error sending command to foobar2000: {e}")
        finally:
            conn.close()

    def context_menu(self, data):
        return [
            {
                "Title": "Foobar2000 Plugin",
                "SubTitle": "Control foobar2000 from Flow Launcher",
                "IcoPath": "Images/app.png",
                "JsonRPCAction": {
                    "method": "open_url",
                    "parameters": ["https://github.com/your-repo/foobar2000-plugin"]
                }
            }
        ]

    def open_url(self, url):
        webbrowser.open(url)

if __name__ == "__main__":
    Foobar2000()