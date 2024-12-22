
# LeetCode Conclusions App

![LeetCode Logo](images/leetcodeimage.png)

## Overview

This is a desktop application built with Python and Tkinter that allows users to save and manage their LeetCode problem-solving conclusions. The app provides a searchable combobox for subjects, a text box for entering conclusions, and options to add new subjects.

## Features

- **Searchable Subject Selection**: Choose subjects easily with a searchable combobox.
- **Add New Conclusions**: Save your conclusions for each subject to an Excel file.
- **Edit Subjects**: Add new subjects directly from the app.
- **Customizable Interface**: Simple and clean UI with a LeetCode-inspired design.

## Installation

1. Clone this repository:
   ```bash
   git clone https://github.com/JoelElias96/Leetcode_conclusions
   ```
2. Install required Python packages:
   ```bash
   pip install pandas openpyxl tkinter
   ```
3. Run the app:
   ```bash
   python main.py
   ```

## Usage

- **Add a Conclusion**: Select a subject, write your conclusion, and press the "Add" button.
- **Edit Subjects**: Press the "Edit" button to add a new subject to the list.

## File Structure

- **main.py**: Main script for the Tkinter GUI.
- **searchableCombobox.py**: Contains the `SearchableCombobox` class, enabling the searchable combobox functionality.
- **Documents/conclusionTable.xlsx**: Excel file where conclusions are saved.
- **Documents/subjectsList.txt**: Text file containing the list of subjects.



## Dependencies

- Python 3.x
- Pandas
- Openpyxl
- Tkinter (built into Python)

