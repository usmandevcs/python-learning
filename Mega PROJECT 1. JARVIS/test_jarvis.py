import unittest
from unittest.mock import patch, MagicMock
import sys
import os

# Ensure the parent directory is in the path
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from main import JarvisAssistant

class TestJarvisAssistant(unittest.TestCase):
    
    def setUp(self):
        # Prevent Pyttsx3 from physically talking during setup
        with patch('pyttsx3.init') as mock_init:
            self.assistant = JarvisAssistant()
            self.assistant.engine = MagicMock()
            
        # Mock speak to just print instead of using engine for all tests
        self.patcher_speak = patch.object(self.assistant, 'speak', side_effect=lambda text: print(f"[MOCK SPEAK]: {text}"))
        self.mock_speak = self.patcher_speak.start()

    def tearDown(self):
        self.patcher_speak.stop()

    @patch('webbrowser.open')
    def test_web_commands(self, mock_webopen):
        """Test simple web opening commands"""
        self.assistant.process_command("open google")
        mock_webopen.assert_called_with("http://google.com")
        self.mock_speak.assert_called_with("opening google")

        self.assistant.process_command("open facebook")
        mock_webopen.assert_called_with("http://facebook.com")
        
    @patch('pywhatkit.playonyt')
    @patch('webbrowser.open')
    def test_media_commands(self, mock_webopen, mock_playonyt):
        """Test media playback via youtube and local library fallback"""
        # Test explicit youtube command
        self.assistant.process_command("play python tutorial on youtube")
        mock_playonyt.assert_called_with("python tutorial")
        
        # Test implicit youtube fallback
        self.assistant.process_command("play obscure indie song")
        mock_playonyt.assert_called_with("obscure indie song")

    @patch('wikipedia.summary')
    def test_information_commands(self, mock_wiki_summary):
        """Test Wikipedia searches"""
        mock_wiki_summary.return_value = "Python is a programming language."
        self.assistant.process_command("wikipedia python")
        
        mock_wiki_summary.assert_called_with("python", sentences=2)
        # Should speak the results
        self.mock_speak.assert_called_with("Python is a programming language.")

    @patch('pyjokes.get_joke')
    def test_joke_command(self, mock_joke):
        mock_joke.return_value = "Why did the programmer quit his job? Because he didn't get arrays."
        self.assistant.process_command("joke")
        self.mock_speak.assert_called_with("Why did the programmer quit his job? Because he didn't get arrays.")

    @patch('subprocess.Popen')
    def test_os_launch_commands(self, mock_popen):
        """Test Windows application launching"""
        self.assistant.process_command("open notepad")
        mock_popen.assert_called_with("notepad.exe")

    @patch('pyautogui.press')
    def test_os_control_commands(self, mock_press):
        """Test system volume controls via pyautogui"""
        self.assistant.process_command("volume up")
        mock_press.assert_called_with("volumeup", presses=5)

        self.assistant.process_command("mute")
        mock_press.assert_called_with("volumemute")

    @patch('psutil.sensors_battery')
    def test_system_status(self, mock_battery):
        """Test reading battery status"""
        mock_batt_obj = MagicMock()
        mock_batt_obj.percent = 85
        mock_batt_obj.power_plugged = True
        mock_battery.return_value = mock_batt_obj
        
        self.assistant.process_command("battery")
        self.mock_speak.assert_called_with("Sir, the system is at 85 percent battery and is currently plugged in.")

    def test_unknown_command(self):
        """Test fallback error handling for gibberish"""
        self.assistant.process_command("lkjasbdfkjsabdf")
        self.mock_speak.assert_called_with("I am sorry sir, I did not understand that command.")

if __name__ == '__main__':
    unittest.main()
