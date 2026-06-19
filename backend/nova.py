from modules.speak import speak
from modules.speech import listen
from modules.ai import ask_ai
from modules.data_analysis import analyze_data
from modules.pdf_report import generate_pdf


def main():

    speak("Nova Assistant Started")

    print("=" * 50)
    print("        NOVA AI ASSISTANT")
    print("=" * 50)
    print("Voice Commands:")
    print("- Analyze sales data")
    print("- Analyze student data")
    print("- Analyze employee data")
    print("- Analyze amazon data")
    print("- Generate PDF report")
    print("- Say 'stop' or 'bye' to exit")
    print("=" * 50)

    while True:

        command = listen()

        if not command:
            continue

        command = command.lower().strip()

        print(f"\nYou: {command}")

        # ==================================
        # DATA ANALYSIS
        # ==================================

        if "analyze" in command or "analyse" in command:

            filename = "sales.csv"

            if "student" in command:
                filename = "students.csv"

            elif "employee" in command:
                filename = "employee.csv"

            elif "amazon" in command:
                filename = "amazon.csv"

            elif "sales" in command:
                filename = "sales.csv"

            speak(f"Analyzing {filename}. Please wait.")

            try:

                report = analyze_data(filename)

                print(report)

                speak("Data analysis completed successfully.")

            except Exception as e:

                print("Analysis Error:", e)

                speak("Sorry, I could not analyze the dataset.")

            continue

        # ==================================
        # PDF REPORT
        # ==================================

        if "pdf" in command or "report" in command:

            speak("Generating PDF report.")

            try:

                report = analyze_data("sales.csv")

                pdf = generate_pdf(report)

                print(f"\nPDF Saved Successfully : {pdf}")

                speak("PDF report generated successfully.")

            except Exception as e:

                print("PDF Error:", e)

                speak("Sorry, I could not generate the PDF report.")

            continue

        # ==================================
        # NORMAL AI COMMANDS
        # ==================================

        response = ask_ai(command)

        print(f"Nova: {response}")

        speak(response)

        # ==================================
        # EXIT
        # ==================================

        if (
            "goodbye" in response.lower()
            or "stop" in command
            or "bye" in command
        ):

            speak("Shutting down. Have a nice day.")

            break


if __name__ == "__main__":
    main()