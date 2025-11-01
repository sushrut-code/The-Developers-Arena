import tkinter as tk
from tkinter import ttk,scrolledtext

BLANKS_TO_FILL = [
    {"label": "Adjective (e.g., small, giant)", "key": "adjective1"},
    {"label": "Singular Noun (e.g., motorcycle, teapot)", "key": "noun1"},
    {"label": "Plural Noun (e.g., aliens, cheeseburgers)", "key": "plural_noun"},
    {"label": "Verb ending in -ING (e.g., dancing, exploding)", "key": "verb_ing"},
    {"label": "Another Singular Noun (e.g., sofa, diamond)", "key": "noun2"},
    {"label": "Exclamation (e.g., Woah, Yikes)", "key": "exclamation"},
    {"label": "Verb in the PAST TENSE (e.g., sang, flew)", "key": "verb_past"},
]

STORY_TEMPLATE = (
    "In a land far away, a **{adjective1}** wizard named "
    "Zorp rode his **{noun1}** every morning. One day, he "
    "saw a group of **{plural_noun}** **{verb_ing}** near "
    "a **{noun2}**. He yelled **'{exclamation}'** and "
    "quickly **{verb_past}** away."
)

input_vars={}

root=tk.Tk()
root.title("MadLib's adventure")
root.geometry("600x600")
root.configure(bg="#f0f0f0")

main_frame=ttk.Frame(root,padding=15)
main_frame.pack(fill="both",expand=True)


title_label = ttk.Label(
    main_frame,
    text="Wizard Zorp's Mad Libs",
    font=('Helvetica', 16, 'bold'),
    foreground="#0056b3" # Dark blue text
)
title_label.pack(pady=(0, 15))

for i, blank in enumerate(BLANKS_TO_FILL):
    key = blank["key"]
    label_text = blank["label"]
    input_vars[key]=tk.StringVar()
    field_frame = ttk.Frame(main_frame)
    field_frame.pack(fill='x', pady=3)
    label = ttk.Label(field_frame, text=f"{i + 1}. {label_text}:", width=35, anchor='w')
    label.pack(side='left', padx=(0, 10))
    entry = ttk.Entry(field_frame, textvariable=input_vars[key])
    entry.pack(side='right', fill='x', expand=True)


# --- 4. The Controller Function ---
def generate_story():
    # 4.1. Collect the user words from the StringVars
    user_words = {}
    for key in input_vars:
        user_words[key] = input_vars[key].get()

    # 4.2. Format the story
    try:
        final_story = STORY_TEMPLATE.format(**user_words)
    except KeyError:
        # Handle cases where a key might be missing (shouldn't happen here)
        final_story = "Error: Please make sure all fields are filled."

    # 4.3. Display the story in the text widget
    story_display.config(state=tk.NORMAL)  # Enable editing for update
    story_display.delete('1.0', tk.END)  # Clear previous text
    story_display.insert(tk.END, final_story)
    story_display.config(state=tk.DISABLED)  # Disable editing

    # Update the title message
    status_label.config(text="Your Adventure is Ready!", foreground="green")



status_label = ttk.Label(main_frame, text="Fill in the words above...", font=('Helvetica', 10), foreground="#555")
status_label.pack(pady=10)


generate_button = ttk.Button(
    main_frame,
    text="Generate Mad Libs Story",
    command=generate_story
)
generate_button.pack(pady=10)


story_display = scrolledtext.ScrolledText(
    main_frame,
    wrap=tk.WORD,
    height=8,
    width=50,
    font=('Times New Roman', 11),
    relief=tk.FLAT  # Gives it a clean look
)
story_display.insert(tk.END, "The final story will appear here after you click the button.")
story_display.config(state=tk.DISABLED)  # Start disabled so the user can't type in it
story_display.pack(pady=10, fill='x', expand=True)


root.mainloop()