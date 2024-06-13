import tkinter as tk
from tkinter import ttk
from Translatium import Translator

class LanguageTranslatorApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Language Translator")

        # Create translator object
        self.translator = Translator()

        # Input text area
        self.input_label = ttk.Label(root, text="Enter text to translate:")
        self.input_label.grid(row=0, column=0, padx=10, pady=10, sticky="w")
        self.input_text = tk.Text(root, height=5, width=50)
        self.input_text.grid(row=0, column=1, padx=10, pady=10, sticky="ew")

        # Output text area
        self.output_label = ttk.Label(root, text="Translated text:")
        self.output_label.grid(row=1, column=0, padx=10, pady=10, sticky="w")
        self.output_text = tk.Text(root, height=5, width=50, state="disabled")
        self.output_text.grid(row=1, column=1, padx=10, pady=10, sticky="ew")

        # Language selection
        self.from_label = ttk.Label(root, text="From language:")
        self.from_label.grid(row=2, column=0, padx=10, pady=10, sticky="w")
        self.from_language = ttk.Combobox(root, values=self.get_languages(), width=20)
        self.from_language.grid(row=2, column=1, padx=10, pady=10, sticky="ew")
        self.from_language.set("Auto")

        self.to_label = ttk.Label(root, text="To language:")
        self.to_label.grid(row=3, column=0, padx=10, pady=10, sticky="w")
        self.to_language = ttk.Combobox(root, values=self.get_languages(), width=20)
        self.to_language.grid(row=3, column=1, padx=10, pady=10, sticky="ew")
        self.to_language.set("English")

        # Translate button
        self.translate_button = ttk.Button(root, text="Translate", command=self.translate)
        self.translate_button.grid(row=4, column=0, columnspan=2, padx=10, pady=10, sticky="ew")

    def translate(self):
        input_text = self.input_text.get("1.0", "end-1c")
        from_lang = self.from_language.get()
        to_lang = self.to_language.get()

        translation = self.translator.translate(input_text, src=from_lang, dest=to_lang)
        self.output_text.config(state="normal")
        self.output_text.delete("1.0", "end")
        self.output_text.insert("1.0", translation.text)
        self.output_text.config(state="disabled")

    def get_languages(self):
        return [lang.lang for lang in self.translator._validated]

def main():
    root = tk.Tk()
    app = LanguageTranslatorApp(root)
    root.mainloop()

if __name__ == "__main__":
    main()
