import subprocess
import sys
import time
import signal
import os

def main():
    """
    Runs the Django development server and the Tailwind CSS watcher concurrently.
    Terminates both processes gracefully on Ctrl+C.
    """
    django_process = None
    tailwind_process = None

    # --- Windows-Specific Configuration ---
    # Use the CREATE_NEW_PROCESS_GROUP flag to prevent the "Terminate batch job (Y/N)?"
    # prompt on Windows. This gives our script full control over the shutdown process.
    creation_flags = 0
    if sys.platform == "win32":
        creation_flags = subprocess.CREATE_NEW_PROCESS_GROUP

    try:
        # --- Start the Django Development Server ---
        print("--- Starting Django development server on http://0.0.0.0:8000/ ---")
        django_process = subprocess.Popen(
            [sys.executable, "manage.py", "runserver", "0.0.0.0:8000"],
            stdout=sys.stdout,
            stderr=sys.stderr,
            creationflags=creation_flags
        )
        print(f"Django server process started with PID: {django_process.pid}")

        # A small delay to allow the Django server to start up cleanly
        time.sleep(2)

        # --- Start the Tailwind CSS Watcher ---
        print("\n--- Starting Tailwind CSS watcher ---")
        tailwind_process = subprocess.Popen(
            "npm run watch:css",
            shell=True, # Use shell=True for npm commands on some systems
            stdout=sys.stdout,
            stderr=sys.stderr,
            creationflags=creation_flags
        )
        print(f"Tailwind watcher process started with PID: {tailwind_process.pid}")

        print("\n--- Servers are running. Press Ctrl+C to stop. ---")
        # Wait indefinitely until a process exits or Ctrl+C is pressed.
        while True:
            if django_process.poll() is not None or tailwind_process.poll() is not None:
                print("\n--- A server process has stopped unexpectedly. Shutting down. ---")
                break
            time.sleep(0.5)

    except KeyboardInterrupt:
        print("\n--- Ctrl+C detected. Shutting down all processes. ---")

    except FileNotFoundError as e:
        print(f"\n[ERROR] Command not found: {e.filename}")
        print("Please ensure that Node.js and npm are installed and that you are in the correct Django project directory.")

    except Exception as e:
        print(f"\n[ERROR] An unexpected error occurred: {e}")

    finally:
        # --- Gracefully terminate both child processes ---
        print("\n--- Cleaning up... ---")
        if tailwind_process and tailwind_process.poll() is None:
            print("Stopping Tailwind watcher...")
            if sys.platform == "win32":
                # On Windows, CTRL_BREAK_EVENT is sent to the entire process group
                tailwind_process.send_signal(signal.CTRL_BREAK_EVENT)
            else:
                tailwind_process.terminate()
            tailwind_process.wait()
            print("Tailwind watcher stopped.")

        if django_process and django_process.poll() is None:
            print("Stopping Django server...")
            if sys.platform == "win32":
                django_process.send_signal(signal.CTRL_BREAK_EVENT)
            else:
                django_process.terminate()
            django_process.wait()
            print("Django server stopped.")

        print("\n--- All processes terminated. Goodbye! ---")


if __name__ == "__main__":
    main()
