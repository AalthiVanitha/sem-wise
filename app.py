from flask import Flask, render_template, jsonify
import pandas as pd

app = Flask(__name__)

EXCEL_FILE = "SEM3 CSE E.xlsx"

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/analyze', methods=['GET'])
def analyze():
    try:
        # Load the Excel file
        df = pd.read_excel(EXCEL_FILE)

        # Ensure 'SGPA' column exists
        if "SGPA" not in df.columns:
            return jsonify({"success": False, "error": "SGPA column not found in Excel"})

        # Count failed students (SGPA = "Promoted")
        failed_students = df[
    (df["SGPA"].astype(str).str.upper() == "PROMOTED--") |
    (df["SGPA"].astype(str).str.upper() == "MALPRACTICE")
    ].shape[0]

        # Calculate passed students as total - failed
        total_students = len(df)
        passed_students = total_students - failed_students

        # Calculate percentages
        pass_percentage = (passed_students / total_students) * 100
        fail_percentage = (failed_students / total_students) * 100

        return jsonify({
            "success": True,
            "total_students": total_students,
            "passed_students": passed_students,
            "failed_students": failed_students,
            "pass_percentage": round(pass_percentage, 2),
            "fail_percentage": round(fail_percentage, 2)
        })

    except Exception as e:
        print(f"Error: {e}")
        return jsonify({"success": False, "error": str(e)})

if __name__ == '__main__':
    app.run(debug=True)
