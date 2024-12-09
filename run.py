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
        song_info = self.get_current_song()
        artwork_url = self.get_current_artwork()
        if query == "play":
            
            self.send_command("/api/player/play")
            return [{"Title": "Playing", "SubTitle": song_info + " is now playing", "IcoPath": artwork_url}]
        elif query == "pause":
            
            self.send_command("/api/player/pause")
            return [{"Title": "Paused", "SubTitle": song_info + " is paused", "IcoPath": artwork_url}]
        elif query == "toggle":
            
            self.send_command("/api/player/pause/toggle")
            return [{"Title": "Paused", "SubTitle": "Toggled audio for " + song_info, "IcoPath": artwork_url}]
        elif query == "stop":
            
            self.send_command("/api/player/stop")
            return [{"Title": "Stopped", "SubTitle": "Stopped playing " + song_info, "IcoPath": artwork_url}]
        elif query == "next":
            self.send_command("/api/player/next")
            return [{"Title": "Next", "SubTitle": "Playing next item", "IcoPath": artwork_url}]
        elif query == "previous":
            self.send_command("/api/player/previous")
            return [{"Title": "Previous", "SubTitle": "Playing previous item", "IcoPath": artwork_url}]
        elif query == "current":
            
            return [{"Title": "Current Song", "SubTitle": song_info, "IcoPath": artwork_url}]
        else:
            return [{"Title": "Unknown command", "SubTitle": "Use play, pause, toggle, stop, next, previous or current", "IcoPath": "Images/app.png"}]

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

    def get_current_song(self):
        conn = http.client.HTTPConnection(self.base_url)
        try:
            conn.request("GET", "/api/query?player=true&trcolumns=%25artist%25,%25title%25")
            response = conn.getresponse()
            if response.status == 200:
                data = response.read()
                player_state = json.loads(data)
                if 'player' in player_state and 'activeItem' in player_state['player']:
                    artist = player_state['player']['activeItem']['columns'][0]
                    title = player_state['player']['activeItem']['columns'][1]
                    return f"{artist} - {title}"
                else:
                    return "No song is currently playing"
            else:
                return f"Error query current song: {response.status} {response.reason}"
        except Exception as e:
            return f"Error querying current song: {e}"
        finally:
            conn.close()

    def get_current_artwork(self):
        conn = http.client.HTTPConnection(self.base_url)
        try:
            conn.request("GET", "/api/query?player=true&trcolumns=%25artist%25,%25title%25")
            response = conn.getresponse()
            if response.status == 200:
                data = response.read()
                player_state = json.loads(data)
                if 'player' in player_state and 'activeItem' in player_state['player']:
                    playlist_id = player_state['player']['activeItem']['playlistId']
                    index = player_state['player']['activeItem']['index']
                    return f"http://{self.base_url}/api/artwork/{playlist_id}/{index}"
                else:
                    return "Images/app.png"
            else:
                return "Images/app.png"
        except Exception as e:
            return "Images/app.png"
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